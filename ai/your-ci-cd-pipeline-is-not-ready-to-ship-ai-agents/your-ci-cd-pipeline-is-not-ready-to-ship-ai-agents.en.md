Let’s be honest with ourselves for a minute. If you look past the hype cycles, the viral Twitter demos and the astronomical valuation of foundation model companies, you will notice a distinct gap in the AI landscape.

We are incredibly early, and our infrastructure is failing us.

While every SaaS company has slapped a copilot sidebar onto its UI, actual autonomous agents are rare in the wild. I am referring to software that reliably executes complex and multistep tasks without human hand-holding. Most agents today are internal tools glued together by enthusiastic engineers to summarize Slack threads or query a SQL database. They live in the safe harbor of internal usage where a 20% failure rate is a quirky annoyance rather than a churn event.

Why aren’t these agents facing customers yet? It is not because the models lack intelligence. It is because our delivery pipelines lack rigor. Taking an agent from cool demo to production-grade reliability is an engineering nightmare that few have solved because traditional CI/CD pipelines simply were not designed for non-deterministic software.

We are learning the hard way that shipping agents is not an AI problem. It is a systems engineering problem. Specifically, it is a [testing infrastructure problem](https://thenewstack.io/why-your-microservice-integration-tests-miss-real-problems/).

## **The Death of ‘Prompt and Pray’**

For the last year, the industry has been obsessed with frameworks that promised magic. You give the framework a goal and it figures out the rest. This was the [“prompt and pray”](https://www.oreilly.com/radar/beyond-prompt-and-pray/) era.

But as recent discussions in the engineering community highlight, specifically the insightful [conversation around 12-Factor Agents](https://github.com/humanlayer/12-factor-agents), production reality is boringly deterministic. The developers actually shipping reliable agents are abandoning the idea of total autonomy. Instead, they are building robust and deterministic workflows where large language models (LLMs) are treated as fuzzy function calls injected at specific leverage points.

When you strip away the block-box magic of the LLM, a production-grade agent starts to look a lot like a conventional microservice. It has a control flow, state and dependencies. It needs to interact with the world to be useful.

The 12-Factor philosophy correctly argues that you must own your control flow. You cannot outsource your logic loop to a probabilistic model. If you do, you end up with a system that works 80% of the time and hallucinates itself into a corner the other 20%.

So we build the agent as a workflow. We treat the LLM as a component rather than the architect. But once we settle on this architecture, we run headfirst into a wall that traditional software engineering solved a decade ago but which AI has reopened. That wall is integration testing.

## **The Trap of Evals**

When teams start testing agents, they almost always start with evals.

Evals are critical. You need frameworks to score your LLM outputs for relevance, toxicity and hallucinations. You need to know if your prompt changes caused a regression in reasoning.

However, in the context of shipping a product, evals are essentially unit tests. They test the logic of the node, but they do not test the integrity of the graph.

In a production environment, your agent is not chatting in a void. It is acting. It is calling tools. It is fetching data from a CRM, updating a ticket in Jira or triggering a deployment via an [MCP (Model Context Protocol) server](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/).

The reliability of your agent is not just defined by how well it writes text or code. It is defined by how consistently it handles the messy and structured data returned by these external dependencies.

## **The Integration Nightmare**

This is where the platform engineering headache begins.

Imagine you have an agent designed to troubleshoot Kubernetes pod failures. To test this agent, you cannot just feed it a text prompt. You need to put it in an environment where it can do several things. It must call the Kubernetes API or an MCP server wrapping it. It must receive a JSON payload describing a CrashLoopBackOff. It must parse that payload. It must decide to check the logs. Finally, it must call the log service.

[![](https://cdn.thenewstack.io/media/2025/12/044f79d7-image1-1024x631.png)](https://cdn.thenewstack.io/media/2025/12/044f79d7-image1-1024x631.png)

Source: Signadot

If the structure of that JSON payload changes, or if the latency of the log service spikes, or if the MCP server returns a slightly different error schema, your agent might break. It might hallucinate a solution because the input context did not match its training examples.

To test this reliably, you [need integration testing](https://thenewstack.io/we-need-a-new-approach-to-testing-microservices/). But integration testing for agents is significantly harder than for standard web apps.

## **Why Traditional Testing Tails**

In traditional software development, we mock dependencies. We stub out the database and the third-party APIs.

But with LLM agents, the data is the control flow. If you mock the response from an MCP server, you are feeding the LLM a perfect and sanitized scenario. You are testing the happy path. But LLMs are most dangerous on the unhappy path.

You need to know how the agent reacts when the MCP server returns a 500 error, an empty list or a schema with missing fields. If you mock these interactions, you are writing the test to pass rather than to find bugs. You are not testing the agent’s ability to reason. You are testing your own ability to write mocks.

The alternative to mocking is usually a full staging environment where you spin up the agent, the MCP servers, the databases and the message queues.

But in a modern microservices architecture, spinning up a duplicate stack for every pull request is prohibitively expensive and slow. You cannot wait 45 minutes for a full environment provision just to test if a tweak to the system prompt handles a database error correctly.

## **The Need for Ephemeral Sandboxes**

To ship production-grade agents, we need to rethink our CI/CD pipeline. We need infrastructure that allows us to perform high-fidelity integration testing early in the software development life cycle.

We need ephemeral sandboxes.

A platform engineer needs to provide a way for the AI developer to spin up a lightweight, isolated environment that contains:

* The version of the agent being tested.
* The specific MCP servers and microservices it depends on.
* Access to real (or realistic) data stores.

Crucially, we do not need to duplicate the entire platform. We need a system that allows us to spin up the changed components while routing traffic intelligently to shared and stable baselines for the rest of the stack.

[![Intelligently routing traffic using an agent ](https://cdn.thenewstack.io/media/2025/12/d509ff94-ephemeral-sandbox-diagram_updated.png)](https://cdn.thenewstack.io/media/2025/12/d509ff94-ephemeral-sandbox-diagram_updated.png)

Source: Signadot

This approach solves the data fidelity problem. The agent interacts with real MCP servers running real logic. If the MCP server returns a complex JSON object, the agent has to ingest it. If the agent makes a state-changing call like restart pod, it actually hits the service or a sandboxed version of it. This ensures the loop is closed.

This is the only way to verify that the workflow holds up.

## **Shifting Left on Agentic Reliability**

The future of AI agents is not just better models. It is better DevOps.

If we accept that production agents are just software with fuzzy logic, we must accept that they require the same rigor in integration testing as a payment gateway or a flight control system.

We are moving toward a world where the agent is just one microservice in a Kubernetes cluster. It communicates via MCP to other services. The challenge for platform engineers is to give developers the confidence to merge code.

That confidence does not come from a green checkmark on a prompt eval. It comes from seeing the agent navigate a live environment, query a live MCP server and execute a workflow successfully.

## **Conclusion**

Building the agent is the easy part. Building the stack to reliably test the agent is where the battle is won or lost.

As we move from internal toys and controlled demos to customer-facing products, the teams that win will be those that can iterate fast without breaking things. They will be the teams that abandon the idea of “prompt and pray” and instead bring production fidelity to their pull request (PR) review. This requires a specific type of infrastructure focused on request-level isolation and ephemeral [testing environments that work natively within Kubernetes](https://thenewstack.io/kubernetes-isnt-your-ai-bottleneck-its-your-secret-weapon/).

Solving this infrastructure gap is our core mission at Signadot. We allow platform teams to create lightweight [sandboxes to test agents](https://thenewstack.io/sandbox-testing-the-devex-game-changer-for-microservices/) against real dependencies without the complexity of full environments. If you are refining the architecture for your AI workflows, you can learn more about this testing pattern at [signadot.com](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q4_25_sponsored_content).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)