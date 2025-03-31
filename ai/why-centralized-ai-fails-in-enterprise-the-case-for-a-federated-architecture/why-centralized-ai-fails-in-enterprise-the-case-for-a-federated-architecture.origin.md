# Why Centralized AI Fails in Enterprise: The Case for a Federated Architecture
![Featued image for: Why Centralized AI Fails in Enterprise: The Case for a Federated Architecture](https://cdn.thenewstack.io/media/2025/03/58b3b4df-alex-kotliarskyi-qbpzgqemskg-unsplash-1024x683.jpg)
As companies look to deliver value and ROI from their AI investments, one critical challenge threatens to derail these initiatives. The problem? Traditional AI implementation [strategies require centralizing data](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/) from diverse sources, an approach that conflicts with enterprise governance policies, security frameworks, and regulatory obligations.

According to analyst surveys, [90% of enterprises have already developed a multicloud strategy](https://thenewstack.io/multicloud-why-its-the-best-choice-for-data/), with data distributed across various systems. This reality makes the conventional “copy all your data to one place” approach inefficient and often completely unfeasible for enterprise-scale implementations.

**The Fatal Flaw in Centralized AI Systems**
Centralizing data creates multiple governance problems that become increasingly unmanageable at scale. When organizations create new copies of data from source systems in a central AI repository, they introduce significant challenges:

**Data accuracy:**Working with “fresh,” timely data is challenging when AI systems rely on outdated duplicate copies**Governance complexity**: Each[data copy creates another instance that must be managed](https://thenewstack.io/aws-brings-trusted-extension-support-to-managed-postgres/)according to organizational policies**Compliance risks**: GDPR’s “right to be forgotten” and similar regulations become exponentially more difficult to enforce when user data exists in multiple locations**Access control degradation**: Carefully designed permissions in source systems often devolve to lowest-common-denominator controls in centralized repositories**Security vulnerabilities**: Centralized data stores present attractive targets with potentially catastrophic breach impacts
The biggest challenge is that for many enterprises, even the idea of centralizing all data in one source is a no-go position — governance and privacy concerns make this legally and technically impossible.

**Federated Architecture: A Data-Centric Approach**
The solution lies in a successful architectural pattern in data engineering: a federated architecture, also known as a [data mesh design](https://thenewstack.io/designing-a-data-mesh-to-reign-in-data-sprawl/) pattern. This approach fundamentally reimagines how AI systems interact with enterprise data.

In a federated architecture:

- Data remains in its source systems where it belongs
- Governance, access controls, and compliance remain localized to each data domain
- Processing occurs where the data resides, respecting existing security boundaries
- Only results are temporarily centralized for analysis and presentation
This pattern isn’t theoretical — organizations like Capital One have successfully implemented [data mesh architectures at scale](https://www.capitalone.com/tech/cloud/data-mesh-for-data-governance/). These organizations maintain governance while unlocking analytical capabilities by keeping [data](https://thenewstack.io/python-mqtt-tutorial-store-iot-metrics-with-influxdb/) in its natural domain and bringing compute resources to the data (rather than the reverse).

**AI Agents in a Federated System**
The federated approach extends naturally to AI implementation. Rather than one central AI accessing all data, a federated AI system deploys specialized agents across different data domains.

In this model:

- A coordination layer delegates tasks to domain-specific AI agents.
- Each agent specializes in its data domain with targeted capabilities.
- Agents process data locally and return only results.
- No persistent copies of data are created outside source systems.
This mirrors effective organizational structures. If you’re the CEO of a company and you give your leadership team a task, it’s not like one person goes everywhere and does all the work. It’s delegated to people with the necessary expertise, access, and knowledge to operate in their domains. Then, the information is brought back together and presented to the CEO as the outcome. We can use the same approach with AI agents.

This approach enables organizations to leverage specialized AI models optimized for specific systems. For example, Salesforce Einstein can process Salesforce data, while a different agent might handle Atlassian data — each operating in its domain of expertise.

**Identity and Access Controls in Federated AI**
One critical challenge in this architecture is maintaining proper access controls. The solution is “identity pass-through” — when users interact with AI, their identity and permissions are passed through to all underlying systems.

Most IT systems are built on Role-Based Access Controls (RBAC), which means that an AI system needs to consider a user’s [role before determining if someone can see certain data](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/) categories, such as Social Security numbers. When training data is combined, this centralized data creates a “least common denominator” problem, where all data is opened up to the lowest RBAC access level, creating privacy and security issues.

For an AI system to honor these controls, these RBAC controls need to be checked in real time as data is accessed.

In a federated system where the AI coordinates with domain-specific agents, each agent essentially acts as the requesting user, ensuring the AI agent only accesses information that the specific user is authorized to see. This means:

- The same query by different users returns individualized results based on the user’s role and permissions
- Changes to access controls in source systems are immediately reflected in AI interactions
- Governance remains in the systems designed to enforce it
This approach eliminates the need to duplicate complex permission structures or maintain multiple access [control systems in sync — a task that inevitably leads to security](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/) gaps.

**Addressing Compliance and Regional Data Requirements**
The federated architecture provides elegant solutions to regulatory challenges like GDPR and CCPA compliance. The AI system inherits these capabilities since data remains in source systems that are already implementing compliance controls.

For example, when handling “right to be forgotten” requests:

- The request is implemented in the source system as usual
- The AI system has no persistent copies to manage
- Future queries immediately reflect the updated data state
This approach is especially valuable for multinational enterprises operating under different regulatory regimes. Data in European systems can remain compliant with GDPR while US-based systems adhere to local requirements, with no need to reconcile these differences in a central repository.

Unlike systems that fine-tune [models on user data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/) (creating persistent artifacts that may violate deletion requests), our federated AI system uses data as runtime context. When source data changes or is deleted, subsequent AI interactions reflect those changes without model retraining.

**Moving Beyond Proofs of Concept**
For many enterprises, a federated architecture isn’t a choice — it’s the practical, governed difference between AI remaining a limited proof-of-concept and becoming a production capability. Without this approach, organizations often resort to small pilots using limited [data sets, never realizing AI’s full potential to use different data sources across a company](https://thenewstack.io/can-companies-really-self-host-at-scale/).

With a federated approach to AI, a company can derive massive value from visibility into all [data sources and automate business processes](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/) with AI. This not only reassures an information security team but also makes implementation possible.

By adopting federated AI architectures, enterprises can align their AI strategies with existing governance frameworks, security requirements, and compliance obligations. This unlocks AI’s transformative potential while maintaining the controls that protect their business and customers.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)