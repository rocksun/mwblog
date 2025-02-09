# Prepare Your Mac for Python Development
![Featued image for: Prepare Your Mac for Python Development](https://cdn.thenewstack.io/media/2024/09/8a15b6c4-python-1024x683.png)
I dabble in the world of [Python](https://thenewstack.io/what-is-python/) development for fun, and recently, I decided to get a bit more serious with a dedicated environment. While I considered a new [Raspberry Pi 5](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/) (and may still get one!), I decided to keep things local with a dedicated Parallels virtual machine on my MacBook Pro. Mac VM images are available through Parallels, so the installation was a breeze.

The rest of this article covers my next steps and should help anyone curious about setting up a useful but straightforward [Python3 dev environment](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) on macOS. Keep in mind that some of the software choices are based on my own preferences. Feel free to make your own selections. My deep preference for [Vim](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) is probably the most controversial choice.

## MacOS and Python
I’ll provide specific commands where I can and suggestions otherwise. Admittedly, a few of these topics are basic common sense and best practice (such as managing software updates).

### Set Up My Mac
Take a few minutes to customize macOS the way you like it. Creating an efficient and comfortable user interface is essential to setting up an environment that works with you, not against you.

Here are some common settings:

- Clean up the Dock by removing the (many) apps Apple adds by default. Reduce the Dock to just the apps you use frequently. Add the programs you install later in this list for easy access.
- Set some inspirational wallpaper. I used the Python icon for motivation.
- Configure at least two
[Spaces](https://support.apple.com/guide/mac-help/work-in-multiple-spaces-mh14112/mac). If you’ve never used Spaces, this is one of the most helpful macOS efficiency tools. Spaces are virtual desktops that exist offscreen. You can switch between them quickly, leaving specific applications open on each. I use four Spaces on my Macs. - Adjust the display settings, font sizes and other visual settings to your preferences.
- Set trackpad and keyboard settings to your taste. There are several efficiency options around these two devices, so be sure to research those. I use multiple monitors at high resolutions, so I bump up the size of the pointer to make it easier to find on such a broad visual area.
I prefer Chrome over Safari, so I also switch browsers at this point.

I use cloud storage for most of my business documents, but I also run regular Time Machine backups. Set up a backup routine for your work.

Finally, I update macOS and any applications currently installed to ensure I have the latest features and security updates. Be sure to do this regularly!

You should have your own macOS preferences, but perhaps these ideas will give you new ideas.

### Install Parallels Tools
My macOS/Python platform is a virtual machine. I use [Parallels](https://www.parallels.com/) to host the various Linux and macOS VMs I use for my business. You could choose another virtualization platform, manage your Python projects on a physical Mac or use a non-Apple platform like Linux.

Once I create my macOS/Python VM, I add Parallels Tools to ensure efficient communication. This doesn’t need to be a very powerful VM, as most Python applications are fairly small, especially when first starting out.

### Install Homebrew
Few general utilities will be as helpful as the Homebrew package manager. Linux users will already be familiar with package managers like [DNF and APT](https://thenewstack.io/how-to-manage-linux-software/), but if you’re new to this software management approach, get ready to be impressed. Package managers give you the ability to install applications quickly and easily. Homebrew also lets you install software that is not available on Apple’s App Store. Not all developers want to bend to Apple’s strict requirements, and not all software is ready for the App Store.

Install [Homebrew](https://thenewstack.io/homebrew-for-macos-developers/) by typing the following command in the Terminal:

1 |
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" |
### Hot-Rod the Terminal
You’ll likely spend a lot of time at the command prompt while developing programs. While GUI tools are wonderful, sometimes the CLI is the better choice. Apple’s built-in Terminal application is tolerable, but there are other options. My favorite is [iTerm2](https://iterm2.com/). This highly customizable Terminal replacement offers many practical features — far too many to list here.

Take a look at these standout options to get you started with iTerm2:

- Split pane views.
- Extensive search capabilities.
- Autocomplete options.
- Customizable profiles for various projects. (Imagine a profile for Python development and another for file management tasks.)
For extra credit, consider enhancing iTerm2 with the [Oh-My-Zsh](https://ohmyz.sh/) framework to customize your shell environment further.

### Update Python3
The latest macOS (Sequoia) includes Python 3.9.6. However, you really should update your Python version to the latest version to address bug fixes in the older Apple version. Open the Terminal and type python3 to see the current version. It’s probably Python3 3.9.6 — woefully out of date compared to the 3.13.1 version that was current at the time I wrote this piece.

![](https://cdn.thenewstack.io/media/2025/02/9fdd54fb-python-3-9-6old.png)
Homebrew maintains extensive package support for Python3, Python modules, the PIP package manager and other necessary components, so I use it to update my Python.

Here are the basic Homebrew commands:

123 |
brew updatebrew install python3brew link python3 |
These commands should automatically add the
/opt/homebrew/bin/ PATH variable to the
.zshrc file, but you’ll need to run the
source command (or log out and back in) to update the session.
If you type python3 now, you should see the updated version.

![](https://cdn.thenewstack.io/media/2025/02/d7023a84-python-3-13-1new.png)
Consider running brew upgrade python3 periodically to maintain current versions.

### Spend Time IDLE-ing
You should already have access to the default Python3 editor, IDLE. You can access it from the Terminal or the Launchpad.

IDLE is a good basic editor, and it’s nice that Python3 includes it. However, I’m looking for something more robust.

### Install PyCharm Community Edition
I have nothing against the IDLE IDE, but I want to work with Python using [PyCharm Community Edition](https://www.jetbrains.com/pycharm/) from JetBrains. [Download the .dmg file](https://www.jetbrains.com/pycharm/download/?section=mac) (scroll to the bottom of the page for the Community Edition) and drag the PyCharm CE icon into the macOS Applications folder. That’s it — a typical easy Mac program install.

Customize the PyCharm CE user interface theme to taste and add any plug-ins you prefer. PyCharm also supports various other languages and includes a new AI support feature to explore. For those new to Python and PyCharm, the IDE contains a 40-lesson set of tutorials to get you started!

![](https://cdn.thenewstack.io/media/2025/02/d7f3000a-pycharmce.png)
### Install and Customize Vim
It may seem archaic, but I’m a big fan of the [Vim text editor](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/). There’s nothing quite like a basic text editor for getting things done without the distraction of wacky icons and 10,000 specialized features. As an author, I frequently just need to get words on paper (or screen, in this case), and Vim serves that purpose magnificently.

Coding is a great example. Vim offers Python3 syntax highlighting, auto-indention and code folding to simplify your coding experience. To load these options automatically when Vim launches, I edit the
~/.vimrc file and add the following (use
" for comment lines):

1234567891011 |
" Syntax checkingsyntax on" Line numberingset number " Highlight cursor lineset cursorline" Indentionsfiletype indent on" Foldingset foldmethod=indentset foldlevel=99 |
![](https://cdn.thenewstack.io/media/2025/02/afc63837-vimrc.png)
Many other useful settings exist, but these are a good start for me. Many folks have placed their highly customized .vimrc configuration files online for reference. Some of these profiles are specifically tuned for Python development.

![](https://cdn.thenewstack.io/media/2025/02/e64f6c25-pythonvim.png)
Many Python-specific Vim plug-ins exist to further extend Vim’s capabilities as an IDE. Consider a plug-in manager if you decide to go down this rabbit hole.

### Add the CotEditor
My latest favorite macOS application is [CotEditor](https://coteditor.com/). I needed a basic GUI text editor to replace VS Code. I wanted something simple, graphical and (if possible) open source. And I found CotEditor. So far, this tool has been wonderful, and exactly what I need. You may or may not use it directly for coding, but it’s great for Markdown documentation or other basic editing projects.

![](https://cdn.thenewstack.io/media/2025/02/b610da62-coteditor.png)
### Set Up venv for Python3 Projects
[Python virtual environments](https://docs.python.org/3/library/venv.html) help avoid dependency hell. Your various projects may require different modules or even different Python versions. Managing these rigid requirements systemwide would be challenging, so Python uses [virtual environments](https://thenewstack.io/why-every-python-dev-needs-virtual-environments-now/) (venv). Modules and other components installed in a venv are limited by its boundaries and do not affect other venvs. I typically create a new venv for each Python project. You will activate and deactivate the virtual environments as you change from project to project.
The basic process to create and activate a venv for a project named “new-app” is:

1234 |
mkdir new-appcd new-apppython3 -m venv .venvsource venv/bin/activate |
The best practice is to name virtual environments “venv”, “env” or “.venv”.
## Wrap Up
You’re now ready to begin constructing Python projects on your Mac! As noted in the beginning, some of these tools and preferences are my own choices, so simply select the ones you like or are curious about and ignore the others.

Macs make great dev platforms, and using a virtual machine is a handy way of experimenting with different tools and options. Get yourself rolling with macOS and Python today!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)