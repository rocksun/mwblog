*This is the second part of the “Agentic AI That Ships” series. [Read Part 1](https://thenewstack.io/how-to-build-agentic-ai-that-ships/).*

Previously, we explored why AI initiatives fail and described a fictional auto-shop chain with national presence that’s about to embark on its first agentic AI project. Our fictional chain wants to join the 5% of enterprises already seeing ROI on their AI efforts, and so it has decided to create an agent that will automate a task that store managers have been spending four hours on every week. Next, we’ll dig into the five factors of AI agents that operate with predictable autonomy.

Using the auto-shop chain example, we’ll explore a solution that will reclaim more than 200 hours of management time per store, per year, and can be rolled out in 12 weeks or less. We’ll plant our ROI-flag firmly with an on-time, on-budget, on-quality release of a solution that has:

1. **Narrow context**
2. **Simple tools**
3. **Detailed prompts**
4. **The right model for the use case**
5. **Centralized management of AI assets, connections and policies**

## **Narrow Context**

For agentic AI, context is everything. It defines everything tailored to us that a model must know to answer a question. For example, some international companies may choose to operate by the highest legal standard of all the countries they serve to avoid complications across the board. Asking what should be done by an agent of the company in a given country shouldn’t rely on the generally accepted knowledge of geography alone; it should rely on a combination of both public and internal policy for a given jurisdiction.

In the scenario of our auto-shop chain, the context couldn’t get more narrow. We’re interested in our service tickets. They log every drop off, every pickup, every service performed and survey response collected. There’s a wealth of additional information, such as part numbers and service codes, much of it useless given our current task of transforming survey data trapped in service tickets into a reportable data feed.

For this reason, we’ll want to describe the fewest fields possible for our AI agent to sift through because we want to describe each of them precisely; in this case, we aren’t hiring our AI agents for their creativity.

## **Simple Tools**

We’ll define a query in our service ticket system that gets the drop-off date, the pickup date, the specific services performed and the survey response. We’ll allow our AI agent to access that query through a view or a stored procedure, and we’ll expose it via an AI programming construct called a **tool**.

We’re not going to simply unleash the model on our database and let it “figure out what we need.” We’re going to give it exactly the shape of data needed to solve our problem, and we’re going to give it a dead-simple way to execute: Either get me everything that changed to “closed” between two specific dates, or get me everything that has changed to “closed” in the current week.

We’re going to use [Spring AI](https://thenewstack.io/production-worthy-ai-with-spring-ai-1-0/) and the Model Context Protocol (MCP) to quickly wire our agent to our context. Spring AI will ensure that our code allows for flexibility in model interactions and MCP will ensure that our tools are invoked when needed and that our context flows into the model as it considers our user’s prompt. What’s remarkable about Spring AI is that the majority of what I’ve described above is implemented using human language, not code.

Tools are blocks of code that developers provide and AI makes use of. Developers describe behaviors using plain English, which the LLM then uses to understand how the tool is used. It really is a remarkable paradigm shift where the developer has 90% of their coding replaced by documentation that helps the LLM consume the code correctly, leaving only 10% of the remaining code to actually write.

[![SpringAI code block](https://cdn.thenewstack.io/media/2025/09/b4ab3435-springai_code.png)](https://cdn.thenewstack.io/media/2025/09/b4ab3435-springai_code.png)

Spring AI blends natural language and programming interfaces. (Source: VMware by Broadcom)

I cannot stress enough how revolutionary the concepts demonstrated by the above snippet are to software development. The tool description describes to its consumer (the AI) how to use it and how to understand its response. Back in 2023, we’d have to write dozens, if not hundreds, of lines of code, to mediate the interactions between two unrelated systems.

Here we are, less than two years later, using natural language to instruct AI on how to mediate those interactions for us. All we have to do is provide the functions to be called under the hood when a tool is invoked. But something has to stitch all these function calls together into a meaningful outcome, and that’s where the agent and their system prompt become the glue.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## **Detailed Prompts**

When an agent is instantiated (when the service hosting the agent starts), the first thing that a model will want to know is what the system prompt is for this agent. In other words, what is this agent’s mission and purpose?

In the system prompt, we tell the agent exactly what its job is. We can tell our agent exactly which tasks it can perform and even under what circumstances. Perhaps a task that is initiated during business hours should be scheduled for an off-hours window for processing.

These kinds of things can be baked into prompts incredibly quickly and by mere mortals. No coding required. The system prompt is in plain old English, just like the tool description we reviewed. The following snippet comes from the properties file used to configure our Spring app:

[![System prompt](https://cdn.thenewstack.io/media/2025/09/bfd8871f-system-prompt.png)](https://cdn.thenewstack.io/media/2025/09/bfd8871f-system-prompt.png)

The system prompts driving the behavior of the constrained Customer Satisfaction Data Analyst Agent. (Source: VMware by Broadcom)

Think of the hundreds of lines of code eliminated here in determining, based on time of day and day of week, whether to schedule a process or run it immediately. It’s not just the implementation of that logic, it’s the encapsulation of it and the integration of it so that it can interact with other services. That capability can be completely invented by being described in the agent prompt as long as a tool exists to determine the current date, and another tool exists for scheduling a task.

By being extremely explicit with our agent about what it should do and when with the tools it has at its disposal, we can start to reap the rewards of the predictable autonomy we expect from AI. In this case, the rewards come in the form of over 200 manager hours per year per store. Not too shabby for our first shot over the bow.

## **The Right Model for the Use Case**

[![A simplified model-selection decision tree ](https://cdn.thenewstack.io/media/2025/09/1aa13866-simplified-model.png)](https://cdn.thenewstack.io/media/2025/09/1aa13866-simplified-model.png)

A simplified model-selection decision tree (for illustrative purposes only). (Source: VMware by Broadcom)

Admittedly, the auto-shop example doesn’t provide for much in the way of storytelling around model selection. The first and most important question for every enterprise should be: Are we willing to use public models? Consider that we must send our narrow context to these models; every time we ask a question about a grouping of service tickets, we have to send that [data to the model](https://thenewstack.io/5-useful-datasets-for-training-multimodal-ai-models/) over the wire to evaluate. Perhaps our auto-chain isn’t overly concerned with the contents of the current data set, but over time, the importance of private AI could increase.

This is why we wrap our model interactions in a framework like Spring AI — a business decision to change model providers should not require a massive change to the solution. It will, though, without a layer like Spring AI between the dev and the model.

Were we to tackle scheduling rather than survey data, model selection would have more interesting storytelling. Scheduling requires reasoning, and so a reasoning model will be much more effective than a generic LLM. However, when it comes to asking an LLM to prepare a batch file in a given format using fields cleanly and readily available in a view created for the task, there’s not much savvy needed to make the right decision. The use case is easily handled by any of the major players, public or private, as long as MCP is in their bag of tricks.

## **Day 2 is the Longest Day**

Earlier I mentioned [Spring AI to insulate the developer](https://thenewstack.io/spring-cloud-gateway-the-swiss-army-knife-of-cloud-development/) from the complexities of interacting with one or more models. Interacting with the model is just the tip of the iceberg in terms of needs we must serve to operationalize this inaugural agentic effort. As Tanzu’s AI Native report reveals in detail (available [here](https://go-vmware.broadcom.com/from-cloud-native-to-ai-native)), there is no shortage of jobs to be done to successfully operationalize AI. We need to be able to apply policy across a spate of concerns: Which models are allowed and to which teams? How are tokens issued? How are quotas and chargebacks handled? How are credentials rotated for tools and MCP servers? How do we restrict access to MCP services to subsets of consumers? How do we manage deployments and certify which versions of which models are safe for use?

We need to do all of this and more, and we need to do it in a repeatable manner, for multiple environments, before we ever see the light of production.

Being able to manage the above is important because of what our systems will look like as things evolve. AI agents will have a great deal of symmetry with microservices in terms of underlying technologies and deployment architectures, but with more granularity. The services will be smaller and their tasking more discrete; microservices will be replaced by nanoservices. Our customer satisfaction analysis agent is an example of a nanoservice. We’re going to keep that service small and focused on one thing so it behaves predictably.

There will be hundreds, if not thousands, of nanoservices like this in our fictional auto shop’s future, each with a narrow set of responsibilities and tools. The trade-off for the granularity of our services will be the increase in their numbers. The speed with which AI native solutions will go from idea to production will be both shocking and overwhelming. We will need guardrails if we want to do this sustainably at scale, and that’s what an AInative platform provides.

Without a platform to manage it all, day two becomes month two becomes year two before you have a chance to get your legs under you. [MIT’s paper, critical of enterprise AI rollouts,](https://www.npr.org/2025/08/23/nx-s1-5509946/bubbling-questions-about-the-limitations-of-ai) quantifies this. For the AI efforts that actually made it to production, 67% of them did so using vendor-supplied solutions for AI asset management. Only 22% of the successful systems they created for managing the concerns of their AI integrations. Similarly, [independent research](https://go-vmware.broadcom.com/from-cloud-native-to-ai-native) found the majority of respondents, 82%, believe AI platforms are important or essential for scaling AI.

[![Graph showing that nearly half of IT leaders say AI app platforms are essential for scaling AI](https://cdn.thenewstack.io/media/2025/09/5a895ca6-ai-app-platform-importance.png)](https://cdn.thenewstack.io/media/2025/09/5a895ca6-ai-app-platform-importance.png)

## **Setting Yourself Up to Ship AI Apps at Scale Successfully**

Agentic AI is a powerful thing, but the pitfalls are many. To move quickly and safely while at the same time delivering value, it’s critical that we reduce the problem space we’re asking AI to solve for us. By providing just enough information required to find a solution, and by providing *just enough* capability to our agent via simple tools, we minimize the chances of hallucination poisoning our responses.

Similarly, by crafting a job description for each agent via its prompt, we can constrain the behaviors of our agents, limit the tools they are allowed to access and provide specific expectations of their job performance.

We’ve also learned that not all models are created equally, and that the use case should determine the model we choose. Perhaps most crucially, though, we’ve learned that we double our odds for successful deployment when we use an AI native platform to herd the cats rather than attempting to roll our own AI integration platforms.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/58de93df-cropped-506f2e42-brianfriedman-600x600.jpg)

Brian Friedman is a solutions leader in Tanzu’s Strategic Advisory Practice with Rapid Modernization as his core practice area  With more than 25 years of experience and a self-described “polyglot with a thick .NET accent,” Brian joined Pivotal Software in...

Read more from Brian Friedman](https://thenewstack.io/author/brian-friedman/)

[![](https://cdn.thenewstack.io/media/2025/02/225ef326-jonathan-eyler-werve.jpg)

Jonathan Eyler-Werve has been launching products online for 15 years and has worked in product management, design and full-stack engineering roles. He mentors mid-career PMs, and advises startups and social ventures. He currently looks after app development teams at Broadcom,...

Read more from Jonathan Eyler-Werve](https://thenewstack.io/author/jonathan-eyler-werve/)