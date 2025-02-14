# Security Is Blocking AI Adoption: Is BYOC the Answer?
![Featued image for: Security Is Blocking AI Adoption: Is BYOC the Answer?](https://cdn.thenewstack.io/media/2025/02/defe521b-cloud-1024x576.jpg)
The landscape of [AI adoption](https://thenewstack.io/ai/) has transformed dramatically in the 18 months since ChatGPT’s debut. According to [McKinsey’s 2024 Global Survey on AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai?t), organizational AI adoption has surged from 50% to 72%, with half of the surveyed organizations implementing AI across multiple business functions, up from less than a third in 2023.

However, this wave of AI adoption presents unique challenges for regulated industries like finance and health care. While these sectors recognize AI’s transformative potential to enhance productivity and maintain competitive advantage, they face significant obstacles in implementing AI solutions at scale.

The challenge isn’t merely adopting the technology — it’s doing so while maintaining stringent security and [compliance standards](https://thenewstack.io/compliance/). For example, [49% of health care organizations fully restrict the use of generative AI](https://www.liminal.ai/case-studies-foundational-papers/generative-ai-adoption-report) due to data privacy and security concerns.

**The AI Implementation Dilemma**
Picture a typical scenario playing out in boardrooms across regulated industries: A CIO presents the results of their AI pilot program. The excitement is palpable as they showcase how their prototype AI system has reduced customer service response times by 40% while improving accuracy. The board members are impressed, and the CEO is eager to roll out the solution across the organization. Then comes the pivotal question: “How soon can we deploy this in production?”

This is where the enthusiasm hits a wall. The CIO explains that moving from prototype to production isn’t just a matter of scaling up — it’s about navigating a complex maze of security requirements, compliance regulations and operational constraints. The available paths forward each come with significant drawbacks.

## The Public SaaS Dilemma
One seemingly straightforward option is adopting public SaaS AI solutions, such as public API services for [embedding models](https://zilliz.com/ai-models?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns), large language models (LLMs) and fully managed [vector databases](https://zilliz.com/learn/what-is-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns). These platforms offer robust out-of-the-box capabilities with minimal operational overhead for users.

However, the downside is significant: Data resides in the vendor’s cloud account rather than customers’, and communications with public API services must pass through public networks. For regulated industries, this option is often a nonstarter. Security teams flag concerns about customer data traveling across public networks, compliance officers worry about data residency requirements and risk managers highlight the difficulties in maintaining audit trails and accountability when relying on third-party services.

## The Challenge of On-Premises
The alternative is to deploy everything on premises using [open source software](https://thenewstack.io/is-community-backed-open-source-software-worth-the-risk/). When executed correctly, this approach promises complete control and compliance, but it also presents its own set of challenges.

First, it requires significant investment in a dedicated DevOps team to manage on-premises deployments, troubleshoot issues and handle ongoing maintenance. The operational overhead can be daunting, and the risk of outages is higher compared to relying on expert-managed services. With AI technology evolving at a breakneck pace, keeping up with software updates and new model releases becomes nearly impossible for in-house teams. Additionally, organizations may face delays and disruptions due to a lack of specialized support when encountering production issues.

This creates what one health care CTO describes as “AI purgatory.” Organizations find themselves caught between promising prototypes and production deployment, watching as others race ahead with AI implementation. The business case for AI is clear, and the technology is proven, but the path to secure and compliant deployment remains frustratingly out of reach.

**Key Security Challenges in AI Deployment**
Enterprises face unique hurdles in adopting AI at scale. Sensitive data must remain within secure, controlled environments, avoiding public networks or shared infrastructures. Traditional SaaS models often fail to meet these stringent data sovereignty and compliance demands.

Beyond this, organizations require granular control, comprehensive auditing and full transparency to trace every AI decision and data access. This ensures vendors cannot interact with sensitive data without explicit approval and documentation. These unmet needs create a significant gap, preventing regulated industries from deploying AI solutions while maintaining compliance and security.

**BYOC: A Third Way Forward**
The concept of Bring Your Own Cloud (BYOC) isn’t new. It emerged as a middle ground between traditional SaaS and on-premises deployments, promising to combine the best of both worlds: the convenience of managed services with the control and security of on-premises infrastructure. However, its history in the industry has been marked by both successes and cautionary tales.

Early BYOC implementations often failed to live up to their promises. Some vendors merely deployed their software into customer cloud accounts without proper architectural planning, resulting in what was essentially remotely managed on-premises environments. Moreover, hosting data in a customer’s cloud account alone does not guarantee security. The vendor still has to log in to the customer’s account for troubleshooting, which could break a lot of assumptions. Achieving true security in BYOC is a unique challenge. As one industry veteran aptly described it, this approach became “[an architectural dead end](https://jack-vanlightly.com/blog/2023/9/25/on-the-future-of-cloud-services-and-byoc)” — appearing promising at first but ultimately creating more problems than it solved.

**Reimagining BYOC for AI Workloads**
The story of BYOC doesn’t end there. The rise of enterprise AI workloads has created a new context where BYOC, when implemented thoughtfully, offers distinct value. A new generation of BYOC architectures effectively addresses previous security concerns through a clear separation of control and data planes. In this model, all business logic and data processing stays within the customer’s private network, while the vendor’s control plane manages operational tasks like resource scheduling and system upgrades without accessing sensitive data. This approach goes far beyond simply deploying software in a customer’s VPC (virtual private cloud). A well-designed BYOC implementation typically includes these key characteristics:

**Data sovereignty within customer networks**: All data processing and flows remain strictly within the customer’s VPC, ensuring complete data control.**Security-first architecture**: Rather than retrofitting security into an existing design, the entire control flow is architected with security as a foundational principle.**Limited, controlled vendor access**: Vendor access is strictly limited to customer-approved operations on a just-in-time basis, with comprehensive logging of all actions.**Complete operational visibility**: The system maintains detailed audit trails of all interactions between control and data planes, particularly during troubleshooting sessions.
### The Zilliz Approach to BYOC
[Zilliz](https://zilliz.com/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns) has developed a [BYOC](https://zilliz.com/bring-your-own-cloud?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns) solution designed explicitly for vector search to meet enterprise-grade security. The architecture separates system operations into two distinct areas: control and data. Each serves a specific purpose while maintaining security boundaries.
**Clear Separation of Administration and Data**
The control plane, managed by Zilliz, acts as the management layer, handling tasks like resource scheduling and system upgrades. Think of it as a supervisor who monitors the system’s health and manages infrastructure, but never interacts with the actual data. The data plane runs entirely within the customer’s VPC and cloud account, ensuring that communications between the customer’s application servers and the vector database are contained within the customer’s VPC. All data is protected by industry-standard encryption, both in transit and at rest.

**Enterprise-Grade Network Security**
To meet enterprise network security requirements, administrative traffic is encrypted and outbound-only from the data plane to the control plane, preventing the vendor from directly accessing the customer’s VPC. AWS PrivateLink support ensures secure communication between the control plane and the data plane without exposing it to the public internet. The connection uses TLS 1.2+ over port 443/HTTPS, and can only be initiated from the customer’s data plane by default.

**Granular Access Control**
Fine-grained permission settings ensure least-privileged access to the control plane. Each permission granted to the cross-account IAM role for managing the cluster within the customer’s cloud account is carefully curated and reviewed to uphold the principle of least privilege. Access is also restricted to specific resource names or customer-defined resource tags, preventing exposure to other data within the customer’s cloud account.

**Just-in-Time Vendor Access and Audit Logging**
Vendor access to the data plane for troubleshooting is contingent on customer consent, and is tightly controlled. All access aspects — including authentication details, actions performed, authorization, contextual information, changes made and any anomalous or suspicious activities — are thoroughly logged and continuously monitored. Zilliz’s security team conducts regular audits and risk reviews to ensure compliance with security standards and quickly address any potential issues.

This approach enables organizations to continue AI innovation with production-ready vector search capabilities without compromising the control and [security necessary to meet stringent compliance requirements](https://thenewstack.io/master-difficult-user-authentication-requirements-with-oauth/).

**Looking Ahead**
While there is no one-size-fits-all solution for every AI deployment, BYOC offers a practical middle ground. It allows enterprises to leverage managed AI services while retaining the control and security necessary for compliance in regulated industries. As AI adoption continues to accelerate across sectors, approaches like BYOC will be essential for organizations striving to balance innovation with stringent security and compliance demands. If you are interested in bringing a vector database with enterprise-grade security to your application, consider checking out the Zilliz Cloud BYOC [documentation](https://docs.zilliz.com/docs/byoc/byoc-intro#how-it-works?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns) for more details.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)