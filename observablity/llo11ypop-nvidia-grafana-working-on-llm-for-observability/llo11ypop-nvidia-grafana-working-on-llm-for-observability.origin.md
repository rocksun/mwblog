# LLo11yPop: Nvidia, Grafana Working on LLM for Observability
![Featued image for: LLo11yPop: Nvidia, Grafana Working on LLM for Observability](https://cdn.thenewstack.io/media/2024/10/1534875f-llo11ypop-nvidia-and-grafana-work-on-an-llm-for-observability-1024x576.png)
NEW YORK — It wasn’t an announcement per se, but [Nvidia](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/) Senior Engineering Manager [Aaron Erickson](https://www.linkedin.com/in/aaronerickson) described during a keynote here at [ObservabilityCON](https://grafana.com/events/observabilitycon/) several AI initiatives Nvidia is working with [Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) on.

The projects include the two organizations developing AI training to better understand model performance and consistency. Another initiative leverages telemetry to create an interface for [observability](https://thenewstack.io/observability/) into [large language models](https://thenewstack.io/llm/) and AI applications.

As Erickson described in the Sept. 24 keynote, Nvidia relies on Grafana Cloud for its observability support.


[@nvidia]‘s[@AaronErickson]said during[#ObservabilityCON]that Nivida relies on[@grafana]to “understand the telemetry for how training is going.”[https://t.co/ZcNv6TZ5Aq][pic.twitter.com/2gxfvZaYX7]— BC Gain (@bcamerongain)

[October 3, 2024]
One of the more interesting projects — called [LLo11yPop](https://developer.nvidia.com/blog/optimizing-data-center-performance-with-ai-agents-and-the-ooda-loop-strategy/) — is an LLM for observability. Nvidia is developing an LLM designed with Grafana’s support to ask questions like, “Show me a graph of job failures.” Or, “What are the five best possible causes of last night’s issues?” Or, “Which clusters need maintenance over time?”

Erickson told conference attendees during the keynote address, “It’s still early days, but we’re starting to get answers from the data center using multiple LLMs trained in different areas of expertise. It’s an incredible concept, and we’re excited about the possibilities. We believe this, and more [agents](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) added over time, will allow us to solve a wide range of problems.”

## Telemetry to Check LLM Training Status
Nvidia is also working with Grafana on a Grafana-led [application for training observability](https://github.com/grafana/ai-training-o11y?tab=readme-ov-file#readme); Nvidia is a design partner with Grafana Labs on this project.

Nvidia’s status as a Grafana customer, Erickson said, is “critical for what we’re trying to accomplish: actually being able to understand the telemetry of how training is going

“Imagine you’re trying to build a foundation model or doing a massive tune of a model. You need to understand: Is the model converging? Is the training progressing? And, on a lower level, is the GPU performance stable? Is the heat OK? All of this is crucial to evaluate if you’re making a good investment in these training runs.”

Moreover, Erickson said during his keynote: “One of our key convictions is that this system won’t work unless it’s grounded in truth. The query results from the LLM must be backed by actual data, like what’s shown on a Grafana dashboard. We know LLMs aren’t perfect — [they do hallucinate](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/) — so we want to use them to build dashboards dynamically.

“You should be able to ask a question, get a dashboard link, and then dive deeper into the data center’s status across the world, across cloud providers, and across continents where we have GPUs.”

Grafana is working with several AI companies, in addition to Nvidia, “to push the boundaries on what we can monitor, learn and generate using both technologies,” [Tom Wilkie](https://www.linkedin.com/in/tomwilkie), CTO of Grafana Labs, told me.

“Our current efforts with Nvidia will help drive more useful observability to both those running and monitoring GPU infrastructure as well as those building and training models to run on GPUs. This foundational work can lead to a number of more reliable outputs from today’s models, and is something that should only continue to improve in accuracy and value to users as model performance improves.”

## What’s Under the Hood?
NIM retrieval agents based on Nvidia NIM (Nvidia Inference Microservices) technology, serves as the building blocks for the system Nvidia is building. NIM can also be described as offering optimized inference microservices for large-scale LLM deployments.

These agents gather data from sources like Grafana to answer questions. The questions come from analyst agents trained on how different applications run in data centers. With an observability agent framework for GPU fleet management using a multi-LLM compound model in the architecture design, agents manage orchestration and task execution for observability frameworks. These are orchestrated by what’s called an OODA loop — Observe, Orient, Decide, Act.

“The loop drives the agents to ask questions, identify what went wrong, and take action, like opening Jira tickets or calling [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention),” Erickson told The New Stack.

Debugging, of course, is paramount as without proper observability tools, making application and network fixes can take weeks or even months, he said.

“If they fail, that’s a lot of wasted resources for no good reason,” Erickson said. “That’s why it’s really important to have this insight, and we’re thrilled to be design partners, helping build out this capability. This collaboration allows us to achieve our goals and helps other customers running training jobs on GPUs too.”


[@nvidia]‘s[@AaronErickson]remembers those dreaded middle-of-the-night pages before proper observability became a thing, during[#ObservabilityCON]in New York last week.[@grafana][https://t.co/ZcNv6TZ5Aq][pic.twitter.com/uiaUCvioM5]— BC Gain (@bcamerongain)

[October 3, 2024]
## ‘Who Among Us Hasn’t Hallucinated a Little?’
During his talk, Erickson waxed not so nostalgic during his days as vice president of engineering for an unnamed “observability company.”

“Imagine waking up every day at 6 a.m., responsible for helping your CEO understand, by 8 a.m., what happened the night before,” he said. “My routine was to read the backscroll in Slack, call directors and [[independent contributors](https://thenewstack.io/tech-works-how-to-get-promoted-without-becoming-a-manager/)], and track down the people handling incidents.

“I had to gather information like which customers were impacted, which regions were affected and possible root causes. We needed all this to write the incident report and inform customers. This happened every day for six months while we transitioned to the cloud — it was not a fun time.”

LLMs are not perfect, or at least not yet. Frequent hallucinations across all LLMs are one of the most cited failures. But at the same token, humans do have hallucinations as well.

“You’ve had an incident, and the next morning, a senior leader asks what happened,” Erickson said. “Who among us hasn’t hallucinated a little to fill in the gaps? If you’re skeptical, just ask your developers. It happens all the time.

“This inspired me to think: with [GPT-4](https://thenewstack.io/30-non-trivial-ways-for-developers-to-use-gpt-4/), we can take a human question and translate it into a query language like [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/), or anything we use with Grafana, to figure out what happened last night. As an engineer, this allows me to start with a rough idea, ask follow-up questions, and get closer to plausible causes — and while it may not be perfect, neither are humans.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)