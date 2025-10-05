When Bloomberg decided to standardize its [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) infrastructure in 2018, the company faced a decision that would impact more than 1,000 engineers and some of the world’s largest deployments of [Apache Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/), [Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) and [Solr](https://solr.apache.org/). The stakes were high. As a provider of financial infrastructure to investment and business professionals globally, reliability was not optional — it was mandatory.

The company’s choice — [Eclipse Temurin](https://adoptium.net/temurin), the [OpenJDK](https://thenewstack.io/your-guide-to-navigating-openjdk-in-2023/) distribution from the [Eclipse Foundation’s](https://www.eclipse.org/) [Adoptium Working Group](https://adoptium.net/) — provides lessons for any enterprise navigating the increasingly complex landscape of open source adoption.

According to Eclipse, the Adoptium Working Group promotes and supports high-quality runtimes and associated technology for use across the Java ecosystem, providing Java Technology Compatibility Kit (TCK)-certified OpenJDK builds through Eclipse Temurin.

## The Vendor Neutrality Imperative

“We were looking for vendor neutral,” [Andrey Rybka](https://www.linkedin.com/in/arybka/), head of CTO cloud compute, platform & security architecture at Bloomberg told The New Stack. Rybka has been working with Java since 1995 and leads Bloomberg’s open source initiatives.

In addition to [Oracle](https://www.oracle.com/developer?utm_content=inline+mention)[’s](https://openjdk.org/projects/jdk/25/), “There are [IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention), [Red Hat](https://developers.redhat.com/products/openjdk/overview), [AWS](https://aws.amazon.com/?utm_content=inline+mention)[-specific distributions](https://www.theserverside.com/news/252452738/Amazon-Corretto-extends-OpenJDK-support), [even Microsoft](https://thenewstack.io/microsoft-openjdk-goes-ga-at-build/) is in the game now. There is a myriad of choices,” he said.

In a landscape where single-vendor open source projects dominate, organizations face real risks of misalignment. “If there is an open source project that’s just one company’s open source, you always run the risk of potentially misalignment at some point with what you want to do, or what that company wants to do,” Rybka said.

For Bloomberg, which describes itself as an “open source-first” company, vendor neutrality provided by foundation governance was non-negotiable. “If it’s a vendor-neutral entity, Eclipse Foundation or some other foundations that we participate with, this is where you can ensure better alignment and priorities,” he explains.

While Bloomberg calls itself “open source-first,” that is different from open source-only, Rybka noted. They will use commercial software when it makes sense, but when they build something new, they look to open source options first. For a company with that philosophy, having a foundation in the middle — Eclipse, Apache, Linux Foundation, whoever — provides a buffer. “If it’s a vendor-neutral entity, this is where you can ensure better alignment and priorities,” Rybka said.

## Beyond Free Beer: The Real Value Proposition

The company needed long-term support that wouldn’t force constant risky updates, full TCK certification to ensure compatibility and platform support that matched their specific hardware and OS requirements. The TCK is the test suite that proves you’re running a compliant Java implementation, not someone’s creative interpretation of the spec.

Timely security patches were essential, as was OSI-approved licensing that provided predictable terms, Rybka said.

Beyond these technical requirements, Bloomberg also looked at strategic factors including vendor neutrality and governance structures, [software supply chain security](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/) capabilities, the vibrancy of surrounding communities and options for commercial support when specialized expertise was needed.

In a statement, [Phil Vachon](https://www.linkedin.com/in/philvachon/), head of infrastructure in Bloomberg’s office of the CTO, stressed the quality dimension: “As a supplier of financial infrastructure, we look to utilize software that is of the highest quality and stability, since our infrastructure needs to have the same reliability and stability that we deliver to our clients.”

Eclipse Temurin delivered on these requirements. The distribution’s TCK certification, secure development practices and transparent [Software Bill of Materials (SBOMs)](https://thenewstack.io/sboms-are-great-for-supply-chain-security-but-buyers-beware/) gave Bloomberg confidence to rely on the technology for both internal systems and customer-facing products.

Plus, the Eclipse Foundation’s governance meant no single company could hijack the project.

“Organizations are seeking secure, high-quality, open source and vendor-neutral alternatives, and Temurin delivers just that,” said [Mike Milinkovich](https://www.linkedin.com/in/mikemilinkovich/?originalSubdomain=ca), executive director of the Eclipse Foundation. “With the latest release, we’re continuing to deliver the quality and assurance organizations expect from commercial offerings, while also introducing new ways for the community to support and sustain this momentum.”

## The Security Dimension

In financial services, software supply chain security is critical. Bloomberg maintains mature processes for vulnerability tracking and patch cycles, generating and ingesting SBOMs across its stack.

“Software supply chain security is probably the biggest thing,” Rybka says. “[Log4Shell](https://thenewstack.io/log4shell-lives/) was a major alert that brought this to light. But we were already doing this even before that.”

[Daniel Scanteianu](https://www.linkedin.com/in/daniel-scanteianu-656794120/), a Bloomberg software engineer who serves as co-chair of the company’s Java and [JVM (Java Virtual Machine)](https://thenewstack.io/chicory-write-to-webassembly-overcome-jvm-shortcomings/) Guild and contributes to the Eclipse Adoptium Project, pointed to the transparency factor.

“Enhanced transparency into the components and dependencies of the software has enabled Bloomberg to proactively manage vulnerabilities and mitigate potential risks,” he said in a statement.

The Eclipse Foundation’s governance model and Temurin’s security focus aligned well with these requirements. “Temurin’s work in secure software development and certifying its JDKs with the TCK gave Bloomberg the confidence to trust Temurin’s OpenJDK builds,” Scanteianu said.

## The Reality of Migration

The transition to Temurin was not trivial, Rybken explained. In 2018, Bloomberg switched from its [JDK 8](https://thenewstack.io/end-of-the-road-for-javafx-in-jdk-8-keeping-your-apps-alive/) binaries and standardized its JVM on Eclipse Temurin. Given the depth and breadth of Java integration across Bloomberg’s operations, the mostly manual migration was, in Rybka’s words, “a massive, but worthwhile undertaking.”

However, the execution was smoother than anticipated. “Quality-wise, it was pretty solid,” Rybka said. “We haven’t seen too many regressions, or even if we reported something, it was addressed promptly.”

The automation and observability tools worked well out of the box. “[Eclipse Mission Control](https://projects.eclipse.org/projects/adoptium.mc), the [Memory Analyzer](https://projects.eclipse.org/projects/tools.mat) for heap analysis — if you have any issues, we have not seen anything that would say we had some major issues here,” he noted.

When you can see exactly what is in your Java runtime, down to the dependency level, you can do something about vulnerabilities before they bite you. Temurin’s secure development practices were not just marketing — they aligned with what Bloomberg’s security teams needed to do their jobs.

However, one challenge that persists: the absence of default commercial support. “There’s no quote-unquote commercial support by default,” Rybka said. “If I have a vendor relationship with somebody who also supports the particular open source product, that’s a kind of perfect intersection.” Bloomberg addresses this through a combination of internal expertise and selective vendor relationships for specialized support.

## Contributing Back: Not Just Free Riders

Bloomberg’s philosophy extends beyond consumption. “We don’t want to just be free riders. We want to give back,” Rybka emphasizes.

The company’s contributions to Adoptium include significant work on the [VDR generator](https://github.com/adoptium/temurin-vdr-generator) and Temurin build tools, with Scanteianu particularly involved in security and supply chain initiatives within the Adoptium Working Group. One Bloomberg engineer even serves on the [Python Steering Council](https://github.com/python/steering-council), while teams contribute to numerous other projects, including Chromium, [Kubernetes](https://thenewstack.io/kubernetes/), Prometheus and Grafana.

This commitment stems from both philosophy and pragmatism. “As we build our capabilities to be mature in this particular project or foundation, there’s going to be some challenges,” Rybka explained. “It helps when you have contributors who can help us with that.”

## Advice for Enterprise Java Adoption

Based on Bloomberg’s experience, Rybka offers pragmatic guidance for organizations evaluating Java distributions. The first step is understanding your own context.

“I would want to understand their ecosystem and their capabilities. We have thousands of engineers — for us, this was the right choice,” he said. “If you’re all-in on AWS, maybe the AWS distribution would be a better choice. It depends on the particular problem you’re trying to solve.”

Rybka recommends creating a decision matrix that lists all critical requirements and scores each vendor option accordingly. [Long-term support (LTS)](https://thenewstack.io/java-25-oracle-makes-java-easier-to-learn-ready-for-ai-development/) might be a must-have, platform compatibility another essential factor, and cloud strategy yet another consideration. The key is matching your specific needs against what’s available rather than following industry trends blindly.

Rybka also cautions against looking for a universal solution.

“I don’t think there should be only one distribution that rules them all. I actually like that there’s a lot of good choices here, and some are really good fits in some particular areas,” he said.

Different organizations have different needs, and the diversity of options reflects the diversity of use cases in the enterprise Java ecosystem.

Rybka particularly emphasized the importance of long-term support.

“If you have a JDK with no LTS, you have to be really good with updates,” he said. “Every update is going to carry some risk because there’ll be regressions potentially if you jump around without long-term support.”

## Looking Forward: AI and the Value of Foundations

As Bloomberg continues expanding its open source footprint — particularly in AI, where investment is “growing extremely robustly,” Rybka says — the company maintains that fundamental software architecture skills remain essential, even in the age of AI coding assistants.

“I think it’s very promising, but I do have optimism that good software engineering is safe,” Rybka said of [vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) and [AI-powered development tools](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/). “Good sense of architecture, good practices, software development life cycle practices — that doesn’t go away.”

The company continues investing in “boring stack” fundamentals like middleware and databases, while simultaneously exploring cutting-edge areas including the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) and [agent frameworks](https://thenewstack.io/ai-agents-unite-conference-reveals-next-gen-frameworks/),” he said. [Python](https://thenewstack.io/what-is-python/), [JavaScript](https://thenewstack.io/introduction-to-javascript/), Kubernetes and [security tooling](https://thenewstack.io/the-security-tooling-faceoff-open-source-security-vs-commercial/) all factor prominently in future plans.

Bloomberg’s Eclipse Temurin decision stands as a model of thoughtful enterprise open source adoption.

“Temurin’s ongoing investment in secure, timely builds has made it very easy to keep choosing it as our preferred JDK,” Vachon said.

Indeed, for Rybka, the Temurin choice reflects Bloomberg’s broader evolution. “By moving through the whole process, from consumption to community participation, project contribution and now as a leader in open source, Bloomberg can ensure Temurin continues to be available as a free, open source, enterprise-grade OpenJDK platform for both our internal use and for the wider tech community.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)