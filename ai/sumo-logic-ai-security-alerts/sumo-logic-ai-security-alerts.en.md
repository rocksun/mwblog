The instinct is almost universal: When something goes wrong, security teams reach for more data. The belief is that if they log everything, the bad guys will eventually reveal themselves in the noise.

“In an ideal world, we would just collect all the data and find the bad guys,” said [Chas Clawson](https://www.linkedin.com/in/chasclawson), VP of Security Strategy at [Sumo Logic](https://www.sumologic.com/), speaking during the recent TNS webinar, “[Log Everything, Alert Smarter: A SecOps Framework for AI-Driven Detection](https://thenewstack.io/webinar/log-everything-alert-smarter-a-secops-framework-for-ai-driven-detection/).”

“In reality, there are a lot of reasons why that historically has never worked,” Clawson says.

A veteran of US federal security operations and the NSA’s Red Team, Clawson has used the session to explain why the model keeps [failing SOCs](https://thenewstack.io/elastic-ai-soc-data-unification/) and what’s changing as agentic AI enters the picture.

## **The** “single glass of pain”

There’s a joke Clawson likes to tell: You buy a SIEM expecting a single pane of glass, and what you actually get is a single glass of pain. Collecting more data doesn’t fix anything on its own; it just means more alerts piling up faster than an analyst can get through them.

What Clawson calls the “funnel of fidelity” is his answer to that. Collection stays wide at the top, and then the noise gets stripped away until what lands in front of an analyst is a short list of alerts worth acting on, ideally strung together into something resembling an attack timeline rather than a pile of disconnected events. “There is no easy button,” he says. Getting there takes real work.

Is that a tooling problem or a discipline problem? Clawson’s answer: both. But he pointed to a bigger change underway: SOCs moving away from workflows where a human had to lay hands on every single alert, toward ones where agents take the first pass, and humans step in for what’s actually worth their time.

## **Entities, not events**

A recurring theme was entity-centric detection: grouping alerts around a user, host, service account, IP address, or hash rather than triaging each one in isolation. “It’s a losing proposition to try and triage every single alert that comes across your tools because there’s just too many of them,” Clawson says. Clustering by entity turns disconnected signals from email security, EDR and identity tools into a single, legible picture.

He also flagged non-human identities as a growing concern, expecting Red Teams to increasingly target autonomous agents through social engineering. “An agent is nothing more than a toddler with absolutely no street smarts, but all the keys to the kingdom,” he said, and many SOCs may lack the audit logs to catch it when one gets manipulated.

## **Trust is the new battleground**

Clawson spent a good chunk of the session talking about where AI actually pulls its weight, and his go-to comparison was treating an agent like a new hire. Given proper training, the right context, and clean data, it does the job well. But hand it raw, messy logs and ask it to find the bad guys, and it ends up burning a lot of effort just working out which field is the source IP.

That’s why Sumo Logic still leans on deterministic, rules-based detection for real-time alerting. AI comes in afterward, reasoning over the smaller, cleaner set of signals those rules surface, rather than trying to replace them.

Trust was the thing that most shaped how Sumo Logic built Dojo.ai, the platform housing its purpose-built agents, including a SOC analyst agent. Early users made their objection clear pretty fast: nobody wanted another black box they couldn’t verify. So every step an agent takes now traces back to the actual query behind it. As Clawson put it, “Maybe one day we’ll be in a world where I can just blindly trust an agent. We’re not quite there yet.”

On where to draw the line between automated and human-reviewed decisions, Clawson described a spectrum from human-in-the-loop to human-on-the-loop to human-out-of-loop, cautioning that the most cautious option isn’t always the safest, given how fast modern attacks move.

## **Data tiers and budget trade-offs**

Clawson’s advice on data management: figure out what you actually want to detect first, then work backward to the data that supports it, rather than hoovering everything up and sorting it out later. At Sumo Logic, that means tiering storage: cheap, low-touch storage for the low-priority stuff, and pricier, AI-ready processing reserved for whatever feeds real-time detection.

When budgets get squeezed, Clawson says the first thing to go is usually tool sprawl, not headcount or coverage. Getting several teams to give up their favorite point solution in favor of one consolidated platform is a hard conversation, but it tends to pay off more than letting every team keep the tool they like.

He closed by comparing the moment to the early days of cloud adoption: “If you don’t have an AI strategy, expect to be obsolete very, very soon.”

## **Watch on demand for more on breaking the alert fatigue cycle**

REGISTER NOW FOR THIS WEBINAR

You have successfully registered for the webinar.

Key Webinar Takeaways:

* Why “log everything” backfires, and the funnel of fidelity model to fix it.
* How entity-centric detection turns scattered alerts into a single, investigable picture.
* Where AI agents genuinely earn their keep in a SOC workflow, and where they don’t.
* How to build a data management strategy that keeps the right telemetry AI-ready without breaking the budget.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1cf43e50-cropped-bc46c9c3-headshot-disrupt-600x600.png)

Carly Page is a technology journalist covering cybersecurity, digital policy, and emerging tech, with more than 15 years’ experience reporting on how systems break and who gets burned when they do. She previously served as senior cybersecurity reporter at TechCrunch,...

Read more from Carly Page](https://thenewstack.io/author/carly-page/)