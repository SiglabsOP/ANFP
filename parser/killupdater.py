import psutil
import ctypes

def check_and_kill_updater():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'python.exe':
            cmdline = proc.cmdline()
            if len(cmdline) > 1 and "updater.py" in cmdline[1]:
                print("Updater.py is running with PID:", proc.pid)
                print("Terminating it...")
                proc.terminate()
                if proc.is_running():
                    print("Updater.py did not terminate gracefully. Killing it...")
                    try:
                        proc.kill()
                    except psutil.NoSuchProcess:
                        pass
                else:
                    print("Updater.py terminated successfully.")
                return True
    return False

def display_message_box(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Updater Report", 0x40)  # 0x40 is MB_TOPMOST flag

if __name__ == "__main__":
    if check_and_kill_updater():
        display_message_box("Updater.py was running and has been killed.")
    else:
        display_message_box("Updater.py was not running.")
