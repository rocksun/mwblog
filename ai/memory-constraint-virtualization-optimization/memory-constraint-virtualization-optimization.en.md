Memory has replaced compute as a primary constraint for modern tech teams. A perfect storm of hardware architecture limitations, semiconductor supply chain uncertainty, and changing software licensing models has left enterprises confronting increasingly memory-constrained environments. All while high-bandwidth AI workloads overload the production chain’s ability to provide sufficient memory — and when your [AI token bill is starting to cost more than your salary](https://www.thestateofbrand.com/news/ai-now-costs-more-than-employees) bill.

Over the past year, the cost of high-bandwidth memory (HBM) and dynamic random access memory (DRAM) [has increased](https://bisi.org.uk/reports/global-ram-shortage-and-price-hikes-causes-consequences-and-market-outlook) [by an unprecedented 170%](https://bisi.org.uk/reports/global-ram-shortage-and-price-hikes-causes-consequences-and-market-outlook), with some [virtualization subscriptions more than doubling in price](https://www.cloudtango.net/blog/2025/11/03/vmware-price-increase-what-you-need-to-know/).

All this adds up to a demand for enterprises to shift from the previous buy-all-you-can mindset to a data-driven optimization strategy.

Fortunately, AI isn’t only part of the problem. When AI is applied to memory economics in modern virtualization, it becomes a vital part of the solution.

[Bharath Ram](https://www.linkedin.com/in/connect2bharath/), director of product management at [Hewlett-Packard Enterprise (HPE)](https://www.hpe.com/us/), explains it to *The New Stack* this way: “There’s a component shortage. Today the prices have increased. So customers are looking at ways to save and optimize the existing footprint, so that they can run their workloads on whatever and not have to procure anything new.”

By switching focus from gobbling up every bit of memory your organization can grab to optimizing your workloads and their placement across multi-cloud and hybrid-cloud environments, enterprises cannot only speed up modernization but also shorten decision-making cycle time by up to 80%, all while [cutting costs by up to 50%](https://www.hpe.com/us/en/storage/cloudphysics.html). Read on for how to transition your enterprise from guesswork to smarter IT.

## **Tech has to confront its waste problem**

Most enterprises operate with significant over-provisioning driven by limited visibility and risk avoidance.

These same companies are standing up legacy applications that become less efficient over time, including a significant number of zombie services running without any use.

On top of this, most AI workloads rely on advanced memory technologies, which has led chip manufacturers to shift production priorities from DDR4 to DDR5 RAM, further reducing DDR4 supply. This impacts the whole industry, with even a personal computer costing 15% to 30% more than last year.

Add to this volatile DRAM pricing and higher core densities, and it’s clear that even non-technical leadership is worried about memory efficiency. Tech giants Microsoft, Google, Amazon, and Meta are buying up as many AI chips as they can, which is triggering even more shortages and price pressure across the supply chain. And thus more enterprises are hoarding more infrastructure and memory.

And this overbuying isn’t limited to memory. Companies are now also buying infrastructure like servers even before they need them, too, Ram reflects, “because the cost is so exorbitant, the quote that you might have today might not be the same price that you’re quoted for the same infrastructure tomorrow. That’s how we’re seeing the market right now. It’s very volatile.”

But it might all be ok. HPE estimates that between 20% and 40% of infrastructure is overprovisioned today. Which is an opportunity for efficiency — not only in these limited resources but also in faster, more secure workloads.

Enterprises are more capable than ever to optimize the use of what they’ve got today, especially before they go searching for more RAM that will cost significantly more.

## **It all starts with understanding**

So much of this waste persists because enterprise infrastructure is obscured — no one really knows what does what with which data, or which services rely on it.

The same thing that holds companies back from doing anything more than lift-and-shift to the cloud is usually what keeps them from unlocking memory efficiency. There’s simply too little visibility across most enterprises’ complex, hybrid and multi-cloud distributed systems. Which has left organizations guessing and then rounding way up for over a decade now.

“It’s a combination of over-provisioning and not understanding underlying infrastructure. Because many of them are doing public cloud-based provisioning and self-service, where you don’t know what the underlying infrastructure is and you have admins leveraging whatever there is in terms of their service capabilities,” Ram explains. “One piece is memory shortage, and the other is understanding what’s been deployed and rightsizing it.”

To break these over-provisioning bad habits, any change has to be grounded in reality. The first step is to gather and analyze real usage data, using a tool like [HPE CloudPhysics](https://www.hpe.com/us/en/storage/cloudphysics.html) to establish a factual baseline that separates real cost drivers from those years of assumptions.

This allows enterprises to:

* Understand their virtualization footprint and licensing exposure.
* See their workload initialization and efficiency.
* Identify true cost drivers before taking action.

You cannot right-size until you have real-time monitoring of how many hosts have how many VMs, and which are on and off.

## **Predictive, not reactive provisioning**

Once an enterprise has a single source of truth for its complex distributed systems, it can explore what to deploy, where, when, and how.

“An application like SAP HANA is highly memory-intensive and highly latency-intensive. It’s not like this algorithm is optimized to pivot between hot and cold memory tiering” for cost reduction, Ram explains, without risking the application performance, akin to how, when older PCs had limited amounts of memory and, once that ran out, the computer would swap the program from running in memory to disk, slowing way down.

Part of the modern solution, Ram argues, is that companies “can over-provision with what they already have. They don’t have to buy any new memory,” because of better shared resources available to all the virtual machines managed by a single host.

“For example, a host with 64GB of physical memory may have more memory allocated across VMs than physically available,” he explains. “In practice, not all VMs consume their full allocation simultaneously, allowing unused capacity to be dynamically reassigned where needed.”

Memory ballooning, which, Ram says, is nothing new, but something desperately needed in the market right now. Version 9.0 of Morpheus, due out this summer, will feature a more modern sort of memory oversubscription, which, HPE explains, allows administrators to oversubscribe physical memory across VMs on a host, enabling higher VM density and more efficient use. This is particularly useful for testing and development environments, virtual desktop infrastructure, and workloads with variable memory demands.

## **Shift to architectural efficiency**

Eventually, once you’ve optimized and rightsized every memory allocation, it’s time to shift your workloads to a new platform to improve hardware efficiency.

“The final step is increasing workload density per server, especially as per-core software licensing becomes more expensive,” Ram explains. He says this is best achieved using a virtualization solution with an open-source hypervisor, which can improve utilization now and help organizations shift toward per-socket licensing models. For suitable applications, that modernization may also include moving to containerized deployment, while in-memory deduplication reduces redundant data structures in RAM, improving memory efficiency.

“Not everybody can keep running on existing hardware forever. At some point, some organizations will need to move to a new platform to improve hardware efficiency. But higher workload density still brings added benefits,” he continues, especially at a time when even the biggest tech companies are overbuying infrastructure, driving up costs and tightening capacity.

## Per-socket licensing saves more

And if you do go for a hardware refresh with HPE’s Morpheus Software, then you can unlock a different kind of subscription model, which charges per socket or CPU licensing, where multiple cores can share one socket. Some early results indicate that this can deliver up to 90% in savings.

*In the end, it all starts with that baseline. Take the [free cloud visibility assessment](https://www.hpe.com/uk/en/storage/cloudphysics.html) to see where your organization stands.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)