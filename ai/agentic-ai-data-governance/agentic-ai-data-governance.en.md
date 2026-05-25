Software development has always had a way of quietly distributing sensitive data in unexpected places, and many organizations have lost track of where it is.

However, the rise of agentic AI has pushed that problem into new territory. AI agents are not just accelerating the software development lifecycle (SDLC); [they are evolving the process](https://thenewstack.io/how-generative-ai-is-reshaping-the-sdlc/) by touching data at every stage in ways that teams may not fully see. The concern is that it is interacting with potentially sensitive data without a specific request. The scale and speed at which this can occur can exceed the governance frameworks of many organizations.

The encouraging news is that this is a solvable problem. Teams that build strong data governance practices designed for machine speed and autonomous systems, and not just human workflows, will comply more confidently and innovate faster. This, in turn, will support organizations’ ability to build AI they can trust.

Test Data Management best practices have been relatively well understood for years. Managing the test data throughout the product development cycle can be performed safely and efficiently.

Unfortunately, sensitive data still often appears across the SDLC, including development sandboxes, CI/CD pipelines, model training datasets, feature stores, regression testing environments, and [AI agent memory](https://thenewstack.io/red-hat-agentic-skills-repository/) stores. It can be present in every environment and across every model, throughout the development lifecycle, creating significant organizational risk.

This matters because the volume of code and test data are growing sharply. With the rise of agentic AI, fewer humans are involved in the coding, and more are instructing AI agents to do it.

That shift places greater emphasis on the need for test data because, as more code is generated, more of it needs to be tested.

Agentic AI is increasingly capable of autonomously driving this process. As a result, many organizations are reporting that AI adoption is accelerating faster than their data privacy strategies can keep up.

## Non-production environments and known risks

There is a persistent blind spot in how organizations think about data security. Production and [non-production environments](https://www.perforce.com/blog/pdx/non-production-environment-risks) are treated very differently, even when both hold large volumes of sensitive data. Production environments are equipped with SOC monitoring, strict access controls, and incident response protocols.

Non-production environments, on the other hand, include development, test, analytics, and AI. These environments were simply not built to withstand the same level of threats as production data, which is precisely why allowing real customer data, financial records, or health information to flow into them is high risk.

The problem is compounded by the economics of convenience, doing more of what is easier. DevOps culture has encouraged environment proliferation, such as [spinning up multiple production-like clones](https://www.perforce.com/blog/pdx/database-cloning), refreshing data regularly, and accelerating delivery pipelines. More environments mean more copies of data.

When shortcuts feel low-risk, they become the default. Conversely, when properly governed, using techniques such as virtualization and masked data makes access just as frictionless, and teams do the right thing. The answer is not to restrict the data; it is to make compliance the path of least resistance.

> “The answer is not to restrict the data; it is to make compliance the path of least resistance.”

[Data governance frameworks](https://thenewstack.io/data-governance-ai-agents/) were built for human workflows and allow for manual reviews, approval committees, and periodic audits. That model was already straining before AI arrived. With autonomous agents now capable of making hundreds or thousands of data requests per hour, it is simply incompatible with the new reality.

Governance needs to function as a service, with automated controls that enforce policy at the point of data delivery, in real time. [Data compliance](https://www.perforce.com/solutions/data-compliance) is increasingly being executed at runtime, meeting the ultimate requirement for continuous compliance. That puts much greater pressure on organizations to know exactly what kind of data they are working with, meaning that classification and data intelligence need to be [embedded into the pipeline](https://www.perforce.com/blog/pdx/etl-pipeline-best-practices), not bolted on as an afterthought.

## Building governance for the agentic era

DevOps best practices do not become obsolete in the age of agentic AI. In fact, they become more important. The [2026 State of DevOps Report](https://www.perforce.com/resources/state-of-devops) reinforces that mature DevOps is foundational to AI success. The same holds for data governance. Here are the practices that matter most:

* Embed compliance controls into the data pipeline itself, not as a downstream review step. Compliance logic should execute automatically when data is requested or delivered. This is what transforms governance from a bottleneck into a service.
* Replace production data copies with virtualized, masked, and synthetic alternatives. Virtualized environments allow teams to spin up production-like database copies in seconds without moving raw sensitive data. [Synthetic data can be generated](https://www.perforce.com/resources/pdx/synthetic-data-generation) to exact specifications, including edge cases that do not exist in production.
* Use the Model Context Protocol (MCP) to provide agentic DevOps pipelines with a standard interface for testing data environments. MCP allows AI agents and developers to interact with data infrastructure through natural-language conversational prompts, removing the need to log in to multiple systems or wait for infrastructure teams to establish integrations. When requesting a properly governed data copy is as easy as cloning a production one, teams will do the right thing by default.
* Shift from audit-based governance to runtime enforcement. Classification and tagging should be done initially, continuously revised, and then enforced at runtime.

Two scenarios illustrate how this plays out in modern engineering organizations. In the first case, a testing agent runs regression tests overnight and discovers it needs a fresh copy of a payments database, masked for PCI compliance.

No human is available to approve the request. The agent calls a data API, receives a virtualized, masked copy within 90 seconds, completes its tests, and tears the environment down without a compliance ticket ever being raised.

In the second situation, a QA agent needs to test how a payment system handles 10,000 simultaneous expired credit cards during a leap year. That scenario does not exist in production data. The agent generates a synthetic dataset with exactly those characteristics, runs the tests, validates a fix, and closes the defect before the team’s morning stand-up. No real customer data was involved at any point.

What both scenarios share is a design philosophy of being compliant with production-quality data on demand. All this is done through an API or natural language interface, with policy enforcement built into the delivery mechanism, rather than applied as a gate afterward.

The SDLC has never been more productive, and it has never exposed more sensitive data to more systems, more agents, and more environments simultaneously. The window to get governance right is narrowing, as regulatory frameworks like the [EU AI Act](https://www.perforce.com/blog/pdx/eu-ai-act) raise the bar for compliant AI development and data breaches in non-production environments continue to make headlines.

> “The SDLC has never been more productive, and it has never exposed more sensitive data to more systems, more agents, and more environments simultaneously.”

It’s no surprise that 86% of enterprises are looking to invest in AI and data privacy solutions, according to the [2025 State of AI and Data Privacy Report](https://www.perforce.com/resources/pdx/state-of-ai-and-data-privacy-report) from Perforce Delphix.

The organizations that will navigate this well are not those that build manual compliance processes. They are the ones that redesign governance as infrastructure: automated, embedded, real-time, and built for a world where the primary consumers of data are autonomous systems operating at machine speed. Approached the right way, a solid backbone of trusted data tangibly accelerates innovation.

That is not a future state. The tools, processes, and techniques are in place; now is the time for engineering leaders to build this foundation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/05/2936c880-cropped-d34a4c10-brian-muskoff_headshot.png)

Brian leads global teams to build category-defining DevOps for data products that help the world's largest enterprises move faster and safer across multi-cloud and AI environments. As the VP of Product at Perforce Delphix, he leads portfolio strategy for its...

Read more from Brian Muskoff](https://thenewstack.io/author/brian-muskoff/)