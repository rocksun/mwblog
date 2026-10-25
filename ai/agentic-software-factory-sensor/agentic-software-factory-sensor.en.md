A gap has long existed between the shipping velocity of the best engineering teams and the rest of the bell curve. For most of the industry’s history, it was a multiple measured in deploys per week. Agents are turning that multiple into an exponent, and the dividing line is no longer tooling or talent. It is whether a team has rebuilt its delivery system into what the industry now calls a “software factory,” a largely autonomous system where intent goes in, agents plan, write, test, and ship the changes. People own the specifications and the gates.

Anthropic put a number on the gap this month. [In May the company merged around 2,500 code changes a day, and by September it merged more than 30,000](https://www.anthropic.com/engineering/redesigning-source-control). Coding stopped being the bottleneck, they write. The bottleneck became the developer infrastructure built for human scale, and they now ask what [continuous integration](https://thenewstack.io/ci-bottleneck-agent-verification/) (CI) even means when thousands of changes merge while the tests are still running.

> “Agents are turning that multiple into an exponent, and the dividing line is no longer tooling or talent. It is whether a team has rebuilt its delivery system into what the industry now calls a ‘software factory.'”

Getting there means rethinking the delivery lifecycle around one question: how does the factory know a change works before the next thousand land on top of it? Read as a control loop, intent is the setpoint, agents are the controller, and verification is the sensor. A controller that outruns its sensor does not go faster. It retries on stale information and ships the failures the sensor would have caught. The sensor decides how much of the factory can run on its own.

## What an agentic software factory is made of

Addy Osmani’s definition is the one most people use: a software factory is [many harnessed loops running at once, fed by a work queue and drained through a review gate into production](https://addyosmani.com/blog/software-factories/), with humans owning the whole thing from above.

Intent is the specs, tickets, and scenarios that say what done means. A queue holds the backlog. A harness constrains each agent with tools, context, and rules. [Generation is the coding agents](https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/). Verification is the tests, scenario runs, and runtime checks that report whether a change works before it merges. A review gate is where a person or a policy lets a change merge. Integration and deploy move it to production, and production feedback carries telemetry and incidents back into the queue.

## Agents changed the controller, and the sensor has to change with it

Agents change the lifecycle in two places. They add a generation step, so later stages receive changes at the rate agents write them, and they turn verification from a stage people wait at into a service agents call from inside their own loop.

> “A controller that outruns its sensor does not go faster. It retries on stale information and ships the failures the sensor would have caught.”

Control engineers mount the sensor on the running system for a reason: it is the only reading that reflects what the system does. The traditional lifecycle got by with cheaper stand-ins at every stage, unit tests at commit, integration tests in CI, a shared staging environment before release and telemetry after, because reading the real system for every change was slow and expensive. Each stage traded fidelity for speed, and the trade held while people set the pace.

A developer who spent two days on a change barely noticed that staging took four hours to report. An agent that writes the change in four minutes either waits, which wastes the speed, or keeps going with whatever it can see. What it can see depends on the environments and tests it can access, and for many teams that is unit tests and mocks.

Dan Shapiro’s five levels of AI coding, read by what verifies the code at each one, are a ladder of sensors. At level 3, the agent writes, and [you review diffs all day, which is where almost everyone tops out](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/). At level 4, the tests are the sensor, and whether that is safe depends on what they run against.

StrongDM’s [two rules](https://factory.strongdm.ai/) — that code must not be written by humans and must not be reviewed by humans — certainly received attention. What made them workable was its Digital Twin Universe, behavioral clones of its third-party dependencies that agents run thousands of scenarios against. That is the line between adding agents to a pipeline and running a factory. The rules are free to copy, but the sensor is the expensive part, and it is what gives people their place: on the intent and the slow loops like architecture, not as the per-change check for a controller a hundred times faster than they read.

![Flow diagram of the software factory control loop.](https://cdn.thenewstack.io/media/2026/10/e7103469-image-1024x546.png)

## A sensor has three properties, and the factory needs all three

### Latency

Latency is how long the sensor takes to report, and delay destabilizes the loop. Every action between a change and its signal rests on a state that no longer exists, so the agent retries on an unverified change and other agents build on that. Track time to signal: the minutes from a change being ready to a verified result in a production-like environment.

### Fidelity

Fidelity is how closely the reading matches the real system, and it matters more than latency, because the loop trusts a biased sensor. Unit tests and mocks report what a change does against a model of its dependencies, and agents optimize for whatever the sensor rewards. StrongDM saw its agents return true to pass narrow tests, so it moved its scenarios outside the codebase as a holdout set. The number to track is escape rate, the share of failures found after merge.

### Bandwidth

Bandwidth is how many readings the sensor can take at once, and it is the property agents strain first. Shared staging takes one reading at a time, so with fifty agents’ readings queued or mixed, failures stop being attributable to a change. The number is concurrent verification capacity.

## Autonomy follows the sensor, so measure the sensor

A factory can run as much autonomy as its sensor can verify and no more, which Osmani calls back pressure. With only compilers and unit tests, the agent proposes, and a person verifies everything. With per-change checks in a production-like environment, the agent iterates in a loop until the change is verified, and a person reviews the intent and evidence. Anthropic’s engineers still review every major change to their codebase, but they examine evidence that the change does what was intended rather than reading every line. With held-out scenarios and fast rollback, defined classes of change can merge without review.

> “A factory can run as much autonomy as its sensor can verify and no more. The sensor, not the model, sets the level.”

The sensor, not the model, sets the level. A better controller on a biased sensor reaches the wrong answer faster, and reviewing every change is also a sensor, with latency in hours and bandwidth of a few changes per reviewer per day.

So measure the sensor, not the agents’ effort. Pull requests and tokens per engineer count how hard the agents work. Time to signal, escape rate, and concurrent verification capacity tell you which property is weak, and change failure rate and rework rate tell you whether the loop is stable. Start with the first three.

## Cloud-native systems make the sensor harder

In a distributed system, behavior breaks across service boundaries. A field renamed in one service that another team’s service still reads. A consumer that assumes an ordering its topic does not guarantee. Each change is correct at its own boundary and wrong in combination, so a faithful sensor has to include the real services around a change. That is what makes all three properties hard to get at once: fidelity means real neighbors, and latency and bandwidth mean an environment with those neighbors for every change, in minutes. Most teams get two of the three.

Verifying a batch of pull requests on a shared environment gets fidelity and nothing else. The environment is real, but it takes one reading at a time and reports hours after the change, outside any agent’s loop. Testing several changes in one run to save time makes a failure impossible to attribute, so the agent cannot act on a red result.

Duplicating the full stack, or a large part of it, per change improves fidelity and isolation but adds latency and bandwidth costs. Provisioning takes tens of minutes, far longer than an agent’s attempt, and cost grows with every concurrent agent, so teams ration it to the changes that justify it. Behavioral twins work for third-party services with stable public behavior. Still, for 150 internal services, a clone is a second implementation that drifts while the real services already run in a cluster.

At scale, a factory needs a way to give each agent, and each change, a realistic environment where the real services answer its calls, without the cost or latency of duplicating the stack. That sensor satisfies all three properties, and it is the model we built [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=paid_sponsorship&utm_campaign=q4_26_sponsored_content&utm_content=software-factory) to enable.

![A diagram showing the various software factory sensor approaches.](https://cdn.thenewstack.io/media/2026/10/be35d653-image-1024x512.png)

## Rethinking the SDLC for agents starts with the sensor

The gap between the teams merging 30,000 changes a day and the rest is not the agents, which everyone now has. It is a delivery system rebuilt around a sensor that reports in minutes, matches the real system, and runs for every change at once.

On [cloud-native systems](https://thenewstack.io/agent-loops-cloud-native-verification/), that sensor is the hardest part to build, and it decides whether more agents ship more software or only break more of it. For the full architecture, see our [complete guide to software factories for cloud-native systems](https://www.signadot.com/software-factory/?utm_source=tns&utm_medium=paid_sponsorship&utm_campaign=q4_26_sponsored_content&utm_content=software-factory).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)