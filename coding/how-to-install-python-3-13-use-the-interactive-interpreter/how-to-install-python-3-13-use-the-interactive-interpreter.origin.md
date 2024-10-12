# How to Install Python 3.13? Use the Interactive Interpreter
![Featued image for: How to Install Python 3.13? Use the Interactive Interpreter](https://cdn.thenewstack.io/media/2024/10/08963947-line-1644072_1280-1024x526.jpg)
With the latest release of [Python (version 3.13)](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/), there are several exciting features, including the new [interactive interpreter](https://docs.python.org/3/tutorial/interpreter.html). This interpreter features multiline editing with history preservation; support for read–eval–print loop (REPL)-specific commands (such as help, exit and quit) without having to call them as functions; prompts and tracebacks (with color enabled); interactive help browsing with a separate command history; history browsing; and paste mode.

Combined, these features make for a considerable leap forward in an interpreter that hasn’t seen a lot of new features appear in the recent past. For anyone who uses the [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) interactive interpreter, this should be an early Christmas.

This interactive interpreter is based on code from the [PyPy](https://pypy.org/) project and can be disabled by setting the PYTHONG_BASIC_REPL environment variable. The new interactive shell is available to [UNIX](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/)-like systems (such as [Linux](https://thenewstack.io/learning-linux-start-here/)) with curses support and Windows. By default, the interpreter uses color for things like prompts and tracebacks. It’s possible to disable the color option by setting the TERM variable to *dumb*.

Let’s look at how the new interpreter works.

## Easier Exit
If you’ve used the Python interpreter, then you know exiting it requires the Ctrl+D keyboard shortcut.

Or at least it used to.

Now, the interpreter exit makes sense because all you have to do is type “exit.” As someone who’s been using the Linux terminal for decades, this is a welcome change. It never fails that when I’m finished using the interpreter, I type exit, only to be presented with an error.

Until Python 3.13, it was full-on [Jean-Paul Sartre and no ](https://en.wikipedia.org/wiki/No_Exit)exit.

In the same vein, you can also now clear the interpreter screen with the *clear *command, which is very helpful when you need to start over and want a clean space to use.

## Improved Error Messages
Confession time: When I first started learning Python, I had no idea that you had to be careful with file names. For example, I’d be creating an app that uses the random library module and name the file random.py. I’d then try to run the code, only to receive a rather cryptic message that gives me no indication about what was wrong.

Little did I know that the problem was the file name. Eventually I figured that out, changed the file name and re-ran the app without problems. Clearly, the error was not in the code itself.

With the new interpreter, those error messages are far less cryptic. For example, you might see something like this in the error message:

1 |
(consider renaming '/home/jack/PYTHON/random.py' since it has the same name as the standard library module named 'random' and the import system gives it precedence) |
That certainly would have been nice back when I was taking my first steps with Python. I’d have saved a lot of time troubleshooting silly issues such as a file name conflict.
Speaking of error messages…

## Color, Color Everywhere
Okay, the new Python interpreter doesn’t spill color over everything. What you’ll find is that color is enabled (by default) for prompts and tracebacks. What does this mean? It means you’ll be able to spot problems a lot easier from within output of the interpreter.

Let’s take our improved error messages feature for a ride. We’ll stick with our numpy.py example. If I attempt to run that app, I know I’ll get error messages because of the file name. However, with Python 3.13, those errors are colored for easier reading.

**Figure 1**
![](https://cdn.thenewstack.io/media/2024/10/78d64b40-python313.jpg)
Error messages are not only smarter; they’re easier to read in Python 3.13.

## Executable Scripts
Another cool feature is the ability to make a Python script executable on Linux, without having to run it with python3. To do this, you must add the following line to the top of your code:

1 |
#!/usr/bin/env python3 |
Save and close the file. Next, give the file executable permission with:
1 |
chmod u+x name.py |
Where name is the name of your script.
Now, to run your Python script, all you have to do is issue the command:

1 |
./name.py |
Where name is the name of your script.
## Getting Python 3.13 on Ubuntu
If you attempt to install Python 3.13 from the standard repositories, you won’t have much luck. However, there is a repository you can use (if you can’t wait for your distribution of choice to add the latest version to the standard repos). Let me show you how to take care of this.

First, open a terminal window and install the solo dependency with:

1 |
sudo apt-get install software-properties-common -y |
Once that’s taken care of, add the required repository with:
1 |
sudo add-apt-repository ppa:deadsnakes/ppa |
When prompted, hit “Enter” on your keyboard.
After the repository has been added, you can then install Python 3.13 with the command:

1 |
sudo apt-get install python3.13 -y |
You’re not out of the woods yet. At the moment, your system is probably still defaulting to Python 3.10, so you have to configure it to use 3.13. To do that, we’ll add both 3.10 and 3.13 as alternatives. First add 3.10 with:
1 |
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1 |
Next, add 3.13 with:
1 |
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.13 2 |
Finally, configure the default with:
1 |
sudo update-alternatives --config python |
When prompted, select 2 and Python 3.13 is set. If you issue the command *python -v*, you should see that 3.13 is now the default.
To find out more about what’s been added to Python 3.13, make sure to check out the [official release announcement](https://docs.python.org/3.13/whatsnew/3.13.html).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)