![](/blog/assets/images/shipyard-e6dcb9e9c9ab517c2a3bdcb1450dc15f.webp)

如果你从事人工智能工作，你可能正在使用 Python。也许你有一个用现在流行的任何 JS 框架编写的 Web 应用，但人工智能中的大多数核心工具都是围绕 Python 构建的。所以，像我这样的 Go 程序员也许该弄清楚生产环境的 Python 是如何构建的了。

上周，我重新发现了 [Development Containers（开发容器）](https://containers.dev/)。当你使用它们时，你会在容器中进行所有开发，而不是直接在你的机器上。这个容器是使用 [`devcontainer.json`](https://containers.dev/implementors/json_schema/) 文件定义的，当你创建一个开发容器时，它每次都会从头开始重建。这意味着，当你的构建在开发环境中可以工作时，它不仅仅是在你的机器上工作。它将在任何人的机器上工作。

不得不使用 Python 应该没什么大不了的，我的第一门编程语言就是 Python，但有一个小问题导致我认为自己受到了远古神灵的诅咒：Python 环境管理工具会随机地崩溃。我一直没能弄明白为什么会发生这种情况，但在过去的三年里，我一直无法始终如一地让基本的编辑、测试或其他项目管理工具可靠地工作。我花了几个小时调试奇怪的 SIGBUS 错误，但其他人无法重现，以及其他超出正常问题调试范围的事情。

崩溃最严重的是我编辑器中的语言服务器。如果我无法让语言服务器工作，我就不知道在文件中允许对任何给定的事物做什么，而不用打开一堆文档选项卡。再加上 Python 没有像 Go 那样的 [标准文档站点](https://pkg.go.dev)，这意味着弄清楚我能做什么并不容易。

更糟糕的是，管理 Python 的方法和地球上的沙粒一样多。开始使用 Python 意味着你需要做出很多可爱的决定：

*   你使用什么环境管理器？Conda？Virtualenv？uv？Anaconda？Miniconda？Homebrew？Pipenv？
*   你的项目依赖于哪个版本的 Python？许多大型库（如 tensorflow）出于性能原因，会对 Python 进行深度猴子补丁，因此它们无法在新版本的解释器上工作。
*   你如何安装你的依赖项？Pip？Pip3？Uv？

[![](/blog/assets/images/xkcd_standards-34f86e57eaef756c15ecfb2521124998.webp)](https://xkcd.com/927/)
[Standards -- XKCD](https://xkcd.com/927/)（标准 —— XKCD）

必须存在某种中间道路。我们应该能够拥有美好的事物，比如能够简单地打开一个 git 仓库并获得一个可用的开发环境，对吗？

## 工作原理[​](#how-it-works "Direct link to How it works")

当你将你的应用程序打包到 Docker 镜像中时，你会创建一个 `Dockerfile` 清单，其中包含一个基础镜像，然后列出你对该基础镜像所做的所有更改，以使事情正常工作。这可以是任何事情，从将你的源代码复制到镜像中，构建该代码，安装依赖项，或者任何归结为复制文件和运行命令的事情。当你定义一个开发容器时，你会创建一个 `devcontainer.json` 清单，其中指定你正在使用的基础镜像以及你想要添加到其中的任何 [功能](https://containers.dev/features)。

例如，让我们考虑一下你需要做什么才能让 [Node.js](http://Node.js) 环境正常工作。这是一个用于 Node 的示例 `devcontainer.json` 文件：

```
{  
  "name": "Node",  
  "image": "mcr.microsoft.com/devcontainers/base:bookworm",  
  "features": {  
    "ghcr.io/devcontainers/features/node:1": {},  
    "ghcr.io/devcontainers-extra/features/neovim-apt-get:1": {}  
  },  
  "postCreateCommand": "npm ci"  
}  

```

这告诉你的编辑器创建一个 [Microsoft 的基础 Debian 镜像](https://github.com/devcontainers/images/tree/main/src/base-debian) 的副本，并自动安装 [Node](https://github.com/devcontainers/features/tree/main/src/node) 和 [neovim](https://github.com/devcontainers-extra/features/tree/main/src/neovim-apt-get)。它还会安装你的所有 Node 依赖项，以便你只需执行以下操作即可启动并运行：

1.  在开发容器中打开 repo
2.  打开一个终端
3.  运行 `npm run start`
4.  没有第 4 步。

想象一下这个工作流程能给你带来什么。让人们快速上手将易如反掌。

### Python 怎么样？[​](#what-about-python "Direct link to What about Python?")

你可能坐在那里问自己“是的，这很酷，但是 Python 呢？”Python 在开发使用方面提出了很多挑战，因为存在很多变量。如果你知道自己在做什么，这很好并且可以管理。如果你不知道，你最终会陷入 pip 地狱。你不想和我一起陷入 pip 地狱。

开发容器给拥有 Python 专家和非 Python 专家的团队带来的一个重要好处是，它能够让人们在他们不是 Python 环境元物理学专家的情况下，拥有一个已知的工作设置以供他们回退。这对于像我这样关心最终结果的人来说非常棒，但根本不在乎事情是如何完成的，只要它能工作（对于某些合理的“工作”定义）。更好的是，你可以定义特定于该项目的编辑器配置设置和扩展列表，这意味着你真的可以简单地打开一个新的 repo 并在几秒钟内启动并运行。

这种编辑器预配置意味着你可以永远解决诸如“我需要哪个版本的 Python？”或“我如何只安装依赖项？”之类的问题。以 [tigrisdata-community/huggingface-datasets-with-tigris](https://github.com/tigrisdata-community/huggingface-datasets-with-tigris) 为例。它的 [`devcontainer.json`](https://github.com/tigrisdata-community/huggingface-datasets-with-tigris/blob/main/.devcontainer/devcontainer.json) 为你解答了这个问题：

```
{  
  // ...  
  "postCreateCommand": "uv python install && uv venv && uv sync",  
  "remoteEnv": {  
    "UV_LINK_MODE": "copy",  
    "UV_PYTHON": "3.10"  
  }  
  // ...  
}  

```

当你使用此清单创建开发容器时，它会执行以下操作：

1.  使用 [uv](https://docs.astral.sh/uv/) 安装 Python 3.10.x
2.  为你的所有依赖项创建一个 [Python 虚拟环境](https://docs.astral.sh/uv/pip/environments/#using-python-environments)
3.  安装所有 Python 依赖项

然后你可以使用 `uv run` 运行代码，事情就能正常工作了。所有这些复杂的依赖项管理都变成了你环境的问题。更好的是，看看 [清单的这一部分](https://github.com/tigrisdata-community/huggingface-datasets-with-tigris/blob/5d32918c5d890b924b46703074e9966249406032/.devcontainer/devcontainer.json#L33-L51)：

```
{  
  // ...  
  "customizations": {  
    "vscode": {  
      "extensions": [  
        "ms-python.python",  
        "ms-python.vscode-pylance",  
        "tamasfe.even-better-toml",  
        "ms-toolsai.jupyter",  
        "ms-toolsai.vscode-jupyter-cell-tags",  
        "ms-toolsai.jupyter-renderers",  
        "ms-toolsai.vscode-jupyter-slideshow",  
        "ms-python.debugpy",  
        "ms-toolsai.jupyter-keymap",  
        "amazonwebservices.aws-toolkit-vscode"  
      ],  
      "settings": {  
        "python.defaultInterpreterPath": "./.venv/bin/python"  
      }  
    }  
  }  
  // ...  
}  

```

这使 VS Code 安装你需要的所有扩展来获得一个可用的开发环境，并且 `python.defaultInterpreterPath` 设置是锦上添花，使语言服务器集成工作。这使你可以简单地克隆一个 repo 并获得一个可用的语言服务器。

## 结论[​](#conclusion "Direct link to Conclusion")

我意识到这听起来很简单，而且说实话，它应该如此简单，但我花了三年的实验、辛勤劳动和痛苦才达到你可以真正克隆一个 repo 并获得可用的语言服务器集成的地步。如果你也一直在为安装 Python 而苦苦挣扎，以便你可以通过编写代码来实现 IPO，请尝试开发容器。

即使你使用 [GitHub Codespaces](https://github.com/features/codespaces)，这也能正常工作，这意味着你甚至不需要安装 VS Code 的副本即可处理该项目。