*The industry has recognized that shipping agent code at scale requires runtime verification, and it is moving that way fast. However, the scope of that verification remains limited for most teams.*

A consensus is forming in agentic development: To ship [code from agents](https://thenewstack.io/ai-agents-software-engineering/) at scale, you have to enable them to verify their code at runtime. Static verification, reading the diff and running unit tests against mocks, is not enough.

The constraint is knowing whether what an agent produced actually works, and that answer only exists once the code runs. So the industry is moving verification out of the human review queue and into the agent’s own loop, giving agents a place to run their work and check it before a person ever sees the change.

> “The industry has recognized that shipping agent code at scale requires runtime verification, and it is moving that way fast. However, the scope of that verification remains limited for most teams.”

Greptile, Cursor, Codex, and Devin all now run the code an agent writes rather than only reading it.

That is the right direction. Once [agents open pull requests](https://thenewstack.io/ai-generated-code-crisis/) faster than people can review them, review becomes the bottleneck. Stripe’s internal agents [ship more than 1,000 reviewed PRs per week](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents). An agent that can run its own code, read the failures, and fix them before handoff is what keeps that bottleneck from landing entirely on your senior engineers.

For cloud-native teams, this is not a nice-to-have. And it is where the approach most companies are adopting hits a ceiling. The common pattern gives each agent its own sandboxed environment, a snapshot that reproduces what a developer can run locally. For a self-contained application, that is enough.

For an agent working in a distributed system, it verifies one service against mocks and misses behavior that only appears when the change interacts with the rest of the system.

That behavior, integration, and the other system-level tests are where the expensive bugs live. The trend is right. The question is whether the runtime your agents verify against is the real system or a stand-in for it.

## The industry is converging on runtime

The clearest signal is that agent tools have stopped just reading the diff and started running it. Static analysis has a ceiling: It can reason about what code says, not what it does. A race condition that needs a real request, a regression that only appears after a page renders — none of it shows up in the text.

The trend is visible everywhere. Greptile [recently announced TREX](https://www.greptile.com/blog/trex-code-execution), a new feature that executes each change in a disposable sandboxed environment and returns logs, traces, and screenshots of what happened. [Cursor’s cloud agents](https://cursor.com/docs/cloud-agent) clone the repo into their own VM to build and test. [OpenAI’s Codex Cloud](https://openai.com/index/introducing-codex/) does the same. [Devin](https://devin.ai/) runs in a full environment with its own shell and test runner. Different products, one move: Give the agent a place to run its work and prove it before handoff.

Runtime verification is exactly the layer most agentic stacks are missing, and pushing it into the agent’s own loop is how review stays fast as volume climbs. The open question is the level of runtime fidelity it takes to actually call a change verified.

## Where it has to go further for cloud-native teams

The approach all these tools have taken is to give an agent roughly what a developer has at their desk: its own service, the dependencies it can start locally, and mocks standing in for everything else. That is a real and useful capability, and it is the correct direction.

For a cloud-native application built from many services, it covers less than half of it. The rest of the surface it misses is the part that matters most: How the change behaves relative to the rest of the system. A mock only returns the answer someone expected in advance. It can confirm an assumption but never catch a wrong one. And the expensive bugs in these systems are exactly the ones that break an assumption where two services meet:

* Contract drift between services
* A serialization mismatch at a boundary
* A retry or timeout policy that misbehaves two hops away

None of that shows up in a unit test or against a mock. It surfaces in integration tests, end-to-end tests, and the other system-level checks that only mean something when the change runs against the real services, real data, and real traffic around it.

The same goes for the non-functional behavior teams care about most: Performance and load regressions, resource contention, and runtime security issues surface only when the change runs inside a realistic system. That is the layer a sandboxed environment cannot reach.

The intuitive fix, cloning the whole system into every agent’s environment, does not hold up. Standing up dozens of stateful services with their data and config, fresh for each agent on every iteration, is impractical at the volume and speed with which agents generate code. And a copy is still a snapshot, not the live system.

![Diagram showing the extent of stand-ins for real dependencies in a sandbox model.](https://cdn.thenewstack.io/media/2026/06/030fe0c7-image2-1024x601.png)

## An architecture that reaches the whole system

The way through is to stop giving each agent its own copy of the system and instead let every agent run verification against one shared, production-like system with isolation.

The pattern is straightforward. A shared cluster runs all the real dependencies, the full set of services as they behave in production. To verify a change, you deploy only the modified service into that baseline and use request-level isolation to keep each agent’s traffic on its own path. The agent’s requests hit its version of the service and then flow through the underlying real services. Everyone else’s traffic stays on the baseline, untouched.

This gives the agent a realistic runtime in which its change runs alongside the live services, data, and policies it has to work with. Integration and system behavior become observable because the interactions are real rather than mocked.

It also scales to the way agents work. Because each change is just one service layered onto the running system rather than a private copy of everything, many agents can verify at once, cheaply, without colliding. The environment is lightweight and short-lived, and it runs on infrastructure the team already operates. This is the model we build at [Signadot](https://www.signadot.com/). Today, that means Kubernetes, though the same idea will carry over as the tooling matures.

![Diagrammatic representation of an architecture that reaches the whole system.](https://cdn.thenewstack.io/media/2026/06/3b921db6-image1-1024x677.png)

It fits the loop the agent tools already use. The agent writes, runs, reads the failure, and tries again, all before the pull request. What changes is the bar for a passing run. Not green against mocks the agent wrote to match its own assumptions, but correct against the real system those assumptions describe.

## The trend is right. The reach is the question.

Runtime verification is becoming a first-class part of how software ships, and that is the correct evolution. The teams furthest ahead already treat the agent’s job as write, prove, debug, repeat, not just write.

> “Not green against mocks the agent wrote to match its own assumptions, but correct against the real system those assumptions describe.”

The question for anyone running a [cloud-native system](https://thenewstack.io/introduction-to-cloud-native-computing/) is how far that proof reaches. An isolated per-agent environment verifies a change on its own, and for many changes, that is enough.

Proving a change is right when it has to work alongside everything around it is a different problem. It takes integration and system-level verification against a runtime that holds the rest of the system, not a stand-in for it.

The teams that get the most out of background agents will be the ones whose verification loop reaches the whole system, not just the service in front of them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)