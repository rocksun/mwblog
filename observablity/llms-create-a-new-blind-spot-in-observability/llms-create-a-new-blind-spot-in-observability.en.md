Teams that have run Software as a Service (SaaS) products know the routine: An alert goes off, and everyone scrambles to the [observability stack](https://thenewstack.io/introduction-to-observability/) first. [Metrics, logs, and traces](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/) have been the signals that help engineers figure out what broke, why users are stuck or where a service-level agreement (SLA) may have slipped. And for years, these tools have worked well enough.

But then AI showed up.

Behind all the hype and potential surrounding copilots, chat interfaces, and [intelligent assistants](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/), engineering teams have quietly run into something more complicated: Large language model (LLM)-powered applications don’t behave like traditional software, and the tools we’ve relied on can’t always fully explain what’s happening under the hood.

## **Why LLMs break traditional observability**

If [microservices](https://thenewstack.io/introduction-to-microservices/) are like puzzle pieces that fit together, [LLMs](https://thenewstack.io/introduction-to-llms/) are more like improv actors. They take direction, but the outcomes aren’t entirely predictable. This unpredictability changes the entire equation for reliability.

LLM workloads are:

* **Probabilistic.** The same inputs don’t always produce the same output.
* **Transient and multistep.** A single user request might trigger retrieval, multiple model calls, tool execution, parsing and retries.
* **Constantly evolving.** Prompt templates change weekly, model versions get swapped out and quality fluctuates without warning.

A simple user search can trigger a cascade of steps, so when something goes wrong, where do you even start? Logs don’t explain why the model hesitated or how a prompt drifted over time. Metrics can’t tell you if a hallucination slipped into a response that ended up on a customer’s screen.

It’s not that the legacy tools are bad; they just weren’t built for systems that reason, adapt and change this quickly.

## **What teams actually end up monitoring**

Once LLMs move into production, teams quickly realize they are watching a new set of signals every day:

* **Token usage**, because cost is directly tied to prompt and response size, often chosen by developers with little visibility.
* **Latency**, especially when AI sits in the critical path of a customer-facing API.
* **Error rates**, from model failures, tool calls, or upstream integrations.
* **Response quality**, including correctness and hallucinations, which traditional telemetry cannot measure.

These are reliability concerns, but they do not map cleanly to CPU, memory or request counts.

## **What Does LLM Observability Really Mean?**

LLM observability isn’t a fancy dashboard or another logging format. It’s a way to understand how AI behaves in production.

We don’t just want to know if a request finished; we want to know what the model attempted to do, how it arrived there and whether the result was worth the cost. That requires new dimensions of telemetry, including:

* **Prompts and feedback:** Prompt versions, runtime substitutions and user feedback need to be treated as first-class signals. When quality degrades, teams should be able to trace it back to a prompt change, just like a code deploy. In practice, this becomes version control for language.
* **Tracing agent pipelines:** Today’s LLM apps are workflows, not calls, because one step triggers another, then another. Observability needs to follow that full chain: retrieval time, model calls, tool execution, parsing and retries. When you can trace the entire journey, debugging stops being a guessing game.
* **Latency, token usage and model choice:** Engineering teams are discovering that reliability, performance and cost are tightly entangled. One slow model call can stall an entire workflow. One verbose prompt can triple token spend. [Observability must surface these trade-offs clearly](https://thenewstack.io/how-ai-can-help-it-teams-find-the-signals-in-alert-noise/) so teams can make informed decisions.
* **Retrieval analysis:** For [retrieval-augmented generation (RAG](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary/)) workloads, the model is only as good as the context it’s given. Understanding retrieval performance, cost and relevance will become as important as tracking GPU usage. Garbage in, garbage out, as the saying goes. But now the garbage comes from a vector store.

## **Instrumenting without pain**

One reason many teams drag their feet on observability is instrumentation. SDKs, code patches, proxies and agents can feel endless. AI stacks evolve faster than most teams can instrument them. New models, new tools and new workflows appear monthly. In many organizations, engineers are not even sure which models are currently running in production.

This is pushing observability down the stack. Instead of relying on application-level instrumentation, newer approaches hook into the infrastructure itself, sometimes through kernel-level visibility,such as eBPF, which observes traffic without modifying code. For engineering teams, that’s a win: Visibility on day one, even as pipelines change over time without modifying code or redeploying services.

For engineering teams, that matters. Visibility on day one is often more valuable than perfect instrumentation that arrives too late.

## **Cost, Quality and Reliability Intersect**

With LLM observability in place, teams usually notice something surprising: The biggest reliability issues are often cost issues in disguise.

Common discoveries include:

* Latency is not caused by the model but by the retrieval call before it.
* A premium model is being used for tasks that a smaller one handles perfectly well.
* A single overly verbose prompt is driving half the monthly token bill.
* A hallucination traces back not to the model, but to stale context retrieved weeks ago.

The moment you can see those patterns, optimization goes from fixing bugs to adjusting behavior. And that’s a different mindset.

## **Security isn’t optional**

There’s yet another wrinkle. AI workloads often carry customer data, internal documents, or proprietary knowledge straight into prompts. That means observability data frequently contains information that compliance teams would never allow to leave the company in any other circumstance.

Many organizations respond by keeping LLM telemetry inside their own cloud boundaries, whether through self-hosted or BYOC (bring-your-own-cloud) models. Sending prompts or completions to a third-party service for monitoring is simply too risky.

Observability has to evolve, but it has to do so responsibly.

## **Creating a path to production-ready AI**

AI isn’t replacing observability, but it’s forcing it to grow up. The shift looks something like this:

* From debugging code to evaluating model behavior
* From request traces to workflow traces
* From resource monitoring to token and model monitoring
* From uptime to quality and correctness
* From dashboards to continuous optimization loops

LLM observability doesn’t just make AI-powered applications more reliable. It makes them cheaper, safer and genuinely worthy of being called “production-ready.”

Just as observability helped SaaS scale, it will shape the next generation of intelligent software as it matures.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/01/2bb3b428-shahar.jpg)

Shahar Azulay, CEO and co-founder of groundcover, the startup reinventing the cloud native application performance monitoring domain with eBPF, is a serial R&D leader. Shahar brings experience in the world of cybersecurity and machine learning having worked as a leader...

Read more from Shahar Azulay](https://thenewstack.io/author/shaharazulay/)