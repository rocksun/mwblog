With careful governance and validation, AI agents are increasingly gaining adoption for specific enterprise functions, according to speakers at the [AI Agent Conference](https://www.agentconference.com/) this week in New York.

The popularity of new, highly capable AI coding agents has grown dramatically over the past year. Still, the code they generate cannot be trusted in production, said [Datadog](https://www.datadoghq.com/)’s Chief Scientist, [Ameet Talwalkar](http://linkedin.com/in/atalwalkar), in the opening keynote.

> “One of the hardest things for humans to do is no longer building production systems. It’s actually reviewing the vibe-coded software that gets shipped into production.”  
> —Ameet Talwalkar of Datadog

“One of the hardest things for humans to do is no longer building production systems. It’s actually reviewing the vibe-coded software that gets shipped into production,” Talwalkar said.

## Challenges of vibe-coded software

Datadog is extending its observability product line to model real-world systems and predict production issues with AI agents before they happen, he said.

The most popular use of AI agents in business applications is for customer service and customer assistance chatbots.

T-Mobile, for example, uses AI agents to handle 200 thousand customer conversations a day, said [Julianne Roberson](https://www.linkedin.com/in/julianne-roberson-07206557/), Director of AI Engineering at T-Mobile. This project took about a year to complete, she said.

Zhou Yu, co-founder and CEO of ArklexAI, an agentic framework supplier, told *The New Stack* that the company’s new ArkSim product aims to shorten time-to-market for customer-facing bots by simulating AI-agent interactions with customers. AtkSim collects data to improve quality, since agentic interactions are not deterministic.

“You can use Claud Code to build an agent in five minutes, but you don’t know what it will do when it goes into production, especially when you have a large group of customers,” Yu said.

“You don’t know what people are going to do with it. We create simulations of your users so you can get an idea of what the user experience is and how to improve it.”

## Simulating the user experience

“Initially, it was all about building and deploying agents,” said [Joe Moura](https://www.linkedin.com/in/joaomdmoura/), founder and CEO of leading agent framework supplier [CrewAI](https://crewai.com/), in his keynote. “But now it’s all about security and enterprise adoption.”

Moura told *The New Stack* that CrewAI added enterprise features in response to customer requirements. They became a leading framework because they started early — 2003 — and offered an opinionated platform that encoded agentic best practices, he said.

Yu of Arklex told *The New Stack* that, despite Walmart still using its original agent framework product, agent frameworks have become commoditized, which is why they pivoted to simulation.

In the future, Moura said, CrewAI will focus on “entangled agents” that adapt automatically to what their customers are doing with them.

“What I’m calling entangled agents are agents that get better over time. Beyond self-improving agents is this idea that entangled agents become unique for that company,“ Moura said.

## Solving the hallucination problem

LLMs often produce incorrect results and hallucinations, said Akamai CTO [Bobby Blumofe](https://www.linkedin.com/in/robert-blumofe-258233/) in his keynote. AI agents that rely solely on an LLM are unlikely to produce accurate results.

“As you all probably know, most chatbots, when they sample from an LLM, sample probabilistically. The same chatbot can give you different answers at different times,” he said.

Pulling information from a web search into the context window is a huge change, he added. “It’s fundamental to everything that we’re talking about when it comes to producing a correct result.”

Providing context to agents as a knowledge graph to improve results is also increasingly popular, [Chang She](https://www.linkedin.com/in/changshe/), founder and CEO of [LanceDB](https://www.lancedb.com/), told *The New Stack*.

Lance DB has been adopted as a storage plug-in for OpenClaw, he said, and improves agent developer productivity by unifying access to multiple data modalities such as voice, video, text, structured, and unstructured data.

In addition to supporting the popular open source multi-modal Lance Format, “there’s now a new Lance Graph project so you can also store knowledge graphs,” he added.

“Our first thought was, how do we tightly integrate an AI product into our platform?” [Tim Dreyer](https://www.linkedin.com/in/timgdreyer/), Sr. Director, Analyst Relations, at cloud telephony provider [Ring Central](https://www.ringcentral.com/), told *The New Stack*.

“We saw a demand for improving productivity, so we introduced a product called AI Conversation Expert as a kind of post-call analysis tool,” Dreyer said. “An AI agent analyzes the call recording and looks for areas for improvement and how we can provide coaching insights.”

> “Our goal isn’t to eliminate a live agent. We’re trying to make their lives easier. If we can offload fifty or sixty percent of the tedious stuff… that leaves them more time for strategic work.”  
> — Tim Dreyer of Ring Central

Following the initial success of the Conversation Expert agent, “we added an AI Receptionist agent,” he added. “Our goal isn’t to eliminate a live agent. We’re trying to make their lives easier. If we can offload fifty or sixty percent of the tedious stuff that they have to do, that leaves them more time for strategic work.

## Focusing on human supervision

Things have changed since Bill Gates famously wrote about [AI agents](https://www.gatesnotes.com/ai-agents) in 2023, highlighting the importance of autonomy.

Few speakers and exhibitors at the conference spoke about autonomy as a driving force for adoption; rather, they tended to characterize it as a long-term goal to be achieved by taking careful initial steps to resolve or eliminate errors.

The debate about whether AI agents will replace humans or “supercharge” humans is more front and center now.

A strong conclusion from the discussion on agents in the enterprise is that, whatever tasks and roles are assigned to AI agents, human supervision remains necessary.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/01/9843bda4-cropped-6e8aff6e-eric-newcomer-intellyx-analystwithhand2023-s341x512.jpg)

Eric Newcomer is CTO at Intellyx. He has served as CTO for leading integration vendors WSO2 and IONA Technologies and as Chief Architect for major enterprises such as Citibank and Credit Suisse. He has created some of the best-known industry...

Read more from Eric Newcomer](https://thenewstack.io/author/eric-newcomer/)