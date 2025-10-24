The modern cloud native world has created a fundamental clash of cultures. On one side, you have the developers, acting like race car drivers who live for speed. Their goal is to innovate, to ship new code and features as fast as possible, pushing the limits of velocity.

On the other side, you have the platform engineers, the air traffic controllers of the digital sky. Their singular mission is to maintain safety, stability and control, ensuring every workload is secure and compliant.

Both roles are vital to the business, but when their goals might collide — autonomy versus control — it can create a deep and costly friction. This isn’t about one side being wrong; it’s about two essential functions working at cross-purposes, a disconnect that slows everything down.

## The Unspoken Burdens of Cloud Native Development

A developer’s core desire is simple: to ship code. But this seemingly straightforward goal is a complex journey fraught with roadblocks and a number of points of friction. For the race car driver, these are the equivalent of sudden chicanes and pit stops that constantly disrupt the pursuit of velocity. Each of these delays the application delivery and requires a different solution.

First is access friction. Imagine a developer needing to test their new application in a Kubernetes cluster. Instead of simply spinning one up, they have to file a ticket, wait for approvals and go back and forth with the platform team. Multiply this across dozens of developers, and the platform engineers are suddenly buried under a mountain of repetitive requests. This turns developers into a bottlenecked ticketing system, frustrating both sides and distracting from more strategic work.

Next, there is delivery friction. This comes from the delays caused by manual handoffs, slow approvals and inconsistent processes. A new feature might require a ticket for resources, followed by a wait for a security review and then a code review. Because these steps are handled by different people, inconsistencies are often introduced, and by the time the code finally ships, the business has lost valuable time. This isn’t a minor slowdown; it’s a competitive disadvantage where the race car is stuck in the pits while others are on the track. When competitors are releasing multiple times a day, every delay becomes a serious competitive disadvantage.

Finally, we have cognitive friction, which is caused by the complexity of the environment itself. Developers are experts at building business logic and coding in languages like Go or  [Java](https://thenewstack.io/introduction-to-java-programming-language/), but they often don’t want to become masters of YAML configurations, Helm charts or intricate networking. When they are forced to navigate this complexity, their focus shifts from creating value to wrestling with infrastructure. This “plumbing” drains their mental energy, slows down delivery and can lead to costly mistakes.

## Two Essential Functions Working at Cross-Purposes

While developers are focused on the finish line, the [platform engineer is managing](https://thenewstack.io/how-platform-engineering-helps-manage-innovation-responsibly/) the entire ecosystem. Their job is not just about building and maintaining clusters; it’s about juggling an ever-growing list of responsibilities. Like the air traffic controller, they must keep a close eye on everything to ensure it runs safely and predictably.

They are the builder who creates the clusters and CI/CD pipelines, ensuring the infrastructure is reliable and performant. They are also the guardian, responsible for the security and compliance of the entire platform, from understanding digital sovereignty regulations to enforcing policies that prevent risks.

On top of that, they are a financial manager, with the unenviable task of optimizing cloud costs and making sure the entire system is efficient and sustainable.

And they are the strategist, always looking ahead to new technologies and evolving the platform to keep the business competitive.

But no matter how skilled the controller is, they can’t manage everything on their own. The reality is that platform engineers are vastly outnumbered. The typical ratio is about one platform engineer for every 10 developers. In large enterprises, that number can skyrocket to one for every 200. This imbalance creates an unsustainable situation where every developer request — from a simple access ticket to a complex troubleshooting issue — piles up, leaving [platform engineers buried](https://thenewstack.io/platform-teams-start-small-to-win-big/) under a flood of small requests. They are left with little to no time for the strategic work that is so critical to the business.

## The Golden Path to Collaboration

The concept of a golden path has been introduced in the industry as a powerful way to empower developers without sacrificing control. For the race car driver, it’s a clear, well-paved track with no sudden roadblocks. For the air traffic controller, it’s a standardized flight plan that ensures every aircraft lands safely. It’s a well-defined, standardized and secure route that cuts through the maze of friction developers face.

But while the idea is a good start, it’s not enough. A platform vision must include a comprehensive set of capabilities to truly bridge the divide. First, self-service sandboxes must be available. Developers need the ability to spin up lightweight, local environments and isolated virtual clusters on demand. This gives them the freedom to experiment and even break things safely, without ever risking production.

Curated base images are also a core component. Developers shouldn’t have to wonder if a base [image they pull from the internet contains vulnerabilities](https://thenewstack.io/container-image-fault-lines-are-being-exposed/). Instead, platform teams should offer a secure and continuously maintained set of building blocks, allowing developers to start with a foundation that has near-zero vulnerabilities.

A curated set of trusted components, including open source applications, allows developers to start their projects with a solid foundation and enable a true “shift-left” security approach.

The path must also include built-in security. Security shouldn’t be a gate at the end of the pipeline. It must be embedded into the entire workflow from the start. By automatically applying policy enforcement and security guardrails, developers can move quickly with confidence, and [platform engineers can rest easy knowing](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/) every workload is protected.

Furthermore, automated, consistent deployments are non-negotiable. A golden path should use principles like GitOps to ensure zero-touch automation and zero-drift consistency. This eliminates manual, error-prone steps and frees up both developers and platform teams from the tedium of deployments.

Finally, the path must provide guided observability. Instead of drowning developers in a flood of dashboards, the platform should offer clear, correlated data and guided troubleshooting. This empowers developers to fix their own issues quickly, without needing to become experts in the underlying infrastructure.

## Conclusion: The Future Is a Shared Path

The core of this new approach is finding a balance between speed and control, allowing the race car driver to accelerate with confidence and the air traffic controller to guide them securely. By implementing a comprehensive golden path, we can move beyond simply managing a fragile divide and instead build a unified vision where both developers and platform engineers can succeed. It’s a future where their goals are no longer at odds, but in perfect sync.

* For developers, the golden path delivers the autonomy, speed and freedom they need to innovate. They can focus on building value, not fighting infrastructure.
* For platform engineers, it provides the control, peace of mind and time they need to evolve the platform strategically. They become enablers, not gatekeepers. The future of [cloud native development](https://thenewstack.io/cloud-native/ "cloud native development") isn’t about one side winning; it’s about building a path where everyone wins.

Building this shared path requires a fundamental change in the way organizations think about platform tooling. For a business to be truly resilient and flexible, its [platforms must be rooted in open source](https://thenewstack.io/building-an-idp-with-help-from-the-open-source-cnoe-framework/), providing the freedom to innovate without vendor lock-in.

By embracing an open source golden path, companies can create a robust and reliable foundation that is not only faster and more secure but also truly sustainable. We’d love to learn about your approaches to bridging the DevOps divide and swap stories at the SUSE booth (110) at KubeCon + CloudNativeCon North America.

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia.* [*Register now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/32d96169-cropped-99730b59-jeroen-van-erp-600x600.jpeg)

Jeroen van Erp is a technology evangelist at SUSE, specializing in the observability platform. With a rich background spanning engineering, architecture and product management, Jeroen brings over a decade of experience in the DevOps space. Before joining SUSE, he played...

Read more from Jeroen van Erp](https://thenewstack.io/author/jeroen-van-erp/)