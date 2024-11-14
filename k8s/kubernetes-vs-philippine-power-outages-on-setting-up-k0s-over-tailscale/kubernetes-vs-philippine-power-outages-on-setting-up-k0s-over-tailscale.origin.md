[< BLOG HOME](/blog)
# Kubernetes vs. Philippine Power Outages - On setting up k0s over Tailscale
![Kubernetes power outage orchestration](https://a.storyblok.com/f/153547/1080x608/95e9fc915f/kubernetes-power-outage-orchestration.jpg/m/)
Building a reliable IT system in the Philippines presents unique challenges such as frequent power outages and unreliable internet connectivity. To address these issues effectively, our team has implemented a resilient setup ensuring uninterrupted access to critical services for our end-users.

This guide will walk you through a similar setup using Tailscale and [k0s](https://k0sproject.io/), which can be replicated in your homelab environment. If you're curious only about the setup, feel free to jump to Section II.

## I. The Challenge
To give you some background, our team manages multiple projects for various clients, hosting most services on local servers near them. However, a significant issue we face is frequent power interruptions due to maintenance or emergencies at local substations. These disruptions occur nearly every week, sometimes lasting 8-12 hours, effectively rendering our services unavailable for entire workdays.

## *Side-note: Why not host on cloud?
Well, it's a bit complicated. Some services work well in the cloud (so we've put them there), but others have their own unique needs. For example, let's take a closer look to two of our main projects: [Impactville](https://impactville.com/) and [Lupain.AI](https://www.lupain.ai/landing/new).

Impactville deals with private data from organizations that prefer not to store it in the cloud due to privacy concerns. Meanwhile, Lupain.AI handles sensitive land data from local government units, requiring secure and local storage.

From a cost perspective, Lupain.AI involves intensive processing of satellite data. Using cloud resources could drive up costs, especially with the increasing USD-PHP exchange rates. It's more cost-effective for us to manage these tasks using a self-hosted cluster of GPU nodes.

## Back to the challenge
To summarize our scenario:

We have full control and ownership of nodes distributed across the country.

Our goal is to achieve fault-tolerant services with minimal downtimes (ideally less than 1 minute, with 5-10 minutes being acceptable).

Data redundancy and high availability are essential requirements.

Given these needs, the most viable solution is to set up an orchestrator capable of detecting downtimes, automatically rescheduling services, and distributing them across a cluster of nodes.

In this setup, if one server experiences a power outage, the services will be temporarily shifted to other servers until normal operations resume.

Therefore, adopting Kubernetes is an obvious choice for us. [Kubernetes](https://kubernetes.io/) is an open-source system designed specifically for automating deployment, scaling, and management of containerized applications.

This guide will walk you through the basic setup of deploying your own Kubernetes cluster using [k0s](https://k0sproject.io/) and [Tailscale](https://tailscale.com/).

**Disclaimer:** The setup described here is simplified and may differ from our production setup. Our production environment addresses various complexities such as ISP DNS issues [1][2], rate-limiting, weather-related challenges for Starlink-connected nodes, server security hardening, encryption of redundant data, and cluster ingress. These topics require detailed discussions and are either reserved for future posts or treated as internal know-how.
For a small homelab setup, however, this guide should provide sufficient guidance.

## II. Kubernetes setup
In this guide, we'll set up a Kubernetes cluster using k0s and connect our nodes via Tailscale. Here's an overview of the technologies involved:

### k0s
k0s is an open-source Kubernetes distribution designed for simplicity and versatility. It includes all necessary features to build a Kubernetes cluster and is lightweight enough to run on various environments such as cloud, bare metal, edge, and IoT devices. Its minimal setup and easy configuration make it ideal for our needs.

### Tailscale
While any VPN could be used, Tailscale stands out for its ease of setup, comprehensive documentation, and reliable networking capabilities. MagicDNS, which simplifies DNS management, adds an extra layer of convenience.

### Distributed storage
For distributed storage, you have various options to choose from. The simplest approach is setting up [NFS](https://en.wikipedia.org/wiki/Network_File_System) or [NAS](https://en.wikipedia.org/wiki/Network-attached_storage), though configuring it for high availability (HA) may be required. In our setup, we've chosen to use [SeaweedFS](https://github.com/seaweedfs/seaweedfs), a distributed storage system that provides scalability and efficient management of large data volumes. Note that configuring [SeaweedFS](https://github.com/seaweedfs/seaweedfs) for HA is beyond the scope of this guide.

### Instructions
To begin setting up your Kubernetes cluster, follow these steps:

#### 1. Manual node setup
First, ensure SSH is configured securely to access your nodes. Verify you have SSH access to all nodes and that they use key-based authentication. Disable password authentication temporarily for cluster setup; you can re-enable it later in your SSH configuration.

#### 2. Connect them over VPN
Next, establish a secure connection between your nodes using Tailscale:

Sign up for Tailscale and add your devices to the network. Check

[https://tailscale.com/](https://tailscale.com/)Follow Tailscale's instructions to install and connect Tailscale to your network. See

[https://tailscale.com/kb/1017/install](https://tailscale.com/kb/1017/install)Check that

`tailscale0`
appears in your network interfaces (e.g., via`ifconfig`
).Ensure your control machine, where you'll run

`kubectl`
, is also connected to the Tailscale network.
#### 3. Install k0s
To set up your Kubernetes cluster, follow these steps:

**Install k0s in your control machine**. Begin by installing k0s on your control machine. You can find detailed instructions at [k0s Installation](https://docs.k0sproject.io/stable/install/). Use the command:
```
curl -sSLf https://get.k0s.sh | sudo sh
```
**Use k0sctl for automated deployment:** To streamline the installation across nodes, use k0sctl:
Install k0sctl depending on your OS. Refer to [k0sctl Installation](https://github.com/k0sproject/k0sctl#installation):

```
brew install k0sproject/tap/k0sctl
choco install k0sctl
```
**Generate a k0sctl configuration file:** Create a k0sctl configuration file to define your cluster setup:
```
k0sctl init > k0sctl.yaml
```
Customize the configuration as needed. Here's an example configuration:

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
name: k0s-cluster
spec:
hosts:
- role: controller
ssh:
address: 10.0.0.1 # replace with the controller's IP address
user: root
keyPath: ~/.ssh/id_rsa
- role: worker
ssh:
address: 10.0.0.2 # replace with the worker's IP address
user: root
keyPath: ~/.ssh/id_rsa
```
For further customization, refer to the [k0sctl Configuration Documentation](https://docs.k0sproject.io/stable/configuration/).

**Bootstrap the Cluster: **To initialize and deploy your Kubernetes cluster, execute the following command:
`k0sctl apply --config k0sctl.yaml`
k0sctl will automatically install and deploy k0s on the designated machines within your network, configuring the Kubernetes cluster for operation. Once deployed, generate the kubeconfig file to manage the cluster using kubectl:

```
k0sctl kubeconfig > kubeconfig
kubectl get pods --kubeconfig kubeconfig -A
```
**Uninstall or Reset the Cluster: **If you need to reconfigure or remove the cluster, use the following command:
```
k0sctl reset --config k0sctl.yaml
```
This command resets the cluster configuration, allowing for subsequent deployments or modifications as needed.

#### 4. Configuration
While the previous instructions provide a standard setup, additional configurations are necessary to integrate with Tailscale and manage private container registries effectively.

##### Tailscale-connected Nodes
To ensure proper IP assignment by k0sctl for Tailscale-connected machines, specify the correct network interface in the configuration. For Tailscale, use `tailscale0`
. Here’s an example configuration snippet:

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
hosts:
- ssh:
address: machine-1
privateInterface: tailscale0
role: controller
- ssh:
address: node-2
privateInterface: tailscale0
role: worker
```
##### Private Container Registry
If your application's images needs extra privacy, chances are you're storing container images in a private registry. To ensure that k0s (specifically, containerd) pull the image from the right registry, follow the these instructions:

Create a custom configuration file for containerd on each worker node:

```
sudo nano /etc/k0s/containerd.d registry.toml
```
Add the following content:

```
[plugins."io.containerd.grpc.v1.cri".registry]
config_path = "/etc/containerd/certs.d"
```
This directs containerd to look for hosts in `/etc/containerd/certs.d`
.

Create a

`hosts.toml`
file for your registry domain or IP
```
sudo nano /etc/containerd/certs.d/<registry-domain or ip>:<registry port>/hosts.toml
```
Populate it with:

```
server = "http://<domain or ip>:<port>"
[host."http://<domain or ip>:<port>"]
skip_verify = true # If your registry is not configured via TLS
```
Note: For production environments, ensure TLS certificates are correctly configured. Refer to [containerd documentation](https://github.com/containerd/containerd/blob/main/docs/hosts.md) for additional configuration details.

Once configured, k0s will utilize these settings to pull private images from your registry as needed

##### Networking
Network configuration has proven to be quite challenging, consuming considerable time and effort as we troubleshooted various issues with our server setups. After days of painstaking work, here's what we've uncovered.

For networking, k0s supports various providers for managing inter-pod networking, known formally as a Container Network Interface (CNI). For more detailed information about k0s networking capabilities, you can refer to the official documentation [here](https://docs.k0sproject.io/stable/networking/).

By default, k0s uses the kube-router CNI, known for its lightweight and performant nature. However, we encountered specific issues where inter-pod communication between nodes failed. Key diagnostics such as `nslookup`
failing to connect to nameservers and `traceroute`
showing asterisks led us to investigate further.

After extensive troubleshooting involving iptables, we determined that kube-router was not utilizing the correct interface for communication—in our case, Tailscale. Additionally, kube-router does not currently support explicitly setting the network interface and may not add this functionality in the near future (refer to [GitHub issue #567](https://github.com/cloudnativelabs/kube-router/issues/567)). As a result, we've made the decision to transition to a different CNI.

Another built-in CNI option for k0s is Calico, which offers more flexible configuration options, including network interface settings. If you're encountering issues with kube-router and need to switch to Calico, you can use the following configuration during cluster bootstrap:

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
name: k0s-cluster
spec:
k0s:
config:
spec:
network:
provider: calico # <-- use Calico
calico:
envVars:
IP_AUTODETECTION_METHOD: "interface=tailscale0" # <-- use tailscale
hosts:
- role: controller
ssh:
address: 10.0.0.1 # replace with the controller's IP address
user: root
keyPath: ~/.ssh/id_rsa
- role: worker
ssh:
address: 10.0.0.2 # replace with the worker's IP address
user: root
keyPath: ~/.ssh/id_rsa
```
It's important to note potential edge cases when integrating Calico with Tailscale as discussed [here](https://github.com/tailscale/tailscale/issues/591). To avoid conflicts, we recommend remapping Calico's netfilter packets. This ensures compatibility and smooth operation in your network setup.

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
name: k0s-cluster
spec:
k0s:
config:
spec:
network:
provider: calico
calico:
envVars:
FELIX_IPTABLESMARKMASK: "0xff00ff00" # <- use mask
IP_AUTODETECTION_METHOD: "interface=tailscale0"
```
After redeployment, pods can now communicate with each other across different nodes!

#### Node-local load balancing
With the nodes set up, our Kubernetes cluster now handles inter-node communication effectively, even during power outages. However, there's an important scenario we need to address: *what happens if the control node experiences an outage?* Without a functioning control node, there's no orchestrator to manage pod events, which could lead to downtime for critical services.

To ensure continuous operation, it's essential to plan for high availability of the control plane. This can be achieved by setting up multiple control plane nodes within the cluster.

Fortunately, k0s offers a built-in solution for this with [Node-local load balancing](https://docs.k0sproject.io/stable/nllb/). Adjusting a small portion of the configuration allows us to enhance our setup:

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
name: k0s-cluster
spec:
k0s:
config:
spec:
network:
nodeLocalLoadBalancing:
enabled: true
type: EnvoyProxy
```
#### 5. Use your Kubernetes cluster
Now that your Kubernetes cluster is deployed and configured using the steps outlined above, the final step is to set up kubectl, the Kubernetes command-line tool, on your local machine. This tool allows you to manage your cluster effectively.

Follow these steps to complete the setup:

**Install kubectl**: Install the Kubernetes command-line tool, kubectl, on your local machine. You can download it from the official Kubernetes documentation or use package managers like `apt`
or `brew`
.
**Configure kubeconfig**: Once your cluster is deployed, set the generated kubeconfig file as your default configuration by copying it to the appropriate directory
```
cp kubeconfig ~/.kube/config
```
This step ensures that kubectl uses the correct credentials and configuration to access your Kubernetes cluster.

**Verify setup**: Confirm that kubectl is correctly configured by checking the status of pods in your cluster
`kubectl get pods -A`
This command will list all pods across all namespaces (`-A`
flag), indicating that your cluster is operational and ready to deploy applications.

With kubectl configured, you're now equipped to manage and orchestrate containerized applications on your Kubernetes cluster seamlessly!

## Final Thoughts
Thank you for reading! I appreciate you taking the time to read up to this point ❤ . If you find any parts confusing or have any issues with replication, I'd be happy to help. Just shoot me an email ([thepiesaresquared@gmail.com](mailto:thepiesaresquared@gmail.com)) or DM/tweet me at [@justfizzbuzz](https://twitter.com/justfizzbuzz).

I thoroughly enjoyed the process of making this guide! If you're interested in more posts like this, I invite you to subscribe to this blog, or let's connect and share our posts on [Twitter/X](https://twitter.com/justfizzbuzz)!

Footnotes

[1] [https://answers.netlify.com/t/every-netlify-site-i-visit-cant-be-reached-from-the-philippines/49205?page=2](https://answers.netlify.com/t/every-netlify-site-i-visit-cant-be-reached-from-the-philippines/49205?page=2)

[2] [https://www.reddit.com/r/PinoyProgrammer/comments/wo7qcl/any_pldt_dev_here_why_pldt_blocks_netlify/](https://www.reddit.com/r/PinoyProgrammer/comments/wo7qcl/any_pldt_dev_here_why_pldt_blocks_netlify/)

*This guest post was originally published in the author's *[personal blog](https://justrox.me/kubernetes-vs-philippine-power-outages-a-simple-guide-to-k0s-over-tailscale/)*. Reposted here with permission by the author. Photo by *[natsuki](https://unsplash.com/@myr0326)* / Unsplash.*