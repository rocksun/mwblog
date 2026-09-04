**I have been waiting for agent-generated code** to show up in public infrastructure data rather than in vendor benchmarks. In August, it did. GitHub now handles [2.9 billion commits a month and says it cannot keep up](https://thenewstack.io/github-2-9b-monthly-commits/). Monthly commit volume [more than doubled in four months](https://www.engadget.com/2241272/github-says-commits-have-doubled-in-the-last-four-months/), from 1.4 billion in April to 2.9 billion in August.

The growth broke the platform. On August 17, GitHub went down for [7 hours and 47 minutes](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) after a core infrastructure component in its Central US data center failed to scale with traffic. The postmortem from CTO Vladimir Fedorov did not hedge: If you were trying to ship software that day, GitHub let you down. The remediation is what a hyperscaler does when demand outruns supply. More than 3 million new CPU cores, 120 petabytes of high-speed storage, and an accelerated migration to Azure, which [now serves 58% of platform load](https://www.theregister.com/devops/2026/08/21/we-let-you-down-github-pledges-to-scale-up-before-developers-give-up/5291031).

Most coverage treated this as a capacity story, and for GitHub it is one. The number that should worry you is one the postmortem never touches. Every one of those 2.9 billion commits carried an implicit claim that the change works. Almost nothing in the system that produced, transported, and merged them checked that claim against a running system.

> “Code generation has become machine-paced, and its volume curve is exponential. Verification is still human-paced, and its capacity curve is close to flat.”

That is the warning inside GitHub’s data. Code generation has become machine-paced, and its volume curve is exponential. Verification, the work of proving a change does what was intended without breaking what already worked, is still human-paced, and its capacity curve is close to flat. The distance between those two curves is the defining infrastructure problem of the next three years.

## The commit curve is the first public trace of machine-paced development

GitHub’s telemetry is a proxy for your own organization: it aggregates what thousands of engineering teams are doing at once. Alongside the commit number, the postmortem reports about 130 million merged pull requests and 24 million new repositories a month. Engadget’s reporting notes that GitHub attributes the surge to AI-generated code.

The shape of the curve matters more than its height. Commit volume grew for years at roughly the same rate as the developer population, because commits tracked people. Then it doubled in four months, because it stopped tracking people. A developer who [runs three coding agent](https://thenewstack.io/github-mcp-security-scanning/) sessions in parallel produces commits at a rate no hiring plan ever predicted.

> “A developer who runs three coding agent sessions in parallel produces commits at a rate no hiring plan ever predicted.”

Your internal dashboards almost certainly show the same shape in miniature: pull request counts climbing quarter over quarter, more commits per engineer, more branches open at once. The public number matters because it proves your curve is not a local anomaly. This is what development looks like when generation is no longer the scarce step.

## GitHub’s bottleneck is capacity. Yours is confidence

GitHub’s problem, for all its severity, has a known fix: When traffic outgrows infrastructure, you add infrastructure. Cores, disks, and data centers scale with money, and Microsoft has plenty.

The problem on your side of the platform does not respond to money the same way. A commit is not traffic. It is a claim about behavior: This change does what its description says and breaks nothing downstream. In a distributed, cloud-native system, checking that claim means running the change against the services, data, and traffic it will meet after merge.

The pipeline in front of that check keeps getting faster. AI code review tools triage diffs before a human looks at them, CI has learned test selection and caching, and static analysis catches more than it used to. Those are real gains, and none of them runs the change. The step that verifies behavior, integration, and end-to-end tests against a live system still funnels through a shared staging environment or waits on a full copy of the stack, which takes too long and costs too much to stand up for each change.

That step has a hard ceiling. Staging is one environment per organization, so it functions as a queue. Full-stack duplicates are expensive enough that teams ration them. Neither doubles in four months because you approved a budget. Generation now scales like GitHub. Verification still moves one change at a time.

![Workflow diagrams comparing a single shared queue vs one environment per change.](https://cdn.thenewstack.io/media/2026/08/6bd721a6-image-1024x546.png)

## Verification was sized for human pace, and agents broke the sizing

None of this is new. Large engineering organizations were complaining about staging contention and review backlogs years before coding agents existed. The apparatus was built when code arrived at the pace humans type, and at that pace its costs were a tax teams could manage: an occasional staging conflict, a review queue that cleared by Friday. Deferring expensive full-fidelity testing to the end of the pipeline was a reasonable trade while changes were scarce.

Agents do not introduce the bottleneck. They multiply it past the point where the old coping strategies work, and they bring it to smaller teams. Throughput that used to strain a 500-engineer platform now appears on a 50-engineer team running agents in parallel. The assumption under all of those design decisions, that code is the scarce input, is gone, and the checking machinery built on it has not moved. The two curves that used to track each other roughly have come apart. GitHub’s chart is the aggregate picture of that separation.

![Chart showing monthly commits vs verification capacity](https://cdn.thenewstack.io/media/2026/08/e737df17-image-1024x609.png)

## The gap between the curves fills with unverified merges

Teams respond to the widening gap in a few ways. The first is to make review faster. AI code review tools sit in front of human reviewers, catch real defects in the diff, and keep improving. They also have a limit: A reviewer, human or model, is reasoning about code they have not run, and a diff cannot tell you whether the change holds up against its real dependencies.

The second is to throttle the agents, capping the amount of generated work that enters the pipeline. That protects the verification queue by returning most of the throughput the agents were designed to deliver.

The third is to merge anyway and absorb downstream failures. Changes that were never run against a real system land in main at the rate commits arrive, and the cost surfaces later as broken staging environments and lengthy debugging sessions. Or worse, production incidents and rollbacks.

The August 17 outage is a preview of how that ends. The root cause was not a bad change. It was a component that everyone depended on, and nobody had scaled, failing on the day traffic finally exceeded its design. In most delivery systems, verification is that component.

## Verification has to run on the same curve as generation

The structural fix is to make verification match the shape of generation: parallel and per-change. For a single application, this is nearly solved: an agent runs the app on a laptop or in a CI container and checks whether the change works. The hard case is the cloud-native one, where the change’s behavior only exists when interacting with other services, databases, and queues. Both familiar options fail at agent volume: A shared staging environment serializes everything into a queue, and duplicating the full stack for each change is too costly and too time-consuming.

There is a third shape. Keep one shared environment running the stable version of every service, and for each change, deploy only the services that the change touched. Test traffic carries the change’s routing key, so at each hop, a request for that change reaches the changed version while every other request flows through the stable one. Each change gets isolation where it matters, at the services it modified, and shares everything else: the same cluster, the same data, the same downstream dependencies.

![Workflow diagram showing request routing in the shared environment](https://cdn.thenewstack.io/media/2026/08/2aa97818-image-1024x443.png)

That shape changes the economics and the actor. Verifying one more change costs one extra deployment, not another copy of the stack, so hundreds of changes can be checked in parallel on the cluster you already run.

Because an environment appears in seconds, an agent can use one inside its loop: open a change, run functional checks against real upstream and downstream services, read the failures, and iterate until they pass. The pull request that reaches a human arrives already exercised against the real system, and review time goes to intent and design.

## Match the curves or lose the generation gains

[GitHub’s 2.9 billion commits](https://thenewstack.io/qwen-autonomous-coding-audit/) quantify a shift that every engineering organization is living through on a smaller scale. Generation is now effectively free and unlimited, so it is no longer the source of advantage.

> “The teams pulling ahead are not the ones producing the most commits. They are the ones whose verification capacity rises with their generation capacity.”

The teams pulling ahead are not the ones producing the most commits. They are the ones whose verification capacity rises with their generation capacity, so more generated [code becomes more shipped](https://thenewstack.io/snyk-pentesting-ai-agents-security/) code, rather than a longer review queue, a deeper staging backlog, and a bigger incident bill. Ask what happens to your pipeline when commit volume doubles in four months, because that is no longer a hypothetical. It is the gap we work on at [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q3_26_sponsored_content), and it is worth closing before the curve doubles again.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)