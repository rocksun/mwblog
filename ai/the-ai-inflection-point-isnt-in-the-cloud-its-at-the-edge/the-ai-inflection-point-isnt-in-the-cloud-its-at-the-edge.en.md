AI model development has reached an inflection point, bringing high-performance computing capabilities typically reserved for the cloud out to edge devices. It’s a refreshing perspective compared to the all-consuming nature of [large language models (LLMs)](https://thenewstack.io/introduction-to-llms/) and the GPUs needed to run them.

“You’re gonna run out of compute, power, energy and [money](https://thenewstack.io/a-guide-to-navigating-gpu-rentals-and-ai-cloud-performance/) at some point,” said [Zach Shelby](https://www.linkedin.com/in/zachshelby/), CEO and co-founder of [Edge Impulse](https://edgeimpulse.com/), a [Qualcomm Technologies](https://www.qualcomm.com) company. “We want to deploy [generative AI] so broadly. It’s not scalable, right? And then it runs into so many reliability issues. It runs into power issues.”

At the edge, power matters differ, according to the device. The upshot, though? These devices can run a variety of language models, but LLMs pose a noteworthy challenge.

The AI story is about more than just the big data centers. We need the edge to run applications close to the data that the models process. Round-trip trips to a cloud service in a region across the country get expensive and pose a variety of issues that make real-time applications unusable.

## Challenges and Use Cases for LLMs in Industrial Settings

Shelby started Edge Impulse in 2019 with [Jan Jangboom](https://www.linkedin.com/in/jan-jongboom/), the company’s CTO. Shelby spoke with The New Stack on two occasions following Edge Impulse’s annual [Imagine](https://edgeimpulse.com/imagine) conference at the Computer History Museum in Mountain View, Calif. The company offers an edge AI platform for collecting data, training models and deploying them to edge computing devices.

“We need to find ways to make these probabilistic LLM architectures behave more deterministic, for no human in the loop, or minimum human in the loop applications,” Shelby said.

LLMs have multiple use cases for the back office, but the edge is a bit different in industrial environments.

There are many different types of architectures, such as [small language models (SLMs)](https://thenewstack.io/the-rise-of-small-language-models/), [visual language models (VLMs)](https://thenewstack.io/a-developers-guide-to-vision-language-models/) and others that are increasingly useful on the edge. But the use case remains unclear when it comes to large language general models typically used in consumer markets.

“Where do companies see real value?” Shelby asked. “That’s been a challenge in the early days of LLMs in industrial” settings.

It’s a matter of what people in the industry really trust, he said: “With industrial, we have to have [a return on investment], right? We have to understand what we’re solving. We have to understand how it works. The bar is much higher.”

VLMs, for example, are maturing fast, Shelby said.

“I do think now, with VLM just maturing fast, we really are finding lots of use cases, because it lets us do complex vision analysis that we couldn’t normally do with discrete models. Super useful, but it requires a lot of testing. You have to have end-to-end testing. You have to parameterize and put these guardrails around it.”

## From XR Glasses To Distributed AI Agents

At Imagine, I wore a pair of extended reality (XR) glasses to view a circuit board part. With the glasses, I could detect the part and then choose from a range of questions to ask. I used voice to ask the question, enabling [Whisper](https://github.com/openai/whisper), a speech recognition service, [YOLO](https://www.edgeimpulse.com/blog/introducing-yolo-pro-object-detection-optimized-for-the-edge/) (You Only Look Once) and OpenVocabulary for object detection.

![](https://cdn.thenewstack.io/media/2025/10/c3191c74-xrglassesgraphic-1024x576.png)
:   How extended reality glasses work.

That was in turn fed into a [Retrieval-Augmented Generation (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) tool and integrated with [Llama 3.2](https://thenewstack.io/running-llama-3-2-on-aws-lambda/), which includes small and medium-sized vision LLMs (11B and 90B), and lightweight, text-only models (1B and 3B). The models, according to Meta, fit onto edge and mobile devices, including pre-trained and instruction-tuned versions.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

The next step, according to Shelby? Apply agents to the [physical AI](https://thenewstack.io/integration-of-ai-with-iot-brings-agents-to-physical-world/) that Edge Impulse enables with [cascading models](https://www.edgeimpulse.com/blog/coming-soon-in-edge-ai-model-cascading-with-vlms/).

The workload might run in the glass, with one agent interpreting what it sees and what the person is saying. That data may then be cascaded into an [AI appliance](https://thenewstack.io/ai-at-the-edge-architecture-benefits-and-tradeoffs/), where another agent performs the lookup.

“I think that’s really interesting from an edge AI technology, we’re starting to be able to distribute these agents on the edge,” Shelby said. “That’s cool. But I do think that agentic and physical AI does make it understandable.”

People can relate to the XR glasses, Shelby said. And they show the connection between agentic AI and physical AI.

Small, discrete models, such as object detection, are feasible with battery-powered, low-cost embedded devices, he said. However, they cannot manage generative AI (GenAI). For that, you need far more powerful devices on the edge.

“A 10-billion model parameter model, think of that as a [small VLM](https://thenewstack.io/which-vision-language-models-should-you-use-for-your-apps/),” Shelby said. “Or a small SLM. So you’re able to do something that is focused. We don’t have a worldview of everything, but we can do something very focused, like vehicle or defect analytics, a very focused human language interface, or a simple SLM to interpret it.

“We could run that on one device. The XR glasses are a good example of this. That is kind of the 12 to 100 TOP class of devices that you can produce today.”

[TOP is a term used to describe an NPU’s processing capabilities](https://www.qualcomm.com/news/onq/2024/04/a-guide-to-ai-tops-and-npu-performance-metrics). An NPU is a neural processing unit used in GenAI. According to Qualcomm, “TOPS quantifies an NPU’s processing capabilities by measuring the number of operations (additions, multiplies, etc.) in trillions executed within a second.”

The XR glasses can run simple, focused applications, Shelby said, such as natural language processing with an SLM for interpretation, on a 12 to 100 TOPS-class device.

## Why Agentic Architectures Are Essential for the Edge

Beyond the screen, there is a need for agentic applications that specifically reduce latency and improve throughput.

“You need an agentic architecture with several things going on,” Shelby said about using models to analyze the packaging of pharmaceuticals, for instance. “You might need to analyze the defects. Then you might need an LLM with a RAG behind it to do manual lookup. That’s very complex. It might need a lot of data behind it. It might need to be very large. You might need 100 billion parameters.”

The analysis, he noted, may require integration with a backend system to perform another task, necessitating collaboration among several agents. AI appliances are then necessary to manage multiagent workflows and larger models.

The more complex the task, the more general intelligence is required, which necessitates moving to larger AI appliances.

[David Aronchik](https://www.linkedin.com/in/aronchick/), CEO and founder of [Expanso](https://www.expanso.io/), said three things will never change on the edge, which will have an impact on how developers build out on edge devices:

* Data growth.
* The speed of light isn’t getting any faster, and networking will never keep up because there is just too much data.
* Security and regulations are here to stay as data proliferates, and networking must take into account a host of factors.

Agentic architectures are a layer on top of the data and the networks, Aronchick said. “With those three things being true, that means you’ve got to start moving your agents out there, or programs, or whatever they may be. You’ve got to.”

[Expanso provides distributed computing to workloads](https://thenewstack.io/a-startup-complements-kubernetes-docker-and-wasm-at-the-edge/). Instead of moving the data, the compute goes to the data itself — increasingly relevant as enterprise customers look beyond the cloud for their computing needs. It offers an open source architecture that enables users to run jobs that generate and store data.

What we call the tools of agentic architecture is anyone’s guess, Aronchick said. But like Shelby, Aronchick said latency and throughput are the big issues to resolve. Further, moving data opens security and regulatory issues. With this in mind, it makes sense to keep your applications as close as possible to your servers.

## Ensuring Reliability: Guardrails for Industrial AI

The nature of LLMs, Shelby said, requires a person to tell you if the LLM’s output is correct, which in turn impacts how to judge the relevancy of LLMs in edge environments.

It’s not like you can rely on an LLM to provide an answer to a prompt. Consider a camera in the Texas landscape, focusing on an oil pump, Shelby said. “The LLM is like, ‘Oh, there are some campers cooking some food,’ when really there’s a fire” at the oil pump.

So, how do you make the process testable in a way that engineers expect, Shelby asked. It requires end-to-end guard rails. And that’s why random, cloud-based LLMs do not yet apply to industrial environments.

Edge Impulse tests the output pattern matching that developers expect, while also understanding end-to-end performance and accuracy. The tests are run on real data.

It’s not just the raw camera stream Edge Impulse tests, but also the object detector plus the VLM, and the output’s categorization.

LLMs, Shelby said, need training on relevant base data, such as industrial machinery: “Then you do transfer learning, which is like fine-tuning those models.”

## A Cautious Approach To Deploying LLMs at the Edge

Edge Impulse may then squeeze a lot more neurons into smaller compute, Shelby said, as it controls the architecture for the edge compute environment.

But the LLM use cases still show immaturity, so the company is developing edge constraints for industrial use cases. The base models are essential. The company processes the data as soon as it arrives from the camera using basic preprocessing models.

It needs to be careful with the LLMs, putting up the guardrails and testing the developer experience and usability so that an LLM can be deployed in the field.

“We’re careful to do it really step by step, like we haven’t brought in our LLMs yet,” Shelby said. “We’re still getting convinced how these can be safely used in industry.”

A text-based input for someone out on a wind tower may work OK. Still, there are other input methods, such as voice interfaces, which Shelby said the company is looking at as a way to interact, such as using an SLM with voice interfaces like Whisper to better understand a problem or to do maintenance using natural language automatically.

“We’ll bring in the technology and make it, make it very easy for developers, but you have to do it a little bit more slowly than what the hype is for the cloud,” Shelby said. “It’s interesting. So, that’s the challenge now: How do you expose this stuff?

“With LLMs, what are you going to do — have your maintenance guy chat with the chatbot on an oil pump?”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/13c3d9d6-cropped-0fe18b69-ef774ac85213a6506cf973dc6380cd57.jpeg)

Alex Williams is founder and publisher of The New Stack. He's a longtime technology journalist who did stints at TechCrunch, SiliconAngle and what is now known as ReadWrite. Alex has been a journalist since the late 1980s, starting at the...

Read more from Alex Williams](https://thenewstack.io/author/alex/)