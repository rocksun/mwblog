# Automation Can Solve Resource Overprovisioning in Kubernetes
![Featued image for: Automation Can Solve Resource Overprovisioning in Kubernetes](https://cdn.thenewstack.io/media/2025/03/41f1dbcb-light-1024x576.jpg)
Teams running Kubernetes applications in the cloud often fall into the [overprovisioning trap](https://thenewstack.io/neglect-kubernetes-resource-management-at-your-peril/) while trying to guarantee high performance and availability. As a result, they generate cloud waste that translates into a significant cost item for the organization.

Recently, Cast AI published the [2025 Kubernetes Cost Benchmark Report](https://cast.ai/kubernetes-cost-benchmark/), which showed that the gap between provisioned and requested resources is still considerable — 40% for CPUs and 57% for memory. This indicates teams are deploying fewer workloads onto clusters than their capacity.

Notably, 99.94% of clusters analyzed were overprovisioned with CPU, a problem consistent across major cloud providers (AWS, Google Cloud Platform and Microsoft Azure), with no significant variations in resource efficiency.

These inefficiencies suggest that the challenge lies not with the cloud platforms themselves but with the complexities of managing Kubernetes clusters manually.

## Overprovisioning Is Just One Side of the Coin
The average levels of Kubernetes resource utilization show that the problem doesn’t only relate to the size or type of compute instances selected. CPU utilization across Kubernetes clusters averaged 10%, with memory utilization at 22%. This shows teams face another challenge: setting the right requests for Kubernetes workloads without too much headroom.

Despite the widespread adoption of Kubernetes in cloud native environments, managing cloud resources remains manual and effort-intensive. When teams spend time on repetitive tasks and micromanage the cloud infrastructure, they tend to overprovision their clusters, fail to efficiently assign applications to them and generate cloud waste by leaving large headrooms in workload requests.

The data underscores the need for better tooling and automation in Kubernetes environments to reduce overprovisioning, improve [resource utilization and eliminate unnecessary cloud costs](https://thenewstack.io/engineers-guide-to-cloud-cost-optimization-engineering-resources-in-the-cloud/).

## Six Ways to Boost Resource Utilization and Efficiency
### Flexible Compute Generation Selection
An automation engine lets teams dynamically select from different generations of compute instances based on real-time price trends. This will enable them to capitalize on the latest hardware for performance or select older, cost-effective generations to balance their budgets.

The graph below illustrates the price evolution of three compute instances representing three generations, showing that the flexibility in instance choice can be a game changer.

### Automating Processor Architecture Selection (x86 vs. Arm)
The choice between x86 and Arm processors can lead to significant cost savings as Arm CPUs are generally more affordable than x86. Arm spot instances on platforms like Azure, GCP and AWS consistently offer better pricing, with up to 65% savings. By automating workload placement across architectures, teams can ensure the best performance-to-cost ratio without manual intervention.

Cloud provider |
Azure |
GCP |
AWS |
Avg. x86 spot price per CPUper hour |
$0.0254 | $0.0212 | $0.0389 |
Avg. x86 on-demand price per CPU per hour |
$0.1354 | $0.0659 | $0.0783 |
Avg. Arm spot price per CPU per hour |
$0.0079 | $0.0156 | $0.0200 |
Avg. Arm on-demand price per CPU per hour |
$0.0474 | $0.0410 | $0.0496 |
### Custom Autoscalers for Dynamic Resource Scaling
Companies like Akamai have usedcustom autoscalers to adjust cloud resources based on real-time demand automatically. This approach ensures applications always have the necessary resources while minimizing waste during low-usage periods. Automated scaling optimizes both costs and performance, eliminating the need for manual adjustments.

### Bin-Packing Workloads for Maximum Efficiency
Organizations can significantly reduce overprovisioning by bin-packing workloads, particularly spot-friendly, stateless workloads. Heureka Group, for example, achieved a 30% reduction in compute [costs by automatically optimizing](https://thenewstack.io/engineers-guide-to-cloud-cost-optimization-prioritize-cloud-rate-optimization/) workload placement and removing unused nodes. This technique reduces the number of idle CPUs and boosts overall utilization.

### Autonomous Request Setting Based on Real-Time Data
Stateful workloads are memory-intensive. The example below illustrates what may happen if a company uses autoscaling solutions at the workload level and, at some point, turns it off.

The resulting sharp rise in memory requests forced the system to provision more resources. This, in turn, drove CPU provisioning up due to the correlation between memory and CPU, causing substantial overspending on resources.

### Leveraging Spot Instances Safely
Spot instances offer substantial discounts but are often underused due to the risk of interruptions. Automation can help monitor price fluctuations and interruption rates, allowing teams to adopt [spot instances for non-critical workloads](https://thenewstack.io/saving-with-confidence-the-strategic-advantage-of-spot-instances/) confidently. By automating this process, companies can maximize savings without risking performance.

## Conclusion
Automation is a powerful solution for addressing the inefficiencies that plague Kubernetes environments. Organizations can significantly reduce cloud waste and improve resource utilization by using automated tools and best practices like flexible compute generation selection, dynamic autoscaling and intelligent workload placement.

As cloud environments grow more complex, this approach will become essential to ensuring that resources are efficiently used, workloads are optimized and teams continue to innovate without overspending on cloud infrastructure.

*To learn more about Kubernetes and the cloud native ecosystem, join us at *[KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)* in London on April 1-4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)