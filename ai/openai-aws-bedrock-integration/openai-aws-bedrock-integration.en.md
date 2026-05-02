OpenAI wasted little time since [announcing changes](https://thenewstack.io/openai-microsoft-partnership-restructured/) to its partnership with Microsoft on Monday. The ChatGPT hitmaker is now [bringing its models](https://openai.com/index/next-phase-of-microsoft-partnership/), coding tools, and agentic capabilities to Amazon Web Services (AWS), with a new set of integrations launching on [Bedrock](https://aws.amazon.com/bedrock/) — AWS’s [platform for building](https://thenewstack.io/mcp-summit-aws-bedrock/) and deploying AI applications.

For AWS customers, this means they can now access OpenAI’s models and tools natively within their existing cloud environments, rather than relying on external APIs or Azure-based services. It also places OpenAI’s technology alongside rival models already available on Bedrock, such as [those from Anthropic](https://aws.amazon.com/bedrock/anthropic/), giving enterprises more flexibility in how they build and deploy AI systems.

The seven-year saga has brought Microsoft and OpenAI countless breakthroughs and flashpoints, with both companies ultimately seeking a path to greater flexibility and freedom. Which of them stands to benefit most from that newfound room to maneuver is up for debate — but AWS is well-positioned to capitalize on the shift.

But how did we get here?

## The story so far

Microsoft and OpenAI’s tumultuous tie-up dates back to 2019, when [Microsoft invested $1 billion](https://openai.com/index/microsoft-invests-in-and-partners-with-openai/) in the then-upstart lab and became its exclusive cloud provider. The deal gave Microsoft early access to OpenAI’s models, while anchoring OpenAI’s training and deployment stack on Azure. Subsequent investments deepened that tie, including a major 2023 deal, bringing Microsoft’s total investment to a [reported $13 billion](https://www.nytimes.com/2023/01/23/business/microsoft-chatgpt-artificial-intelligence.html) and securing a significant minority stake in OpenAI’s for-profit arm, thought to be just shy of 50%.

The relationship has also faced more than a few moments of instability. In November 2023, OpenAI’s board abruptly ousted CEO Sam Altman, prompting Microsoft to hire him — only for [Altman to return](https://thenewstack.io/why-microsoft-has-to-save-openai/) to OpenAI days later after internal backlash.

While that episode exposed fault lines, it didn’t alter the underlying incentives that tied the two companies together. For Microsoft, it offered a way into the emerging market for large language models (LLMs), at a time when it lacked a comparable in-house offering. For OpenAI, it provided the compute, capital, and distribution needed to train increasingly large systems and reach enterprise customers.

But the cozy coupling came with trade-offs. As OpenAI’s ambitions grew, so too did its infrastructure needs, placing increasing strain on Azure’s capacity and tying the company to a single cloud at a time when enterprises were spread across multiple providers. That pressure was already starting to show by mid-2025, when reports emerged that [OpenAI had struck a deal with Google Cloud](https://www.cnbc.com/2025/07/16/openai-googles-cloud-chatgpt.html), adding to a mix of providers including Microsoft, [CoreWeave](https://www.coreweave.com/news/coreweave-announces-agreement-with-openai-to-deliver-ai-infrastructure), and Oracle, to supplement its compute needs — a move that pointed to growing cracks in the single-provider setup.

> “Our customer demand continues to exceed our supply.”

On its [Fiscal Year 2026 Q2 earnings call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) in January, Microsoft alluded to exactly that pressure, with CFO [Amy Hood](https://www.linkedin.com/in/amyhood1/) stating that “our customer demand continues to exceed our supply,” as the company poured tens of billions into GPUs and data center buildouts to keep pace with AI workloads.

Notably, the company also disclosed that roughly 45% of its commercial remaining performance obligation — effectively its future contracted cloud revenue — is tied to OpenAI, underscoring just how central the partnership had become to Azure’s growth.

Put simply, OpenAI was not only a major source of demand for Azure, but also a significant draw on the very capacity Microsoft was racing to expand.

But perhaps more than that, it also left Microsoft heavily exposed to a single partner at a time when the market was moving toward a multi-model approach. And as such, it had already begun responding to that reality ahead of this week’s big news.

## “Broad model choice”

During the same earnings call in January, Microsoft CEO [Satya Nadella](https://www.linkedin.com/in/satyanadella/) pointed to a broader set of pressures shaping its cloud strategy, including growing demand for sovereignty — not just where data sits, but who controls it across regions and environments. That, in turn, places a premium on flexibility in how AI systems are built and deployed.

> “Our customers expect to use multiple models as part of any workload.”

“It starts with having broad model choice,” Nadella said during the call. “Our customers expect to use multiple models as part of any workload that they can fine-tune and optimize based on cost, latency, and performance requirements.”

He framed this in the context of a wider reset in how software is being built, arguing that “like in every platform shift, all software is being rewritten” and that “you can think of agents as the new apps.”

In that paradigm, applications aren’t tied to a single model; instead, they draw on different models depending on the task, making flexibility in model choice a core requirement.

Microsoft’s response has been to position [Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) — its platform for building, deploying, and managing AI models and agents — as a multi-model environment. While Foundry already supported a range of models, including those from [Deepseek](https://azure.microsoft.com/en-us/blog/deepseek-r1-is-now-available-on-azure-ai-foundry-and-github/) and [Cohere](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/cohere-models-now-available-on-managed-compute-in-azure-ai-foundry-models/4423428), Microsoft began adding Anthropic’s Claude models [in November 2025](https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/), bringing a direct rival to OpenAI into the same platform.

![Model choice in Foundry](https://cdn.thenewstack.io/media/2026/04/d878bce1-recording-2026-04-30-094937.gif)

***Model choice in Foundry***

The company has [said](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) more than 1,500 customers are already using both OpenAI and Anthropic systems through Foundry, while pointing to a separate [$30 billion compute commitment](https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/) from Anthropic.  
In effect, Microsoft was already hedging — building out a multi-model ecosystem even while its deepest ties remained with OpenAI.

And so that tension set the stage for this week’s reset, with both companies moving to loosen the terms of their agreement and open the door to a more flexible arrangement.

In real terms, this meant ending Azure’s exclusivity as the sole cloud provider, allowing OpenAI to run and serve its models across other clouds, while Microsoft retains access to OpenAI models under a now non-exclusive license and continues as a major shareholder.

A reset that, effectively, gives both sides more room to maneuver.

## OpenAI and AWS deepen ties with Bedrock rollout

Just as Microsoft has been laying the groundwork for flexibility, OpenAI and AWS have been doing the same for some time.

For context, developers have long been able to use OpenAI’s models from within AWS by [calling its public API](https://thedeveloperspace.com/how-to-invoke-openai-apis-from-aws-lambda-functions/). AWS has also supported a small subset of OpenAI’s [open-weight GPT-OSS models](https://www.forkable.io/i/170464622/the-return-of-openai) through [Bedrock and SageMaker](https://www.aboutamazon.com/news/aws/openai-models-amazon-bedrock-sagemaker).

But the “relationship” took a more [formal turn in February](https://www.aboutamazon.com/news/aws/amazon-open-ai-strategic-partnership-investment) via a multi-year partnership spanning infrastructure, enterprise tooling, and custom silicon, with Amazon investing $50 billion in OpenAI.

This was perhaps the clearest signal yet that whatever “exclusivity” deal was in place was on shaky ground at best, with reports emerging in March that [Microsoft was mulling legal action](https://www.ft.com/content/e814f4c3-4fb5-4e2e-90a6-470044436b39?syn-25a6b1a6=1) against Amazon and OpenAI over the deal.

The agreement outlined plans to bring OpenAI’s models and agent platforms to Bedrock, alongside the development of a so-called “stateful runtime environment” to support more complex, long-running AI workloads. It also included a significant compute commitment, with OpenAI agreeing to consume large-scale capacity on [AWS’s Trainium chips](https://aws.amazon.com/ai/machine-learning/trainium/) as part of the deal.

The latest announcement builds directly on that foundation. OpenAI’s models are now becoming available through Bedrock, giving AWS customers access through the same APIs, security controls, and governance frameworks they already use. Codex, OpenAI’s coding agent, is also being brought into Bedrock, allowing teams to run development workflows without leaving their existing AWS environments.

Alongside this, Amazon is introducing Bedrock Managed Agents, powered by OpenAI, to help enterprises deploy agents that can perform multi-step tasks across internal systems without assembling the underlying infrastructure themselves.

All three components are launching in a limited preview, and together they mark a major shift toward integrating OpenAI’s tools more tightly into AWS’s platform.

## So… who’s the real winner here?

Depending on who you listen to, either OpenAI or Microsoft was the big winner from the deal announced on Monday.

OpenAI gaining access to AWS should massively boost its business — not only against its arch-rival Anthropic, but more broadly as the company tries to go public, as investor and writer [M.G. Siegler argued on Spyglass](https://spyglass.org/the-openai-microsoft-agi-clause/).

But Microsoft gave up something it was clearly already losing, evidenced by OpenAI’s existing dalliances with AWS. And so Microsoft extracted real concessions in return — the new deal allows Microsoft to stop paying a revenue share to OpenAI, while OpenAI will continue to pay a revenue share to Microsoft through 2030. Moreover, Microsoft retains a non-exclusive license to OpenAI’s models and products through 2032, and as a 27% shareholder, it profits from OpenAI’s growth regardless of where those workloads run.

> The reality is that neither OpenAI nor Microsoft was effectively served by any exclusivity agreement, as both companies need to operate across multiple clouds, partners, and chip architectures to compete at scale.

The reality is that neither OpenAI nor Microsoft was effectively served by any exclusivity agreement, as both companies need to operate across multiple clouds, partners, and chip architectures to compete at scale.

Speaking at an [AWS event in San Francisco](https://www.youtube.com/watch?v=bhz0F33fc7Y) on Tuesday, OpenAI CEO [Sam Altman](https://en.wikipedia.org/wiki/Sam_Altman) argued that while AI will “lower the barrier to creating new products,” models alone aren’t enough.

“These systems need to run reliably and robustly, they need to be secure, they need to scale, and they need to fit into environments where companies already run their businesses, on infrastructure they already trust,” Altman said, framing the AWS tie-up as a way to meet enterprises where they already are.

> “[Customers] want the broadest set of choices — which means they need access to the best frontier models.”

AWS CEO [Matt Garman](http://linkedin.com/in/mattgarman), meanwhile, made a similar point from the other side, noting that its customers don’t want to be hamstrung by restrictive agreements that limit where they can run their AI systems.

“When we talk to companies, they always want the best options,” Garman said on stage. “They want to be able to run in the absolute best cloud. And when they’re looking at their AI applications, they want the broadest set of choices — which means they need access to the best frontier models.”

While it’s easy to argue either case for OpenAI or Microsoft, the more interesting question is whether AWS has quietly emerged as the big winner here.

Around a week before OpenAI announced it was hopping into bed with Amazon’s cloud subsidiary, [AWS revealed that Anthropic](https://thenewstack.io/anthropic-amazon-aws-investment/) had committed to spending more than $100 billion on AWS over the next ten years — the bulk of it on Trainium — while Amazon invested $5 billion in Anthropic immediately, with up to an additional $20 billion to follow tied to certain commercial milestones.

As *The New Stack* [reported on Wednesday](https://thenewstack.io/openai-bedrock-trainium-silicon/), within eight days, AWS had locked in major silicon commitments from two of the world’s leading AI labs. Two labs that compete on every benchmark and every architectural decision just made parallel bets on the same custom-silicon roadmap.

> Two labs that compete on every benchmark and every architectural decision just made parallel bets on the same custom-silicon roadmap.

Anthropic has been [leaning into that positioning](https://www.anthropic.com/news/anthropic-amazon-compute), proclaiming that it remains the only frontier AI model available across all three major cloud platforms — AWS, Google, and Microsoft. If that becomes the expectation, it’s hard to see OpenAI holding out for long — particularly when extending that arrangement into broader model availability on Google Cloud would close that gap.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)