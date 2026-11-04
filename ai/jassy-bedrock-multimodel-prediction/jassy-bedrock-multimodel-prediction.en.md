Amazon CEO Andy Jassy expects the frontier AI model race to produce several competitive models rather than a single winner, telling analysts on Amazon’s Q3 2026 earnings call Thursday that the challenge ahead will be choosing among models rather than committing to one.

> “6- 8 models that are about as good as each other, or at least good enough for 95%+ of the workloads.”

During [the call](https://stockanalysis.com/stocks/amzn/transcripts/720308-q3-2026/), [Jassy](https://www.linkedin.com/in/andy-jassy-8b1615/) responds to a question from Goldman Sachs analyst [Eric Sheridan](https://www.linkedin.com/in/eric-sheridan-b2866736/) about the market opportunity for [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), predicting that within two to three years there will be “6- 8 models that are about as good as each other, or at least good enough for 95%+ of the workloads.”

## No single AI winner

Jassy has seen plenty of technology leaders lose their early advantage over the past 20 years. He pointed to databases and analytics as examples, along with TensorFlow, which once seemed likely to become the standard framework before PyTorch took the lead.

He expects something similar to happen with AI models. As Jassy put it, “there is not one tool to rule the world.” Some models will be better at reasoning or coding, while others will have an edge in visual tasks, speed, or [cost per token](https://thenewstack.io/minimax-flash-agent-costs/). That leaves companies with plenty of reasons to use more than one. Jassy believes “most customers are going to use multiple models, and many will use multiple models in the same generative AI application.” For developers, that could mean choosing a model based on the task at hand rather than committing to one provider for everything.

> “most customers are going to use multiple models, and many will use multiple models in the same generative AI application.”

## One API, many models

That argument is effectively a description of how Bedrock is built, since the service reaches more than 100 foundation models from providers including Anthropic, OpenAI, Meta, Mistral, DeepSeek, Moonshot AI, and xAI through one API, letting a team call Claude, GPT, Llama, or a smaller specialized model without wiring up a separate pipeline for each.

Amazon [recently brought OpenAI’s models](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/) onto the service alongside the closed models it already hosted, and Jassy says it has since added managed versions of open models such as Moonshot’s Kimi and Zhipu’s GLM, part of a hunger for Western open models he thinks Bedrock will keep feeding.

## Switching models isn’t free

Bedrock’s [Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) gives developers a common way to work with models from different providers without rewriting their integrations each time. But switching isn’t always straightforward. Models have different context limits, tool capabilities, and supported features, so developers still need to test how their applications behave.

Things can get even more complicated when a team has built its workflow around a particular vendor’s [agent harness](https://thenewstack.io/microsoft-copilot-harness-foundry/). Jassy said customers want to “swap them back and forth as they leapfrog each other, as different constraints of their applications require them.”

Security also factors into that decision. According to [AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html), Bedrock doesn’t give model providers access to customer prompts or responses, and that information isn’t used to train the underlying models. Jassy pointed to those protections as another reason enterprises choose the service.

## Why Amazon wins anyway

The strategy beneath the prediction is that Amazon does not need to ship the best model as long as it owns the place developers go to choose one, a position it is hardly alone in chasing, since Google’s Vertex AI and Microsoft’s Azure AI Foundry pitch much the same multi-provider catalog and unified access.

A market where six or eight models keep trading the lead and teams [constantly rotate between them](https://thenewstack.io/anthropic-s1-models-revenue/) is exactly what a neutral access layer monetizes, and Jassy makes little effort to disguise that Bedrock is the intended beneficiary, calling the opportunity “gigantic” and suggesting it could grow into a service “as large as EC2,” still one of AWS’s biggest businesses.

The early numbers lend that some weight, with Fortune 500 companies now spending close to seven times more on Bedrock year over year, token volume up nearly 17 times, and the service ranking, by Jassy’s account, as the fastest-growing multibillion-dollar product in AWS history.

It all arrives as AWS reaccelerates, with the segment growing 39.3% in the quarter to $46 billion and reaching a $184 billion annualized run rate, and Jassy notes that most Bedrock traffic already runs on Amazon’s own Trainium chips, which lets the company hold prices down while protecting its margins.

> Jassy notes that most Bedrock traffic already runs on Amazon’s own Trainium chips, which lets the company hold prices down while protecting its margins.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=jassy-bedrock-multimodel-prediction)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)