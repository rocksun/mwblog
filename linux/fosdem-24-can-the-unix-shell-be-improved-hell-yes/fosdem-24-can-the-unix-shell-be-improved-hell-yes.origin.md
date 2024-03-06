# Can the Unix Shell Be Improved? Hell Yes! (FOSDEM 24)
![Featued image for: Can the Unix Shell Be Improved? Hell Yes! (FOSDEM 24)](https://cdn.thenewstack.io/media/2024/03/a270fc6f-liquid_prompt-1024x703.png)
*Notes from a Feb. 3* [FOSDEM 2024](https://fosdem.org/2024/)talk “Liquid Prompt: yes, we can drastically rethink the design of a shell prompt.” (aw1.126 in your FOSDEM index) [Nojhan](https://github.com/nojhan) (full name) is a [visual designer](http://nojhan.net/) and creator of the [LiquidPrompt](https://github.com/liquidprompt/liquidprompt) alternative shell, “an adaptive prompt for Bash & Zsh” [that promises](https://liquidprompt.readthedocs.io/en/stable/) “a nicely displayed prompt with useful information when you need it.”
Despite
[decades of GUI advances](https://thenewstack.io/cloud-ides-have-a-wow-factor-but-for-developers-its-just-different/), most admins and many devs still use dot-matrix-era command line interfaces, through a shell of some sort. When you know the commands, [ it’s faster](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) and easier to [integrate different tasks](https://thenewstack.io/pipe-how-the-system-call-that-ties-unix-together-came-about/) with a shell.
Today’s command interpreter shells —
[Bash](https://www.gnu.org/software/bash/) being the most widely used since forever — have usability issues though, Nojhan pointed out in his FOSDEM presentation.
They are not very user-friendly: no ergonomics, no feng shui, just endless lines of tiny ASCII text. The shells were not designed to highlight the important bits of what the user is interested in, nor do they, as Nojhan points out, “Follow the state of the work.”
Why, with a screen of undifferentiated text, is it so difficult to find the prompt on these shells?
As it happens, there are plenty of
[alternative shells,](https://thenewstack.io/posh-a-data-aware-shell-for-faster-distributed-text-processing/) or “opinionated prompt systems” all of which have innovative designs to get around these limitations.
Nojhan points not only to his own LiquidPrompt but to others, each with a name more outstanding than the last:
[Starship](https://starship.rs/), [Oh-My-Posh](https://ohmyposh.dev/), [Powerline](https://github.com/b-ryan/powerline-shell), and [Powerlevel10k](https://github.com/romkatv/powerlevel10k) and [Pure](https://github.com/sindresorhus/pure).
Nojhan compared all of the above mentioned in exhaustive
[detail for a blog post](https://github.com/liquidprompt/liquidprompt/wiki/why). And through this considerable analysis, Nojhan concluded LiquidPrompt to be the finest of all of the prompt systems (though he admits each one has its strong points and they all should be considered against specific user requirements, natch).
But however innovative these inventions may all be, will any be sufficiently arresting to move admins and coders from their trusted-if-dreary single-line shells of choice?
## Design Tips for a Better Shell
![](https://cdn.thenewstack.io/media/2024/02/01c5064c-oh-my-popsh-300x195.png)
ohmyposh.dev
“A good prompt should be focused, ” Nojhan said. It should highlight states that are useful for the user. Do you need to know the version numbers of your tools? Maybe not. Some states change more than others, so they don’t need to be reiterated. It all depends on the scope that you need, which should be definable.
Some overlays, such as Oh-My-Posh use color to differentiate different parts of the data. Nojhan derides this as “psychedelic rainbows” and notes they are useless for the colorblind.
But at the same time, you want to avoid “text overload,” or too much text on the screen.
LiquidPrompt, based on Bash, uses a three-line approach. It uses only four colors: black, white and two opposing colors of your choice that are discernable from one another for those with color blindness.
“The important information should be visible” — Nojhan.
Here is the default command line:
And here is the “Powerline” theme:
A three-headed command line is certainly intriguing, but what really sells the package is what you can put into each line. There are all sorts of neat widgets you can embed,
[including](https://liquidprompt.readthedocs.io/en/latest/overview.html): **Current path**: displays where you are, with ” smart path shortening.” **Last command execution time** **Battery level** **Username** **Hostname** **Exit code**: the last command’s exit code if it was an error. **Jobs**: counters for background, sleeping, and detached jobs. **Time** **Available Memory/Disk space** **Remote shell** **Wifi**signal strength.
It can embed version control information for
[git](https://thenewstack.io/tutorial-git-for-absolutely-everyone/) and other repositories, showing the current branch/tags, current state, and statistics on the current commits/edits.
In the presentation, Nojham displays a line that shows the status of a pending git command,
*git st*. The command itself sits, as usual, on the far right of the line.
But the line also shows, before the prompt, the number of changes pending to master branch — 68 additions and 189 removals. It can also warn the user when there other, possibly conflicting, commits pending, all delivered through a clever use of line shades and pointers.
LiquidPrompt can be configured for specific environments, including
[AWS, ](https://aws.amazon.com/?utm_content=inline-mention) [Kubernetes](https://thenewstack.io/kubernetes-1-29-mandala-tests-mutable-pod-resources/) and [Terraform](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/). It even offers customized virtual environments for [Python](https://thenewstack.io/what-is-python/), [Ruby](https://thenewstack.io/why-were-sticking-with-ruby-on-rails-at-gitlab/), [Perl](https://thenewstack.io/getting-started-at-long-last-on-perl-6/), [Docker](https://www.docker.com/?utm_content=inline-mention) and others.
So many features to remember! And so only time will tell if the modern coder brain is prepared for the Tres Hombre command line.
*FOSDEM is not uploading to YouTube this year, but you can view this presentation, and many others, directly from the FOSDEM video collection:* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)