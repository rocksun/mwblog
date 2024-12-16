# Homebrew for MacOS Developers
![Featued image for: Homebrew for MacOS Developers](https://cdn.thenewstack.io/media/2024/12/9be3eb5f-homebrew-1024x683.png)
Few things are as easy to install as a new Mac application when using the GUI. However, not all software comes nicely bundled or relies on the graphical environment. In addition, some users may want to customize the installation of specific software. The Homebrew package manager for macOS fulfills this role nicely.

This article explains the use of package managers from a developer’s perspective, demonstrates the installation and basic use of Homebrew and discusses its features.

## What Is a Package Manager?
Package managers help users and administrators [maintain software](https://thenewstack.io/an-introduction-to-the-snap-universal-package-manager/). They install, remove, update and report on software packages on the system. Most package managers are used from the command line, although some also have graphical interfaces.

Homebrew is the de facto standard package manager for macOS. Where Linux users are familiar with DNF or [APT](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/) and Windows users have MSI or Chocolately, macOS users rely on [Homebrew](https://docs.brew.sh/).

Package managers have different features, but they generally keep track of what software is installed and provide an interface for managing that software and its dependencies. Maintaining software using a package manager offers many advantages, some of which I note below:

- Easy to add, remove and update applications.
- Easy to distribute applications you’ve written.
- Scriptable for automation.
- May handle software dependencies, making installation easier.
- Streamline system management.
- Provide access to nonstandard or unreleased tools.
Homebrew is a crucial tool for developers coding on a Mac.

## Install Homebrew on Your Mac
Homebrew itself is easy to install. The homepage provides the necessary
curl command to pull Homebrew to your Mac Intel or Silicon system. You can also install Homebrew from [GitHub](https://github.com/Homebrew/brew).

Paste the following
curl command into your shell to install Homebrew:

1 |
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" |
The installation script clearly explains the procedure so you can confirm the installation. Once installed, type
brew -v to see version information.
![](https://cdn.thenewstack.io/media/2024/12/364d65e8-brewversion.png)
If you installed Homebrew a while ago and are just getting around to exploring it, bring it to the latest version by typing brew update.

That’s it! You’ve just added a powerful new application to your Mac. It’s time to start using it.

### Homebrew Terminology
Homebrew uses its own terminology, including a few basic concepts you should be familiar with. These include:

- Cask: Package definition that installs GUI macOS native applications.
- Formula: Package definition that installs CLI applications built from source code.
- Keg: Destination installation directory.
- Tap: Directory or Git repository of formulae or casks.
You’ll quickly become familiar with this terminology as you work with Homebrew.

## Manage Software
Managing the dev tools and other software on your Mac means installing, updating and removing applications — exactly what Homebrew excels at doing. Homebrew’s syntax combines the primary brew command with secondary subcommands and options to act on the specified argument (usually the software package).

Syntax: brew subcommand -options argument

Syntax example: brew info iterm2

I cover several practical examples below.

### Basic Package Management
Obviously, the key task is deploying software. The install subcommand handles this.

If you’re a fan of the Vim text editor, consider beginning your adventures with Homebrew by installing [NeoVim](https://neovim.io/). The command to install this formula is:

1 |
brew install neovim |
The [iTerm2](https://iterm2.com/) terminal program is another great place to start. It’s far more robust and configurable than the standard macOS Terminal. Install this cask (GUI application) with the following command:
1 |
brew install --cask iterm2 |
![](https://cdn.thenewstack.io/media/2024/12/aa0b1f1f-install-iterm2.png)
Another example is the [PyCharm Python IDE](https://www.jetbrains.com/pycharm/). Run this command to install it:

1 |
brew install --cask pycharm |
In this case, [PyCharm](https://formulae.brew.sh/cask/pycharm#default) is a native macOS application, hence the use of the
--cask flag. You typically only need this flag if there is both a formula and a cask version of the program.
Display information on PyCharm by using the
info subcommand, as seen below:

1 |
brew info pycharm |
Remove the IDE by using the
uninstall subcommand:
1 |
brew uninstall pycharm |
It may be useful to see a complete inventory of the packages Homebrew manages on your system. For that task, use the
list subcommand. You could redirect the results to a
grep search if you have an idea of what you’re looking for.
1 |
brew list |
![](https://cdn.thenewstack.io/media/2024/12/44c69063-brewlist.png)
### Avoiding Dependency Hell
In earlier days, one of the most challenging aspects of managing software was [dependencies](https://thenewstack.io/a-guide-to-software-dependencies/). Much of today’s open source (or even proprietary) software relies on an interconnected relationship with other applications and code libraries. In other words, installing an application isn’t always as simple as just adding that program to your system. You might also need to add other programs it relies on and possibly other programs *those* programs rely on. This situation was frequent enough to lead to a common term: [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell).

Modern package managers — including Homebrew — recognize and handle these dependencies for you. That’s good news because it simplifies managing software on your system.

The result is that you may enter a command to install one application but observe that the process actually deploys lots of other software, too. Homebrew even tracks and maintains dependency versions for each application to avoid compatibility problems.

### Keeping your Applications Current
You need to keep your software current to mitigate security risks, access new features, and ensure performance and stability.

As mentioned above, use the brew update command to acquire the latest version of the package manager itself. But what about the applications you’ve already installed? The upgrade subcommand handles those.

Use the
upgrade subcommand without an argument to bring all installed packages to the current version. Be aware that this could take some time if you have a lot of applications and haven’t upgraded them recently. Homebrew updates the dependencies, too.

1 |
brew upgrade |
You may only want to update a particular application. If so, just specify it as the argument for the
upgrade subcommand. For example, to update just the mtr [network diagnostic software](https://formulae.brew.sh/formula/mtr#default), type:
1 |
brew upgrade mtr |
## Finding Software
Mac users have various options for acquiring software. In some cases, you can go to the vendor’s website to download a .dmg or .pkg file directly. Other times, you may be directed to clone a Git repository and build the application from source files. A third alternative is browsing the Apple App Store for the application you want.

The App Store presents a specific challenge to developers and other power users. Applications go through a rigorous testing process to ensure their quality and consistency. Not all applications are ready for this process, and not all developers need or want Apple dictating the availability of their software.

Homebrew makes applications available that might not be available in the App Store. Perhaps the software is in the beta testing stages and not yet ready for mainstream production, or maybe it deals with a field Apple doesn’t approve of. Whatever the circumstance, software vendors can make their applications available through Homebrew, providing an alternative to the App Store.

![](https://cdn.thenewstack.io/media/2024/12/c0720b3b-neovim-brew-not-appstore.png)
### Dev Tools to Get You Started with Homebrew
Homebrew provides the IDEs, libraries and other applications needed to maintain a functional development platform.

Search for applications by using the
brew search {application-name} command or browse the immense [formulae list](https://formulae.brew.sh/formula/). Here are a few examples to get you started:

[neovim](https://formulae.brew.sh/formula/neovim#default)Vim text editor fork commonly used on Macs.[pycharm](https://formulae.brew.sh/cask/pycharm#default)Powerful Python IDE.[python3](https://formulae.brew.sh/formula/python@3.13#default)Common programming language.[iterm2](https://formulae.brew.sh/cask/iterm2#default)Robust replacement for Apple’s Terminal application.[mariadb](https://formulae.brew.sh/formula/mariadb#default)Alternative to the MySQL database.[masscan](v)Powerful and fast port scanner.[nmap](https://formulae.brew.sh/formula/nmap#default)The definitive port scanner.
![](https://cdn.thenewstack.io/media/2024/12/6ac15cf6-brew-search-apps.png)
### Create a Formula
Up to this point, I’ve discussed Homebrew from the perspective of a developer setting up a workstation. However, the next logical point is the developer who has already completed a project and is ready to distribute it via Homebrew.

The process involves many steps and several Homebrew commands, but the general process begins with pointing Homebrew to your source files. Next, you’ll edit the formula file, including description, license, dependencies, etc. Create a tap (distribution repository) for your formula, then create the actual formula and push it to your tap.

## How Does Homebrew Compare to Linux and Windows Package Managers?
If you’re already familiar with Linux package managers, then Homebrew won’t present a challenge to you. It provides the same intuitive syntax and similar subcommands as most Linux package managers, so it’s likely to be an easy transition. Windows users don’t tend to use command-line package managers as much as others, so it may take a little getting used to. However, you’ll quickly be hooked on the simplicity of finding and managing your applications using straightforward brew commands.

Begin with the most common tasks: installing, updating and inventorying applications. Get in the habit of using the list and info subcommands. In many cases, a simple brew upgrade command that brings all installed applications Homebrew manages current is enough.

Note that Homebrew also works with Linux if you prefer it to package managers like DNF or APT. You can also add it to Windows systems under the Windows Subsystem for Linux platform. Having a single package manager is certainly handy if you work on all three major platforms (as I do).

## Wrap-Up
Mac systems are very viable development platforms, and many IDEs and other support software packages are available for them. Managing these packages was a challenge until Homebrew entered the scene. Now, finding and maintaining the software you need is straightforward and predictable.

Adding Homebrew to your Mac should be step one as you set up your system for coding projects or system/network administration tasks. Even regular home users benefit from the ability to add the applications they want easily and independently of App Store oversight.

Install Homebrew today using the simple script and begin exploring the available dev tools you need. You’ll quickly discover it’s easier to find these tools and keep them current with this powerful package manager.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)