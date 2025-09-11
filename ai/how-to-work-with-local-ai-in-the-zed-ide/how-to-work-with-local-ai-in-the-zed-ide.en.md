For those who believe AI is a great way to not only learn a new [programming language](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/) but also to help refine your code, there’s an [IDE](https://thenewstack.io/best-open-source-ides/) that just might be right up your alley. That IDE Is [Zed](https://zed.dev/).

The [creators of Zed](https://thenewstack.io/how-rust-based-zed-built-worlds-fastest-ai-code-editor/) call it “a next-generation code editor designed for high-performance collaboration with humans and AI.”

I’ve tested several IDEs that include AI support, and although Zed might not have the massive feature list of some other IDEs, with regard to AI integration, I would place it right up there with the best of them.

Zed is a cross-platform IDE (currently only for [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) and macOS, with a Windows port coming soon) that can be used for free (for personal use only) or $20/month for the Pro version. The difference between the two is that the free version only gives you 50 Zed-hosted prompts per month, 2000 accepted edit predictions and unlimited prompts with an API key. The Pro plan gives you 500 prompts per month (with usage-based billing beyond 500), unlimited edit predictions and community support.

The Zed feature set includes GPU rendering, Language Server Protocol, Tree-sitter, debugger with support for Debug Adapter Protocol, AI assistance, [Model Context Protocol (MCP)](https://thenewstack.io/is-model-context-protocol-the-new-api/), [Git support](https://thenewstack.io/need-to-know-git-start-here/), multibuffer editing, remote development and real-time collaborative editing with other Zed users or AI agents. There are also hundreds of extensions to extend the feature set.

The big draw for many will be the AI integration. I decided that would be my focus here and that I would specifically concentrate on connecting Zed with a local [large language model (LLM)](https://thenewstack.io/introduction-to-llms/). My local LLM of choice is gpt-oss, powered by a locally installed instance of [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/).

How do you make this work? It’s surprisingly easy.

Let’s walk through it.

## What You’ll Need

To make this work, you’ll need either a Linux or macOS machine and an internet connection. That’s it. I’ll demonstrate the process on Pop!\_OS Linux. The only difference between using Zed on Linux and macOS will be the installation process. With macOS, you simply grab the binary installer from the official download page, double-click it and walk through the install wizard.

## Installing Ollama

Before we get to the Zed installation, you’ll need to first install Ollama and then pull the gpt-oss LLM. To install Ollama, open a terminal window and issue the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -fsSL https://ollama.com/install.sh | sh |

Once the installation completes, you’ll then need to download the LLM we’ll use with Zed. To do that, issue the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Once the model has been pulled, it will be available to use. You can test it by issuing the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

If you land on the Ollama console, congratulations, gpt-oss:20b is installed and ready. You can exit from the prompt with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Installing Zed

As I mentioned, I’ll install Zed on Pop!\_OS Linux, which is done with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -f https://zed.dev/install.sh | sh |

The above command installs the stable build. If you’d like the preview build (which receives updates a week before stable), the command is:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -f https://zed.dev/install.sh | ZED\_CHANNEL=preview sh |

When the installation finishes, locate Zed in your desktop menu and click to launch.

## Using Zed With Ollama

When you first open Zed, you’ll want to make sure Ollama is configured in the Default Settings, which is accessed from the hamburger menu at the top left of the Zed window. From the drop-down, click Default Settings.

In the resulting page, click the search icon and type language\_models in the search field. Hit Enter, and it will take you to the correct section within the settings. Keep in mind, the Zed settings are taken care of in a JSON file (Figure 1), which you will edit.

[![](https://cdn.thenewstack.io/media/2025/09/7ef7d831-zedsettings.jpg)](https://cdn.thenewstack.io/media/2025/09/7ef7d831-zedsettings.jpg)

Figure 1. The Default Settings file in Zed.

In that section, you should see an entry that looks like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | }, |
|  | "ollama": { |
|  | "api\_url": "http://localhost:11434" |
|  | }, |

If you don’t see that entry, add it. And if you have Ollama set up to use a different port, make sure to change it.

You don’t have to save anything, as any changes are automatically saved.

Close the Default Settings tab.

## Using Your Local LLM With Zed

From the Zed main window, click + in the upper-right corner and then click New Thread. When the New Thread pane opens, look down near the bottom right corner, where you’ll see an LLM drop-down that is used to select the LLM you want to use. From that list, you should see gpt-oss listed. Select that option and you’re set. From the drop-down directly to the left, make sure Write is selected.

Let’s have Zed write a C++ Hello World program (Figure 2). For that, type the query:

*Write a C++ Hello World application*

[![](https://cdn.thenewstack.io/media/2025/09/22bd603f-zedcplus.jpg)](https://cdn.thenewstack.io/media/2025/09/22bd603f-zedcplus.jpg)

Figure 2. Zed successfully created a C++ Hello World app.

Depending on your machine (whether it has a GPU, how many cores, etc), this process can take some time. I first tested Zed with a [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) program that accepted input from a user and wrote the input to a file. That query took about five minutes to complete.

Yes, Zed can be pretty slow with local LLMs, but it does work and works well. I’ve tested the applications it produced, and they’ve yet to fail me.

You could also open your own project, select Ask from the drop-down to the left of the model selector, ask your question (such as “What’s wrong with my Python code?”), paste your code, and hit Enter on your keyboard.

My only beef with Zed is how slow it is with local LLMs. I’ve used similar tools and found them to be considerably faster. If, however, you have a GPU and a powerful CPU, you might not experience the same thing.

Either way, I find Zed to be a fascinating IDE that might serve you well.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)