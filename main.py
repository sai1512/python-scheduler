from datetime import datetime
import time
import os


def load_schedule(filename):
    """Read schedule.txt and return a list of tasks.
    Each line format: HH:MM:SS command argument
    Returns a list of dicts: {"time": "09:00:05", "action": "print", "args": "Hello!", "done": False}
    """
    tasks = []
    # TODO: open the file, skip blank lines
    # split each line into 3 parts: time, action, args
    # append a dict with "time", "action", "args", "done" to tasks
    # handle missing file gracefully
    return tasks


def execute_action(action, args):
    """Execute a single action.
    Supported commands: print, list_files, create_file
    """
    # TODO: handle each command using action and args
    pass


def run_scheduler():
    tasks = load_schedule("schedule.txt")
    if not tasks:
        print("No tasks loaded. Exiting.")
        return

    print("Scheduler running... (Ctrl+C to stop)")
    try:
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            # TODO: loop through tasks, execute if time matches and not done
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


run_scheduler()
