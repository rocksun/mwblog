GitHub recently published [an update on availability](https://github.blog/news-insights/company-news/an-update-on-github-availability/) following a couple of rough incidents in April. The article opened with a sentence that every engineering leader should see:

*“We started executing our plan to increase GitHub’s capacity by 10X in October 2025 with a goal of substantially improving reliability and failover. By February 2026, it was clear that we needed to design for a future that requires 30X today’s scale.” –* Vlad Fedorov, GitHub CTO

Software is being produced at a volume without precedent, and the inflection point coincides exactly with coding agents moving from early prototypes to default tools within engineering organizations.

When the CTO of GitHub, running some of the most battle-tested developer infrastructure on the planet, says that a 10x scaling plan already in flight is insufficient and has to be torn up for a 30x one, that is not a routine capacity announcement. It is a public admission that the underlying assumptions about how software is produced have shifted faster than even GitHub anticipated, and the rest of us are downstream of those same assumptions.

The long-predicted agent code explosion is here, and incremental scaling is not the answer. Software is now being produced at a volume that the existing software development lifecycle (SDLC) was never designed to absorb.

## Volume becomes a problem when you can’t convert it into throughput

Volume is not inherently a problem. A 30x increase in code production could, in principle, translate into a 30x increase in shipped features. The reason it does not is that the SDLC has never converted raw code volume into shipped throughput at anywhere near a 1:1 ratio. The conversion has always been lossy, and the point of loss is validation.

This was already true before agents arrived. Anyone who has built software at scale knows the symptoms: test suites that take an hour, staging environments that are perpetually broken or contended, integration bugs that nobody catches until a release candidate, review queues that pile up because reviewers are the only people who can actually tell whether a change is safe. Validation is the slowest, most human-dependent, most error-prone part of the pipeline, and it sits between the code being written and the code being shipped.

This is made much more difficult in [cloud-native architectures](https://thenewstack.io/introduction-to-cloud-native-computing/). A modern application is a graph of services owned by different teams, each with its own state, dependencies, and deployment cadence. A change to one service can ripple through half a dozen others, and the things that actually break, contract drift, race conditions, multi-tenancy edge cases, and performance under load are runtime properties that do not reveal themselves in source code or unit tests.

The reason this has to be rethought, not just scaled, is that the cost of validation compounds. A bug caught in the inner loop, where the developer or agent is iterating, costs almost nothing to fix. The same bug caught in CI costs a full build cycle. Caught in staging, it costs a deploy and a queue slot. Caught in production, it costs an incident, a rollback, and a revert PR that itself has to go through the same pipeline.

At human authoring speeds, the SDLC absorbs some of this inefficiency because volume is bounded by the number of engineers. At agent authoring speeds and scale, it stops being absorbable and starts compounding into an ever-growing backlog.

This is why the answer is not more CI capacity, more staging environments, or more reviewers. Those are tactical responses to a structural shift. The structural answer is to push validation as far left as possible, into the inner loop where the agent is producing the code. Efficiencies gained there compound downstream. Inefficiencies left there compound just as ruthlessly in the other direction.

> “The structural answer is to push validation as far left as possible, into the inner loop where the agent is producing the code.”

![Bar chart showing the growing costs of a defect for each stage](https://cdn.thenewstack.io/media/2026/05/1cfa3fa8-1.png)

## The closed loop is the missing piece

There is a reason this shift has not already happened, even though the case for moving validation left has been around as long as the SDLC has. Today’s coding agents are only half of a working system. They can write code at unprecedented speed, but they cannot tell whether the code they wrote behaves correctly when it meets the rest of a distributed system. Compile-clean is not correct. Unit tests pass for the things unit tests are scoped to. Everything beyond that, the entire interaction surface between services, is outside what the agent can verify on its own.

> “Today’s coding agents are only half of a working system. They can write code at unprecedented speed, but they cannot tell whether the code they wrote behaves correctly when it meets the rest of a distributed system.”

So the agent does the only thing it can. It declares the change ready and pushes it downstream, where the work of figuring out whether it actually works gets picked up by a human reviewer, an integration test, a staging deploy, or a production incident. The compounding cost of validation kicks in, and the inner-loop opportunity is lost.

The fix is to close the loop at the source. An agent that can validate its own work against the real system, in the inner loop, before the change ever becomes a pull request, removes the burden from everything downstream. An agent that cannot do that adds load to a pipeline that is already past its limits.

## What closing the loop actually requires

The technical challenge here is real. As established, the validation surface for cloud-native systems lives in the interactions between services, not in the source code itself. Closing the loop means giving the agent a way to autonomously reach that surface.

This is why so many existing approaches to agent validation come up short. Mocks fake the behavior of dependencies and miss the real ones. Unit tests cover individual functions and miss the integration surface. A green CI run tells you that the [things tested](https://thenewstack.io/stop-running-tests-with-your-ci-cd-tool/) passed, which is not the same as saying the change is correct.

For an agent to actually close its loop, it needs to run its candidate change against a real version of the system, with real services, real dependencies, and real traffic patterns. And it needs to do that fast enough and cheaply enough that the agent can iterate, observe what broke, and try again, without involving a human, without contending for a shared environment, and at the speed and scale that agents demand.

An agent that can do that, validating broadly across integration, contracts, performance, and failure modes before it opens a pull request, takes work out of the downstream pipeline rather than adding to it. The PRs that arrive at CI have already passed runtime validation against the real system. The reviewer is no longer the first validation layer. They are a confirmation step on a change that has already been shown to work.

![Infographic showing the downstream pipeline for open loop and closed loop](https://cdn.thenewstack.io/media/2026/05/8fbf9d84-2-1024x441.png)

## The strategic question for every engineering org

The 30x curve will keep climbing, and the agents producing the code will keep getting better at the writing part. On its own, that makes the validation gap worse, not better. A more capable agent that still cannot validate its own output simply produces more unvalidated output, faster.

> “A more capable agent that still cannot validate its own output simply produces more unvalidated output, faster.”

The strategic question for engineering leaders is whether the agents in their organization are operating in a closed or open loop. An [agent that can write code](https://thenewstack.io/ai-agents-software-engineering/) and validate it against the full system in the inner loop is a force multiplier on engineering throughput. An agent that can only write code that passes basic tests is a force multiplier on the validation bottlenecks that were already your biggest constraints.

This is what we are building toward at [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content), with lightweight ephemeral environments that give agents production-like signals in the inner loop. The broader point holds regardless of which approach an organization adopts: closing the loop is the capability that changes the economics of agent-generated code.

The agent code explosion is here. The question is whether your agents are closing the loop, or whether your pipeline is being asked to close it for them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)