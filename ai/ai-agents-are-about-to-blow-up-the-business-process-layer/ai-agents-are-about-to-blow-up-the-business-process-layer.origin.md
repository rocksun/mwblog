# AI Agents Are About To Blow Up the Business Process Layer
![Featued image for: AI Agents Are About To Blow Up the Business Process Layer](https://cdn.thenewstack.io/media/2025/01/7ae5f9a7-sparks-1024x576.png)
When people think of generative AI, many envision it working as part of a “system of engagement” — a customer service agent, a supply chain management tool or a way to intelligently interact with and search an organization’s PDFs and other proprietary data.

That’s an accurate view: For the next year or two, applications that intelligently create content by [leveraging large language models (LLMs)](https://www.datastax.com/guides/what-is-a-large-language-model?utm_medium=byline&utm_source=thenewstack&utm_campaign=agentic-ai&utm_content=) will remain a primary [AI focus](https://thenewstack.io/ai/) for enterprises.

But consider this: Most of the code written at enterprises sits within business processes — systems like inventory planning, which sit between the engagement layer and the more rigid systems of record (an organization’s data, etc.) How will GenAI benefit that layer? How can an organization improve its business processes with this pervasive technology?

![A classic enterprise architecture](https://cdn.thenewstack.io/media/2025/01/9c44e2c3-image1.png)
A classic enterprise architecture.

Agentic AI is the answer. While AI agents are built to do specific tasks or automate specific, often-repetitive tasks (like updating your calendar), they generally require human input. Agentic AI is all about autonomy (think self-driving cars), employing a system of agents to constantly adapt to dynamic environments and independently create, execute and optimize results.

When agentic AI is applied to business process workflows, it can replace fragile, static business processes with dynamic, context-aware automation systems.

Let’s take a look at why integrating AI agents into enterprise architectures marks a transformative leap in the way organizations approach automation and business processes, and what kind of platform is required to support these systems of automation.

## What Agents Are Doing Now
When you provide an agent with context, the agent then feeds that [context to an LLM](https://thenewstack.io/llm/) and asks it to complete and respond to it. AI agents can also use capabilities to complete tasks on the behalf of users. These AI agents can perform several key functions guided by instructions and information derived from context:

**Tool use**: The agent uses external functions, APIs or tools to extend its capabilities and perform specific tasks. This can include calling predefined functions or interfacing with external services (like making web requests using cURL or accessing RESTful APIs) to obtain context or execute actions beyond its inherent functionalities.**Decision-making**: The agent evaluates available information and selects the most appropriate action to achieve its goals. This involves analyzing context, weighing possible outcomes and choosing a course of action that aligns with the desired objectives.**Planning**: The agent formulates a sequence of actions or strategies to achieve a specific goal.**Reasoning**: The agent analyzes available context, draws conclusions, predicts outcomes of actions and makes informed decisions about the optimal steps to take to reach the desired outcome.
These latter kinds of functions — decision-making, planning and reasoning — often involve multiple agents working together toward a goal. The agents could seek to refine generated code for correctness, debate whether an agentic decision is biased or plan the use of other [agentic capabilities](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) to complete a task.

## Orchestrating an Agentic Network
Models that power networks of agents are essentially stateless functions that take context as an input and output a response, so some kind of framework is necessary to orchestrate them. Part of that orchestration could be simple refinements (for example, having the model request more information). This might sound analogous to [retrieval-augmented generation (RAG)](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_medium=byline&utm_source=thenewstack&utm_campaign=agentic-ai&utm_content=) — and it should, because RAG is essentially a simplified form of agent architecture: It provides the model with a single tool that accesses additional information, often from a vector database.

But multiagentic model frameworks take this further: They broker requests for additional information or provide a response that’s designed to be fed to another agent for refinements.

![Frameworks enable agents to work in concert.](https://cdn.thenewstack.io/media/2025/01/cbae4a70-image2-1024x484.png)
Frameworks enable agents to work in concert.

For example, one agent could write some Python while another then reviews it. Or an agent could express a goal or idea, and then a second agent’s job could be to break that up into a set of tasks, or review the idea to find problems that the first agent can review and then refine the idea. Your results start to get better and better.

## OK, But How Do I Build Agentic AI?
In the near future, a lot of software engineers will become agentic process authors. They’ll build these processes by mixing and matching components — models, user input, goals — and critical business services.

An example of one of these components is the stock in an inventory management system. What if you connected that system to an agent that could help optimize inventory levels during the holiday season? With the help of another agent that has done some historical inventory level analysis, you could ensure that there is just enough inventory to meet seasonal demand yet leave little inventory after the holiday rush. This might disappoint fervent after-Christmas sale shoppers, but it would also help prevent retailers from selling their wares at a loss.

But how will developers build these systems?

Agentic processes can, of course, be expressed with code, but it also helps to visualize them as “agentic flows” — one agent’s output becomes the input of another agent, and so on. Tools available now are already providing a lot of value in this effort to simplify building agentic systems. One such solution is [Langflow](https://www.datastax.com/products/langflow?utm_medium=byline&utm_source=thenewstack&utm_campaign=agentic-ai&utm_content=), a visual, low-code builder for [creating agentic AI applications](https://thenewstack.io/datastax-aims-to-simplify-building-ai-apps-with-ragstack/) and complex AI workflows by dragging and dropping different components, without the need for much coding.

![Agentic “flows” help to automate business processes.](https://cdn.thenewstack.io/media/2025/01/7bcd77f4-image3-1024x442.png)
Agentic “flows” help to automate business processes.

Langflow enables developers to define anything as a tool, including components like a prompt, data source, model, APIs, tools or any other agents. We’ve recently seen significant demand for building “flows” with agents, as developers are creating a lot of applications that include several multiagent capabilities. Agents are the most popular type of component that developers are inserting into flows with Langflow.

## Wrapping Up: From Copilot to Pilot
Agentic workflows [bring together enterprise data](https://thenewstack.io/bringing-ai-to-the-data-center/), AI and APIs, forming the systems of automation that empower domain experts to scale their abilities and make enterprises work better through AI. Integrating AI agents into enterprise architectures marks a big leap in how organizations approach automation and business processes. These agents, empowered by LLMs and agentic frameworks, transcend traditional boundaries by seamlessly operating across processes, workflows and code.

![How AI can transform enterprise architecture](https://cdn.thenewstack.io/media/2025/01/a64863a4-image4-1024x381.png)
How AI can transform enterprise architecture.

Adopting agentic workflows promises to enhance efficiency, scalability and responsiveness across business operations. They’ll manage entire workflows, handle complex tasks with greater adaptability and improve customer experiences by providing more personalized and timely interactions. As automation becomes embedded in enterprise systems, AI copilots will graduate to pilots, and organizations that employ agentic AI will be better positioned to innovate, compete and deliver value.

*For more details on agentic AI, read the free whitepaper, “**Systems of Automation: The Future of Enterprise Architecture Is Agentic.**” And check out **this page** to learn more about Langflow. *
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)