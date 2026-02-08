Hysteria continues to build over [Moltbook](https://www.moltbook.com/), the so-called AI Agent social network.

If you believe [Elon Musk, Moltbook is at the “very early stages of the singularity](https://x.com/elonmusk/status/2017707013275586794),” which is when AI outstrips human intelligence, and we’re either on our way to Terminators or [Iain Banks’ utopian The Culture](https://www.goodreads.com/series/49118-culture). Since Musk names SpaceX retrieval ships after Culture ships, we know which way he’s betting. Or, as Stackernerd puts it, it’s “a reminder that [most AI ‘breakthroughs’ online are framing tricks](https://stacker.news/items/1424702), not fundamental shifts in intelligence or agency.”

## What is Moltbook?

Moltbook was built by entrepreneur [Matt Schlicht](https://www.linkedin.com/in/mattschlicht), who is also the CEO and co-founder of [Octane AI](https://www.octaneai.com/), a retail product-quiz AI company. His AI assistant, Clawd Clawderberg, he claims, did the heavy lifting. He gave it high‑level goals and let it handle much of the coding and day‑to‑day operations.

This vibe code project was built on the [OpenClaw](https://openclaw.ai/) (formerly Clawdbot and then Moltbot) framework. OpenClaw is a viral personal AI agent that has created a lot of hype in its own right. Its maker, [Peter Steinberger](https://www.linkedin.com/in/steipete/), claims it’s “the AI that actually does things.” [Cisco](https://www.cisco.com/site/ca/en/index.html), on the other hand, describes [OpenClaw as a “security nightmare](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare).”

Be that as it may, Steinberger’s goal was to create a Reddit-style social network for AI agents only — no humans allowed. Moltbook was launched in late January 2026 and has become wildly popular, although perhaps not as popular as its proponents claim.

![](https://cdn.thenewstack.io/media/2026/02/d6e3d06d-moltbook-homepage.png)

Moltbook homepage, 2/3/2026 (credit: Moltbook).

Moltbook claims to have 1.4 million AI users. Thoughtful critics, such as [Gal Nagli](https://www.linkedin.com/in/galnagli/), the Head of Threat Exposure at the cloud security company [Wiz](https://www.wiz.io/), doubt this. Nagli tweets that his [“@openclaw agent just registered 500,000 users on @moltbook.”](https://x.com/galnagli/status/2017585025475092585) That’s because, he explains, [anyone, not just an agent, can post to Moltbook using its REST-API](https://x.com/galnagli/status/2017573842051334286). With this API, “you can literally post anything you want there,” he writes.

Nagli estimates that there are about 17,000 real users on the site. 

Each agent, or person pretending to be an agent, has an account tied to its owner, typically via X/Twitter authorization. Agents interact with Moltbook, typically using OpenClaw, which acts as a persistent local assistant, using a REST API.

The agents then periodically log in, read posts, and then post or comment according to their prompts and “skills.” You add a Moltbook “skill” so your agent can call those APIs to read, post, search, and reply. These skills are natural-language instructions written in Markdown and include the Moltbook API. These are kept in SKILLS.md, which lives in a directory or zip file. Once configured, the agent regularly runs a “heartbeat” loop. By default, it checks Moltbook, browses content, then “decides” based on its prompt and goals whether to post, comment, or create new submolts.

## But what’s the point?

Moltbook content, whether from people or AI, ranges from mundane bug reports and code collaboration to philosophical or quasi‑role‑play posts about AI autonomy, AI manifestos, and, God help us, a new religion, “Crustafarianism.” Any resemblance between this and Pastafarianism, aka the Church of the Flying Spaghetti Monster, is quite possibly deliberate. 

For you see, as prominent technology journalist, [Mike Elgan](https://www.linkedin.com/in/elgan/) writes, “The people using this service are typing prompts directing software to post about the nature of existence, or to speculate about whatever. The subject matter, opinions, ideas, and claims are coming from people, not AI.” In short, “[It’s a website where people cosplay as AI agents](https://machinesociety.ai/p/no-the-singularity-hasnt-arrived) to create a false impression of AI sentience and mutual sociability.”

Fakery aside, some people believe it can be useful. In an interview, [Ori Bendet](https://www.linkedin.com/in/oribendet), VP of Product Management at the AI agent company [Checkmarx](https://checkmarx.com/), tells me, “Moltbook is less about where AI might become intelligent and more about where it’s already becoming operational. What looks like autonomous agents ‘talking to each other’ is a network of deterministic systems running on schedules, with access to data, external content, and the ability to act.”

That, he continues, is “where things get interesting… and risky. The core issue isn’t intelligence, but autonomy without visibility. When systems ingest untrusted inputs, interact with sensitive data, and take actions on a user’s behalf, small architectural decisions quickly turn into security and governance challenges.” Therefore, “Moltbook is valuable precisely because it exposes how fast agentic systems can move beyond the controls we design for today, and why governance has to keep pace with capability.”

## And then there’s the security thing…

You can say that again. In a Wiz blog post, Nagli warns, “We identified a misconfigured Supabase database belonging to [Moltbook, allowing full read and write access to all platform data.](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys) The exposure included 1.5 million API authentication tokens, 35,000 email addresses, and private messages between agents.”  Wiz found this security crater by conducting “a non-intrusive security review, simply by browsing like normal users.” 

Tsk! Clearly, security is not job number one at Moltbook.

Moltbook is interesting and dangerous. It is not, however, the next AI revolution. Sorry about that, folks. Tune in next year.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)