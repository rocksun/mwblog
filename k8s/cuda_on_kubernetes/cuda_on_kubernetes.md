<!--
title: 在 Kubernetes 上使用 CUDA
cover: ./cover.png
-->

随着大语言模型(LLM)时代的到来，我一直想玩玩一些[开源的](https://github.com/gradio-app/gradio)[自托管小工具](https://github.com/lllyasviel/Fooocus)。我正在使用一台老工作站作为家庭实验室，方便的是它安装了一个老的 NVIDIA GPU。由于我正在运行一个 Kubernetes 集群，我希望将 GPU 暴露给工作负载，以便利用现有的基础设施轻松托管、调度和部署 GPU 助力的应用程序。

> 译自 [CUDA on Kubernetes](https://blog.stonegarden.dev/articles/2024/01/cuda_on_kubernetes/)。作者 Vegard S. Hagen 。

这篇文章主要是为了作为参考材料，当我开始实际的应用程序时，希望它也能帮助其他人。

我目前在一台运行 Debian 11 的裸机单节点上使用 `containerd` 运行 Kubernetes 1.28“集群”，所以这篇文章将假设一个类似的设置，尽管我尝试链接到其他设置的相关资源。

将来，当我切换到使用 [Proxmox](https://www.proxmox.com/en/) 或类似的虚拟化时，我可能也会更新这篇文章以新增配置。

## 配置

NVIDIA [k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin#quick-start) 的前提条件是节点上运行工作负载的 NVIDIA [CUDA 驱动](https://developer.nvidia.com/cuda-downloads)程序和[容器工具包](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)能够正常工作。

### CUDA 驱动程序

开始之前，请确保您没有任何现有的 NVIDIA 驱动程序，可以使用以下命令卸载它们:

```
sudo apt-get autoremove cuda* nvidia* nouveau* --purge
```

并重新启动计算机。

> 卸载图形驱动程序可能会破坏您的桌面环境。它应该会在下面的步骤中使用新的驱动程序自行修复。

在安装 GPU 驱动程序之前，我们需要适当的内核头文件，可以通过运行以下命令获取:

```
sudo apt-get install linux-headers-$(uname -r)
```

接下来我们添加 CUDA 驱动程序的密钥环和仓库

```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g')
wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.1-1_all.deb 
sudo dpkg -i cuda-keyring_1.1-1_all.deb
```

这样我们就可以轻松地使用 `apt-get` 安装驱动程序:

```
sudo apt-get update
sudo apt-get install cuda-drivers
```

重启并通过运行以下命令确保驱动程序正常工作:

```
nvidia-smi
```

然后您应该会看到有关连接的 GPU 和驱动程序版本的信息。

```
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 545.23.08              Driver Version: 545.23.08    CUDA Version: 12.3     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce GTX 1080        On  | 00000000:02:00.0 Off |                  N/A |
| 30%   37C    P8              12W / 180W |      1MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+

```

### 容器工具包

按照 NVIDIA 容器工具包适用于 `apt` 的[安装指南](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)，我们首先配置容器工具包软件仓库

```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
  sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg  && \
  curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

在安装 `nvidia-container-toolkit` 之前

```
sudo apt-get update
sudo apt-get install nvidia-container-toolkit
```

### containerd 运行时环境

备份现有的 `containerd` 配置，以防接下来的步骤出错

```
sudo cp /etc/containerd/config.toml /etc/containerd/config.toml.bak
```

然后，我们可以根据 [k8s-device-plugin 自述文件](https://github.com/NVIDIA/k8s-device-plugin?tab=readme-ov-file#configure-containerd)手动配置 `containerd`，或者运行

```
sudo nvidia-ctk runtime configure --runtime=containerd
```

来将 `nvidia-container-runtime` 设置为 `containerd` 的默认底层运行时环境。

## NVIDIA 设备插件

安装工作的 CUDA 驱动程序、设置 NVIDIA 容器工具包和将 containerd 配置为使用 NVIDIA 运行时环境，我们现在可以使用其 Helm chart 来应用 NVIDIA 设备插件。

```
helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
helm repo update
helm upgrade -i nvdp nvdp/nvidia-device-plugin \
  --namespace nvidia-device-plugin \
  --include-crds \
  --create-namespace \
  --version 0.14.3
```

### 时间切片(可选)

NVIDIA 设备插件的默认行为是将整个 GPU 分配给单个 pod，这意味着如果有多个 pod 请求 GPU 时间，每次只会调度一个 pod。

为了克服这个问题，我们可以配置 GPU 的时间切片，即 GPU 在 pod 之间共享。

首先创建一个 `ConfigMap`，配置最大 10 个副本(第 14 行)来配置时间切片。

```yaml
# cm-time-slicing.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-time-slicing
  namespace: nvidia-device-plugin
data:
  time-slicing: |-
    version: v1
    sharing:
      timeSlicing:
        resources:
          - name: nvidia.com/gpu
            replicas: 10
```

然后应用 `ConfigMap`，并通过名称(第 5 行)和提供的默认配置键(第 8 行)配置 `nvidia-device-plugin` 使用它。

```bash
kubectl apply -f cm-time-slicing.yaml

helm upgrade nvdp nvdp/nvidia-device-plugin \
  --reuse-values \
  --set config.name=cm-time-slicing \
  --set config.default=time-slicing
```

现在您应该通过运行下面的命令看到每个节点每个 GPU 有 10 个 `nvidia.com/gpu` 的容量：

```bash
kubectl get node -o 'jsonpath={.items[*].status.capacity}' | jq
```

```json
{
  ...
  "nvidia.com/gpu": "10",
  ...
}
```

请注意，工作负载从同一 GPU 获取副本，每个工作负载都可以访问相同的 GPU 内存，并在同一故障域中运行，这意味着如果一个工作负载崩溃，它们都会崩溃。

有关配置设备插件的更多详细信息，请参阅 [GitHub 上的自述文件](https://github.com/NVIDIA/k8s-device-plugin?tab=readme-ov-file#configuring-the-device-plugins-helm-chart)。

## 运行工作负载

假设配置都正常，我们现在可以尝试运行一个测试工作负载，通过启动一个请求 GPU 资源的 pod 来使用 GPU(第 11-13 行)。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-vectoradd
  namespace: cuda-test
spec:
  restartPolicy: OnFailure
  containers:
  - name: cuda-vectoradd
    image: "nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda11.7.1-ubuntu20.04"
    resources:
      limits:
        nvidia.com/gpu: "1"
```

```bash
kubectl create ns cuda-test
kubectl apply -f cuda-vectoradd.yaml
```

如果一切顺利，工作负载的日志应该显示:

```bash
kubectl logs -n cuda-test cuda-vectoradd
[Vector addition of 50000 elements]
... Test PASSED
```

如果一切正常，只需在每个您想要访问 GPU 资源的工作负载上添加 `nvidia.com/gpu` 的资源限制即可。

```yaml
resources:
  limits:
    nvidia.com/gpu: "1"
```

查看请求 GPU 资源的 pod 内部，我们也会发现两个与 NVIDIA 相关的环境变量:

```bash
kubectl exec -it <pod> -- env | grep NVIDIA
NVIDIA_DRIVER_CAPABILITIES=compute，video，utility
NVIDIA_VISIBLE_DEVICES=GPU-<UUID>
```

这表明我们在 pod 中有可用的 GPU 加速计算和视频[编码/解码](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new)。

## 故障排除

如果您遇到类似的 pod 启动错误:

```
0/1 nodes are available: 1 Insufficient nvidia.com/gpu. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod..
```

可能是您没有足够的 GPU 资源，请尝试从[“时间切片”部分](https://blog.stonegarden.dev/articles/2024/01/cuda_on_kubernetes/#time-slicing-optional)增加时间切片副本数量，或者购买另一个 GPU，无论对您更划算。

我也遇到过这样的错误，即在重新启动节点后，多个长时间运行的工作负载试图启动时发生错误。重新启动 `nvidia-device-plugin` pod 和请求 GPU 资源的工作负载似乎可以解决该问题。

使用 Argo CD，我添加了一个负的 `sync-wave` [注解](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/)，以确保在工作负载之前启动 `nvidia-device-plugin` 以避免此问题。

```yaml
annotations:
  argocd.argoproj.io/sync-wave: "-1"
```

## 附录

我首先尝试使用 [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html)，我认为这是一个全能的解决方案，它可以安装设备插件以及驱动程序和容器工具包。但是，我无法让它工作，所以我选择了不幸更多的手动方法，将设备插件、驱动程序和容器工具包作为单独的组件进行安装。

可能是我的设置问题，或者我在文档中理解错了什么。如果您有解决方案，我很乐意倾听！

## 总结

我正在使用 [Argo CD 与 Kustomize + Helm](https://blog.stonegarden.dev/articles/2023/09/argocd-kustomize-with-helm/) 尝试遵循 GitOps 最佳实践。 在撰写本文时，我的完整家庭实验室配置可在 [GitHub 上作为参考](https://github.com/vehagn/homelab/tree/daf55205cce79c2ca8cdd6c1c0ff70e1757de3fd/infra/nvidia-device-plugin)。

```yaml
# kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
commonAnnotations:
  argocd.argoproj.io/sync-wave: "-1"

resources:
  - namespace.yaml
  - cm-time-slicing.yaml

helmCharts:
  - name: nvidia-device-plugin
    repo: https://nvidia.github.io/k8s-device-plugin
    version: 0.14.2
    releaseName: "nvidia-device-plugin"
    namespace: nvidia-device-plugin
    includeCRDs: true
    valuesFile: values.yaml
```



```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nvidia-device-plugin
```

```yaml
# values.yaml
config:
  name: cm-time-slicing
  default: time-slicing
```

```yaml
# cm-time-slicing.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-time-slicing
  namespace: nvidia-device-plugin
data:
  time-slicing: |-
    version: v1
    sharing:
      timeSlicing:
        resources:
          - name: nvidia.com/gpu
            replicas: 10
```

