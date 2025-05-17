# AWS Launches Its Take on an Open Source AI Agents SDK
![Featued image for: AWS Launches Its Take on an Open Source AI Agents SDK](https://cdn.thenewstack.io/media/2025/05/da2ae77f-img_6899-edit.7fa451fddc234945b82d58b2daf091ed-1024x576.jpg)
[AWS](https://aws.amazon.com/?utm_content=inline+mention) today [launched](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) [Strands Agents](https://strandsagents.com), an [open source](https://github.com/strands-agents/sdk-python) AI agents SDK that is the result of AWS’s internal efforts to build enterprise-ready agents.
Accenture, Anthropic, Langfuse, mem0.ai, Meta, PwC, Ragas.io, and Tavily are joining AWS in these efforts.

With LangChain, CrewAI, OpenAI’s Swarm and plenty of other frameworks in the market, choosing which agent framework to use is becoming almost as hard as choosing with model to use to power those agents. But AWS says that its take on agents makes for a simpler developer experience because it relies more on the models themselves. The argument here is that models have gotten significantly smarter in the last few years, meaning they’ll need less hand-holding to figure out how to use tools, for example.

Strands supports a wide variety of models, including from Amazon’s own Bedrock service and LiteLLM, as well as local models with the help of Ollama. It’ll come with a number of built-in tools out of the box to allow the agent to retrieve data from Amazon Bedrock’s knowledge bases, call APIs and run Python logic, for example. Support for Model Context Protocol (MCP) servers, is, of course, also available.

“[The] Strands SDK will help you build the agent by actually using the power of the model,” Neha Goswami, the Director of Developer Agents and Experiences at AWS, told me. “That’s really the evolution that we have seen in the last two years. Strands allows you now to build an agent by really using the model’s reasoning capabilities, and the tool use is actually now incorporated in the model itself. So we use that, and then we also use the model’s own reflection and thought chain capabilities to really figure out how to build the right agent.”

Because of this, Strands also comes with a thinking tool, which prompts the model to use multiple cycles for thought processing and self-reflection. “In the model-driven approach, modeling thinking as a tool enables the model to reason about if and when a task needs deep analysis,” AWS principal engineer Clare Liguori writes in today’s announcement.

There is also support for multi-agent tools like [workflow, graph, and swarm](https://github.com/strands-agents), though today’s announcement downplays this a bit. Strands will, however, be able to orchestrate tasks across multiple agents and manage agent swarms.

For the most part, building agents with Strands is indeed quite straightforward and, like with similar frameworks, a lot of the work is in writing the tools and the right prompts as most of the code to run the agents is boilerplate.

“As a developer who’s building an agent now, even my own teams, the way we do it, we just write some prompts, and we are very now focused on the right tools for the job,” Goswami said. “So we bring that to the SDK, and then we build our agents just by using a combination of these prompts, these tools, and then we basically enter an agentic loop where the model is guiding itself on how to build the agent correctly.”

Looking ahead, Goswami noted that one area where there is still a lack of tooling is around telemetry. It’s likely that we will see Strands (or a different AWS project) tackle this in the future.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)