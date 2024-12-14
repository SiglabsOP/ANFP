import subprocess
import time
import os
import datetime

def run_and_wait(executable_path, log_file):
    try:
        subprocess.run(executable_path, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        error_message = f"Error running {executable_path}: {e}"
        print(error_message)
        log_error(log_file, error_message)

def log_error(log_file, error_message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as log:
        log.write(f"{timestamp}: {error_message}\n")

# Replace 'X.exe' and 'cleaner.exe' with the actual paths or names of your executables THIS ONE DOES THE ACTUAL CLEANING AND POSTING! its the HUB!
executable_paths = ['X.exe', 'cleaner.exe']
log_file = 'apiaccesserrors.log'

while True:
    for executable_path in executable_paths:
        if os.path.exists(executable_path):
            run_and_wait(executable_path, log_file)
        else:
            error_message = f"Executable not found: {executable_path}"
            print(error_message)
            log_error(log_file, error_message)

    time.sleep(600)  # 300 seconds = 5 minutes U CAN SET THIS LOWER TO TWEET LONGER OR MANUAL RESTART TO TEST FASTER
