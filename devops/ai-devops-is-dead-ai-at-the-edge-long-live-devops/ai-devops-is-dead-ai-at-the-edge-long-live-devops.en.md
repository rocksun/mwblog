Artificial intelligence is transforming the software delivery life cycle (SDLC). AI is helping to write code, optimize code, review code, debug code and more. And then there’s the code itself: SaaS offerings are incorporating AI in summarization features, chat features and various forms of analysis.

Finally, there are the other implications of AI, particularly [generative AI](https://thenewstack.io/keeping-up-with-ai-the-painful-new-mandate-for-software-engineers/) (GenAI), on the SDLC, such as observability for non-deterministic AI output. Hallucinations can join “off by one errors” and cache invalidations as the punchline in many a programming joke.

But something that hasn’t really changed with AI is the need for [DevOps](https://thenewstack.io/devops/): the practice of delivering higher-quality code to production, faster and more frequently. According to [DORA’s State of DevOps](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/) reports, there are four statistically proven measures that describe software delivery performance along these lines: Lead time to change, deployment frequency, change fail rate and failed deployment recovery time. We’ll come back to those.

According to Google Trends, interest in the term “DevOps” peaked in March 2022. After steady growth for the 10 prior years, the term is now seeing a very gradual decline. AI, on the other hand, has exploded in interest since the launch of ChatGPT in November 2022. Coincidence? I think not.

> AI is taking the proverbial oxygen out of the mindshare room. But is that because AI is somehow replacing or obviating the need for DevOps? Hardly. In fact, it’s quite the opposite.

On the surface, one could infer that AI has supplanted DevOps. But, as a wise data scientist once said, correlation does not equal causation. Sure, AI is taking the proverbial oxygen out of the mindshare room. But is that because AI is somehow replacing or obviating the need for DevOps? Hardly. In fact, it’s quite the opposite.

## DevOps: You Must Be This Tall to Ride the AI Ride

I once gave a talk about how [DevSecOps is pronounced “DevOps” because the “Sec” was silent](https://www.youtube.com/watch?v=xAN76xwGRJg). I argued that if you’re really doing DevOps right, your “higher quality code” has fewer security vulnerabilities, and your ability to deploy “faster and more frequently” includes patches and remediations of whatever vulnerabilities remain. It requires the same muscle group. In fact, without strong DevOps practices, organizations often have rampant known vulnerabilities in production.

The same DevOps “muscle group” applies with AI. Why? Because AI demands high-frequency code updates, automated quality processes and rapid remediation methods. Take a look at [Hugging Face](https://huggingface.co/) — the GitHub of AI — and you’ll see how foundational models are evolving rapidly. Data sets for retraining or [retrieval-augmented generation (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) are continually updated. Prompt engineering is iterative and can trigger changes in your AI codebase.

> If you haven’t figured out DevOps for your ‘regular’ non-AI code, you will face even more challenges implementing AI. There is no ‘leapfrogging’ the DevOps trend.

In other words, if you haven’t figured out DevOps for your “regular” non-AI code, you will face even more challenges implementing AI. There is no “leapfrogging” the DevOps trend. If you want to deploy model updates at high frequency, start with familiar, non-AI code bases.

And that’s just the “faster and more frequently” parts of DevOps. Being able to deliver “higher quality” AI code is similarly paramount. No one wants AI code vulnerable to prompt injection. Everyone wants AI models that have been tested and aligned. If the practices you have for ensuring AI code works and is secure are at odds with delivering updates quickly, then you will either have stale AI or broken AI. So, make sure you have code quality practices that allow you to confidently deploy code quickly.

*(Aside: What about MLOps? And AIOps? Yes, MLOps has evolved to apply DevOps principles to the life cycle of machine learning models. And there are some great advancements from MLOps that will help you extend your DevOps practice to AI. But let’s face it: MLOps is not where you start. MLOps is part of how you build on DevOps foundations to support running AI workloads. AIOps, however, became associated with using AI and ML to assist IT operations. This is useful for dealing with the deluge of data produced up and down the software stack, but it’s not the same as operating AI itself in production.)*

## Case Study: AI at the Edge Requires DevOps at the Edge

DevOps and the cloud have grown up together. The aggregation and abstraction of compute in the cloud is a great complement to the automation of DevOps. Whole ecosystems have sprung up around “cloud native” tooling, much of which supports achieving DevOps outcomes. DevOps practices have matured in many organizations, implemented around deploying code to the cloud.

And many workloads have moved to the cloud. In particular, user-facing applications have shifted from clunky, on-premises deployments, to product-driven SaaS. Behind any SaaS application, you’ll find some of the industry’s best DevOps practitioners. Enterprises have worked hard to catch up with digital darlings, and many large banks and media companies now boast DevOps thought leadership.

But there are entire categories of software that cannot move to the cloud or a data center. And there will be more software written that has to run at the edge. Why? Because data generated at the edge — on oil rigs, factory floors, shipping vessels, even retail stores — can be too costly and too slow to send all the way back to the cloud for processing.

For example, consider a factory with video cameras along its entire assembly line to scan for production defects. Sending all that data to the cloud would be cost-prohibitive. Next, consider an oil rig with a pressure sensor on a crucial valve. By the time the data is sent to the cloud, analyzed and a command is sent back to remediate the problem, the valve could have failed catastrophically.

The data intensity of the edge holds a lot of potential for AI use cases. They [may look different than AI in the cloud](https://thenewstack.io/ai-is-coming-to-the-edge-but-it-will-look-different/), but a recent survey found that [90% of CIOs were increasing investment in edge AI](https://zededa.com/edge-ai-survey/). Back to our previous examples: Factories can use AI to analyze camera feeds and immediately take corrective action on defective parts. Energy companies can analyze data from a drill site locally to immediately detect an impending failure or optimize drill operation. These are just a couple of ways in which the edge and AI are growing up together.

> DevOps hasn’t gone away, but it is more important than ever in the age of AI.

Almost paradoxically, DevOps at the edge has not matured at the pace of DevOps in the cloud. That’s because many of the “cloud native” practices and tools are based on a set of assumptions that don’t hold true at the edge. Availability of plentiful compute, power and storage. Relatively stable and high-bandwidth connectivity. Physical security around racks of servers. Taking the cloud-based systems built up for DevOps and forklifting them to edge environments doesn’t work.

This creates a conundrum at the edge. The edge holds such AI promise and yet lacks the DevOps maturity to see high-quality code deployed to the edge quickly and frequently. How do we overcome this? Start with the basics:

* **Don’t treat the edge like the cloud.** Embrace the realities of the edge even as you push toward cloud-like experiences. Edge native is not cloud native.
* **Use the** [**DORA metrics**](https://dora.dev/guides/dora-metrics-four-keys/) **for edge code.** Baseline where you are today on the four key metrics. Your improvement in those measures are key performance indicators.
* **Take a platform approach.** Don’t solve for one workload at a time at the edge. Every workload brings “friends” (security and connectivity, in particular). AI is no different: You may have Python, TensorFlow, PyTorch, Docker and more. Make sure you’re solving for all components and all layers of the stack.
* **Always bring observability along for the ride**. Don’t fly blind. Whether it’s application code, a single model or an AI agent, have a way to understand how the code is behaving in production. Observing a model is different from observing code; you’ll want to measure inference time, GPU utilization, and inference request count and success rate.
* **Don’t forget security.** Your edge AI applications will not only need to work in a zero trust environment, but also need to behave appropriately if the device they’re running on is physically stolen. Capabilities like secure enclaves and geofencing are crucial.
* **Add on MLOps.** AI at the edge requires MLOps to manage the ML/AI model used in the application, encompassing everything from dataset collection and training to model versioning, packaging and monitoring model performance. Once you have a solid DevOps foundation, MLOps introduces additional AI/ML-specific practices and patterns, such as feature stores, model registries and dataset stores.

DevOps hasn’t gone away, but it is more important than ever in the age of AI. The measures of DevOps success and health continue to be useful guideposts for AI deployments. Where DevOps practices aren’t strong, like at the edge, harden DevOps first before introducing AI.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2022/06/6d6b252b-cropped-d75d0304-dormain-drewitz-600x600.jpg)

Dormain Drewitz is vice president of marketing at ZEDEDA, the leader in edge computing platforms. Before joining ZEDEDA, Dormain was vice president of product marketing and developer relations at PagerDuty and led product marketing and content strategy for VMware Tanzu....

Read more from Dormain Drewitz](https://thenewstack.io/author/dormain-drewitz/)