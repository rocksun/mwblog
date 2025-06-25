More organizations than ever are deploying AI models, whether through managed cloud services or self-hosted solutions. According to [The State of AI in the Cloud 2025](https://www.wiz.io/reports/the-state-of-ai-in-the-cloud-2025) report from cloud security provider Wiz, 85% of organizations now use AI services, up from 70% in 2024. With this growth comes more integrations, tools and security risks.

Platform engineers are on the front lines of securing these AI systems, especially as [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) enter production. While cloud-hosted LLMs pose significant security challenges, self-hosted models, such as [Meta’s LLaMa](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/), introduce even greater complexity. Self-hosting provides more control over security, customization and costs, but also expands the attack surface.

[Platform engineers](https://thenewstack.io/platform-engineering/) must understand the key threats that LLMs pose and apply effective defensive measures to deploy AI securely. The six most pressing risks that we’ll explore are:

1. Prompt injection attacks
2. Model extraction and theft
3. Private data leaks
4. Resource management and cost control challenges
5. Infrastructure and API security vulnerabilities
6. Performance and scalability limitations

Let’s break down each of these risks and how to mitigate them.

## 1. Watch Out for Prompt Injection

Prompt injection is the AI-era equivalent of SQL injection. Attackers craft malicious inputs to manipulate an LLM, bypass safeguards or extract sensitive data. These attacks range from simple jailbreak prompts that override safety rules to more advanced exploits that influence backend systems.

For example, an attacker might inject SQL-like syntax into prompts to manipulate database-connected applications or exploit model vulnerabilities to reveal internal system instructions. Left unchecked, these risks can expose confidential processes and compromise AI-driven workflows.

To reduce the risk of prompt injection, implement these key defenses:

* **Input validation:** Filter and sanitize user prompts at the API gateway.
* **Context-aware filtering:** Use AI-based detection to identify manipulation attempts.
* **Web application firewall (WAF) rules:** Deploy WAF rules to detect and block malicious prompt patterns.
* **Rate limiting:** Prevent repeated adversarial queries that could expose vulnerabilities.

## 2. Protect Your Model’s Intelligence

[Model extraction](https://thenewstack.io/microsoft-machine-learning-models-can-be-easily-reverse-engineered/) attacks allow adversaries to systematically query an LLM to reconstruct its knowledge base or training data, essentially cloning its capabilities. These attacks often rely on automated scripts submitting millions of queries to map the model’s responses.

One common technique, model inversion, involves strategically structured inputs that extract sensitive or proprietary information embedded in the model. Attackers may also use repeated, incremental queries with slight variations to amass a dataset that mimics the original training data.

To prevent unauthorized model extraction, implement these key defenses:

* **Advanced rate limiting:** Control usage per user, IP and API key to prevent automated scraping.
* **Token-based rate limiting:** Restrict the number of requests per user session to curb excessive querying.
* **Response randomization:** Introduce slight variations in outputs to disrupt pattern analysis.
* **Behavioral analytics:** Detect and block suspicious query patterns indicative of extraction attempts.

## 3. Keep Private Data Private

LLMs introduce significant privacy and regulatory risks from both user input and model output. Users may unintentionally submit sensitive data, while models can generate responses that expose confidential details from training data or past interactions.

On the output side, an LLM might inadvertently reveal private information embedded in its dataset or previously entered user data. A common risk scenario involves users unknowingly submitting financial records or passwords into an AI-powered chatbot, which could then store, retrieve or expose this data unpredictably. With cloud-based LLMs, the risk extends further. Data from one organization could surface in another’s responses.

To mitigate private data leaks, apply these key protections:

* **Personally identifiable information (PII) detection and redaction:** Automatically scan and sanitize inputs and outputs for PII.
* **Data leak prevention (DLP):** Monitor responses for sensitive content exposure and enforce compliance policies.
* **Strict access controls:** Restrict who can interact with and retrieve model responses.
* **Conversation history management:** Prevent multitenant environments from exposing data across users.

## 4. Manage Resources and Control Costs

Running an LLM is expensive. Cloud-based LLM billing can escalate quickly, while self-hosting demands the deployment of high-performance GPUs and significant additional infrastructure investment. Without proper controls, resource consumption can degrade platform performance and drive up costs.

Self-hosted models require strict enforcement of usage limits to prevent excessive token consumption and performance slowdowns. Meanwhile, organizations using cloud APIs risk unexpected overages if users submit long prompts that trigger high token processing costs.

To optimize resource usage and control costs, implement these key strategies:

* **Real-time monitoring:** Track GPU utilization and token consumption.
* **Request quotas:** Set per-tenant usage limits to prevent resource overuse.
* **Token-based rate limiting:** Restrict excessive token processing to control spending.
* **GPU-aware scheduling and load balancing:** Distribute inference workloads efficiently across multiple instances.

## 5. Secure Your Infrastructure and APIs

Misconfigured infrastructure is a major attack vector. Exposed debug endpoints, weak authentication and insecure APIs can lead to unauthorized access. Shadow APIs — undocumented or forgotten endpoints that unintentionally expose model capabilities — are a particularly dangerous risk.

For example, a misconfigured Kubernetes ingress controller could unintentionally expose an internal API to public traffic, allowing unauthorized queries to bypass security controls.

To secure LLM infrastructure and APIs, implement these key protections:

* **Strong authentication:** Use OAuth2 or JWT tokens to enforce API access control.
* **Mutual TLS (mTLS):** Encrypt service-to-service communications for secure data exchange.
* **Network segmentation:** Isolate model endpoints to minimize exposure to attacks.
* **Regular security audits:** Continuously scan for misconfigurations and unauthorized access.

## 6. Optimize Performance and Scale Efficiently

LLMs demand significant resources, and performance bottlenecks become inevitable as usage grows. Cold-start latency is a major challenge; model instances can take too long to initialize during traffic spikes. Inefficient GPU utilization further degrades performance, especially in self-hosted deployments with limited resources, and adds unneeded cost. Additionally, highly concurrent queries can overwhelm the system, causing delays and reducing throughput.

To optimize performance at any scale, implement these key strategies:

* **GPU-aware autoscaling:** Use tools like KEDA to scale resources dynamically.
* **Caching strategies:** Reduce redundant inference calls to improve response times.
* **Model optimization:** Deploy multiple models for different workloads and route users accordingly.

## The Future of LLM Security

Securing AI systems is an ongoing battle. As new threats emerge, staying ahead requires continuous monitoring, regular security audits and adoption of the latest defense strategies. The challenge is finding the right balance — too much security can slow performance and raise costs, while too little puts sensitive data at risk.

By taking a proactive, strategic approach, platform engineers can keep AI deployments secure, efficient and valuable, without unnecessary trade-offs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/02/b9306f49-cropped-10957b1b-screenshot-2025-02-21-at-7.53.08%E2%80%AFam-600x600.png)

Ron Northcutt is the director of technical marketing at HAProxy Technologies, where he focuses on performance metrics, developer content, and deep industry knowledge to drive technical innovation and engagement. With over 25 years of experience in the open source ecosystem,...

Read more from Ron Northcutt](https://thenewstack.io/author/ron-northcutt/)