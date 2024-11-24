# Warp Is a Power User’s Dream Terminal for Linux
![Featued image for: Warp Is a Power User’s Dream Terminal for Linux](https://cdn.thenewstack.io/media/2024/10/ad5a3912-warpterminal-1024x719.jpg)
I’ve been using [Linux](https://thenewstack.io/learning-linux-start-here/) since the late 90s, which means very early on I had to depend on the[ terminal window](https://thenewstack.io/tutorial-your-terminal-og-style-no-libs-or-plugins/) (because the GUIs back then were not what they are now). I’m perfectly comfortable with the command line and can run most Linux commands in my sleep.

But not all terminal applications are created equal. Sure, many [Linux terminal](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/) apps offer profiles and other simple features, but when you want real power and options, where do you turn?

For the past year or so, I’ve made the switch from the built-in terminal apps for a new paradigm called [Warp](https://www.warp.dev). This [app was built](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) with Rust so it’s designed for speed. However, speed isn’t the really impressive piece of the Warp puzzle because there’s so much more to the app.

There’s Agent Mode, which leans heavily into AI so you can use plain English to accomplish multistep workflows. For example, you could type “I want to update Ubuntu” and Warp will return with the step-by-step instructions for doing so and even automatically add the initial command to the prompt, so all you have to do is hit Enter on your keyboard.

You can even use this feature for your current development projects. You might want to find out which pull requests caused a merge conflict, so you could type, “Find out which PR caused this merge conflict using the GitHub CLI.”

You could even use it for troubleshooting, such as: “Why can’t I SSH into my server?” Warp will respond with advice on how to start troubleshooting.

There’s also Warp Drive, which adds a secure space to save and share interactive notebooks and reusable workflows. For example, you could create a new workflow for updating and upgrading your Ubuntu machine by adding a notebook with the command `sudo apt-get update && sudo apt-get upgrade -y`
.

Once you’ve created the Workflow, all you have to do is select it from Warp Drive and hit Enter on your keyboard. The Workflow will execute and you’re good to go. Warp Drive also allows you to save Notebooks, which can contain just about any text you want (be it commands, code snippets, notes, or anything). You can also set environment variables within Warp Drive and even create folders to house related content.

Warp AI is another feature that is decidedly helpful. Say, for instance, you need to run a command and you’re not sure what the command does. Type the command in the Warp Terminal CLI, highlight the command, and use the Ctrl+` keyboard command and Warp’s AI will explain what the command does.

-
Warp AI makes it easy to understand what a command does.

On top of these features, you can also customize the look of Warp, create a custom prompt, pin the command line to the top or bottom of the window, and even work with a transparent background (for added coolness). Warp uses [modern IDE-like editing](https://thenewstack.io/best-open-source-ides/) (so you can use both your mouse and your cursor), uses [Vim keybindings](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/), works with tab auto-completion, and automatically catches types or missing parameters in your commands.

In other words, Warp is the Linux terminal on steroids.

Of course, there’s also Team Drive, Session Sharing, and Block Sharing, which are features not found in the free version.

Speaking of which, the free version of Warp Drive (which is available for Linux and macOS — with a version for Windows coming soon), limits you to 100 AI requests per user per month, only a personal Warp Drive, up to three notebooks, and 10 workflows in a shared drive, all offline features and free support via public forums. The Pro version ($15/user/month) adds up to 1,000 AI requests per user per month and private email support. The Tem version ($22/user/month) adds unlimited AI requests, unlimited shared Notebooks and Workflows in Warp Drive, and real-time session sharing. The Enterprise version (custom pricing available) allows you to use your own LLM and adds, OpenAI zero data retention policy, SAML-based SSO, E2E encryption, and a dedicated account manager.

## Installing Warp on Linux
Installing Warp terminal on Linux is simple. All you have to do is download either the DEB (for Ubuntu-based distributions or RPM file (for Fedora-based distributions), open your default terminal window, and run one of the following commands:

- Ubuntu –
`sudo dpkg -i warp-terminal*.deb`
- Fedora – sudo rpm -i warp-terminal*.rpm
For macOS, download the .dmg file and install it as you would any app for the platform. As for the Windows version, you’ll want to [sign up for the waitlist](https://www.warp.dev/windows-terminal) to be notified as soon as it becomes available.

As I said, I’ve been using Warp Terminal for about a year now and I cannot imagine going back to the boring, featureless, default terminal apps found in most [Linux distributions](https://thenewstack.io/choosing-a-linux-distribution/). The developers behind Warp have created the single best terminal application on the market and any Linux (or macOS) user would be remiss if they didn’t give it a try.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)