# My 5 Favorite Command Line Tools
![Featued image for: My 5 Favorite Command Line Tools](https://cdn.thenewstack.io/media/2024/10/28e31613-5favoritecommandlinetools-1024x576.jpg)
Whether you’re new to the [Linux command line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) or have been using it for years (or maybe even decades?), I’d like to show you my top five command-line interface (CLI) tools: SDKMAN, eza, ffmpeg, queue and find. You’ll be more productive and feel like a CLI rockstar after reading this article.

Open a terminal and let’s get to know these tools!

## 1. SDKMAN for Managing JDKs
SDKMAN, which stands for “Software Development Kit Manager,” is a tool for managing multiple SDKs and switching between them easily. Let’s use it to install and manage the Java Development Kit ([JDK](https://thenewstack.io/end-of-the-road-for-javafx-in-jdk-8-keeping-your-apps-alive/)).

To install it, just follow the simple instructions on the [SDKMAN installation page](https://sdkman.io/install/), whether you’re on Linux, MacOS or Windows. I’ll install the free Azul Zulu builds, which is Azul’s completely free build of OpenJDK.

You can list all the available JDKs by typing this from the command line:

1 |
sdk list java |
This will produce output like this:
Since [Java 23 just came out](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/), let’s install it! This is simple with SDKMAN; just issue the command:

1 |
sdk install java 23-zulu |
And *voilà*, you now have Java 23 installed. You can check that it’s installed and is the default build with the command `java -version`
:

You might want to install an older version of Java, and that’s easy enough. For example, you want to install Java 17? Punch this into the console:

1 |
sdk install java 17.0.12-zulu |
It will ask if you want to set it as the default — that’s up to you. You can easily switch versions on the fly by issuing this command; it will set the JDK you specify within the command as the one that will be used in that shell session:
1 |
sdk use java sdk use java 17.0.12-zulu |
## 2. A Better ls: eza
The `ls`
command is great for listing files, but I prefer to use `eza`
because it color codes the output and knows about [symlinks](https://en.wikipedia.org/wiki/Symbolic_link) and [Git](https://roadmap.sh/git-github), among other things.

For example, you can specify a tree depth, and it will output all files to that depth:

1 |
eza -l –TL3 |
Often, I want to see the directories at the top and the files in a directory after that. You can do that with `eza`
:

1 |
eza -al --group-directories-first |
I use this so often, I created an alias for it:

1 |
alias ll="eza -al --group-directories-first" |
So now I just type `ll`
and it formats and orders the output so that it’s faster for me to find something.
## 3. A/V Swiss Army Knife: ffmpeg
The `ffmpeg`
tool is a comprehensive command for working with audio and video files. It can do anything: resize video files, output the audio from a video file to MP3, convert from different video formats, and so much more. There are some great tutorials and books on`ffmpeg`
, but I’d like to show you an example of how to resize a 1080p video file to 480p.

1 |
ffmpeg -i ./AltantaTimeLapse.mp4 -vf scale=-1:480 -c:v libx264 -crf 0 -preset veryslow -c:a copy AltantaTimeLapse-480.mp4 |
The scale option tells `ffmpeg`
to resize and preserve the aspect ratio (as I’m only providing one dimension: `scale=-1:480`
.) It’s also telling ffmpeg to copy the audio, as I don’t need to change that.
Here’s both the original and downsized video file on my desktop so you can see the difference:

If you’d like to learn more, I recommend this in-depth [tutorial on ffmpeg](https://img.ly/blog/ultimate-guide-to-ffmpeg/).

## 4. Multi-Step Job Processing with Pueue
The `pueue`
command is short for “process a queue” — or as its [website says](https://github.com/Nukesor/pueue), “Pueue is a command-line task management tool for sequential and parallel execution of long-running tasks.” It’s a super useful command for when you don’t want to sit at your computer to run a series of commands that take a lot of time. Or just as a way to automate a bunch of commands, so you can get that cup of Java and take a break.

We just used `ffmpeg`
to process a video file, which will take some time (and depending on the length or resolution of the video, it could take a *long* time). Let’s do these things with `pueue`
, so we don’t need to babysit our task:

- Process the files (resize).
- Move them to a folder called Finished using the
`find`
command.
Install `pueue`
using your system’s package manager, then make sure the daemon for it is running:

1 |
pueued –d |
Now queue up the `ffmpeg`
command:

1 |
pueue add -- ffmpeg -i ./AtlantaTimeLapse.mp4 -vf scale=-1:480 -c:v libx264 -crf 0 -preset veryslow -c:a copy AtlantaTimeLapse-480.mp4 |
Also queue the command to move the files into a folder called Finished:
1 |
pueue add -- find . -type f -name "*480p*" -exec mv {} finished/ |
Type the command `pueue`
to see what’s in the queue and its status:
## 5. Don’t Hunt; Use Find
The Unix `find`
command is a great tool to save time when you’re looking for files. You can even use it to run a command against the files that are found. You can find files by type, name, attribute, etc. We used the `find`
command above to move processed files:

1 |
find . -type f -name "*480p*" -exec mv {} finished/ |
The `.`
says to find files starting in this directory.
Let’s look at the options.

- Find file only (no directories):
`-type f`
- Find files with 480p in the filename:
`-name "*480p*"`
- Execute a command on found files:
`-exec mv {} finished`
The `exec`
flag says, “Execute the `mv`
command for each thing the `find`
command finds.” The `{}`
are used to substitute the file or directory found.

There are a ton of options, and I recommend [this tutorial for getting started](https://www.softwaretestinghelp.com/find-command-in-unix/).

## Conclusion
We’ve stepped through five command-line tools I find invaluable for day-to-day work when developing software. I hope you were able to add a few new tools to your toolbelt!

** Learn more by registering for **.
[All Things Open 2024](https://thenewstack.io/event/all-things-open-2024/), where you can hear
[Pratik](https://2024.allthingsopen.org/speakers/pratik-patel)and other open source experts share their insights and knowledge
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)