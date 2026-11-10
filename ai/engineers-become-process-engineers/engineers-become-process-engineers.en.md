For most of software’s history, the scarce resource was people who could write code. Every process the industry built assumed it. Sprints, code review, staging, and release trains were all designed around humans doing the work by hand.

That assumption is gone. By September, [more than 40% of pull requests on GitHub started with an agent’s first draft](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/), up from 17% in March. Work is moving to machines, but the process around it hasn’t caught up.

Agents made [generating code cheap](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/) and fast. For the most part, they have not yet had the same impact on shipping it. CircleCI’s 2026 delivery data showed [average daily workflow runs grew 59% year over year](https://circleci.com/blog/five-takeaways-2026-software-delivery-report), with the top 5% of teams up 97% and the bottom quartile showing no measurable increase. A study of one company that mandated doubling pull request output found that [load per reviewer doubled](https://arxiv.org/abs/2607.01904) and automated review overtook human review in coverage within months.

> “When work gets automated in any industry, the people don’t disappear. They stop doing the work and start designing the system the work runs through.”

When work gets automated in any industry, the people don’t disappear. Their job changes. They stop doing the work and start designing the system the work runs through. Software engineers are becoming process engineers, and what they build is a software factory.

## Three manufacturing lessons carry over to agents

Software is not a car plant. A factory builds the same product thousands of times, and software never ships the same change twice. But three ideas carry over, because they are about running a system where machines do the work.

The first is that people design the system, not the output. Ford’s Model T went from [12.5 hours per car to one every 93 minutes by 1914](https://www.thehenryford.org/collections/explore/articles/ford-methods-and-the-ford-shops), and the workers did not get eight times faster. Engineers redesigned the line.

Second, quality gets built in at every step. Sakichi Toyoda invented [a loom that stopped automatically when any thread broke](https://www.lean.org/lexicon-terms/jidoka/), so one operator could run many machines instead of watching one. Toyota built its production system around that idea, and W. Edwards Deming spent decades telling manufacturers to stop relying on end-of-line inspection.

The third is that the slowest step sets the pace. That was Eliyahu Goldratt’s point in “The Goal.” Speed up any step other than the bottleneck, and you pile up work in front of it. Agents sped up coding, and the pile is now in review and verification.

## A software factory is a network of agents

A software factory runs on many specialized agents, each good at one job, passing work to others across the lifecycle. A research agent turns usage data and customer calls into a brief, and a spec agent writes requirements with acceptance criteria. A coding agent writes the change, and a review agent reviews the change. A test agent runs the change and sends failures back, and a release agent rolls it out behind feature flags. A site reliability engineering (SRE) agent triages what breaks in production and opens the next piece of work.

Most handoffs in that loop are agent-to-agent, and that changes what a handoff is. Between humans, a handoff can be a Slack thread and some shared context. Between agents, it has to be a contract that states what gets passed, in what shape, and with what proof. A spec without acceptance criteria gives the coding agent nothing to aim at, and a change without test evidence gives the release agent nothing to trust.

> “A spec without acceptance criteria gives the coding agent nothing to aim at, and a change without test evidence gives the release agent nothing to trust.”

Agent-to-agent work also fails in new ways. Errors compound, because each agent builds on the last one’s output. Agents can agree too easily, or loop forever trading the same fix back and forth. A factory of agents needs what a factory of machines needs: checks between the stations, and someone who decides where those checks go.

![Diagram of an agent network](https://cdn.thenewstack.io/media/2026/11/24891d2a-image-1024x350.png)

## Software engineers become process engineers

That someone is the software engineer. The job moves from writing code to designing the system that writes, tests, and ships it. That is more technical, not less, because you are now responsible for how all the code gets made. The work comes down to four jobs, and the first is designing the flow: which agents exist, what each one owns, what runs in parallel, and what each handoff must contain.

The second is defining good. An agent can’t hit a target nobody wrote down. Specs, acceptance criteria, performance budgets, and API contracts used to live in people’s heads. Now they have to be explicit enough for a machine to check.

The third is improving the line. When an agent ships a bug, the useful question is not why the agent did that but why the line let it through. Every escaped defect is a process bug.

The fourth is placing the human gates. Humans belong where a mistake is expensive, and the call takes judgment. Line-by-line human review of every agent pull request is a craft-era habit, the factory equivalent of hand-inspecting every bolt.

> “When an agent ships a bug, the useful question is not why the agent did that but why the line let it through. Every escaped defect is a process bug.”

Agents write code and fix tests. A schema migration is costly to get wrong but cheap for a machine to check, so agents run it behind hard checks. User interface (UI) copy tastes but is cheap to change, so a human reviews it after it ships. What to build and where a security boundary sits gets a human gate.

![Diagram of the human gates, placed according to the amount of judgment needed and the cost of a mistake.](https://cdn.thenewstack.io/media/2026/11/efd4a054-image-1024x512.png)

## Quality gets built into every change, not inspected at the end

Most teams still run the old model of quality assurance. Changes pile up, then go through one inspection at the end: a shared staging environment and a human reviewer. That is a single test bench for the whole plant, and once agents multiply the number of changes, it becomes the [bottleneck Goldratt described](https://thenewstack.io/merge-gate-coding-agents/).

Toyoda’s loom freed the operator because it checked every thread as it ran and stopped the moment one broke. Agent-written code needs the same mechanism. In a working software factory, the test agent checks every change as it is made, the coding agent fixes what fails, and nothing moves until it passes.

That check only means something if it runs where the failure would show up. Mocks don’t count, because they tell you a change works in a world that doesn’t exist. They were a stopgap that made sense when the pace of change was slow and standing up a production-like environment for every change was hard.

So, each change gets its own environment that behaves like production, with the services, databases, and APIs it will meet after release. A human only sees the change if it hits a gate, and by then it already works, with the evidence attached.

That model needs a test station for every change, cheap enough to use on every attempt. In practice, that means an environment that comes up in seconds, deploys only what the change touched and shares everything else so that you can verify the change end to end before merge.

![Diagram comparing one inspection at the end vs. every change being verified on its own.](https://cdn.thenewstack.io/media/2026/11/47fd00eb-image-1024x606.png)

## Guardrails belong in the line, not in the prompt

Verification catches mistakes. Guardrails stop the ones that would cost too much to catch late. Assume agents will do anything the line allows, and design the line so that everything it allows is safe.

Manufacturing calls this error-proofing. You don’t put up a sign telling workers to insert the part the right way. You build a fixture that fits only one way. For agents, an instruction in a prompt is a sign on the wall, and a permission boundary is a fixture.

So each agent holds only the access its station needs, and the coding agent never holds production credentials. Every run is isolated, so one agent’s test can’t corrupt another’s. Required checks are enforced, every release can roll back on its own, and when a check can’t run, the change stops.

A line that quietly skips a broken inspection is worse than no inspection, because everyone believes it’s working. Agent-to-agent work adds one more rule: trust doesn’t pass down the chain. A review agent approving a change shouldn’t widen what the release agent can do.

## Judgment stays human, and it becomes most of the job

Factories didn’t get rid of engineers. They created industrial engineering. You can’t design a line for work you don’t understand, so the best factory builders will be engineers who know what good code, good tests, and a safe rollout look like from doing it by hand.

Some work stays off the line. The first version of something new, a strange production bug, and a design nobody has tried are bench work. They stay hands-on until they are understood well enough to standardize.

Some decisions never move to a machine: what’s worth building, what a customer means rather than what they said, when to trade speed for risk and who answers for what ships. Those were always the hard part of the job. Now they’re most of it.

## The best process wins, not the best model

Agents made code cheap, and every team can reach for the same models. What separates the teams pulling ahead is the line they build around those agents, with contracts between stations, human gates where judgment matters, and [verification on every change](https://thenewstack.io/ci-bottleneck-agent-verification/). Designing that line is now the software engineer’s job. We built [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q4_26_sponsored_content) to give every change its own test station, and it is a practical place to start building yours.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)