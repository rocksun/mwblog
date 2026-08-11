I recently argued with a software factory provider, whose position was that coding agents cannot be evaluated.

Their reasoning was understandable. Software engineering is open-ended. Requirements are incomplete. Repositories contain years of undocumented decisions. Two engineers can solve the same problem in completely different ways, and both can be right. An agent may fail one run and succeed on the next. A benchmark can never reproduce all the context, negotiation, and judgment involved in shipping production-grade software.

> “Coding agents are non-deterministic, operate over long horizons, and can produce many valid solutions. None of that makes them unevaluable. It means we need to stop grading them like chatbots.”

All true. But “difficult to evaluate” and “cannot be evaluated” are very different claims.

We already evaluate traditional software systems with many possible implementations. I argue coding agents should be held to the same standard.

## Agent !== Model

A coding agent is *not* just a model.

It is made up of a model, a harness, tools, repository context, instructions, permissions, an execution environment, and a feedback loop. Change any one of those and the outcome can change materially. A stronger model with poor repository context may perform worse than a smaller model with the right tools and a fast test suite.

This is one reason public benchmarks are easy to misuse. A score is often described as if it measures the underlying model, when it actually measures a particular model-agent-environment combination under a particular token and time budget.

When evaluating a coding agent, we are evaluating the whole system.

## “There are many valid solutions”

One objection to coding-agent evals is that exact-match grading does not work. An agent can produce a valid patch that looks nothing like the human-authored reference patch.

I agree. But that just means we need to grade behavior, not compare to a reference diff.

Start the agent from a known repository state. Give it a task and the context available then. Then evaluate the resulting repository against executable contracts:

* Does it build?
* Do the existing tests still pass?
* Do hidden tests for the requested behavior pass?
* Are public APIs and data formats still compatible?
* Do migrations work in both directions?
* Are performance and resource-use limits respected?
* Did the agent modify anything outside the allowed scope?
* Did static analysis or security checks find new problems?

These checks allow multiple implementations while preserving a clear definition of acceptable behavior. They are also much harder to bluff than a prose explanation of what the agent believes it accomplished.

Some qualities are not fully captured by executable tests, e.g., maintainability, architectural fit, naming, or whether a change makes the next change unnecessarily difficult. These require judgment.

But human-written software has never stopped being testable because code review contains judgment.

## A coding agent eval needs more than a pass rate

“Did the tests pass?” is necessary. I argue it’s not enough in this context.

An agent can make the new test pass by weakening an existing assertion. It can hard-code an expected value. It can replace a focused implementation with an enormous rewrite that happens to be correct today. It can solve the task after twenty failed attempts, consume an unreasonable budget, and leave behind changes no engineer would approve.

A useful evaluation therefore has several layers:

1. **Outcome**: Did the final repository satisfy the task?

2. **Change** quality: Would we accept the implementation?

3. **Trajectory**: How did the agent get there?

4. **Human intervention**: How much help did the agent need?

5. **Economics**: Was the result worth the financial cost?

6. **Production impact**: What happened after the merge?

No single number captures all six layers, and that is fine. Engineering teams already use a scorecard rather than one magic metric to assess delivery.

## Non-determinism is a statistical problem

A coding agent may solve the same task on one run and fail it on another. That is often presented as evidence that evaluation is impossible.

Really, it’s evidence that a single run is insufficient. Run the same task multiple times with controlled starting conditions. Report the success distribution, not the best demo. Measure pass rate at a fixed budget, variance in cost and completion time, and the frequency of serious failure modes. Include confidence intervals when comparing systems.

> “We must ask: ‘How often can it solve this class of task, within our budget, without introducing an unacceptable failure?'”

For a [production coding agent](https://thenewstack.io/agent-runtime-application-server/), we should not ask: “Can it solve this task?”

We must ask: “How often can it solve this class of task, within our budget, without introducing an unacceptable failure?”

## Open-ended work still has boundaries

The hardest tasks begin with incomplete intent: “make onboarding better,” “modernize this service,” or “build the new billing workflow.” There may be no complete test suite because deciding what to build is part of the work.

This is where an eval should include interaction, not pretend ambiguity does not exist.

[Give the agent access](https://thenewstack.io/googles-data-commons-gives-ai-agents-access-to-a-vast-trove-of-stats/) to a controlled user or product-owner simulator backed by a private set of requirements. Score whether it identifies ambiguity, asks useful questions, incorporates the answers, and avoids inventing requirements. Then evaluate the finished system against the hidden behavioral contract.

The agent should not be penalized for asking a necessary question. It should be penalized for confidently implementing the wrong assumption.

Newer research benchmarks are already moving in this direction. [ICAE-Bench](https://arxiv.org/abs/2607.21217) evaluates agents as interactive project builders, while [Dialogue SWE-Bench](https://arxiv.org/abs/2606.13995) isolates dialogue as a capability distinct from raw coding performance. The methods will evolve, but the premise is clear: ambiguity changes the shape of the evaluation; it does not make evaluation impossible.

## The standard is useful, not perfect

No evaluation will capture the full future cost of a design decision. No private suite will represent every task an engineering organization will encounter. Human rubrics will contain disagreement. Hidden tests will miss cases. Production will surprise us.

Perfection is not the bar – at the end of the day, humans do not produce perfect software either. The bar is whether the evaluation helps us make a better decision than demos, anecdotes, or provider claims alone.

> “Claiming that coding agents cannot be evaluated gives providers the benefits of an engineering product without the burden of engineering evidence.”

If an evaluation can answer those questions with reproducible evidence, it is doing its job.

Coding agents are harder to evaluate than code-completion models because they do more. They explore, plan, edit, execute, recover, and sometimes negotiate intent. Our evaluation systems [need to observe](https://thenewstack.io/debugging-observable-ai-systems/) that entire loop.

But claiming that coding agents cannot be evaluated gives providers the benefits of an engineering product without the burden of engineering evidence.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/01/4191ee4f-pete-hampton.jpg)

Pete Hampton is a Principal Engineer on the AI/ML team at ClickHouse. The team builds and operates inference infrastructure and AI-powered product features across the ClickHouse Cloud platform.

Read more from Pete Hampton](https://thenewstack.io/author/pete-hampton/)