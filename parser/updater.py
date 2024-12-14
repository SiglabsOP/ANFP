import os
import shutil
import time
import schedule
import subprocess
import threading
import sys
import requests.exceptions
import urllib3.exceptions
import re
import signal
import psutil

# Start errorhandler.py at the beginning
# subprocess.Popen(["python", "errorhandler.py"])
# subprocess.Popen(["python", "reminders.py"])

# Delete dnserrorsparser.txt if it exists safely
if os.path.exists("dnserrorsparser.txt"):
    os.remove("dnserrorsparser.txt")

# Delete vpnerrors.txt if it exists safely
if os.path.exists("vpnerrors.txt"):
    os.remove("vpnerrors.txt")

# Delete all txt and log files in the current directory
file_extensions_to_delete = ['.txt', '.log']
current_directory = os.getcwd()

for file_name in os.listdir(current_directory):
    if file_name not in ["last_run.txt", "screen.txt"] and any(file_name.endswith(ext) for ext in file_extensions_to_delete):
        os.remove(os.path.join(current_directory, file_name))


def write_pid_to_file():
    pid = os.getpid()  # Get the PID of the current process
    with open("updater_pid.txt", "w") as pid_file:
        pid_file.write(str(pid))  # Write the PID to the file

def display_countdown(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"\rNext iteration in: {minutes:02}:{seconds:02}", end='', flush=True)

def move_binglist():
    print("Executing move_binglist function...")
    write_pid_to_file()

    with open("screen.txt", "w") as f:
        print("Running combined.py to create binglist.txt...")
        subprocess.Popen(["python", "combined.py"], stdout=f, stderr=subprocess.STDOUT)

    while not os.path.exists("binglist.txt"):
        print("Waiting for binglist.txt to be created...")
        time.sleep(1)

    print("binglist.txt created.")

    while True:
        try:
            with open("binglist.txt", "r", encoding="utf-8") as f:
                f.readlines()
            break
        except PermissionError:
            print("Waiting for writing to binglist.txt to finish...")
            time.sleep(1)

    print("No processes writing to binglist.txt.")

    destination_folder = "../"
    shutil.move("binglist.txt", os.path.join(destination_folder, "binglist.txt"))

    print("binglist.txt moved successfully.")

    # Close the screen.txt file after writing
    f.close()

def check_existing_process():
    """Check if another instance of the script is already running."""
    current_pid = os.getpid()
    for process in psutil.process_iter():
        if process.name() == "python.exe" and process.pid != current_pid:
            cmdline = process.cmdline()
            if len(cmdline) > 1 and cmdline[1] == __file__:
                return True
    return False

if __name__ == "__main__":
    # Check for existing process
    if check_existing_process():
        print("Another instance is already running. Exiting...")
        sys.exit()

    move_binglist()

    schedule.every(20).minutes.do(move_binglist)

    def monitor_dns_errors():
        while True:
            time.sleep(60)
            if os.path.exists("dnserrorsparser.txt"):
                with open("dnserrorsparser.txt", "r") as f:
                    if any("DNS Error" in line for line in f):
                        print("DNS Error detected")
                        subprocess.Popen(["startupdater.bat"])
                        sys.exit()
                        break

    dns_error_monitor_thread = threading.Thread(target=monitor_dns_errors)
    dns_error_monitor_thread.start()

    def monitor_vpn():
        while True:
            time.sleep(60)
            if not os.path.exists("screen.txt"):
                with open("screen.txt", "w"):
                    pass
            with open("screen.txt", "r") as screen_output:
                try:
                    output_lines = screen_output.readlines()
                except Exception as e:
                    print(f"Error reading screen.txt: {e}")
                else:
                    for line in output_lines:
                        if re.search(r'\b(?:DNS|ConnectionError)\b', line):
                            error_message = "DNS or Connection Error"
                            print(f"VPN Error: {error_message}")
                            with open("vpnerrors.txt", "a") as f:
                                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} VPN Error: {error_message}\n")
                            subprocess.Popen(["startupdater.bat"])
                            sys.exit()

    vpn_monitor_thread = threading.Thread(target=monitor_vpn)
    vpn_monitor_thread.start()

    while True:
        next_run = schedule.next_run().timestamp() - time.time()
        display_countdown(int(next_run))
        try:
            schedule.run_pending()
        except (requests.exceptions.ConnectionError, requests.exceptions.MaxRetryError, urllib3.exceptions.MaxRetryError) as e:
            with open("dnserrorsparser.txt", "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} DNS Error: {str(e)}\n")
            print(f"\nDNS error detected: {e}. Starting startupdater.bat and shutting down the script.")
            subprocess.Popen(["startupdater.bat"])
            sys.exit()
        time.sleep(1)
