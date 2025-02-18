# AI Agentic Evaluation Tools Help Devs Fight Hallucinations
![Featued image for: AI Agentic Evaluation Tools Help Devs Fight Hallucinations](https://cdn.thenewstack.io/media/2025/02/3abd7127-jr-korpa-quxyfcoa4qm-unsplashb-1024x576.jpg)
Agentic refers to a system’s ability to act autonomously and independently achieve goals. AI agentic evaluation tools, then, are solutions that evaluate generative AI and [AI agents](https://thenewstack.io/ai-agents-are-about-to-blow-up-the-business-process-layer/) for hallucinations and other problems.

The field is so new, solution providers and researchers are still working out which metrics to use. To learn more, we spoke with [Atin Sanyal](https://www.linkedin.com/in/atinsanyal/), an expert in the emerging area of AI agentic evaluations. Sanyal is the chief technology officer and co-founder of [Galileo](https://www.galileo.ai/), an AI evaluation platform startup that grew out of a Stanford lab about five years ago. Previously, he worked as an engineer and researcher at organizations such as Uber, Apple, LinkedIn, UCLA and [Oracle.](https://developer.oracle.com/?utm_content=inline+mention)

## Evaluating Hallucinations
Sanyal identified two types of [hallucinations](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/). Open-domain hallucinations occur when an AI model generates false information without specific context or input. Closed-domain hallucinations happen when an AI model fabricates incorrect information based solely on limited contextual data.

Closed-domain hallucinations pose particular concerns when building AI agents. Two key metrics for closed domain hallucinations are context adherence — measuring how much context appears in the output — and instruction adherence, which gauges how well the AI follows user prompts.

## Beyond LLM-as-Judge
When organizations first began to attack the problem of hallucinations, they deployed a large language model (LLM)-as-judge model that basically used one LLM to check the generative AI model. However, this approach has its limitations, such as [position bias](https://eugeneyan.com/writing/position-bias/), [verbosity bias](https://arxiv.org/abs/2310.10076), [self-enhancement bias](https://arxiv.org/abs/2402.11436) and [limited reasoning ability](https://news.mit.edu/2024/reasoning-skills-large-language-models-often-overestimated-0711), according to a [2023 research paper](https://arxiv.org/abs/2306.05685).

Another big issue is that large enterprises have hit limits with this approach, Sanyal added.

“They simply don’t scale because there’s [rate limits](https://thenewstack.io/how-nuanced-rate-limiting-transforms-your-api-and-business/) and all kinds of restrictions that third party APIs would put [on], which really makes the source application suffer in quality,” he said.

There’s one more complicating factor when evaluating AI agents: A single issue in the output of even one part of the AI system can compound and lead to an “out of whack output,” Sanyal said. The challenge is tracing an error in the output back to the part of the AI system that caused it, he explained.

## Evaluating AI Agents: Open Source
This is where agentic AI evaluation comes into play.

“It’s really about how do we help the AI engineer make these unpredictable systems a little more predictable and give them the right guardrails and to help, essentially, what we call evaluation,” Sanyal said.

There are [open source](https://thenewstack.io/the-metamorphosis-of-open-source-an-industry-in-transition/) libraries and frameworks that evaluate AI agents, including [RAGAS](https://docs.ragas.io/en/stable/) and [TruLens](https://www.trulens.org/), the latter having been acquired by cloud data warehouse platform Snowflake last year. These tools have gained traction in the past 12-15 months, Sanyal said.

Open source solutions tend to be “insufficient and myopic,” he contended, with open source tooling typically focusing on *quantitative* measurements that generate a number rather than more detailed *qualitative* information.

“A lot of the open source solutions still are focusing on statistical ways of quantifying [RAG](https://thenewstack.io/tutorial-build-a-rag-agent-with-azure-ai-agent-service-sdk/) hallucinations or open domain hallucinations and various other common form errors that LLM systems make, but we’ve discovered that’s really not enough, not sufficient,” he said. “They miss out on that customization piece, the ability to define your own metrics, own scorers, based on the use case.”

## An AI Agent Co-Pilot
Galileo acts as an AI agent co-pilot and integrates into the developer’s workflow with two lines of code, he said. It provides default guardrails with general purpose qualitative and quantitative measures.

Developers also have a “core need” to create their own metrics and modify others, he added. So, code-based metrics are critical, but because not all LLM creators are coders, there’s also a need for qualitative natural language definition-based metrics.

“We’ve built this auto [ML [machine learning](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/)] pipeline, which allows you not only to author custom metrics that you want for your app but also evolve them over time through human feedback, through different forms of feedback,” he said. “They’re almost like little agentic evaluation systems that we’ve built in-house to be able to make your metric adapt to your data.”

Which metrics to use actually depends on the kind of [agentic system that the developer is building](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/). Currently, there are dozens of [design patterns for agentic building systems](https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/) and that also influences which metrics should be used, he noted.

## Galileo’s Dual Approach
Galileo’s Evaluation Intelligence Platform takes a dual approach to evaluating AI Agents.

First, it developed [ChainPoll](https://arxiv.org/abs/2310.18344), an agentic AI that is similar to a judge-based agentic framework but provides step function improvements over basic LLM-as-judge techniques and is designed to detect various types of LLM hallucinations. It uses LLMs behind the scenes and is designed to be customizable so that a user can provide their own definitions of a hallucination and the system works off of that.

Luna is a suite of low latency eval models with open weights running on scalable LLM inference infrastructure developed in-house at Galileo. It’s focused on circumstances where there’s a high volume of user requests and a need for data privacy.

“We give the developer the tools to either surface it back to the user, or restate the generation or retry the end-to-end request if there is hallucination.”

– Atin Sanyal, CTO and co-founder of Galileo
Luna was created in 2024 and represents a year of going back to the drawing board to experiment with smaller generative models, Sanyal said. It is a DeBERTA-large (440M) encoder — that’s a fancy way of saying that with 440 million parameters, Luna is smaller than other LLMs. By comparison, GPT-3.5 has 175 billion parameters. This makes Luna more efficient to run and less computationally expensive. The [model is also fine-tuned for hallucination detection in RAG](https://thenewstack.io/rag-vs-fine-tuning-models-whats-the-right-approach/) settings.

Smaller evaluation models like Luna hold promise for better hallucination evaluation moving forward, Sanyal said. For instance, Luna outperformed RAGAS and Trulens, as well as Galileo’s own ChainPoll, according to Galileo’s [research paper about Luna](https://arxiv.org/abs/2406.00975).

“It’s a suite of smaller models, typically in the range of 2 billion to 10 billion, which are fine-tuned and trained specifically to detect hallucinations and we host them on commoditized GPUs on our end,” he said.

Sanyal described Galileo as an “evaluation co-pilot” that runs on the side while [web developers build the app](https://thenewstack.io/web-app-development-sans-javascript-with-microsoft-blazor/). It requires just two lines of Galileo code inserted into an application. Galileo offers [Typescript](https://docs.galileo.ai/client-reference/evaluate/typescript) and [Python SDKs](https://galileo-sdk.readthedocs.io/en/latest/index.html), he added. The platform can run on-premise or in Galileo’s SOC 2 complaint cloud.

“We give the developer the tools to either surface it back to the user, or restate the generation or retry the end-to-end request if there is hallucination,” he said. “What to do next lies in the developer hands versus it directly being surfaced to the user.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)