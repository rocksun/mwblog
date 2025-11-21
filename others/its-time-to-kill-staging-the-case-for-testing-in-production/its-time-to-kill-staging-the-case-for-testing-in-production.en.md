Staging has always been a necessary evil. New approaches to isolation and on-demand sandboxes have finally made it just plain evil.

For decades, the staging environment has been a fixture of software development. And for just as long, it has been hated by developers everywhere. It’s the proverbial traffic jam that every developer is forced to sit in just to get their work validated.

Yet staging is no longer necessary; its time has come and gone. Newer [isolation methods](https://thenewstack.io/smart-ephemeral-environments-share-more-copy-less/) enable developers to test safely in live environments, providing fast, high-fidelity feedback that is impossible to achieve in a staging environment.

It is time to kill your staging environment.

## The Problem We All Know

Staging environments make sense, in theory. We must test code in a production-like environment before we ship to production. Anything else would be madness.

But the cure has become its own disease. In any organization with more than a handful of microservices, the staging environment inevitably becomes a wasteland of developer pain and burned cash.

* **It’s a bottleneck:** When 50 developers merge code, staging becomes a shared queue. Tests fail not because of bad code, but because another developer deployed a conflicting change.
* **It’s not production:** We call it “production-like,” but it never has the same data scale, traffic patterns or identity and access management (IAM) policies. This fidelity gap is where dangerous bugs hide.
* **It kills velocity:** Commit code, wait for CI, wait for a deploy slot, run a 40-minute test suite. This multihour cycle destroys flow state.
* **Nobody maintains it:** Teams treat it as a dumping ground for unstable builds, further diverging from production.

We have accepted this broken workflow for 20 years. We believed it was the only way.

## **From Environment Isolation To Request Isolation**

Staging exists because of the assumption that testing must be isolated at the environment level. To test a new version of the payment service, you must deploy it to an environment that also contains a cart service, user service and auth service.

This assumption is outdated and obsolete.

The new model is request-level isolation. Instead of cloning an entire environment, you spin up only the service you’re changing. This model is enabled by Kubernetes-native platforms that provide on-demand sandboxes for every request.

Here is how it works:

* A new service version is spun up in an on-demand, isolated “sandbox.”
* When a test request is sent (tagged with a unique header), it is routed to the sandboxed service.
* As that service calls its dependencies, those calls are routed back to the stable, baseline services in production.
* The [test request remains isolated](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/) as it travels through the stack, while all other traffic flows normally.

With this approach, you get high-fidelity testing (real dependencies, real network policies) without the downsides of shared environments (no collisions, no queues, dramatically lower cost).

Request-level isolation can be implemented into a traditional local > staging > production deployment flow to improve it, eliminating contention and long waits for a CI pipeline. But its real power lies in bypassing the need for staging altogether, enabling testing in production.

## **The Safety Model**

Testing in production sounds dangerous. It’s not when you have the right guardrails.

* **Strict data isolation is critical.** The biggest concern is that a sandboxed service could corrupt data in other services. The solution is simple. The same routing header that isolates test traffic also routes database operations to separate test databases. For example, when a test request flows through the system, each service recognizes the test context and directs all database writes to isolated test data stores, completely separate from production databases. Test users interact only with test data. Production data remains untouched.
* **Multitenancy provides the foundation.** Virtual private network (VPN) restrictions ensure test traffic originates only from authorized internal networks. Audit logs track every sandbox session for compliance.
* **Request routing provides blast radius control.** Your sandbox is isolated at the request level. Your colleagues’ work is unaffected. Production traffic flows normally.
* **Progressive rollout remains essential.** Sandboxes handle preproduction validation, but you still use canary deployments, feature flags and observability to safely roll out to real users.

## **Answering the Hard Questions**

Testing in production is the logical evolution of the movement to shift testing left. But making such a foundational change to your CI/CD pipeline naturally brings up some critical questions:

* **“How do you guarantee test traffic doesn’t corrupt production data?”** Test writes are isolated. The isolation header redirects all database writes to ephemeral, nonproduction data stores that are destroyed after the test. Production data is never touched.
* **“What about the blast radius? How do you stop a bad test from DDoSing a downstream service?”** [Sandboxes are “shadow” deployments](https://thenewstack.io/microservice-integration-testing-a-pain-try-shadow-testing/) built with guardrails like circuit breakers and network policies. A buggy test with runaway network requests is automatically throttled and contained, preventing it from overwhelming baseline services or affecting other users.
* **“This sounds fine for simple APIs, but what about Kafka or gRPC?”** The isolation model is protocol-agnostic. The isolation header is propagated over gRPC or as a [Kafka message header](https://www.signadot.com/blog/shift-left-meets-kafka-testing-event-driven-microservices). A sandboxed consumer, for example, reads from the main topic but only processes messages with its unique sandbox ID.
* **“What about compliance and audit requirements?”** This model is more auditable. Every sandbox is tied to a specific user and a pull request/dev session. [All test traffic is explicitly tagged with a sandbox](https://thenewstack.io/sandbox-testing-the-devex-game-changer-for-microservices/) ID and user identity, creating a granular audit log that is far superior to a shared staging environment.

Addressing these and making the shift to testing in production will inevitably involve some upfront engineering investment. However, the return on investment for that work is not just the savings from eliminating the direct infrastructure costs of your staging. It’s also a better developer experience, faster product delivery and fewer opportunities are lost to competitors that can iterate and ship faster than you.

## **It’s Time To Let Go**

Eliminating staging may sound like a pipe dream, but several prominent cloud native teams like [DoorDash](https://careersatdoordash.com/blog/moving-e2e-testing-into-production-with-multi-tenancy-for-increased-speed-and-reliability/) and [Uber](https://www.uber.com/blog/shifting-e2e-testing-left/) have already made the shift left to testing in production. Driven by their highly complex [microservice stacks and a need to get better testing](https://thenewstack.io/why-microservice-environments-break-lack-of-unification/) fidelity, they are also realizing huge infrastructure cost savings.

Teams like these deprecating their staging environments to test in production represent a broader trend: the rejection of approximation in favor of reality. Staging environments are [artifacts of an era when duplicating infrastructure](https://thenewstack.io/why-duplicating-environments-for-microservices-backfires/) was a harder problem to solve than coordinating humans around shared resources.

That era is ending.

The future isn’t about building better approximations of production or optimizing your CI pipeline. It’s about adopting an entirely new paradigm. The teams taking this step aren’t just moving faster and cutting costs. They’re also shipping more reliable code.

It’s time to kill your staging environment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)