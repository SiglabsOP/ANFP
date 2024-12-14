import os
import subprocess
import time

def start_executables():
    # Get the directory of the script file
    script_dir = os.path.dirname(__file__)

    # List of executables to start in order
    executables = ["Autie.exe", "APIaccess.exe", "patch.exe"]

    for exe in executables:
        # Construct the full path to the executable
        exe_path = os.path.join(script_dir, exe)

        # Check if the executable exists
        if os.path.exists(exe_path):
            # Start the executable using subprocess
            subprocess.Popen(exe_path)
        else:
            print(f"Executable {exe} not found in the directory.")

    # Launch updater.exe from the 'parser' subdirectory after a one-minute delay
      # parser_dir = os.path.join(script_dir, "parser")
       #updater_path = os.path.join(parser_dir, "updater.exe")
       #if os.path.exists(updater_path):
        # Delay for one minute
           #time.sleep(30)
        # Launch updater.exe
           #subprocess.Popen(updater_path)
       #else:
           #print("Updater executable not found in the 'parser' subdirectory.")

if __name__ == "__main__":
    start_executables()