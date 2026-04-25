OpenAI may dominate the consumer chatbot market with ChatGPT, but among developers, Anthropic’s Claude models, via its [Claude Code agent](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/), have become the tool of choice.

More broadly, the two companies are moving in near lockstep, trading features and model releases. And so after [Anthropic unveiled Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) last week, it was only a matter of time before its rival followed suit. On Thursday, [OpenAI introduced](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/) GPT-5.5 and GPT-5.5 Pro, its latest general-purpose models with improvements in coding and more complex tasks.

## Beyond benchmarks

The headline from OpenAI itself is “a new class of intelligence for real work,” riffing off a growing effort among AI firms to present their models as ready for day-to-day work.

The company is also leaning heavily on benchmark results to support that claim, pointing to gains across coding, reasoning, and system-use tests. But benchmark scores don’t always reflect how models perform in real-world use, and [can in some cases](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/) be gamed or sidestepped entirely.

Which makes a more immediate question: how does GPT-5.5 hold up when developers actually use it?

Blogger and open-source developer [Simon Willison](https://www.linkedin.com/in/simonwillison/), who had early access to the model, [describes it](https://simonwillison.net/2026/Apr/23/gpt-5-5/) as “fast, effective and highly capable,” but quickly hit a notable limitation: the lack of API access, which meant he couldn’t immediately run his usual tests.

One of those tests is his long-running “[pelicans on a bicycle](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/)” benchmark, where models are asked to generate an SVG of a pelican riding a bicycle — a deliberately awkward prompt designed to test how well they handle structured, unfamiliar tasks.

To get around the lack of API access, Willison built his own plugin using a semi-official Codex “backdoor” API to run his tests. Willison found that the model’s default output lagged behind GPT-5.4 on this task, but improved when given more reasoning time — at the cost of far higher token use and slower responses.

“I’ve seen better from GPT-5.4, so I tagged on *`-o reasoning_effort xhigh`* and tried again,” Willison said after his initial efforts with GPT-5.5 yielded poor results. “That one took almost four minutes to generate, but I think it’s a much better effort.”

In short, better results are there, but possibly at the expense of time and compute.

Others testing the model point to improvements in how little guidance it needs. [Soumitra Shukla](https://www.linkedin.com/in/soumitra-shukla/), a research fellow at Harvard’s AI Institute, [observes](https://x.com/soumitrashukla9/status/2047515787695472741) on X that after using GPT-5.5 in the Codex app, that the new model “just gets it,” and it requires “much less hand-holding,” and that it handles longer-running tasks more smoothly.

Pricing is also shaping early reactions. Willison noted that GPT-5.5 [will cost](https://openai.com/index/introducing-gpt-5-5/#availability-and-pricing) roughly twice as much as its predecessor once it reaches the API, with GPT-5.5 Pro priced significantly higher again, meaning that GPT-5.4 might have a longer shelf-life as a lower-cost alternative.

That trade-off also sits alongside the access constraints Willison ran into. OpenAI explains that the delay in API access is due to additional safety and security requirements, adding that support for GPT-5.5 and GPT-5.5 Pro is on the way. However, the decision to hold it back comes amid heightened scrutiny around how more capable models are deployed, particularly in areas such as coding and cybersecurity.

Anthropic, for example, [announced in early April](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) it was withholding broader access to its Mythos model over safety concerns.

For OpenAI, its enterprise push brings those same concerns into focus. The company has rolled out features such as [workspace agents](https://thenewstack.io/openai-shared-workspace-agents/) and a [PII-focused privacy filter](https://thenewstack.io/openai-privacy-filter-pii/) this week alone, and [tested GPT-5.5 with partners including Nvidia](https://blogs.nvidia.com/blog/openai-codex-gpt-5-5-ai-agents/), which said it gave early access to more than 10,000 employees.

Those efforts hinge on how the model performs in security-critical tasks.

## “Mythos-like hacking, open to all”

Some early testers say GPT-5.5 is already showing strong performance on real-world security tasks. [Albert Ziegler](https://www.linkedin.com/in/albert-ziegler-6b3b24138/), a former GitHub researcher and machine learning engineer who’s now head of AI at security firm Xbow, writes in a [blog post](https://xbow.com/blog/mythos-like-hacking-open-to-all) that the company evaluated GPT-5.5 against known software vulnerabilities using its internal benchmarks.

On those tests, he writes, GPT-5.5 reduced the rate at which it missed vulnerabilities to 10%, down from 40% in GPT-5 and 18% in [Anthropic’s Opus 4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/), suggesting a step change in how it performs in penetration testing tasks.

“Every missed vulnerability is a real-life liability,” Ziegler writes.

Ziegler cast that as “*Mythos-like hacking, open to all*,” referring to Anthropic’s limited-access cybersecurity model. However, as some in the Hacker News community [noted](https://news.ycombinator.com/item?id=47883953), the comparison is hard to justify given that Mythos isn’t publicly available. Other researchers [have also found](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) that smaller open-weight models can reproduce much of the analysis shown in Anthropic’s own Mythos examples when given the same tasks.

That lack of independent verification around Mythos [has also drawn criticism](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/), with some arguing that the gap between claims and reproducible results risks undermining trust in how these systems are being presented.

At any rate, the broader point likely holds true: what is useful for the good guys is also useful for the bad guys. And for now, the lack of API access hampers how easily those capabilities can be misused.

## The “jagged frontier”

For Willison and others with early access, describing what has improved isn’t always an easy endeavor. “As is usually the case these days, it’s hard to put into words what’s good about it – I ask it to build things and it builds exactly what I ask for!” Willison writes.

[Ethan Mollick](https://en.wikipedia.org/wiki/Ethan_Mollick), an AI researcher and professor at the Wharton School of the University of Pennsylvania, [makes a similar point](https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55), noting that it’s “increasingly hard to quickly demonstrate each generational change” as many of the tasks models once struggled with are now trivial.

Even so, Mollick argues the underlying gains are still significant.

“I think it is a big deal. It is a big deal because it indicates that we are not done with the rapid improvement in AI,” Mollick contends in his Substack, *[One Useful Thing](https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55)*. “It is also a big deal because it is just plain good. And it is a big deal because even with all of this, the frontier of AI ability remains jagged.”

In his own testing, Mollick asked GPT-5.5 Pro to build a “procedurally generated 3D simulation” of a harbor town evolving over thousands of years, comparing the results against earlier OpenAI models and open-weight alternatives. Only GPT-5.5 Pro produced a version that meaningfully simulated change over time, rather than simply swapping static assets.

He also points to advances across what he describes as the three main layers of AI: models, apps and [harnesses](https://thenewstack.io/ai-agent-harness-pricing-split/) — the systems that connect models to tools and real-world workflows. Using Codex powered by GPT-5.5, he was able to analyse years of research data and draft an academic paper, producing what he described as work comparable to an early-stage Ph.D. project.

“The models keep getting smarter, the apps keep getting more capable, and the harnesses keep getting better, making them ever more effective at solving real problems,” Mollick writes.

However, a closer look reveals that the “jagged frontier” of AI ability is not entirely gone. While models have become highly effective in structured domains such as coding, where outputs can be verified and iterated on, they continue to struggle with more open-ended or creative tasks.

In his own testing, Mollick found that while GPT-5.5 can handle complex, multi-step work — from simulations to drafting academic papers — those gains do not extend evenly across all tasks, particularly in areas that require sustained coherence or originality.

“GPT-5.5 is clearly not the end of this process, but it is a noteworthy step along the way,” Mollick writes. “The jagged frontier is still there. It is just much further out than it used to be.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)