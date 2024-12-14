import subprocess
import time
import os
import datetime

def run_and_wait(script_path, log_file):
    try:
        subprocess.run(['python', script_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        error_message = f"Error running {script_path}: {e}"
        print(error_message)
        log_error(log_file, error_message)

def log_error(log_file, error_message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as log:
        log.write(f"{timestamp}: {error_message}\n")

# Replace 'Sort.py' with the actual name of your Python script // change the paths as needed 
script_path = r'C:\VermeerSuite 10-1\VermeerSuite Development\cloud development\Autie\Sort.py'
log_file = 'apiaccesserrors.log'

while True:
    if os.path.exists(script_path):
        run_and_wait(script_path, log_file)
    else:
        error_message = f"Script not found: {script_path}"
        print(error_message)
        log_error(log_file, error_message)

    time.sleep(4)  # 240 seconds = 4 minutes NEEDS TO BE LOW
