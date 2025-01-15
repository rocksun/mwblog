# The Configuration Crisis and Developer Dependency on AI
![Featued image for: The Configuration Crisis and Developer Dependency on AI](https://cdn.thenewstack.io/media/2025/01/6160404d-osarugue-igbinoba-oofgkbu0g3o-unsplashb-1024x576.jpg)
We’ve been saying forever that there are three hard problems in computer science; or maybe two if you like the off-by-one joke. But **naming** and **cache invalidation** pale in comparison to the really hard problem nowadays: **configuration**. As our IT infrastructure grows ever more modular, layered and interconnected, we deal with myriad configurable parts — each one governed by a dense thicket of settings. All of our computers — whether in our pockets, on our desks or in the cloud — have a bewildering labyrinth of components with settings to discover and fiddle with, both individually and in combination. We join these computers to form networks of unfathomable complexity governed by yet more settings.

## Tech Support for Friends and Family
If your day job is in IT you are also a provider of tech support for friends and family, and that job isn’t getting any easier, either. Last month, when my wife asked a question about strange text message behavior on her phone, I got that sinking feeling you’re probably familiar with. Sure enough, it turned into a multi-hour hair-pulling ordeal. Until then, I’d been blissfully unaware of the whole RCS (Rich Communications Service) fiasco. What I think happened is that Google convinced my wife to install its RCS-enabled Messages app on her Android phone *in addition to* the native Samsung Messages app that was already there. I’ve been an iPhone user in recent years, so I wasn’t very fluent in general Android configuration, nevermind the specific pathologies that arise when two installed messaging apps are fighting with one another.

The industry shenanigans that consign innocent people to interop hell make my blood boil.

I’ll spare you the details which, honestly, I’d rather forget. The industry shenanigans that consign innocent people to interop hell make my blood boil. How do regular folks deal with this craziness? My wife likes to say she’d be lost without me to rescue her. But nowadays I, in turn, would be lost without [AI to help me grapple with the complexity](https://thenewstack.io/choosing-when-to-use-or-not-use-llms-as-a-developer/). Increasingly, I don’t know the tech, as my wife still imagines I do. Instead, I know how to [wrangle the AI systems](https://thenewstack.io/techniques-for-using-llms-to-help-write-a-postgres-function/) that embody (unreliably and imperfectly!) knowledge of the tech.

## Grappling with All the Clouds
Meanwhile, in my professional life, the same thing is happening. I was tasked with documenting how to install and configure an enterprise software product on each of the big three cloud platforms. I’ve scratched the surfaces of AWS, GCP and Azure, but I don’t use any of them deeply or regularly. Now, as prerequisites for the installations, I needed to learn and explain (among other things) how to create custom roles in all three. So there were three GUI consoles in play, each with its own layers of byzantine complexity, as well as three corresponding CLIs, each with its own universe of commands and arguments.

A couple of years ago, it would have been a challenge to figure things out for just one of the clouds, never mind all three. There would have been no lack of information — these are well-trodden paths that have been signposted by many people in many ways. But the devil is always in the details. If I’m at *this* particular place in a UX flow and I’m seeing *this* particular view on the screen, what is my next step? Where do I click? Documentation and online discussions often don’t convey the kind of granular situational awareness you need at that moment. A knowledgeable colleague looking over your shoulder could, but that person’s attention is a scarce and valuable resource. [AIs embody the knowledge](https://thenewstack.io/human-insight-llm-grunt-work-creative-publishing-solution/) of many such people: again, unreliably and imperfectly, but still well enough to provide an unprecedented level of on-demand assistance.

AIs are amnesiacs in a useful way. The reset that happens every time you start a new chat usefully counters the human tendency to bury tacit knowledge.

A couple of strategies I’ve mentioned before bear repeating. One is [the use of screenshots](https://thenewstack.io/how-to-create-software-diagrams-with-chatgpt-and-claude/), which are now a powerful index in the corpus of synthesized knowledge. Like all forms of web software, the cloud platforms’ GUI consoles present a haphazard mix of UX idioms. A maneuver that is conceptually the same across platforms will often be expressed using very different affordances. AIs are pattern recognizers that can help us see and work with the common underlying patterns.

It’s hard for people to describe how to use the UX affordances that embody those patterns because, once learned, they recede into tacit awareness. A piece of workflow that initially seemed inscrutable becomes so obvious that you forget it once wasn’t, and you lose touch with the beginner’s mind that would enable you to help other beginners. But AIs are amnesiacs in a useful way. The reset that happens every time you start a new chat usefully counters the human tendency to bury tacit knowledge.

Another strategy that continues to pay dividends is rule #4 from [Best Practices for Working with Large Language Models](https://thenewstack.io/7-guiding-principles-for-working-with-llms/): put the same question to several different LLMs. You always have to keep your BS detector running in high gear, and consensus is no guarantee of accuracy, but differences in how the models are fed and trained help mitigate the error that monolithic use is vulnerable to.

## Cascading Configuration
With respect to the insidious growth of systematic complexity, we are like frogs in slowly boiling water. Just today, for example, I found myself in a novel situation. I’m working with a tool that downloads modules from a container registry. These modules aren’t container images; they’re just binaries that are managed using the same infrastructure: the OCI (Open Container Interface) distribution mechanism. Normally, the downloads are transparent and I’m not even aware it’s happening. But today, working with an unreleased private module, I ran into an authentication error I’d never seen before. The registry is ghcr.io, so a flavor of GitHub authentication is required. But despite having a personal access token with the necessary scope (*read:package*), I kept hitting the error. In a conversation with ChatGPT, we figured out the counterintuitive solution. Even though the tool itself doesn’t use docker, it was necessary to do a *docker login* in order to place a GitHub token into yet another of my endlessly proliferating config files, one that I’d never known about: *~/.docker/config.json*.

The explosion of configuration complexity taxes our human ability to keep track of all this stuff and to manage our systems effectively.

We’ve all experienced these cascades of dependencies that expand the number of moving parts in our interconnected systems and add configuration overhead. Now we find ourselves in an odd situation. The explosion of configuration complexity taxes our human ability to keep track of all this stuff, and to manage our systems effectively. But we have a new breed of assistants with superhuman ability who help us do that. I’m grateful for them, and would never want to go back. But I do worry about perverse incentives. Why engineer understandable systems when we can outsource the understanding of them?

## A Better Way, But Not in This Timeline
Ward Cunningham once showed me an implementation of an idea, which he attributed to Brian Marick, called [visible workings](https://blog.jonudell.net/2008/03/04/). They both imagined self-describing systems that could reveal their inner workings on demand. As applied to my docker-related example, that would mean that when the system said:

“Response status code 401: unauthorized: authentication required.”

I could ask:

“Why? And how?”

The system would have been engineered to know the answer to that question. It would understand its own dependencies and guide me through the process of resolving them. You never really understand something until you write it down. If the “why?” and “how?” of configuration were encoded in the DNA of systems from the ground up, they’d be harder to build but easier to use and maintain.

Of course, that’s a hard sell, and it gets even harder as AIs improve our ability to reverse-engineer the “why” and the “how.” Perhaps, even though they are not themselves explainable, AIs can help us engineer explainable systems. But I’m not optimistic. It feels like we’re on a path to keep making systems harder for humans to configure, and we keep expanding our reliance on superhuman intelligence to do that for us.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)