**As enterprises move from experimenting with AI** to running autonomous agents in production, an infrastructure problem is emerging: rising telemetry costs. Non-deterministic, iterative, and capable of generating data at machine speed, agents are far harder to monitor — and their costs far harder to predict — than conventional applications.

Many companies are struggling to attribute and defend their telemetry bills. In fact, [59% of organizations](https://www.prnewswire.com/news-releases/new-apica-research-agentic-ai-poised-to-trigger-9-5x-telemetry-data-explosion-leaving-most-enterprises-exposed-302789312.html) have already terminated or delayed an agentic AI deployment due to monitoring costs, according to a survey of more than 300 enterprise IT decision-makers in North America and Western Europe, commissioned by Apica and conducted by Omdia/Informa TechTarget.

The agents most affected are often in some of the most high-stakes deployments: think cybersecurity, compliance, and fraud detection. As monitoring bills explode, deployments aren’t necessarily getting killed by engineering teams. More often than not, it’s finance pulling the plug.

[Andi Mann](https://www.linkedin.com/in/andimann/), chief product and technology officer at [Apica](https://www.apica.io/), recently saw this play out at a large bank. The organization couldn’t pin down exactly what it was spending on its AI programs.

“They knew they couldn’t afford to keep going on the same trajectory, so they had no choice but to cancel certain AI programs,” Mann tells *The New Stack*. “It’s a pattern I have seen before, because AI projects are cannibalizing typical budgets.”

> “It’s a pattern I have seen before, because AI projects are cannibalizing typical budgets.”

The implications are huge. As people, funding, and monitoring resources are diverted toward new AI workloads, other parts of the business start to suffer. Mann says he’s seeing outages, downtime, penetration attacks, and DDoS protection compete for the same resources.

The problem is already showing up in research. Most (54%) enterprises have seen telemetry volume [triple](https://www.prnewswire.com/news-releases/new-apica-research-agentic-ai-poised-to-trigger-9-5x-telemetry-data-explosion-leaving-most-enterprises-exposed-302789312.html) in the past year alone, with 43% of that growth coming from AI/ML workloads — by far the largest driver. Businesses are under pressure to address this crisis as their observability bills climb. They report spending an average of $3.17 million on observability, with that figure growing 28% year over year and showing no obvious ceiling. No wonder then that 83% rank AI observability as a top priority for the year ahead.

They report spending an average of $3.17 million on observability, with that figure growing 28% year over year and showing no obvious ceiling. No wonder then that 83% rank AI observability as a top priority for the year ahead.

## The coming wave could be catastrophic

With a new cloud service, database, or application, you’d expect the monitoring burden and telemetry data to rise by a relatively predictable increment. But enterprises now foresee an average 9.5X increase in telemetry data within two years.

“Imagine if your credit card or grocery bill went up more than nine times — that is not a marginal amount,” Mann says. “This isn’t a gentle ramp; it’s a skyscraper, and it’s prompting panic.”

> “This isn’t a gentle ramp; it’s a skyscraper, and it’s prompting panic.”

Some 44% of organizations expect their telemetry data to increase by 6X to 100X.

The reason is that an agent task isn’t the same as a single application request. A customer-support task might generate a top-level trace, several model calls, retrieval operations, tool calls, retries, and loops. But if the agent delegates work to another agent, that adds another branch to the trace.

Each model can produce token, latency, cost, and provider data, while each tool call generates its own records for arguments, results, status, and downstream activity. Identifiers such as `tool_name`, `agent_id`, and `trace_id` also create high cardinality, making data harder to aggregate and more expensive to index, with costs compounding at every stage.

That creates an uncomfortable gap between AI ambition and infrastructure readiness. Although 35% of enterprises claim widespread agentic AI deployment, operating and managing those systems is very different. Nearly two-thirds are only somewhat prepared for the shift. Unlike conventional applications, agents can call multiple models and tools, repeat tasks, or expand a workflow in unpredictable ways, making both capacity and monitoring costs difficult to forecast.

## From extreme telemetry costs to an upstream control layer

The answer, according to Mann, is to intervene earlier. “You can’t keep sending essentially useless data to an expensive central analytics or storage platform because there’s no point analyzing data which says everything is fine,” he says. “As early as possible, get the pipeline to use data collectors and manage those at source.”

Legacy observability platforms were built around collecting data, ingesting it, storing and indexing it, and then analyzing it. That model worked for human-driven, dashboard-queried workloads, but agentic AI requires decisions to be made before telemetry reaches the most expensive parts of the stack.

A pipeline-first architecture can sample repetitive successful events while retaining failures, retries, policy violations, and unusually slow traces. It can enrich records with agent, session, model, tool, token, and estimated-cost data, redact sensitive prompts and identifiers, and aggregate metrics and long-term records to destinations with different cost and retention profiles.

A compact metric or sampled span might represent a routine successful tool call, while a failed call retains its parent trace, error details, retry history, and security context. The aim is to preserve the information needed to explain an agent’s behavior while reducing redundant data and limiting what gets indexed.

Agents also need millisecond-level context for autonomous decisions. Processing telemetry close to its source allows organizations to quickly detect retry storms, excessive tool loops, or unusual token consumption, rather than waiting for data to be ingested and indexed centrally.

Without upstream control, businesses risk feeding fragmented, unnecessary telemetry into platforms that charge for every additional gigabyte, index, and retained record.

## Architecture that separates winners from cancellations

The payoff for rethinking the telemetry pipeline is hard to ignore. Enterprises with a telemetry pipeline are 50% more likely to be prepared for the growth of agentic AI data. Among mature agentic AI organizations, pipeline adoption is what sets them apart: these organizations are 80% more likely to have avoided the operational cost challenges hampering their peers.

> Rather than treating the observability platform as a catch-all destination, enterprises can make decisions about telemetry before it gets there.

The answer is to move the intelligence upstream. Rather than treating the observability platform as a catch-all destination, enterprises can make decisions about telemetry before it gets there — filtering out noise, enriching what matters, and routing data according to its value and purpose. That means less data hitting expensive storage and analytics systems, while the information that does make it through is more useful and available in real time.

Crucially, this isn’t about ripping out the observability platforms enterprises already rely on. It’s about putting a smarter control layer in front of them: deciding what data deserves to be ingested, where it should go, and how much it should cost.

Existing observability platforms still have an important role to play. “The pipeline can’t do everything, but it can act as a first responder,” says Mann. “You still work with the big analytics platforms, but you’re saving money, reducing risk, and improving your compliance performance.”

The Apica study finds that its pipeline control, metrics foundation, and data readiness services, for example, can reduce the total cost of ownership by 40% compared to legacy observability platforms. Of course, though, the actual savings will depend on telemetry volumes, retention policies, sampling rules, routing decisions, existing contracts, and the proportion of data that can be processed before ingestion.

The window to rethink the architecture is now. Some 68% of enterprises plan to evaluate changes to their observability stack within the next six months, while almost a quarter say existing vendor relationships won’t be a significant factor in those decisions. The next phase of observability will be won by the ability to handle what agentic AI throws at the infrastructure.

That means the pipeline can no longer be treated as plumbing that moves telemetry from A to B. It’s becoming the control layer for an increasingly autonomous, data-hungry environment.

Organizations that establish agentic-ready infrastructure will be better positioned to reduce observability costs and improve risk performance. Mann doesn’t think platform engineering and SRE teams have much choice. “This has already become a board-level decision,” he says. “Ultimately, it’s a choice about how smart you can afford to make your business.”

***Download the Omdia research report: “***[***The Agentic AI Telemetry Crisis: Are You Ready for What’s Coming?***](https://www.apica.io/state-of-agentic-ready-observability-infrastructure-report-2026/)***”***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/e36dae7b-cropped-6c610b3e-megan-carnegie-square-sizing-600x600.jpg)

Megan is a London-based independent technology journalist with over a decade of experience writing analytical features for publications like WIRED, Fast Company, and the BBC. She specializes in the world of work, covering Big Tech, startups, AI, recruitment trends, and...

Read more from Megan Carnegie](https://thenewstack.io/author/megan-carnegie/)