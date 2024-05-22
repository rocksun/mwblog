# How To Use VS Code for Python (and Why You Should)
![Featued image for: How To Use VS Code for Python (and Why You Should)](https://cdn.thenewstack.io/media/2024/05/d5db76ac-getty-images-glhpcnwhrmm-unsplash-1-1024x683.jpg)
Since I started my journey with
[Python](https://thenewstack.io/guido-van-rossums-ambitious-plans-for-improving-python-performance/), I’ve been working with nothing more than a [Linux OS](https://thenewstack.io/a-guide-to-linux-operating-systems-for-kubernetes/) and a [terminal window](https://thenewstack.io/off-the-shelf-hacker-embrace-the-linux-command-line/). Nano has been my editor of choice and it’s been fairly easy going. But there was always something bothering me: Nearly every developer I know uses an integrated development environment (IDE) to code. That always surprised me because, when I was studying [C++](https://thenewstack.io/c-on-the-move/) in school way back when, I used that same combination of tools, partly because I couldn’t afford the software the instructor suggested. On top of that, I didn’t have a machine running Windows, and [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) didn’t offer a version of their IDE for Linux.
That was a long time ago and things have changed considerably. I’m no longer constrained to the terminal window because there are plenty of GUI tools available for Linux, and some were created and distributed by Microsoft.
One of those tools is
[Visual Studio Code](https://thenewstack.io/how-to-use-vs-code-as-your-python-ide/), which also happens to be one of the more popular IDEs on the market. In fact, VS Code comes in second on [PYPL’s Top IDE Index](https://pypl.github.io/IDE.html) behind Visual Studio, and has a 13.51% market share.
So I decided to give VS Code a try with Python and quickly discovered that it was a fantastic move.
But why? When a terminal window and nano were getting me by just fine, why would I bother with a more complicated GUI? Let me first talk about the why and then we’ll deal with the how.
## Why You Should Use VS Code for Python
Essentially, it all boils down to features. Writing Python within the Linux terminal window (using nano) doesn’t really offer much. Sure, you do get syntax highlighting (so you can tell when you’ve left out a ” a ‘ or a ), but that’s about it. You don’t get automatic indentation and other helpful features found in an IDE.
Another big plus of using VS Code is the wealth of extensions available for Python. You’ll find extensions for debugging, indentation, environments, previews,
[Django](https://thenewstack.io/what-is-pythons-django/), [Intellicode](https://thenewstack.io/top-5-code-completion-services/) (AI assistance), docstring generation, [Jupyter Notebook](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) support and much more. To access all of these features from the command line would require considerable work.
The truth of the matter is, you really won’t need any of these features until you’ve gone beyond the very basics of learning Python. At first, I would highly recommend sticking with a text-based editor and the Python interpreter. Because you’re dealing with rudimentary code, there’s no need for all the bells and whistles offered by VS Code.
However, as you gain more experience with Python, you might want to migrate to an IDE like VS Code.
With that in mind, let me show you how to get started with VS Code and Python.
## What You’ll Need
I’m going to demonstrate this on Pop!_OS Linux, but you can install VS Code on macOS or Windows as well. For those two operating systems, the installation is as simple as downloading the installer file, double-clicking it and walking through the installation wizard.
For Linux, the process is a bit more challenging. Although you can download an installer file for APT and DNF package managers, you don’t receive automatic updates unless you download the latest version when it’s released and then reinstall.
With that in mind, let’s install VS Code on both
[Ubuntu](https://thenewstack.io/enable-automatic-updates-for-ubuntu-server/) and Fedora-based distributions.
## Installing VS Code on a Ubuntu-Based Distribution
The first thing to do is to make sure that wget and gpg are installed on your machine. For that, issue the command:
|
1
|
sudo apt-get install wget gpg -y
Next, we download the official Microsoft GPG key:
|
1
|
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
We can now install the key with this command:
|
1
|
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
Create a new apt repository entry:
|
1
|
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
Install the necessary dependencies with this command:
|
1
|
sudo apt install apt-transport-https -y
Update apt:
|
1
|
sudo apt update
Finally, install VS Code with the command:
|
1
|
sudo apt install code -y
## Install VS Code on a Fedora-Based Machine
First, install the required key:
|
1
|
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
Create the dnf repository entry:
|
1
|
echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null
Update dnf with this command:
|
1
|
dnf check-update
Install VS Code:
|
1
|
sudo dnf install code -y
Once you have VS Code installed, open it from your desktop menu and walk through the user-friendly onboarding wizard.
## Enable Python Support
The next thing to do is enable Python support. For that, click the Extensions icon in the sidebar (which looks like the small Tetris-y icon, and can be found near the middle of the bar). In the resulting menu, type
python and wait for the results. Click the Install button associated with the official Python extension. It should be the top result (refer to the image below).
![](https://cdn.thenewstack.io/media/2024/05/4323e724-vscode1.jpg)
Installing Python support in VS Code.
Once the extension is installed, you can then scroll through the remaining results and install any other Python-related extensions you might want. With that taken care of, you can then open a folder on your machine (select File > Open Folder) that contains your existing Python code. Your files will be listed in the left sidebar. Open one of your files and and continue working with it. For example, I’ll open a file from my Typecasting tutorial. The code appears in the editor. I can then click the Run button (a right-pointing arrow found near the top-right of the window). A pane will open below the editor, and the code will run.
One additional bonus that I didn’t mention earlier is that VS Code provides quick access to all of the files found in your selected folder. You won’t have to remember the name of what you’ve created and open it manually. That’s a small addition that can make a big difference in efficiency.
If you’re starting to get the hang of Python, I’d highly recommend that you add an IDE like VS Code into the mix. You’ll enjoy the added power and efficiency.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)