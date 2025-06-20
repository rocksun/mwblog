Have you already started your programming journey? Or maybe you’ve just recently started it, and you’re finding learning your first [programming language](https://thenewstack.io/programming-languages/) (or a new one) to be a bit more challenging than you thought.

You’ve read books, studied online tutorials and even sought out assistance from others, but nothing seems to be sticking.

What if there was another way? What if there were a way that could not only help you to understand the concepts, but even show you specific examples of what you’re trying to do?

That way is AI.

I know, I know … you’re probably shaking your head at the thought of using AI to write code because that feels like cheating. But what if it wasn’t? What if, instead of using it to just do the work for you, you used it as a tool to help get you up to speed on what might otherwise be a daunting task?

I’ve written about AI quite a bit and have some pretty strong feelings about it. I strongly believe that AI shouldn’t be used for the purpose of creating, but when AI is used for research or as a learning tool, I’m all for it.

I’ve tested a few different AI solutions for these purposes, and when it comes to learning about coding, one has stood out above the rest, and that is the AI found in [Warp Terminal](https://www.warp.dev/).

## Why Warp Terminal?

First off, [Warp is a terminal app](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/), so it already has an advantage because it was developed for those who use a terminal application for just about anything. And with a built-in AI that can also help you learn [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) commands (because it allows you to type in human-readable language and then turn that language into a command), it already has a leg up on other AI solutions.

Another thing about Warp Terminal is that it’s not just about writing the code you request. With Warp Terminal, you can query the AI to create a program and have it save the code to a file. Then it will show you how (if necessary) to compile and run the program.

It really is that good and easy.

Let me demonstrate with a simple Hello, World app written in [C++](https://thenewstack.io/introduction-to-c-programming-language/).

## How To Use Warp Terminal To Write Your First Piece of Code

After you’ve installed Warp Terminal (available for Linux and Windows), open the app from your desktop menu, and you should see a fairly straightforward prompt. But what happens when you type the following:

All of a sudden, things change, and Warp goes to work. It will eventually present you with the code for the app (Figure 1).

![](https://cdn.thenewstack.io/media/2025/06/96a7a20f-warpapp1.jpg)

Figure 1. A basic C++ app, created by Warp Terminal.

You should also see a row of options for Cancel (Ctrl+C), Refine (R), Edit (E) and Apply Changes (Enter). If you hit Enter, Warp will use the code it created and create a file for it (aptly named, hello\_world.cpp). When that finishes, it will then present you with the compile command (g++ hello\_world.cpp) and run command (./hello\_world).

If you look in the current working directory, you’ll see all the files required to compile and run the code, and all you had to do was tell Warp to create it.

But what happens if you don’t understand how the code works? Warp’s AI can help you with that as well.

Let’s take a look at the Hello, World file Warp created, which looks like this:

What if you’re new to C++ and have no idea what the above means? Let’s ask Warp’s AI. For example:

The response looks like this:

It continues on with the description, but you get the idea.

You could then go line by line, asking what each bit of code does, so you have a better understanding of how the C++ Hello, World app works.

You could also go a more challenging route.

This time, I asked Warp to create a graphical user interface (GUI) app in C++ for Warp Terminal. Almost immediately, Warp discovered that I didn’t have the necessary GUI toolkit installed and, instead, opted to go a different route: – X11 (as opposed to the gtk4 libraries). Warp then presented the necessary code. I hit Enter to apply the changes (which had to be done several times as Warp found and solved some issues), and then Warp presented me with the next steps, which involved the installation of libgtk-3-dev and then the compile and run commands.

It worked.

I could also open the file Warp created for the app and ask it to explain what each line does, so I can start to better understand how C++ works.

This can be done for nearly any programming language, such as [Python](https://thenewstack.io/python/), [JavaScript](https://thenewstack.io/javascript/), [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/), [Go](https://thenewstack.io/introduction-to-go-programming-language/) … you name it.

Although the idea of letting AI do the work for you doesn’t sit right with me, for getting up to speed with a language so that I can do the work correctly, I’m all for it. AI is a very valuable tool that can be used for good, and, as far as I’m concerned, letting it help you learn the art of programming falls under that category.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)