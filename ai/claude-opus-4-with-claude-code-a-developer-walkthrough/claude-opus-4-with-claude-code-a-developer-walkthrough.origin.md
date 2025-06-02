# Claude Opus 4 With Claude Code: A Developer Walkthrough
![Featued image for: Claude Opus 4 With Claude Code: A Developer Walkthrough](https://cdn.thenewstack.io/media/2025/05/8cc21d33-kamran-abdullayev-ik1duxu9aae-unsplashb-1024x576.jpg)
Claude Opus 4 has already grabbed [quite a bit of attention](https://www.bbc.co.uk/news/articles/cpqeng9d20go) in the short time it has been public, and in some ways I feel I’m a little slow to the party. I was reading a very detailed breakdown that [Federico Viticci](https://www.linkedin.com/in/federicoviticci/) [did using Claude 4](https://www.macstories.net/stories/early-impressions-of-claude-opus-4-and-using-tools-with-extended-thinking/) on the web to sort through his emails. I know he likes detail, but I was slightly worried about the 200-line prompt file he was maintaining. (I later understood that Claude writes a lot of notes into its own file.)

I was looking to use [Claude Opus 4](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) with Claude Code [(which I tried out last month)](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) and had a specific idea of what I wanted to apply its agentic abilities to. I was working with a Rails app that was mainly doing CRUD management, but I wanted to apply [Bootstrap](https://getbootstrap.com/) CSS to improve its styling. For me, this is a good example of suitable work for a large language model (LLM) — if the CSS is “wrong,” there should be no fatalities.

What I liked about Claude Code is that it maintains a flow separate from your IDE, so you are not considering code file by file. As styling has to be applied to a number of view files irrespective of their function, this makes sense.

I was hoping to give the minimum guidance I reasonably could (because I’m the human) and just apply further detail to improve areas as appropriate. When I do use LLM tooling, I certainly don’t let it rampage through my code, but to show off agentic abilities I will have to “just let go” — that is, let it work on the project as a whole.

Note: Since Claude Code works inside your terminal, I am using [Warp](https://thenewstack.io/developer-review-of-warp-for-windows-an-ai-terminal-app/) — my terminal app of choice — for the rest of this article.

## Setting up the Project
First, I’ll get an old version of the Rails CRUD project and put it in a fresh directory for Claude to work on. The project is for an upcoming game I’m developing, and is used to organize conversations that various characters can make.

I was initially puzzled by how to download code based on a particular commit within Bitbucket, but fortunately, Stack Overflow showed a simple [REST](https://www.codecademy.com/article/what-is-rest) pattern that worked:

`https://bitbucket.org/<username>/<reponame>/get/<commitCODE>.tar.gz`
I then untarred this into its own directory:

Starting a Rails server, I checked the state of my old example code:

So I’m in need of some styling help.

## Setting up Claude Code
Now let’s get the latest Claude Code. I’ve already [installed it once](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/), but I ran this in the command line to ensure it was up-to-date:

1 |
> npm install -g @anthropic-ai/claude-code |
The important thing before starting was to ensure it started with the updated Opus 4 model:
1 |
> claude --model claude-opus-4-20250514 |
As before, it asks if I can trust the code in the folder, which of course, I do. We then get the important reference:
So I know we have the right model, and it’s looking at the right project.

I also want it to create the prompt file (CLAUDE.md) so that I can do the oh-so-important and mysterious prompt engineering:

It’s actually when firing off this command that it *gets busy* analyzing my code.

It kept updating and amending a “todo” list from its initiation in order to track what I asked, as well as making tasks for itself while scanning:

In fact, it asked quite a few times before just writing the file. Unlike most developers, it’s definitely weighted towards asking permission — as opposed to begging for forgiveness later.

As CLAUDE.md is a Markdown file, Warp allowed me to view it in another tab (not running Claude Code):

It records many basic relationships and understands the Rails setup. The idea is that it can check these before starting new tasks.

It turns out I can use the `#`
key to give Claude an instruction, which it will automatically incorporate into the prompt file. The first time I did this (and then subsequently), it checked what context it should check into:

This shows that Claude 4 differentiates between local project settings and global settings.

## Instructing Claude
I started adding instructions with the `#`
key, but forgot that it would also just action that command immediately as well. So after telling it what I meant by Bootstrap (with the URL to Bootstrap 5), I only got around to adding:

- Apply Bootstrap color utilities to improve visual hierarchy
- Update buttons with Bootstrap button classes
…before the agentic powers whipped into full effect. I meant to start by restricting Claude to editing only files in the views directory, but it knew all this already.

It suggested a bunch of changes to the main layout — which I admit I didn’t quite understand — and it also wrote some template code:

When I let it make the changes, the sidebar was styled in a much nicer way:

So, I thought I would let it continue. But for me, this was the most important thing:

It understood that part of the front page had two separate functional parts. It did not just assume that this was a page and treat everything the same way. The risk was that it would get a bit lost with the Ruby template code, but it generally left that alone. In fact, it did a great job making the display neater, but only by extending some of my own ideas.

Meanwhile, it showed me every file it changed, even though I could have just let it carry on by itself.

It was now getting nearer to the section of code I’ve displayed here, so I can show you how it updated the links to buttons:

Fortunately (for this post), it did not turn the create links into buttons, so I will get the chance to instruct it again. I let it finish the uplift.

At the end, it summarized all the changes it has made for all the views in the app and stated: “The application now has a modern, consistent Bootstrap 5.3 design with improved visual hierarchy, better spacing, and professional styling throughout.”

However, when I asked for the last change, I got the dreaded message:

So I had blown my $6. I ~~fed my addiction~~ continued funding my account to finish the job. And after taking more money, it continued. Look how it has taken my description of the new path and codified it properly:

It edited five other files, including the one we’re looking at:

Here we can see that it did precisely the right thing. Also note the little icons it added to the sidebar:

## Conclusion
This is the first time I have totally underestimated an LLM’s capabilities before using it. It really didn’t put a foot wrong in this task, even though I made a mistake in not putting the right restrictions on it. Claude totally understood this simple CRUD interface from Rails, as well as my intentions.

It’s true to say this was “just” styling, but Claude had to move around quite a lot of template code in the Embedded Ruby (ERB) files. So far, this is the most premium experience I’ve had with an LLM — and for the price of an espresso in London. And with Claude doing the work, perhaps I didn’t even need that coffee.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)