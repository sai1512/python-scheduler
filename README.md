# Task Scheduler

A Python program that reads scheduled tasks from a file and executes them at the right time.

## File format

Each line in `schedule.txt` follows this format:
```
HH:MM:SS command argument
```

Three supported commands:

| Command | Argument | Example |
|---|---|---|
| `print` | Message to print | `09:00:05 print Good morning!` |
| `list_files` | Directory path | `09:00:10 list_files .` |
| `create_file` | Filename | `09:00:15 create_file log.txt` |

## Sample schedule.txt
```
09:00:05 print Good morning!
09:00:10 create_file log.txt
09:00:15 list_files .
09:00:20 print All done!
```

## How to run

1. Create your `schedule.txt` with tasks set a few seconds from now
2. Run the scheduler:
```
python scheduler.py
```

3. Press `Ctrl+C` to stop

## What to implement

Complete the three functions in `scheduler.py`:

- `load_schedule(filename)` — reads and parses `schedule.txt`, returns a list of task dicts
- `execute_action(action, args)` — executes a single command
- `run_scheduler()` — the main loop that checks the time every second and fires tasks

## Error handling to consider

- What happens if `schedule.txt` doesn't exist?
- What happens if a line is missing the argument?
- What if `list_files` is given a directory that doesn't exist?