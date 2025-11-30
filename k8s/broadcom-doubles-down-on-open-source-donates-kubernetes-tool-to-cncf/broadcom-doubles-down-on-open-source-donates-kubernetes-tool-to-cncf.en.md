ATLANTA — [Broadcom](https://thenewstack.io/why-broadcoms-ubuntu-bet-on-vmware-will-delight-devs-and-ops/) used [KubeCon + CloudNativeCon NA](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) to allay fears that it was pulling back on its support for open source, highlighting ongoing backing for [VMware](https://tanzu.vmware.com?utm_content=inline+mention)-developed projects and unveiling further contributions to the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention).

Broadcom’s [VMware Cloud Foundation (VCF)](https://www.vmware.com/products/cloud-infrastructure/vmware-cloud-foundation) engineers and developers have consistently continued to contribute to open source, and Broadcom remains one of the top five CNCF open source contributors and a major [Kubernetes](https://thenewstack.io/kubernetes/) contributor.

## Ramping Up

During KubeCon + CloudNativeCon NA here, Broadcom VMware representatives sought to reassure the community that it is ramping up open source support and contributions.

[Prashanth Shenoy](https://www.linkedin.com/in/prashanthshenoy/), vice president of product marketing, VCF division at Broadcom, said during a press and analyst briefing that Broadcom is “doubling down” on open source. He described new contributions it was making, including working more actively in key areas of open source related to Kubernetes.

These cloud native contributions include diagnostic tools, enhancements and operational features that help VCF support Kubernetes clusters across distributed environments. These efforts allow customers to leverage modern developer services, Infrastructure as a Service (IaaS) services and open source capabilities that are natively integrated into VCF.

One key contribution is the donation of the etcd-diagnosis tool to the CNCF. This tool enables automated analysis of cluster configuration, state and health consistency, helping operators quickly identify underlying issues within etcd — the system of record for Kubernetes. Broadcom has also developed etcd-recovery, an open source companion tool designed to simplify restoration when an etcd cluster loses quorum. Together, these tools reduce manual, error-prone processes and improve the reliability and stability of Kubernetes environments.

Another focus is the open source [Cluster API (CAPI)](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/), which addresses the complexity of managing multiple Kubernetes clusters throughout their entire life cycle. By using declarative, Kubernetes-style APIs, CAPI automates cluster provisioning, upgrades and day-to-day management, allowing organizations to operate fleets of clusters more consistently and with less overhead. This standardization frees teams to concentrate on delivering applications rather than managing infrastructure.

Additionally, Harbor (originally developed by VMware) continues to serve as the open source industry standard for securely storing container images and artifacts. As a trusted cloud native registry, it ensures that application images are managed with strong security, compliance and performance capabilities, making it a foundational component for organizations building and deploying modern cloud native applications.

[Nabarun Pal](https://www.linkedin.com/in/palnabarun/?originalSubdomain=in), principal engineer at Broadcom, and [Arka Saha](https://www.linkedin.com/in/arkasaha30/?originalSubdomain=in), software engineer at Broadcom, discussed common causes of etcd failures that affect Kubernetes stability and performance in their conference talk “Kubernetes and etcd: Common Pitfalls and How To Avoid Them.” They offered details about improving diagnosis for etcd in running clusters. During the talk, they covered best practices for operating etcd, covering upgrades, backups, recovery and key workarounds to ensure a resilient control plane.

While Broadcom is a top contributor to Kubernetes based on ReveCom, ESG and CNCF metrics, the stats do not tell all of the story, [Torsten Volk](https://www.linkedin.com/in/torstenvolk/), an analyst with TechTarget’s Enterprise Strategy Group who previously worked with ReveCom in a consulting capacity, told me.

“The pure number of contributions often is not as meaningful as the actual strategy behind them,” Volk said. “This strategy needs to strike a balance between contributing to the upstream community and adding integrations for the company’s own software portfolio.”

VMware’s historical commitment to open source, now reinforced under Broadcom, ensures customers can rely on VCF as a robust platform for running Kubernetes while aligning with open community standards such as the CNCF Certified Kubernetes AI Platform Conformance Program, said Shenoy during the press and analyst briefing.

“Broadcom is one of the first vendors certified under this initiative, guaranteeing that AI workloads on VKS adhere to community-defined standards for APIs, configurations and infrastructure capabilities,” Shenoy explained.

Market research shows that customers see open source projects as a critical element of their transformation strategy. Users significantly benefit from communities solving specific sets of problems and then continuously supporting these solutions because their own businesses depend on that very support, according to Volk. In other words, VCF’s credibility and Broadcom’s ability to hone VCF to meet the changes its customers require. This will depend on Broadcom’s ability to continue to closely collaborate with the open source community to develop and adapt VCF to changing needs, as it has traditionally done.

“Therefore, credible open source participation is key for Broadcom VMware’s success in the platform game,” Volk said. “At play are the company’s upstream contributions in addition to contributions that fully focus on integrating Kubernetes with its own platform.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)