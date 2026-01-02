如果你使用过 Linux，你可能听说过 [Vim](https://thenewstack.io/vim-after-bram-a-core-maintainer-on-how-theyve-kept-it-going/)。

别急着跑。

是的，Vim 绝不是世界上最简单的文本编辑器，但它是功能最强大的编辑器之一。Vim 不仅仅是一个文本编辑器；它是一个高度可配置且功能强大的[文本编辑器](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/)，因其作为命令行中高效的编码工具而受到程序员的欢迎。

Vim 允许用户通过键盘快捷键发出复杂的命令，这样你的手指就永远不必离开键盘。Vim 还可以通过插件扩展以添加 [IDE](https://thenewstack.io/best-open-source-ides/) 功能。

但[Neovim](https://thenewstack.io/neovims-future-could-have-ai-and-brain-computer-interfaces/) 又是什么呢？

Neovim 是 Vim 的一个可扩展分支，旨在简化应用程序管理、提高可用性、提供更好的插件支持，并包括内置的语言服务器协议 ([LSP](https://microsoft.github.io/language-server-protocol/)) 以及对现代 GUI 和 UI 的支持。Neovim 保持了与 Vim 的核心兼容性，但提供了更加精简的体验。

如果从终端应用和命令行进行开发的想法很合你的胃口，那么 Neovim 可能是适合你的工具。

Neovim 包含以下功能：

*   比 Vim 更好的默认设置。
*   一个用于插件的时尚 API。
*   专注于开箱即用的可用性。
*   一个功能强大的 [Lua](https://thenewstack.io/how-roblox-makes-programming-beginner-friendly-with-luau/) API，以及将配置分解为模块的能力，使复杂的设置更易于管理。
*   处理代码检查、语法检查和文件索引等任务。
*   一个内置的、完全可脚本化的终端模拟器。
*   支持大多数现有 Vim 插件。

让我们来安装和配置 Neovim。

## 安装 Neovim

Neovim 可以安装在 Linux、macOS（使用 brew）和 Windows 上。操作方法如下：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Windows (via Winget): winget install Neovim.Neovim |
|  | macOS (via Brew): brew install neovim |
|  | Ubuntu-based distributions: sudo apt-get install neovim -y |
|  | Fedora-based distributions: ssudo dnf install -y neovim python3-neovimudo -y |
|  | Arch-based distributions: sudo pacman -S neovim |

注意：要使用插件系统，你必须安装每夜版（稍后会详细介绍）。

## 配置 Neovim

一旦安装了 Neovim，你当然可以直接使用它。当然，考虑到这个工具的灵活性和可扩展性，你会希望创建自己的配置文件。

要创建配置文件，你必须首先创建必要的目录。我将在 Linux 上演示这一点。如果你使用的是 macOS 或 Windows，你需要相应地更改配置文件的位置。

使用以下命令创建新目录：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

使用以下命令创建配置文件：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | nano ~/.config/nvim/init.vim |

在该文件中，你将添加所有配置选项。一个示例配置可能如下所示：

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

你可以在 [Neovim 文档](https://neovim.io/doc/user/options.html)中找到完整的选项列表。

创建配置文件后，按 Ctrl+X 保存。

## 插件

Neovim 可以使用 vim-plug 作为插件管理器。唯一的问题是，除非你使用每夜构建版（可以在[这里](https://github.com/neovim/neovim)找到），否则许多插件无法正常运行。

要在 Ubuntu 上安装每夜版，请遵循以下步骤：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo add-apt-repository ppa:neovim-ppa/unstable |
|  | sudo apt-get update |
|  | sudo apt-get install neovim -y |

完成这些后，安装 vim-plug，使用以下命令：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |

现在这些步骤都已完成，让我们使用一个小技巧让事情变得更容易。有一个名为 Kickstarter 的脚本，可以非常轻松地设置 Neovim。要使用 Kickstarter，你需要将 `init.vim` 文件从 nvim 目录中移出，然后执行以下命令：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | git clone https://github.com/nvim-lua/kickstart.nvim.git "${XDG\_CONFIG\_HOME:-$HOME/.config}"/nvim |

之后，启动 Neovim 以加载 Kickstarter。运行应用程序的命令是：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

一旦加载完成，你就会进入 Neovim 窗口，在那里你可以开始使用编辑器。

要加载插件，可以使用 `:packadd` 命令，像这样：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

之后，你就可以像这样调用插件：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

DiffTool 插件可以并排比较两个目录或文件，并支持目录差异、重命名检测和高亮显示更改。

## 使用内置教程

此时，我强烈建议你使用交互式教程，它将极大地帮助你入门 Neovim。要开始教程，请使用以下命令退出 Neovim：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

回到你的终端窗口，执行命令：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

这个交互式教程将真正帮助你理解如何快速上手 Neovim，鉴于有很多东西需要学习，这对于任何刚开始的人来说绝对是必不可少的。

说真的，这个教程是必不可少的。

Neovim 是一个非常强大的文本编辑器，通过一些前期配置，它可以取代你当前的编程编辑器，甚至更多。是的，它有陡峭的学习曲线，但内置教程将大大帮助你。