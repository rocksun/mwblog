# 教程：使用 Nvkind Kubernetes 设置云原生 GPU 测试平台

![教程：使用 Nvkind Kubernetes 设置云原生 GPU 测试平台的特色图片](https://cdn.thenewstack.io/media/2025/03/172a3446-kind-1024x768.png)

[DevOps 工程师](https://thenewstack.io/DevOps/)和[开发者](https://thenewstack.io/developer-tools/)都很熟悉 [kind](https://kind.sigs.k8s.io)，它是一个构建在 [Docker](https://www.docker.com/?utm_content=inline+mention) 上的 [Kubernetes](https://thenewstack.io/kubernetes/) 开发环境。在 `kind` 中，集群的控制平面和节点作为单独的容器运行。虽然 `kind` 易于使用，但从集群访问 GPU 可能具有挑战性。本教程将引导您从 [Nvidia](https://thenewstack.io/nvidia-unveils-next-gen-rubin-and-feynman-architectures-pushing-ai-power-limits/) 安装 `nvkind`，这是一个支持 GPU 的 `kind` 集群，用于在开发或测试环境中运行云原生 AI 工作负载。

我的环境由一台由单个 Nvidia H100 GPU 驱动的主机组成。我们的目标是在 `nvkind` 集群中部署一个可以访问同一 GPU 的 Pod。

## 前提条件

- 基于以下各项的 GPU 主机：
  - [Ubuntu 22.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/)
  - [Go](https://go.dev/doc/install)
  - [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
  - [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
  - [Kubectl](https://kubernetes.io/docs/tasks/tools/)
  - [Helm](https://helm.sh/docs/intro/install/)
  - [Nvidia driver](https://www.nvidia.com/download/index.aspx)
  - [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

请确保 Docker 已正确配置，并将 Nvidia 运行时作为默认运行时。然后，您可以从 Docker 容器访问 GPU。

## 编译并安装 Nvkind 二进制文件

克隆 `nvkind` 的 GitHub 存储库并构建二进制文件。

```
git clone https://github.com/NVIDIA/nvkind.git
cd nvkind
make
sudo cp ./nvkind /usr/local/bin/
```

执行 `nvkind` 二进制文件以检查构建是否已成功完成。

## 定义模板并创建集群

Nvkind 接受一个配置文件，该文件可以对向工作节点公开 GPU 进行细粒度控制。由于我们只有一个 GPU，我们将把它公开给工作节点。

创建一个名为 `nvkind-cluster.yaml` 的 YAML 文件，内容如下：

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
  extraMounts:
  - hostPath: /dev/null
    containerPath: /var/run/nvidia-container-devices/all
```

最后，我们将基于上述模板创建一个集群。

```
nvkind cluster create --config-template=nvkind-cluster.yaml
```

现在，您可以使用 `kubectl` CLI 访问集群。

## 安装 Nvidia GPU Operator

集群就绪后，我们将安装 GPU Operator 以访问底层 AI 加速器。

```
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update
helm install --wait --generate-name \
 -n gpu-operator --create-namespace \
 nvidia/gpu-operator --set driver.enabled=false
```

确保 `gpu-operator` 命名空间中的所有 Pod 都是健康的。

## 运行工作负载以测试 GPU 访问

让我们创建一个测试 Pod 来验证 GPU 访问。

```
<img class="aligncenter size-large wp-image-22779667" src="https://cdn.thenewstack.io/media/2025/03/4a006a11-nvkind-6-1024x291.png" alt="" width="1024" height="291" />
```

我们已成功在 H100 GPU 上安装、配置和测试了 `nvkind` 集群。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。