# Warp vs. Ghostty: Which Terminal App Meets Your Dev Needs?
![Featued image for: Warp vs. Ghostty: Which Terminal App Meets Your Dev Needs?](https://cdn.thenewstack.io/media/2025/01/b4c24844-zyanya-citlalli-dhv25adxf74-unsplashb-1024x576.jpg)
After the recent [review of Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/) on The New Stack, I thought I’d take a look at it from the point of view of a [Warp user](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/). They are both terminal apps (GUI shells, if you like), although Warp is decidedly more heavyweight in terms of features (including AI). Ghostty, on the other hand, is designed to be a good fit straight out of the box. This post is an introductory appreciation of both terminals in their context.

## Why the Terminal At All?
When I described Warp as “heavyweight,” this can be seen just from the size difference of the apps on my MacBook (300MB vs 50MB):

There does seem to be a cultural gap between developers who virtually “live” inside their terminal — buying fonts they like, running commands and writing scripts as far as possible without using any GUI apps — and developers who spend most of their time in apps and tense up if they have to use a terminal for any reason. I recognize that [Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/) is targeted very much at the former audience, so it has a plethora of configuration options. However, there are reasons for developers to understand and use both styles.

I’m using a MacBook now, but the power of a good terminal is that it will work on as many operating systems and distributions as possible — that is why people still learn how to use vim properly. [Warp is coming to Windows](https://www.warp.dev/windows-terminal) shortly (there is a waiting list), and Ghostty will after version 1. Both cover the major Linux distributions, though I expect Ghostty to do this with more gusto.

Whether we like it or not, computing on any platform is still about files, folders and processes. A good app can hide these basics, but your effectiveness as an engineer will decrease rapidly if you can’t control file permissions or understand long-running tasks.

For example, on my MacBook, I can quickly install a tree (or I could just make the function)…

1 |
brew install tree |
…and then show a directory-only view of one project structure.
Even if I had never heard of [Avalonia](https://thenewstack.io/avalonia-an-open-source-option-for-cross-platform-ui-work/), this tree tells me a great deal about what it is, far more quickly than messing about with Finder on my Mac.

A terminal also becomes a very strong **place of record.** With a terminal that supports multiple tabs, I can effectively show the record of different sessions — and continue any of them as need be.

## Installing Ghostty
I’m not going to look too much into introducing Ghostty, as our [previous post does](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/) that nicely. I’m happy to use Homebrew to install it, but you can use [binaries too](https://ghostty.org/download).

1 |
brew install --cask ghostty |
Here it is being installed from Warp.
Notice that Warp gave us a notification for long-running commands (processes). This is a good example of something done neatly and efficiently on the terminal. If you look at the top, you can see that as the Warp **block** is done (a completed command call and response), it records the time taken.

Ghostty starts off out of the box with no config. However, it should be understood that much shell behavior comes from the shell configuration itself. I have the [zsh shell](https://www.zsh.org/) installed and also [oh-my-zsh](https://ohmyz.sh/) (an [“opinionated prompt system”](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/)), which also has behavior. I fully admit I don’t always know which is responsible for what.

To take a quick check of how Ghostty starts up, we can stream the log as we start Ghostty:

1 |
log stream --level debug --predicate 'subsystem=="com.mitchellh.ghostty"' |
This gives us an idea of the defaults it tries for. I’ve summarised these below:
1234567 |
- known but unimplemented action action=29- found Ghostty resources dir: /Applications/Ghostty.app/Contents/Resources/ghostty- shell integration automatically injected shell=termio.shell_integration.Shell.zsh- known but unimplemented action action=16- started subcommand path=/usr/bin/login pid=89591- received and ignored icon=~- unimplemented OSC command: change_window_icon |
The one I was looking for was that it automatically integrated (injected) my zsh shell, so that is nice. But equally importantly, it doesn’t wobble if it comes across settings it doesn’t understand.
If I do want to set a config, I just press **cmd-,** in the app. In this example, I copied a random config I saw mentioned in a blog:

12345678 |
theme=catppuccin-latte window-height=30 window-width=110 title="Oh, hello" window-title-font-family="MonoLisa Variable" font-family="MonoLisa Variable" font-size=14 font-feature=-ligafont-thicken=true |
I don’t actually have the fonts or the theme installed, but the log we streamed above confirms that Ghostty rejects and moves on without stopping the startup. Even so, it did “thicken” my font and change the window title:
## Sessions, Windows and Tabs
The most common way to use a terminal for a place of record is to open the terminal window with several tabs. Each tab is effectively a separate shell focused on a separate project or process.

On Warp, I just hit the plus sign on the bar for a new tab on the window. In Ghosty, command **⌘**T does the same thing as well:

Ghostty also sets up those quick tabs, **⌘1, ⌘2** and **⌘3** — which is a nice idea. Notice that Ghostty sensibly inherits my git colouring.

In many cases we can leave the terminal on for extended periods, but it is unwise to never think of restoring.

In Warp, after working in a few tabs, I can then name and save the configuration, or launch a named configuration:

If I then quit Warp, reopen and launch, I get the window and tabs — plus I have the history available to help remember what I was doing.

If I want similar behavior in Ghostty, I can add these key-value pairs to the config:

1234 |
...window-save-state = always quit-after-last-window-closed=true |
If I then quit Ghostty with **cmd**–**z**, restarting resets my windows correctly. Interestingly, I have the same session history as on Warp. I think *omz_history* manages this shared history behavior:
Right now, you can’t change the color of a tab in Ghostty, which is a strong way to differentiate the process going on it — I’ve certainly used that in other terminals. It is simple in Warp:

But I’ve already seen a [feature request](https://github.com/ghostty-org/ghostty/issues/2509) for this.

## Conclusion
There are plenty of good terminal apps (e.g., [Kitty](https://sw.kovidgoyal.net/kitty/)) that Ghostty has to compete with, but right now, it is pretty solid. As a developer, you should value any terminal app that will be available on any platform so you can get up and running on new projects in new environments quickly.

Sometimes, you will benefit from the details in Warp (AI in the terminal can aid you in remembering obscure commands and flags), but otherwise, speed and personalization matter. With languages like [Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/) established, there are likely to be more quick apps in production. So keep Warp *and* Ghostty — using each one as appropriate.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)