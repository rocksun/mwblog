TOKYO — So, you say you want long, long — one more time, with feeling — *long*-term support for [Kubernetes](https://kubernetes.io/)? Boy, does [Canonical](https://canonical.com/) have a deal for you.

At [Open Source Summit Japan](https://events.linuxfoundation.org/open-source-summit-japan/), [Youssef Eltoukhy](https://uk.linkedin.com/in/youssef-eltoukhy-47828210b), the company’s senior silicon alliances manager, revealed that Canonical is now offering up to 15 years of Long Term Support (LTS) for Kubernetes. This news comes after the U.K.-based Linux and open source company announced in February that it had already extended its [support for its Kubernetes distros for up to a dozen years.](https://thenewstack.io/canonical-extends-kubernetes-distro-support-to-a-dozen-years/)

Specifically, Canonical is pushing Kubernetes maintenance into mainframe territory by extending long-term support on its distributions to as much as 15 years for customers. It’s doing this by pairing Canonical Kubernetes LTS with its [Ubuntu Pro](https://ubuntu.com/pro) and new [Legacy add-on](https://canonical.com/blog/canonical-expands-total-coverage-for-ubuntu-lts-releases-to-15-years-with-legacy-add-on). Legacy had an extended paid source for up to 15 years for the company’s LTS Ubuntu Linux distros.

For Kubernetes, this means starting with [Kubernetes 1.32](https://thenewstack.io/kubernetes-1-32-aces-api-conformance-testing/), extended support will be offered until 2040 for [MicroK8s](https://canonical.com/microk8s), [Charmed Kubernetes](https://ubuntu.com/kubernetes/charmed-k8s) and [Canonical Kubernetes](https://ubuntu.com/kubernetes). This support package will be made available across all of Canonical’s supported platforms: Bare metal, public clouds, MicroCloud, [OpenStack](https://www.openstack.org/?utm_content=inline+mention) and [VMware by Broadcom](https://www.vmware.com/?utm_content=inline+mention).

Eltoukhy told the OSS Japan attendees that the company is essentially transplanting the Ubuntu LTS model onto Kubernetes, describing it as bringing the firm’s “10‑plus years of security patching on a date” concept to the container orchestration layer.

Kubernetes LTS releases will appear on a two‑year rhythm, he said, aligned with Ubuntu LTS, while interim Canonical Kubernetes builds will track upstream’s roughly four‑month cadence and receive short‑term maintenance.​​

## A Response to Real-World Demands

Why such long-term support? After all, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) only offers [three years of Extended Update Support (EUS) for OpenShift 4.14](https://www.redhat.com/en/blog/announcing-additional-extended-update-support-openshift-414-and-beyond) and subsequent even-numbered Red Hat OpenShift 4.x series releases.

Most cloud vendors also provide support beyond what the Kubernetes project offers. For instance, [Microsoft Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service) offers two years of support, while [Amazon](https://aws.amazon.com/?utm_content=inline+mention) [Elastic Kubernetes Service (EKS)](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/) provides 26 months of extended support.

Canonical is offering this service, Eltoukhy said, as a response to a tension between fast‑moving Software as a Service (SaaS) and AI developers and highly regulated sectors such as banking, medical imaging and telecoms.

On one side, he said, are hyperscale and SaaS teams that want Kubernetes to act as an abstraction layer they can refresh every few months; on the other sit telco operators who insist they want a stack that stays unchanged for 10 to 15 years while still receiving security fixes.​

He pointed to real‑world upgrade cycles to argue that upstream’s roughly 14‑month support window is out of step with enterprise practice. “One Nordic bank, when we said ‘Oh, by the way, you need to update Kubernetes every three to four months,’ their response was, ‘Get real!'” Eltoukhy said, “‘To update Kubernetes,  I need to get a buffer of six months ahead. I can only do that every two years.'”

The extended Canonical Kubernetes LTS, combined with long‑lived Ubuntu Pro and Legacy coverage, is pitched as a way to keep those clusters patched and compliant without forcing constant disruptive re‑platforming.​​

This will work, Eltoukhy said, because Canonical’s life cycle design follows each upstream Kubernetes release with a Canonical Kubernetes version and designates every sixth upstream release as an LTS.

For those LTS builds, customers can receive at least 12 years of Kubernetes security maintenance under Ubuntu Pro, and then extend that with the Legacy add‑on to reach up to 15 years of combined platform support for specific long‑lived deployments.​​

## Stability vs. Flexibility

In the Open Source Summit session, Eltoukhy described how enterprises that want to move forward can upgrade through interim versions or jump between LTS releases. He highlighted a newly introduced one‑year grace period after each new LTS ship, during which the previous LTS continues to receive full support, giving customers time to decide.

He also stressed that Canonical is not reinventing Kubernetes itself, but packaging upstream, [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)‑conformant Kubernetes with its own tools such as snaps, charms and Cluster API. These will be offered either as a self‑managed platform or as a fully managed service operated by Canonical engineers for customers such as the [European Space Agency (ESA)](https://www.esa.int/).

On Kubernetes specifically, Canonical is pairing the LTS offering with its newly released  [FIPS‑enabled Kubernetes](https://canonical.com/blog/canonical-releases-fips-enabled-kubernetes) variant designed for federal and other high‑compliance workloads. These entities require FIPS-validated cryptographic modules and hardening guidance, such as the [Defense Information Systems Agency’s Security Technical Implementation Guides (DISA‑STIG)](https://public.cyber.mil/stigs/), rather than a separate paid feature.

Eltoukhy also highlighted collaborations where Canonical quietly supplies and maintains open source components under the hood for partners such as Nvidia, telcos, and VMware, positioning the company as a component supply chain that keeps kernels, user space, Kubernetes, and GPU operators aligned and supported over long time horizons.​​

During the Q&A, Eltoukhy acknowledged that a 15‑year untouched stack would make any eventual migration a substantial undertaking. Still, he argued that for devices and platforms with similar lifespans, such as telco network infrastructure, stability is the priority. In many cases,  he added, the hardware itself will enter end of life before the software support window closes.​​

He also noted that the “legacy” window recently expanded from two to five years at the request of partners. He then hinted that the total support lifetime could grow further for strategic customers, suggesting that 15 years may not be the final ceiling.

For now, Canonical is betting that a Kubernetes distribution that can remain patched and supported well into the late 2030s will appeal to operators who are tired of what one audience member described as the pain of upgrading Kubernetes “every three months” and are looking instead for a container platform with the longevity of traditional infrastructure.​​

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)