# Tutorial: Set Up a Cloud Native GPU Testbed With Nvkind Kubernetes
![Featued image for: Tutorial: Set Up a Cloud Native GPU Testbed With Nvkind Kubernetes](https://cdn.thenewstack.io/media/2025/03/172a3446-kind-1024x768.png)
[DevOps engineers](https://thenewstack.io/DevOps/) and [developers](https://thenewstack.io/developer-tools/) are familiar with [kind](https://kind.sigs.k8s.io), a [Kubernetes](https://thenewstack.io/kubernetes/) development environment built on [Docker](https://www.docker.com/?utm_content=inline+mention). In `kind`
, the control plane and nodes of the cluster operate as individual containers. While `kind`
is easy to use, accessing GPUs from the cluster can be challenging.
This tutorial walks you through installing `nvkind`
from [Nvidia](https://thenewstack.io/nvidia-unveils-next-gen-rubin-and-feynman-architectures-pushing-ai-power-limits/), a GPU-aware `kind`
cluster for running cloud native AI workloads in a development or test environment.

My environment consists of a host machine powered by a single Nvidia H100 GPU. We aim to deploy a pod within the `nvkind`
cluster with access to the same GPU.

## Prerequisites
- GPU hosting based on
[Ubuntu 22.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/) [Go](https://go.dev/doc/install)[Docker Engine](https://docs.docker.com/engine/install/ubuntu/)[Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)[Kubectl](https://kubernetes.io/docs/tasks/tools/)[Helm](https://helm.sh/docs/intro/install/)[Nvidia driver](https://www.nvidia.com/download/index.aspx)[Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
Please ensure that Docker is correctly configured with Nvidia runtime as the default. Then you can access the GPU from a Docker container.

## Compile and Install the Nvkind Binary
Clone the GitHub repository of `nvkind`
and build the binary.

1234 |
git clone https://github.com/NVIDIA/nvkind.gitcd nvkindmakesudo cp ./nvkind /usr/local/bin/ |
Execute the `nvkind`
binary to check that the build has been successfully completed.
## Define a Template and Create the Cluster
Nvkind accepts a configuration file that gives fine-grained control on exposing GPUs to worker nodes. Since we only have one GPU, we will expose it to the worker node.

Create a YAML file called `nvkind-cluster.yaml`
with the below content:

12345678 |
kind: ClusterapiVersion: kind.x-k8s.io/v1alpha4nodes:- role: control-plane- role: worker extraMounts: - hostPath: /dev/null containerPath: /var/run/nvidia-container-devices/all |
Finally, we will create a cluster based on the above template.
1 |
nvkind cluster create --config-template=nvkind-cluster.yaml |
You can now access the cluster with the `kubectl`
CLI.

## Install the Nvidia GPU Operator
With the cluster in place, we will install the GPU operator to access the underlying AI accelerator.

12345 |
helm repo add nvidia https://helm.ngc.nvidia.com/nvidiahelm repo updatehelm install --wait --generate-name \ -n gpu-operator --create-namespace \ nvidia/gpu-operator --set driver.enabled=false |
Ensure all the pods in the `gpu-operator`
namespace are healthy.
## Run a Workload To Test GPU Access
Let’s create a test pod to verify GPU access.

1 |
<img class="aligncenter size-large wp-image-22779667" src="https://cdn.thenewstack.io/media/2025/03/4a006a11-nvkind-6-1024x291.png" alt="" width="1024" height="291" /> |
We have successfully installed, configured and tested the `nvkind`
cluster on an H100 GPU.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)