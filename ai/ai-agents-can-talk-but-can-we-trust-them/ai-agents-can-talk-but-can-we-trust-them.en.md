Ever since Google released the Agent2Agent (A2A) protocol, followed by the Agent Communication Protocol (ACP) from IBM/BeeAI, the promised result has been a multi-agent ecosystem where agents communicate with each other autonomously and complete tasks without human intervention.

Consider this simple use case.

In the real world, you would typically call your travel agent, who would then contact other individuals to book flight tickets or plan activities by calling the tour guides. In the agentic future (or present!), your travel agent would be replaced by an [AI agent that talks with other AI agents](https://thenewstack.io/agentic-ai-for-enterprises-4-key-benefits-driving-innovation/), which book tickets or plan activities. (At this point, we won’t delve deeper into how these agents do these tasks, whether by using MCP tools or invoking other agents.)

The critical point to be kept in mind is that these agents could be operating across organisational boundaries. You may be interacting with an agent on a site like Expedia or Booking.com. The ticket booking agent could belong to the airline company, and online tour guide companies like Showaround or TourHQ could own the activity planner agent.

While A2A and ACP (called “the protocols” from hereon) have given a common “language” and set of rules for agents to be discovered, share context, and communicate, regardless of the underlying technology stack they use, cross-organisational agent interactions add significant complexity and risk.

In this post, let us talk about some of these challenges and see how they can be solved using existing technologies, and identify the gaps.

## The Challenges of Creating Audit Trails

When multiple agents collaborate on a task, tracking decision-making becomes exponentially complex.

Consider another slightly more complex use case. A company has a SaaS application and uses both AWS and Azure (or GCP, I have nothing against them!) for the underlying infrastructure. Both these platforms have SRE agents that can help debug and fix any infrastructure problems. The company has its own SRE [agent who talks to these platform](https://thenewstack.io/gitlab-launches-its-ai-agent-platform-in-public-beta/) agents, providing them with context and additional information.

Consider the following sample incident and resulting audit trail chain:

```
Incident: Database connection timeouts causing 500 errors
Audit Trail Chain

1. [10:15:32] Company-SRE-Agent: Detected high error rate (23% 500 errors)
   - Data source: Application logs, metric aggregation
   - Decision: Escalate to infrastructure investigation

2. [10:15:45] Company-SRE-Agent → AWS-SRE-Agent: 
   - Request: "Analyze RDS performance for db-prod-cluster"
   - Credentials exchanged: Temp access token with read-only RDS permissions
   - Authentication: Certificate chain verified

3. [10:16:12] AWS-SRE-Agent: Analysis complete
   - Finding: "CPU utilization normal, connection pool at 98% capacity"
   - Recommendation: "Scale connection pool or investigate connection leaks"
   - Data accessed: RDS CloudWatch metrics, connection pool stats

4. [10:16:20] Company-SRE-Agent → Azure-SRE-Agent:
   - Request: "Check Application Gateway backend health"
   - Cross-cloud context: Shared incident ID #INC-2024-0610-001

5. [10:16:35] Azure-SRE-Agent: Analysis complete
   - Finding: "Backend pool showing intermittent health check failures"
   - Root cause identified: Network latency spikes between regions

6. [10:16:50] Company-SRE-Agent: Correlation analysis
   - Decision: Implement connection retry logic + scale RDS connections
   - Actions taken: Deployed config update, scaled RDS
```

This scenario highlights several audit trail challenges:

1. **Data sovereignty:** AWS-SRE-Agent accessed the RDS data  —  is there a record of exactly what data was shared?
2. **Decision attribution:** If the fix fails, was it the Company agent’s correlation logic or the cloud agents’ recommendations?
3. **Compliance:** Is there any proof that only [authorized agents accessed](https://thenewstack.io/agentic-access-is-here-your-authorization-model-is-probably-broken/) production systems?
4. **Cross-platform correlation:** How do we merge audit logs from three different organizations’ systems?

Both protocols give a bunch of features that help in creating basic audit trails for inter-agent communication. Most importantly, a common language provides structured message formats that [standardize how agents exchange information to ensure that message data](https://thenewstack.io/vex-standardization-for-a-vulnerability-exploit-data-exchange-format/) can be consistently logged. The protocols also offer basic conversation tracking through IDs and message threading, which allows sequential grouping of related messages, helping in following the flow of a single, multistep dialogue. They also make it possible to identify any agent using standardized sender/receiver addressing schemes and basic temporal ordering of the messages using timestamps.

And what the protocols don’t give:

* **Semantic decision logging:** Protocols focus on message format, not reasoning content. This lack of semantic decision logging ignores the context, making reasoning chain reconstruction difficult.
* **Federated audit standards:** It becomes nearly impossible to correlate audit trails from different companies’ agent networks and hence trace which agent influenced which decision.
* **Tamper-proof audit trails:** Without built-in cryptographic verification, it is difficult to trust the integrity and correctness of the logs.

This is not to say that current [systems can’t capture audit trails of agentic](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) systems at all. Far from it! Many cross-organizational systems communicate using synchronous (REST APIs) or asynchronous (e.g., message queues) mechanisms and use either OOTB tools and technologies (shared Kafka cluster, Redis streams, blockchain, etc.) or industry-specific solutions to manage the audit trails. The problem is that these pre-existing solutions answer questions like:

* WHO called WHAT service WHEN
* WHO accessed WHICH data
* WHAT errors occurred WHERE

Whereas for agentic systems, we also need to know:

* Why did the agent make the specific decision?
* HOW agents influenced each other.
* WHAT reasoning led to outcomes?
* WHETHER agents are behaving as designed.

In short, much of the infrastructure is available, but needs to be extended with agent-aware capabilities that can track the “why” and “how” of agent decisions, not just the “what” and “when.”

## Ensuring Agent Authenticity and Capability

Both protocols use capabilities advertised by agents to discover the correct agents for the right job. For example, if an agent needs to generate a summary of a document, it can query a registry or a discovery endpoint to find another agent that has “document summarization” listed as one of its capabilities.

But how can we ensure that an agent is as capable as it claims to be?

An agent may lie about its capabilities in the following ways:

* **Capability inflation:** Agent embellishes its abilities. E.g., it claims to have advanced reasoning abilities but uses simple rule-based responses. This is probably harmless for an agent doing document summarization, but could be catastrophic for an agent doing advanced analysis for stock prices.
* **Credential spoofing:** Agent presents fake certifications or training provenance.
* **Performance degradation:** Agent had advertised capabilities initially, but has degraded with time and did not update its capability.

The protocols address agent authentication and registration, and existing infrastructure can handle identity verification, which is about 80% of the way there. Certificates can be used to confirm an agent’s organizational identity, and digital signatures or mTLS to ensure messages are authentic and connections are secure.

However, there are no standard solutions for capability attestation (proving an agent’s claims of capabilities), training provenance (verifying the authenticity of its training data or model), or capability drift detection (identifying the performance/result drift).

Since modern problems need modern solutions, we either need to come up with newer solutions or use existing solutions to augment these.

For example, continuously monitoring an agent’s performance against a baseline, using tools like benchmarking pipelines or model drift detection frameworks, will help in ensuring it’s still capable of performing its job as advertised. Using new methods for signing models will assist in verifying the agent’s model. Capability attestation is a tricky problem and will need benchmarking services that can act as “IQ tests for AI”. Running these pipelines and services at scale could be an engineering problem worth solving!

The protocols assume agents are honest about their capabilities, which is an obvious first step. Still, if our experience with software has taught us anything, it is that not all actors in a system are always trustworthy.

This is a nice segue to our last problem.

## The Threat of Malicious Agents

An agent lying about its capabilities can significantly hamper the system’s performance, but what if the agent is actively malicious and has been created to harm a system?

This is not a futuristic dystopian scenario but something that is happening at present. (Read [here](https://www.technologyreview.com/2025/04/04/1114228/cyberattacks-by-ai-agents-are-coming/) and [here](https://thehackernews.com/2025/03/how-new-ai-agents-will-transform.html).) You would already have read the [OWASP Top 10 GenAI security risks](https://www.lasso.security/blog/owasp-top-10-llm-vulnerabilities-security-checklist#owasp-top-10-for-large-language-model-llm-applications-with-examples), which can impact the models and AI applications. Hence, it [becomes even more critical](https://thenewstack.io/software-developers-are-becoming-critical-members-in-the-us-space-force/) that these recommendations are followed when developing agentic systems.

However, there are some challenges that are unique to multi-agent systems:

1. **Social Engineering at scale:** Agents can manipulate other agents through conversation, asking for sensitive or confidential [data or manipulating consensus by compromising the voting/decision-making process](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/).
2. **Prompt Injection:** A compromised agent could inject malicious prompts into conversations with other agents, causing downstream agents to execute unintended actions and propagate malicious instructions across the agent network.
3. **Information Cascade Failures:** A malicious agent can provide corrupted or biased information to degrade performance, or give wrong results, and these errors or biases get amplified as they spread through agent networks.
4. **Trojan Capabilities:** The agent may perform legitimate functions, but also may have hidden malicious behaviours.

As you would see, the biggest unsolved problem is semantic security, protecting against threats that operate at the meaning/content level rather than just the technical level. Traditional security assumes deterministic, predictable systems. Agent security requires defending against systems that can be creative, adaptive, and deceptive.

Some of these challenges can be tackled by using existing solutions and practices. Using sandboxed collaboration (isolated environments) and network segmentation (protected network zones) for untrusted agent interactions can be a crucial but straightforward approach to safeguard against malicious agents.

However, to combat conversational manipulation, we’ll need new solutions, such as “conversational firewalls” that analyze the meaning behind communications and influence-detection algorithms that can spot manipulation attempts. Red Teaming can play a critical role in hardening our agents against such attacks.

We previously discussed benchmarking pipelines to monitor external agents’ behavior and performance to catch performance drift. These pipelines can also be run for our agents to constantly [monitor data quality](https://thenewstack.io/the-new-face-of-data-quality-anomalo-and-automated-monitoring/) trends and detect any seeping errors or bias in their responses. The system design could also be updated to employ cross-validation systems where multiple agents verify critical information.

The agent communication protocols, while a significant first step, still have a long way to go to ensure [security and trust in a multi-agent ecosystem](https://thenewstack.io/the-challenges-of-securing-the-open-source-supply-chain/). While they provide the “language” for agents to talk to one another, they don’t solve the more complex challenges that arise from cross-organizational interactions. While some existing tools and practices can help, we ultimately need new, agent-aware solutions to tackle these issues. The future of a safe, reliable agentic ecosystem depends on our ability to build these solutions.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/08/fecf91a5-1614746241814.jpeg)

Architect with nearly two decades of experience in software development. Specializes in cloud-native solutions and enterprise-grade applications. Loves tech and photography, in often oscillating order.

Read more from Abhishek Asthana](https://thenewstack.io/author/abhishek-asthana/)