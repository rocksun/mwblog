When operations teams get an alert, three questions need to be answered before any action can take place:

1. What broke?
2. What depends on it?
3. Who owns it?

Without a clear map of how business and technical services connect, finding the answers to those questions can turn into hours of trial and error, frustrated customers, and even lost revenue.

Service mapping and service architecture design are critical to minimizing service disruption and accelerating incident recovery, as they can both enable faster, more accurate mobilization and more efficient [root cause analysis](https://thenewstack.io/elastic-agentic-observability-enterprise-adoption/).

As more of that triage work shifts from people to automated and AI-driven systems, it becomes even more evident that those systems are only as good as the service map they’re reasoning over.

Well-designed service architecture begins with a clear understanding of what a service is: a self-contained unit of functionality with a single owning team. It’s also important to distinguish technical from business services:

* Technical services: The APIs, databases, authentication systems, and microservices that power digital operations.
* Business services: The customer-facing capabilities built on top.

In short, technical services show how things work under the hood while business services show what the customer actually experiences.

> “Technical services show how things work under the hood while business services show what the customer actually experiences.”

A single business service might need several underlying technical services to function, while one technical service might power multiple business services. This complexity is precisely what slows [incident management](https://thenewstack.io/when-ai-fails-the-new-reality-of-incident-management/), but it can be solved with proper service mapping.

## Five steps to guide service architecture design

Organizations can take the following steps to structure their business and technical services with a clear architectural design:

### 1: Start with customer-facing business services

Begin with the services that matter most to customers, rather than getting bogged down in a complex web of underlying technical components. It can be an online checkout system for an e-commerce provider, or a claims processing function for an insurer. The bottom line is that it’s something customers recognize and depend on. Teams should identify these services and map them first, as this will help engineers and operations teams—as well as any automated systems triaging on their behalf—to target and prioritize the underlying technical services when something goes wrong.

### 2: Map the supporting technical services

The next step is understanding which underlying components make up each business service. Without a clear view of these dependencies, incident management becomes a matter of guesswork, prolonging outages, eroding customer loyalty, and negatively impacting revenue in the long term.

An accurate map connecting business to technical services gives engineers and digital operations teams a powerful analytical tool to cut through the noise of alerts and narrow in on the cause of a failing service.

For example, a wire transfer service might be supported by multiple technical services, including a transaction authorization service, fraud detection API, payment gateway service, notification service, and so on. If operations teams (and the automation meant to assist them) can’t see the downstream impacts of a wire transfer service outage, they risk flying blind.

Regulators around the world are increasingly formalizing this expectation. Financial services companies in the European Union, for example, are now required to demonstrate they can identify critical services and their dependencies, and restore them within a defined tolerance.

This means good service architecture is becoming a compliance requirement for some industries.

### 3: Assign clear ownership

Each service should have one accountable team. Assign one team to each business function so incidents have a defined response path, and ensure each technical service has a single owner.

> “Good service architecture is becoming a compliance requirement for some industries.”

That doesn’t mean a team can’t “own” multiple services, but it does mean that if something goes wrong, it’s immediately clear who needs to be mobilized. Such specificity lowers the operational cost of every incident and reduces unnecessary interruptions for subject matter experts who may not be able to help.

Teams without this clarity incur both operational and human costs: responders repeatedly alerted to the same unresolved issue are much more vulnerable to burnout.

### 4: Use deployment cycles as a guide

If something deploys independently, teams should treat it as a standalone service and use this rule of thumb when technical service boundaries aren’t obvious.

Breaking technical components down into individual services provides more accurate operational insight. This way, when a problem occurs, it’s easier to pinpoint the cause and relevant team. If a service is made too broad, then the failure gets hidden.

### 5: Connect operational data

The final step is to connect operational data into a single reliable source of truth. Integrations should consolidate monitoring signals, and the service directory should be synced with the developer portal so that service architecture, on-call schedules, and incident data are all kept in one place. Additionally, connect existing configuration management data to surface sources of service and dependency data that already exist.

The goal is a single, continuously updated system that connects engineers, operations teams, and any AI or automation layered on top to the right intelligence.

## Start small for incremental wins

If this all seems like a significant extra workload on top of day-to-day operations, it’s better to break it down into bite-sized pieces. Pick one of the organization’s most critical business services and map its underlying technical services. Define ownership, set escalation policies, and connect monitoring tools. Then repeat.

> “Pick one of the organization’s most critical business services and map its underlying technical services. Define ownership, set escalation policies, and connect monitoring tools. Then repeat.”

Once the service architecture is complete, it gives digital [operations teams](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/) the context to show the blast radius of an incident and which teams to mobilize. The cost of every incident that follows is lowered, and a stronger foundation for operational resilience is built. As more of the incident response process becomes automated, that mapping is what gives AI-driven tools the context they need to act correctly, making service architecture as much a foundation for the future of operations as it is a fix for today’s incidents.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/08/b92d7ebf-cropped-b12add8e-debora-cambe.jpg)

Débora Cambé is a product marketing manager at PagerDuty supporting the company's Incident Response go-to-market initiatives. Her 10+ years of experience as a marketing professional include working as owned media manager at PlayStation and as social media consultant for Yorn,...

Read more from Debora Cambe](https://thenewstack.io/author/debora-cambe/)