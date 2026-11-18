![](https://cdn.thenewstack.io/media/2026/11/f01f76df-azure-cobalt-200-image-01-updated-1024x576.png)

Microsoft is making its Cobalt 200 virtual machines generally available, with CPU improvements aimed at the sandboxes, tools, and code execution that keep AI agents running.

At its Ignite conference in San Francisco on Tuesday, the company announced that the VMs, powered by its second-generation Arm-based CPUs, are available in 14 Azure regions, expanding to 23 by the end of the year. Microsoft says they offer up to 50% better performance compared with Cobalt 100.

It’s been almost exactly a year since Microsoft first announced Cobalt 200 and about six months since the new VMs [went into preview](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/). Microsoft’s benchmarks show up to 1.5 times the performance for AI agent tool execution compared with Cobalt 100, for workloads like searching files, compiling code, and [executing tasks in sandboxes](https://thenewstack.io/cloud-agent-code-sandboxes/).

Pat Stemen, Microsoft’s vice president for Azure Cobalt, tells *The New Stack* that the team spent part of the past year tuning the infrastructure for these operations. The chip’s large caches, memory performance, and physical cores already suited workloads like starting sandboxes, he says. Microsoft then built “a set of benchmarks inside the company for those common operations” and tuned the product against them.

![](https://cdn.thenewstack.io/media/2026/11/4809ba9a-01-1024x576.jpg)

## Predictable performance or more speed

Cobalt 200 lets developers choose between two processor modes. Deterministic mode runs cores at a consistent 3.2 GHz, while opportunistic mode lets them reach 3.6 GHz when power and thermal headroom allow.

Microsoft says opportunistic mode can deliver up to 12% more performance, but clock speeds will vary.

“Customers love fixed frequency, by the way,” Stemen says. “They love the predictability that comes with that.”

Microsoft recommends deterministic mode for distributed data and analytics clusters, where the slowest node can set the pace, and services with tight performance targets. Web and API services, transaction processing, and media workloads may benefit more from the additional speed of opportunistic mode.

![](https://cdn.thenewstack.io/media/2026/11/caf98dfa-image-4.png)

Developers can select the mode for each VM when they create it or change it later through the Azure portal, command-line tools, or infrastructure templates.

“So if you buy four cores from us,” Stemen says, “you can choose all four of them to run flexibly or deterministically.”

He adds that the extra performance is typically available until the machine’s cores are heavily loaded.

## Designing around Azure workloads

Cobalt 200 uses 132 [Arm Neoverse V3 cores](https://thenewstack.io/arm-eyes-ai-with-its-latest-neoverse-cores-and-subsystems/), manufactured on TSMC’s 3nm process, while the VMs scale to 128 vCPUs. Each vCPU corresponds to a full physical core, with 3 MB of private L2 cache. The chip also includes 192 MB of system-level cache and 12 channels of DDR5 memory.

Stemen says the move from Cobalt 100 involved switching from a cost-optimized Arm core to a performance-optimized design, alongside larger caches and improved memory bandwidth.

Every Cobalt 200 VM also includes [Azure Boost](https://thenewstack.io/microsofts-rust-bet-from-blue-screens-to-safer-code/), which offloads networking and storage processing from the host. Microsoft reports up to 15% higher network bandwidth and 20% higher remote storage IOPS compared with Cobalt 100.

![](https://cdn.thenewstack.io/media/2026/11/937a6751-04-1024x576.png)

“They need remote storage. They need high-performance networking. They need local SSD,” Stemen says of the workloads customers bring to Azure.

Stemen says the team breaks Microsoft’s own workloads into smaller components, models their behavior before the hardware exists, and uses those results to make decisions about cache sizes, memory, and even the fans in a server rack. Product teams participate in the earliest planning reviews.

“They’re influencing the beginning of the product from when it’s just in PowerPoint,” Stemen says.

The Teams media-processing service, for example, reported 1.65 times the performance on Cobalt 200 compared with Cobalt 100. Microsoft says the service saw linear scaling across physical cores and could load vCPUs to 90% utilization while serving traffic.

Outside Microsoft, Amadeus reported more than 30% higher flight-search throughput in its benchmark lab compared with Cobalt 100.

## A wider range of Arm workloads

Indeed, quite a few Microsoft services like Azure Database for PostgreSQL, Azure DevOps, Azure SQL, Microsoft 365, Xbox, and others already run on Cobalt today.

A while ago, Stemen says, “customers had real concern about the lift.” Since then, “there’s more evidence of that working out, and the tools have improved, and the products have gotten better all at the same time.”

Alongside its general-purpose and memory-optimized VMs, Cobalt 200 brings two additional families to general availability: the high-memory Mpsv4 family, with 16 GiB of memory per vCPU, and the storage-optimized Lpsv5 family, with up to 23 TB of local NVMe storage.

“But now we’re seeing interest and desire for large in-memory databases, large existing enterprise workloads,” Stemen says, “and the ability to port them now being easier has helped.”

And while Microsoft will continue to invest in x86 chips, the company says it expects Cobalt 200 to make up “a significant portion of our new Azure Compute capacity in 2027 and moving forward.”

Developers can deploy the VMs through the existing Azure tools and use them in Virtual Machine Scale Sets or as Azure Kubernetes Service node pools.

The post [Microsoft’s ARM-based Cobalt 200 chips go GA. Why it matters for AI agents.](https://thenewstack.io/microsoft-cobalt-200-ga/) appeared first on [The New Stack](https://thenewstack.io).