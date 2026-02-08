Kubernetes continues to evolve and mature as the most preferred orchestration platform for containerized applications and microservices. Kubernetes 1.35, [the most recent version](https://thenewstack.io/kubernetes-1-35-timbernetes-introduces-vertical-scaling/), released in mid-December 2025, offers several enhancements that are now generally available. These features bring reliability and efficiency to workloads running on Kubernetes clusters.

This article focuses on five major enhancements that are generally available in Kubernetes 1.35.

## In-place pod resource updates

[In-place pod resource update](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) is the standout GA feature of the latest Kubernetes release. In prior versions, modifying CPU, memory requests, and limits on a container forced a pod restart, disrupting stateful workloads and long-running processes. With the in-place pod vertical scaling feature, you can resize the resources of a running pod’s containers seamlessly without killing the pod.

Implementing this capability is similar to manipulating the specifications of an existing pod. By using `kubectl patch` or `kubectl edit`, you can directly change the CPU and memory requests. When manipulating controllers such as deployments and StatefulSets, the spec can be changed and applied to make it persistent. Remember that this capability is limited to CPU and memory, not other resources such as ephemeral storage, which still forces a pod restart.

This feature has a significant impact on pod vertical autoscaling. When integrated with [Vertical Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) (VPA), a pod can be vertically scaled based on real-time metrics from sources such as the Metrics Server or Prometheus. It’s especially useful for managing stateful services, where restarts trigger data rebalancing or failovers. For AI and machine learning (ML) workloads, it helps preserve in-memory caches and model checkpoints, minimizing interruptions during training, fine-tuning, and inference.

DevOps professionals should be aware of the potential limitations of this feature. The host node must have sufficient resources available before scaling up the pod’s CPU or memory allocation. Overcommitting resources may lead to out-of-memory (OOM) errors or pod eviction. Use commands like `kubectl describe pod` to check the status of resizes, and pair this with the Cluster Autoscaler for proactive node provisioning.

## Fine-grained supplemental group control

Security in shared Kubernetes clusters depends on effective management of group permissions for file access. The new [supplemental groups policy](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#supplementalgroupspolicy) field, now GA, provides precise control over how supplemental Unix groups are assigned to individual containers in a pod.

Previously, all containers in a pod inherited the same set of supplemental groups from the pod’s top-level [security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/). This could lead to overly permissive access in configurations with multiple containers in the same pod. The new approach provides options such as merging all groups from containers or applying a strict mode that uses only explicitly specified groups per container, preventing unintended inheritance.

DevOps and DevSecOps engineers can configure this in a pod’s security context, choosing the policy type and then defining groups as needed per container. This approach ensures that individual containers receive only their designated groups, enforcing strong security and isolation.

For multitenant clusters, this reduces the risk of accessing shared volumes defined via persistent volume claims (PVCs) using POSIX access control lists. It allows legacy applications that rely on group-based permissions to operate securely alongside other workloads, without granting broad access that violates the principle of least privilege. This is especially useful in highly regulated sectors such as financial services and health care, where detailed audit trails must be maintained for compliance.

Combining this feature with Pod Security Admission enables a comprehensive security framework. DevSecOps teams can audit existing pods through policy enforcement tools such as [Open Policy Agent](https://www.openpolicyagent.org/) (OPA) or [Kyverno](https://kyverno.io/) to mandate strict mode. By narrowing potential attack surfaces, this feature helps meet benchmarks such as those from the [Center for Internet Security](https://www.cisecurity.org/benchmark/kubernetes) (CIS) for Kubernetes.

## PreferSameNode traffic distribution

Networking efficiency is crucial in high-throughput clusters, and the GA of the [PreferSameNode](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution) option in the traffic distribution field for services effectively addresses this. This policy directs components, such as kube-proxy or Extended Berkeley Packet Filter (eBPF) alternatives like Cilium, to prioritize endpoints on the same node as the requesting pod, with a fallback to cross-node endpoints only if necessary.

[DevOps engineers](https://www.thenewstack.io/DevOps) can enable it by setting the traffic distribution field in the service specification to PreferSameNode. This ensures that node locality is enforced across cluster-wide internal traffic, thereby reducing network hops and latency.

Drawing on concepts from topology awareness, it minimizes latency and is well-suited for architectures with chatty microservices, where frequent intracluster communication occurs, such as in API gateways or message queues. In sidecar-based patterns, such as those in [Istio](https://istio.io/), it reduces overall network overhead, leading to faster response times. Applications with node-local caches, such as Redis instances, see reduced cross-node traffic, which can lower data-transfer costs in cloud environments.

Real-world measurements show meaningful latency reductions for node‑local traffic paths, especially in latency‑sensitive services. DevOps teams can validate these gains with simple tests, such as running curl commands from within pods to measure response times, or using eBPF-based observability tools for deeper insights. The feature works across all service types, including headless ones, but monitoring for load imbalances in uneven workloads is advisable — integrate it with the Horizontal Pod Autoscaler for balanced scaling.

## Structured authentication configuration

Configuring authentication in Kubernetes relied heavily on a collection of fragmented kube-apiserver flags, which are error-prone and difficult to track in version control. The GA of [structured authentication configuration](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) introduces a declarative, versioned API via a dedicated Authentication configuration kind, consolidating all settings into a single, manageable YAML file.

This file is referenced via a specific flag on the API server and contains settings for various authentication methods, including client certificate authorities, webhooks, OIDC providers, and anonymous access, all in a unified structure.

For cluster administrators, this shift supports GitOps workflows, especially when launching clusters to [CAPI](https://cluster-api.sigs.k8s.io/). With the configuration stored in Git repositories, changes can be reviewed through pull requests and applied using tools like Flux and Argo CD. Inspecting the current setup becomes simpler with standard kubectl commands. It also eases version upgrades by leveraging versioned APIs that maintain compatibility.

In enterprise settings, this reduces the likelihood of misconfigurations that might expose clusters to unauthorized entry. It complements role-based access control (RBAC) for more refined permissions management. Testing new configurations in staging clusters is recommended to prevent operational disruptions.

## OCI image volumes

[OCI image volumes](https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/), now GA-stable, enable mounting OCI-compliant container images as read-only volumes in pods. This leverages existing container registries but treats the images purely as data repositories rather than executable containers. Though this is not GA yet, it is stable and enabled by default for Kubernetes 1.35 clusters.

The pod specification now supports adding a volume that references an image by its registry path and pull policy. Kubernetes pulls the image layers and mounts them at a specified path within the container, providing read-only access to the files within the image.

This approach separates large or frequently updated data from application images, keeping the latter lightweight. It’s particularly useful in AI and ML scenarios, where models from repositories like Hugging Face can be versioned and pulled independently. Similarly, it simplifies distributing content bundles for web applications or shared utilities in CI/CD pipelines, allowing reuse across namespaces with familiar tagging mechanisms.

Advantages include quicker image builds, less storage redundancy, and streamlined versioning. The read-only nature enhances security by preventing modifications. Administrators should ensure consistent handling of pull secrets and monitor registry usage limits. Building these data images can be facilitated by tools designed for container image creation.

## Conclusion

Kubernetes 1.35’s GA features empower admins to build [more resilient, efficient clusters](https://thenewstack.io/kubernetes-get-the-most-from-dynamic-resource-allocation/). Get started by setting up a test environment running the latest version of Kubernetes and testing these features in a nonproduction environment.

In the upcoming parts of this series, I will provide a deep dive into each feature, including step-by-step guides and tutorials. Stay tuned!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)