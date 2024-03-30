## 警告

此帖子可能包含不准确的信息或部分信息或解决方案。

为了减少我的文档积压，我决定发布由 AI 辅助完成的几乎完成的草稿。

我撰写了以下内容的大部分，但使用了生成式 AI 来格式化、组织和完成帖子。我确信在此过程中会丢失一些语调。

如果您发现任何问题，请留言！

*(最初创建于 2019 年 6 月 4 日)*

## 概述

[#](#overview)

Kubectl 是访问 Kubernetes 集群的核心。文档传统上专注于 Linux，此帖子提供了在 Windows 10 上使用 kubectl 的最佳实践，包括：

- [为 PowerShell 设置 kubectl](#setup-kubectl-for-powershell)
- [在公司代理后面使用 kubectl](#setup-kubectl-for-use-behind-a-company-proxy)
- [向 kubectl 添加集群](#adding-a-cluster-to-kubectl)
- [常见的 kubectl 多集群命令](#common-multi-cluster-kubectl-commands)
- [升级 kubectl](#upgrading-kubectl)
- [故障排除和提示](#help-and-troubleshooting)

随着 Kubernetes 1.14 宣布完全支持 Windows 节点，现在有更多关于在 Windows 上运行 kubectl 的文档。此帖子将这些内容与实际经验相结合，以提供全面的指导。您可以根据组织的特定设置进行调整。

### 需了解的关键术语

[#](#key-terms-to-know)

| 术语 | 说明 |
|---|---|
| kubectl | 用于对 Kubernetes 集群运行命令的 CLI |
| 上下文 | 一个友好名称下的访问参数组（集群、用户、命名空间） |
| kubeconfig | 包含 kubectl 用于身份验证的上下文的配置文件 |
| 代理 | 一个公司拥有的服务器，用于过滤和控制外部互联网访问 |

### 为何采用此方法？

[#](#why-this-approach)

- 无需手动编辑 kubeconfig 文件
- 跨环境统一 kubectl 工作流
- 简化开发人员入职
- 每个集群和命名空间的自定义上下文

### 要求

[#](#requirements)

- Windows 10
- PowerShell v5.2+
- 互联网访问权限，用于下载 kubectl.exe

## 为 PowerShell 设置 kubectl

[#](#setup-kubectl-for-powershell)

初始设置只需执行一次：

- 为 kubectl 二进制文件创建一个文件夹：

```
New-Item -ItemType directory -Path "C:\k"
```

- 将文件夹添加到您的 $PATH：

```
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\k", "User")
```

注意：更改在新 PowerShell 会话中生效

- 下载 kubectl.exe（版本应与您的集群匹配）并将其放在 C:\k 中

- 验证 kubectl 是否正常工作：

```
kubectl version --client
```

## 在公司代理后面使用 kubectl

[#](#setup-kubectl-for-use-behind-a-company-proxy)

如果您的公司使用代理服务器，您可能需要配置 HTTP_PROXY、HTTPS_PROXY 和 NO_PROXY 环境变量，以便 kubectl 连接到您的集群。

### 代理变量 101

[#](#proxy-variables-101)

代理旨在成为一种在大型环境中规范和保护出站流量的方法。正确配置您的 kubectl / PowerShell 基于两个重要参数：

- 用于 NO_PROXY 的内部 Kubernetes 集群 HTTPS API
- 用于 HTTP_PROXY 和 HTTPS_PROXY 的公司代理 URL:PORT

| 变量 | 说明 | 示例 |
|---|---|---|
| NO_PROXY | 应绕过代理的 IP/域（以逗号分隔） | "corp.com,10.0.0.0/8" |
| HTTP_PROXY | 用于 HTTP 流量的代理服务器 URL | "http://proxy.corp.com:80" |
| HTTPS_PROXY | 用于 HTTPS 流量的代理服务器 URL | "http://proxy.corp.com:443" |

我**不**应在何时设置 NO_PROXY？

- 如果您的集群是外部（公共）集群

我应在何时设置 NO_PROXY？

- 如果您的集群是内部（私有）集群

### 推荐设置

[#](#recommended-settings)

要在通过代理发送外部流量的同时直接路由所有内部 IP：

```
[Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://proxy.corp.com:80", "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://proxy.corp.com:443", "User")
[Environment]::SetEnvironmentVariable("NO_PROXY", "localhost,127.0.0.1,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16", "User")
```

重新启动 PowerShell 以使更改生效

## 向 kubectl 添加集群

[#](#adding-a-cluster-to-kubectl)

- 从您的管理员那里获取集群 API 服务器 URL 和身份验证详细信息
- 创建集群上下文：

```
kubectl config set-cluster mycluster --server=https://k8sapi.corp.com:6443 --certificate-authority=./ca.crt --embed-certs
```

- 为上下文设置凭据：

```
kubectl config set-credentials mycluster-admin --token="<bearer token here>"
```

- 创建一个将集群和用户联系在一起的上下文：

```
kubectl config set-context mycluster --cluster=mycluster --user=mycluster-admin
```

- 开始使用新上下文：

```
kubectl config use-context mycluster
```

## 常见的 kubectl 多集群命令

[#](#common-multi-cluster-kubectl-commands)

- 显示当前上下文

```
kubectl config current-context
```

- 切换上下文

```
kubectl config use-context mycluster
```

- 列出可用上下文

```
kubectl config get-contexts
```

- 为上下文设置默认命名空间

```
kubectl config set-context --current --namespace=dev
```

- 重命名上下文

```
kubectl config rename-context old-name new-name
```
## 删除上下文
```
kubectl config delete-context mycluster
```

## 升级 kubectl
[升级 kubectl](#upgrading-kubectl)
- 下载新的 kubectl.exe 二进制文件
- 替换 kubectl 目录中现有的文件（例如 C:\k）

## 帮助和故障排除
[帮助和故障排除](#help-and-troubleshooting)

### 修复 kubectl 性能缓慢
[修复 kubectl 性能缓慢](#fix-slow-kubectl-performance)
缓慢通常是由 kubectl 使用网络驱动器作为缓存造成的。通过覆盖 $HOME 来修复：
```powershell
[Environment]::SetEnvironmentVariable("HOME", $env:USERPROFILE, "User")
```
警告：这将重置您的 kubectl 配置位置并删除现有配置

### 还原所有代理设置
[还原所有代理设置](#revert-all-proxy-settings)
```powershell
[Environment]::SetEnvironmentVariable("HTTP_PROXY", $null, "Machine")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", $null, "Machine")
[Environment]::SetEnvironmentVariable("NO_PROXY", $null, "Machine")
```

### 提示
[提示](#tips)
- 使用 `kalias` 而不是 `kubectl`，方法是将二进制文件重命名为 `k.exe`
- 使用以下命令备份 kubeconfig：
```powershell
$env:KUBECONFIG_SAVE=$env:KUBECONFIG
```
- 使用以下命令还原 kubeconfig：
```powershell
$env:KUBECONFIG=$env:KUBECONFIG_SAVE
```

通过此配置，您将在 Windows 上拥有一个健壮的 kubectl 设置，该设置可与公司代理和多个 Kubernetes 集群无缝协作。关键是利用上下文来组织对集群和命名空间的访问。将其与 PowerShell 环境变量结合使用以进行动态配置。