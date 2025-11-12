In the days of on-premises data centers, when procurement cycles were measured in months, [overprovisioning](https://thenewstack.io/how-to-avoid-overprovisioning-java-resources/) was a logical risk management strategy — so commonplace that no one gave it a second thought.

In theory, the rise of elastic utility compute offered by public cloud providers should have gotten us away from it, but [it simply hasn’t](https://thenewstack.io/automation-can-solve-resource-overprovisioning-in-kubernetes/). Companies I’ve worked with are typically overprovisioned by at least 50%, even in the cloud. [Zombie servers](https://thenewstack.io/zombie-resources-eat-up-your-cloud-budget/), which were once doing useful work but are no longer, abound.

## Why Cloud Overprovisioning Persists Despite Elastic Compute

[Enrico Bruschini](https://www.linkedin.com/in/enricobruschini/), COO of autonomous optimization platform vendor [Akamas](https://akamas.io/?utm_content=inline+mention), believes he knows why overprovisioning remains such a problem.

“The DevOps revolution and the rise of platform teams put developers in charge. Developers don’t want to be woken up in the middle of the night, and they don’t want to be accused of configuring applications in a way that is not reliable. So they demand overprovisioning,” he said in an interview.

“We are seeing two relevant trends: the ever-increasing number of configuration parameters nested in every layer of the stack, and the decreasing time between releases. These make it progressively harder for anybody to study what the correct configuration could be. Adjusting that continuously to the ever-evolving needs is simply inconceivable,” Bruschini explained.

Correctly [tuning a runtime like the Java Virtual Machine (JVM) is indeed notoriously hard](https://akamas.io/events/java-on-kubernetes-lessons-in-performance-engineering-with-akamas-and-microsoft/), and it has long been the case that tuning the JVM requires specialist knowledge held by only a handful of developers in a typical organization. The result can be large amounts of configuration copy-pasting.

“Someone in the team will raise their hand and say, ‘I know a fair bit about Kubernetes or the JVM or Node.js; let me take a look,’” Bruschini said. “They’ll go in, tweak something, and then for the next few years, there is a superhero configuration that everyone is copy-pasting. It becomes a static blueprint, producing apps that are poorly configured by design.

“You can overprovision as much as you want, but if you haven’t tuned your runtime configuration, you are just scaling inefficiency — and that applies equally if you are using a Kubernetes [Horizontal Pod Autoscaler](https://thenewstack.io/reduce-kubernetes-costs-using-autoscaling-mechanisms/),” he said.

## DevOps Culture vs. Reliability and Cost Optimization

This isn’t just expensive. Overprovisioned hardware is also bad from an [environmental standpoint](https://thenewstack.io/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability-2/) and constitutes a reliability risk. The problem is compounded, Bruschini suggested, by different motivations for various teams and their respective visibility.

“We were observing repeatedly with our clients a fracture between their platform, SRE [site reliability engineering] and development teams,” he said. “The platform team optimizes costs and is keen to configure its platform directly. The SRE team aims at reducing risk. But both teams have a limited reach. They can touch the infrastructure layer and the platform they’ve built, but they can barely touch workload and runtime configurations, like JVM heap size, garbage collector choice and so on; that is the responsibility of the application teams.”

Bruschini is referring to silos — the very things DevOps is trying to eradicate. The difficulty is that humans naturally form themselves into groups around clear incentives. According to [Russell Miles](https://www.linkedin.com/in/russmiles/), an experienced platform team lead working as a technical product owner at ClearBank, this means: “It not only takes energy and intention to break down silos in the first place, but it’s a constant investment to make sure they stay broken down.”

## FinOps and Sustainability Feedback Loops

Miles said challenges around cost and suitability need to be thought of as an extension to DevOps culture, not as a conflict. DevOps has feedback loops modeled after the Observe, Orient, Decide, Act (OODA) loop, a four-stage decision-making model developed by military strategist [John Boyd](https://en.wikipedia.org/wiki/John_Boyd_(military_strategist)).

“DevOps culture emphasizes feedback loops and continuous improvement,” Miles said in an interview. “But what it doesn’t do very well in some organizations is balance feedback loops such as sustainability and cost.”

> Challenges around cost and suitability need to be … an extension to DevOps culture, not a conflict.

FinOps and sustainability feedback loops are often extremely immature, even in organizations that understand the value, Miles explained. Enabled by the platform team, ClearBank has introduced metrics such as “carbon impact per payment transaction.”

“We can see carbon reduction as we make decisions and tie them to the business,” Miles said. It is still early days, however. “At ClearBank, we’ve seen that you often grow the O’s of the OODA loop first, so if a tool can provide developers with the Decide and Act parts, that’s great.”

## Closing the Runtime Optimization Gap

Plenty of tools exist to help developers optimize code, but Bruschini sees a gap in the market for a tool that can help with coordinated full-stack optimizations to improve reliability, performance and costs. This observation led to the creation of the Akamas Platform, which currently has two modules, [Akamas Offline](https://akamas.io/offline-optimization/) and [Akamas Insights](https://akamas.io/insights/).

Akamas Offline is designed to carry out what the vendor calls optimization studies at the end of a load test. To use it, you first define the optimization goal, any service-level agreement (SLA) and other boundaries, then run the study with a load test that generates traffic.

“The tool will provide different iterations of the configuration with explanations as to why, plus all the necessary configuration, which you can take and apply,” Bruschini said.

Launched in beta earlier this year and now generally available, Akamas Insights is an AI-driven Software as a Service (SaaS) solution that aims to enable organizations to effortlessly unite developers, SREs and platform engineers around one goal: delivering reliable, efficient services. This is done by providing ready-to-apply workload, runtime and Kubernetes configurations to tune the entire stack based on production.

“We turn the spotlight on the many optimization opportunities scattered throughout the stack,” Bruschini said. “The Insights module was the result of speaking to many corporations and finding they were blind to where the optimization opportunities lie,” he added.

Akamas Insights uses existing observability data, meaning there is no requirement to install another agent. The vendor is building integrations for each observability tool separately. Currently, [Datadog](https://www.datadoghq.com/?utm_content=inline+mention), [Dynatrace](https://www.dynatrace.com/?utm_content=inline+mention) and [Prometheus](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along/) are supported with integrations to other observability tools planned.

## The Two-Stage Evolution: From Empowerment to Automation

The vendor’s long-term vision is a two-stage evolution, which Bruschini described as “first empower teams, then automate and reduce their workload.”

“We start with empowerment because we’re tired of seeing SRE or platform teams chasing application teams to configure things correctly between the layers,” he said.

“SREs can now easily spot unreliable applications and raise a PR [pull request] from Akamas with all its recommended changes. Developers can then review and approve the PR, effortlessly optimizing the full stack while remaining in control.”

Then, as teams gain confidence, they can allow Akamas to automate the process until “optimization becomes a native platform capability: automated, continuous, thus effortless, and always safe.”

Bruschini believes he can get continuous, real-time, AI-driven optimizations into production for Akamas customers. The technology is getting ready for that reality, with Kubernetes in-place pod resizing one step in that direction.

## Closing a Widening Gap in Cloud Efficiency

As larger enterprises grapple with the competing pressures of rapid delivery, reliability and cost optimization, the overprovisioning problem shows no signs of resolving on its own. With AI coding assistants accelerating development cycles and performance engineering roles fading into the background, the gap between application delivery speed and runtime efficiency continues to widen.

Tools like Akamas recognize that optimization can no longer be an afterthought or rely on occasional “superhero configurations” — it must be automated, continuous, thus effortless, and always safe.

Whether Bruschini’s vision of continuous AI-driven optimization becomes the industry standard remains to be seen. But one thing is clear: The era of casually overprovisioning cloud resources, zombie servers and all, cannot continue indefinitely.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)