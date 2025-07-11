[Google Cloud](https://thenewstack.io/need-a-trillion-parameter-llm-google-cloud-is-for-you/) now offers a fully managed version of the [Lustre parallel file system](https://wiki.lustre.org/images/6/64/LustreArchitecture-v4.pdf). The [Google Cloud Managed Lustre service](https://www.ddn.com/press-releases/google-cloud-launches-general-availability-of-managed-lustre-powered-by-ddns-exascaler-technology/) went live (“general availability”) globally on July 8.

An open source, high-performance file system, [Lustre](https://www.lustre.org/) has long been used in high-performance computing (or [supercomputing)](https://thenewstack.io/xs-colossus-supercomputer-changes-the-sc500-performance-game/) systems, for large-scale work such as weather modelling.

Google is presenting its Lustre offering as a lower-headache way of [running those supercomputing jobs](https://cloud.google.com/products/managed-lustre?hl=en#high-performance-computing-hpc). And Lustre’s ability to stream data in the range of terabytes per second should also make it appealing to [large-scale AI jobs as well](https://cloud.google.com/products/managed-lustre?hl=en#artificial-intelligence-ai-or-machine-learning-ml-workloads). Those hungry GPUs need feeding; you can’t get to artificial general intelligence without plenty of data.

This service offers a 1TB/s read throughput per namespace, with less than a millisecond of latency.

Deploys can start at 18TiB — a tebibyte is 2 to the 40th bytes (or [very approximately 1TB](https://simple.wikipedia.org/wiki/Tebibyte)) — and can scale up to 8PiB or more.

With this release, Google Cloud has caught up with other cloud providers in offering a cloud-based Lustre. It competes with [Azure Managed Lustre](https://azure.microsoft.com/en-us/pricing/details/managed-lustre/), [AWS](https://aws.amazon.com/?utm_content=inline+mention)‘s [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) and [Oracle](https://developer.oracle.com/?utm_content=inline+mention)‘s [OCI File Storage with Lustre](https://www.oracle.com/cloud/storage/file-storage-with-lustre/).

But this service comes with some special sauce: It heavily relies on [EXAScaler](https://www.ddn.com/products/lustre-file-system-exascaler/), a Lustre deployment optimized for throughput and scalability, courtesy of a partnership with [DDN](https://www.ddn.com/about-us/).

“By integrating DDN’s enterprise-grade data platforms and Google’s global cloud capabilities, organizations can readily access vast amounts of data and unlock the full potential of AI,” suggested [NVIDIA](https://thenewstack.io/nvidia-gtc-2025-wrap-up-18-new-products-to-watch/) Director of Accelerated Computing Products [Dave Salvator](https://www.linkedin.com/in/davesalvator/), in a statement.

In other words, Lustre could help keep those NVIDIA GPUs busy.

## The Lustre Way

Created by Carnegie Mellon researcher [Peter J. Braam](https://www.braam.io/) in 1999 specifically for HPC systems, Lustre addressed supercomputing’s need for extremely high throughput. At the time, traditional network file systems, such as [NFS](https://thenewstack.io/linux-create-and-connect-to-an-nfs-share/), had difficulty scaling to the levels required by HPC.

Lustre is a parallel file system: The files themselves are sharded across multiple servers for faster access, and each server can deliver its bits simultaneously.

Metadata for each file (file locations, permissions, directory hierarchies, etc.) is kept separately on a metadata server, which also controls the file system operations like creating and deleting files and eliminating I/O bottlenecks at the server level.

## How Much Does It Cost?

Google’s Lustre service is globally available as four different throughput tiers: 125 MB/s, 250 MB/s, 500 MB/s and 1000 MB/s for each TB of data. Each namespace can be as large as 1PB.

A Managed Lustre instance is billed in 1-second increments, based on the instance’s provisioned capacity. As an example, storing a gibibyte on the 125MB/s tier will run $0.145 a month.

There’s a [whole page](https://cloud.google.com/products/managed-lustre/pricing?hl=en) dedicated to pricing:

[![screenshot of prices](https://cdn.thenewstack.io/media/2025/07/51a50693-lustre-pricing-1024x270.jpg)](https://cdn.thenewstack.io/media/2025/07/51a50693-lustre-pricing-1024x270.jpg)

Sample managed Lustre pricing list (Google).

The managed Lustre is natively integrated with other Google Cloud services, such as Google Cloud Compute Engine, Google Kubernetes Engine (GKE), IAM, VPC Service Controls and Google Cloud’s Vertex AI platform.

## The Google HPC Stack

At Google Next 25, [Wyatt Gorman](https://www.linkedin.com/in/wyattgorman/), Google solutions manager for HPC and AI infrastructure, further discussed the managed Lustre offering.

Google set up the service to keep “the scratch space as close to the compute as possible,” he said.

The managed Lustre offering provides persistent scratch space, though at the conference, Gorman also spoke about [Parallelstore](https://cloud.google.com/parallelstore?hl=en), a complementary service built on the open source [DAOS project](https://daos.io/) that would provide super-speedy *non-persistent* scratch space.

![](https://cdn.thenewstack.io/media/2025/07/1768c07c-google-managed-lustre-1024x569.png)

The ideal Google HPC stack would also include [H4D CPU VM](https://cloud.google.com/blog/products/compute/new-h4d-vms-optimized-for-hpc)s (now in preview), which are built on AMD’s EPYC processors and RDMA-enabled, as well as the Terraform-based [Cluster Toolkit](https://cloud.google.com/cluster-toolkit/docs/overview) for repeatable deployments.

For more about Google’s HPC stack, check out the [entire Google Next HPC presentation](https://cloud.withgoogle.com/next/25/session-library?session=BRK2-019).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 25 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)