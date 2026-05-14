**If you work the high wire at a circus**, you’d better have a net down below if you want to continue in that line of business. Likewise, if you have an IT system that’s producing night and day for you and your clients, you should have complete protection if a slip-up or security breach happens – whether it affects one customer or 5 million.

Seattle-based [Temporal](https://temporal.io) has been getting a good measure of attention lately for how its software protects IT systems, whether small or scale-out — particularly when they’re processing large AI-related workloads.

Temporal, which hosted its [Replay 2026 developer conference](https://replay.temporal.io/) last week here in San Francisco, makes its own version of [Durable Execution](https://temporal.io/blog/what-is-durable-execution), an open-source-based software development framework that renders code fault-tolerant by automatically persisting its state. This allows long-running processes to resume exactly where they left off after crashes, network failures, or restarts. It converts fragile code into crash-proof workflows by recording steps, ensuring reliability without manual error-handling logic.

***See also: [Temporal reveals a serverless option for its Durable Execution platform](https://thenewstack.io/temporal-replay-2026-news/)***

Temporal, founded in 2019 by [Samar Abbas](https://www.linkedin.com/in/samar-abbas-381997/) and [Maxim Fateev](https://www.linkedin.com/in/fateev/) using their open-source [Cadence](https://github.com/cadence-workflow/cadence) workflow orchestration engine, is growing rapidly with more than 3,000 paying customers (including Nvidia, Netflix, Snap, and Stripe) and many thousands more open-source users.

Cadence is an open-source, fault-tolerant, and highly scalable workflow orchestration engine originally developed by Uber (and specifically, by Abbas and Fateev) in 2017 to manage complex, long-running, and distributed processes. It enables developers to use code rather than DSLs (Domain-Specific Languages) to define workflows that remain durable and stateful, even during service failures.

DSLs fall short in guaranteeing the state of enterprise software because they are designed for limited, high-level abstractions.

## **Direct fork of the Cadence engine**

Taking the concept to a new level, Abbas and Fateev created Temporal as a direct fork of the Cadence engine. While they share a common ancestor, Temporal does not use Cadence in its current software. Rather, Temporal is an evolution of Cadence that has diverged significantly to focus on improved developer experience, SDK design, and data handling, CTO and co-founder Fateev told conference attendees.

> “In a world where API calls fail, servers crash, and data becomes inconsistent, Temporal ensures that business processes … run to completion without manual intervention.”

“At its core, Temporal is a durable open-source execution framework that allows developers to write code that is inherently resilient,” Fateev said in his remarks. “In a world where API calls fail, servers crash, and data becomes inconsistent, Temporal ensures that business processes — from simple transactions to complex AI agent lifecycles — run to completion without manual intervention.

“It effectively creates a foundational layer that sits beneath your application logic, managing the hard work of building large-scale distributed systems, so your team doesn’t have to.”

## **Cloud and serverless options**

In addition to its frontline server-based product, Temporal offers a consumption-based [SaaS hosting service for backend clusters](https://temporal.io/cloud). The company guarantees full compatibility between the open-source model and the cloud versions. This reflects the company’s belief that every engineer should have access to the tools needed for successful, reliable code.

[Temporal’s Serverless Workers](https://docs.temporal.io/) enable users to run standard Temporal Workers on serverless compute platforms such as AWS Lambda. There are no servers to provision, no clusters to scale, and no idle compute to pay for, Fateev said. Temporal invokes the Workers when tasks arrive, and the Worker shuts down when the tasks are done.

“**Temporal** has made a set of strategic decisions to support our users’ ability to effectively manage and scale their agentic workflows,” said [Preeti Somal](https://www.linkedin.com/in/preeti-somal-131890/), Senior VP of Engineering at Temporal. “Temporal is already foundational to AI workflows, but we understand the importance of investing in it to make better products and to support our customers. We would like to demonstrate our feature launches, and partnerships are not random, but they will change the way that developers experience Durable Execution.”

## **Example of a key use case**

At the conference, [Tom Wheeler](https://www.linkedin.com/in/tomwheelerstl/), principal developer advocate at Temporal, offered a fictional use case based on real-life users to explain how this works:

* **Meridian Global**, a major retailer, faced an operational nightmare immediately after acquiring **Grafton Direct**. Grafton’s order management system (OMS) was fundamentally broken, characterized by a 7% failure rate across all orders, instances of double-charging customers, endless package delays, and a flood of complaints on social media. The crisis was compounded when Grafton’s burned-out engineering team resigned before the deal closed, leaving behind an undocumented, complex tangle of technical debt.
* Doug and Naomi began a two-day deep dive. Doug investigated the system’s internal workings, finding that logic for application check-pointing, state recovery, and retries was “woven all throughout the code base,” making the business logic hard to follow. He discovered critical bugs, such as inventory reserved early in the order process never being released if the system crashed, and faulty retry logic that triggered rate limits or silently swallowed exceptions.

Naomi approached the system externally, placing test orders to map out the exact business requirements. She documented the complex, seven-step order flow:

1. **Validation:** Verify completeness and use AI to check for suspicious activity.
2. **Reserve Inventory:** Reserve items so they are not sold to others.
3. **Charge Customer:** A complex step involving checks for credit card fraud (leading to immediate cancellation) or non-fraud declines (giving the customer 24 hours to provide a new form of payment).
4. **Request Fulfillment:** An asynchronous step notifying the warehouse to pack and select shipping.
5. **Shipment Confirmation:** Notifying the driver to pick up.
6. **Delivery Confirmation:** The driver marks the package as delivered.
7. **Order Completion:** The order remains open for 30 days after delivery for returns, then is marked closed.

They concluded that the system’s complexity was the problem, relying on proprietary home-grown retry logic, multiple message queues, database polling, and unreliable nightly Cron jobs. As Doug noted, crashes often caused the database and queues to get out of sync, leading to lost payloads or repeated retries, which resulted in customers being charged multiple times.

## **Implementation of Temporal**

Naomi met Elena, a Solutions Architect at Temporal. Elena introduced them to Temporal, a durable execution platform designed to handle the exact problems they were facing.

Key concepts and primitives that would solve Meridian’s problems included:

* **Workflows:** Provide crash-proof, durable execution, eliminating the need for manual checkpointing and state persistence logic.
* **Activities:** Used for calling external systems (like databases or microservices) and include built-in, fault-tolerant support for retries and timeouts.
* **Durable Timers:** Allow execution to be paused for arbitrary durations (seconds, days, or years), solving the 24-hour payment window and the 30-day return-closing problem and replacing the existing but unreliable Cron job.
* **Queries:** Enable external systems to retrieve the current state of a running workflow.
* **Signals:** Allow external systems (such as the shipping clerk’s app or the delivery driver’s app) to change the workflow state in human-in-the-loop scenarios.

Doug and Naomi quickly built a proof of concept (PoC). Their tests confirmed durable execution: killing agentic workers mid-execution did not cause data loss or duplicated work, such as double-charging. When they simulated an outage of the payment service, the workflow automatically paused, retried until the service was restored, and then resumed from the exact point of failure.

> “Within days, the system was handling five times Grafton’s prior peak volume without losing a single order.”

Impressed by the PoC, they deployed a few dozen workers to their Kubernetes cluster. Within days, the system was handling five times Grafton’s prior peak volume without losing a single order. Doug was particularly impressed with the simplicity of the code, noting that the workflow code “reads like a spec.”

They presented their recommendation to Alex: replace the old system with the new one built on Temporal. To meet the tight deadline, they opted to use Temporal Cloud, the managed service, for rapid scaling.

The new OMS was rolled out incrementally and was handling 100% of orders by the following Thursday, resulting in “zero orders lost [and] zero customer complaints.” When Black Friday arrived, the system smoothly handled a volume nearly five times Grafton’s former peak.

The project concluded with Jane announcing that Meridian would replace its own legacy order management system with the one built by Doug and Naomi. They had eliminated significant infrastructure and complexity, proving that Temporal delivers the necessary building blocks to simplify modern applications.

## **The Enterprise Platform: Connecting the dots**

The real power of Temporal lies in its ability to link disparate applications, agents, and tools into a single, cohesive enterprise platform. Through protocols such as Nexus, Temporal enables long-running operations to communicate reliably across different systems. This enables end-to-end platforms where static workflows, autonomous agents, and data transformations work smoothly together.

For the business leader, Temporal represents a “future-proof” investment. It does not lock users into specific libraries or frameworks. Instead, it provides the underlying layer that allows your organization to move fast, make bold technology choices, and adapt to change without fearing the structural integrity of your applications.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)