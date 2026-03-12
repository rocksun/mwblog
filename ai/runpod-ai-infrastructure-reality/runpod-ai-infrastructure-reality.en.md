The rise of agentic AI services has enabled the enterprise technology market to blossom with a new, fully evolved set of automation and acceleration tools that can be applied to almost every use case across every industry vertical. That’s the somewhat cheesy mantra currently offered by heads of industry, AI evangelists, and even politicians.

Infrastructure specialist [Runpod](https://www.runpod.io/) sees a slightly different reality, the shape of which might help developers focus on which AI tools and services are seeing the most practical, functional deployment.

It does so by virtue of its ability to act as a GPU instance platform built for AI. The company offers on-demand pods, autoscaling serverless endpoints, and instant cluster services to run distributed training workloads.

Consequently, Runpod oversees what it calls the “volume of raw infrastructure exhaust” behind AI workloads, giving it a privileged view of which models are actually deployed. It can also assess whether models are used for inference, fine-tuning, or training, and identify which GPUs are selected and where workloads originate.

## Anonymized serverless deployment logs

The Runpod State of AI report is not based on benchmarks, surveys, or human-evaluated leaderboards. Instead, this analysis is based on anonymized serverless deployment logs that sit on Runpod’s platform, which the company says currently serves more than 500,000 developers globally.

“We built internal pipelines to classify model usage at scale, ran LLM-based analysis across production logs, mapped workloads to GPU selection patterns, and used IP intelligence to understand geographic distribution. The result isn’t anecdotal. It’s behavioral,” writes [Charlotte Daniels](https://www.linkedin.com/in/danielscharlotte/), head of data at Runpod, [in a blog post](https://www.runpod.io/blog).

## Contradicting the public narrative

This record of what AI workloads actually make it to production is at odds with the publicity machines behind some of the bigger brands. Runpod says it “contradicts much of the public narrative” in real terms.

Among the reality checks offered here is that Qwen — *not* Llama — is now the most-deployed self-hosted LLM. Created and developed by Alibaba Cloud, [Qwen is a family](https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1) of open-weight LLMs known for its complex reasoning capabilities that work across text, audio, and vision application modalities simultaneously.

> “Strikingly, Llama 4 has near-zero adoption. The ecosystem hasn’t meaningfully migrated… developers optimize for performance per dollar, latency, compatibility and fine-tuning.”

Despite its power (and apparent appeal for multi-modal apps), Runpod points out that Qwen clearly enjoys a lower share of voice than Meta’s monolithic ability to surface Llama in [benchmarks,](https://virtualizationreview.com/articles/2024/04/19/llama-3-ranking.aspx) on [X (formerly Twitter) threads,](https://x.com/AIatMeta/status/1908598456144531660) and [on](https://www.ibm.com/think/news/meta-llamacon-2025) [conference slides](https://www.ibm.com/think/news/meta-llamacon-2025).

“Even more striking: Llama 4 has near-zero adoption. Despite launch coverage and attention, the ecosystem hasn’t meaningfully migrated. The [AI software engineering] market is pragmatic. It optimizes for performance per dollar, latency, compatibility and [the presence of] fine-tuning ecosystems,” writes Daniels.

## Rendering killed the video star

Another emerging area within the total AI universe is video. Services designed to produce text-to-video cinematic demos for use cases like model launches and product demonstrations have been met with wonder. Vendors such as Synthesia, Runway, and [CraftStory](https://www.computerweekly.com/blog/CW-Developer-Network/CraftStory-developers-expand-extend-AI-video-generation-services) have emerged in this space, promising to create movie-grade AI videos in minutes.

If this concept were working as comprehensively as organizations specializing in these technologies promised, then the raw infrastructure exhaust would indicate widespread upscaling.

By this, we mean AI video test cases would be prototyped, developers would be elated and order more pizza, the deployment would be upscaled to accommodate more space… and the team would move to the feature-length version of its project faster than Martin Scorsese having a boozey reunion lunch with Robert de Niro.

“Production behavior tells a different story: upscaling workloads outnumber generation roughly two to one. Teams are not betting everything on a single expensive render; instead, they generate fast, low-resolution drafts, select winners, and then allocate compute to enhancements. Roll the dice, then refine,” explains Daniels.

All of which leads to a revelation about AI datacenter resource capital allocation. Quite simply, optimization is absorbing more GPU time than raw creation.

## Settled in on ComfyUI

For image tasks, Runpod says ComfyUI has become the “de facto standard for image generation,” powering more than two-thirds of image endpoints with its node-based approach. The company’s full report on this subject states that this dominance “reflects a broader shift” toward modular, customizable pipelines rather than simple text-to-image calls.

The advice to developers from Runpod is, if you’re building image generation workflows, investing in ComfyUI expertize is increasingly essential because it’s where the ecosystem has converged.

Looking at the big picture, this analysis notes that nearly two-thirds of organizations using Runpod’s AI infrastructure are in industries outside pure AI services. Unsurprisingly, perhaps, HealthTech and FinTech lead the enterprise verticals.

The bottom line appears to be rather less glossy than the firehose of alerts promising easy-to-deploy single-click AI services. Instead, the raw infrastructure exhaust shows that production-grade AI usage patterns are consolidating around performance, efficiency, and workflow control.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)