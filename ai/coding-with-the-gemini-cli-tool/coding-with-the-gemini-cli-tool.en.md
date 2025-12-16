Some time ago, [Google](https://cloud.google.com/?utm_content=inline+mention) released the [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) (Command Line Interface) tool that is pretty impressive.

Unlike many [AI tools](https://thenewstack.io/the-top-ai-tool-for-devs-isnt-github-copilot-new-report-finds/), the Gemini CLI app is installed locally, so you don’t have to worry about your queries (or the results thereof) being used for any nefarious purposes.

Currently, Gemini CLI features:

* Fully open source, allowing users to inspect and contribute to the code.
* Powered by Gemini 2.5 Pro.
* Free tier allows 60 requests per minute and 1,000 requests per day with a personal Google account.
* Includes tools for Google Search, file operations, and shell commands for enhanced functionality.
* Supports custom integrations and enhances the AI’s ability to understand context.

As you’ve probably assumed, based on the name, Gemini CLI is a command-line-only tool, so there’s no GUI. If you’re not comfortable using the command line, then Gemini CLI is not for you.

If, on the other hand, you’re at home in a terminal window, Gemini CLI can easily become yet another tool for your programming journey. You can use Gemini CLI to help you learn how to use a new programming language, how to up your skills with a certain language, and much more.

Let’s find out how to install this handy tool and then how to use it to learn a little something about [JavaScript](https://thenewstack.io/introduction-to-javascript/).

Shall we?

## What You’ll Need

To make this work, you’ll need any operating system that supports [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) and NPM. I’ll be demonstrating the installation on Zorin OS, which is based on [Ubuntu Linux](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/). On [Linux](https://thenewstack.io/introduction-to-linux-operating-system/), you’ll also need a user with sudo privileges.

Let’s get busy.

## Installing the Prerequisites

Before you can install Gemini CLI, you have to first install [Node.js](http://node.js) and NPM. To do that, we’ll run the following commands:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install nodejs npm -y |

Once that’s taken care of, you’re ready to install Gemini CLI.

## Installing Gemini CLI

You can install Gemini CLI with a single command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo npm install -g @google/gemini-cli |

It’ll take a minute or two to finish, but it should go off without a hitch.

You’re not done yet.

You have to authenticate Gemini CLI with your personal Google account. To do that, open your default web browser and make sure you’re logged into your Google account. Once you’ve done that, go back to the terminal window and issue the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

If you receive an error, it means your distribution installed an older version of Node.js. To resolve that issue, do the following:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -fsSL https://deb.nodesource.com/setup\_23.x -o nodesource\_setup.sh |
|  | sudo -E bash nodesource\_setup.sh |
|  | sudo apt-get install nodejs -y |

Once you’ve taken care of that, re-run the

*gemini*

command. You will then be prompted to select an authentication method (

**Figure 1**

). Make sure Login with Google is selected and hit Enter on your keyboard.

[![](https://cdn.thenewstack.io/media/2025/12/c0f5d803-geminicli1.jpg)](https://cdn.thenewstack.io/media/2025/12/c0f5d803-geminicli1.jpg)

**Figure 1:** If you’d prefer, you can authenticate with a Gemini API key or Vertex AI.

When your default web browser opens, if you’ve not already logged into your Google account, do so now.

When prompted, click Sign In, and you’ll be informed that the authentication was successful, at which point you can close the browser to find that Gemini CLI is ready for your first query.

Don’t query yet.

Close Gemini by hitting the Ctrl+c key combination twice.

## Let’s Learn Something About JavaScript

Using the terminal window, create a new project directory with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Change into that directory with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Now, run the

*gemini*

command again. The difference this time is that you’re working in a specific directory (as opposed to your home directory).

From the main Gemini window (Figure 2), let’s issue the following query:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | How do I create a drop-down list in JavaScript? |

![](https://cdn.thenewstack.io/media/2025/12/91827f73-gemini2.jpg)

**Figure 2:** Gemini CLI is ready for your first query.

Hit Enter, and Gemini will go to work.

As it works, it’ll most likely prompt you to okay certain tasks, or it’ll prompt you to allow it to create files (**Figure 3**).

[![](https://cdn.thenewstack.io/media/2025/12/a59fb739-gemini3.jpg)](https://cdn.thenewstack.io/media/2025/12/a59fb739-gemini3.jpg)

**Figure 3:** Resistance is futile, so give it permission to create the files.

Continue allowing Gemini to do what it needs as it does what we’ve asked of it.

After a few minutes, Gemini informed me to open the file index.html with my web browser to see the drop-downs in action (**Figure 4**).

[![](https://cdn.thenewstack.io/media/2025/12/e2cc7f31-gemini4.jpg)](https://cdn.thenewstack.io/media/2025/12/e2cc7f31-gemini4.jpg)

**Figure 4:** Our example drop-downs were successfully created.

Okay, but how do we learn from this? Well, if you go back to your JS\_PROJECT directory, you’ll see three files:

Or, you could run a follow-up like this:

*This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | Explain to me what you did to create the dropdowns. |*

Gemini CLI will then walk you through what it did **(Figure** **5**); either that, or it’ll inform you that you’ve either exhausted the resources of your free tier or the service is too busy. If that’s the case, run the query again and see if it works.

[![](https://cdn.thenewstack.io/media/2025/12/03c84e71-gemini5.jpg)](https://cdn.thenewstack.io/media/2025/12/03c84e71-gemini5.jpg)

**Figure 5:**Let Gemini CLI explain to you how it created the drop-downs.

Fun times.

And that, my friends, is how you can install and use the Gemini CLI tool to learn something new or hone your current skills.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)