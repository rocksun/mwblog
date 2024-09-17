# Why Cloud Migrations Fail
![Featued image for: Why Cloud Migrations Fail](https://cdn.thenewstack.io/media/2024/01/9347d1ba-ai-iot-cloud-to-edge-1024x576.jpg)
[Nearly 60% of IT leaders](https://thenewstack.io/cloud-migrations-pick-up-the-pace-in-2024/)plan to migrate more workloads to the cloud this year.
Understandably, [the promise of scalability](https://thenewstack.io/how-to-build-a-scalable-platform-architecture-for-real-time-data/), cost savings and enhanced collaboration make this a compelling proposition. However, it’s a nuanced and sizable undertaking that admittedly requires time, attention and a commitment to safe and effective use.

Occasionally, [cloud migrations](https://thenewstack.io/cloud-migrations-pick-up-the-pace-in-2024/) become so complex or unwieldy that [they fail to deliver the anticipated benefits](https://thenewstack.io/cloud-migration-regrets-should-you-repatriate/), leading to cost overruns and delays or an overreliance on third parties. Ultimately, copying and pasting a roadmap derived from a handful of well-intentioned but perhaps overhyped case studies simply doesn’t work.

Here, I’ll review the top three reasons cloud migrations can fail and offer some critical guidance that may help enterprise security teams and decision-makers right the ship.

**The Shared Responsibility Model**
One stumbling block on the cloud journey is misunderstanding or confusion around [the shared responsibility model](https://www.techtarget.com/searchcloudcomputing/definition/shared-responsibility-model). This framework delineates the security obligations of cloud service providers, or CSPs (which comes down to securing the underlying infrastructure), and customers (that is, safeguarding data, access, applications and configurations). The model necessitates a clear understanding of end-user obligations and highlights the need for collaboration and diligence.

Broad assumptions about the level of security oversight provided by the CSP can lead to security/data breaches that the U.S. National Security Agency (NSA) [notes](https://media.defense.gov/2024/Mar/07/2003407863/-1/-1/0/CSI-CloudTop10-Shared-Responsibility-Model.PDF) “likely occur more frequently than reported.” It’s also worth noting that 82% of breaches [in 2023](https://www.wsj.com/tech/cybersecurity/why-are-cybersecurity-data-breaches-still-rising-2f08866c) involved cloud data.

The confusion is often magnified in cases of a cloud “lift-and-shift,” a method where business-as-usual operations, architectures and practices are simply pushed into the cloud without adaptation to their new environment. In these cases, organizations may be slow to implement proper procedures, monitoring and personnel to match the security limitations of their new cloud environment.

While the level of embedded security *can *differ depending on the selected cloud model (Software as a Service, Infrastructure as a Service, Platform as a Service), the customer must often enact strict security and [identity and access management (IAM)](https://thenewstack.io/getting-started-with-identity-and-access-management/) controls to secure their environment. Today, the latter has become increasingly vital, considering that [nearly 40%](https://www.cybersecuritydive.com/news/exploits-credentials-fuel-ransomware-surge/717943/) of all ransomware incidents 2023 began with compromised, legitimate credentials.

In its guidance, the [NSA](https://media.defense.gov/2024/Mar/07/2003407863/-1/-1/0/CSI-CloudTop10-Shared-Responsibility-Model.PDF) also warns: “Customers often assume the CSP’s responsibility to protect customer data is broader than it is, leading to the customer failing to take needed actions.”

As such, cloud users must develop and pressure-test incident response playbooks, actively hunt for intrusions, deploy [multifactor authentication](https://thenewstack.io/73-of-organizations-dont-enforce-multifactor-authentication/), and perhaps most importantly, carefully review the “fine print,” aka their [service-level agreements (SLAs)](https://thenewstack.io/ignoring-slas-doesnt-pay/) with the provider.

**Data Sovereignty Hurdles**
I’d be remiss not to mention another elephant in the room: compliance. According to a 2024 Cloud Security Alliance report, 61% of IT and security leaders recently cited alignment on compliance standards as a top challenge in SaaS environments. Regulations add layers of complexity, particularly regarding timely considerations like “data sovereignty”—or when data is subject to the laws and regulations of the country in which it is stored or processed.

Enforcement around data localization laws has ticked up globally, partly due to stipulations in more sweeping regulations like the European Union’s [General Data Protection Regulation (GDPR)](https://gdpr.eu/what-is-gdpr/) and the [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa). Each imposes strict guidelines on data privacy and protection for its constituents, including mandates on how the data should be handled, stored, and transferred.

This can present new challenges for enterprise teams, which in turn must develop comprehensive governance frameworks that include, for instance:

- Encryption practices
- Strict CSP selection criteria (including choosing those with local data centers)
- Mandatory, ongoing audits and more
Overall, embarking on a cloud migration without first considering the regulatory implications can increase costs, slow progress, and potentially necessitate a complete redesign as controls are retrofitted.

**Post-Migration Oversight**
The cloud journey continues once data and applications have shifted. Proper management demands an effective cloud operations team for vital support functions, including:

- Performance monitoring to detect and resolve issues
- Ongoing security assessments to protect against known and zero-day vulnerabilities
- Identity controls to manage access to cloud apps
- Cost management to prevent budget overruns
- A process for decommissioning resources to reduce the risk of cloud sprawl or spiraling costs
As the tech-training platform, [InfoSec Institute warns](https://www.infosecinstitute.com/resources/cloud/the-rise-of-cloud-computing-trends-and-predictions/), “[Cloud] is more complex [than on-premises] and requires knowing…fundamentals and principles.” It adds: “Ignoring the new paradigms…creates substantial risk.” I couldn’t agree more.

Organizations must plan for permanent oversight and broach the subject at project inception.

**Ensuring a Smooth Journey**
Despite its challenges, the cloud holds immense promise and offers measurable cost savings as teams ditch significant, upfront investments in physical infrastructure.

With bespoke design, proven controls and effective management, businesses can ensure a smoother cloud journey and unlock its full benefits. Experienced and/or open-minded leadership and core technical staff will also smooth the transition.

Every organization will have a unique path. Still, with proper guidance, teams can avoid clunky, expensive or risky processes, and flourish in the cloud.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)