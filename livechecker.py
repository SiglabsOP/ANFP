import ctypes
import psutil
import logging

def check_processes(process_names):
    running_processes = {}
    for process_name in process_names:
        processes = [proc for proc in psutil.process_iter() if proc.name() == process_name]
        if processes:
            running_processes[process_name] = len(processes)
    return running_processes

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    processes_to_check = ["patch.exe", "Autie.exe", "APIaccess.exe"]
    running_processes = check_processes(processes_to_check)
    
    if running_processes:
        message = "Running processes found:\n\n"
        for process_name, count in running_processes.items():
            message += f"{process_name}: {count} instance(s)\n"
    else:
        message = "No running processes found from the list."

    ctypes.windll.user32.MessageBoxW(0, message, "Process Check", 1)
