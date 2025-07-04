![](/blog/assets/images/shipyard-e6dcb9e9c9ab517c2a3bdcb1450dc15f.webp)

If you're working in AI, you're probably working in Python. Maybe you have a
webapp in whatever JS framework is popular right now, but most of the core
tooling in AI is built in and around Python. So maybe it’s time for a Go
programmer like me to figure out how the production Python gets made.

Last week I rediscovered [Development Containers](https://containers.dev/). When
you use them, you do all your development in a container instead of on your
machine directly. This container is defined using a
[`devcontainer.json`](https://containers.dev/implementors/json_schema/) file and
when you create a development container it’s rebuilt from scratch every time.
This means that when you get your build working in development, it won’t just
work on your machine. It’ll work on anyone’s machine.

Having to use Python shouldn't be that big of a deal, my first programming
language was Python, but there’s one small problem that has resulted in me
thinking that I have been cursed by an elder deity: Python environment
management tools randomly break for me. I’ve never been able to figure out why
this happens, but in the last three years I have not been able to consistently
have basic editing, testing, or other project management tooling work reliably.
I’ve spent hours debugging weird SIGBUS errors that nobody else can recreate and
other things that go way above and beyond normal debugging of issues.

The biggest thing that breaks is the language server in my editor. If I can’t
get the language server working, I don’t know what I’m allowed to do with any
given thing in the file without having to have a bunch of documentation tabs
open. This combined with Python not having
[a standard documentation site like Go does](https://pkg.go.dev) means that
figuring out what I can do is not easy.

Making things worse, there’s as many ways to manage Python as there are grains
of sand on the planet. Starting to use Python means you get to make a lot of
lovely decisions:

* What environment manager are you using? Conda? Virtualenv? uv? Anaconda?
  Miniconda? Homebrew? Pipenv?
* Which version of Python does your project depend on? Many big libraries like
  tensorflow do deep monkey patching of Python for performance reasons and as a
  result they can’t work on newer versions of the interpreter.
* How are you installing your dependencies? Pip? Pip3? Uv?

[![](/blog/assets/images/xkcd_standards-34f86e57eaef756c15ecfb2521124998.webp)](https://xkcd.com/927/)
[Standards -- XKCD](https://xkcd.com/927/)

There has to be some kind of middle path. We should be able to have nice things
like the ability to just open a git repo and get a working development
environment, right?

## How it works[​](#how-it-works "Direct link to How it works")

When you package your app in a Docker image, you make a `Dockerfile` manifest
with a base image and then list out all the changes you make to that base image
to get things working. This could be anything from copying your source code into
the image, building that code, installing dependencies, or anything else that
boils down to copying files and running commands. When you define a development
container, you make a `devcontainer.json` manifest that specifies the base image
you’re working from and any [features](https://containers.dev/features) you want
to add to it.

For example, let’s consider what you need to do in order to get a
[Node.js](http://Node.js) environment working. Here’s a sample
`devcontainer.json` file for working with Node:

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

This tells your editor to make a copy of
[Microsoft’s base Debian image](https://github.com/devcontainers/images/tree/main/src/base-debian)
with [Node](https://github.com/devcontainers/features/tree/main/src/node) and
[neovim](https://github.com/devcontainers-extra/features/tree/main/src/neovim-apt-get)
automatically installed. It also installs all of your Node dependencies so that
all you need to do to get up and running is:

1. Open the repo in a development container
2. Open a terminal
3. Run `npm run start`
4. There is no step 4.

Just imagine what that workflow could give you. Spinning people up would be a
walk in the park.

### What about Python?[​](#what-about-python "Direct link to What about Python?")

You’re probably sitting there asking yourself “yeah, that’s cool, but what about
Python?” Python presents a lot of challenges for development use because there’s
so many variables at play. If you know what you’re doing, this is fine and
manageable. If you don’t, you end up in pip hell. You don't want to be in pip
hell with me.

One of the big things that development containers give teams that have a mix of
Python experts and non-Python experts is the ability to just have a known
working setup for people to fall back on in case they aren’t an expert in Python
environment metaphysics. It’s great for people like me who care about the end
result, but do not care at all how things go about getting done as long as it
works (for some reasonable definition of “works”). Even better, you can define
editor configuration settings and a list of extensions specifically for that
project, meaning that you really can just open a new repo and get up and running
within seconds.

This editor preconfiguration means you can fix problems like “What version of
Python do I need?” or “How do I just install the dependencies?” forever. Take
[tigrisdata-community/huggingface-datasets-with-tigris](https://github.com/tigrisdata-community/huggingface-datasets-with-tigris)
for example. Its
[`devcontainer.json`](https://github.com/tigrisdata-community/huggingface-datasets-with-tigris/blob/main/.devcontainer/devcontainer.json)
answers that question for you:

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

When you create a development container with this manifest, it does the
following:

1. Installs Python 3.10.x with [uv](https://docs.astral.sh/uv/)
2. Creates a
   [Python virtual environment](https://docs.astral.sh/uv/pip/environments/#using-python-environments)
   for all of your dependencies
3. Installs all of the Python dependencies

And then you can run the code with `uv run` and things Just Work™. All of that
complicated dependency management becomes your environment’s problem. Even
better, take a look at
[this part of the manifest](https://github.com/tigrisdata-community/huggingface-datasets-with-tigris/blob/5d32918c5d890b924b46703074e9966249406032/.devcontainer/devcontainer.json#L33-L51):

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

This makes VS Code install every extension you need to get a working development
environment and that `python.defaultInterpreterPath` setting is the cherry on
top that makes the language server integration work. This lets you simply clone
a repo and get a working language server.

## Conclusion[​](#conclusion "Direct link to Conclusion")

I realize this sounds like a fairly simple thing, and let’s be honest, it should
be this simple, but it’s taken me three years of experimentation, toil, and
suffering to get to the point where you really can just clone a repo and get
working language server integration. If you have also been suffering trying to
get Python installed so you can vibe code your way to an IPO, give development
containers a try.

This even works if you use
[GitHub Codespaces](https://github.com/features/codespaces), meaning that you
don’t even need to install a copy of VS Code to work on the project.