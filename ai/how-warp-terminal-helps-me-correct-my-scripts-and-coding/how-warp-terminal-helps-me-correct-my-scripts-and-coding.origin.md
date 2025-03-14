# How Warp Terminal Helps Me Correct My Scripts and Coding
![Featued image for: How Warp Terminal Helps Me Correct My Scripts and Coding](https://cdn.thenewstack.io/media/2025/03/b1b62fca-chris-briggs-u4t-e-ktgmg-unsplash-1-1024x683.jpg)
Every so often, technology really seriously and magically impresses me, which is no easy feat these days. After all, we’ve pretty much seen everything the tech industry has to offer.

Or so we think.

As you know, technology is advancing at a breakneck speed, so every day I wake up thinking, “What gem am I going to find today?”

A while back, I installed [Warp terminal](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/) on both [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) and [macOS](https://thenewstack.io/the-best-macos-terminal-emulation-programs-for-developers/) (it’s also available for Windows, but I don’t use Microsoft’s OS) and found it to be an impressive piece of software, so much so that it has replaced my default terminal apps on both of the operating systems I use.

Warp is impressive. Very impressive.

However… (this is a good “however”) the other day I happened upon a feature found in Warp that blew me away.

Let me set the scene.

I was working on a bash script that would generate random passwords. The goal was to use the *pwgen* command (because I was writing an article about the command) and I wanted to show how it could be used both from the [CLI](https://thenewstack.io/mongodb-atlas-finally-gets-a-command-line-interface/) and from within a script.

I wrote the script, which looked like this:


I gave the script executable permissions with the command:

*chmod u+x pw.sh*
When I ran the script in Warp, I received the following errors:


You’d have thought that would be an easy fix… just follow the errors and fix the issues. No matter what I did, I couldn’t get the script to run. Instead of continually pulling out my hair, I decided to give Warp’s AI a try and see if it could fix the issue.

After I ran the script, I noticed that not only did Warp spot the errors, it also offered to Fix the syntax issues (**Figure 1**).

**Figure 1**
![](https://cdn.thenewstack.io/media/2025/03/b2082cf4-warpai1.jpg)
Warp is smarter than I thought.

I’m game.

I hit Ctrl+Shift+Enter and waited to see what the app would do.

Warp went to work and explained the problem. Once it figured out the issue (it took less than a minute), it displayed the fixed script and gave me the option to Cancel, Refine, Edit, or Apply Changes. I hit Enter to allow Warp to apply the changes to my script. After running the fix, it described what it did, and gave me back my prompt.

The big test was upon me. I ran the edited script to see what would happen and, guess what, it found more errors. Once more unto the breach with another Ctrl+Shift+Enter.

I gave Warp another go at fixing the new problems it injected into my script, hoping this time all would work.

After it went through its process, I hit Enter to apply the changes and ran the script again.

Bingo!

The output of the script was exactly as expected:

*
*Needless to say, I was impressed.
I decided to try something a bit different. This time I wrote a [Python app](https://thenewstack.io/how-to-use-pyscript-to-create-python-web-apps/) that accepted user input for age, height, weight, gender expression, and age and appended it to a file. The original script was:


After running the script, I wound up with a metric ton of errors, so I hit Ctrl+Shift+Enter to have Warp fix the problem.

It should come as no surprise that Warp’s AI did the trick. This time, at the end of Warp’s “big think,” it offered to run the program for me. I hit enter and the script ran. Guess what? Warp did it. On top of that, Warp noticed I had a file in my [PYTHON](https://thenewstack.io/python/) directory named random.py which could cause issues in scripts that require the random modules. I renamed that script and all was well.

Impressive, to say the least.

If you’re learning a new language and your debugging skills are about as good as mine, I would highly recommend giving Warp terminal a go to see if it can fix the problems and help you learn along the way.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)