# Kubernetes 1.31：kubectl Debug 中的自定义分析功能升级至 Beta 版

在集群中，有多种方法可以对 Pod 和节点进行故障排除。然而，`kubectl debug`
是最简单、使用最广泛和最突出的方法之一。它
提供了一组静态配置文件，每个配置文件都用于不同的角色。例如，从网络管理员的角度来看，
调试节点应该像这样简单：

```
$ kubectl debug node/mynode -it --image=busybox --profile=netadmin
```
另一方面，静态配置文件也带来了固有的僵化性，这对于某些 Pod 来说，与易用性相比，会带来一些影响。因为存在各种类型的 Pod（或节点），它们都有各自的特定需求，不幸的是，有些 Pod 无法仅通过使用静态配置文件进行调试。

以一个简单的 Pod 为例，该 Pod 包含一个容器，其健康状况依赖于一个环境变量：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: example-container
    image: customapp:latest
    env:
    - name: REQUIRED_ENV_VAR
      value: "value1"
```
目前，复制 Pod 是唯一支持在 kubectl debug 中调试此 Pod 的机制。此外，如果用户需要将 `REQUIRED_ENV_VAR`
修改为其他内容
以进行高级故障排除？目前还没有机制可以实现这一点。

## 自定义分析
自定义分析是 `--custom`
标志下提供的新功能，在 kubectl debug 中引入，以提供可扩展性。它期望以 YAML 或 JSON 格式提供部分 `Container`
规范。
为了通过创建临时容器来调试上面的 example-container，我们只需定义以下 YAML：

```yaml
# partial_container.yaml
env:
- name: REQUIRED_ENV_VAR
  value: value2
```
并执行：

```
kubectl debug example-pod -it --image=customapp --custom=partial_container.yaml
```
以下是一个同时修改多个字段（更改端口号、添加资源限制、修改环境变量）的 JSON 示例：

```json
{
"ports": [
{
"containerPort": 80
}
],
"resources": {
"limits": {
"cpu": "0.5",
"memory": "512Mi"
},
"requests": {
"cpu": "0.2",
"memory": "256Mi"
}
},
"env": [
{
"name": "REQUIRED_ENV_VAR",
"value": "value2"
}
]
}
```
## 约束
不受控制的可扩展性会损害可用性。因此，不允许对某些字段使用自定义分析，例如命令、镜像、生命周期、卷设备和容器名称。将来，如果需要，可以将更多字段添加到禁止列表中。

## 限制
`kubectl debug`
命令有 3 个方面：使用临时容器进行调试、Pod 复制和节点调试。这些方面的最大交集是 Pod
中的容器规范。
因此，自定义分析仅支持修改 `containers`
中定义的字段。这导致了一个限制，即如果用户需要修改 Pod 规范中的其他字段，则不支持。

## 致谢
特别感谢所有参与此功能的审阅者和评论者，从最初的概念到实际实现（按字母顺序排列）：

### EDITOR'S RESPONSE