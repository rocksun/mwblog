# Policy Engine Showdown - OPA vs. OpenFGA vs. Cedar
- Share:
Developers are faced with a wide array of choices when it comes to policy engines, languages, and standards. From OPA to Cedar, OpenFGA, and beyond, decision-making has become a complex task as developers seek tools that fit their unique use cases while scaling seamlessly.

At **KubeCon + CloudNativeCon NA 2024**, Gabriel L. Manor, VP of Developer Relations at Permit.io, brought together four talented engineers from leading policy engine teams for a panel discussion aimed to provide some clarity amidst the confusion.

*Watch the full panel discussion at **https://www.youtube.com/watch?v=AVA32aYObRE*
Dubbed the **“Policy Engines Showdown,”** this session was designed to help the audience make one of the most critical security decisions for modern application development: choosing a decision engine that fits their specific needs.

Joining Gabriel on the panel were:

**Andres Aguiar**, Director of Product at**Okta**, representing**OpenFGA**.**Omri Gazitt**, CEO of**Aserto**, introducing**Topaz**, built on OPA.**Pauline Jamin**, Staff Engineer at**Agicap**, bringing insights from the end-user perspective on OpenFGA.**Tyler Schade**, Distinguished Engineer at**GEICO**, and a core contributor to OPA.**Joy Scharmen**, Engineering Director at**StrongDM**, representing AWS’ Cedar.
Together, the panel explored the strengths, trade-offs, and unique capabilities of various policy engines. In Gabriel’s words:

"Policy engines, languages, and standards are everywhere, making it increasingly difficult to choose the right engine. In this panel, we’ll delve into how to select the best decision engine for your use case, the nuances of running multiple engines together, and scaling them effectively."

## Rules of the Showdown
At the heart of the **Policy Engines Showdown** was a simple goal: help developers navigate the complexity of policy engines by focusing on **trade-offs and practical insights, helping them to pick the one most suited for their implementation.**

The goal is not to declare a winner but rather to understand that every policy engine has strengths and weaknesses, and suitability depends largely on the specific use case.

"There is no winner. Everything in software comes with trade-offs—some solutions excel in one use case but may not fit another. We’re here to explore those differences and give you the tools to make the best decision for your needs."

While many of the panelists represented engines that could be considered competitors, the emphasis was on **collaboration** rather than rivalry. As Gabriel noted:

"This is a young ecosystem, and we’re all friends here. While the tools we represent may compete in some spaces, we meet regularly, exchange ideas, and ultimately want to create a space where everyone can win."

## Exploring the Policy Engines
Each participant presented a 30-second pitch for their respective policy engine, offering insights into their design philosophies, use cases, and strengths. Here’s what they had to say:

### OpenFGA: Relationship-Based Access Control Inspired by Zanzibar
Andres from Okta began by introducing **OpenFGA**, highlighting its foundation in [ Relationship-based Access Control (ReBAC)](https://www.permit.io/blog/what-is-rebac) and inspiration from

[white paper:](https://www.permit.io/blog/what-is-google-zanzibar)
**Google’s Zanzibar**"OpenFGA is a CNCF sandbox project originally built by Okta, now with contributions from Grafana Labs. It’s based on the concept of ReBAC, where permissions are defined based on relationships. This approach allows for highly scalable and flexible access control."

Andres also emphasized the **rich community and tooling** that make OpenFGA easy to adopt:

"With a large and growing community, we’ve built tools that make it simple for developers to integrate OpenFGA into their systems."

### Topaz: Speed and Flexibility on an OPA Foundation
Omri, CEO of Aserto, showcased **Topaz**, a policy engine built on [ Open Policy Agent (OPA)](https://www.permit.io/blog/introduction-to-opa) but tailored for application-level authorization. He emphasized Topaz’s

**performance, flexibility, and integration capabilities**:
"Topaz is fast—authorizations happen in under a millisecond, thanks to its caching architecture. It’s also flexible, supporting RBAC, ABAC, and ReBAC models by combining OPA’s strengths with a Zanzibar-inspired directory service."

### Cedar: Readability and Determinism from AWS Expertise
Joy of StrongDM spoke about [ Cedar](https://www.permit.io/blog/oss-aws-cedar-is-a-gamechanger-for-iam), a policy language and engine developed by AWS, emphasizing its

**readability, determinism**, and focus on access control.
"Cedar builds on AWS’s extensive IAM expertise, making it a highly readable and predictable policy language. Its analyzability is a standout feature, ensuring that policies do exactly what they’re supposed to."

Joy explained why Cedar works so well for platforms like StrongDM:

"We chose Cedar because it allows us to leverage our existing context and make lightning-fast, accurate decisions. It’s perfect for platforms where speed and determinism are critical."

### OPA: A General-Purpose Policy Engine
Tyler, a core contributor to **Open Policy Agent (OPA)**, pitched its **multipurpose capabilities** and flexibility.

"OPA is a general-purpose policy engine that can be used anywhere you need it. It’s domain-agnostic—feed it data and policies, and it returns decisions in JSON."

Tyler highlighted OPA’s widespread use across industries:

"OPA is popular for Kubernetes admission control, cloud compliance, and infrastructure as code. Its flexibility makes it a go-to for teams handling diverse policies in different contexts."

### Building on Top of Policy Engines with OPAL and Permit.io
Gabriel also highlighted the **Permit.io**** platform**, which provides a comprehensive solution for developers looking to integrate fine-grained authorization into their applications. Permit.io uses engines like OPA, OpenFGA, and Cedar, abstracting their complexities by offering easy-to-use tools for policy management (Like APIs, SDKs, and a no-code UI).

He also mentioned [ OPAL (Open Policy Administration Layer)](https://github.com/permitio/opal), an open-source project that enhances OPA, Cedar, and OpenFGA by automating real-time policy and data updates:

"OPAL synchronizes policies and data seamlessly, bridging the gap between your policy engine and the dynamic nature of your application’s environment. It’s a critical tool for developers scaling policy-as-code solutions."

Permit.io, combined with tools like OPAL, enables developers to leverage these engines effectively for fine-grained, scalable authorization, simplifying their adoption and integration.

With the different engines up for comparison described, let’s explore the various criteria used to compare these policy engines.

## Policy-as-Code vs. Policy-as-Data
One key distinction between policy engines is [the difference between policy-driven and data-driven engines](https://www.permit.io/blog/zanzibar-vs-opa). While all policy engines rely on a combination of policy and data to make decisions, their approaches to balancing these elements can vary significantly.

### Zanzibar: Combining Policy Rules with Relationship-Based Data
Andres provided insights into the **Zanzibar-inspired model** used by **OpenFGA**. This approach relies heavily on **data relationships** to define and enforce permissions:

"In the Zanzibar approach, you define an authorization model—rules like ‘Only the owner of a document can delete it.’ This is the policy, written in code. However, the specific relationships, like who the owners are, live in the data."

He explained how this combination allows flexibility and scalability:

"It’s a hybrid model. Policies define the rules, while relationships in the data instantiate those rules. For example, in role-based access control (RBAC), the fact that a group has permissions is policy, while the members of that group are data."

### Cedar: A Policy-Focused Engine with Ephemeral Data
For Joy, Cedar’s emphasis on **policy over data** was a key differentiator:

"Cedar is very policy-driven. Data flows through the system as ephemeral input, without requiring a predefined data model."

She highlighted why this approach works well for a platform like StrongDM:

"We’re a platform, so we can’t predict the structure of our customers’ data. Cedar lets us focus on writing clear, efficient policies while using only the data we need at decision time."

This policy-first design simplifies integration and ensures fast, deterministic decisions.

### OPA: Supporting Both Approaches
Tyler explained how **Open Policy Agent (OPA)** allows developers to use either a policy-driven or data-driven approach—or a combination of the two.

"OPA combines policy and data into bundles that can be preloaded into the system. Alternatively, you can fetch data during policy evaluation from an external source or include it as part of the input document."

This flexibility allows OPA to adapt to different architectural needs:

"Most users end up using a combination—some preloaded data, some fetched dynamically, and some included with the request. OPA’s flexibility lets you choose the best approach for your specific use case."

### Balancing Policy and Data for Your Use Case
Choosing between policy-driven and data-driven approaches depends heavily on the use case. For systems with complex relationships and frequent data updates, a data-driven engine like Zanzibar or OpenFGA may offer advantages. In contrast, a policy-driven engine like Cedar simplifies integration and ensures deterministic behavior. Engines like OPA, which support both approaches, provide maximum flexibility but may require more configuration.

As Gabriel summarized:

"Understanding whether your system is policy-driven or data-driven is critical. Some engines lean heavily on policy, while others rely on data to define relationships. Choosing the right balance can make all the difference in performance and ease of use."

This distinction set the stage for the next discussion: **centralization vs. decentralization** in deploying policy engines.

## Centralization vs. Decentralization
The debate between **centralized** and **decentralized** policy engine deployments is another key aspect to inspect when making the choice between different policy engines. Each approach has trade-offs in terms of performance, consistency, and complexity, all of which align differently with specific use cases.

### Centralized: A Unified Source of Truth
Pauline began by explaining why her company chose a centralized approach for managing authorization:

"At the start, our authorization logic was scattered across services. We moved from a monolith to microservices, but there wasn’t a unified vision. I couldn’t confidently say whether permissions were being evaluated consistently across all services."

She emphasized how centralization brought clarity and consistency:

"We chose a centralized system so every service could ask the same permission question and always get the same answer. The logic is coded in one place, which ensures reliability."

However, Pauline also acknowledged the challenges of centralization:

"When everything relies on a single centralized system, it has to be very fast because all authorization calls depend on it."

### Decentralized: Minimizing Latency with Localized Decisions
Omri highlighted the performance benefits of decentralizing authorization decisions:

"If your latency budget is extremely tight—like one millisecond—you need to deploy the authorizer as a sidecar. This eliminates the overhead of calling a centralized service and ensures the fastest response time possible."

He framed this as a hybrid approach:

"Authorize locally but manage centrally. You deploy the authorizer close to the workload to minimize latency while keeping the policies and data managed in a centralized control plane."

### Hybrid Models: Balancing the Best of Both Worlds
Gabriel explained how hybrid models can provide a balance between centralization and decentralization:

"With hybrid solutions like Permit.io or Topaz, you can centralize the control plane for policies but decentralize the data plane. This way, you get centralized policy management without sacrificing performance."

He also mentioned other examples, such as OpenFGA’s multi-store option and the open-source [Cedar Agent](https://github.com/permitio/cedar-agent) from Permit.io, which allows Cedar to run statefully in decentralized environments.

**Tailoring Deployment to Your Use Case**
The panelists agreed that deployment models should be guided by the needs of the application. As Joy noted:

"For some systems, centralization simplifies things, but it’s not always feasible. If latency or fault tolerance is critical, decentralized deployments might be a better fit."

Gabriel summed up the discussion with a practical perspective:

"The right model depends on your latency budget, consistency requirements, and how critical it is for your system to stay operational in case of a failure."

This leads us to the next discussion point: **stateful vs. stateless policy engines**, where we explore how data storage and retrieval impact performance and complexity.

## Stateful vs. Stateless Engines
One key consideration in choosing a policy engine is whether to adopt a **stateful** or **stateless** approach. Each has implications for how data is stored, retrieved, and managed, as well as for how it impacts performance and system complexity.

### Stateful: Centralizing Data for Efficiency
Andres described how stateful systems, like those inspired by Zanzibar, rely on a centralized database for storing permissions and relationships:

"In a Zanzibar model, you centralize all the data needed to make authorization decisions. Once the data is there, performing a permission check is as simple as calling an API."

He also acknowledged the challenge of synchronizing data into this centralized system:

"Getting the data into the system is the hard part. You need to handle event-driven updates, CDC streams, or other synchronization patterns to keep everything current."

Pauline added her perspective on the benefits of this approach:

"For us, the big win was eliminating the need to duplicate data retrieval logic across all our services. Now, it’s one API call, and we get everything we need, fast and reliably."

### Stateless: Lightweight and Agile
Joy explained how Cedar’s **stateless approach** allows for simpler integrations and faster decisions:

"Cedar doesn’t rely on a centralized data model. Instead, data flows through the system as part of the request, which keeps the engine lightweight and avoids the need for complex synchronization."

This stateless design ensures that the focus remains on clear, easily verifiable policies:

"With Cedar, you’re not tied to maintaining a large database of permissions. The data comes in as needed, and the engine makes decisions based on that ephemeral context."

### Balancing Both Approaches
Tyler highlighted how OPA’s flexibility allows it to operate in both stateful and stateless modes:

"OPA supports preloading data into the system through bundles, fetching data during policy evaluation, or including it in the request. This means you can choose the level of statefulness based on your architecture’s needs."

This flexibility enables developers to strike a balance:

"If you want the simplicity of stateless decisions, you can rely on request data. But if you need the efficiency of preloaded context, OPA lets you preload data bundles to minimize latency."

The choice between stateful and stateless depends on the system’s requirements for data synchronization, scalability, and consistency. As Gabriel put it:

"Stateful systems shine when you need a single source of truth for complex relationships, but stateless engines can be a better fit when agility and simplicity are your priorities."

This leads us to the next discussion point: multipurpose vs. single-purpose policy engines, where we examine the trade-offs between flexibility and focus in policy engine design.

## Multipurpose vs. Single-Purpose Engines
Another important differentiating factor between policy engines is the difference between **multipurpose engines** capable of handling a variety of use cases and a **single-purpose engine** optimized for a specific domain. Here are some of the trade-offs between flexibility and focus, highlighting how these approaches affect developer workflows.

### Multipurpose: Flexibility Across Use Cases
Tyler introduced OPA as a prime example of a multipurpose policy engine:

"OPA is incredibly flexible and can be used in a wide range of scenarios. Whether it’s Kubernetes admission control, cloud compliance, or CI/CD pipelines, you can deploy OPA wherever you need it."

He emphasized how OPA consolidates tooling across the stack:

"Fragmented tooling doesn’t help developers. With OPA, you have a unified tool that supports multiple use cases, reducing the learning curve and simplifying maintenance."

However, Tyler also acknowledged the responsibility that comes with this flexibility:

"With great power comes great responsibility, and developers need to carefully plan how and where to deploy OPA to avoid unnecessary complexity."

### Single-Purpose: Streamlined and Specialized
Joy highlighted the benefits of Cedar’s single-purpose design, which focuses specifically on access control:

"Cedar’s strength lies in its readability and determinism. It’s optimized for scenarios where clarity and predictable outcomes are critical, like

[role-based access control (RBAC)]."
This focus on access control makes Cedar an attractive choice for developer teams looking for a straightforward, purpose-built solution:

"You don’t have to worry about configuring it for unrelated use cases. Cedar does one thing and does it very well."

### Blurring the Lines
Omri shared how Topaz builds on OPA’s multipurpose foundation but tailors it for application authorization:

"Topaz takes the flexibility of OPA and combines it with opinionated data structures inspired by Zanzibar. This allows developers to benefit from OPA’s ecosystem while leveraging a more specialized approach for authorization."

He also mentioned the value of contributing improvements back to OPA’s ecosystem:

"We believe in the strength of multipurpose engines like OPA, which is why we’ve contributed enhancements, like bundle support, back upstream."

### Choosing the Right Tool for the Job
The decision between multipurpose and single-purpose engines depends on the developer’s needs. As Gabriel summarized:

"A multipurpose engine like OPA is great for developers who want a unified tool to handle diverse policies across their stack. But if your focus is solely on access control, a single-purpose engine like Cedar or OpenFGA might save time and reduce complexity."

Gabriel also noted how the **Permit.io** platform can be used to take the hassle out of adopting multipurpose or hybrid engines. By providing a developer-friendly abstraction over policy engines like OPA, Cedar, and OpenFGA, Permit.io simplifies integration and management, letting teams focus on building secure and scalable applications.

"Permit.io bridges the gap between multipurpose and single-purpose engines by offering SDKs, APIs, and a unified platform. Developers can implement fine-grained authorization without needing deep expertise in policy languages or extensive configuration."

Permit.io allows developers to enjoy the flexibility of multipurpose engines while achieving the focus and clarity of specialized tools—all without the headaches typically associated with hybrid adoption.

This leads us to the next discussion point: scalability, performance, and the challenges of adoption. Here, we examine how policy engines handle growth and developer onboarding.

## Scalability, Performance, and Adoption Curve
Scalability, performance, and ease of adoption are critical to evaluating policy engines. Developers must assess how well an engine can handle increasing complexity and how quickly they can onboard their teams.

### Managing Policies and Data at Scale
As policy engines grow to handle more complex systems, scalability becomes a major concern. Andres highlighted how OpenFGA addresses this with its centralized data model:

"OpenFGA’s approach to storing permissions in a single database makes it easier to manage at scale. Once you have the data in the system, querying permissions is fast and efficient, even as the number of users or resources grows."

However, he also cautioned that synchronizing data into this centralized model can be challenging:

"Scaling isn’t just about handling more requests—it’s about ensuring the data stays consistent and up-to-date. Developers need to plan for event-driven updates or CDC streams to avoid bottlenecks."

### Performance: Balancing Speed and Complexity
Performance is a top priority for many developers, especially when authorization decisions need to be made in milliseconds.

High performance in policy engines often relies on efficient mechanisms such as caching. These optimizations enable authorization decisions to be made in under a millisecond, which is crucial for applications where even slight delays can negatively impact the user experience.

Joy added how Cedar’s focus on deterministic policies enhances both performance and reliability:

"Cedar allows us to process decisions quickly without sacrificing accuracy. By keeping the data ephemeral and focusing on policy determinism, Cedar strikes a balance between speed and simplicity."

### Adoption: Overcoming the Learning Curve
For many developers, the biggest challenge isn’t scalability or performance—it’s the [learning curve of adopting a new tool or language](https://www.permit.io/blog/no-one-wants-to-write-rego). Tyler acknowledged this for OPA and its policy language, Rego:

"Rego isn’t YAML. It’s a declarative language with loops, conditions, and functions, so it requires a bit of time to learn. When I first started using it, it took me about 30 to 40 hours to really get the hang of it."

He reassured developers that the ecosystem around OPA has made significant improvements:

"The tooling has come a long way. Tools like Rego linting and the

[upcoming V1 language standard]will make it easier for developers to onboard quickly."
Joy contrasted this with Cedar’s more intuitive design:

"Cedar’s readability is one of its strongest features. You can look at a policy and immediately understand it, which lowers the barrier to entry for teams new to policy engines."

### Choosing for the Long Term
Addressing scalability and performance requires thoughtful planning, but adoption challenges are equally important to consider. As Gabriel summarized:

"A policy engine is only as good as your team’s ability to use it. Balancing the technical strengths of an engine with its usability and learning curve is crucial for long-term success."

This brings us to the final discussion: testing, verification, maintaining correctness, and best practices for ensuring policies work as intended.

## Testing, Verification, and Correctness
Ensuring policies work as intended is a critical part of adopting a policy engine. Developers need reliable methods to test their policies, verify their correctness, and maintain consistency across deployments. The ability to catch errors early and validate changes before deployment is key to building trust in the system.

### Testing Policies with Assertion Suites
One of the most effective ways to ensure policies behave as expected is through automated testing. By leveraging assertion suites, developers can simulate different scenarios and verify that policies produce the correct outcomes. As Omri described it:

"A good approach is to have a test suite that puts a policy or model through its paces". "Before every check-in, you run the verification suite to ensure everything works as intended."

Testing during CI/CD workflows ensures that policies are correct before they are deployed, reducing the risk of errors in production.

### Verification Tools for Policy Languages
Some policy engines provide built-in tools for verifying policies and ensuring correctness. For example, deterministic engines simplify validation by guaranteeing that the same inputs always yield predictable results.

Other engines offer advanced verification capabilities using formal methods. Tools that analyze policies for logical consistency or allow for the simulation of edge cases can help developers catch complex errors that might otherwise go unnoticed. Joy highlighted Cedar’s approach to verification:

"Cedar uses verification techniques that let you ensure every possible decision is accounted for. It gives developers confidence in the behavior of their policies."

### Logging and Debugging for Correctness
Decision logging is another valuable feature for maintaining correctness. By recording the data and policies used in each decision, developers can troubleshoot errors and even replay past scenarios to identify what went wrong. Tyler described its importance:

"Decision logs let you see exactly what happened and why a particular decision was made. It’s an invaluable tool for debugging and maintaining trust in the system."

This capability is especially useful in systems with versioned data, as it allows teams to track decisions over time and ensure compliance with changing requirements.

### Best Practices for Ensuring Correctness
Developers can adopt several strategies to maintain correctness and reliability in their policy engines:

**Automated Testing:**Build robust test suites to verify policies during development and CI/CD workflows.**Version Control:**Use versioning for policies and data to track changes and ensure consistency.**Decision Logging:**Enable logging to audit decisions and debug issues when they arise.**Formal Verification:**Leverage built-in verification tools to ensure logical consistency and account for edge cases.
As Gabriel summarized:

"Verification and correctness aren’t just about testing policies—they’re about building trust. Developers need tools and workflows that make it easy to validate policies and catch errors before they impact production."

This brings us to the conclusion, where we summarize the key takeaways and reflect on how developers can choose the best policy engine for their needs.

## Key Takeaways, Best Practices, and Choosing the Right Policy Engine
The **Policy Engines Showdown** showed some diverse approaches, strengths, and trade-offs of today’s leading policy engines. Each engine excels in specific scenarios, and the right choice ultimately depends on your use case, data, and team needs.

As Pauline put it:

"It’s all about the use case. What is your data? What is your latency budget? When you can answer these questions, there are great tools available for every situation."

### Main Takeaways to Keep in Mind:
**Understand Your Requirements:**Start by analyzing your specific needs. Do you prioritize speed, scalability, or determinism? Is your system policy-driven or data-driven? These questions help narrow down your options.

**Evaluate Trade-Offs:**Each engine has trade-offs. Multipurpose engines like OPA offer flexibility but may require more effort to configure, while single-purpose engines like Cedar provide clarity and focus for specific domains.

**Plan for Adoption:**Consider the learning curve and team expertise. Tools with intuitive design, robust documentation, and active communities, such as Cedar and OPA, can accelerate onboarding.

**Think Long-Term:**Scalability, performance, and correctness are crucial for sustainable growth. Test policies rigorously, version your data, and leverage decision logging to maintain reliability.

## Contribute!
Many of these projects are open source, and contributions from developers can drive innovation and improve usability for all. As Gabriel noted:

"A decade ago, authentication was where authorization is today. Most developers still roll their own solutions, but we want to change that. By working together, we can build better tools and help the ecosystem grow."

Projects like [ Permit.io’s CLI](https://github.com/permitio/permit-cli) and its open-source tools—

[and the](https://github.com/permitio/opal)
**OPAL**[—are key examples of how developers can contribute to and benefit from the ecosystem.](https://github.com/permitio/cedar-agent)
**Cedar Agent**: OPAL extends Open Policy Agent (OPA) by automating real-time policy and data updates. It simplifies synchronization between your policy engine and the ever-changing data it relies on.**OPAL (Open Policy Administration Layer)**An HTTP server that integrates seamlessly with Cedar, providing tools to manage policies, data, and schemas for fine-grained access control. It enables developers to define, store, and enforce permissions efficiently through real-time authorization checks.**Cedar Agent:**: Designed to streamline the adoption of policy engines,**Permit.io CLI**[Permit.io](http://Permit.io)’s CLI makes it simple for developers to set up and manage authorization across their systems.
By contributing to these projects, developers can help improve the tooling and build a better ecosystem for managing policies at scale. Contributions can range from submitting code and improving documentation to sharing feedback and insights that drive future development.

"It’s not just about using these tools; it’s about building them together," Gabriel emphasized. "The more we contribute, the more accessible and powerful these engines will become for everyone."

Whether you’re exploring OPA for its flexibility, OpenFGA for its relationship-based approach, or Cedar for its clarity, engaging with these open-source communities can help you make a meaningful impact.

Want to learn more about authorization and see how you can contribute? Join our [ Slack Community](https://io.permit.io/permitslack), where there are hundreds of devs building and implementing authorization.

## Written by
### Daniel Bass
Application authorization enthusiast with years of experience as a customer engineer, technical writing, and open-source community advocacy. Comunity Manager, Dev. Convention Extrovert and Meme Enthusiast.

## Related Tags
Like this Article?

[Star us on Github](https://github.com/permitio)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgithub.35b09e10.svg&w=48&q=75)
Disagree?

[Tell us why](https://io.permit.io/blog-slack)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fslack.cbb6ed5c.svg&w=48&q=75)
Want more?

[Join our Substack](https://io.permit.io/blogstack)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpen.e40711f5.svg&w=48&q=75)