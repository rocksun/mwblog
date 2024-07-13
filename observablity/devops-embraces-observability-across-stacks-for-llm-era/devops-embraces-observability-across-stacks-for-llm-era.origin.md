# DevOps Embraces Observability Across Stacks for LLM Era
![Featued image for: DevOps Embraces Observability Across Stacks for LLM Era](https://cdn.thenewstack.io/media/2024/07/939dc367-alex-shuper-nkbruh3ngbs-unsplash-1-683x1024-1.jpg)
NEW YORK — The leviathan-esque impact of AI, security concerns and the continued challenges associated with the shift to cloud native represent major disruptions for [DevOps](https://thenewstack.io/devops/). All of this will lead to a change in the coming months or years if not months.

While [platform engineering](https://thenewstack.io/platform-engineering/) looks to offer promising ways to deal with the associated explosion in infrastructure and data to manage, and applications to manage, the underlying way to deal with these challenges will involve proper [observability](https://thenewstack.io/observability/) and support for [OpenTelemetry](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/). This is one of the key takeaways of [DASH 2024](https://www.dashcon.io/), [Datadog](https://thenewstack.io/datadog-brings-big-observability-directly-to-your-phone/)‘s annual users conference here recently.

The theme could be associated with any user or any conference as the community is looking for ways to deal with this explosion of data and applications to manage and observe, nobody knows exactly what the impact of AI will be for software development and deployment, [CI/CD](https://thenewstack.io/ci-cd/), and DevOps and IT in general. However, the argument can be made that as the dust settles in the future, it will be up to proper observability processes, tools, and practices to analyze and make proper decisions about the best way to utilize LLMs for application development and other AI-assisted processes.

“We hear from a number of you that your LLM-powered applications are moving to production. And once in production, it is crucial that they’re monitored like any other load-bearing machine,” [Alexis Lê-Quôc](https://www.linkedin.com/in/alexislequoc/), Datadog CTO and co-founder, said during the DASH keynote. “But what’s different in their case is the kind of data that’s essential to understand health, performance and safety.”


[@datadoghq]says you can get everything from Datadog monitoring and observability through[@opentelemetry](Datadog is among the top-10 contributors), Engineering director Gordon Radlein said today during the[#DASH]user’s conference keynote today.[pic.twitter.com/nCvNJpLSBt]— BC Gain (@bcamerongain)

[June 26, 2024]
And in order to standardize instrumentation for logs, traces, and metrics for not just [large language models (LLMs)](https://thenewstack.io/llm/) but across the stack and environment of any organization, OpenTelemetry — one of the more dynamic open source projects — will become that much more critical. “OpenTelemetry is revolutionizing observability by providing a standards-based foundation for us to build on, unlocking innovation across the industry,” [Gordon Radlein,](https://www.linkedin.com/in/gordonradlein/) engineering director at Datadog, said during his keynote. “It’s a tide that lifts all boats.”

To help Datadog users and those considering adopting the platform — OpenTelemetry helps to make it easier to mix and match with existing solutions — Datadog unveiled a barrage of new products and features at DASH. This was a culmination of over a year of feedback from 187,000 customer meetings; resulting in about half a million releases to production, covering more than 400 new products and new features, [Olivier Pomel](https://www.linkedin.com/in/olivierpomel/), Datadog co-founder and CEO said during his keynote.

## LLM Peace
Again, LLM security is a big deal and a different animal and to that end, Datadog unveiled Datadog LLM Observability at DASH. With it, the platform is designed to help organizations gain better insights and control over the explosion of LLM data, often manifested in multiple LLMs in a single organization. As [Mohamed Alimi,](https://www.linkedin.com/in/mohamed-kamel-alimi/) engineering lead for Datadog, explained, experimentation with LLMs “has led to an incredible innovation across many industries where many of these experiments have evolved from simple application into much more sophisticated systems running in production using multiple LLMs,” for orchestration framework, retrieval systems and [knowledge graphs](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/). “But this also led to new challenges, he said.

As applications are involved in LLMs and more complex patterns, they become much harder to troubleshoot, Alimi said. Second, due to the inherent unpredictability of LLMs and AI components in general, these applications need continuous monitoring for hallucination. And finally, these applications can face significant risk from prompt hacking and data sharing, Alimi said.

In a demo at DASH, Alim showed how with an LLM-powered e-commerce chatbot, Datadog LLM observability highlights issues that require immediate attention. errors, potential hallucinations, slow responses, token count, and security threats were flagged. “It also highlights ‘faithfulness,’ which is a measure of correctness and accuracy relative to a given context,” Alimi said. “And we use faithfulness here as a proxy for hallucinations.”

During the demo, Alimi used the platform to gather intel about the reported hallucination. The information provided included the duration of the interaction, the token count consumed and the number of LLM calls made. “Organizations will need to embrace observability” in order to properly manage LLMs for security and performance, Alimi said.

As an observability provider, Datadog has a strong interest in both serving as a major contributor to the OpenTelemetry project and using the standardization that OpenTelemetry provides to make its tools compatible with OpenTelemetry.

The idea is that through this OpenTelemetry feature or instrumentation, the user organization can immediately and seamlessly connect and begin utilizing the observability platform of their choice. And, of course, the observability provider is there separately to do its best to make that experience through OpenTelemetry superior to other players.

One of the benefits of OpenTelemetry is that it helps to streamline compatibility, and with contributions from the community, it allows for more features to be developed that can take advantage of this or allow solutions observability providers to take advantage of that compatibility.

## OpenTelemetry Strong
As one of the top-10 contributors to the OpenTelemetry project, Datadog continues to help build the project while its product development continues to outpace OpenTelemetry compatibility. “Because Datadog has been building in this space for so long, OTel [OpenTelemetry] doesn’t yet support all the products offered. With Datadog’s pace of innovation, that is expected to continue to be the case, even as the gap closes. This presents a dilemma: go all in on Datadog and forgo some of the great benefits that OpenTelemetry brings to the table, or be limited to the products that OTel supports,” Radlein said. “Naturally, the question arises, why not have both? Datadog has been working hard on that problem because Datadog is better with OpenTelemetry and OpenTelemetry is better with Datadog.”

During DASH, Radlein described how Datadog is taking the next big step by unifying the Datadog agent and the OpenTelemetry collector. “Now, the agent and the collector work together to form a whole greater than the sum of its parts, enriching OpenTelemetry data and enabling the product suit,” Radlein said.

With the new agent, collector users will immediately get access to the full product suite and platform, Radlein said. App-based management of the collector fleet is provided, “along with peace of mind from dedicated product support. New agent users will also get access to the large and growing number of community-contributed integrations, including out-of-the-box support for the growing number of commercial and open source tools being instrumented natively with OpenTelemetry,” Radlein said. “Better interoperability across the tools in the observability fleet, whether vendor-based or open source, is achieved. Control over OTLP data with full access to the collector’s powerful routing and processing capabilities is provided.”

## Cloud Native Way
LLMS and OpenTelemetry, while huge, were among over a dozen other announcements made at the conference. They included how Datadog is stepping up observability to help mitigate rising cloud costs. As [Danny Driscoll,](https://www.linkedin.com/posts/danielfdriscoll_servelress-activity-7100533805056155649-bq-D) product manager for container and [Kubernetes](https://thenewstack.io/kubernetes/) monitoring at Datadog, said, more than 65% of Datadog-monitored Kubernetes containers are still using less than half of their requested memory and CPU resources.

With Datadog Kubernetes Autoscaling, workloads and clusters with the most savings potential are prioritized in order to take direct action from the Datadog platform to apply and then automate right-sizing recommendations and to observe and measure the impact of your complete auto-scaling program on your key cost and efficiency metrics. This announcement is intended to help users build platforms on Kubernetes to deliver more efficient resource use, which can lead to lower infrastructure costs and lower energy consumption impact for your businesses, Driscoll said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)