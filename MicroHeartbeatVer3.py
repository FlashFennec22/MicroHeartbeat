import subprocess
import sys
import re
import datetime
import tkinter as tk
from pathlib import Path

home = Path.home()

def ping_host():
    if sys.platform.startswith('win'):
        command = ['ping', '-n', '5', '1.1.1.1']
    else:
        command = ['ping', '-c', '5', '1.1.1.1']
    
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(home / "MicroHeartbeat.log", 'a', encoding='utf-8') as log_file:
        log_file.write(output)
        log_file.write(f"{current_time}\n")
        log_file.write('\n')

def count_non_zero_lost():
    pattern = r'Lost = (-?\d+)'
    count = 0
    
    try:
        with open(home / "MicroHeartbeat.log", 'r', encoding='utf-8') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    value = int(match.group(1))
                    if value != 0:
                        count += 1
        
        with open(home / "Packetloss.log", 'a', encoding='utf-8') as log_file:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"[{current_time}] Packet loss incidents detected: {count}\n")
    except FileNotFoundError:
        pass  # Log file doesn't exist yet

def toggle_run_stop():
    global is_running
    if not is_running:
        button.config(text="Stop")
        is_running = True
        root.after(10000, execute_script)
    else:
        button.config(text="Run")
        is_running = False

def execute_script():
    if is_running:
        ping_host()
        count_non_zero_lost()
        root.after(10000, execute_script)

# Initialize GUI
root = tk.Tk()
root.title("MicroHeartbeat")
button = tk.Button(root, text="Start", command=toggle_run_stop, height=25, width=50) 
button.pack()

is_running = False

root.mainloop()

    
    
