# Cloud Native Computing Now Has Its Own File System: CubeFS
![Featued image for: Cloud Native Computing Now Has Its Own File System: CubeFS](https://cdn.thenewstack.io/media/2025/01/44ceb1c1-cubefs-1024x683.jpg)
What’s a Kubernetes-based distributed system without a proper file system, one that cleanly separates the computer from the storage layer?

Now the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) has a highly-scalable open source cloud native distributed file and object storage system for its Kubernetes stack, [CubeFS](https://cubefs.io/) (“储宝” in Chinese).

Chinese e-commerce and services giant [JD.com](https://corporate.jd.com/ourBusiness) launched CubeFS in 2017, originally as [ChubaoFS](https://thenewstack.io/chubaofs-the-cloud-native-computing-foundations-speedy-new-distributed-file-system/), to [support stateful applications](https://cubefs.io/blog/bestPractices/elasticsearch.html) that require separation in compute and storage. It has since found a home in over 200 production environments, many of which are large Chinese e-commerce operations.

Chinese consumer giant [OPPO](https://www.oppo.com/en/about/) uses CubeFS for AI, big data and storage-computing separation. “CubeFS offers rich capabilities for various scenarios and interfaces, demonstrating good stability and continuous iteration, resulting in an excellent user experience,” wrote CubeFS engineer Jade Wang (王红岩), in a statement.

Chinese gaming company NetEase also relies on the technology. “The project’s stability and clear scope and roadmap have built trust with NetEase, making it a reliable component for its cloud native infrastructure needs,” wrote [NetEase’](https://www.neteasegames.com/business.html)s ZCola (张锐), in a statement.

Overall, the file system [collectively stores](https://github.com/kevin-wangzefeng/toc/blob/cubefs-graduation/proposals/graduation/cubefs-graduation-dd.md#adoption) more than 350PBs of data across a wide array of commerce applications, cloud storage and online media streaming.

## Graduation Day for CubeFS
On Tuesday, CubeFS graduated from the CNCF evaluation process, in which an open source technology must demonstrate its stability, maturity and adoption in multiple cloud native environments.

Entering the CNCF program in 2019, CubeFS swiftly moved through the sandbox and incubation stages. To graduate, the project completed a security audit, including the creation of a threat model for risk and entry points. Reviews were also completed for possible vulnerabilities in the code, and the supply chain was inspected as well.

CNCF has helped the project immensely. Since joining, CubeFS has garnered many new contributors, from 27 individuals across five companies to 379 contributors across 42 companies.

## A File System for the Cloud Native Era
CubeFS is a multi-purpose tool for unstructured data storage, with particular emphasis on big data, AI/LLMs, container platforms and other architectures that separate the [compute layer from the storage layer](https://thenewstack.io/setting-microservices-up-for-success-real-world-advice/).

It can be accessed through multiple protocols, such as Amazon Web Servces’ [S3 object storage interface](https://thenewstack.io/why-you-might-bring-your-own-s3-bucket-byob-to-the-observability-party/), the [HDFS](https://thenewstack.io/optimizing-compute-in-the-post-hadoop-era/) favored by big data, and the[ POSIX semantics](https://thenewstack.io/google-cloud-offers-posix-compliant-file-storage-red-hat-gluster/) spoken by all servers today. It offers strong consistency, full isolation and multi-tenancy support, as well as, in the words of CNCF, a highly scalable metadata service.

Going forward, the project plans to add support for tiered storage and distributed cache acceleration. For issue tracking, the project plans to implement call chain tracing.


[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)