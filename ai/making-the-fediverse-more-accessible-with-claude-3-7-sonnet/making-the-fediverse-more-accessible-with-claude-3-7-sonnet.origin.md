# Making the Fediverse More Accessible With Claude 3.7 Sonnet
![Featued image for: Making the Fediverse More Accessible With Claude 3.7 Sonnet](https://cdn.thenewstack.io/media/2025/03/86acb995-joshua-earle-jypu1ftddwk-unsplashb-1024x576.jpg)
A few years ago I abandoned Twitter in favor of Mastodon. Recent events validate that choice and underscore the strategic importance of [a decentralized fediverse](https://thenewstack.io/the-fediverse-points-to-our-social-media-future-post-musk/) that can’t be owned by a single corporate or state actor. But while Mastodon meets my needs, much of the Twitter diaspora has gone to Bluesky. That’s fine for now but might not always be. In an article titled “[Science Must Step Away From Nationally Managed Infrastructure](https://www.thetransmitter.org/policy/science-must-step-away-from-nationally-managed-infrastructure/),” Dan Goodman writes:

How can we prepare for a future migration from Bluesky to Mastodon? [Bridgy Fed](https://fed.brid.gy/) — a service that enables you to [connect together your website, fediverse account and Bluesky account](https://thenewstack.io/bridge-building-the-state-of-the-open-web-heading-into-2025/) — will help. But Bridgy Fed needs to be easier to use. So I recruited Claude’s new Sonnet 7 model to do that.

## The Fediverse/Bluesky Bridge
The bridge, invented and operated by [Ryan Barrett](https://snarfed.org/), enables Bluesky people to follow and interact with Mastodon folks — and vice versa — by way of a pair of agents that enable the creation of ghost accounts on both ends. In principle it’s easy to use the bridge. Here’s a handy cheat sheet from [Kilian Evang](https://kilian.evang.name/):

Easy, right? Well, for most developers’ brains it is, but not for mine and certainly not for many non-devs. To follow the Bluesky handle *jonudell.bsky.social* from the fediverse, you have to translate *@username.app.tld@bsky.brid.gy* to *@jonudell.bsky.social@bsky.brid.gy*. To follow the Mastodon handle *judell@social.coop* from Bluesky, you have to translate *@username.app.tld.ap.brid.gy* to *@judell.social.coop.ap.brid.gy*.

Typical developers, who can do that kind of mental substitution easily and automatically, tend not to realize that it often doesn’t happen that way for others and that many people need help making the transformation. That’s one reason developer-written docs are often less helpful than they might be. It isn’t that the authors don’t care about communicating effectively, it’s just that they don’t perceive how things they tacitly understand must be shown explicitly to bring others to the same place of understanding.

In this case here’s what I, and presumably many others, would like to see:

So I showed Kilian’s screenshot to Claude and asked for [the interactive version](https://jonudell.info/fedi-bsky-interactive-cheatsheet/) shown in that clip.

## Creating the First Draft
This was the initial prompt:

Claude responded with a hosted artifact you can see live [here](https://claude.site/artifacts/a6e31cb1-ce17-4042-b79c-6b6afa27a0c7). Great start! This was indeed the essence of what I wanted; I could have shared the link and called it day. But of course when things happen this quickly and easily you can’t *not* want to embellish. For starters, the Claude artifact is React-based and I never want that unless necessary.

This time the generated artifact failed in the hosting environment provided by Claude, and a couple of turns of the crank didn’t resolve the problem. But that was OK, I now had a stand-alone HTML/CSS/JS construct that I could save, test and evolve locally, and easily publish to any vanilla web host. I created a [repo](https://github.com/judell/fedi-bsky-bridge-interactive-cheatsheet) for it and called it a day.

## Enhancing the First Draft
When I circled back a few days later with ideas for enhancement, I wanted to start by asking Claude to document the existing code. Just as I was debating whether to upload the HTML file or copy/paste it, I noticed the new GitHub integration.

You can now authorize Claude to see your repos, and then point it at the files you want to include in a chat session. Nice!

Here were the enhancements I had in mind:

**Dynamic validation.**As you type a handle, you should see the translation forming. When it becomes valid it should turn from gray to green.**Copy button.**When it goes green, a copy button should appear.**TLD validation.**Mastodon handles end with domains and shouldn’t go green unless those are valid top-level TLDs found on[this list](https://data.iana.org/TLD/tlds-alpha-by-domain.txt).**Bridgy user page.**When you bridge a Mastodon or Bluesky account, the bridge creates a page where you can monitor the corresponding ghost account. The link to that page should form dynamically too and go green only when valid.
As we worked through these enhancements I challenged Claude to prove they worked, and it responded with live artifacts that isolated the changes and made each available for interactive testing. That gave me a good deal of confidence in the changes, but now I had to integrate them into the evolving tool.

## Integrating the Changes
Emboldened by Claude’s newfound GitHub ability, this was my next prompt:

For now, that’s a step too far. But hey, it never hurts to ask, right? I dialed down my expectations and instead asked:

Claude instantly provided a patch file that looked completely plausible but was hopelessly broken. This was surprising, because it seemed like the kind of mechanical pattern-oriented transformation that [LLMs tend to do shockingly well](https://thenewstack.io/choosing-when-to-use-or-not-use-llms-as-a-developer/). We went around and around for a while and I never did get it to produce a working patch. When I realized it might need a version of the source file with line numbers, I provided that — but it still didn’t help. I brought ChatGPT’s o1 into the loop and it was also stumped. I’m not sure why this particular task seems to defeat the smartest LLMs. Was I asking the wrong way? Is there something about the task that cuts against the grain? If anyone can offer insight as to why they failed, I’m all ears.

## Final Cleanup and Refactoring
It feels ridiculous to complain about that limitation. I’m reminded of the classic Louis C.K. bit about the guy with glitchy airplane WiFi. (“This sucks.” “Dude, you are riding in a chair in the sky!”) Nonetheless it’s true that integrating those changes took more time than was required to generate them in the first place.

Once the tool was feature-complete, there was the usual need for refactoring and consolidation. It was pretty clear to me what was needed, but when I asked both Claude and ChatGPT to review the code, they came up with improvements that hadn’t occurred to me, among them that event handlers were being called redundantly from two different places.

Again it was actually harder to integrate these improvements than it was to generate them in the first place. Once that was done, though, Claude was able to write a nice [change log](https://github.com/judell/fedi-bsky-bridge-interactive-cheatsheet/blob/main/CHANGELOG.md).

## Riding in a Chair in the Sky
As Dan Goodin points out, we need to be prepared for inevitable platform shifts. It’s remarkable that these tools enabled me to build and refine this small but useful tool, far more quickly and easily than otherwise possible. Making the fediverse/Bluesky more accessible is one step toward insulating ourselves from the whims of corporate owners and building more resilience into our online communities.

It wasn’t a completely smooth experience, but I’m grateful for the AI help that streamlined the task and enriched the result. After all, we’re riding in chairs in the sky here. The occasional patch-file hiccup seems a small price to pay.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)