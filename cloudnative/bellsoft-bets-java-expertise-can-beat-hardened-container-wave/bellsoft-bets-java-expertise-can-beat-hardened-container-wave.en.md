The hardened container market has been heating up with venture money and startups, but [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) platform provider [BellSoft](https://bell-sw.com/) thinks its eight years of building Java runtimes gives it something others don’t have: expertise in what’s actually running inside those secured containers.

The company used the [KubeCon conference](https://thenewstack.io/kubecon-vclusters-k8s-platform-to-manage-gpus-as-a-service/) in Atlanta last November to launch its [BellSoft Hardened Images](https://bell-sw.com/bellsoft-hardened-images/), betting it can stand out in a space where [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) pioneered the approach, and startups are now piling in. BellSoft’s angle is that it’s not just wrapping containers in security — it’s optimizing the Java workloads themselves.

“The market for containers is emerging,” [Alexander Belokrylov](https://www.linkedin.com/in/alexanderbelokrylov/), co-founder and CEO of BellSoft, tells *The New Stack* in an interview. “I see how much money venture investors put in, and it looks like they feel that it has potential.”

Belokrylov says the problem BellSoft is addressing is real. When development teams use base images, they often inherit a large attack surface, including unnecessary packages, shells, compilers, package managers, and unused libraries that may contain known vulnerabilities that haven’t been addressed, according to [Janet Costello Worthington](https://www.linkedin.com/in/janet-costello-worthington/), a Forrester Research analyst who covers security.

“This can lead to patching chaos, emergency rebuilds, or even production failures,” she says. “Hardened containers strip away these unnecessary components, reducing the risk of exploits and simplifying container management.”

This all comes as Java faces a particular vulnerability problem: [44% of Java services contain known exploited vulnerabilities](https://www.datadoghq.com/state-of-devsecops/), compared to 5% for [Go](https://thenewstack.io/introduction-to-go-programming-language/) and just 2% for other languages. Typical container images carry [600 known vulnerabilities](https://www.netrise.io/resources-whitepaper-brief/supply-chain-visibility-risk-study-edition-2), nearly half of them years old. Two-thirds of organizations had a container security incident in the past year.

## What sets BellSoft apart

BellSoft argues its differentiator is not just building secure containers — it’s understanding what goes inside them. The company ranks among the top five [OpenJDK](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/) contributors.

“Our differentiator is a deep technical expertise in the technologies we provide,” Belokrylov says. “We are not just the experts in building software; we’re experts in these kinds of projects.”

That expertise started with [Alpaquita Linux](https://bell-sw.com/alpaquita-linux/) three years ago, an Alpine-like OS that began as a Java optimization project. “Originally, our idea was to optimize [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) to run Java workloads,” Belokrylov said. “However, it appeared that Linux optimized for Java workloads, optimized pretty much for everything.”

Now BellSoft supports hardened images for .NET, C/C++, [JavaScript](https://thenewstack.io/introduction-to-javascript/), [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/), and Go — all with near-zero common vulnerabilities and exposures (CVEs) and technical support. The company claims 95% fewer vulnerabilities than standard Java images and up to 30% resource savings with its [Liberica JDK Lite](https://bell-sw.com/libericajdk/).

According to Costello Worthington, vendors that provide hardened container images deliver value by addressing key security and operational challenges.

“These images come with less bloat, fewer inherited vulnerabilities, secure configuration defaults, and a smaller attack surface,” she says. Hardened images also offer essential transparency through provenance, attestations, and software bills of materials that detail what’s inside.

## Crowded field

At KubeCon, Belokrylov says he saw plenty of competition. Chainguard has done “a very good job” pioneering hardened containers, but new players are emerging. “There were a number of startups who were making more or less the same, however they are making that from scratch,” he says.

[Dan Lorenc](https://www.linkedin.com/in/danlorenc/), CEO of Chainguard, acknowledges the sudden rush into the space. “It’s kind of baffling to watch, in some ways, how crowded the space has gotten in the last year,” he says in an interview with *The New Stack*. “We started doing it three years ago now, because there was clearly a need.”

But Lorenc sees the proliferation of hardened container offerings as a symptom of a deeper issue.

“The software supply chain is broken, and the recent explosion of hardened container offerings is the industry’s reaction,” he writes in an [article in *The New Stack*](https://thenewstack.io/hardened-containers-dont-fix-a-broken-software-supply-chain/). “The industry has responded by tightening inspection at the end of the assembly line (more checks, more scanners) while largely ignoring how the parts get sourced, assembled, and verified upstream.”

In the article, Lorenc also writes, “The real issue is about trusting where software comes from, and why building open source software directly from source is the only way to secure the entire software supply chain.”

The hardened container market now includes, in addition to BellSoft, established players like Chainguard, Docker, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), [VMware](https://www.vmware.com/?utm_content=inline+mention); cloud providers like [AWS](https://aws.amazon.com/?utm_content=inline+mention), Azure, and [Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention); startups like [RapidFort](https://www.rapidfort.com/), [Wiz](https://www.wiz.io/), [Edera](https://edera.dev/), [Lineaje](https://www.lineaje.com/), [Minimus](https://www.minimus.io/); and others.

The opportunity exists because enterprises now run security scanners on everything. “They are not blind now when they’re accepting software,” Belokrylov says. “They’re asking vendors to provide them the software with the limited number of CVEs.”

BellSoft wants to handle that base layer.

“The idea is here that there is a vendor like BellSoft who actually took care of the significant part of the software delivery package, like base images, and keeps them up to date and zero CVEs,” Belokrylov says. Developers can focus on their applications while BellSoft maintains the foundation, he says.

For enterprises, Costello Worthington notes that customers who leverage hardened container images often find it easier to meet compliance requirements and streamline the process for achieving [FedRamp authorization](https://www.fedramp.gov/).

“Providing development teams with a curated baseline of images ensures development can focus on roadmap features and functionality for the business, while making it easier to meet compliance requirements, reduce vulnerabilities, and accelerate development velocity,” she says.

## Technical approach

The hardened images strip out package managers and nonessential components with locked configurations that can’t be changed at runtime. Alpaquita Linux supports both musl and glibc, letting teams migrate without rewriting code.

Unlike competitors waiting for upstream patches, BellSoft writes its own when needed — a capability that comes from actively contributing to OpenJDK and [GraalVM](https://thenewstack.io/graalvm-finally-gets-java-for-webassembly/).

The company also sells Liberica JDK Performance Edition, which backports the modern JVM from Java 25 into older versions.

“Applications written for JDK 8 API, specifically, they perform as if they were migrated to the most modern Java version without any line of code change,” Belokrylov says. “That’s a killer feature for companies who still run Java 8 applications, specifically in the cloud.”

## Tiers available

BellSoft offers a free Community tier with hardened containers for JDK 21 and 25+. A Standard tier covers all JDK versions plus GraalVM, Go, Python, C, and Alpaquita base with a 7-day CVE remediation SLA. Premium adds support and performance consulting.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)