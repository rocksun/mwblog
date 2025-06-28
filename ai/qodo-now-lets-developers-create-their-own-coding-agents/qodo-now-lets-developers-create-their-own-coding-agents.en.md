[Qodo](https://www.qodo.ai/), the agentic coding platform that lets developers generate code but also helps them review and test it, is launching [Qodo Gen CLI today](https://docs.qodo.ai/qodo-documentation/qodo-gen/qodo-gen-cli), a new agent framework that allows developers to easily create their own AI coding agents based on their unique workflows and codebases. In essence, this means developers will be able to write their own configuration files and prompts to guide these agents’ behavior to work through complex workflows and interact with outside tools.

As Qodo co-founder and CEO [Itamar Friedman](https://www.linkedin.com/in/itamarf/) told me, the team always believed that while [vibe coding may be fun](https://thenewstack.io/vibe-coding-in-a-post-ide-world-why-agentic-ai-is-the-real-disruption/), for enterprises to get real value out of their investments in AI and [coding agents](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/), AI has to be integrated across the software development life cycle with code review and testing at the core. He also highlighted that one feature that makes Qodo unique — and capable of handling large codebases — is its context engine. (If that sounds familiar, that may be because Qodo competitor [Augment Code](https://thenewstack.io/augment-codes-remote-agents-code-in-the-cloud/) also puts a lot of emphasis on its context engine.)

[![A text snippet showing how to define a Qodo coding agents.](https://cdn.thenewstack.io/media/2025/06/2809f91c-qg-cli-custom-agent.png)](https://cdn.thenewstack.io/media/2025/06/2809f91c-qg-cli-custom-agent.png)

Image credit: Qodo.

“Most of the jobs to be done across the [software development life cycle] requires […] bringing the right context and checking the quality of the generated code,” Friedman explained. “For example, if you’re doing root cause analysis, then you need to bring the right context to do that, and you need to check what’s not right with the code and debug it in QA, etc.”

To bring agentic AI to all parts of the software development process, the Qodo team argues, means you have to bring the agent out of the IDE and into the command line. Yet, for most agent-centric command line tools, customization starts and ends with adding Model Context Protocol (MCP) tools to give the agents the ability to use third-party tools and access additional data.

“Most agents behave in the same way. For example, for most agents, you give them some rules and they basically use it as part of the system prompt and then you can customize that rule. It’s a file, and you just hope that it will work as you expected. We use a graph-based agent that we worked hard on, with internal benchmarks, etc., to make the graph follow a certain set of instructions very rigorously,” Friedman said.

[![](https://cdn.thenewstack.io/media/2025/06/22598a09-screenshot-2025-06-24-at-15.25.02.png)](https://cdn.thenewstack.io/media/2025/06/22598a09-screenshot-2025-06-24-at-15.25.02.png)

Image credit: Qodo.

If a development team typically uses the observe, orient, decide and act (OODA) loop, they can now specify this in the configuration document, and the agent will stick closely to these guidelines to solve an issue, for example.

In this configuration file, Friedman said, developers can define the agent’s general behavior, but they can also use it to define MCP permissions and set an overall goal that the agent should try to achieve, including an exit rule. Because these agents are based on large language models (LLMs) and are not deterministic, it’s especially important that the agent follows those exit rules and that developers can force it to provide a very specific output. Friedman said that Qodo’s system will follow those rules 99.99% of the time.

Qodo also added a new command to its CLI tools called “create agent,” which allows the developer to step through the process of creating a new agent, following the company’s best practices. In case the developer isn’t clear enough, the tool will also ask clarifying questions as needed.

By default, Qodo Gen CLI will ship with a few pre-built agents for tasks like code review, test coverage analysis and release note generation. These pre-built agents also integrate with popular CI/CD tools.

As of now, Qodo Gen CLI supports models like OpenAI’s o3 and Anthropic’s Claude Sonnet 4.

Looking ahead, the Qodo team is also thinking about how to best interact with these agents — and what’s the best place to do so. “ADEs [agentic development environments] are the next thing,” Friedman said, noting that if companies like Lovable can build user interfaces on the fly, “why do we need to have this IDE that’s so harsh? I need the interface to fit my task.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)