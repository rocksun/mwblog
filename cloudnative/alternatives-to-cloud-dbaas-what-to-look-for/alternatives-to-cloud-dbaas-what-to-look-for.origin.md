# Alternatives to Cloud DBaaS: What to Look For
![Featued image for: Alternatives to Cloud DBaaS: What to Look For](https://cdn.thenewstack.io/media/2024/10/84a24090-cloud-dbaas-alternatives-1024x576.jpg)
Building a flexible cloud strategy means making decisions that align with operational efficiency, cost management and scalability. Public cloud platforms offer immense convenience, but come with certain downsides. High long-term costs, vendor lock-in and lack of flexibility are concerns for many organizations. As businesses grow, the allure of quick-starting cloud database as a service (DBaaS) solutions can fade, prompting a need for more customizable and cost-efficient solutions.

## The Hidden Costs of Public Cloud DBaaS
Cloud-based DBaaS solutions provide a quick and relatively easy entry point, especially for startups and small businesses. Features like autoscaling, backups and failover options are often ready out of the box, enabling teams to focus on their core business rather than database management. However, as businesses scale, this convenience often comes at a [price](https://thenewstack.io/the-hidden-cost-of-dbaass-convenience/), both financially and operationally.

While initially affordable, public [cloud solutions](https://thenewstack.io/cloud-native/) can become costly as workloads and databases expand. The limited configurability of these platforms can hinder innovation. Internal survey data from the Percona community shows that nearly 74% of users report high costs as their biggest challenge, followed by vendor lock-in and limited database configuration options.

![Percona survey data: 73.77% of users report high costs as their biggest challenge, followed by vendor lock-in (44.66%) and limited database configuration options (42.62%).](https://cdn.thenewstack.io/media/2024/10/8d22a304-dbaas-challenges-percona.png)
The Percona survey was conducted from October to November 2023 and collected 131 responses from those taking care of databases (database admin, site reliability engineer, admin, platform team member, etc.), comprising 81% of the sample, and those using databases but not managing them (developer, data analyst, etc.), comprising 19% of the sample. The survey was focused on exploring the benefits and downsides of public DBaaS solutions (AWS RDS, Amazon Aurora, MongoDB Atlas and similar).

These factors become increasingly problematic as organizations attempt to scale their database environments without sacrificing flexibility.

## What to Look for in a Database Platform
As organizations look to address these challenges, many seek alternatives that provide greater flexibility without sacrificing the benefits of public cloud platforms. Here are key capabilities to consider when choosing or building such a platform:

### 1. Multi-Database Support
According to the Percona survey, many respondents are using more than one database in their stack:

- 36% said MySQL and PostgreSQL were both used.
- 17.6% said
[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)and PostgreSQL were both used.
Organizations increasingly seek platforms that allow seamless management of different databases, such as MySQL, PostgreSQL, MongoDB and [Valkey](https://thenewstack.io/valkey-is-a-different-kind-of-fork/), without signing contracts with different vendors for each technology. This flexibility helps businesses choose the right database for their workload without being locked into a single technology or vendor.

### 2. Cost Efficiency
A solution that balances operational features with cost-effectiveness is critical. Businesses should ensure their database management system can scale cost-effectively as they grow, avoiding hidden costs associated with cloud-based DBaaS offerings.

### 3. Scalability
The ability to elastically scale databases, both horizontally and vertically, is crucial, especially for startups and small and midsize businesses (SMBs). Companies need a solution that can adjust to traffic spikes and scale back down when demand decreases to achieve cost efficiency.

### 4. Kubernetes and Cloud Native Support
Kubernetes has become the standard for orchestrating containers in cloud and on-premises environments. A cloud-agnostic platform built on Kubernetes allows businesses to deploy their database workloads anywhere — on-premises, in the cloud or in hybrid setups. Whether features like disaster recovery, point-in-time recovery and automated backups are available are important considerations.

### 5. Flexibility and Freedom From Vendor Lock-In
Platforms should enable customization of databases based on specific requirements, ensuring operational efficiency without sacrificing control. Open source tools provide the flexibility to move workloads between different infrastructures, helping to avoid vendor lock-in.

## Open Source Enables Flexibility and Efficiency
Many companies are exploring [alternatives](https://thenewstack.io/building-an-open-source-private-dbaas/) to public cloud DBaaS solutions that combine the best of both worlds: the ease-of-use they are accustomed to and the flexibility of open source. One such alternative is Percona Everest, a Kubernetes-based open source platform designed for database provisioning and management that allows organizations to control database infrastructure-related costs while avoiding vendor lock-in.

As organizations continue to grow, balancing the trade-offs between convenience, flexibility and cost will remain critical. Open source platforms like Percona Everest offer a promising middle ground, allowing businesses to maintain control over their infrastructure, scale efficiently and avoid the long-term pitfalls of proprietary cloud solutions.

To future-proof your cloud strategy, explore open source tools like [Percona Everest](https://www.percona.com/software/percona-everest) that provide flexibility, scalability and cost savings and empower you to focus on what matters most: growing your business. And for a real-world example of combining open source technology with regional cloud providers to deliver cost-effective, scalable services, watch this presentation by Handoyo Sutanto, founder and CEO of cloud platform Lyrid.io, at Percona’s recent [Open Source Live](https://event.on24.com/wcc/r/4683903/2FDCEBE5093B0F3FB58313A06CF22C2A).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)