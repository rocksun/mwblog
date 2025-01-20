# Ghostty Will Get You Excited About Using a Terminal Again
![Featued image for: Ghostty Will Get You Excited About Using a Terminal Again](https://cdn.thenewstack.io/media/2025/01/03abe217-ghostty-1024x768.jpg)
I’ve used so many terminal apps over the years that I’ve lost track of what they are, were or will be. To date, my favorite terminal app is [Warp](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/), but there’s another hiding in the shadows, ready to jump out and scare me into switching.

That new [terminal app](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) is called [Ghostty](https://ghostty.org), and it was created by [Mitchell Hashimoto](https://thenewstack.io/hashicorps-mitchell-hashimoto-on-when-to-step-down-to-the-job-you-love/), [co-founder](https://thenewstack.io/mitchell-hashimotos-move-from-cto-garners-r-e-s-p-e-c-t/) of [ HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention). This new terminal is lightweight, fast, feature-rich and cross-platform.

Ghostty does things a bit differently. Where some terminal apps have a GUI feature for configuration, this one uses a flat text file that is loaded upon launch (or reloaded manually, when you make changes). For that reason alone, Ghostty isn’t the ideal terminal for those just getting started with the command line. Instead, Ghostty is aimed at those with plenty of experience.

That’s not to say you can’t use Ghostty with the default minimal configuration; you certainly can, but you’d be missing out on a lot of features.

Speaking of features, what makes Ghostty so special? Where do we start?

- Platform-native GUI.
- Written in Zig and uses GTK4/libawaita on
[Linux](https://thenewstack.io/introduction-to-linux-operating-system)and on macOS; it was written in Swift, which means Ghostty is 100% native to your OS. - Supports multiple windows, tabs and split panes.
- GPU-accelerated rendering.
- 100 built-in themes and supports custom themes as well.
- Regular keyboard shortcuts.
- Shell integration (for bash, zsh, fish and elvish).
- Prompt redrawing on resize.
- Working directory reporting.
- Detection of active processes.
- Programmatic italicization.
- Support for ligatures and variable fonts.
- Grapheme clustering
Currently, Ghostty is installable on Arch Linux (and its derivatives), macOS and from source. I installed Ghostty on both macOS and Arch Linux and found the installation process to be quite simple. On macOS, just download the .dmg package, double-click on it, and then drag the Ghostty icon to the Applications folder.

With Arch Linux, the installation of Ghostty can be done from the standard repositories with pacman, like so:

1 |
sudo pacman -S ghostty |
Once installed, open Ghostty from your desktop menu, and you can immediately start using it as your terminal emulator.
## Configuring Ghostty
This is where things get a bit tricky, especially for those who’ve never configured anything via text file. Let me show you how to customize Ghostty.

The customizations are done the same way you might configure anything on Linux. First off, the configuration file is found in one of the following locations:

- Linux –
`$HOME/.config/ghostty/config`
- macOS –
`$HOME/Library/Application\ Support/com.mitchellh.ghostty/config`
With Linux, you have to configure Ghostty through the configuration file and your favorite text editor. On macOS, you can click *File > Settings* to open a GUI text editor and make the changes you need. Note that, by default, the configuration file is empty, so you’re starting from square 0.

For example, say you want to change the background and foreground (text) color of Ghostty. Let’s say you want a background of Rose Pink and a foreground of black. Those configurations would be:

12 |
background = #ff66ccforeground = #000000 |
Save those options and then click the Ghostty *menu button > Reload Configuratio*n. The Ghostty terminal app should now reflect your changes (Figure 1).
-
Figure 1: It’s much easier to configure Ghostty than you might think.

Let’s say you want to create a keyboard shortcut to split the current Ghostty window into two panes; for that, you could bind the action to the Ctrl+d shortcut like so:

1 |
keybind = ctrl+d=new_split:right |
You can also configure the font family used in Ghostty. To do that, you’ll want to first list the available fonts with the command:
1 |
ghostty +list-fonts |
You don’t get any visual cues as to what each font looks like, so you’ll either have to just guess or run a search on the font name you think might work. For example, you might want to use the Hack Bold font, which would be configured like this:
Or, you could apply one of the 100 themes available like this:

First, list all of the themes with the command ghostty +list-themes, which actually gives you a preview of what each theme looks like (Figure 2).

-
Figure 2: The available themes for Ghostty.

Once you’ve found the theme you want, you can configure it in the config file like so:

1 |
theme = Unikitty |
Another cool trick is you can configure the Ghostty window title bar to use the same theme color as the background with (Figure 3):
1 |
window-theme = ghostty |
-
Figure 3: Adding themes to Ghostty can be a lot of fun.

I will say this regarding themes: For some reason, themes were not working on the Arch Linux installation, but they were on the macOS side of things.

There is an entire list of Ghostty configuration options you can view [here](https://ghostty.org/docs/config/reference). I recommend that you scroll through those options and see if there’s anything that catches your attention.

One thing I would advise with the configurations: Open a separate terminal window app to edit the config file. That way, if something goes wrong, you can easily change it and then reload the configuration file from the Ghostty menu.

Although Ghostty is still in the early stages of development, it’s already a fantastic terminal app that shows promise.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)