**Three posts landed in September** that I think engineering leaders should read together.

Anthropic’s engineering team wrote that their [continuous integration (CI) job volume grew 25x in six months](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic). Their engineers now ship about 8x as much code per quarter as they did from 2021 to 2025. The fix they shipped was test impact analysis: run only the tests a change could affect.

A week later, Linear published a post titled [AI coding has made CI a bottleneck](https://linear.app/now/ci-bottleneck-reworked). Their test suite has nearly quadrupled since January, and agents now write most of their tests. They reworked the pipeline end to end to keep up.

Then Depot’s CEO wrote that [CI is changing](https://depot.dev/blog/ci-is-changing), and that the future is “giving agents a way to validate code and maintain trust as they work.”

Anthropic and Linear do not sell CI tooling. They are reporting what happened to their own pipelines, which is what makes it worth paying attention to. Here is my read: all three are right about the problem, and two of them are fixing the wrong layer.

## **How CI became the bottleneck**

For twenty years, CI was sized for human output. A developer opened a few pull requests (PRs) a week, and the pipeline ran after each one. If it took 20 minutes, nobody cared much, because the developer was already on the next task.

Agents broke that arithmetic in two ways. First, volume. When one engineer runs several agents in parallel, PR count goes up by a multiple, not a percentage. Anthropic’s 25x number is not an outlier. Blacksmith, which sells CI runners, says [the number of CI jobs it runs has grown between 5% and 10% week over week](https://www.prnewswire.com/news-releases/blacksmith-raises-45m-series-b-from-peak-xv-partners-as-ai-generated-code-drives-demand-for-faster-code-validation-302849104.html).

> The agent is fast, and the loop around it is slow.

Second, placement. CI runs after the PR exists. An agent that writes code, opens a PR, and waits 20 minutes for a red check has lost its working context by the time the result comes back. Every failure costs a full round trip. The agent is fast, and the loop around it is slow.

So the industry did the obvious thing and made CI faster. Faster runners, smarter test selection, bigger caches, pipelines that agents can call before commit. All of it helps, and all of it is necessary. All of it also leaves one assumption untouched: that what you’re verifying is a repository.

## **What a green pipeline does not tell you**

For a standalone application, a repository is the system. Run the tests, and you know most of what you need to know.

For a cloud-native system, a repository is one service out of forty. The tests in that repo exercise that service, and they mock everything else. A change can pass every unit test, pass CI in record time, pass a sandbox built from the branch, and still break the first real request that crosses a service boundary.

The failures that hurt in distributed systems live in the seams. A field renamed in a response that a downstream consumer still reads. A timeout tightened in one service that cascades into retries somewhere else. A schema change that works against the test fixture and locks a table in staging. A new endpoint that behaves correctly when the test harness calls it and incorrectly when the service that depends on it calls it.

Nothing in the CI pipeline, fast or slow, sees any of that. It cannot, because it is looking at a repo.

This is why I think the September posts are a symptom, not a diagnosis. CI got slow because verification moved from a human gate to an automated one without anyone asking what the automated gate checks. Making the gate faster does not change what it checks.

> Faster code, same verification, more breakage. That is the gap.

DevOps Research and Assessment (DORA) found something that should worry you: [higher AI adoption is associated with increases in both software delivery throughput and software delivery instability](https://dora.dev/insights/balancing-ai-tensions/). Faster code, same verification, more breakage. That is the gap.

## **The verification loop has to move**

Cursor made a point in February that is only becoming more relevant. Their agents run in cloud sandboxes, each with its own virtual machine, and more than 30% of the PRs Cursor merges now come from agents working that way. Their stated reason: [“Without the ability to use the software they are creating, agents hit a ceiling.”](https://cursor.com/blog/agent-computer-use)

That is the right instinct. The agent has to run the code, not only write it. Every serious coding agent now does some version of this. GitHub’s Copilot cloud agent runs tests in an ephemeral environment powered by GitHub Actions. Codex runs a setup script and resumes cached containers. Devin boots from environment blueprints. Greptile’s TREX runs the branch and attaches logs and screenshots to the PR.

But look at what each of those sandboxes contains: the repo, the branch, and whatever the setup script could install. None of them include the other 39 services, the real message queue, or the database with production-shaped data.

> So the loop closes, but it closes around the wrong thing.

So the loop closes, but it closes around the wrong thing. The agent verifies its change against a copy of its own code. Then the change goes to CI, which verifies it against the same copy, faster. Then it merges into staging, and that is the first moment anything checks whether it works with the rest of the system.

For distributed systems, verification before the PR has to be against the system, not the repo. That is the shift. It is not faster feedback on the same question. It is a different question, asked earlier.

![](https://cdn.thenewstack.io/media/2026/10/00644982-three-validation-loops.svg)





*Click to enlarge image.*

## **Why this looks expensive and is not**

The reflexive objection is cost. If every agent needs the whole system to verify against, and one engineer is running five agents, you need five staging environments per engineer. Nobody can afford that, and nobody should try.

The answer is the same one the industry used for compute two decades ago. You do not give every workload its own machine. You multiplex.

A single Kubernetes cluster can run one shared stable version of every service and host thousands of lightweight test environments on top of it. Each test environment deploys only the changed service. Requests tagged for that environment pass through the modified service, and every other hop resolves to the shared stable versions. The modified service talks to real dependencies, and those dependencies do not know anything changed.

A test environment costs roughly the price of one pod, and it comes up in seconds. Fifty agents working in parallel share one stable environment instead of cloning it fifty times. That is what makes system-level verification inside the agent loop affordable in the first place.

![](https://cdn.thenewstack.io/media/2026/10/10a51f46-clone-vs-multiplex.svg)





*Click to enlarge image.*

## **Agents need governed verification, not only environments**

Cheap, fast environments are not the whole answer. An agent also needs a structured way to use them: send this request, capture that log, assert this contract held, report the result. Left to improvise, each agent invents its own checks, and no two runs are comparable.

The model that works is one where the platform team writes those steps once, as a sequence of approved actions that exercises a change against the live system and records what happened. Agents invoke them through the skills and hooks that Claude Code, Cursor, and similar tools already support, so verification runs as part of the loop rather than after it. The governance matters as much as the steps, because platform teams need to know an agent cannot do something unsafe in a shared cluster.

The output matters too. A record showing which requests were sent, which services were touched, and which contracts were held is an artifact the next layer can read. Review tools and merge gates can see that a change was exercised against live services before a human looks at it, and CI becomes a confirmation step instead of the first place cross-service breakage shows up.

## **Verification belongs inside the agent’s loop**

I expect the CI vendors to keep getting faster, and I expect coding agents to keep getting better at running code in sandboxes. Both are good for everyone, and neither closes the gap between a repo and a system. The teams that come out ahead will stop asking how fast the pipeline can confirm that a repo still passes its own tests and start asking how early an agent can prove that a change works with everything around it. That question gets answered in one place: inside the agent’s loop, against the real system, before the PR. We built [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=paid_sponsorship&utm_campaign=q4_26_sponsored_content&utm_content=ci-bottleneck-wrong-fix) to make that check cheap enough to run on every change, with the governed.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)