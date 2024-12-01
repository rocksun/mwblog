In this blog, you will learn about the tools that you can use to debug DNS Request Flows in Kubernetes Clusters. We will also cover the different debugging scenarios and how to fix each of them.

This blog is based on the talk from Qasim Sarfraz at ContainerDays 2024. You can watch the full version on Youtube: [Demystifying DNS: A Guide to Understanding and Debugging Request Flows in Kubernetes Clusters](https://www.youtube.com/watch?v=KQpZg_NqbZw).

The topics below will be covered:

- Understanding DNS Components and Request Flows
- Challenges of DNS Debugging
- Tools for DNS Debugging
- CoreDNS log plugin
- Hubble
- Inspektor Gadget
- Debugging scenarios
## Understanding DNS Components and Request Flows
To effectively debug DNS issues within a Kubernetes cluster, it’s crucial to understand the DNS architecture and request flows. Typical components involved in DNS requests within a cluster include:

- Application Pod
- Node Local DNS (optional)
- CoreDNS Service and Pod
- Upstream DNS Server
The DNS request journey begins with the application pod. From there, the request may pass through a caching layer like NodeLocal DNS before reaching the CoreDNS in Kubernetes. If the requested domain is external, the CoreDNS will then forward the request to an upstream DNS server.

## The challenges of DNS Debugging
DNS debugging in Kubernetes can be complex due to hidden systems and limited visibility across the entire cluster. Traditional tools like [ tcpdump](https://www.tcpdump.org/) can provide insights into request flows, but they lack cluster-wide aggregation and Kubernetes-specific context, making it difficult to trace DNS requests across multiple nodes.

## Tools for a Deep Dive into Request Flows
Several tools are available to trace DNS request flows effectively in Kubernetes.

## CoreDNS Log Plugin
The [CoreDNS log plugin](https://coredns.io/plugins/log/) is built-in, requires minimal setup, and logs DNS transactions directly from CoreDNS. It allows filtering by domain and response class, providing information on the Client IP, Query ID, Response Code, and Response Duration.

Here’s an example of a sample output:

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-1.png)
## Hubble
[Hubble](https://github.com/cilium/hubble) provides network, service, and security observability for Kubernetes. It is Built on top of Cilium and eBPF, and it offers flow inspection capabilities through its CLI, allowing users to trace DNS requests across the cluster.
![](/static/debugging-dns-request-flows-in-kubernetes-clusters-2.png)
#### How to conduct flow inspection using Hubble CLI:
Before tracing DNS request flows with Hubble, you’ll need to prepare your setup:

**Step 1**: Install Cilium with Layer 7 (L7) Proxy Support. Follow [Cilium’s official documentation](https://docs.cilium.io/en/stable/network/servicemesh/l7-traffic-management/) to enable L7 proxy support during installation.
**Step 2**: Create Cilium network policies to enable DNS traffic for `mypod`
and CoreDNS. Define and apply policies that allow traffic for DNS resolution, and ensure the policies have the correct labels for targeting specific pods.
Keep in mind that network policies block traffic by default, so confirm that the policies are configured to allow necessary traffic.

**Step 3**: Verify the setup. Ensure that all required traffic paths are open for observability purposes.
**Step 4**: After verifying the setup, deploy Hubble CLI to trace DNS request flows.
You can apply filters to focus specifically on DNS protocol traffic, and the CLI will begin displaying DNS requests, responses, and related metadata, providing valuable insights into traffic flows.

Here’s an example of what the output should look like:

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-3.png)
See how you can use **jq** to filter specific errors, making hubble powerful for DNS troubleshooting.

## Inspektor Gadget
[Inspektor Gadget](https://github.com/inspektor-gadget/inspektor-gadget) is the final toolset we’ll cover for inspecting Kubernetes and Linux systems. Inspektor Gadget’s DNS gadget traces DNS requests and responses using eBPF (Extended Berkeley Packet Filter), allowing for rich OS-level context and Kubernetes enrichment. You can deploy it as a DaemonSet in Kubernetes and interact with it via the `kubectl gadget`
plugin, or test it without installation using `kubectl`
node debug.
For more information, visit the [Guide](https://www.inspektor-gadget.io/docs/latest/gadgets/trace_dns) and [Source Code](https://github.com/inspektor-gadget/inspektor-gadget/tree/main/gadgets/trace_dns) for DNS gadget.

**How to debug an application pod using Inspektor Gadget**:
**Step 1**: Run DNS Gadget on Your Kubernetes Cluster
To start debugging an application pod using Inspektor Gadget, ensure you have the appropriate OCI image for your gadgets, accessible through the Inspektor Gadget GitHub container registry. You can discover official and community published gadgets at [artifacthub.io](https://artifacthub.io/packages/search?kind=22&verified_publisher=true&official=true&cncf=true&sort=relevance&page=1).

Use the `kubectl gadget`
command to trace DNS requests for your application pod. This command targets the specific namespace and pod you’re interested in, allowing you to see DNS queries being made.

**Step 2**: Analyze the Initial Output
This is how the output should look like:

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-4.png)
The output will show events such as DNS queries and responses, complete with Kubernetes enrichment data, such as:

- Source: The source (mypod pod) enriched with Kubernetes resource information.
- Destination: The destination (kube-dns service) with Kubernetes resource information.
- Query Information and Response Codes: Details of the DNS query and their response status.
This compact view provides a straightforward method to inspect DNS requests for specific pods.

**Step 3**: Broaden Your Trace Scope
If you want to observe DNS activity beyond a single pod and include DNS requests across different namespaces, adjust the filters in your command. You can filter by pod names or namespaces, which helps isolate issues related to specific components or services. This approach gives visibility into DNS queries exiting a pod and arriving at a CoreDNS (kube-dns) component. Also, since it is an external name (example.com) CoreDNS forwards it to the upstream server (192.168.49.1) by creating a new request (ID=2c39) as show below:

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-5.png)
**Step 4**: Expand Trace Scope Beyond Pod Filters
By removing specific pod filters, you gain a more extensive view of the network interactions within your cluster, especially what happens to the request on the node. This broader scope is particularly useful when diagnosing issues happening across the entire cluster.

Here’s an example of the expected output:

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-6.png)
In this output, you can see all the lines without enrichment, which reflect what happens to the request at a node level.

These lines show how requests are processed on the host. You can use the Network Namespace ID (**4026532220**) to confirm that actions are happening at the host level, providing a clear picture of node-level processing.

Additionally, **IP Translation** is crucial here: you can observe how IP tables convert and route kube-dns service IPs to specific CoreDNS pods. This ensures proper routing and helps diagnose potential issues with request handling within the node infrastructure.

## Summary of the tools
In the following table, you can find the main features of each of the tools we covered:

CoreDNS log plugin | Hubble | Inspektor Gadget |
---|---|---|
Ideal for initial inspection, but its scope is limited to CoreDNS. | Provides a compact overview of request flows with enrichment and retrospective analysis. | Offers rich DNS traces with OS context and kubernetes enrichment / filtering. |
Requires configuration changes for use. | Requires Cilium CNI / specific policies to be in place for L7 flow visibility. | Extensible through custom gadget images; no support for TCP. |
## Concluding Your Kubernetes DNS Debugging Journey
Now that you are familiar with the various tools available for DNS debugging, let’s explore some practical debugging scenarios. For a hands-on experience, you can also [watch the real time demo with the detailed steps](https://www.youtube.com/watch?v=KQpZg_NqbZw?t=1049).

## Scenario 1: Verifying the Health of an Upstream DNS Server
In this scenario, we’ll ensure that requests from CoreDNS to an upstream DNS server are performing as expected. You can check the script that was used [in this file](https://github.com/mqasimsarfraz/talks/tree/main/ContainerDays-2024/debug-scenario1).

**Step 1**: Ensure that the pod is generating DNS requests.
Disable any cache plugins in CoreDNS to prevent requests from being cached, which can obscure the tracing of queries to the upstream server. Edit the CoreDNS `Corefile`
to remove or comment out the `cache`
line.

Restart CoreDNS pods to apply changes swiftly.

**Step 2**: Deploy a test pod that sends DNS requests to domains like `example.com`
and `unknown.example.com`
to generate a mixture of successful and erroneous requests.
**Step 3**: Run Inspektor Gadget.
Use the DNS gadget to filter and observe responses from upstream servers. Focus on the `kube-system`
namespace and the CoreDNS pods with attention to response codes.

**Step 4**: Interpret the results.
Successful responses for `example.com`
indicate proper functioning, while `name error`
responses for `unknown.example.com`
signify expected behavior for unresolved domains.

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-7.png)
## Scenario 2: Identifying Unsuccessful DNS Response
In this scenario, we will determine where within the network a DNS request might be failing. For reference, you can use the script that was used [in this file](https://github.com/mqasimsarfraz/talks/tree/main/ContainerDays-2024/debug-scenario2).

**Step 1**: Intentionally create failures.
To simulate a failure, modify the CoreDNS configuration by using the `erratic`
plugin to purposely drop requests for `example.com`
.

After editing, save the necessary changes and allow them to take effect as the CoreDNS pods restart.

**Step 2**: Generate a DNS Request.
Initiate a DNS lookup with the test pod for `example.com`
and monitor for failures using Inspektor Gadget.

**Step 3**: Analyze the Trace Output
The trace should reveal the request process, ending at CoreDNS without a forward to the upstream server, confirming the drop. This indicates a deliberate failure at CoreDNS.

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-8.png)
## Conclusion
Debugging DNS in Kubernetes requires an understanding of internal request flows and the right tools for observability and tracing. In this blog, we covered three key tools - CoreDNS log plugin, Hubble, and Inspektor Gadget - that can help you to understand what happens to your request at a deeper level. We also explored two practical debugging scenarios using these tools.

For a more detailed guide, watch the full talk at ContainerDays: [Demystifying DNS: A Guide to Understanding and Debugging Request Flows in Kubernetes Clusters](https://www.youtube.com/watch?v=KQpZg_NqbZw&t=308s).

Check out the [slides of the presentation](https://github.com/mqasimsarfraz/talks/blob/main/ContainerDays-2024/Demystifying%20DNS_%20A%20Guide%20to%20Understanding%20and%20Debugging%20Request%20Flows%20in%20Kubernetes%20Clusters.pdf).