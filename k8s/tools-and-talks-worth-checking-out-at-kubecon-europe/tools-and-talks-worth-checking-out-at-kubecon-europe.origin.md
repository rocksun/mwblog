# Tools and Talks Worth Checking Out at KubeCon Europe
![Featued image for: Tools and Talks Worth Checking Out at KubeCon Europe](https://cdn.thenewstack.io/media/2025/03/10287a30-conference12-1024x606.jpeg)
Are you heading to KubeCon + CloudNativeCon Europe 2025? With the event fast approaching, now’s the perfect time to plan your experience. This massive gathering held over four days is packed with cutting-edge [cloud native technologies](https://thenewstack.io/cloud-native/) and expert-led technical talks, so making a clear agenda is essential.

The challenge? Navigating the 229 sessions, 215 vendors and countless networking opportunities without feeling overwhelmed. Let me help you curate the perfect itinerary so you can maximize your KubeCon experience.

Here are five projects that are making significant waves in the cloud native ecosystem, along with the must-attend talks that should be on every attendee’s radar.

## Projects That Are Worth Checking Out
### Chainguard
If you are already spending countless hours trying to patch and triage the CVEs from container images to secure your systems, you need to check out this tool.

In an era where software supply-chain attacks are on the rise, [Chainguard](https://thenewstack.io/chainguard-launches-cpu-gpu-containers-for-ai-frameworks/) is redefining security with its focus on minimal, hardened and continuously verified container images. By eliminating vulnerabilities before they reach production, Chainguard helps organizations enhance their security posture without compromising efficiency.

Chainguard enhances security through several key approaches:

**Distroless container images —**These minimal images contain only what’s necessary to run an application, eliminating unnecessary packages, shells and utilities that could introduce vulnerabilities.**Continuous verification —**Automated scanning and attestation systems cryptographically verify the integrity and provenance of container images throughout the development life cycle.**Software bills of materials (SBOM) integration —**Chainguard generates and maintains detailed SBOMs for its images, providing transparency about all components and dependencies.**Vulnerability elimination —**Rather than just detecting vulnerabilities, its focuses on removing them at the source by carefully curating dependencies and maintaining strict update policies.
Chainguard offers[ publicly available container images](https://images.chainguard.dev/directory/?category=all) that you can explore and use, providing a hands-on experience with their secure, minimal and continuously verified approach.

### Crossplane
[Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/) transforms the way organizations manage their cloud infrastructure by bringing the declarative resource model of Kubernetes to multicloud environments. This powerful tool is reshaping infrastructure management through:
**Infrastructure as Code via Kubernetes API —**Crossplane allows teams to provision and manage cloud resources using the same Kubernetes API and tooling they already use for applications, eliminating the need to juggle multiple cloud provider CLIs and consoles.**Composable infrastructure abstractions —**It enables platform teams to create custom, organization-specific abstractions that hide cloud-specific implementation details, allowing developers to self-service infrastructure without needing to understand the underlying cloud providers.**Multicloud resource orchestration —**Crossplane provides a unified control plane for managing resources across AWS, Azure, GCP and other cloud providers through consistent Kubernetes custom resource definitions (CRDs).
### Kubescape
[Kubescape](https://thenewstack.io/kubescape-achieves-cncf-incubation-status/) is revolutionizing Kubernetes security with its comprehensive, open source security platform built by Armo and designed to identify and remediate risks across your entire Kubernetes stack. In an environment where container security breaches are increasingly common, Kubescape stands out with:
**Comprehensive security scanning —**It performs scans against multiple frameworks including NSA-CISA, MITRE ATT&CK and CIS Benchmarks, providing holistic visibility into security posture from cluster configuration to runtime behavior.**Risk-based prioritization**— Kubescape analyzes vulnerabilities within your specific context, calculating risk scores that help teams focus on what matters most instead of drowning in alerts.**DevSecOps integration —**It seamlessly integrates into CI/CD pipelines and existing workflows with support for CLI, WebUI and Kubernetes native components, enabling security to shift left in the development process.**Compliance automation**— Automatically generates compliance reports and provides remediation guidance, significantly reducing the manual effort needed to maintain regulatory compliance.
### vCluster
[vCluster](https://thenewstack.io/vcluster-to-the-rescue/) is transforming multitenancy in Kubernetes by introducing a revolutionary approach to cluster isolation and resource optimization. In environments where traditional namespace isolation falls short, vCluster enables:
**Virtual Kubernetes clusters —**vCluster creates fully functional Kubernetes clusters that run inside the namespace of another Kubernetes cluster, providing true isolation without the operational overhead of managing separate physical clusters.**Resource optimization —**By running virtual clusters on shared infrastructure, vCluster dramatically reduces resource consumption compared to dedicated clusters, cutting cloud costs while maintaining isolation.**Environment standardization —**Development, staging and production environments can maintain consistent configurations while running as virtual clusters, eliminating the “works on my machine” problem.**Team independence —**Development teams gain full admin rights to their own virtual clusters without affecting other teams or requiring privileged access to the underlying host cluster.
vCluster solves the critical challenge of providing strong isolation in multitenant environments without the prohibitive costs and operational complexity of managing multiple physical clusters, making it ideal for organizations looking to optimize their Kubernetes infrastructure while maintaining security and autonomy for development teams.

### Devtron
“When AI makes your developers two times faster, your Kubernetes shouldn’t hold them back.”

[Devtron](https://github.com/devtron-labs/devtron) is an open source application life-cycle management platform that enables teams to move faster without engaging with the complexities of Kubernetes. [Devtron](https://devtron.ai/) orchestrates Kubernetes and related operations into a single intuitive UI from where developers and DevOps teams can accelerate their Kubernetes operations.
Devtron makes managing Kubernetes easier and has revolutionized the way they are managed with features like:

**Automated and reliable CI/CD —**Devtron comes with integrated GitOps-enabled CI/CD workflows that ensure precise feature deployment in target environments. Key components like[deployment windows](https://devtron.ai/blog/execute-controlled-deployments-in-kubernetes-environments/), predeployment approvals and application promotion enhance reliability while reducing tool sprawl. This provides developers with a streamlined path to deployment.**Simplified and fine-grained RBAC —**Devtron addresses Kubernetes role-based access control (RBAC) configuration challenges through its the intuitive UI. The platform offers simplified, yet powerful[RBAC controls](https://devtron.ai/blog/sso-and-rbac-a-secure-access-strategy-for-your-kubernetes/), enabling fine-grained user access down to specific pods within specific clusters.**Multicluster management —**Easily onboard multiple Kubernetes clusters to a single Devtron instance and manage them through a unified dashboard. This eliminates the complexity of managing clusters via kubectl commands and provides clear[visibility into cluster operations](https://devtron.ai/blog/managing-kubernetes-resources-across-multiple-clusters/).**Policies and governance —**The platform includes robust governance features such as approval policies, configuration locks, built infrastructure controls and comprehensive compliance and audit logging capabilities.
With this, Devtron ensures that your infrastructure-based operations keep pace with the speed and efficiency of AI-accelerated development.

## Top Tracks and Talks Worth Attending
## AI and Machine Learning
“[ A Practical Guide to Benchmarking AI and GPU Workloads in Kubernetes”](https://kccnceu2025.sched.com/event/1tx7Q/a-practical-guide-to-benchmarking-ai-and-gpu-workloads-in-kubernetes-yuan-chen-nvidia-chen-wang-ibm-research?iframe=no&w=100%&sidebar=yes&bg=no) — Yuan Chen, NVIDIA, and Chen Wang, IBM Research

The talk covers benchmarks for a range of use cases, including model serving, model training and GPU stress testing, using tools like NVIDIA Triton Inference Server; fmperf, an open source tool for benchmarking LLM-serving performance; MLPerf, an open benchmark suite to compare the performance of machine learning systems; GPUStressTest; gpu-burn; and cuda benchmark. The talk will also introduce GPU monitoring and load-generation tools.

“[ Orchestrating AI Models in Kubernetes: Deploying Ollama as a Native Container Runtime”](https://kccnceu2025.sched.com/event/1tx97/orchestrating-ai-models-in-kubernetes-deploying-ollama-as-a-native-container-runtime-samuel-veloso-cast-ai-lucas-fernandez-red-hat?iframe=no&w=100%&sidebar=yes&bg=no) — Samuel Veloso, Cast AI, and Lucas Fernández, Red Hat

In this talk, you’ll discover how a custom container runtime integrated with Ollama streamlines AI model deployment in Kubernetes. It will explore how this approach simplifies operations, enhances efficiency and removes the complexity of traditional model-serving solutions. Through real-world examples and a live demonstration, you’ll gain insight into using this innovative runtime to natively run open source AI models in Kubernetes with ease.

## Security
“[ Open Source Malware or a Vulnerability? The Philosophical Debate and How to Mitigate](https://kccnceu2025.sched.com/#)” — Brian Fox, Sonatype; Madelein van der Hout, Forrester Research Inc.; Santiago Torres-Arias, Purdue University

This talk will shed light on the growing threat of open source malware, distinguishing it from traditional vulnerabilities and exploring why it often goes undetected by conventional security tools. A panel of experts, including researchers, analysts and industry veterans, will break down real-world examples, discuss the challenges of securing open source software and provide actionable strategies for mitigating risks. Attendees will leave with a deeper understanding of the evolving security landscape and practical steps to protect their software supply chain.

## Observability
“[ An Exemplary Path: Leveraging eBPFs and OpenTelemetry to Auto-instrument for Exemplars](https://kccnceu2025.sched.com/event/1txEI/an-exemplary-path-leveraging-ebpfs-and-opentelemetry-to-auto-instrument-for-exemplars-charlie-le-kruthika-prasanna-simha-apple?iframe=no&w=100%&sidebar=yes&bg=no)” — Charlie Le and Kruthika Prasanna Simha, Apple

This talk will explore how eBPF and OpenTelemetry can work together to automate exemplar generation without requiring manual instrumentation. You’ll learn how eBPF’s in-kernel aggregation capabilities enable real-time metric and trace collection, seamlessly integrating with OpenTelemetry to enhance observability.

“** The Missing Metrics: Measuring Memory Interference in Cloud Native Systems**“

**—**Jonathan Perry, PerfPod
This session presents the latest research on detecting memory interference, including findings from Google, Alibaba and Meta’s production environments. We’ll explore how modern CPU performance counters can identify noisy neighbors, examine real-world patterns that trigger interference (like garbage collection and container image decompression) and demonstrate practical approaches to measure these effects in Kubernetes environments.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)