import re
import subprocess
import sys
import time
import signal
import tkinter as tk
from tkinter import messagebox
import os
import psutil

monitor_screen_flag = True

def monitor_screen():
    global monitor_screen_flag

    try:
        while monitor_screen_flag:
            try:
                with open("screen.txt", "r") as screen_output:
                    output_lines = screen_output.readlines()
                    for line in output_lines:
                        #print(line.strip())
                        if re.search(r'\b(?:DNS|ConnectionError)\b', line):
                            print("VPN or DNS Error detected. Terminating updater.py and displaying warning dialog...")
                            terminate_updater_process()
                            display_warning_dialog()
                            return
            except Exception as e:
                print(f"Error reading screen.txt: {e}")

            time.sleep(20)
    finally:
        # Exit the script
        sys.exit()

def terminate_updater_process():
    if os.path.exists("updater_pid.txt"):
        with open("updater_pid.txt", "r") as pid_file:
            pid = int(pid_file.read().strip())
            try:
                os.kill(pid, signal.SIGTERM)
                print("Updater.py process terminated successfully.")
            except Exception as e:
                print(f"Error terminating updater.py process: {e}")

def display_warning_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Display a warning message dialog  // this helps detecte connectione errors example due to a firewall
    messagebox.showwarning("VPN or DNS Error", "A VPN or DNS error has been detected. Autie Updater halted. Please take appropriate action (close and restart).")

    root.destroy()  # Destroy the Tkinter window after displaying the dialog

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

    monitor_screen()
