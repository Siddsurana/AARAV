import os
import psutil  

import psutil
import pygetwindow as gw

def save_windows_info():
    windows_info = {}

    # Get a list of all running processes
    running_processes = {proc.pid: proc.info for proc in psutil.process_iter(['pid', 'name'])}

    # Get information about all open windows
    for window in gw.getAllWindows():
        # Filter out windows without title
        if window.title:
            for pid, proc_info in running_processes.items():
                try:
                    if window.title in proc_info['name']:
                        windows_info[window.title] = {'pid': pid, 'process_name': proc_info['name']}
                        break  # Stop searching for this window's process
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue

    # Save the window information to a file
    with open('windows_info.txt', 'w') as file:
        for title, info in windows_info.items():
            file.write(f"{title}: {info}\n")





def open_saved_windows():
    # Read the saved window information from the file or database
    with open('windows_info.txt', 'r') as file:
        windows_info = {}
        for line in file:
            key, value = line.strip().split(': ')
            windows_info[key] = int(value)
    
    # Open the windows based on the saved information
    for name, pid in windows_info.items():
        os.system(f"start /b taskkill /PID {pid} /F")  # Close existing instance if any
        os.system(f"start {name}")

# Save the information about currently open windows
save_windows_info()

# Later, when you want to reopen the windows
str = int(input("saojfbaoba"))
if str == 1:
    open_saved_windows()

