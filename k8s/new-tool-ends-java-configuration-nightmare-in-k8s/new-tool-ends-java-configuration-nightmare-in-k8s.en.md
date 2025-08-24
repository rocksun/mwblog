[Perforce](https://www.perforce.com/) this week launched [JRebel Enterprise](https://www.jrebel.com/products/jrebel-enterprise), a new solution designed to eliminate one of [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) development’s most persistent pain points: the time-consuming redeploy process that can grind productivity to a halt in modern cloud environments.

According to [Perforce’s 2025 Java Developer Productivity Report](https://www.jrebel.com/blog/developer-report-highlights), 73% of enterprise respondents now use cloud-based or remote development environments, creating new friction points that traditional tools struggle to handle, [Jeff Michael](https://www.linkedin.com/in/jnmichael/), senior director of product management at Perforce, told The New Stack.

## Beyond Traditional Hot Swapping

[JRebel](https://www.jrebel.com/products/jrebel) has long been known for its ability to push class-level changes to running Java applications without full rebuilds. But JRebel Enterprise tackles a more complex problem: the configuration nightmare that emerges in [containerized](https://thenewstack.io/introduction-to-containers/), [Kubernetes](https://thenewstack.io/kubernetes/)-driven environments where development containers spin up and down dynamically, Michael said.

“[DevOps](https://thenewstack.io/introduction-to-devops/) environments are maturing at a rapid pace due to the onset of rapidly evolving business needs, adding significant complexity to development and testing environments,” he said. “JRebel Enterprise manages those complexities for your developer — allowing them to seamlessly push code changes to remote environments without the need for lengthy rebuilds and redeploys.”

The traditional JRebel approach required developers to manually configure agents on static deployment servers. In today’s dynamic environments, that model breaks down when containers appear and disappear based on workload demands or when developers need to spin up environments for specific bug fixes, Michael said.

## Automatic Environment Discovery

JRebel Enterprise introduces what the company calls a “phone home” mechanism. When new containerized environments spin up, they automatically register with a central JRebel broker. This broker then exposes available environments directly in the developer’s IDE through a simple drop-down menu, Michael said.

The result is a dramatic reduction in configuration overhead — from 3-5 minutes per server per developer to a one-time, 1-2-minute setup for entire Java development teams. In addition, developers no longer need to track which environments are available or manually reconfigure their tools when deployment targets change.

“As a developer, I no longer need to know which environment I should point to. It shows up in my IDE. I can select it in a drop-down, and now seamlessly, the developer can interact with all of the dynamic environments as they come up and down,” Michael explained.

## Enterprise-Scale Adoption

JRebel’s appeal spans from individual developers paying $595 annually to large enterprises with over 1,000 Java engineers, he said.

The enterprise version currently supports [IntelliJ IDEA](https://www.jetbrains.com/idea/), with the [Eclipse](https://thenewstack.io/eclipse-theia-the-deepseek-of-ai-tooling/) IDE and [VS Code](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) integration planned. It works with all major cloud providers, including [AWS](https://aws.amazon.com/?utm_content=inline+mention), Microsoft Azure and [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform, and supports [Java 21](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/) and newer versions.

## Market Positioning

While JRebel faces competition from hot swap tools and other development efficiency solutions, Perforce believes its class-level change detection and enterprise-grade dynamic environment management set it apart, Michael said. The company’s ability to automatically handle complex DevOps pipelines without requiring developer configuration represents an evolution from traditional approaches, he noted.

For Java shops managing hundreds or thousands of developers across dynamic cloud environments, the promise of eliminating both redeploy delays and configuration overhead could deliver substantial productivity gains.

JRebel Enterprise is now available, with detailed information and demos accessible through Perforce’s website.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)