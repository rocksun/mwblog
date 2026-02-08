These days, malicious actors succeed not by breaking systems, but by [blending into them](https://thenewstack.io/how-ml-defense-projects-change-approaches-to-data-security/). Increasingly, the intruder looks like a legitimate workload. The alarm doesn’t ring, until it’s too late.

Take, for instance, the recently identified [RustyWater implant](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant) associated with the Muddy Water advanced persistent threat. After RustyWater enters a system, it persists quietly. It avoids the obvious paths for escalating the threat, and keeps its interactions to a minimum, the better to stay undetected. It doesn’t generate noticeable side effects, so monitoring software can’t easily catch it. From the system’s perspective, it’s business as usual.

With greater frequency, this is how system compromises happen. Attackers have adapted as infrastructure became more observable. Maintaining visible, normal behavior has become the dominant strategy.

## **When Visibility Became the Default Response**

As systems expanded, changed dynamically and crossed organizational boundaries, end-to-end reasoning became impractical. The industry responded by investing deeply in visibility across every available surface. Logging pipelines, metrics systems, tracing frameworks, dashboards, detectors and incident reconstruction tooling became standard.

Over time, the ability to explain an incident in detail became a marker of operational maturity. Teams felt progress when they could describe timelines, triggers and sequences with confidence – even when the conditions that enabled the incident remained unchanged.

Visibility began to function as a substitute for containment rather than a complement to it. Understanding events increasingly felt sufficient, partly because visibility could be improved continuously without structural change.

## **Authority, Not Entry, Is the Objective**

In contemporary infrastructure, execution itself is no longer unusual or difficult to obtain. Code runs constantly across services, pipelines, controllers and long-lived agents. The more consequential question is what the system assumes once execution is allowed. Permitting execution implicitly grants legitimacy within the system’s trust model. That influence increases as execution occurs closer to coordination layers that shape global state.

Once code executes successfully, the attacker’s challenge changes in character. Initial access focuses on achieving execution somewhere within the environment. Long-term impact depends on what that execution can influence over time. Modern systems blur this distinction because authority is often inherited rather than assigned deliberately.

Code running within build infrastructure can influence artifact creation and distribution paths. Compromising a CI environment does not require breaking isolation to cause widespread impact. Build pipelines determine what software is produced, trusted and deployed downstream. Small changes to dependency resolution or artifact handling can propagate broadly. The authority comes from the pipeline’s position in the system, not the sophistication of the code.

Cloud identity compromises often involve no malware at all. Possession of credentials or overly broad roles allows infrastructure creation and modification. From the system’s perspective, these actions are legitimate and authorized.

Control-plane manipulation follows the same logic. Orchestration systems are designed to converge reality toward the declared desired state. Influencing that declared state allows the platform to perform harmful actions on behalf of the attacker. No escape is required when the system itself executes the changes.

Across these scenarios, initial entry is secondary. Placement within [trusted system roles determines authority](https://thenewstack.io/what-do-authentication-and-authorization-mean-in-zero-trust/) accumulation. Impact results from operating within the trust model, rather than overtly violating it.

## **The Shared Substrate Trade-off**

Modern environments deploy admission controls, runtime enforcement, segmentation, identity systems and signing mechanisms. These controls meaningfully reduce risk and block many attack classes outright. What they tend to share is their position above the execution substrate. They assume execution is permitted before evaluating behavior. Actions are constrained, monitored, and reacted to after authority has already been granted.

Shared kernels, shared control planes and shared infrastructure were chosen deliberately. They improve efficiency, performance and operational simplicity at scale. Resource utilization becomes tractable, and scheduling overhead is reduced.

The trade-off is implicit and shared authority. In shared-kernel environments, scheduling, memory pressure and filesystem semantics converge. Namespaces and cgroups constrain behavior, but the kernel remains globally trusted. Containment, therefore, relies on early detection and fast response – an assumption held better when attacks were noisy and time-constrained. It is less reliable when attackers are patient and align with expected behavior.

## **Making Authority Explicit**

Some [architectural approaches respond by limiting default authority](https://thenewstack.io/5-factors-to-weigh-when-building-authorization-architecture/) rather than improving observation. They assume eventual compromise and focus on restricting propagation. Additional boundaries must be crossed before authority can expand. Systems like Edera follow this philosophy, though the specific implementation is secondary. The central idea treats containment as a primary [design goal rather than a side effect](https://thenewstack.io/how-to-design-effective-access-control-for-generative-ai/).

None of this suggests that earlier architectural decisions were misguided. Visibility addressed the most urgent problem of its time, which was uncertainty. It made complex systems understandable and operable. What has changed is the way attackers behave within those systems. Understanding events does not, by itself, limit how far execution is allowed to propagate. As systems grow and authority concentrates, the [gap between explanation and containment](https://thenewstack.io/hardened-containers-arent-enough-the-runtime-security-gap/) becomes harder to ignore.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/1eadc36b-cropped-486b6ae8-image1-600x600.jpg)

Kavi Daula is vice president of engineering at Edera. She brings deep expertise in container security, Kubernetes and open source operating systems. Previously, she worked at Geico leading containers, operating system and language runtime initiatives. Before that she led AWS...

Read more from Kavi Daula](https://thenewstack.io/author/kavi-daula/)