Installing packages globally isn’t always a good idea. Different tools inside an application can require specific versions of features, functions, or dependencies. These can conflict with or break other parts of the same application or other projects on your system. There’s a simple solution. Install locally not globally. Favoring more local installations isn’t a new idea in software development. One of the core principles of development is to use lightweight, isolated setups, and modular code. This keeps code contained, modular, and predictable.

These same ideas helped drive the rise of container-based development (think [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)). [Containers](https://thenewstack.io/introduction-to-containers/) isolate applications and their dependencies so they can run reliably in different environments. Virtual environments apply that same principle at the language level. They let you isolate dependencies for a specific project, no matter how big or small, without affecting anything else on your system.

## What is a virtual machine?

A [virtual machine](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/), aka virtual environment, is an isolated installation that lives directly in your project directory. Think of it as a self-contained workspace for a single project.

In [Python](https://thenewstack.io/what-is-python/), each virtual environment includes its own Python interpreter, package installer (`pip`), and installed libraries. These aren’t unique to virtual environments, these elements are included in every Python project. The difference with projects built with virtual environments is that everything is isolated. Each environment has its own copies of the Python interpreter, `pip`, and libraries, so changes in one project won’t affect any other project or the system Python.

Global installs aren’t always problem but they can be. For example:

* Project A needs requests version 2.25
* Project B needs requests version 2.31

Globally, only one version of a package is active at a time. With virtual environments, however, each project can have its own version, allowing both projects to work independently. This isolation makes applications easier to maintain. For example, a new version might break Project A but is necessary for Project B. It also makes projects more reliable and safer to experiment with.

Virtual environments are easy to work with. The remainder of this tutorial will build two Python virtual environments inside the same project to show how each can have its own packages and produce different results from the same Python script.

*Virtual environments aren’t unique to Python but this tutorial will use the Python language. Please make sure you have Python installed on your machine before starting.*

## Building Python virtual environments

Open a new project in your IDE and let’s set up our folders:

Once you’re in the new folder, we’re ready to build the virtual environments. We’re going to build two virtual environments.

Upon successful completion, you’ll see a new folder called `venv`with a new folder/ file tree under it. You should see a `venv_old` and `venv_new`.

### Activate Python virtual environment

We’re going to work on`venv_old` first. Use the following command in your terminal. Don’t cd into the venv folder. Run the following command while in the parent folder,`build_venv`.

You will then see a (venv) before your command prompt in your terminal.

### Install packages in Python virtual environment

Now we’re ready to install`numpy` into`venv_old`. This process looks similar to installing globally but it will only install `numpy` in the virtual environment.

### Run Python inside the virtual environment

Next, we’re going to create our `main.py` file. The code in`main.py` will not run if `numpy` isn’t installed (more on that later).

Create the file.

Once`main.py` appears in your folder tree, add this code to the file.

Once added, run the following code in your terminal. Quick note, the command in my terminal for running Python scripts is`python3`. Yours might be`python` or something else entirely. You can check by running `python --version` or `python3 --version`and keep troubleshooting.

Upon successful completion you’ll see  a random number in the terminal.

### Deactivating Python virtual environment

Before we can test `main.py` in `venv_new`, we’ll need to deactivate`venv_old`.  You can do that by typing the following into your terminal.

Working in the second virtual environment

Now, let’s activate`venv_new`.

Run `main.py`.

You should see an error because`numpy`isn’t installed in`venv_new`.

If you then deactivate `venv_new`and run`main.py`with neither virtual environment, you will see a random number. This is because Python uses the system or user-installed packages, so your script can still find NumPy and run successfully. Virtual environments only isolate packages inside that environment, so without one, Python falls back to whatever is installed globally or for your user.

### Working with virtual environments

This simple setup shows how virtual environments let you control exactly which packages each project uses, preventing conflicts and making experiments safe. Even in a small project, isolating dependencies can save a lot of headaches down the line.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)