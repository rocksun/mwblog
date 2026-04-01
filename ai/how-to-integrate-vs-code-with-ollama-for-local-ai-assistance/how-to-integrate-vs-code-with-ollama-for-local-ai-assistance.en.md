If you’re starting your journey as a programmer and want to jump-start that process, you might be interested in taking advantage of AI to make the process of getting up to speed a bit simpler. After all, coding can be a tough business to break into, and every advantage you can give yourself should be considered.

Before I continue, I will say this: use AI to help you learn the language that you’re interested in and not as a substitute for actually learning the language. Consider this an *assistant*, not a replacement for skill.

When I need to turn to AI, I always go for locally-installed options for a couple of reasons. First, using [locally installed AI](https://thenewstack.io/how-to-deploy-a-local-ai-via-docker/) doesn’t put a strain on the electrical grid. Second, I don’t have to worry that a third party is going to get a glimpse of my queries, so privacy is actually possible.

To that end, I depend on [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) as my chosen locally-installed AI tool. Ollama is easy to use, flexible, and reliable.

If your IDE of choice is [Visual Studio Code](https://thenewstack.io/vs-code-becomes-multi-agent-command-center-for-developers/), you’re in luck, as you can integrate it with a locally installed instance of Ollama.

I’m going to show you how this is done.

## What you’ll need

To make this work, you’ll need a desktop OS running [Linux](https://thenewstack.io/introduction-to-linux-operating-system/), macOS, or Windows. I’ll demonstrate the process on a Ubuntu-based Linux distribution (Pop!\_OS). If you’re using either macOS or Windows, the only things that you’ll need to change are the installation of Ollama and VS Code. Fortunately, in both instances, it’s just a matter of downloading the binary installer of each tool, double-clicking the downloaded files, and walking through the setup process.

On Linux, it’s a bit different.

Let me show you.

## Installing Ollama

The first thing we’ll do is install Ollama. If you’re using macOS or Windows, download the [.dmg for Mac](https://ollama.com/download/Ollama.dmg) or the [.exe for Windows](https://ollama.com/download/OllamaSetup.exe), double-click the file, and you’re off.

On Linux, open a terminal window and issue the command:

*`curl -fsSL https://ollama.com/install.sh | sh`*

You’ll be prompted for your sudo password before the installation begins.

After the installation is complete, you’ll then need to pull a specific LLM for Ollama. On macOS and Windows, open the Ollama GUI, go to the query field, click the downward-pointing arrow, type *codellama,* and click the entry to install the model.

On Linux, open a terminal app and pull the necessary LLM with:

*`ollama pull codellama`*

## Install VS Code

Next, you’ll need to install VS Code.

The same thing holds true: with macOS or Windows, [download the VS Code executable binary](https://code.visualstudio.com/download) for your OS of choice, double-click the downloaded file, and walk through the installation wizard.

On Linux, you’ll also need to download the installer for your distribution of choice (.deb for Debian-based distributions, .rpm for Fedora-based distributions, or the Snap package).

To install VS Code on Linux, change into the directory housing the installer file you downloaded. Install the app with one of the following commands:

* For Ubuntu-based distributions: *sudo dpkg -i code\*.deb*
* For Fedora-based distributions: *sudo rpm -i code\*.rpm*
* For Snap packages: *sudo snap install code –classic*

You now have the two primary pieces to get you started.

## Setting up VS Code

The next step is to set up VS Code to work with Ollama. To that, you’ll need to install an extension called Continue.

For that, hit Ctrl+P (on macOS, that’s Cmd+P).

In the resulting field, type:

*`ext install continue.continue`*

In the resulting page (**Figure 1**), click Install.

![](https://cdn.thenewstack.io/media/2026/03/c591870f-ollamacode2.jpg)

**Figure 1:** Installing the necessary extension on VS Code is simple.

Once the extension is installed, click on the Continue icon in the left sidebar. In the resulting window, click the Select Model drop-down and click Add Chat model (**Figure 2**).

![](https://cdn.thenewstack.io/media/2026/03/8e952efb-ollamacode3-1024x641.jpg)

**Figure 2:** You have to add a model before you can continue.

In the resulting window, select Ollama from the provider drop-down (**Figure 3**).

![](https://cdn.thenewstack.io/media/2026/03/1c817b9d-ollamacode5.jpg)

**Figure 3:** You can select from any one of the available models, but we’re going with Ollama.

Next, make sure to select Local from the tabs and then click the terminal icon to the right of each command. This will open the built-in terminal, where you’ll then need to hit Enter on your keyboard to execute the command (**Figure 4**).

![](https://cdn.thenewstack.io/media/2026/03/c66b5613-ollamacode6-1024x643.jpg)

**Figure 4:** This is where the meat of the configuration takes place.

When the first command (the Chat model command) completes, do the same for the second command (the Autocomplete model) and the third (the Embeddings model). This will take some time, so be patient. When each step is complete, you’ll see a green check by it.

After that’s completed, click Connect.

If you click the Continue extension, you should now see a new chat window that is connected to your locally installed instance of Ollama (**Figure 5**).

![](https://cdn.thenewstack.io/media/2026/03/17092a75-ollamacode7-1024x643.jpg)

You are all set up and ready to rock.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)