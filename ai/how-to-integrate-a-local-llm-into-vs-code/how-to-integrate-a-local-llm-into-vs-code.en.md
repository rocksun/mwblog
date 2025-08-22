If your [IDE](https://thenewstack.io/best-open-source-ides/) of choice is [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) and you’ve wondered what it would be like to use it with a localized AI [large language model (LLM)](https://thenewstack.io/introduction-to-llms/), you’re in luck.

But why would you do this?

Well, you might want to make use of AI to enhance your workflow, help debug your code or even learn a new [programming language](https://thenewstack.io/introduction-to-java-programming-language/). For whatever reason you have, integrating VS Code with a local LLM like [Ollama](https://thenewstack.io/install-ollama-ai-on-ubuntu-linux-to-use-llms-on-your-own-machine/) (my go-to AI) is not nearly as hard as you might think it would be. The end result is a powerful tool you can leverage for whatever coding or coding-adjacent need you have.

The benefits of integrating with a local LLM are that you don’t have to use an API, you’ll have more privacy, it can be used offline and you can select your model of choice.

I’m going to show you how to set this up with Ollama on a [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) machine (Pop!\_OS to be exact). Yes, you can do this on both macOS and Windows as well; the only difference is the Ollama installation process. On Windows, installing Ollama is as simple as downloading the app and going through the usual installation process.

## What You’ll Need

To make this work, you’ll need VS Code installed and (for Linux) a user with sudo privileges. That’s it. Let’s get to work.

## Installing Ollama on Linux

To install Ollama on Linux, you only have to run the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -fsSL https://ollama.ai/install.sh | bash |

On macOS, the command is:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl https://ollama.ai/install.sh | sh |

When that command finishes, you’re ready to pull a model. Before you do that, check out the [Ollama Model Library](https://ollama.com/library) and find the model you want to use. One of the better models for code work is called codellama, which can be pulled with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Installing the Required Extension

The extension in question is called Continue. To install Continue, open VS Code and then hit the Ctrl+P keyboard shortcut (for Linux and Windows), or the Cmd+P shortcut (for macOS). When the search bar appears, type the following into it:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | ext install continue.continue |

The Continue extension should appear in the left sidebar. Click Install (Figure 1) and the extension will install.

[![](https://cdn.thenewstack.io/media/2025/08/9e86d332-continue1.jpg)](https://cdn.thenewstack.io/media/2025/08/9e86d332-continue1.jpg)

Figure 1. Installing Continue for VS Code.

## Configuring the Extension

With VS Code open, click on the Continue icon in the left sidebar, and the Continue pop-up should appear. In that window, click “Or, configure your own models” (Figure 2).

[![](https://cdn.thenewstack.io/media/2025/08/b15c0685-continue2.jpg)](https://cdn.thenewstack.io/media/2025/08/b15c0685-continue2.jpg)

Figure 2. You can also log in with a Continue Hub account, but we’re using local models, so it’s not necessary.

In the next window, scroll to the bottom and click “Click here to view more providers.” In the resulting window, select Ollama as the provider and then select CodeLlama from the Model drop-down (Figure 3).

[![](https://cdn.thenewstack.io/media/2025/08/9d858136-continue3.jpg)](https://cdn.thenewstack.io/media/2025/08/9d858136-continue3.jpg)

Figure 3. Connecting VS Code to Ollama.

Click Connect, and a tutorial will appear. I would suggest reading through this to get a better idea of how it works. You’ll find instructions on how to use the autocomplete, edit, chat and agent features.

## Using Continue/Ollama

Let’s say you want Ollama to write a bit of [Python](https://thenewstack.io/what-is-python/) code for you that accepts user input and saves it to a file. In the Continue Prompt (accessed with Ctrl+I), type something like this:

*write a Python program that accepts input from a user and saves it to a file*

Your chosen model will go to work and not only create the script, but also explain how it works.

You’ll notice there’s a run button in the output (which is actually Apply Code). Once that completes, you can ask a follow-up like:

*run the above code*

You should see the sample output that runs the code. If it works, you know the code is golden.

You can also opt to open a terminal window (via VS Code), open a new file, copy/paste the code into the file, save it and then run it as you normally would. Or, you could go back to the main VS Code window, copy/paste the code into a new project and run/debug it like that.

Speaking of debugging, if you want to debug code with Continue, you could go back to the chat window, type something like *fix the following Python code*, paste the code into the window and hit Enter. Your local model should be able to go through the code, fix whatever issues it finds and present the results.

The nice thing about using VS Code with a local model is that it gives you the chance to learn about the language you are using as you work. You can ask questions, such as “What is a Python Tuple?” The results are surprisingly helpful.

And that, my friends, is how you integrate a local LLM into VS Code to use AI to improve your skills.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)