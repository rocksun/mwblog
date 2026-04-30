Nothing is Greenfield in an enterprise. Hybrid cloud complexity sits atop siloed teams and systems, making it nearly impossible to observe, understand, remediate, and prevent outages. Understaffed operations and [site reliability teams](https://thenewstack.io/observability/) now also have to keep pace with AI. All while the enterprise stack faces more risks of instability and insecurity than ever.

To respond, [enterprise operations](https://thenewstack.io/operations/) must fundamentally change how they approach Day 2 and beyond. No longer is it safer to maintain thick boundaries between services or divisions — they block return on AI investment anyway.

To survive, organizations must move from siloed, reactive dashboards to a closed-loop operations model, supported by AI agents, treating orchestration, observability, and remediation as a continuous feedback cycle.

“You’ve got to understand that Day 2 and Day 1 are in a closed loop because what you provision, you need to understand what the current Brownfield is. And you might not want to make a lot of changes when there are a lot of issues going on,” [Phanidhar Koganti](https://www.linkedin.com/in/networkleader/), senior distinguished technologist in [Hewlett Packard Enterprise (HPE) hybrid cloud](https://www.hpe.com/us/en/home.html), tells *The New Stack*.

Under the current restrictions facing ops teams, the only way forward seems to be applying AI techniques to operations, [extracting signals from](https://thenewstack.io/hpe-self-healing-ai-infrastructure/) all the noise. This move from DIY to autonomous remediation requires more than just an infusion of AI.

AI-enabled ops demands a platform engineering strategy, predictive analytics, new ops metrics, and more. All is not to replace today’s operators, but to optimize the team’s time, enabling them to be faster, more strategic, and hopefully less stressed in stressful times.

## **When every resource is constrained**

“Creation is now only limited by the cost of compute, not capacity,” promises the [Outcome Engineering Manifesto](https://o16g.com/manifesto/) about the change AI agents are forcing in the tech industry. Yet AI has actually left most operations teams feeling more limited than ever, in both time and available resources.

“Our customers are under pressure to continue to offer the same SLAs [service level agreements] with a lot less resources,” [Sridhar Katere](https://www.linkedin.com/in/sridharkatere/), VP of engineering for HPE’s data center business unit, says. In practice, this means there are fewer ops team members “to troubleshoot an issue when something happens during Day 2.”

Operations agents, managed by ops teams, are an opportunity to scale up troubleshooting and remediation, without expanding teams.

HPE OpsRamp Software recently went general availability (GA) with its [agentic operations copilot](https://community.hpe.com/t5/the-cloud-experience-everywhere/operations-copilot-from-hpe-opsramp-software-your-partner-for/ba-p/7264586), with which, Koganti explains, “You can express what you are trying to achieve in a very high-level intent, and that will be converted to detailed deployment plans, which will include data center, networking-related automation, storage, and various other components for the whole infrastructure to come together.”

AI can also help ops teams move from reactive to proactive, while advocating for right-sized resource budgeting.

“When we say issues, it doesn’t mean the nature of the failure is service-disruptive only,” Koganti says. “If you’re going to go out of capacity, meaning optics could fall, that’s a binary failure that you’re trying to predict.”

If an ops engineer knows that something, like a switch, is likely to fail in six weeks, Katere explains, then not only do they have time to prevent an outage, but they can also better budget hardware resources, which are extremely constrained by current supply chain uncertainty.

“This is where we are building predictive analytics to help customers plan and procure the necessary hardware and components ahead of time,” he continues.

Through recent acquisitions and ongoing investment, HPE is building its own operations control center to define this next-gen hybrid, multi-cloud operational model. Its [CloudOps Software suite](https://www.hpe.com/uk/en/software/cloud-ops-suite.html) — anchored by [HPE OpsRamp Software](https://www.hpe.com/us/en/opsramp.html) and [HPE Morpheus Software](https://www.hpe.com/us/en/morpheus-enterprise-software/features.html), with [HPE Apstra Data Center Director](https://www.hpe.com/us/en/apstra-data-center-director.html) available as an add-on — is designed to help organizations map out what their full cloud operating model actually requires.

Following OpsRamp’s GA release, other HPE products are expected to release agentic systems with conversational interfaces soon.

“Whatever we are talking about in optimizing the full stack will be applicable to capacity issues or even performance issues across the whole stack,” Koganti says, because enterprise systems’ complexity is many-layered.

## **Ops metrics need redefining**

While the mean time to resolution (MTTR) — total downtime divided by total number of incidents — remains an important metric, it’s insufficient in the face of this enterprise-grade complexity.

Similarly, the means of identification or detection are still key, but they’re viewed differently when you bring AI into the mix. AI operations must prioritize time to correlate, applying AI ops tooling to analyze logs, metrics, and traces to connect disparate signals into a [single, traceable, recommended action](https://thenewstack.io/agentic-ai-observability-auditing/).

> “First instinct is often that network is the culprit, so it’s very important for networking to self-diagnose and come back to say, ‘Hey, I’m not the problem.'”

Like the famous Spider-Man pointing meme, if they were all pointing at networking or storage, AI operations tools must also optimize for mean time to innocence.

“First instinct is often that network is the culprit, so it’s very important for networking to self-diagnose and come back to say: Hey, I’m not the problem,” Katere says.

In a full-stack environment, symptoms and downtime rarely occur in the same layer as the cause.

> “…the symptom of a failure and the cause of the failure are never in the same layer.”

“What is common that we see among the majority of our customers is that the symptom of a failure and the cause of the failure are never in the same layer. What I mean by that is, for example, the symptom can appear in the application layer as my application transactions are timing out, and so on. While the actual cause of it could be somewhere down in the network layer or the storage layer, most of the time, the network is the culprit,” Koganti says.

“IT stacks are getting complicated. You need collaboration between various layers and agentic collaborations, as well as regular traditional AIOps collaboration.”

Enterprise-grade complexity, which can see multiple failures occurring in parallel, requires tighter integrations across the full stack, along with AI to filter the important signals from the noise. Then the next step is [AI agents auto-remediating](https://thenewstack.io/hpe-self-healing-ai-infrastructure/) when appropriate — but only when its actions are explainable to the human operator.

HPE also has its own efficacy metrics, including quarterly KPIs that measure how well its platform predicts and troubleshoots issues. Currently, the platform — backed by graph and GraphQL, with a highly contextualized data stack — is about 40% accurate on troubleshooting, Katere says, with a goal of topping 70% by the end of the year. HPE is baking its nearly 100 years of experience in the enterprise space into its new [CloudOps Software](https://www.hpe.com/uk/en/software/cloud-ops-suite.html), along with [agentic skills](https://thenewstack.io/hpe-agentic-ai-ops-burnout/) trained at different layers: platform, driver, through, replaceable units, system, and more.

“We are not living in a static world. It’s a very dynamic world.” Katere admits that it’s all a “moving target in light of how fast things are changing even in the slower enterprise software development lifecycle.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)