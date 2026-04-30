AWS is finally closing the gap for developers who want OpenAI models without leaving the Amazon ecosystem. Speaking at an event in San Francisco this week, AWS CEO Matt Garman unveiled three major Bedrock integrations — headlined by the arrival of OpenAI’s GPT-5 family — designed to end the forced choice between AWS infrastructure and OpenAI’s top-tier intelligence

Here’s how Garman framed it on stage: “We’ve forced them for the last couple of years to have to, to get the great OpenAI models, to go to other places, and they didn’t like that. Now I think we don’t force people to have to make that choice.”

All three new offerings are currently in limited preview, starting with the latest OpenAI models: GPT-5.4 is available now, and GPT-5.5 is expected in the coming weeks. Also joining the Bedrock lineup is Codex, OpenAI’s coding agent, which already sees 4 million weekly users. Finally, the “Stateful Runtime Environment” first teased in February has been productized as Amazon Bedrock Managed Agents, powered by OpenAI.

## The detail nobody is naming

Eight days before the event, on April 20, AWS and Anthropic [announced an expanded collaboration](https://thenewstack.io/anthropic-amazon-aws-investment/). Anthropic committed more than $100 billion to AWS over the next ten years. The press release language matters. Anthropic secured up to 5 gigawatts of new capacity to train and run Claude.

The commitment spans Graviton and Trainium2 through Trainium4 chips. Andy Jassy’s quote in the [press release](https://www.anthropic.com/news/anthropic-amazon-compute#:~:text=%E2%80%9CAnthropic%27s%20commitment%20to%20run%20its%20large%20language%20models%20on%20AWS%20Trainium%20for%20the%20next%20decade%20reflects%20the%20progress%20we%27ve%20made%20together%20on%20custom%20silicon%2C%20as%20we%20continue%20delivering%20the%20technology%20and%20infrastructure%20our%20customers%20need%20to%20build%20with%20generative%20AI.%E2%80%9D) seals it: “Anthropic’s commitment to run its large language models on AWS Trainium for the next decade reflects the progress we’ve made together on custom silicon.”

Eight days later, the OpenAI announcement is also a Trainium story. The February deal that this week’s event productized committed OpenAI to consume approximately 2 gigawatts of Trainium capacity, spanning Trainium3 and Trainium4. (*The Register* reports the 2GW commitment is also tied to the [remaining $35 billion of Amazon’s investment](https://www.theregister.com/2026/04/28/openai_climbs_into_amazons_bedrock/), though Amazon’s official text only says the second-stage investment depends on “certain conditions” without disclosing them.)

> Two AI labs that compete on every benchmark, every architectural choice, and every safety philosophy just made parallel multi-year commitments to the same custom-silicon roadmap.

Two AI labs that compete on every benchmark, every architectural choice, and every safety philosophy just made parallel multi-year commitments to the same custom-silicon roadmap. Neither lab is exclusive. Anthropic still uses [TPUs from Google and NVIDIA GPUs](https://www.anthropic.com/news/anthropic-amazon-compute), and OpenAI keeps Microsoft as its primary cloud partner. But the parallel scale of the AWS commitments, on AWS-designed silicon, in the same window, is a specific event worth naming.

## Why this is not the Azure story

Microsoft will respond by reminding everyone that [Foundry has both Claude and GPT](https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/). True. Microsoft made that claim in February. But the comparison falls apart at the workload layer.

[Anthropic’s own documentation](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) on the Foundry integration is unusually direct. The “Preview” section states that Claude models on Foundry run on Anthropic’s infrastructure. Foundry handles billing, authentication, and Azure-hosted endpoints. Inference happens elsewhere.

Compare with Anthropic’s [Bedrock documentation](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock). The opening line. “Claude in Amazon Bedrock runs on AWS-managed infrastructure with zero operator access.” Anthropic personnel have no access to the inference infrastructure. The model runs inside the AWS security boundary. That is a different deployment model.

> Bedrock now has a stronger structural claim to cloud-native inference for both Claude and OpenAI models than it did a week ago.

The same difference now applies to OpenAI. On Foundry, OpenAI inference has been Azure-native for years. On Bedrock, OpenAI inference is moving onto AWS infrastructure under a multi-gigawatt Trainium commitment. The Foundry distinction is real for Claude. For OpenAI, it is too early to claim Bedrock has the workloads. What you can say is that Bedrock now has a stronger structural claim to cloud-native inference for both Claude and OpenAI models than it did a week ago.

## The silicon convergence

For two years, the cloud-AI conversation has been about model choice. Anthropic versus OpenAI versus Google. Bedrock versus Foundry versus Vertex. The chips powering all of it have largely been NVIDIA GPUs, with Google’s TPUs as the major alternative and AWS Trainium gaining ground inside Anthropic’s stack.

Custom silicon is the new layer of competition. AWS got both top labs to commit to its silicon roadmap, and the architecture is no accident. Anthropic [works closely with Annapurna Labs](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai), AWS’s chip design team, with engineering teams “communicating on an almost daily basis on everything from low-level optimization work to high-level architectural decisions for next-generation chips.” OpenAI’s commitment also extends to future Trainium generations, with [Trainium3 UltraServers](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-anthropic-meta-partnership-aws-lambda-s3-files-amazon-bedrock-agentcore-cli-and-more-april-27-2026/) announced at re:Invent 2025 and Trainium4 in development.

The strategic read writes itself. Trainium changes the margin structure for AI inference on AWS. Nvidia still ships the GPUs that serve most workloads today. But every gigawatt that moves to Trainium is a gigawatt where AWS captures more of the silicon margin than it would on pure NVIDIA. Jassy disclosed in his recent shareholder letter that AWS’s custom silicon business [generates more than $20 billion in revenue an](https://www.geekwire.com/2026/openais-models-land-on-amazon-bedrock-one-day-after-microsoft-exclusivity-ends/)[nually](https://www.geekwire.com/2026/openais-models-land-on-amazon-bedrock-one-day-after-microsoft-exclusivity-ends/). The Trainium roadmap is no longer a research project.

For the labs themselves, the calculation is supply security. Anthropic [reported run-rate revenue of $30 billion](https://www.anthropic.com/news/anthropic-amazon-compute), up from approximately $9 billion at the end of 2025. Capacity is the constraint. Trainium delivers committed gigawatts on a known schedule. Globally, GPU supply is tight and contested.

## What shipped this week

The three products on Bedrock all run inside AWS infrastructure.

OpenAI frontier models on Bedrock inherit the [full set of enterprise controls](https://www.aboutamazon.com/news/aws/bedrock-openai-models) AWS customers already use. IAM-based access management, AWS PrivateLink connectivity, guardrails, encryption, CloudTrail logging, and existing compliance frameworks. Customers can apply OpenAI usage toward existing AWS cloud commitments. There is no separate procurement, no new security model.

By bringing Codex into the AWS security boundary, developers can now run OpenAI’s coding agent using native AWS credentials and infrastructure. This integration ensures that all inference runs through Bedrock, with usage costs applying directly toward existing AWS cloud commitments. Furthermore, the Codex CLI, desktop app, and Visual Studio Code extensions have been updated to natively target Bedrock endpoints.

Bedrock Managed Agents is the most architecturally interesting of the three. The product is built with the OpenAI agent harness, which AWS VP Anthony Liguori described on stage as the runtime, environment, and inference API that OpenAI uses internally.

AWS’s [own description](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/) calls the harness “engineered for faster execution, sharper reasoning, and reliable steering of long-running tasks.” The harness is optimized for OpenAI frontier models. The agent gets memory that persists across sessions, identity that enforces permissions, skills that encode procedures, and compute options sized to the task. AgentCore provides the default compute environment, with authorization enforcement and observability layered on top.

This is a tighter coupling between model and runtime than other agent platforms have offered. Whether that translates into measurable performance gains in production remains to be seen.

## The honest caveats

Three things to flag before this frame gets oversold.

Both labs run multi-cloud strategies. Anthropic’s [March 2026 deal with Google and Broadcom](https://www.anthropic.com/news/anthropic-google-cloud-tpu) added “multiple gigawatts” of TPU capacity to come online in 2027. Anthropic also has a [$30 billion Azure commitment](https://news.microsoft.com/source/2025/11/anthropic-microsoft-nvidia-strategic-partnerships/) from November 2025. OpenAI keeps Microsoft as its primary cloud partner under the [revised April 27 agreement](https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/), with substantial Azure consumption committed for years. The 5GW and 2GW Trainium numbers are large, but they are not the only chips either lab uses.

Trainium is also not yet battle-tested at the OpenAI training scale. Trainium2 is in production. Trainium3 was [released in December 2025](https://aws.amazon.com/about-aws/whats-new/2025/12/aws-trainium3-ultraservers-generally-available/). Trainium4 is not yet commercially available. Anthropic already trains and serves Claude on Trainium2 across [Project Rainier](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai), one of the world’s largest AI compute clusters. I have not found public evidence of OpenAI training a frontier model end-to-end on Trainium. Until that ships, “OpenAI on Trainium” is mostly an inference and capacity-reservation story.

AWS also still ships Nova as a first-party model. The neutral-shelf framing has limits. AWS competes with both partners at the model layer even while it co-locates them at the silicon layer.

## What every other cloud now has to answer

Microsoft has equity in OpenAI and remains the primary cloud partner. What Microsoft does not have is OpenAI training and inference workloads on Microsoft custom silicon at the scale AWS just landed. Maia, Microsoft’s chip program, is real, but the public record does not show a comparable lab commitment.

Google has TPUs and Anthropic running on them at scale. Google has not announced a comparable OpenAI commitment to its custom silicon. Google also runs Gemini as a first-party flagship, which makes Vertex less of a neutral shelf and more of a Google-coded one.

> For the first time, you can pick between Claude and GPT without picking between clouds, runtimes, or chip roadmaps.

Nvidia still wins in every cloud. The margin floor for inference on the largest cloud just shifted. Every gigawatt of Trainium that comes online is a gigawatt where AWS captures more of the silicon stack than it would on pure NVIDIA.

For developers building on Bedrock, the practical change is sharper than the headlines suggest. For the first time, you can pick between Claude and GPT without picking between clouds, runtimes, or chip roadmaps. Both Anthropic and OpenAI are now tied to multi-year Trainium commitments. Both have managed agent runtimes co-engineered with their model providers. The lock-in is real, the choice is real, and they are happening at the same time.

Call it silicon convergence. The story under the OpenAI on Bedrock headline is that two of the most competitive AI labs in the world have now anchored multi-year commitments to AWS-designed silicon. The agreement is what makes today’s products possible. It is also part of today’s announcement that will still matter in a year.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)