The independence developers gain from open weights comes with a hard infrastructure ceiling, according to Anthropic CEO Dario Amodei.

“AI is structurally a technology that tends to concentrate power, for reasons that have nothing to do with regulation,” Amodei wrote during a public [exchange on X](https://x.com/DarioAmodei/status/2088758816376807762) with investor [Gavin Baker](https://www.linkedin.com/in/gavinbaker-portfoliomanager/). He attributed that concentration to scaling laws rather than government policy.

“Open-weights do help some with this but are nowhere near a sufficient solution because they simply shift the concentration somewhat to those with the most compute and chips,” he added.

What began as an argument over whether regulation makes AI safer or gives too much power to a handful of companies left developers with a practical question once again: Does owning the weights provide real independence when someone else still controls the compute?

> “Open-weights do help some with this but are nowhere near a sufficient solution because they simply shift the concentration somewhat to those with the most compute and chips.”

## Regulation without regulatory capture

Gavin Baker, managing partner at Atreides Management, framed the debate as a choice between concentrating powerful models among a few regulated companies or distributing them widely without the same guardrails, citing Meta CEO Mark Zuckerberg’s argument that placing AI in the hands of a small number of supposedly responsible organizations creates its own danger.

“The notion that AI is so dangerous that the only safe path is an extreme concentration of power seems inherently problematic,” Zuckerberg wrote in the statement quoted by Baker.

Baker argued that putting more models into circulation would spread power and improve the odds that people could use systems reflecting their values. He also said Amodei’s repeated warnings about AI risk could strengthen opposition to new data centers, limiting the infrastructure needed to deliver the technology’s potential benefits.

Amodei rejected the choice between regulation and distribution.

> “I know that there’s a sort of Silicon Valley shorthand where regulation = regulatory capture = concentration of power, but I’ve always found this to be an overly simplified picture of the world.”

“I know that there’s a sort of Silicon Valley shorthand where regulation = regulatory capture = concentration of power, but I’ve always found this to be an overly simplified picture of the world,” he wrote.

He argued that regulation can constrain powerful companies when the requirements are based on objective standards. At their best, Amodei said, institutions “vest power in ideas rather than people, and thereby decentralize that power.”

## Compute limits open-weight independence

Open weights allow developers to adapt a model and keep sensitive data inside their own environment, but that becomes harder as models grow. And while smaller teams can rent the hardware, they remain exposed to its cost and availability. That problem is already visible as [five European companies recently agreed to purchase AI compute that doesn’t exist yet](https://thenewstack.io/mistral-third-party-open-models/).

As you may recall, Anthropic was one of the few major AI labs that did not sign the [July 24 letter organized by Nvidia](https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf) with its signatories arguing that open weights encourage competition by giving customers an alternative to proprietary APIs.

Amodei later said Anthropic does not support a blanket ban. He called open models without dangerous capabilities “a public good,” but his position changes once a model can help someone carry out a serious attack. [Real-world containment failures have already shown](https://thenewstack.io/anthropic-claude-containment-failure/) how difficult it can be to control a capable model, even before its weights are released.

Once the weights are public, the original developer can’t retrieve every copy or prevent users from removing its safeguards. Amodei wants models that reach that level to undergo mandatory safety testing, regardless of how they are released. Anthropic has carried that position beyond its own products and recently [backed an urgent call for the most powerful AI labs to hit the brakes](https://thenewstack.io/ai-pause-framework-letter/).

> “We try very hard to make proposals that disadvantage (slow down) frontier AI companies while advantaging smaller competitors.”

## Tiered rules protect smaller labs

Amodei disputes the argument that AI regulation will inevitably protect Anthropic and other incumbents from competition. He says the company has supported frameworks that place stricter requirements on frontier labs while exempting smaller developers.

“We try very hard to make proposals that disadvantage (slow down) frontier AI companies while advantaging smaller competitors,” he wrote.

Anthropic supported California’s SB 53, which defines a frontier model as one trained using more than (10^{26}) floating-point operations, or FLOPs. Developers earning more than $500 million a year face additional requirements, including publishing a framework explaining how they test for and respond to catastrophic risks.

Amodei has called for a similar distinction in federal policy.

“The testing process we’ve advocated for at CAISI and the White House involves more rigorous tests for frontier models than off-frontier models,” he wrote. He said that approach would give challengers room to catch up while slowing the companies already building the most capable systems.

He also supports DeepMind CEO Demis Hassabis’ proposal for a FINRA-like AI standards body. Under that framework, models would be classified as frontier systems after crossing regularly updated benchmark thresholds. The same rules would apply to open and closed models.

## Capability defies simple thresholds

Training compute gives developers a threshold they can anticipate, but it may not capture capabilities added through fine-tuning or external tools. Benchmarks can measure those abilities more directly, although their results rarely provide a clean dividing line.

[OpenAI has already built a model it doesn’t want most people to use](https://thenewstack.io/openai-gpt56-cyber-daybreak/) and another [it won’t release until its safety testing catches up](https://thenewstack.io/openai-astra-cybersecurity-delay/). Both offer an early look at how difficult capability classification may become.

The U.S. Center for AI Standards and Innovation found that Moonshot AI’s Kimi K3 remained behind the strongest closed models in preliminary cyber evaluations. During a simulated attack against a small corporate network, however, it completed the full 32-step attack path in one of 10 attempts.

Kimi K3 failed to achieve arbitrary code execution on any of the 41 ExploitBench samples. The most capable models achieved it on average of 20. The version tested before release may also behave differently after a developer fine-tunes it or connects it to external tools. [DeepSeek underscored that problem when its smaller model outperformed its own flagship](https://thenewstack.io/deepseek-v4-flash-open-weights/), showing that model size alone doesn’t provide a reliable measure of capability.

Amodei’s proposal would spare most smaller developers from the toughest rules. Regulators would still have to decide when one of those challengers has crossed into frontier territory, ideally before its weights are released and modified beyond the creator’s control.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)