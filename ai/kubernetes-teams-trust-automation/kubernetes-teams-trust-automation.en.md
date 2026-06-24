Kubernetes teams automate deployments without thinking about it. CI/CD pipelines fire dozens of times a day, autoscaling adjusts replicas in the background, rollback is muscle memory. But there is one category of automation where that confidence vanishes: letting a system change [CPU and memory requests](https://thenewstack.io/stop-setting-cpu-and-memory-requests-in-kubernetes/) on a running workload without a human reviewing it first.

And as AI inference lands on Kubernetes at scale, that hesitation is becoming hard to ignore, and increasingly expensive.

## **Why teams trust automation for change but not for constraint**

We surveyed [321 Kubernetes practitioners at enterprise organizations](https://www.cloudbolt.io/industry-research/cii-kubernetes-automation-trust-gap/) earlier this year. The headline finding is one most practitioners will recognize immediately: 82% report high or complete trust in automated delivery controls. But 71% still require human review before applying resource optimization recommendations. Only 27% allow CPU and memory changes to be auto-applied, even within guardrails.

> “Deploying code feels additive… rightsizing feels subtractive because you are removing safety margin from a running service, and the failure mode is fundamentally different.”

Those numbers describe a specific asymmetry. The same engineers who deploy to production dozens of times a day without hesitation slow down the moment automation wants to adjust resource allocation. And the survey data make it clear why. Deploying code feels additive. You are shipping new value, the rollback path is well understood, and if something breaks you usually see it right away. Meanwhile, rightsizing feels subtractive because you are removing safety margin from a running service, and the failure mode is fundamentally different.

As one practitioner in the survey put it: “Automated right-sizing carries a unique risk because it directly impacts the underlying stability of the application runtime. Unlike a code deployment that follows a tested path, resource changes alter the invisible contract between the workload and the scheduler.”

When you change resource requests, you change how Kubernetes schedules, prioritizes, and allocates resources. Those effects are not visible the way a code change is. You can’t trace them through a deployment pipeline. And you might not discover that something went wrong until two weeks later, when a traffic spike hits a threshold that didn’t exist at the old values. By that point, three other things have changed too, and proving causation is nearly impossible. The people responsible for those workloads are the same people who get paged at 2 a.m., and they know this.

## **Why AI workloads raise the stakes**

That trust gap existed before inference workloads showed up. What’s changed is the cost of not closing it.

For a long time, teams could absorb the cost of manual oversight. They knew their workloads, had intuition for where the safe boundaries were, and the inefficiency of over-provisioning was a price worth paying for stability. GPU-accelerated inference workloads change that math. GPU compute is significantly more expensive per hour than CPU. The cost of over-provisioning is no longer a rounding error you can absorb quietly. And the workload behavior is less familiar, as inference jobs are bursty in ways teams haven’t built intuition for, traffic patterns shift as models are updated and usage changes, and the resource dimensions involved differ from what teams have spent years learning to tune.

That unfamiliarity compounds with scale. Rightsizing isn’t a one-lever problem the way horizontal scaling is. It involves, at minimum, CPU and memory requests and potentially limits for both, with four dimensions per workload, multiplied across hundreds or thousands of workloads per cluster. The survey [data indicates that manual optimization breaks](https://thenewstack.io/breaking-data-team-silos-is-the-key-to-getting-ai-to-production/) down at around 250 changes a day. Inference workloads push teams past that threshold faster than anything they’ve managed before, because the resource decisions are more frequent and the cost of getting them wrong is higher.

The economic case for automated rightsizing has never been stronger. The organization’s willingness to delegate hasn’t caught up because teams are being asked to trust automation with workloads they don’t yet have a track record with.

## **What the survey says about closing the gap**

When we asked practitioners what would actually increase their trust in optimization automation, 48% said visibility and transparency into how decisions are made, 25% wanted proven guardrails, and 23% needed instant rollback.

Nobody asked for full manual control and very few asked for blind autonomy. What they described is [automation that earns trust in stages](https://www.forbes.com/councils/forbestechcouncil/2026/05/12/the-speed-of-trust-in-automation-why-autonomous-systems-fail-without-it/), and that’s consistent with how the teams furthest along in their automation journey actually got there. They didn’t start with production. They started with a single namespace in a dev environment, observed the system’s behavior, compared recommendations with outcomes, and gradually expanded the scope. Different environments remained at different levels of automation maturity simultaneously, and that was intentional. Production carried more scrutiny than dev.

CI/CD followed the same curve, and the timeline is easy to forget. Most organizations took years to get from running their first automated pipeline to trusting it with production deploys without manual approval on every commit. Kubernetes resource automation is earlier in that same process, and AI workloads are extending the timeline because teams are building trust from scratch with a workload category that doesn’t yet have a track record.

## **Why automation design matters as much as capability**

Some automation architectures deliver meaningful value only with full delegation. The system needs complete control to function the way it was designed to. That’s a form of forced autonomy, and it creates an adoption problem because it asks for exactly the level of trust that most organizations haven’t built yet. Force generally doesn’t work. Teams that feel pushed into a level of delegation they aren’t comfortable with tend to pull back entirely after the first incident.

The alternative is what I’d describe as adaptive autonomy: designing the system to work at every stage of the trust curve. A team still evaluating gets useful recommendations in read-only mode. A team ready to act but wanting boundaries can run guardrailed execution within limits they define. As confidence grows, the system handles more decisions autonomously while humans manage exceptions. And for environments where the track record supports it, closed-loop optimization runs in the background and becomes boring, which is the goal. Each stage is a legitimate operating mode, not a stepping stone you have to rush through.

That design distinction matters more with AI workloads than it ever did with traditional services, precisely because the trust-building process is starting from zero on workloads where the cost of getting it wrong is highest.

> “Trust takes a long time to build and a single production incident to undermine.”

The other piece that makes this sustainable is rollout safety. Trust takes a long time to build and a single production incident to undermine. Start with the workloads showing the most headroom between requests and actual usage. Make changes incrementally, small enough that a bad outcome stays contained. Rollback needs to be fast and tied to the health signals the team already monitors. And start with opt-in, not opt-out. Let the teams willing to go first build a track record that others can look at.

## **The broader pattern**

The 71% figure is sometimes read as resistance to automation. I think it’s a more accurate picture of how operational trust actually forms: conditional, earned over time, and moving at different speeds depending on what’s at stake. AI workloads are raising those stakes significantly, which means the path to trusted automation matters more now than it did when the cost of caution was just some unused CPU.

> “Most of what gets written about Kubernetes optimization focuses on tooling capability, and the tooling is capable. The harder problem is the human one.”

Most of what gets written about Kubernetes optimization focuses on tooling capability, and the tooling is capable. The harder problem is the human one. If your team is managing AI inference workloads on [Kubernetes and your optimization](https://thenewstack.io/go-beyond-devops-with-autonomous-full-stack-optimization/) tooling is sitting in read-only mode, the question worth asking isn’t whether to trust the system. It’s whether the system is designed to let you build that trust gradually, starting where the stakes are low and expanding as the evidence supports it, on workloads where getting it wrong costs more than it ever has before.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/ef632ec9-cropped-6af8874c-7xl80xrcanikrplucbevvxfkjuymwyrfsehjbhuxqui-600x600.png)

Yasmin Rajabi is the Chief Operating Officer at CloudBolt Software. She is a recognized leader in the FinOps and Kubernetes communities, and her background as an engineer, product leader, and operator gives her a holistic perspective on the challenges facing...

Read more from Yasmin Rajabi](https://thenewstack.io/author/yasmin-rajabi/)