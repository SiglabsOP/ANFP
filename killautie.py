import psutil
import time
import logging

def kill_processes(process_names, max_attempts=3, attempt_interval=5):
    for attempt in range(1, max_attempts + 1):
        logging.info(f"Attempt {attempt}/{max_attempts} to kill processes...")
        for process_name in process_names:
            processes = [proc for proc in psutil.process_iter() if proc.name() == process_name]
            for proc in processes:
                try:
                    proc.kill()
                    logging.info(f"Killed process: {proc.name()}")
                except psutil.NoSuchProcess:
                    logging.warning(f"Process {proc.name()} not found.")
                except psutil.AccessDenied:
                    logging.warning(f"Access denied for process {proc.name()}.")
                except psutil.ZombieProcess:
                    logging.warning(f"Zombie process {proc.name()} cannot be killed.")
                except Exception as e:
                    logging.exception(f"Error occurred while killing process {proc.name()}: {e}")
        time.sleep(attempt_interval)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    processes_to_kill = ["patch.exe", "Autie.exe", "APIaccess.exe", "updater.exe", "cleanerbuggy.exe"]   
    kill_processes(processes_to_kill)
