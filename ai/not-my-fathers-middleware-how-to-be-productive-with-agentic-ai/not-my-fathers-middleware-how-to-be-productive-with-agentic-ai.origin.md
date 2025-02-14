# Not My Father’s Middleware: How To Be Productive With Agentic AI
![Featued image for: Not My Father’s Middleware: How To Be Productive With Agentic AI](https://cdn.thenewstack.io/media/2025/02/85d1a35f-how-to-be-productive-with-agentic-ai-1024x576.jpg)
My father, Nick Humble, worked for IBM for most of his career. In the early 1990s, he worked on the launch team for a brand new piece of messaging-oriented middleware called [IBM](https://www.ibm.com?utm_content=inline+mention) MQ Series (now called [IBM MQ](https://www.ibm.com/products/mq)). Released in 1993, it was an instant hit.

In the early 2000s, I worked with a team that used MQ Series as the foundation for implementing an internet banking system for a major UK High Street bank. Its guaranteed-once (and once only) message delivery worked flawlessly across everything, from the two mainframes that ran the core banking engines to the cluster of Windows servers for the website. By abstracting the networking and data transformation concerns to the point where we no longer thought about them, the middleware dramatically simplified the process of building a distributed system.

Fast forward to today, and many enterprises are wondering where and how to make good use of the [large language models (LLMs)](https://thenewstack.io/llm/) behind the much-hyped rise of generative AI (GenAI).

The two places where GenAI has found early product market fit are software development and marketing. [Jonathan Eyler-Werve](https://www.linkedin.com/in/eylerwerve/), strategy lead for AI/ML developer platforms at Tanzu, a division of Broadcom, believes there is a third, enterprise-specific use case. This would address the set of enterprise problems that sit at the intersection of natural language processing, people and process.

## Enterprise AI: From Inference to Autonomous Systems
Eyler-Werve believes that inferencing, the process of running live data through a trained AI model to make a prediction or solve a task, will become a commonplace part of enterprise applications. These applications will be built not by AI specialists but by enterprise developers.

“We’re going to solve more problems in organizational app development with inference models,” he told me in an interview. “A lot of traditional applications are going to reach out to an inferencing model to solve a problem, particularly with data fusion and translation.”

This advent of enterprise AI inference requires a good range of AI programming frameworks, such as [AutoGen](https://microsoft.github.io/autogen/dev//index.html), [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) or [Spring AI](https://spring.io/projects/spring-ai), that provide a way for developers to rapidly iterate. Eyler-Werve suggested that it also necessitates a new breed of AI-oriented middleware that will, as MQ Series did for messaging, solve a group of [cross-cutting concerns](https://thenewstack.io/vmwares-golden-path/) for enterprise inferencing models, including security, verification, cost control and provisioning.

Moreover, he thinks that by solving these issues, we will radically simplify the building of [agentic systems](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) for the enterprise; systems that have goal-directed behavior and can take autonomous actions to achieve those goals, while continuously learning and adapting based on new information.

To understand why, Let’s take a step back and think about each cross-cutting concern in turn.

## What Do Enterprises Need To Build Agentic Systems?
As enterprises deploy inferencing across their applications, [robust security](https://roadmap.sh/cyber-security) and [management controls](https://thenewstack.io/kubecon-keynotes-wrestle-with-ai-governance-complexities) become essential infrastructure, with three of the four aforementioned concerns — security, verification and cost control — forming parts of the solution.

For security, you need an audit trail recording what the applications and AI models are doing. You also need a way of managing API keys. “Our approach here is that the AI middleware in Tanzu AI Solutions gives you an API key,” [Adib Saikali](https://www.linkedin.com/in/adibsaikali/), distinguished software engineer in Broadcom’s Tanzu division, told me in an interview. “This means that we hand out unique keys to an application, so if an API key leaks, it doesn’t matter so much.”

You also need a method for curation, so your developers can use only the models they should, he suggested. “Within the [Tanzu AI ](https://www.vmware.com/solutions/app-platform/ai)Solutions, we provide endpoints that can be used to make up a collection of models advertised for consumption,” Saikali said. “So an organization might define a personal banking endpoint with a set of models suitable for that, and have a separate endpoint for capital markets with a different set of models.”

Closely related to security, verification is the process of assessing whether the messages passing to and from the model are safe and appropriate. It involves a number of steps, including logging outputs.

“At some level, we get into doing really high-quality evaluation to ascertain whether the information returned by the model is accurate,” Eyler-Werve told me. “But there is an enormous set of considerations in order to make it cost-effective. Logging outputs, for example, needs to be done securely since outputs have all sorts of information in them. Given that, you want to avoid having each team implement their own logging and recording systems.”

Cost control matters even more if you are using proprietary models because calling them can quickly become very expensive. Eyler-Werve sees this as a cross-cutting concern that belongs in the middleware.

“The vendors would love you to use their built-in cost control, but that won’t work well because they also want you to run up costs,” Eyler-Werve told me. “You also don’t want to ask your dev teams to implement cost control because if they don’t do it correctly, you could run up a huge bill overnight with one misbehaving line of code.”

“We [Tanzu] currently offer three solutions to help with cost control,” Saikali said. “The first is that we let you see the token consumption of apps; the second is that we let you apply rate limiting; and the third is that we allow you to switch providers easily, so you can pick the provider with the best price/performance for your particular use case.”

One additional way organizations are addressing control of model consumption is to distill models to speed up responses and reduce both the financial and unreasonably high environmental cost of using LLMs for inferencing. The basic process of distillation is that you capture a set of good results using a larger model, then use the stored completions to evaluate the performance of the larger model and a smaller one to establish a baseline. You can then use a subset of your stored completions as training data to fine-tune the smaller model, improving its results and comparing it with the original benchmark until those results are satisfactory.

Both [OpenAI](https://platform.openai.com/docs/guides/distillation) and [Amazon](https://aws.amazon.com/?utm_content=inline+mention) Bedrock offer ways of performing distillation. [AWS claims](https://aws.amazon.com/bedrock/model-distillation/) that distilled models in [Amazon Bedrock](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/) are up to 500% faster and up to 75% less expensive than original models. Regrettably, there is limited data available on carbon costs, but we can assume that a lower price also means reduced emissions.

## What Do AI Agents Need?
The fourth concern, provisioning, covers both the models themselves and the resources they depend on. Suppose, for example, your program receives some data in a CSV file that it’s unable to process. Rather than throwing an error message, you could hand the CSV to an LLM to see if it can resolve the problem and, if it can, move to a verification step.

In this environment, the development team doesn’t train the models. “They need to be able to provision a model, get it wired up correctly with all the monitoring needed to measure outputs, and make sure it is behaving in the way that they want,” Eyler-Werve said.

This in turn requires some way to expose different enterprise resources to the application, such as a spreadsheet sitting on a hard drive. These resources then form a set of tools that the agents can utilize.

[Anthropic’s Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) is the first real-world attempt at building a protocol for this. “It means we can start putting really thin and fast wrappers around things that would otherwise require both a whole service and a REST API,” Eyler-Werve told me. “We can do it in a day, so an agent can start talking to it if it knows where it is, is allowed to communicate with it and has all the necessary connective tissue.”
In addition to access, agents also need memory so that they can maintain state and context across long-running conversations. [MemGPT](https://research.memgpt.ai) is one example of a pattern that can do this.

Combined, these LLM augmentations — retrieval, tools and memory — are the building blocks for agentic systems. According to Eyler-Werve, this means that “if you have a [good platform](https://thenewstack.io/how-spring-and-java-shaped-internal-developer-platforms) that knows how to provision not just the runtime, storage and now inference, but can also tell you what resources are available and what jobs they can do, you can start stitching together these agentic solutions in a really lightweight way.”

## What Are LLMs Good (and Bad) At?
One significant challenge with using LLMs is that they make stuff up. For example, the [winning solution](https://arxiv.org/pdf/2410.00005) for a benchmarking competition (organized by Meta and based on retrieval augmented generation [RAG] and complex situations), was [wrong about half the time](https://www.aicrowd.com/challenges/meta-comprehensive-rag-benchmark-kdd-cup-2024/problems/meta-kdd-cup-24-crag-knowledge-graph-and-web-retrieval/leaderboards). These findings are similar to those from NewsGuard, a rating system for news and information websites, which showed that the 10 leading chatbots [made false claims](https://www.newsguardtech.com/wp-content/uploads/2025/01/December2024AIMisinformationMonitor.pdf) 40% of the time and gave no answers to 22% of questions. Using RAG and [a variety of other techniques can help](https://www.nature.com/articles/d41586-025-00068-5), but eliminating errors completely looks to be impossible.

Given this, the key to taking advantage of LLMs is to keep them in their sweet spot, which is understanding — not generating output. “The consumer use of ChatGPT is the weakest one,” Eyler-Werve told us. “Much of the ChatGPT world is based on plopping out 600 words, 200 of which are made up. With agents, we are getting back to what they are best at, which is understanding things and making the best guess decisions.”

Eyler-Werve also thinks that progress with LLMs will likely stall. “LLMs are where they are going to be for a while because we’ve trained on everything we can. So, while they will get better at specific things like calling functions, the LLMs themselves will plateau. This means that wrapping rules around the core model is how you are going to get value out of them sooner.”

If he’s right, this would mean that the race isn’t going to be who has the best LLM, but rather how you can use it cost effectively and how quickly you can expose all these enterprise resources to inferencing models.

Building AI-powered applications requires a versatile architecture that can effectively bridge conventional and AI-driven logic. That challenge increases as applications grow more sophisticated — the non-deterministic nature of AI systems means that the greater use of agent autonomy brings with it a pressing need for protective measures. These guardrails, including content safety protocols, usage limits and audit trails, become especially critical when developing agentic applications that operate with high degrees of independence.

It is also worth saying that using AI effectively requires the ability to rapidly iterate, experiment and learn what does and doesn’t work. In that context, it is noticeable that [organizations that have an experimental mindset](https://blog.container-solutions.com/why-run-thousands-of-failed-experiments) and have adopted modern, cloud native, and microservices patterns and architectures are well placed to adopt agentic models. It is a great example of how those companies and teams that went through the so-called “digital transformation” future-proofed themselves to take advantage of innovations like agentic AI.

For readers looking to explore practical implementations, a recent[ article](https://www.anthropic.com/research/building-effective-agents) from Anthropic shows a set of foundational patterns for building LLM agents with a corresponding [cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents). On the Spring Source blog, Christian Tzolov provides a set of [Spring AI implementations](https://spring.io/blog/2025/01/21/spring-ai-agentic-patterns) that have the same fundamental patterns.

*For more information on AI middleware capabilities included in Tanzu AI Solutions, please read the latest Tanzu Platform blog post, What is AI Middleware, and Why You Need It to Safely Deliver AI Applications at Scale.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)