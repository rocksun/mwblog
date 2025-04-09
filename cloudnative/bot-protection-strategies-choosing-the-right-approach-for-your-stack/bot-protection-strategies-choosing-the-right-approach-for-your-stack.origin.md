# A Cloud Native Approach for Protecting Against Bad Bots
![Featued image for: A Cloud Native Approach for Protecting Against Bad Bots](https://cdn.thenewstack.io/media/2025/04/b913ec79-bots12-1024x576.png)
[Bot traffic](https://thenewstack.io/can-you-bot-proof-your-applications-and-apis/) is divided between beneficial and malicious bots. Beneficial bots, like search engine crawlers, uptime monitors and archival services, typically respect site policies and contribute value. Malicious bots engage in data scraping, credential stuffing, DDoS attacks and spam campaigns, often ignoring traditional access controls like `robots.txt`
.
Recent reports show that about [half of all web traffic is bots](https://securitybrief.co.uk/story/half-of-online-traffic-in-2024-generated-by-bots-report-finds), and “bad” bots make up a [rising percentage](https://www.statista.com/statistics/1264226/human-and-bot-web-traffic-share/). AI bots are a growing portion of this traffic, with some companies showing up to [90% of their AI bot traffic](https://www.haproxy.com/blog/nearly-90-of-our-ai-crawler-traffic-is-from-tiktok-parent-bytedance-lessons-learned) coming from a single source. These crawlers often bypass existing protections by mimicking legitimate users, requiring more advanced solutions that combine traffic analysis with [bot detection](https://www.haproxy.com/blog/bot-protection-with-haproxy) algorithms for accurate identification.

Infrastructure diversity increases the challenge. Organizations run workloads across bare metal servers, Kubernetes clusters and serverless platforms — each with its own security constraints and requirements. This creates the “multi-multi” problem: multiple tools protecting multiple stacks across multiple environments, each with distinct needs. According to the [OWASP Automated Threats project](https://owasp.org/www-project-automated-threats-to-web-applications/), this heterogeneous landscape makes an approach based on independent services increasingly ineffective.

This issue is complex, but we can manage it in three layers: traffic management to control requests at the entry point, policy-driven security to manage security at scale, and edge protection to stop threats before they reach internal systems. A [cloud native approach](https://thenewstack.io/cloud-native/10-key-attributes-of-cloud-native-applications/) unifies these layers, ensuring adaptable, scalable security that evolves with emerging threats.

## Traffic Management
Open source proxies are a standard solution for those seeking greater control and performance in traffic management. Proxy-level implementations add minimal latency compared to third-party services, yet provide robust bot mitigation. These technologies use multiple defense mechanisms to identify and block malicious traffic patterns, including advanced rate-limiting systems, [access control lists](https://thenewstack.io/a-guide-to-linux-access-control-lists/) (ACLs ) and flexible response policies to counter evolving bot threats.

It is crucial to have a rate-limiting system that effectively mitigates evolving bot threats while maintaining minimal resource overhead and false positives. Effective systems combine flexible algorithms with multiple identification methods — tracking IP addresses, browser fingerprints, session cookies, requested URLs and custom headers as composite keys. This approach should incorporate allow/deny lists, geolocation-based restrictions and adaptive rate-limiting rules that detect patterns across various attack vectors, including brute-force attempts, web scraping and session hijacking.

Based on specific threat profiles, both sliding window and fixed window rate limiting can be deployed. As attackers continuously modify their techniques, the system must remain adaptable without sacrificing performance. Further enhancements include distributed rate limiting across clusters and dynamic threshold calculations based on historical profiling.

For example, proxies use technologies such as [stick tables](https://docs.haproxy.org/3.1/intro.html#3.4.5) in [HAProxy](https://www.haproxy.com/?utm_content=inline+mention) or [shared memory zones](http://nginx.org/en/docs/dev/development_guide.html#shared_memory) in [NGINX](https://www.nginx.com?utm_content=inline+mention) to enable real-time monitoring of request patterns and help detect malicious activities like DDoS attacks, credential stuffing and web scraping.

Response policy options may include challenging requests with a CAPTCHA (either visible or invisible), limiting response bandwidth or directing requests to a honeypot. Furthermore, if backends are overloaded, priority-based queuing can give precedence to certain requests (such as logged-in users) over others.

Traffic management becomes even more powerful when using custom resource definitions (CRDs) to enable declarative traffic policy configuration. Teams can define sophisticated bot protection rules as [native Kubernetes resources](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/), using GitOps workflows and standardizing policy management across clusters. Integrating with a cloud native security model ensures consistent, scalable protection.

## Policy-Driven Security
To address the “multi-multi” problem, organizations need a unified strategy that integrates traffic management with platform-level policy-driven security. This approach enables fine-grained traffic control, [policy enforcement and real-time observability](https://thenewstack.io/real-time-policy-enforcement-with-governance-as-code/).

Cloud native technologies enable the separation of concerns: A centralized [control plane](https://www.haproxy.com/glossary/what-is-a-control-plane) manages security policies, while distributed [data planes](https://www.haproxy.com/glossary/what-is-a-data-plane) enforce those policies at the traffic-processing layer. This architecture allows teams to adapt protection levels contextually without duplicating effort, ensuring consistent security (and compliance) across different environments.

A unified control plane architecture can offer significant advantages over standalone security control planes often provided by bot protection providers. These advantages include reduced latency, simplified operations and the ability to incorporate other native delivery and security capabilities. Furthermore, a unified control plane can simplify the complexities of implementing a multilayered security policy by automatically combining lower-level security building blocks with threat-focused mitigation strategies.

Observability completes this feedback loop, transforming reactive security into a proactive practice. [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver) instrumentation enables teams to trace suspicious request patterns, while [Prometheus](https://prometheus.io/blog/2015/04/24/prometheus-monitring-spreads-through-the-internet/#using-prometheus) metrics provide real-time anomaly detection. Real-time visibility allows teams to continuously improve their defenses by adjusting rate limits, IP reputation scores and targeted countermeasures.

## Edge Protection
Edge-layer security enhances performance and reduces the attack surface by filtering high-risk traffic. A well-designed edge network not only strengthens security and improves the user experience but also lowers infrastructure costs by offloading bot mitigation and optimizing resource consumption.

AI-powered detection at the edge is essential, using actual traffic patterns to refine bot mitigation strategies dynamically. Machine learning models continuously adapt to emerging threats, ensuring defenses remain effective at scale. Rather than performing resource-intensive analysis on each request, systems should regularly analyze the traffic across the network with machine learning to identify new threats and patterns, then update filtering algorithms in real time to maintain efficiency without adding latency.

While managed edge services simplify operations, building your [own cloud native edge network](https://www.haproxy.com/user-spotlight-series/how-oui-sncf-built-its-cdn-with-haproxy) offers greater control, cost efficiency and flexibility. A cloud native approach makes this possible with the same tools that power traffic management and platform-level orchestration, ensuring seamless integration and scalability. A self-managed edge provides customized security policies, reduces reliance on third-party services and enables a unified stack that applies the same cloud native principles across all layers for consistent, scalable security.

## Designing Your Approach
The choice of bot protection strategy depends on organizational context, including technical expertise, scalability needs and compliance obligations. Bot protection should start with proxy-level controls, enforcing rate limiting and access policies at the data plane to mitigate immediate threats.

At scale, policy-driven security and unified control plane solutions ensure consistent enforcement across distributed environments. Organizations should adopt cloud native solutions that unify internal and external protections for long-term security consistency. Kubernetes and GitOps workflows enable scalable, automated security enforcement that evolves with emerging threats.

Edge security provides an extended line of defense for external traffic, filtering malicious requests before they reach internal infrastructure. This approach minimizes attack surface exposure while preserving performance for legitimate users.

By layering these approaches, organizations can implement adaptive, scalable bot mitigation, ensuring their infrastructure remains secure without compromising efficiency and simplicity.

*To learn more about Kubernetes and the cloud native ecosystem, join us at KubeCon + CloudNativeCon Europe in London on April 1-4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)