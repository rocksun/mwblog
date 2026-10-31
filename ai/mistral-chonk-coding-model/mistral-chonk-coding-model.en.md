**On Thursday, Mistral released the weights** for its frontier open model, Mistral Large 4 (ML4), on Hugging Face.

Made available for preview just three weeks ago, the French AI company says ML4 has significantly improved since then, thanks to reinforcement learning and testing with customers and partners. Now, it claims, ML4 is the “best open agentic coding model in the world,” beating GLM-5.3 on cybersecurity and coding benchmarks (though only barely on the latter), at a fraction of the cost, Mistral says.

> “We want to be in a position in which we dictate the frontier.”

From here, the AI company promises continued growth. In an embargoed press briefing attended by *The New Stack*, [Pierre Stock](https://www.linkedin.com/in/pierrestock/), Mistral’s VP of Science, calls ML4 merely “a stepping stone,” saying, “We want to be in a position in which we dictate the frontier.”

## Mistral’s VP of Science doesn’t want to live in a world without open weights

Stock told reporters that Mistral fully supports “the power of open weight,” calling it essential to ensure business continuity, transparency, and auditability for everyone: “I’m not comfortable living in a world in which open weights [don’t] exist,” he said.

> “I’m not comfortable living in a world in which open weights [don’t] exist,” he said.

Recalling when [OpenAI announced plans to cut off Cursor’s direct access to its models](https://thenewstack.io/anthropic-spacex-cursor-compute-openai/) or when [the US](https://thenewstack.io/fable-ban-open-weights/) [government ordered Anthropic to suspend Claude Fable 5 and Mythos 5 for all foreign nationals](https://thenewstack.io/fable-ban-open-weights/), Stock’s case for open weights bears weight — perhaps why he says the philosophy is in the French company’s DNA.

> “Our stance is that AI is going to be like electricity.”

“Our stance is that AI is going to be like electricity. You don’t want to live in a world in which your neighbor or an oligopoly can cut off electricity from one day to another.”

Mistral puts open weights at the center of its approach. Anthropic CEO and co-founder [Dario Amodei](https://www.linkedin.com/in/dario-amodei-3934934/) has [argued](https://thenewstack.io/amodei-open-weights-compute-regulation/) that open weights alone cannot resolve the concentration of AI power because access to computing infrastructure remains concentrated.

As Stock points out, this way, “nobody can switch it off because it can run either on your infrastructure or on an infrastructure that you can trust.”

## Coding + cyber = the biggest impact

An open-weight model, though, does need the goods to back it up, and Mistral says ML4 is there, calling it “the best open model built in the West.”

To back those claims, the company points to Terminal-Bench 4.0, one component of Artificial Analysis’s Coding Agent Index, where, by Mistral’s numbers, [Le Chonk](https://thenewstack.io/mistral-large-4-weights/) — Mistral’s official nickname for ML4 — ranks as the top open model in the world for agentic coding, scoring 41% to Muse Spark Open’s 6%, Kimi K3’s 21%, and just eking past GLM 5.3’s 40%.

![](https://cdn.thenewstack.io/media/2026/10/1353f6a4-cybergym-e2e.png)





Click to enlarge image. *(*Source: Mistral*)*

“What the graph doesn’t tell you,” Stock said, “is that it’s more efficient than the competitors,” adding that Le Chonk uses 47% fewer tokens per task on average than GLM 5.3. “It means that you can get things done way faster and at a lower cost,” he explained.

Coding prowess, however, wasn’t the startup’s only focus when training its model.

“We identified, really, coding and cyber as the two main areas that impact and that can benefit our customers and help them transform their entire business with AI,” Stock said in the briefing.

So Mistral backed investments to advance the model’s cyber capabilities. In CyberGym E2E from the Artificial Analysis Cyber Index, which tests defensive cybersecurity capabilities, the French model once again pulls ahead of much of the competition, scoring 79% to GLM-5.3’s 29% (though Z.ai’s smaller GLM-5.3 Flash scored 74% in the same chart). In Mistral’s comparison, ML4 exceeded DeepSeek v4.1 Flash 1017’s 76% and tied MiMo-V2.6-Pro’s 79%.

![](https://cdn.thenewstack.io/media/2026/10/e3dafb41-terminal-bench-4.0.png)





Click to enlarge image. (*Source: Mistral*)

To that point, Stock explains how some Mistral customers are already putting the model to work, using it to support automated pen testing, where specialized agents analyze an application’s logs and test for potential entry points.

## Breakneck improvements, at a fraction of the cost

When [Mistral launched ML4 in public preview at the start of October](https://thenewstack.io/mistral-large-4-weights/), it came after about two months of training on about 3,800 Nvidia Grace Blackwell GPUs in its European data centers. In the last three weeks, Stock says the model has undergone “significant improvement,” which he chalked up to the team’s reinforcement learning. Mistral’s own Terminal-Bench 4.0 score rose from 28% at preview to 41%.

> “I have no information about someone being able to do it with this amount of resources.”

More notably, he claims, the French company ran that reinforcement learning on only 10 megawatts of power, “a fraction of what all the competitors have.”

When pressed on how Mistral can know with certainty that it’s more cost-efficient than its competitors, Stock told reporters, “I have no information about someone being able to do it with this amount of resources.”

He also said Mistral’s resource efficiency means the French startup could advance further with the right investments: “If you give us 10 times more capital, then we’ll factor in these efficiency gains.”

## Mistral wants to lead the frontier

Throughout the embargoed briefing, Stock consistently referred to ML4 as “a stepping stone,” hinting at Mistral’s plans for what’s next.

One certainty? Developers can expect smaller versions of Le Chonk to ship in the coming months, with Stock confirming, “There’s going to be a family of models, and one of them is going to be on a laptop.”

Mistral says ML4 can help software engineers modernize legacy codebases (where [OpenAI has recently made a striking leap for COBOL migration](https://thenewstack.io/penai-cobol-migration-benchmark/)), as well as in finance, manufacturing, industrial engineering, and geospatial applications. Looking ahead, the French company seems to have its sights set on playing an even bigger role:

“We think the only way forward [is] to own the entire stack.”

[AI Agents
Learn to design, build and ship AI agents in 2026

Learn the Pre-requisites
LLM Fundamentals
Understand the Basics
AI Agents 101
Prompt Engineering
Model Context Protocol (MCP)
Agent Memory
Agent Architectures
Building Agents
Security & Ethics](https://roadmap.sh/ai-agents?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=mistral-chonk-coding-model)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)