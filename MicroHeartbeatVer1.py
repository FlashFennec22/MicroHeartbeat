import subprocess
import sys
import datetime
import tkinter as tk

from pathlib import Path
home = Path.home()


def ping_host():
    # Determine the appropriate ping command based on the operating system
    if sys.platform.startswith('win'):
        command = ['ping', '-n', '5', '1.1.1.1']
    else:
        command = ['ping', '-c', '5', '1.1.1.1']
    
    # Execute the ping command and capture both stdout and stderr
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode() + result.stderr.decode()
    
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Append the output to a log file in /home/user/
    with open(home / "MicroHeartbeat.log", 'a', encoding='utf-8') as log_file:
        log_file.write(output)
        log_file.write(f"{current_time}\n")
        log_file.write('\n')





    

def toggle_run_stop():
    global is_running
    if not is_running:
        # Start running
        button.config(text="Stop")
        is_running = True
        root.after(10000, execute_script)
    else:
        # Stop running
        button.config(text="Run")
        is_running = False

def execute_script():
    global is_running
    if is_running:
        ping_host()
        print("Running script...")
        # Schedule next execution in 10 seconds
        root.after(10000, execute_script)

root = tk.Tk()
root.title('MicroHeartbeat')
button = tk.Button(text="Run", command=toggle_run_stop, height=25, width=50)
button.pack()

is_running = False

root.mainloop()

    
    
