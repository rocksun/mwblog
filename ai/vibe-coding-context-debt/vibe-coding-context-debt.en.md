Some of the engineers who made [vibe coding](https://thenewstack.io/vibe-coding/) possible have decided it’s a problem. Last month, *The Wall Street Journal’s* Christopher Mims [interviewed](https://www.wsj.com/tech/ai/vibe-coding-slop-ai-tools-e6a99394) Armin Ronacher and Mario Zechner, the engineers behind the Pi engine that powers OpenClaw. These engineers have been instrumental in popularizing these agentic tools, and their assessment was blunt: The tools are flooding the world with bad, sometimes dangerous code. “Eventually it will catch up to us,” Zechner told Mims.

They’re referring to vibe slop. Code that’s bug-ridden, inefficient, hard-to-maintain software produced by someone prompting it into existence. Ronacher and Zechner talked about an overlooked aspect of vibe coding, too. Sloppy code doesn’t just break more; it burns more compute, more memory, and more bandwidth, they said. They warned some vibe-coded startups may not be able to pay their own compute bills, either.

I largely agree with Ronacher and Zechner. But someone put a sharper name to the problem, and he did it in a product launch post.

## The real debt is context

On June 2, [Postman](https://www.postman.com/), an AI-native platform, shipped what it calls the AI Engineer, and CEO [Abhinav Asthana](https://www.linkedin.com/in/abhinavasthana/) used the launch post [to make the case](https://blog.postman.com/introducing-the-ai-engineer/).

![](https://cdn.thenewstack.io/media/2026/06/e37a1831-1528853823461.jpg)

Abhinav Asthana, CEO and founder of Postman

Bad code, he argues, is the part you can see. It’s visible, so it gets the blame.

The harder problem is everything wrapped around it, the services and APIs that stack up faster than anyone can keep track of. He calls it context debt, and I’m buying what he’s selling.

The idea goes like this. With vibe-coded platforms, systems quickly evolve from MVPs into products filled with countless APIs, services, and databases, and those pieces interact in ways nobody fully designed or understands.

Every new service, every new platform, every agent-generated change stacks on past work, and these are often lost when adding new work. Like technical debt, context debt compounds.

Unlike technical debt, you can’t refactor your way out of it because the debt isn’t in the code. It’s in what the code means **and how it connects.**

> Unlike technical debt, you can’t refactor your way out of it because the debt isn’t in the code. It’s in what the code means and how it connects.

Most organizations still handle this the old-fashioned way, with a handful of senior engineers who keep the whole map in their heads. The org rests on the institutional knowledge of these engineers, and the process doesn’t scale. Now, when a fleet of coding agents starts building and shipping at machine speed, the rate of production outpaces the team’s ability to understand what has been built.

That’s the trap. Fixing slop without fixing context moves the failure upstream. You start pushing code into a system no one understands anymore.

Asthana thinks the clock is short. He puts the window at six to nine months before context debt outruns most teams’ ability to manage it by hand, and he says the warning sign is already visible: early-stage startups that can’t keep their own architecture coherent. In his view, in this era of vibe coding, the smallest, fastest-moving companies are hitting the wall first.

## Agenting Engineering needs a memory.

Simon Willison points to [agentic engineering](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/) as a useful frame for this. The agents run in a loop, writing and executing code, while the real human skill lives in goal definition, tool prep, and verification. The human becomes the architect who defines, reviews, and integrates.

This framing defines how a person should work with an agent on a task. Context debt is the question of what happens across thousands of those tasks in one organization. An agent can verify that its code works. It has a much harder time verifying whether the API it just designed duplicates one already used by another team, or whether the contract it quietly changed breaks something nobody documented.

Postman’s answer is what it calls a Context Graph: an always-on, continuously updated map of the APIs, services, and dependencies across a Postman organization that grounds the AI Engineer before it acts. The agents run in a sandbox and perform write operations that require a human-in-the-loop; the output integrates with the existing PR review process. Asthana describes the risk model as a junior engineer whose work can go through code review. A regular coding agent can write a function. It can’t tell which of your 17 payment APIs you’re actually supposed to use.

> A regular coding agent can write a function. It can’t tell which of your 17 payment APIs you’re actually supposed to use.

This matters more at scale. The largest Context Graphs Postman mapped run well exceeded anything a senior engineer could hold in their head, Asthana told me. They mapped more than 1,100 APIs at a major U.S. telecom, more than 2,600 at a global telecom, and over 11,000 at one large tech company.

Postman has been running the agents on its own engineering team and has shared some data with me. APIs touch 68% of the company’s pull request traffic, Asthana tells *The New Stack*, and Postman runs the AI Engineer across the API-related work. The most consequential catch so far, he said, was a set of downstream dependency changes that likely would have cleared review but failed in production.

> An out-of-date map can be worse than none, because the agent acts on it with confidence.

Postman’s bet is that ten years of customers documenting their APIs within its tools give it a head start in building that map. That’s a real advantage, with a real catch. The map is only as good as the information behind it, and plenty of companies’ records are years out of date. Asthana cites a failure from Postman’s own use: An agent didn’t know about some live systems running in another data center, so it worked from an incomplete map and got part of its analysis wrong. The failure was the map. An out-of-date map can be worse than none, because the agent acts on it with confidence.

## This is a category, not a feature

Whether Postman’s AI Engineer wins or not, the framing is starting to look like a trend. Cursor and Windsurf index your repository. Claude Code reads your [CLAUDE.md](http://claude.md) and knows your codebase. GitHub is integrating Copilot deeper into the dependency graph. The major coding-agent companies seem to be heading to the same spot: Context is a bottleneck just like the model.

Expect more vendors in this space to announce a context layer, and most engineering teams will end up buying into one. And when they do, it’s important to consider whether their orgs’ context exists in a form that’s readable by a machine (and not in someone’s head).

Infrastructure is becoming more critical in this new agentic world. It’s the ground on which agents need to stand. Teams need to start treating context more importantly.

Context debt has always been around. Agents are making the problem more urgent. The Pi engineers are probably right that slop will catch up to us. The teams that get ahead of it won’t be the ones using the best model or coding agents, but the ones whose systems are available to humans and machines alike.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.