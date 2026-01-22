One of the more meaningful consequences of AI’s growth in the enterprise is its impact on the cloud race. The industry is shifting from the consolidation of services in the three main hyperscalers — [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) and [Microsoft Azure](https://aka.ms/modelmondays?utm_content=inline+mention) — to a new model in which specialization, not centralization, is the top priority.

[Neoclouds](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-evolution-of-neoclouds-and-their-next-moves), with their hyperspecialized workloads for statistical AI, are driving this growing movement. Cloud providers such as CoreWeave, Lambda and Crusoe deliver GPUs on demand while focusing on fundamental AI tasks like model training, fine-tuning and inferencing. By promising better performance at a lower cost, they’re attracting enterprise users.

One effect of this development is that organizations are beginning to employ multiple compute providers. According to [Tigris Data](https://www.tigrisdata.com/?utm_content=inline+mention) CEO [Ovais Tariq](https://www.linkedin.com/in/ovaistariq), this trend helps organizations avoid vendor lock-in and gain portability. Instead, they can “utilize any compute service, whether it’s because of cost performance or whether it’s due to data locality requirements.”

The other effect is an increased need for a flexible, distributed storage layer to support distributed computing across any cloud. Transitioning data between providers means users must be able to intelligently tier storage from remote to local resources with data placement in mind. They can do so by maintaining cost-effective, remote object storage as their source of truth.

Competitive vendors offer such elastic storage without egress fees, the notorious “cloud tax” charged when companies want to move data between providers. Using this flexible storage, organizations can position data close to their compute and hydrate it on demand for neoclouds. There, they get fast-access local storage to optimize AI workloads.

## The Role of Dynamic Storage for Distributed Data

The decentralized compute necessities for reaping the benefits of neoclouds are largely predicated on the underlying storage. Credible vendors utilize direct data placement methods in which data is kept in object storage in a distributed manner, said Tariq. They may have multiple data centers throughout the region, so they can replicate data closest to where the compute is.

For example, if a neocloud is located in Texas, the data will be replicated in the Southwest. If a neocloud is headquartered in Rhode Island, the storage vendor can replicate specified data to New England.

Because these providers can “move data to the same geographic location, there’s lower latency for copying the data, and you can copy the data with high throughput,” Tariq said. These advantages aren’t always possible with hyperscalers because their storage architecture is centralized — the data is always stored in one location.

## Benefits of Inexpensive Remote Object Storage

Contemporary [storage tiering](https://thenewstack.io/stop-freezing-your-data-to-death/) for distributed compute and cloud architectures is binary. There’s a remote layer that provides the source of truth and a local layer that “is close to the compute and in the same network, in the same LAN or in the same data center,” Tariq said. Since the remote layer is external to the neocloud, organizations can adapt their workloads to any neocloud and reap the benefits of elastic object storage.

The cloud’s elasticity allows for scaling storage capacity on demand; object storage is primed for the semistructured and unstructured data fueling advanced machine learning (ML) deployments. Object storage is also extremely cost-effective, which complements the lower overhead of serverless computing and lack of egress with competitive object store vendors.

## When To Use Fast Local Storage for AI Workloads

Because local storage is much faster than remote storage, the local layer is ideal for AI use cases. This storage is typically flash-based and involves SSDs or [NVMes](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/).

“Local storage is used for processing frequently accessed data,” Tariq explained. “Or, it’s used as a cache or to store a subset of the data.”

In terms of performance, any ML inference job benefits from the local layer. However, the same factors that result in quicker access also contribute to the greater costs of using local, nonelastic storage, Tariq said.

“You need to buy a fixed capacity, and you only have a limited amount of capacity. It’s not serverless.”

Consequently, local storage is undesirable for long-term use and is better for ephemeral AI workloads, which is why data primarily remains in object storage until a local cluster is spun up for neocloud AI.

## How Neocloud Storage Deployments Work in Practice

Users can select neoclouds based on the provider’s AI specialization, such as predictions, fine-tuning and having the GPU capacity for the job. Direct placement object store providers can dynamically replicate data to data centers close to where the compute processing will occur.

This practice reinforces fast access and lower costs for [hydrating data](https://thenewstack.io/mastering-progressive-hydration-for-enhanced-web-performance/) — hyperscalers with availability zones on the coasts can’t match the costs of hydrating data using a neocloud located in the middle of the country.

This also allows you to hydrate your local storage with data from the object store, Tariq said, using batch tools like [PyTorch](https://thenewstack.io/why-pytorch-won/). Once the workloads are complete, you simply spin down the cluster. This approach is aligned with contemporary stateless principles for cloud native architectures. Plus, the original data and the computation outputs are stored in the decentralized object store.

## How Tiered Storage Enables Cloud Choice and Portability

The bifurcation of remote and local storage does more than underpin the distributed compute foundation on which neocloud deployments are based. While there are also significant cost savings, the primary benefit of these storage tiering layers is the ability to avoid vendor lock-in while employing any cloud of choice, including neoclouds and hyperscalers.

This advantage is integral to the newfound freedom of the distributed compute, neocloud reality. Coupling fast local storage with cost-effective, long-term object storage also results in better performance for lower cost, which is critical for successful advanced ML applications.

Finally, the ability to choose clouds specialized for a given workload also reinforces data locality, as users can now position their data closest to the cloud of choice. Doing so reinforces the speed at which they’re able to hydrate their data, underpinning the performance and cost advantages of this modern architecture.

With a growing number of users availing themselves of this model, it also increases competition in the market to provide more specialized services for AI workloads that compete on both quality and cost.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/ee3e39b7-cropped-52925a32-jelani-harper-110x110-1.jpg)

Jelani Harper has worked as a research analyst, research lead, information technology editorial consultant, and journalist for over 10 years. During that time he has helped myriad vendors and publications in the data management space strategize, develop, compose, and place...

Read more from Jelani Harper](https://thenewstack.io/author/jelani-harper/)