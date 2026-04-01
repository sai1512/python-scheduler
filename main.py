from datetime import datetime
import time
import os

def load_schedule(filename):
    """Read schedule.txt and return a list of tasks.
    Each line format: HH:MM:SS command argument
    Returns a list of dicts: {"time": "09:00:05", "action": "print", "args": "Hello!", "done": False}
    """
    tasks = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                time, action, args = line.split(' ', 2)
                tasks.append({
                    "time": time,
                    "action": action,
                    "args": args,
                    "done": False
                })
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return tasks

# printing the splitted tasks for the above function
tasks = load_schedule('schedule.txt')
for task in tasks:
    print(task)

def execute_action(action, args):
    """Execute a single action.
    Supported commands: print, list_files, create_file
    """
    if action == "print":
        print(args)
    elif action == "list_files":
        files = os.listdir('.')
        print(files)
    elif action == "create_file":
        with open(args, 'w') as f:
            f.write('New file have been created.')
        print(f"File created: {args}")
    else:
        print(f"Unknown action: {action}")


def run_scheduler():
    tasks = load_schedule('schedule.txt')
    if not tasks:
        print("No tasks loaded. Exiting.")
        return
    
    print("Scheduler running... (Ctrl+C to stop)")
    try:
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            for task in tasks:
                if not task["done"] and task["time"] <= now:
                    execute_action(task["action"], task["args"])
                    task["done"] = True
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


run_scheduler()
