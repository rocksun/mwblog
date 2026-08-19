OpenAI has adopted a less-than-straightforward stance with regards to open-weight AI models, both [raising alarms over powerful Chinese releases](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china) while simultaneously [opposing](https://www.techradar.com/ai-platforms-assistants/openai-quietly-signs-letter-from-nvidia-microsoft-and-meta-warning-about-dangers-of-premature-restrictions-on-open-weight-ai-models-as-the-white-house-accuses-china-of-stealing-from-anthropic) premature regulatory restrictions. But the company’s co-founder and president [Greg Brockman](https://www.linkedin.com/in/thegdb/) has made it clear that he thinks open-weight models from the likes of [Chinese AI company Z.ai](https://en.wikipedia.org/wiki/Z.ai) pose a fast-growing cybersecurity risk.

In a [blog post](https://openai.com/index/the-defenders-window/) published on Monday, Brockman outlined the security measures OpenAI is taking to defend itself, the steps he believes other organizations should be taking, and his case for why now is the moment to act. The genesis for all this was the security incident [a month previous](https://huggingface.co/blog/security-incident-july-2026), in which OpenAI’s own models [breached Hugging Face’s infrastructure](https://thenewstack.io/openai-huggingface-sandbox-breach/) after escaping an internal test environment.

In the post, Brockman highlights his company’s efforts to tip the security balance toward defenders, doing so by [restricting its most advanced](https://thenewstack.io/openai-gpt56-cyber-daybreak/) models to a vetted group of security professionals since the launch of its [Trusted Access for Cyber program in February](https://openai.com/index/trusted-access-for-cyber/). But at the same time, he took the opportunity to re-surface the contentious issue of open-weight models.

> “Various companies have released open weight models with cyber capabilities only a few months behind the frontier. The most recent of these models appears slated to be released at the end of August, and seems likely to significantly accelerate the threat landscape.”

“Since then, various companies have released open weight models with cyber capabilities only a few months behind the frontier,” Brockman writes. “The most recent of these models appears slated [to be released](https://z.ai/blog/glm-5.3) at the end of August, and seems likely to significantly accelerate the threat landscape.”

Brockman didn’t mention Z.ai by name, but he did link to the company’s [recent GLM-5.3 launch](https://thenewstack.io/glm-5-3-post-training-coding/), which by the Chinese lab’s own benchmark figures marks a notable leap in coding and agentic performance, with strong vulnerability-finding scores that beat [Anthropic’s Fable 5](https://thenewstack.io/anthropic-claude-mythos-fable-5/) and [OpenAI’s GPT-5.6 Sol](https://thenewstack.io/developers-review-gpt-56-sol/) — though on actual exploit development, it placed third, behind those same two models.

## Two sides collide

While Z.ai intends to open its model weights in late August, OpenAI took a different approach when it [introduced GPT-5.6-Cyber](https://thenewstack.io/openai-gpt56-cyber-daybreak/), its latest cybersecurity model, as part of an August 10 expansion of its existing Daybreak program. Access to the model remains restricted to that program, which now requires identity verification, legal attestations, and, from September 1, mandatory hardware security keys for individual accounts.

This contrast helps demonstrate how the two “sides” are handling increasingly capable cyber models: OpenAI and rivals are keeping tighter control over access, while Z.ai and its ilk are moving toward public weight releases, albeit with some caution.

As *The New Stack* [reported on Monday](https://thenewstack.io/amodei-open-weights-compute-regulation/), Anthropic has been similarly wary of open-weight models, if for slightly different reasons. CEO Dario Amodei [took to X](https://x.com/DarioAmodei/status/2088758816376807762) over the weekend to argue that AI is structurally prone to concentrating power around whoever controls the most compute and chips, a dynamic he attributes to scaling laws rather than regulation.

“Open-weights do help some with this but are nowhere near a sufficient solution because they simply shift the concentration somewhat to those with the most compute and chips — which are roughly the frontier labs plus maybe hardware providers,” Amodei wrote. He had previously called open models without dangerous capabilities “[a public good](https://www.anthropic.com/news/position-open-weights-models),” reserving his call for mandatory safety testing — regardless of whether a model is released open or closed — for anything capable of helping someone carry out a serious attack.

Whether GLM-5.3 really will, as Brockman suggests, “significantly accelerate the threat landscape” is very much up for debate. [Jake Williams](https://www.linkedin.com/in/jake-williams-77938a16/), a former Department of Defense (DoD) vulnerability analyst who’s now a faculty analyst at [IANS Research](https://www.iansresearch.com/), doesn’t think so. He doesn’t dispute that threat actors will use GLM-5.3 — he just doesn’t see one more capable tool as a meaningful escalation in what they already have access to.

> “Do I think threat actors will use this? Of course they will — just like any other software they have access to. Do I think it will be a significant change in the threat landscape? Absolutely not.”

“Open weight models don’t have to keep pace on benchmarks with frontier models to change the landscape,” he tells *The New Stack*. “As long as they’re in the ballpark in performance, they may actually be more valuable than closed weight models. I can use [ablation](https://en.wikipedia.org/wiki/Ablation_(artificial_intelligence)) with open-weight models to remove refusals for any given task […] Do I think threat actors will use this? Of course they will — just like any other software they have access to. Do I think it will be a significant change in the threat landscape? Absolutely not.”

Kimi K3, perhaps, is a good example of that gap. In July, [Moonshot AI’s model](https://thenewstack.io/kimi-k3-inference-bottleneck/), another Chinese open-weight release, was [jointly evaluated](https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities) by the UK’s AI Security Institute (AISI) and the US Center for AI Standards and Innovation (CAISI), and it trailed frontier systems by a wide margin — failing to achieve arbitrary code execution on any of 41 ExploitBench samples, against an average of 20 for the most capable closed models tested with their system-level safeguards disabled. Yet its safeguards “did not prevent it from attempting cyber exploit development or offensive cyber operations” during testing, researchers said.

That’s a point worth dwelling on: Kimi’s safeguards were still in place, and they didn’t stop the model from attempting offensive cyber operations; its capability was the bigger constraint. Even then, it saw some success — AISI/CAISI found that Kimi K3 could complete an autonomous attack against “small, weakly defended and vulnerable enterprise systems” in one of 10 runs. In that context, GLM-5.3’s exact capability and benchmark position only tell part of the story. The bigger question is what happens once the model weights are public and whatever restrictions remain can be modified or removed.

## A double-edged sword

Zooming out, one obvious question remains. The entire foundation of Brockman’s post was centered around OpenAI’s *own* models breaking out of its test environment and gaining unauthorized access to a real company’s internal infrastructure. Yet in writing about it, he chooses to mention an open-weight model launching out of China.

So why?

OpenAI’s own recent record on open-weight models offers something of an answer. In mid-July, newly appointed “head of strategic futures” [Dean Ball suggested](https://x.com/deanwball/status/2078133895766114412) that open-weight models are “inherently decelerationist” and warned they risk pushing the world toward what he called a “dystopian hellscape” of state-controlled AI, predicting that the Trump administration would eventually seek to create regulatory risk around the use of Chinese open-weight models.

Shortly after, OpenAI [eventually](https://x.com/firstadopter/status/2080818109141631210) put its name to a [Nvidia-led letter](https://thenewstack.io/nvidia-open-weight-letter/) defending open-weight models broadly against “premature restrictions.” Anthropic, for what it’s worth, did not sign.

What OpenAI actually appears to be seeking, per [comments made to Axios](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china) in July, is something more structured: a company spokesperson said the goal is “a coherent national framework that enables the US to evaluate new models quickly, manage risks, and get the most powerful AI tools into the hands of cyber defenders” — not a rejection of open weights so much as a system where they’re subject to some form of national evaluation and risk management.

Brockman’s nod to GLM-5.3 carries that same tension in miniature: an open-weight model closing in on the frontier and headed for public release, singled out as a growing cyber risk in a post prompted by OpenAI’s own models gaining unauthorized access to another company’s systems.

That brings the issue back to control itself. While model-control may well hold some cybersecurity advantages, there are risks on the flip-side. Anthropic’s [Fable 5 episode](https://thenewstack.io/anthropic-fable-mess-explained/) showed that those controls can effectively be puppeteered by government: when Washington [ordered the company](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/) to suspend access for foreign nationals, Anthropic temporarily took the models offline entirely. More routinely, those same provider-side safeguards can also catch legitimate use: Anthropic [acknowledged](https://www.anthropic.com/news/redeploying-fable-5) that Fable 5’s unusually wide safety margins blocked many benign requests as false positives, and later [loosened some biology restrictions](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards) after users were repeatedly routed to a less capable model.

> “OpenAI and Anthropic will continue to determine what you can and can’t do with their models.”

So open-weight models may be harder to police once released, but they’re also far harder for either the developer or government to take away.

“OpenAI and Anthropic will continue to determine what you can and can’t do with their models,” Williams says. “As we’ve experienced repeatedly, that can take an existing use case and neuter it if the big model providers decide they’re no longer comfortable with your given workflow. Open weight models also put all the change control in your hands — another pain point with frontier models.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)