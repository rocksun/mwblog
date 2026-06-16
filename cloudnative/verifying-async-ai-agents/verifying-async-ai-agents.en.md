*Async agents are only useful if you can trust what they hand back. In a distributed system, that trust comes down to the runtime you can give them: in the inner loop, before the PR.*

Ido Pesok at Cognition [recently published a post](https://x.com/ido_pesok/status/2060416230641881336?s=20) about a milestone worth sitting with.

For the first time, his team triggers more Devins asynchronously, from events, schedules, automations, and other agents, than they do in interactive sessions. The agents are no longer something a developer drives. They run on their own and hand back work.

The number is a milestone. The point is what it forces.

When a developer drove every agent, that developer was also the verifier. They read the diff, ran it against the real system, and decided if it was right. Take the developer out of each step, and you remove the verifier, too. Now the agent has to verify its own work at the speed and volume at which agents generate code. As Ido puts it, async agents are only useful if [developers can trust](https://thenewstack.io/fix-developer-burnout-outages/) what they return.

> “An async agent that cannot verify itself is not saving anyone time. It is opening a PR and asking something downstream to grade it.”

That reframes the whole problem. Generation stopped being the constraint a while ago. The constraint is verification. And an async agent that cannot verify itself is not saving anyone time. It is opening a PR and asking something downstream to grade it.

## Why a green test run can mean nothing

A [harnessed agent](https://thenewstack.io/agent-harness-distributed-feedback-problem/) does real work on its own. It writes the code, runs the unit tests it can run locally, exercises its mocks, and reports back green. The trouble is what green means.

The agent wrote those mocks. It wrote them to match its own model of how the dependency behaves, and that model is exactly what might be wrong. So the agent tests its change against its own assumptions; if those assumptions pass, nothing in that loop ever touches the part of reality the agent guessed at. A clean run against a stub is evidence the agent is internally consistent. It is not evidence the change works.

In a service that runs in one place, this gap is small. In a cloud-native system, it is the whole risk. The change does not live alone. It lives next to the services it calls, the brokers and databases it depends on, and a mesh enforcing timeouts and retries it cannot see from inside its own process. The failures that matter live at those boundaries. A contract that drifted. A field that serializes differently than the consumer expects. A downstream call that now times out under the retry policy. A schema change that nothing local will catch.

None of that behavior exists until the change runs beside the rest of the system. So the agent can record a flawless run and still ship something that takes down a service two hops away under real traffic. Green locally, broken in production. The agent did everything right. The environment in which it did it was the issue.

## Where the loop closes decides what a defect costs

Here is the part that gets expensive.

A failure the agent catches while it is still iterating costs seconds. It runs the change, sees the real error, fixes it, runs again. No human ever knows it happened.

The same failure caught after the PR is merged costs hours, and not the agent’s hours. By then, the agent has moved on. The context is cold. Some engineer gets pulled in to debug a boundary failure in code they did not write, produced by an agent that cannot re-explain what it was thinking.

That is the good case. The bad case is that other changes are already stacked on top of the broken one. Other agents built against the wrong behavior. Now you are not fixing one PR. You are unwinding a chain.

This is the cost that never shows up in a demo and always shows up in the quarter. When one developer ran one agent, rework was bounded by that developer. When agents run agents and merge in parallel, every defect that escapes the inner loop lands in a shared system that other work already assumes is correct.

Generation got cheap. Catching a bad change late did not. Push verification to the right, after the PR, and rework grows with every agent you add. Push it to the left, into the inner loop, and most defects never become PRs at all.

> “Generation got cheap. Catching a bad change late did not.”

Adding agents does not automatically lift throughput. If verification still happens after the merge, more agents just means a longer queue of plausible-looking changes waiting to be proven wrong by a person. You scaled the writing and left the trusting exactly where it was.

![Workflow loop after the PR, and also the inner loop within.](https://cdn.thenewstack.io/media/2026/06/2aea674d-image1-1024x547.png)

*Verify after the PR, and a boundary failure surfaces late and bounces back as human rework. Verify in the inner loop, and the agent runs against a real ephemeral runtime, fixes its own failures, and opens a PR that is already proven against the system.*

## What closing the loop actually looks like

The fix is not more checks after the fact. It is a loop that closes before the PR.

Give the agent an isolated runtime that behaves like production. It deploys its change there. It runs the change against the real surrounding services, not their mocks. It reads the real failure. It fixes. It runs again. The scope of what it checks is deliberately wide: not just unit tests, but also the integration paths, the contracts, and the downstream behavior under real routing. The agent keeps looping until every check is green against the actual system, and only then does it open a PR.

Now the PR means something different. It arrives already verified against the world it has to live in. The human review is about intent and design, not “did this agent quietly break something three services away.” That question was answered by the agent in seconds before the PR existed.

That is the closed loop that async development needs. The agent is not submitting a draft for grading. It is delivering a change it has already proved out.

## Isolation, fidelity, cost. Most answers give you two.

The catch is the runtime. At the agent scale, the usual options each fail on a different set of axes: isolation, fidelity, and cost.

Shared staging gives you fidelity and low marginal cost. It gives you no isolation. Point a hundred agents at it, and they corrupt each other’s runs. One agent’s half-finished change is another agent’s flaky test, and access to the environment becomes the bottleneck.

Full per-PR environments give you isolation and fidelity. They cost you everything else. Minutes to stand up, close to a second copy of production each, created and torn down thousands of times a day. The economics do not survive contact with agent scale.

Mocks and agent-owned sandboxes provide isolation and are cheap and fast. They give you no fidelity. This is the model that works beautifully for software that runs on one machine, and it is the exact model that fails for distributed systems, because the agent is back to testing against its own assumptions.

You need all three at once. The way to get there is to stop duplicating the system and start sharing it. Run one production-like environment in the cluster. Isolate only the service the agent changed, and route a tagged request through it so the change exercises the real surrounding services. Isolation is request-scoped. Fidelity is real because the dependencies are real. Cost is amortized because thousands of ephemeral environments share a single cluster and spin up in seconds.

![Diagrammatic representation of the speed, fidelity, and cost trilemma.](https://cdn.thenewstack.io/media/2026/06/fcfdadc6-image2-1024x727.png)

*Shared staging sacrifices speed. Full per-PR environments sacrifice cost. Mocks and sandboxes sacrifice fidelity. Sharing a production-like environment and isolating only the service being tested is how you get all three.*

## The future is verified, and it closes in the cluster

Ido is right that the future of async development is verified. As harnesses improve, [agents will write more of the code](https://thenewstack.io/ai-agents-software-engineering/) and the interactive session will recede to the edge cases. What separates an agent you trust from one you babysit is verification. And the runtime bounds verification the agent can reach.

> “What separates an agent you trust from one you babysit is verification.”

In a cloud-native system, that runtime is the whole game, and it lives in the cluster, next to everything the change has to work with.

That is the pattern we build at [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content): Kubernetes-native ephemeral environments that let an agent exercise a change against the real surrounding services in seconds before the PR, at the parallelism async development demands. If you are pointing coding agents at a cloud-native system and watching them hit the verification wall, that is the gap to close first.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)