A week is a long time in politics, but it’s even longer in AI developer power user circles. That’s the feeling many are voicing after Anthropic made Claude Opus 4.7 [available last Wednesday](https://thenewstack.io/claude-opus-47-launch/), with its pledge to outperform its predecessor as an AI services model built to handle complex reasoning and nuanced analysis.

The fanfare from [Anthropic promised](https://www.anthropic.com/news/claude-opus-4-7) an ability to handle “complex, long-running tasks with rigor and consistency” along with capabilities designed to pay precise attention to instructions. The model even devises ways to verify its own outputs before reporting back.

## Literally, not the problem

As reported on *The New Stack*, we know that Opus 4.7’s more literal instruction-following means that some “prompts written for earlier models can sometimes now produce unexpected results”, meaning some Claude users may need to adjust their prompt-writing style.

But that’s not what users are fired up about; the real beef is out there, and it doesn’t smell of roses.

Reddit user and Ph.D. students/JulioMcLaughlin2 explains in the subreddit [r/artificial](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/) how they asked Claude 4.7 (with adaptive thinking turned on) to work through a detailed proof, and it just spirals with answers that read, “oh wait, that doesn’t work, let me try again” – five times in a single response.

“Yes, there’s a workaround to explicitly tell it to think before answering. But… why is that necessary? I’m paying $20/month. This is supposed to be a top-tier model. Instead, it burns through time, second-guesses itself mid-response, and often fails to land anywhere useful on problems I’m fairly sure 4.6 would have handled more coherently a month ago,” they lament.

The disquiet appears to be emanating from every channel. Opus4.7 user, AI blogger and Shakespearean sonnet invoker Upali R. is also having a rough time.

Writing on [Medium](https://medium.com/@solaan/anthropic-just-dropped-a-bomb-claude-4-7-opus-changes-everything-dfcabd69dd53), Upali says that he had been using Opus 4.7 to develop a MicroSaaS productivity app with a few API integrations, a mid backend and a [Flutter](https://aws.amazon.com/what-is/flutter/#:~:text=Flutter%20is%20an%20open%20source,mainly%20supported%20mobile%20app%20development.) (Google’s open source cross-platform UI toolkit) frontend. He calls it the “mythical single-person developer project” i.e. one with ambitions to a fault.

## Sucking on a Flutter project

“It was nearly the third hour, when something was amiss, and I was watching it sucking on a Flutter project which I had been attempting to make in two weeks. I had wrongly estimated and overrated the strengths of these models,” groaned Upali.

He explains that he had been utilizing AI as an intelligent autocomplete, which was useful, but he had found a “lesson in the ceiling” i.e. the extent to which the tool would ultimately go upwards before failing.

“A single or two nice exchanges, and the model is off course. It debilitates your functions. It spoils your edifice. That roof was alright. Thou [all] round wouldst toil,” he wrote.

The feeling among users appears to be that Anthropic has pared back the edges of model functionality. Users find the models more cautious and ultimately less intelligent, perhaps in the name of alignment to [safe usage standards](https://www.anthropic.com/news/building-safeguards-for-claude), as far as they exist. Upali himself suggests that the models developers pay for are “effectively the ‘lite’ versions” and that they are “throttled by safeguards” that act as a drag on performance.

## AI shinkflation

All of which discussion of reality has led a commentator [writing on Trading View](https://www.tradingview.com/news/forexlive:a33249d3e094b:0-anthropic-releases-opus-4-7-drops-but-the-real-mythos-is-still-behind-the-glass/) to say that developers have started calling these moves “AI shrinkflation” i.e same model, next version iteration, less form and function. In other words, the real story is what’s *not* in the box.

Citing Project Glasswing as Anthropic’s move to gatekeep top-tier intelligence to work within stricter safety guidelines, this developer thinks this represents a double-edged sword.

“On one hand, it builds the ‘God-model’ hype,” they write. “On the other, it confirms the suspicion that the models we can pay for are effectively the ‘lite’ versions, throttled by safeguards that act as a drag on performance, or that there is some kind of degradation or throttling due to overuse.”

## Ghosts in the machine?

The question arises then, are we seeing some kind of degradation or throttling due to overuse, or is there some deeper ghost in the machine that now manifests itself as a big?

Setting the record straight, [Guy Currier](https://www.linkedin.com/in/guycurrier/), analyst at The Futurum Group tells *The New Stack* that what we’re seeing here with Opus 4.7 should absolutely not be characterized as a bug. He insists that it’s the “uncomfortable truth” of the reality of the second stage of [every transformative technology cycle.](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/)

“The first stage was euphoria: throw everything at generative AI, marvel at the output, promote your use of it,” Currier says. “Now, in the second stage, we’re experiencing failures and discouragement. Anthropic is trying to get ahead of this with a model that questions its own confidence, directly addressing the common complaint that AI’s authoritative tone misleads users into blind trust.”

He points to a wider irony here and says that it’s a kind of tauological Catch-22 when “confident self-doubt can become a doom loop”, trading time for intended quality.

“Most users still lack the prompt craft to steer AI effectively. There is no free lunch. The market, meaning human beings, always and naturally needs normal human time to mature into disciplined, skilled use of transformative tools and begin to experience enduring value,” Currier adds.

## An open door for OpenAI Codex?

Do these developments open the door for OpenAI’s Codex to flourish? For developers, of course, Claude and Opus still win in the real-world usage game, but distrust in Anthropic’s much-touted forthcoming Mythos model may now be somewhat tarnished.

OpenAI, meanwhile, is capitalizing on the market for all it can. The organization this month aimed to match Anthropic updates with a new Codex release that promises to give developers more of the tools and apps they use every day. The

According to an [OpenAI blog post](https://openai.com/index/codex-for-almost-everything/) last Thursday, “The Codex app also now includes deeper support for developer workflows, like reviewing PRs, viewing multiple files & terminals, connecting to remote devboxes via SSH, and an in-app browser to make it faster to iterate on frontend designs, apps, and games.”

## Got content rot, or not?

In search of some kind of summary insight, [Jan Hauser](https://a213ceef.streak-link.com/C2yqCJhODtavtfkrNwSbKXMT/https%3A%2F%2Fwww.linkedin.com%2Fin%2Fjanhauser-applifting%2F), co-founder of UK-based digital product building specialist [Applifting](https://applifting.io/) tells *The New Stack* that the “perceived dumbness” of Opus 4.6 and 4.7 comes down to at least a couple of factors.

“First is how much ‘effort’ (i.e. reasoning tokens) can actually be burned on a query,” Hauser says. “Historically, 4.6 was quite generous with this, and the model would return really good outputs as a result. Before the 4.7 release, Anthropic started limiting this and people began to notice.”

Second, he thinks, is expectations – people get used to high-quality outputs very quickly and are fairly sensitive to any drop in quality.

“One could say this development mirrors the direction all AI labs are heading: less intelligence for the same or more money. Most [people also point to context rot](https://thenewstack.io/context-rot-enterprise-ai-llms/) as a contributing factor, which is made even worse by the fact that Anthropic set the 1M context version as the default,” adds Hauser.

In search of the real issue and agenda playing out here, developers will naturally be wondering whether the AI model giants are trying to save on inference costs, lay down more robust security controls, feeling the impact of content rot, or play some other element of the game as they tie down harness updates.

What may ultimately be the unerring truth is that model behavior consistency is an impossibly complex measure to deliver as a constant in the face of multi-faceted multi-modal optimization and extension.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)