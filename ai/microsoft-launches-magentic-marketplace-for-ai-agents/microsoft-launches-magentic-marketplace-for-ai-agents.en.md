Microsoft Research has just launched an open source environment for studying agentic markets, called [Magentic Marketplace](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/). In advance of the release, I spoke to [Ece Kamar](https://www.linkedin.com/in/ecekamar/), Managing Director of the AI Frontiers Lab at Microsoft Research.

Kamar’s research group had previously developed [AutoGen](https://microsoft.github.io/autogen/stable/), an agentic development framework that has become popular with Python developers — especially for [building multi-agent AI systems](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/). In part due to that success, the development of Magentic Marketplace was inspired by AutoGen.

“AutoGen is part of the Microsoft Agent Framework [that] was released a month ago,” Kamar told me. “So we were able to get all of that programming layer and ship it on a Microsoft product. And now we use all of the learnings from AutoGen — what people do with AutoGen — to think about what agents are going to become.”

## What Is Magentic Marketplace?

The idea of Magentic Marketplace is to allow researchers to simulate a marketplace for AI agents, to test “how agents negotiate, transact, and collaborate under real-world market dynamics.” The marketplace will also monitor safety and fairness in these systems.

[![Magentic Marketplace high-level](https://cdn.thenewstack.io/media/2025/11/31cc8d96-magentic-marketplace1.jpg)](https://cdn.thenewstack.io/media/2025/11/31cc8d96-magentic-marketplace1.jpg)

Magentic Marketplace high-level.

Although Magentic Marketplace is a research project, it could easily become a commercial project later — similar to how AutoGen has evolved into [Microsoft Agent Framework](https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/) (the result of a recent merger between AutoGen and Semantic Kernel, an SDK [I profiled back in April 2023](https://thenewstack.io/microsoft-semantic-kernel-for-ai-dev-a-chat-with-john-maeda/)).

“We are expecting that there will be public markets coming,” Kamar said. “We [Microsoft Research] are probably not going to be the team to build them, sitting in research. But […] when you look into some of the latest releases coming in this space, it’s all kind of gearing towards starting to test these marketplaces.”

“I personally believe that a lot of the way we use technology will be rethought, redesigned with these agents in mind,” she added. “And marketplaces is going to be one of the domains I expect to see a lot of activity going on.”

## Protocols in a ‘Society of Agents’

Like any good research project, there is a working theory about how AI agents should work. Kamar, whose PhD at Harvard during the 2000s was on the very subject of AI agents, is using the phrase “society of agents” to describe the project’s goals.

“In this notion of ‘society of agents’, it is really about AI agents coming together, interacting, collaborating, negotiating,” she said. “Also, with the supervision of people, and really uncovering how the world is going to look like when we have these agents, how having these agents by our side is going to be able to address some of the inefficiencies we have in the world.”

> “In this notion of ‘society of agents’, it is really about AI agents coming together, interacting, collaborating, negotiating.”  
> **– Ece Kamar, Microsoft Research**

A key part of the research is testing communications protocols like [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) and [Agent2Agent](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) (A2A), along with emerging payment protocols. For agentic commerce, there isn’t yet a default protocol — although recently OpenAI announced the [Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/) (ACP), Google announced [Agent Payments Protocol](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) (AP2) in September, while others (like Shopify) have been using [MCP-UI](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/).

Kamar also expects new protocols to emerge that will help agents collaborate, or for protocols like MCP and A2A to expand for marketplace use cases. For example, what is the right way for agents to show information for a transaction?

## Key Challenges and Biases in AI Agent Simulations

Kamar said they also recognize the risks that come with AI agents — like safety and bias — and she described some of the challenges they’ve come across so far in the marketplace simulations.

“One of the things that we are seeing is that, again, while we have these communication protocols [MCP, A2A, et al], the models powering these agents sometimes can get into some kind of a decision paradox. If they have too many choices, they may not be that effective yet in terms of being able to make the right choices.”

[![Magentic Marketplace in action](https://cdn.thenewstack.io/media/2025/11/3a42a9b9-magentic-marketplace2.jpg)](https://cdn.thenewstack.io/media/2025/11/3a42a9b9-magentic-marketplace2.jpg)

Magentic Marketplace in action.

The group has also seen “some biases coming up.”

“For example, one of the biases we have identified is something called a ‘proposal bias.’ The models right now are preferring options that are coming up fast. Like, if you’re a fast agent, you are much more preferred whether you have the best proposal or not.”

So while agents have been able to communicate with each other in the marketplace simulation, there is much work to be done to make multi-agent collaboration a reality. To get to the highest level of utility from these marketplaces, Kamar noted, “we will need to train these agents and build them in different ways.”

She mentioned a couple of the technical issues they’ve come across so far in the simulations. One is what she termed “tool space interference”, which basically means the agents get confused by the proliferation of AI tools. “Right now, MCP has so many different tools,” she said, “and sometimes they are named the same way, or even the name conventions are not there yet; and we are seeing that as this protocol is maturing, there are still issues with it.”

> Magentic Marketplace has already shown “the limitations of the existing frontier models when it comes to collaboration and negotiation.”  
> **– Kamar**

In fact, Kamar’s group has itself built an open source MCP tool, called [MCP Interviewer](https://thenewstack.io/new-python-cli-tool-catches-mcp-server-issues-before-agents-do/). She explained that it “helps developers […] kind of interview these tools, look at interference issues, so that they can be more informed about which tools to bring in; and see issues like tool interference before it happens in their real systems.”

The second issue is further down the stack — she noted “the limitations of the existing frontier models when it comes to collaboration and negotiation.” They’ve tried to get LLMs to collaborate with each other to help agents perform a task, and found that model performance degrades with this collaboration.

“So, as a team, we’re also looking into what needs to change in the way models are trained, so that these models can empower stronger agents in terms of their collaboration capabilities,” Kamar said.

## Balancing AI Agent Autonomy with Human Supervision

Those of you old enough to remember the dot-com era of the internet will recall that it took several years for people to feel confident entering their credit card information into a web browser to make an online purchase. So how long will it take to feel confident giving our credit cards — or indeed our personal preferences — to an AI agent?

“I think it is for us, for researchers, it is just very important that we are improving the technology and creating clarity around the technology as much as we can,” Kamar said. “And when it is time for these technologies to be in the hands of the people, we are not giving them something that we built but we don’t really understand; but we are giving them something that we truly understand and we have tested, we understood the rough edges and we have worked on improving them.”

She added that her team also considers when human supervision is appropriate in these agentic systems — more commonly referred to in the industry as “human in the loop.”

> “If we are going to be building these marketplaces and ecosystems, we can also invest time on understanding and building these layers where, as a user, I still have the control…”  
> **– Kamar**

“So I think there is also going to be a spectrum where we are not going to go to full agent autonomy on day one,” she said. “You know, it doesn’t have to be. If we are going to be building these marketplaces and ecosystems, we can also invest time on understanding and building these layers where, as a user, I still have the control — I’m still looking at all the interactions, I’m still looking at the options, I can still ask questions about what the agent is recommending to me.”

Before this interview, I must admit I wasn’t sure why Microsoft would be releasing a simulated marketplace instead of the real thing. But Kamar has convinced me that it’s not only sensible to fully test how agents collaborate before a public marketplace goes live, but it’s actually dangerous *not* to run the simulations first!

Also, Magentic Marketplace should help us improve the LLMs, protocols and AI tooling that companies will need to make a public agent marketplace viable.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)