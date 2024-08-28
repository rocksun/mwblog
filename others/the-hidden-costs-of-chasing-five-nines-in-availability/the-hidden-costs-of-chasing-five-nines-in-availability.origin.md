# The Hidden Costs of Chasing Five 9s
![Featued image for: The Hidden Costs of Chasing Five 9s](https://cdn.thenewstack.io/media/2024/08/b902d86d-servers-1024x576.jpg)
Achieving five nines (99.999%) availability is a benchmark of excellence in distributed systems. This uptime guarantees only 5 minutes of downtime annually, ensuring near-constant availability and reliability. Even though it offers greater resilience and up-time, the question around this is: at what cost?

The pursuit of consistent uptime comes with significant financial, operational, and human costs. There are often overlooked aspects of chasing the five nines through analysis aiming to question if the benefits justify the investment by considering the law of diminishing returns.

**Financial Costs: Infrastructure and Beyond**
Although most mid-sized companies now leverage the cloud, it’s essential to consider the capital expenditure on redundancy for an on-prem infrastructure for high availability. Companies need to deploy multiple data centers across different geographical locations to ensure continuous availability.

These multiple data centers protect against localized failures, but there is a cost to maintain these data centers, which revolves around the following:

- Real estate and facilities: Leasing and purchasing land and buildings. According to a report by
, the potential cost of setting up a Tier III data center can range from $7,000 to $12,000 per square foot. For a 10,000-square-foot facility, this amount could go up to $120 million.[Uptime Institute](https://journal.uptimeinstitute.com/data-center-costs-set-to-rise-and-rise/) - Hardware: Servers, storage systems, and networking equipment must be duplicated across multiple sites for a high-availability infrastructure. A single server costs around $2,000 at least, and a company might require 100s of servers, resulting in an investment of around $2 million to $5 million.
- Networking: High-speed, redundant network connections between data centers to facilitate failover handling and load balancing. High-speed networking connections can cost between $100,000 and $1 million annually, depending on the bandwidth and assistance.
**Operational Costs**
The costs to manage complex and multiple layers of redundancy, sophisticated failover mechanisms, and a multitude of interconnected services can lead to operational challenges due to the following reasons:

- Increased Monitoring requirement: As infrastructure grows, so does the need to monitor anomalies in real time. Large enterprises spend around $50,000 to $200,000 annually on solutions like Datadog, New Relic, or Splunk. In some scenarios, there is also a need for custom monitoring solutions, which increase costs.
- Increased need for incident management: When monitoring grows, it’s crucial to handle incidents through robust incident management processes like runbooks, escalation protocols, and communication strategies. According to
[Ponemon Institute’s](https://www.ponemon.org/)“Cost of Data Breach Report”, the average cost of a data breach in 2023 was ~$4.45 million. Although not all incidents result in breaches, the costs associated with downtime, investigation, and remediation can be significant. Even minor incidents can disrupt services and require many resources, especially in systems designed for high availability. - Increased need for Quality assurance and Testing: A multilayer infrastructure requires rigorous testing, including:
- Disaster Recovery Drills: Regularly simulate a disaster recovery scenario to ensure active and functional recovery processes. Costs revolve around personnel time, resource allocation, and potential disruption to normal operations.
- Pen Testing: Conducting frequent scans and tests to ensure all the services are available and non-vulnerable.
- Performance Testing: Continuously monitoring the system’s capability under peak traffic loads and the ability to scale dynamically without compromising availability.
![](https://cdn.thenewstack.io/media/2024/08/52d5a1c8-picture1.png)
A hypothetical bar chart comparing costs of Disaster Recovery, Penetration Testing and Performance Testing for different availability levels for a medium-sized enterprise.

**Human Costs**
When you think of high availability, financial and operational considerations are always at the forefront; however, the human cost of maintaining these systems is also crucial. The impact on IT operations and teams is significant enough to affect their overall well-being and job satisfaction. Some of these factors are not limited to:

- Stress and Burnout: The pursuit of five nines results in employing a significant amount of personnel available around the clock to address any issues immediately. The expectation to respond instantly to incidents results in a high-pressure environment. The fear of severe repercussions further exacerbates this — reputational damage or job loss — if service availability is compromised. This also results in a severe impact on mental health.
- Human Factor in Error Rates: In a high-pressure environment, the likelihood of human-induced errors increases.
- Employee Turnover: A high-stress environment also results in higher turnover rates as developers avoid high-pressure environments and pursue better work-life balance.
**Law of Diminishing Returns**
Per this economic principle, as an investment in a particular area increases, the gains in output or performance will eventually decrease. Applying this to the pursuit of high availability in distributed systems suggests that beyond a certain point, the additional investments yield more minor improvements in uptime.

Moving from 99% to 99.9% often yields significant performance gains in customer satisfaction and reliability. These are also the most cost-effective since they can be achieved by implementing standard practices in infrastructure redundancy, incident management, and monitoring. However, as you move from 99.9% to 99.99% or 99.999%, the costs escalate dramatically due to all the factors we mentioned earlier, such as enhanced redundancy, monitoring, and comprehensive testing.

As investments grow, the returns measured in reduced downtime also decrease. For example:

- Moving from 99.9% to 99.99% availability results in a drop from 8.76 hours/year to 52.6 minutes/year. While this improvement might sound notable, the costs are justified only in specific industries like finance and healthcare.
- Moving from 99.99% to 99.9999% availability further reduces downtime to 5 minutes/year. This also comes at a significant cost; most organizations would struggle to justify the expense.
As you can tell, balancing the cost of critical vs. non-critical systems is extremely important. Businesses must differentiate between mission-critical and non-critical systems and strive for availability only when downtimes can impact their reputation or costs significantly.

**Conclusion**
Achieving five nines involves significant organizational, operational, financial, and human costs.

While it makes sense for specific organizations in specific sectors to pursue the five nines, most organizations must weigh the costs against the benefits.

In most cases, aiming for a lower availability target might be worthwhile to attain a better balance, offering sustainable operations and a healthier work culture. As systems evolve, it becomes equally essential to develop the need for availability, prioritizing resilience, flexibility, and well-being of the people behind these systems.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)