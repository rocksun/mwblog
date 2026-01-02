If you’ve ever used Linux, you might have heard of [Vim](https://thenewstack.io/vim-after-bram-a-core-maintainer-on-how-theyve-kept-it-going/).

Don’t run away just yet.

Yes, Vim is not exactly the easiest text editor in the world, but it is one of the most powerful available. Vim isn’t just a text editor; it’s a highly configurable and powerful [text editor](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) that’s popular among programmers because it’s a very efficient tool for coding in the command line.

Vim allows users to issue complex commands via keyboard shortcuts, so your fingers never have to leave the keys. Vim can also be extended with plugins to add [IDE](https://thenewstack.io/best-open-source-ides/) functionality.

But what is [Neovim](https://thenewstack.io/neovims-future-could-have-ai-and-brain-computer-interfaces/)?

Neovim is an extensible fork of Vim that is designed to simplify managing the app, improve usability, offer better plugin support and include built-in Language Server Protocol ([LSP](https://microsoft.github.io/language-server-protocol/)) and support for modern GUIs and UIs. Neovim maintains core compatibility with Vim, but offers a much more streamlined experience.

If the idea of developing from a terminal app and the command line sounds up your alley, Neovim might be the right tool for you.

Neovim includes features like:

* Better default settings than Vim.
* A sleek API for plugins.
* Focus on out-of-the-box usability.
* A powerful [Lua](https://thenewstack.io/how-roblox-makes-programming-beginner-friendly-with-luau/) API and the ability to break configurations into modules to make complex setups more manageable.
* Handles tasks like linting, syntax checking and file indexing.
* A built-in, fully scriptable terminal emulator.
* Supports most existing Vim plugins.

Let’s get Neovim installed and configured.

## Installing Neovim

Neovim can be installed on Linux, macOS (using brew) and Windows. Here’s how it’s done:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Windows (via Winget): winget install Neovim.Neovim |
|  | macOS (via Brew): brew install neovim |
|  | Ubuntu-based distributions: sudo apt-get install neovim -y |
|  | Fedora-based distributions: ssudo dnf install -y neovim python3-neovimudo -y |
|  | Arch-based distributions: sudo pacman -S neovim |

Note: To use the plug-in system, you have to install the nightly version (more on that in a bit).

## Configuring Neovim

Once you have Neovim installed, you can certainly use it as is. Of course, given how flexible and extensible the tool is, you’ll want to create your own config file.

To create a config file, you must first create the necessary directory. I’m going to demonstrate this on Linux. If you’re using either macOS or Windows, you’ll need to alter the location of the config file accordingly.

Create the new directory with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Create the config file with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | nano ~/.config/nvim/init.vim |

In that file, you’re going to add all your configuration options. A sample config might look like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | set nocompatible                 " disables compatibility with old-time vi |
|  | set showmatch                    " shows matching |
|  | set ignorecase                     " case insensitive |
|  | set mouse=v                        " middle-click paste with |
|  | set hlsearch                         " highlight search |
|  | set incsearch                        " incremental search |
|  | set tabstop=4                        " number of columns occupied by a tab |
|  | set softtabstop=4                  " see multiple spaces as tabstops so <BS> does the right thing |
|  | set expandtab                       " converts tabs to white space |
|  | set shiftwidth=4                     " width for autoindents |
|  | set autoindent                       " indents a new line the same amount as the line just typed |
|  | set number                           " adds line numbers |
|  | set wildmode=longest,list     " gets bash-like tab completions |
|  | set cc=80                             " sets an 80-column border for good coding style |
|  | filetype plugin indent on       "allows auto-indenting depending on file type |
|  | syntax on                             " enables syntax highlighting |
|  | set mouse=a                       " enables mouse click |
|  | set clipboard=unnamedplus " uses system clipboard |
|  | filetype plugin on |
|  | set cursorline                      " highlights current cursorline |
|  | set ttyfast                            " Speeds up scrolling in Vim |
|  | " set spell                            " enables spell check (may need to download language package) |
|  | " set noswapfile                  " disables creating swap file |
|  | " set backupdir=~/.cache/vim " Directory to store backup files. |

You can find a complete listing of options in the [Neovim documentation](https://neovim.io/doc/user/options.html).

Once you’ve created your config file, save it with Ctrl+X.

## Plugins

Neovim can use vim-plug as a plug-in manager. The only problem is that a lot of plugins won’t function properly unless you’re using the nightly build, which can be found [here](https://github.com/neovim/neovim).

To install the nightly version on Ubuntu, follow these steps:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo add-apt-repository ppa:neovim-ppa/unstable |
|  | sudo apt-get update |
|  | sudo apt-get install neovim -y |

With that taken care of, install vim-plug, which is done with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |

Now that those steps are taken care of, let’s use a little cheat to make things easier. There’s a script called Kickstarter that makes it really easy to set up Neovim. To use Kickstarter, you’ll want to move the init.vim file out of your nvim directory and then issue the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | git clone https://github.com/nvim-lua/kickstart.nvim.git "${XDG\_CONFIG\_HOME:-$HOME/.config}"/nvim |

After that, start Neovim to load Kickstarter. The command to run the app is:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Once it loads, you’ll find yourself in the Neovim window, where you can begin using the editor.

To load a plugin, you use the `:packadd` command like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

After that, you then invoke the plugin like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

The DiffTool plugin compares two directories or files side by side, and supports directory diffing, rename detection and highlights changes.

## Use the Built-in Tutorial

At this point, I would highly recommend using the interactive tutorial, which will greatly help with your introduction to Neovim. To start the tutorial, exit out of Neovim with the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Back at your terminal window, issue the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

This interactive tutorial will really help you understand how to get up to speed with Neovim, and given how much there is to learn, this should be an absolute must for anyone just getting started.

Seriously, the tutorial is a must.

Neovim is a very powerful text editor that, with some upfront configurations, could replace your current editor for programming and much more. Yes, it has a step learning curve, but the built-in tutorial will go a long way to helping you out.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)