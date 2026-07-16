Microsoft recently took the wraps off Brain, the internal AI system that continuously monitors Azure’s health and, increasingly, acts on what it finds — declaring outages, pausing harmful rollouts, and notifying affected customers.

Azure CTO [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/) first wrote about the system in a blog post, “[Meet Brain: The AI system behind Azure reliability](https://azure.microsoft.com/en-us/blog/meet-brain-the-ai-system-behind-azure-reliability/),” the first in a planned multi-part series about the Azure team’s reliability and resiliency tooling.

To dive deeper, *The New Stack* sat down with Russinovich, who is also Azure’s deputy CISO and a technical fellow, to talk about how the Brain project came to be and how it evolved over time.

Brain, as Microsoft describes it, is Azure’s centralized AIOps system for cloud health. It operates as an intelligent layer on top of [Azure Resource Graph](https://azure.microsoft.com/en-us/get-started/azure-portal/resource-graph) (ARG), and together, the company says, the two form a real-time digital twin of Azure’s health.

## A real-time digital twin

While Brain today uses many AI tools, the project is actually much older than the generative AI boom, and to get started, the team had to build a solid foundation first. “At the heart of this system is Azure Resource Graph, which started as ‘let’s create a digital twin of Azure, so we can understand the relationship between the different resources in Azure,’” Russinovich tells *The New Stack*.

That internal digital twin became a public service at the urging of what Russinovich calls whale customers, those “that have huge estates across many different tenants and subscriptions that wanted to do easy queries across the whole thing, like, ‘What Linux VMs do I have, and what versions of Linux are they on?'”

It was actually the root cause analysis on top of that graph that Brain really began with. “Many times you can just trace dependencies and say, well, these services all depend on this other service that has gone unhealthy, and so that I think was the genesis of having Brain go and start to have a lot of ML-driven algorithms to identify root cause on top of the graph,” Russinovich explains.

Around the same time, Microsoft kept encountering a measurement gap: A service team’s own health metrics indicated everything was fine, but customers saw failures. Russinovich says that could happen because the Azure team wasn’t “measuring what customers are experiencing, or because they’re aggregating at scopes that hide customer-specific problems.”

So Microsoft decided to standardize. “We decided, let’s go standardize on the way that we measure health,” Russinovich says, “and we came up with service level indicators, SLIs.”

Getting services across Azure to actually emit them through shared libraries that conformed to the schema was a complex task that took several years.

“It’s kind of a whole bunch of different things that happened in parallel that all have come together,” he says. “There’s just a tremendous amount of data engineering that goes into this, and trying to keep it as automated as possible.”

## Three signals feed Brain

In his blog post, Russinovich writes that Azure’s reliability challenge isn’t a lack of tooling but a “comprehension problem,” with a hyperscale cloud now producing more signal than humans can read.

Azure runs hundreds of services across more than 80 regions, 500+ data centers, and 800,000+ kilometers of fiber and subsea cable. And yet, he writes, Microsoft still sometimes learns about a quietly degrading service from a customer before its own systems detect it.

Today, Brain pulls from three classes of signals. The standardized SLIs come first. Service teams also build and register their own domain-specific monitors, which run alongside telemetry-like deployments, support volume, and cross-service dependency signals. Third-party indicators make up the rest.

> Brain produces the same four outputs for any subject, whether that’s a service, a region, a deployment unit, or a customer’s resources.

Based on this, Brain produces the same four outputs for any subject, whether that’s a service, a region, a deployment unit, or a customer’s resources. It reports the health state, how severe the issue is, who is impacted, and — crucially — why it reached that conclusion.

Those conclusions then drive alerts and remediations. Brain declares outages based on blast radius, Russinovich notes, and scopes customer notifications to the impacted subscriptions and regions. The system automatically routes incidents to the appropriate service team and sends deployment-gate signals to pause rollouts causing the issues.

Russinovich says the system is “very pluggable in terms of what signals go into it, and includes even things like customer support tickets that have been opened, and social media posts that mention Azure.” He says Brain is “primarily monitoring,” but “it also can take automated repair actions, too. So for some incidents, teams can specify if, when this happens, go try these things, and Brain kicks those off as well.”

He says the SLIs are “emitted at the scale unit level, so that we can do aggregations for overall health. We can pinpoint specific customers that are being impacted, because we know what customers map to which scale units, and that’s the way that the auto notification triggers off that.”

## Why ML sets the thresholds

Microsoft’s original plan for turning SLIs into health determinations was the textbook one, asking every service team to [define its own SLOs](https://thenewstack.io/how-to-correctly-frame-and-calculate-latency-slos/). It didn’t work.

Russinovich says the schema work itself was hard enough, but “even more challenging is coming up with an SLO that is actually a good SLO.” Teams sandbagged their thresholds, he says.

“[Everyone] wants to be very conservative because they don’t want to get paged or have customers told that things are unhealthy when they’re not, so they’re like, ‘You know what, my SLO is 5% of API queries can fail, and then let’s call it unhealthy,’ when actually that’s not a good way to determine health or regressions as rollouts happen, so we decided, ‘Let’s just stop asking them to define their SLOs.'”

> “Everyone wants to be very conservative because they don’t want to get paged… so we decided, ‘Let’s just stop asking them to define their SLOs.'”

Instead, ML models now derive the thresholds from each service’s own behavior, per scale unit and per region.

“There’s a baseline for behavior of the service in this region versus that region,” Russinovich says, “and then we can see when there’s regressions.” The resulting SLOs are dynamically adjustable and automated, he explains.

Tying a regression back to the change that caused it is harder still, he says. Brain tracks rollouts of service updates, and “we’ve got ML algorithms too that can identify with confidence this rollout is causing a regression.” But, he says, the rollout that just reached a scale unit isn’t necessarily the culprit.

“A change doesn’t necessarily show up as a regression immediately. It can have latency; it can take hours to show up, or in some cases even days… there can be many, many deployments that have happened over the last day, and you’re like, which one was it?” That’s why, he says, “there’s a lot of ML going into symptom versus change mapping and automated detection.”

## Agents that fix outages

The published post keeps its results vague. Detection precision “has improved significantly”; a “substantial majority” of Brain-integrated outages were auto-communicated to customers in the past year; and time-to-notification improved “materially” over manual notifications. In the interview, Russinovich puts numbers on some of it.

He says, “The thing that frustrates customers the most is when they’ve got to call us and tell us there’s an issue, because then they’re like, you guys don’t even know that there’s a problem. I have to tell you there’s a problem. If we can tell them, hey, there’s a problem, we know about it.” Auto-notification, he says, has driven “this reduction of like four to 6x in terms of customer support tickets open, because Brain is automatically notifying them, and they know that we’re on it.”

> “The second you put a human in that loop, you can blow right past the 15 minutes.”

“Our time-to-mitigate goal is 15 minutes, from some problem to actually being resolved within 15 minutes,” Russinovich says. “The second you put a human in that loop, you can blow right past the 15 minutes.”

According to Russinovich, the company hits this 15-minute notification window for 80 to 90 percent of the services on Brain. Often, it’s also much shorter and closer to five minutes.

One caveat here is that not everything runs through Brain yet. Microsoft prioritized what it calls its critical services, the foundation the rest of Azure depends on, and Russinovich puts their coverage at “like 70 or 80% of them, and then the tail’s being worked on.”

He notes the rest aren’t flying blind. “It’s not like the services that aren’t on Brain don’t have health systems and alerting and everything. Brain improves things, even for those services.”

For the engineers who do get paged, Brain assembles the picture they used to piece together by hand.

“The incident gets populated initially with an automated collection of information that will say, here’s the graphs of availability on this SLI over these scale units over the last 24 hours, here’s the list of impacted customers, this is the scale unit, here’s the other information supporting this, and so already there you’re saving the engineer huge amounts of time just in going and information gathering and just presenting it right in front of them.”

## Agents on top

In the Brain announcement, Russinovich writes that “agents need something to be agentic about.” A triage agent that doesn’t know the dependency graph can’t triage anything, he argues, and the health model is “the prerequisite, not the consequence, of agentic operations at this scale.”

At this point, Microsoft has started running agents on top of Brain. A system called Triangle, which Microsoft Research also [described in a](https://www.microsoft.com/en-us/research/publication/triangle-empowering-incident-triage-with-multi-agents/) [2025 paper](https://www.microsoft.com/en-us/research/publication/triangle-empowering-incident-triage-with-multi-agents/), gives each service team an LLM-based agent trained on its historical incidents and troubleshooting guides, with an orchestrator that routes ambiguous incidents among them.

“This Triangle system has agentic representatives for the services, where the Triangle orchestrator then fans it out and says, ‘Here’s the incident; raise your hand if you think it’s yours,’” Russinovich says. Without it, tickets would bounce from team to team — something Microsoft calls handoffs — which increases response times.

> “We don’t have to write down every single rule prescriptively… let the agent do things based on its own judgment.”

It’s still early days for Triangle, though. “We’re still relatively early, so there’s only a small number of services onboarded to it, but already for them the handoffs are much faster and more direct than pre-Brain,” Russinovich says.

In the long term, he wants agents to replace the deterministic remediation rules that teams write today.

“We don’t have to write down every single rule prescriptively,” he says. “And have this tree of decision making, but rather let the agent do things based on its own judgment, which has a whole bunch of benefits, like the system keeps up to date automatically. Then it can also find paths to resolution that we might miss in the deterministic rules that we’ve got.” On agents that actually fix things, he says, “We still consider ourselves at the beginning of that.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)