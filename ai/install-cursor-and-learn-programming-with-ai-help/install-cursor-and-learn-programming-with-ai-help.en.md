I’m not a big fan of using AI as a shortcut. On the other hand, I’m perfectly OK using it as a tool for learning. One thing AI is very good at is teaching [programming languages](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/). Yes, you have to be careful to ensure you’re not being misled by mistakes, but with follow-up queries, I’ve found you can almost always get AI to help correct its gaffes.

There are plenty of [AI-powered IDEs](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) on the market now and even terminal applications (such as Warp) that include a powerful AI that can do the very same thing.

One such IDE is called [Cursor](https://cursor.com/en). You can make [Cursor a part of your workflow](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow) and learn how this new IDE [sets the standard for AI-powered programming tools](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance). However, before you get to those stages, you’ll need to get Cursor installed and configured, so it’s usable for helping you interact with AI to learn the art of programming.

Let’s do just that.

## What You’ll Need

Because [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) is my go-to OS (and because it’s rising in popularity), I’m going to demonstrate this process on Pop!\_OS Linux. You can also install this IDE on macOS and Windows by downloading the installer file from the downloads page and going through the standard motions of installing apps on your platform of choice.

If you’re using Linux, the only option is an AppImage, which is nice because it means Cursor will run on any Linux desktop distribution.

## Installing Cursor on Linux

Before you download the Cursor AppImage, I would suggest you install a handy app called Gear Lever, which makes working with AppImages much easier. Gear Lever can create a launcher in your desktop menu so you don’t have to run the AppImage from the command line.

Gear Lever can be installed on any Linux distribution that supports Flatpak with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | flatpak install flathub it.mijorus.gearlever |

Once installed, log out and log back in to make sure the Gear Lever launcher is added to your desktop menu.

Next, download the AppImage from the Cursor [download page](https://cursor.com/downloads).

After the download is finished, open Gear Lever and click the Open button in the top left corner (Figure 1).

[![Figure 1 shows a screenshot of the Gear Lever main window, listing the installed applications.](https://cdn.thenewstack.io/media/2025/08/bef0f5f3-gearlever_ns.jpg)](https://cdn.thenewstack.io/media/2025/08/bef0f5f3-gearlever_ns.jpg)

Figure 1. The Gear Lever main window.

Navigate to the folder housing the Cursor AppImage and select the file. You will then be prompted to move the AppImage to the desktop menu. Do that and you’re ready to launch the app.

## Using Cursor

When you first launch Cursor, you’ll have to walk through a welcome wizard, during which you’ll need to sign up for an account. You can either use an email address or sign up with an account such as [Google](https://cloud.google.com/?utm_content=inline+mention).

Once you’re finished, it’s time to start using Cursor.

Let me walk you through the process of using Cursor’s AI features.

The first thing you must do is select a model. As you’re probably aware, some models require an account (paid even) and/or an API. For your first steps, I would suggest opting for one of the free models. To do this, locate the model drop-down in the query field at the bottom right of the Cursor window. From that drop-down (Figure 2), select a model like deepseek-v3.1 (which can be used for free). After you’ve selected the model you want to use, run your query.

[![Figure 2 is a screenshot of Cursor showing that you can select whatever model you want, but if you choose a paid model, you'll have to use your account and (possibly) an API.](https://cdn.thenewstack.io/media/2025/08/7c5196d3-cursor_llm.jpg)](https://cdn.thenewstack.io/media/2025/08/7c5196d3-cursor_llm.jpg)

Figure 2. You can select whatever model you want, but if you choose a paid model, you’ll have to use your account and (possibly) an API.

For example, let’s have Cursor write a Python program that accepts input from a user for name, address, email and phone. That prompt might look like this:

*Write a Python program that accepts user input for name, address, email and phone and then writes it to a file named users.txt.*

Before you hit Enter, it’s important that you switch from Agent to Ask, which is done via the drop-down to the left of the model selector. If you try to use Agent, you’ll be prompted to sign up for a Pro or Business plan.

Cursor will then begin to write the app, and does so very quickly.

At this point, I attempted to use the Run Without Debugging option and was presented with an error. It wasn’t a Python error but, rather, the inability of Cursor to find the \_\_main\_\_ module in my home directory.

To that end, I copied the code, pasted it into the file *collect\_user\_info.py,* and then ran it with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | python3 collect\_user\_info.py |

Guess what? The code ran perfectly.

I then went back for a follow-up and added (via query):

*Add to the program the ability to accept user input for gender.*

Cursor went to town and generated the new code. I overwrote the original file to see if the new code would work as expected. Blammo — worked like a charm.

At the end of the presented code, Cursor even gives you the steps to run the new Python program.

I’m not saying you should install Cursor and start using it to build all of your applications, but this is a good way for those trying to learn how to code to make that a reality.

Give Cursor a try and see if it doesn’t help with your understanding of whatever programming language you want to learn.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)