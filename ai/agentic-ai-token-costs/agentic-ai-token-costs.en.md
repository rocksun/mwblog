Finding the most capable model at the lowest cost has always been the goal. But as agentic AI evolves, a new problem is frustrating engineers: token consumption is becoming too high across AI systems. Every agent operation consumes tokens, but in very different ways. For instance, a moderately complex agent request [can consume 20,000 to 60,000 tokens](https://arxiv.org/abs/2604.22750) across its reasoning chain, but a nontrivial engineering task can burn 150,000 to 200,000 tokens per problem.

> Every agent operation consumes tokens, but in very different ways.

Developers are realizing that selecting the right model is important, but the bigger issue is limiting unnecessary token movement throughout an agent’s workflow. That is why teams are starting to consider how to accomplish the same tasks with fewer tokens.

## **Compounding costs across agents**

The costs add up quickly. A task that takes about 50,000 tokens with one agent can easily consume several hundred thousand with multiple specialized agents together. That’s because each one needs enough context to do its job. It’s not unusual for an agent to process 30,000 tokens of context just to return a 500-token response, and those exchanges add up over the course of a workflow. Each handoff effectively pays a tax in input tokens that compounds with every loop iteration.

> Each handoff effectively pays a tax in input tokens that compounds with every loop iteration.

This is especially noticeable among multi-agent architectures. When one agent delegates to another, it must encode its current state and task instructions into the downstream agent’s context window. The receiving agent processes all of that, produces a result, and passes it back. Then the orchestrating agent reingests it alongside everything else it’s tracking. Every exchange adds another layer of overhead.

## **Building more token-efficient architectures**

A growing collection of strategies addresses this problem. Three practical solutions stand out:

**Compress context, preserve reasoning**

The most direct solution is to reduce the amount of context an agent carries from step to step. Rather than accumulating an ever-growing interaction history and replaying it with every task, systems can summarize earlier portions of a conversation or working memory before passing them forward.

One way to do that is by narrowing the agent’s field of view. Instead of handing it an entire codebase or document collection, the system surfaces only what’s relevant to the task at hand. Go too far, though, and the agent can lose important context that it will need later.

To make this work, the system needs a compact memory layer of key facts and decisions alongside the compressed context. The agent needs to recall the reasoning chain without having to reread it each time.

**Route tasks to cheaper models**

Hierarchical routing lets engineers parse a JSON response, format a log entry, or check whether a file exists without using the same model used to architect a system design. It assigns each subtask to the smallest model that can reliably do the job. A lightweight model, for instance, handles routine classification, extraction, and formatting steps, while a more suitable model handles decisions that truly require deeper reasoning.

So if 60 to 70 percent of an agent’s steps are routine operations, then a smaller model can handle the work at a fraction of the cost, substantially reducing the overall token spend for the workflow.

**Cache reasoning, skip redundancy**

That’s where semantic caching comes in. Instead of solving the same problem twice, it compares the meaning of a new request using embeddings. If the match is close enough, the agent can reuse earlier work instead of generating a new reasoning chain.

The savings make a difference, especially in scenarios involving customer support systems that answer similar questions all day, or even document-processing pipelines that handle thousands of nearly identical files. In such scenarios, reusing prior reasoning can significantly reduce the number of tokens an organization consumes.

## **Measuring what matters**

But these workflows only deliver value if teams see their impact, and many organizations are still figuring out how to measure them effectively. Poorly designed agent loops or inefficient multi-agent handoffs can dominate costs in ways that are invisible when you’re only looking at per-request pricing.

It’s also easy to focus too much on tokens. Running an agentic application also means paying for GPUs, memory, vector databases, and the tooling needed to monitor everything in production. Saving tokens helps, but it won’t solve the whole problem if the rest of the stack is still expensive.

## **The next phase of AI infrastructure**

The next generation is increasingly focused on building systems based on better architectural decisions. That means context management, model invocation, task decomposition, and intermediate work reuse are becoming just as important as inference pricing or even benchmark scores.

Model capabilities will continue to improve, and inference costs will likely fall. But if autonomous agents become the dominant way organizations build AI applications, the systems that scale most effectively may not be the ones with the cheapest models, but those that waste the fewest tokens.

> The systems that scale most effectively may not be the ones with the cheapest models, but those that waste the fewest tokens.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)