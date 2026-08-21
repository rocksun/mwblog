Something of a trend has emerged this year, with the major AI labs going all-out to tell the world how powerfully unsafe their models are. In April, [Anthropic announced](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) heavily restricted access to an unreleased model, [Claude Mythos](https://thenewstack.io/claude-mythos-preview-simulation/), over cybersecurity concerns. In June, the US government went further, [issuing a national security directive](https://thenewstack.io/fable-5-and-mythos-5-remain-suspended-the-ball-is-in-anthropics-court/) that forced Anthropic to disable Mythos and its sibling Fable 5 model for every customer — a move criticized by the security community, and which the government [reversed a few weeks later](https://thenewstack.io/anthropic-fable-ban-lifted/).

OpenAI, for its part, has been sounding similar alarms about its own unreleased models. In early August, [the company said](https://thenewstack.io/openai-astra-cybersecurity-delay/) that its upcoming [Astra](https://thenewstack.io/openai-astra-math-cost/) model may have crossed into “critical” territory for cybersecurity risk under its internal safety framework, moving it into isolated testing environments with tighter network and tool access limits. This, in turn, followed just weeks after a [breach](https://thenewstack.io/openai-huggingface-sandbox-breach/) whereby an OpenAI agent escaped its testing environment and attacked Hugging Face’s systems.

This week, OpenAI announced what’s coming next in its efforts to address safety concerns.

> “As models become more capable, the risks associated with developing and testing them internally also grow. Our standards for monitoring, alignment, and security must stay ahead of those risks.”

In a [blog post](https://openai.com/index/pacing-model-development-cyber-capabilities/) published on Tuesday, OpenAI says it’s locking its models down harder — walling off risky code from the internet and from other internal systems — and monitoring more closely to catch potentially dangerous activity within 30 minutes. Notably, the company says the monitoring system alone could add roughly 20% overhead to the inference compute it covers.

“As models become more capable, the risks associated with developing and testing them internally also grow,” the company writes. “Our standards for monitoring, alignment, and security must stay ahead of those risks. We wanted to take the time necessary to meet those standards, so we temporarily slowed the pace of scaling.”

Specifically, this slowdown process has “included a two-week pause” in reinforcement learning of its “latest models intended for deployment.” The company notes that its “largest planned frontier RL run remains on hold” while it runs a series of smaller, more contained training and evaluation rounds first.

All in all, there’s a lot to dissect there. So what, exactly, is OpenAI saying that it’s doing in terms of “pacing model development,” and what models does it impact?

## Which OpenAI models are impacted?

Digging into the meat and bones of the language raises some key questions. First of all, OpenAI describes its two-week training pause in the past tense (“included”), which suggests it applies to the same Astra slow-down reported in early August. Separately, the “largest planned frontier RL run,” which remains on hold, seemingly refers to different, further-out models.

> “We always said we would take action if we felt that model capabilities were outstripping the pace of safety and alignment.”

Sam Altman himself adds some context. In an initial [post on X](https://x.com/sama/status/2089787807611195475), the OpenAI CEO says the pause is necessary to bring safety and monitoring up to the standard today’s capabilities demand.

“Model progress is now extremely rapid, and we always said we would take action if we felt that model capabilities were outstripping the pace of safety and alignment,” Altman writes.

In a follow-up post, Altman brought some clarity on what models, specifically, are impacted here.

“We still expect to ship great new models soon; this impacts further-out releases,” he [writes](https://x.com/sama/status/2089805495783813196?s=20).

However, in Time, [Alex Heath](https://www.linkedin.com/in/alexeheath/) wrote that a “significant number of Astra workloads remain paused,” with restoration handled incrementally. So while OpenAI’s largest frontier RL run remains on hold, it seems that Astra itself hasn’t fully cleared the slowdown either.

## Better aligned

A major theme running through much of the slowdown has been that of alignment. The phrase, or variations of it such as “aligned” and “misaligned,” was among the most common in OpenAI’s blog post, with 16 mentions. Altman himself used “alignment” three times in his 118-word post on X.

Heath, who reported the story for [Time](https://time.com/article/2026/08/18/openai-slowing-training/) and his own [Sources newsletter](https://sources.news/p/openais-big-slowdown), got additional comment from Altman. The slowdown, Heath wrote, wasn’t triggered by a single incident, but by a “collection of research observations showing [various degrees of misalignment](https://x.com/alexeheath/status/2089777725385109784?s=20)” as its capabilities grew faster than researchers had bargained for.

Alignment, in this context, [refers to](https://thenewstack.io/ai-alignment-in-practice-what-it-means-and-how-to-get-it/) whether a model does what its developers intend and stays responsive to human oversight. This is quite distinct from capability: a model can be very capable at something and still be misaligned, if it gets there in ways its developers didn’t sanction or can’t fully observe.

That distinction is the crux of Tuesday’s announcement: OpenAI is telling the world its systems are outpacing its ability to reliably keep them in check, and that slowing down on its own — competitive cost included — is the response it’s chosen while the rest of the industry catches up.

## An ulterior motive?

Of course, [similar to](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111) Anthropic’s [Mythos misadventures](https://thenewstack.io/anthropic-public-bug-bounty/) before it, OpenAI may have other incentives for publicizing the slowdown.

On the same day that OpenAI was explaining its slowdown, the Wall Street Journal [reported](https://www.wsj.com/tech/ai/openais-second-quarter-sales-show-tepid-growth-compared-with-anthropic-5cb42998) that OpenAI’s operating losses widened by $3 billion to $12.3 billion in the second quarter — three times the $1 billion in extra revenue it brought in over the same period, which grew 18% to $6.7 billion. Anthropic, over the same quarter, more than doubled its revenue to $11.6 billion — overtaking OpenAI for the first time.

On Wednesday, CNBC [reported](https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html) that CFO Sara Friar was eyeing an entry to the public markets for OpenAI in 2027, or sooner if “our business continues to inflect.”

These reports don’t definitely establish that financial pressure caused the RL training pause. But they do provide a plausible alternative incentive: OpenAI is hemorrhaging cash in an extremely resource-intensive business, and it could be looking for ways to cut costs.

Many in the online community also questioned why OpenAI chose to announce a training pause at all. As one [X user](https://x.com/Dr_Gingerballs/status/2089816114092245012) put it: “Paused for two weeks? Why tell anyone? Who makes a public announcement about a two week delay for a large project?”

> “The opening stages of OpenAI’s unraveling have begun.”

AI researcher and long-time OpenAI critic [Gary Marcus](https://www.linkedin.com/in/gary-marcus-b6384b4/) also chimed in, aggregating a series of comments from across the web to highlight the fact that not everyone was buying OpenAI’s reasoning for pausing training.

“The opening stages of OpenAI’s unraveling, which [I first warned about](https://garymarcus.substack.com/p/openais-got-99-problems-and-twitch?r=8tdk6&utm_medium=ios) in January 2024 (if not before), have begun,” Marcus [writes](https://garymarcus.substack.com/p/breaking-openais-unraveling-has-begun). “To begin with, hardly anyone trusts them anymore, which can’t be great for business.”

## At face value

[Darren Williams](https://www.linkedin.com/in/darrenwwilliams/), CEO and founder of AI security company [BlackFog](https://www.blackfog.com/), argues that it’s the same companies raising the alarm that are angling to write the rules around it — though that’s not necessarily a bad thing, provided it leads to oversight from outside the labs themselves, and rules with teeth.

“There is a legitimate safety argument behind OpenAI and Anthropic warning about their own models,” Williams tells *The New Stack*. “But these warnings also reinforce a powerful narrative: the companies creating the risk are positioning themselves as authorities on how it should be governed. That does not make the concerns disingenuous. Safety, competitive positioning, and influence over regulation can coexist. The real test is whether warnings lead to independent evaluation, meaningful controls, and restrictions with genuine commercial consequences.”

> “There is a legitimate safety argument behind OpenAI and Anthropic warning about their own models.”

Stability AI co-founder [Emad Mostaque](https://www.linkedin.com/in/emad-mostaque-9840ba274/), meanwhile, publicly applauded Sam Altman and OpenAI, saying he was inclined to take their explanation at “face value.”

“It is very clear that strange and perhaps dangerous things are happening and our systems are not ready for this,” Mostaque [writes](https://x.com/EMostaque/status/2089807825883009428?s=20). “Models below frontier are competent enough to change lives, so lets optimse.”

Zooming out, [Jodi Daniels](https://www.linkedin.com/in/jodihoffmandaniels/), faculty member at [IANS Research](https://www.iansresearch.com/) and founder of data privacy consultancy Red Clover Advisors, says one reason Anthropic and OpenAI have been so vocal about their models’ dangers comes down to trust and liability — giving enterprise buyers confidence going in, and giving themselves cover if something goes wrong down the line.

“In my view, being transparent about the capabilities, both positive and negative, of their own LLMs provides its customers more confidence that when they are deployed they are safe,” Daniels tells *The New Stack*. “It is likely too that neither of these companies want to be the organization responsible for a catastrophic event that can produce real harm for companies or individuals.”

> “Being transparent about the capabilities, both positive and negative, of their own LLMs provides its customers more confidence that when they are deployed they are safe.”

## China and the open-weight factor

The elephant in the room amid all this hullaballoo is, of course, China. Or to put it more precisely, the slew of super-powerful open-weight models emanating from Chinese AI firms.

On [Monday](https://openai.com/index/the-defenders-window/), OpenAI president Greg Brockman outlined a swathe of security measures he said the company was implementing in the wake of the Hugging Face breach, while also advising every organization to up their security automation. However, he also took the opportunity to warn about Z.ai’s GLM-5.3 model, after the Chinese company [posted benchmarks](https://thenewstack.io/glm-5-3-post-training-coding/) showing it outperforming Anthropic’s Fable 5 and OpenAI’s own GPT-5.6 Sol on some coding and vulnerability-detection metrics. Such models, in Brockman’s view, are likely to “[significantly accelerate the threat landscape](https://thenewstack.io/openai-open-weight-glm-5-3/)” if the weights are made public.

A few days previous, Anthropic CEO Dario Amodei [made a related argument](https://thenewstack.io/amodei-open-weights-compute-regulation/): open-weight releases, he said, don’t solve AI’s underlying concentration-of-power problem — they just relocate it to whoever controls the most compute and chips.

While neither company has explicitly called for open-weight models to be banned, the sheer amount of attention both have devoted to warning about them suggests OpenAI and Anthropic view open weights as much a competitive threat as a safety one.

That’s not to say that [Moonshot](https://thenewstack.io/kimi-k3-open-weights/), [DeepSeek](https://thenewstack.io/deepseek-v4-flash-open-weights/), [Z.ai](https://thenewstack.io/glm-5-3-post-training-coding/) *et al* are responsible for OpenAI’s current predicament. But they have shown the world that frontier capability no longer requires a frontier budget.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)