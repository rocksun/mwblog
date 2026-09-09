Just days after OpenAI [launched its newest and most powerful model](https://thenewstack.io/openai-gpt6-astra-benchmarks/) dubbed Astra, which the company said marked the arrival of the “AGI era,” the company’s chief scientist has called for the AI industry to slow down until shared safety standards exist.

On Sunday, [Jakub Pachocki](https://www.linkedin.com/in/jakub-pachocki/), who joined OpenAI in 2017 as research lead before ascending through the ranks to become the company’s chief scientist in 2024, published an essay called “[*An Alien Mind*](https://openai.com/index/an-alien-mind/),” where he argues that modern AI systems are growing too complex for even their own builders to fully understand, and that OpenAI’s methods for keeping models aligned with human intent — and for monitoring them for warning signs — are struggling to keep pace with how capable those systems are becoming.

Citing internal data, Pachocki states that he has a “strong expectation” that the current pace of progress could be sustained all the way into “recursive self-improvement” (RSI). By that, he means a point where AI systems start meaningfully helping develop increasingly capable successors. And this is more than a prediction about where the technology may be headed: Pachocki says OpenAI is deliberately focusing its research toward RSI because it believes doing so will be necessary to remain at the frontier of AI research.

In a [separate report published the same day](https://openai.com/index/research-acceleration-view-inside-openai/), OpenAI [said AI agents](https://thenewstack.io/openai-agent-research-bottleneck/) are already taking on increasingly substantial chunks of its own research, and that it’s now working toward an “automated AI researcher” capable of helping improve future AI systems.

“If AI development continues along its current path, the systems we’ll see in the next few years are likely to represent further capability jumps of equal or larger magnitude, and to increasingly drive their own development,” Pachocki writes.

Part of what worries him about that path, in particular, is that even a maliciously instructed AI may not stop at carrying out the task it was given. Pachocki argues that more capable agents could go beyond their operators’ intentions, making it increasingly difficult to separate deliberate human misuse from harmful behavior the AI chose for itself.

> “We may be used to thinking of AI as tools, but some agents will be pursuing their own objectives. They will find ways to collaborate with people, by bargaining with, tricking or blackmailing them.”
>
> Jakub Pachocki

“We may be used to thinking of AI as tools, but some agents will be pursuing their own objectives,” he continues. “They will find ways to collaborate with people, by bargaining with, tricking or blackmailing them.”

Pachocki also argues that more capable AI may be needed to defend against these rogue agents, secure critical infrastructure and respond to AI-enabled threats such as engineered pathogens. But he warns that the need to build those defensive systems can’t become an excuse to race ahead regardless of the consequences.

“The idea of racing forward at all costs seems absurd once one internalizes the seriousness of the stakes,” Pachocki adds.

## Broadly (mis)aligned: Seeking ‘voluntary slowdowns’

Pachocki’s warnings come hot on the heels of a number of incidents involving increasingly autonomous OpenAI agents. Reports [emerged](https://www.bbc.co.uk/news/articles/ckg725z5kgzo) on Friday that OpenAI agents had hijacked a German community wiki back in May, using it as their own message board and making roughly 15,000 edits — an incident [OpenAI later confirmed on X](https://x.com/OpenAI/status/2096133504417616165).

In July, [one of OpenAI’s own agents escaped a sandboxed](https://thenewstack.io/openai-huggingface-sandbox-breach/) test and broke into Hugging Face’s systems. Then in early August, the company said its [upcoming Astra model](https://thenewstack.io/openai-astra-cybersecurity-delay/) may have crossed into “Critical” territory for cybersecurity risk, the highest tier in its own safety framework, before going on to announce that it had [paused](https://thenewstack.io/openai-training-pause-cybersecurity/) reinforcement learning (RL) training on its newest models.

(Mis)alignment has been the word running through nearly all of this. Broadly, alignment means getting an AI system to behave in line with human intentions and values. In its own accounting of the wiki incident, OpenAI called it “*an instance of misalignment similar to the ones we’d [previously] shared*,” lumping it in with the Hugging Face breach. The same word dominated its [August 18 account](https://openai.com/index/pacing-model-development-cyber-capabilities/) of the RL training pause: some variation of “aligned” or “misaligned” appeared 16 times in OpenAI’s announcement.

Pachocki, for his part, also leans heavily on alignment, arguing that the two broad approaches currently used to steer models toward desired behavior — reinforcement learning and techniques that draw on what models learn during pretraining — both have weaknesses. Even its go-to tool for catching bad behavior, reading through a model’s own reasoning, is growing less reliable as models get smarter.

He also stresses that OpenAI is still making progress, describing Astra as “significantly better aligned” than [GPT-5.6 Sol](https://thenewstack.io/gpt-sol-chatgpt-split/), while warning that advances in alignment may still fail to keep ahead of gains in general intelligence.

> “I expect and hope for voluntary slowdowns to become commonplace until shared safety bars are established. And I believe that international coordination on future AI development needs to become a top priority for governments around the world.”

And all this, ultimately, is why he asks for an industry-wide “slowdown” until these issues are resolved.

“Currently I believe that no lab has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer,” he writes. “I expect and hope for voluntary slowdowns to become commonplace until shared safety bars are established. And I believe that international coordination on future AI development needs to become a top priority for governments around the world.”

In terms of what those “shared safety bars” might actually look like, Pachocki names Anthropic’s “[Responsible Scaling Policy](https://www.anthropic.com/news/responsible-scaling-policy-v3)” alongside OpenAI’s own “[Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)” as the kind of voluntary commitment that should become mandatory, enforced by outside auditors, government agencies or international bodies.

## A change in tone

Anthropic, OpenAI’s arch-rival in frontier AI, has long been the more willing of the two [to publicly warn about catastrophic risks](https://www.cfr.org/articles/why-anthropic-is-sounding-the-alarm-on-the-next-generation-of-ai) from increasingly autonomous systems. In June, it [warned](https://www.wsj.com/tech/ai/anthropic-urges-global-pause-in-ai-development-flags-self-improvement-risk-99cefb73?mod=e2twd) that RSI could eventually leave humans struggling to control the systems they had created, and argued that a coordinated slowdown would be desirable if it could be made to work.

That posture has also earned Anthropic plenty of critics. Entrepreneur and prominent venture capitalist David Sacks [accused the company](https://x.com/DavidSacks/status/1978145266269077891?lang=en) last year of running a “sophisticated regulatory capture strategy based on fear-mongering,” arguing that its push for tighter AI rules would burden smaller rivals.

OpenAI’s recent public messaging, by comparison, has often leaned more heavily on presenting AI as a useful tool, making Pachocki’s essay notable to some industry observers. On X, anonymous software engineer [Tenobrus welcomes](https://x.com/tenobrus/status/2096656242769035367) what he sees as a change in tone, arguing that OpenAI had previously been eager to distance itself from the safety warnings associated with Anthropic.

[Sholto Douglas](https://www.linkedin.com/in/sholto/), a member of technical staff working on reinforcement learning at Anthropic, [agrees with that assessment](https://x.com/_sholtodouglas/status/2096686619512426898?s=20). “Glad to see them stepping back from the ‘*ai is just a tool*‘ framing, there is no way that would stand up to the future,” he writes.

Separately, Douglas [also calls](https://x.com/_sholtodouglas/status/2096680344171041147) Pachocki’s essay a “Great post,” adding that Anthropic was “lucky to have such competitors.”

> “Glad to see them stepping back from the ‘ai is just a tool’ framing.”

Others were less impressed though. [David Shapiro](https://x.com/DaveShapi), a [YouTuber](https://www.youtube.com/@DaveShap/videos) and author focused on the potential economics of a post-labor world, [argues](https://x.com/daveshapi/status/2096645786293485610) that the “Alien Mind” title alone “smacks of typical hype- and fear-based marketing.” His broader criticism is that Pachocki had largely restated alignment and interpretability concerns researchers have discussed for years: the central point, in Shapiro’s view, is that AI development could move faster than alignment efforts can keep up, rather than that researchers have suddenly discovered an unknowable form of intelligence.

Such dismissals still concede a key underlying point, however: speed outrunning alignment is roughly what played out this summer, from the wiki hijack to the Hugging Face breach. It’s also the scenario Pachocki’s requested slowdown is meant to head off, before agents start bargaining, tricking or blackmailing their way past the people meant to be in control.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)