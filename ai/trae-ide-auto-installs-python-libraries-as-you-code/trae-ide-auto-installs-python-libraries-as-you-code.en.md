You’ve heard all about [AI and IDEs](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/). At this point, they are a dime a dozen, and many of them actually work pretty well.

But what sets them all apart?

A better UI? Better LLMs? Local AI?

I’ve used several of these IDEs, and most often they all do the same things and do them fairly well. When I saw yet another such IDE, I had to find out if there was anything that set it apart from the others.

It only took me about five minutes to figure out what makes [Trae](https://www.trae.ai/) stand out. I’m going to show you what that is by way of creating a [Python](https://thenewstack.io/what-is-python/) app that creates a Dungeons & Dragons character sheet. Yeah, let’s get nerdy.

## How To Get Trae

Before we actually start using it, you might want to know how to install it. Trae can be installed and used for free (although you get more bang for your buck when you pay for a license) on macOS and Windows. There is also a waiting list for the [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) version, which you can sign up for on the [project’s main site](https://www.trae.ai).

I installed Trae on my MacBook Pro running macOS Tahoe, and it installed perfectly. After the installation was completed, I opened Trae and discovered that I did have to sign up for an account. No problem, as it was free.

After signing up for an account and logging in, I was greeted by the Trae AI prompt (**Figure 1**).

[![](https://cdn.thenewstack.io/media/2025/12/3eabde0b-screenshot-2025-12-03-at-2.13.42%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/12/3eabde0b-screenshot-2025-12-03-at-2.13.42%E2%80%AFpm.png)

**Figure 1**: The Trae AI prompt is very easy to figure out.

Alright, it’s time to get our D&D on.

## Using Trae for Nerdy Purposes

With my decision made as to what I wanted Trae to do for me, I typed my prompt, which looked like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Write a Python program that allows a user to create a Dungeons & Dragons character sheet by asking the standard D&D questions and then rolling the required dice to finish creating the character. |

After hitting Enter, Trae went to work. At first, everything ran like any other AI-powered IDE. Out of nowhere, however, Trae gave me a warning that there was a Python library that needed to be installed for the program to run. To my surprise, Trae offered to install it for me.

Sure, Trae, go right ahead.

It worked. In seconds, Trae had the missing library added, without me having to figure out the exact name of the library and use PIP to install it.

Impressive.

This actually happened three times, and each time Trae handled it with ease.

I’m digging this.

It took Trae roughly two minutes to create the program. I copied the resulting text into a file named dnd\_character\_creator.py and ran it with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | python3 dnd\_character\_creator.py |

The program asked me tons of questions related to creating a D&D character

**(Figure 2 –** 

you know the routine). When the interrogation was complete, I could scroll through the terminal to see the results, but that’s all.

[![](https://cdn.thenewstack.io/media/2025/12/2d8ec5f3-screenshot-2025-12-03-at-2.03.16%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/12/2d8ec5f3-screenshot-2025-12-03-at-2.03.16%E2%80%AFpm.png)

**Figure 2:** Running my new D&D Character Creator in a macOS terminal window.

Back to the AI prompt, where I said:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Make this so the results of the character creation are saved to the file dnd\_character\_creator.txt. |

Hit Enter, and Trae went back to work.

Once again, Trae had to install another Python library, which I allowed, and it happened without fail. When Trae finished, I copied the new code into a new file and ran it.

To my curiosity, the program didn’t write the results to a file, so I had to go back to the prompt and inform it that it hadn’t written the results to the file. It ran through the troubleshooting process and worked its magic.

That’s when I realized something: I didn’t need to copy/paste the code because Trae actually wrote it to a file itself.

Nice.

I then changed into the folder /Users/jackwallen/Documents/trae\_projects/DD/ and ran the correct file.

Huzzah! It worked. I now have a Python script to help me create D&D characters.

In the end, what I found that set Trae apart was its ability to install the necessary libraries required to create the program. I didn’t even need to know what libraries were necessary for the Python program, which was a big help.

Understand that I only scratched the surface of using Trae, but even just using it without getting too deep into the woods, the IDE really impressed me.

What other features does Trae offer?

* AI is integrated into the entire development process.
* Autonomous shipping with Trae Solo.
* Multiple agents for troubleshooting.
* Ability to create your own agent team.
* Structured “Builder mode” for complex projects
* Multimodal capabilities like image-to-code generation.
* Intelligent code completion.
* Conversational chat mode for coding help.
* Integrated debugging and testing.
* VS Code extension compatibility.

As I mentioned, Trae can be used for free, but that plan is limited to:

* 10 Fast requests and 50 Slow requests of Premium models/month
* 1000 Requests of Advanced models/month
* 5000 Autocomplete/month

If you upgrade to the paid plan $10/month (first month only $3), you get:

* 600 Fast requests and unlimited Slow requests of Premium models/month
* 300 bonus Fast request/month (limited-time offer)
* Unlimited Requests of Advanced models
* Unlimited Autocomplete

If someone like me can create complex Python programs by way of AI queries and follow-ups for troubleshooting, anyone can.

Give Trae a try and see if it doesn’t become your new favorite [AI-powered IDE](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)