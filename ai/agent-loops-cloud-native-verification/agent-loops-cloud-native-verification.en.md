Something shifted in the AI coding discourse this month. The argument is no longer about whether agents can write production code or which model is best. It is about who, or what, should be prompting them.

The phrase that captured it, “design loops that prompt your agents,” set off a week of discussion that Matt Van Horn [synthesized well](https://x.com/mvanhorn/status/2063865685558903149). Strip away the noise, and the signal is clear: A third era of  [agentic development](https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/)  is taking shape, and it raises significant questions about what engineers do, what software delivery costs, and what infrastructure must exist beneath it.

For teams building cloud-native applications on Kubernetes, the answers to those three questions are about to matter a great deal.

## Three eras, one direction

Agentic development has moved the human up one level of abstraction at a time.

The first era was prompt-driven. A developer sat inside the loop, typing instructions, reading output, typing corrections. Throughput was capped at one developer’s attention.

The second era is spec-driven, and it is where most adopting teams sit today. The developer invests up front: detailed specifications, context documents, conventions encoded in the repo. The agent executes against the spec, and the human reviews completed work. The unit of work grew from a prompt to a task.

The third era makes the loop itself the unit of work. A loop is a small program that prompts the agent, evaluates the response, decides whether the goal is met, and, if not, prompts again with what it has learned. It runs on a schedule rather than on human attention. Loops dispatch other loops.

The developer no [longer writes the code](https://thenewstack.io/netlify-agent-experience-engineers/), and increasingly no longer writes the task. They write the system that generates, evaluates, and retries the work.

> “The developer no longer writes the code, and increasingly no longer writes the task. They write the system that generates, evaluates, and retries the work.”

Skeptics have called this a “cron job with better marketing”, and the comparison is useful for where it breaks. A cron job executes a fixed script. A loop has a decision-maker in the body: a model that reads the state of the work and chooses the next action. The engineering challenge is everything you wrap around that decision so the loop converges on correct instead of wandering.

## What the developer becomes

In a prompt-driven world, the developer’s leverage came from skill at steering. In a spec-driven world, it came from clarity of intent.

In a loop-driven world, leverage comes from the quality of the system around the agent. The engineering question that matters becomes: What does this loop check before it declares success? What feedback does it receive when it fails? When does it stop?

Those questions split the role in two. Application developers become authors of intent and of loops: they decide what to build and encode the goal. Platform engineers become the owners of what done means.

The checks a loop runs, the environments it runs them in, the budget it operates under, and the evidence it attaches to its output all have to be consistent across every loop in the organization, not improvised by each one.

This is a familiar pattern with a new subject. A decade ago, platform teams turned CI/CD from a thing every team hacked together into a paved road. The verification layer for agent loops is the same transition, except it sits in the inner loop, before any PR exists, at whatever parallelism the loops generate.

## The economics: loops converge, or they burn

It is tempting to assume agents made code generation cheap, so none of this matters. Not quite.

Agents made generation fast, and cheaper than developer hours, but tokens are a real and growing line item. An agent running for hours is a spend decision, and a loop is an agent running indefinitely by design. Budgets that survived interactive sessions do not automatically survive loops.

The first-order response is guardrails: iteration caps, no-progress detection, and spend ceilings. They are necessary, but they only bound the damage of an inefficient loop. They do not make it efficient.

Loop efficiency comes down to two dimensions, and they multiply.

The first is feedback quality, which determines how many iterations the loop needs. A loop that gets a vague failure signal guesses at the cause and tries again. A loop that gets the real error, from the real system, with enough context to localize the cause, fixes the actual problem and moves on. Feedback quality also bounds how correct the loop can ever be: a loop can only converge on what its feedback can see.

The second is where the loop closes, which determines the cost of each iteration. If the loop closes in CI or after the PR, every cycle pays for a pipeline run plus queueing, and the cadence is minutes to hours. If it closes in the inner loop, against a runtime the agent can reach directly, the cadence is seconds.

> “Total loop cost is the product: iterations to verified, times cost per iteration.”

Total loop cost is the product: iterations to verified, times cost per iteration. The dimensions feed each other too. Push truthful feedback to CI, and each cycle slows while the agent iterates on partial signals in between. Pull it into the inner loop, and you compress both terms at once.

## Cloud-native raises the bar for done

For a self-contained program, both dimensions come nearly free. The test suite runs locally in seconds and tells the whole truth, because the whole truth is local.

In a distributed system, the truth is not local. A change is correct or broken based on how it behaves alongside the services it calls, the data stores and queues it touches, and the routing and policy layers it runs under.

The feedback the agent can reach quickly, local tests and stubs, is partial. The feedback that tells the truth traditionally lives in CI and shared staging, where cycles are slow and contended. Cloud-native teams get forced to choose between a fast loop that converges on the wrong target and a truthful loop that iterates at pipeline speed.

I have written before about why the traditional environment options fall short at agent scale. The conclusion that matters here: in cloud-native systems, the loop’s feedback has to come from a runtime, and that runtime has to be reachable from the inner loop. The architecture of a cloud-native agent loop is mostly the architecture of the verification surface you give it.

## The four layers of a cloud-native agent loop

The complete system has four layers. The loop itself is the smallest part.

**The runtime layer.** The loop needs an environment per iteration that behaves like production without costing like production. The answer is lightweight ephemeral environments on a shared cluster: deploy only the services the change touches, and use request routing on one shared cluster to steer the loop’s traffic through them and through a live shared baseline for everything else.

Environments materialize in seconds, marginal cost tracks the changed pods rather than the whole stack, and the feedback comes from real dependencies and real data paths. This is what moves where the loop closes into the inner loop.

**The verification interface.** Agents do not click through dashboards, and they should not invent their own definition of done. The checks a change must pass belong in declarative workflows that platform teams define, version, and expose to agents as the sanctioned way to prove a change.

The organization, not the agent, decides what passing means. The evidence attached to a change comes from a process humans can audit, and human review can concentrate on intent and design.

**The feedback layer.** This is the convergence engine. A pass or fail bit tells the loop to retry but not what to change. The runtime needs to hand back structured results: which check failed, the logs and traces scoped to the loop’s own requests, the behavior diff at the boundary that broke.

Every increment of feedback precision removes guesswork, and removed guesswork is removed cost.

**The control layer.** Budgets, iteration ceilings, no-progress detection, and a durable record of what each loop ran and proved. This is what lets an organization run many loops with confidence instead of one loop with anxiety.

When spend is bounded and convergence is measured, agentic development becomes a capacity you can plan rather than a bill you discover.

“Write loops, not prompts” is the visible tip of a larger claim: the team’s leverage now lives in the verification system the loops share, and that system is owned by the platform organization.

## Where to start

The shift to loop-based development will not arrive as a single decision. It will arrive as one team’s experiment that converges fast and another’s that burns a quarter’s budget producing changes nobody trusts. The difference will be the four layers, not the cleverness of the loops.

For cloud-native teams, the runtime layer is the place to start, because every other layer depends on it. Verification workflows are only as meaningful as the environment they execute in, and feedback is only as truthful as the system that generates it.

That layer is what we build at Signadot: Kubernetes-native lightweight ephemeral environments and governed validation workflows that let agent loops prove changes against the real system, in seconds, in the inner loop. [Check out our docs here to see how it works.](https://www.signadot.com/docs/overview?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content)

If your [agents are writing code](https://thenewstack.io/ai-agents-software-engineering/) faster than your team can trust it, the loop is already telling you which layer is missing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)