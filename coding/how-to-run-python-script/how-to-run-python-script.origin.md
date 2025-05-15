# How To Run a Python Script on MacOS, Windows, and Linux
![Featued image for: How To Run a Python Script on MacOS, Windows, and Linux](https://cdn.thenewstack.io/media/2025/04/2b530c1e-how-to-run-python-script-1024x683.jpg)
Stop copy‑pasting the same command every time you run Python. This guide will teach the practical ways to run Python scripts no matter which operating system, editor, or automatic scheduler you use.

## What Is a “Python script”?
It’s any plain text file with Python code inside, typically saved with the`.py`
extension.

For this tutorial, we’re going to use a password generator script. This script also includes the Python module `random`
. A Python module is a file containing Python code (functions, classes, variables) that can be imported and reused in other Python programs. A Python module is meant to be imported and reused, while a script is intended to be executed directly to perform a specific task.

## Run the Script From the Command Line
### MacOS and Linux
Open Terminal and type the following command to run the password generator script:

If you want to make it executable and run it like an app, follow these steps:

- Add a shebang at the top of your code. The shebang tells the OS to use the Python interpreter (Python 3 in this case) so you don’t need to type
`python3`
every time. Your code will now start like this:
- Grant execution permission:
2. Run the script directly:

### Windows 10/11
Python installs with a launcher called `py`
. Use it to run your script:

Alternatively, if Python is set in your PATH, you can run the following:

If you get errors like `'python' is not recognized`
, rerun the installer and check “Add Python to PATH,” or just use the `py`
launcher.

## Passing Command-Line Arguments
Passing command-line arguments lets users provide input without changing the original code. It promotes a few Pythonic principles by making your script more flexible and modular. Passing in command-line arguments allows one script to handle different tasks or settings efficiently.

You’ll need to update the original password generator code file to include the argparse module. In addition to importing `argparse`
, we are going to add a function to parse input and pass the `length`
argument into` generate_password()`
in the `__main__`
block.

If you’re running the script on macOS or Linux, you’ll also need to add a shebang (e.g., `#!/usr/bin/env python3`
) to the top of your file. This line tells the operating system what interpreter to use when executing the script directly.

Now we’re ready to go!

### MacOS / Linux
- Make the script executable:
2. Run it with the argument:

### Windows
Windows doesn’t use the shebang (`#!/usr/bin/env python3`
) like Unix systems do. But you can still run the script from Command Prompt or PowerShell using `python`
or `python3`
.

Open Command Prompt (or PowerShell):

Press `Win + R`
, type `cmd`
or `powershell`
, and hit Enter.

- Navigate to the correct folder
2. Run the script now with a custom length:

## Run a Python Script in an IDE
Running a script in an IDE gives you helpful tools like autocompletion, debugging, and visual feedback. It’s great for development. It’s a more comprehensive option than using the command line, especially for more complex projects.

### Running Python in PyCharm
PyCharm is a powerful Python IDE with smart editing, debugging, and project tools that streamline development. It excels at code completion, debugging, and integration with version control and virtual environments.

- Open PyCharm and create or open a project.
- Open password_generator.py in the editor.
- Click the green ▶ Run button (or press Shift + F10).
- PyCharm remembers the run configuration, so next time you can run it with one click.
### Visual Studio Code
VS Code is faster, lighter, and more flexible than PyCharm — perfect for multilanguage projects and custom setups.

- Install the Python extension if needed.
- Click the interpreter name (bottom left) and select your Python version.
- Hit F5 or click ▶ Run Python File at the top of the file.
### Jupyter Notebook/JupyterLab
Jupyter Notebook isn’t a traditional IDE like VS Code or PyCharm. It stands out for interactive, cell-based execution and real-time visualization, all in one document. Jupyter is great for data analysis but also runs regular Python scripts.

Jupyter Notebooks are my preferred way to build tutorials. I use VS Code when I build applications.

There are many ways to run Python in Jupyter, but here’s one example. This example focuses on building and running the code inside the Jupyter notebook. It doesn’t use any files that are saved elsewhere.

We’ll need to adjust our `password_generator.py`
code before it works in Jupyter.

After clicking the run button ( ▶ in the upper left), the script will ask for a password length. Enter the number, press enter, and it will generate your password.

## Schedule and run scripts automatically
### MacOS and Linux: `cron`
`cron`
is great for recurring tasks and for running scripts at specific times.
- Open crontab:
2. Add a line to run your script daily at 3:00 AM:

`cron`
will now run this script on its specified schedule.
You can log the output with the following code:

### Windows: Task Scheduler
- Open Task Scheduler from the Start menu.
- Click Create Task… (avoid Basic Task—it’s limited).
- On the General tab: name the task and choose “Run whether user is logged on or not.”
- On the Triggers tab: click New… to set a schedule.
- On the Actions tab:
- Program/script: Path to
`python.exe`
(e.g.,`C:\Users\you\venv\Scripts\python.exe`
) - Add arguments: Path to your script (e.g.,
`C:\Projects\password_generator.py`
)
- Program/script: Path to
- Click OK and enter your Windows password.
### Linux servers: `systemd`
timers
`systemd`
is a modern alternative to `cron`
that ensures scripts run even after reboots. The following runs the script daily at 3 a.m.
Create a new timer file:

Enable:

## Quick Troubleshooting
Errors are part of the process. If you run into errors while executing your Python script, here are some quick troubleshooting tips to help you get back on track.

ModuleNotFoundError

Make sure your virtual environment is activated:

- Unix:
`source venv/bin/activate`
- Windows:
`.\venv\Scripts\activate`
Permission denied (Unix)

Make the script executable with `chmod +x script.py`
, or run with `python3 script.py`
.

PATH confusion

Use absolute paths (`/usr/bin/python3`
, `C:\Projects\password_generator.py`
) to avoid environment issues.

## Best Practices Once You’re Comfortable
Here are some best practice tips you can implement once you’re running scripts smoothly.

Isolate dependencies using a virtual environment.

Freeze dependencies to lock in versions.

Avoid unintended execution when importing by guarding the entry point.

Bundle scripts with PyInstaller for systems without Python.

## Conclusion
Now that you know how to run Python scripts across macOS, Windows, and Linux, you’ve got everything you need to take your ideas from concept to execution no matter the platform.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)