# Databases on Kubernetes: Why, When and What To Consider
![Featued image for: Databases on Kubernetes: Why, When and What To Consider](https://cdn.thenewstack.io/media/2024/09/42b3f3bd-databases-on-kubernetes-considerations-1024x576.jpg)
Databases are an increasingly popular workload for Kubernetes; in a recent Portworx-commissioned [survey of organizations using Kubernetes](https://portworx.com/resources/voice-of-kubernetes-expert-report/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand), over 72% of respondents noted that their teams were running [databases on Kubernetes](https://portworx.com/database-as-a-service/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand).

Clearly, the discussion surrounding [data on Kubernetes](https://thenewstack.io/managing-data-on-kubernetes-dok-solving-the-underlying-challenges) (DoK) has matured since persistent volumes in Kubernetes entered general availability in 2019. Teams with more advanced Kubernetes practices are moving beyond the simpler debate of [stateless versus stateful](https://thenewstack.io/3-reasons-to-bring-stateful-applications-to-kubernetes/) applications and the need for persistent storage. Instead, they’re considering how a container data management layer — inclusive of databases — fits with the broader set of business goals, as well as the infrastructure, development and delivery solutions in their internal platforms.

## Why Organizations Run Databases in Kubernetes
For software, infrastructure and [platform engineering](https://thenewstack.io/platform-engineering/) leaders, deciding to run databases in containers and manage them with [Kubernetes](https://thenewstack.io/kubernetes/) often comes down to some mix of the following factors:

### Development Velocity
If data is the payload for differentiated value to the end user, then applications are the delivery vehicle. For example, a social news feed provides similar functionality to everyone, but it relies on underlying data to ensure relevance to the reader.

Kubernetes’ declarative nature allows database teams to define consistent deployment guidelines and standardize across development, staging and production environments. This removes database provisioning as a bottleneck, leading to delivering more value, faster, to the end user.

### Lower Costs, Less Complexity
Amid economic challenges, database teams are being asked to do more with less. They must manage more database instances, at greater scale, from more database providers and vendors, integrated with an increasingly complex set of infrastructure services.

Kubernetes offers a way to reduce complexity, as its standardized approach to database deployments across environments simplifies maintenance. While managed cloud databases offer shortcuts to deployment, in practice [they often introduce more complexity](https://portworx.com/blog/break-the-chains-of-cloud-databases-with-data-on-kubernetes/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) through managing auxiliary cloud services, with the added drawback of cloud lock-in that drives up costs and hampers data mobility.

### Reduced Risk, Greater Uptime, Resilience at Scale
Kubernetes is purpose-built to run elastic, scalable, highly resilient applications. Why not allow databases to benefit from running on Kubernetes, as well as the collective knowledge of a massive, global cloud native community building to these principles?

## When To Run Databases on Kubernetes
If your applications demand scalable, automated data management with minimal friction, and you need to maintain consistency across development, testing and production environments, running databases on Kubernetes is an excellent choice.

Kubernetes’ advantages include life cycle management, self-service capabilities and enhanced data portability, especially for modern, cloud native applications where schema and data sizes can change rapidly.

## What Are the Benefits of Data on Kubernetes?
Running databases on Kubernetes enables:

**Automated operations and life cycle management at scale**, especially given that[operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)are available for nearly every database solution on the market.**Consistency across dev, test and production environments**. It’s the original promise of[Docker](https://www.docker.com/?utm_content=inline+mention)containers, but for databases. Developers can deploy databases locally on[minikube](https://minikube.sigs.k8s.io/docs/)with greater confidence their applications will work elsewhere as configured.**Easier data portability**for near-line or local processing, resulting in faster performance, less data drift and a greater overall ability to withstand the churn and elasticity of cloud native applications.**Self-service capabilities****for end users**including developers, data scientists and machine learning operations (MLOps) engineers. Database teams can provide guidelines and policies, while end users can make informed decisions about schema, location and consumption. And if databases are properly integrated with a broader development platform, neither database administrators (DBAs) nor developers bear the burden of[managing Kubernetes](https://roadmap.sh/kubernetes)itself.
Other databases — like terabyte-scale relational database management system (RDBMS) deployments with decades of historical transactional data or massive unstructured data lakes — have inertia, and are unlikely candidates for containerization. They’re big, they’re hard to move and they serve a different purpose than modern databases supporting modern application development.

## What To Consider When Introducing Databases on Kubernetes
Let’s say your organization has decided against managed cloud databases or running databases on virtual machines (VMs), and believes that the benefits of faster development velocity, lower costs and risk reduction are worth the leap towards databases on Kubernetes. What else should you and your team consider as you make this change?

As a leader, you’ll likely focus on your team’s priorities, skills and time and invest in technical solutions accordingly. Database teams are generally experts in databases, not in Kubernetes. And while many developers are familiar with containers and Kubernetes, it’s unusual for their primary job to include managing Kubernetes deployments.

Consider whether DBAs or developers will handle provisioning and managing databases on Kubernetes, or if this requires a broader, automated as-a-service approach enabled by an internal developer or database platform. If it’s the latter, you’ll need to decide the level of Kubernetes abstraction your internal platform should offer to support other teams. Additionally, you’ll need to define how containerized databases will be configured with respect to persistent volumes, storage arrays, and backup or data protection policies.

## Embrace Data on Kubernetes
For organizations that have just started their Kubernetes journey, running data-intensive workloads on Kubernetes can seem daunting. (And if this is where your organization is today, you’re far from alone!) But it can be done; businesses like [Rivian](https://portworx.com/blog/breakthrough-award-winner-rivian-automotive-cloud-champion/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) are running databases on Kubernetes in production and provisioning them within hours instead of days, all while increasing uptime, resilience and controlling costs.

*To learn more about how to unlock the value of data on Kubernetes at scale, visit Portworx.com or set up a conversation.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)