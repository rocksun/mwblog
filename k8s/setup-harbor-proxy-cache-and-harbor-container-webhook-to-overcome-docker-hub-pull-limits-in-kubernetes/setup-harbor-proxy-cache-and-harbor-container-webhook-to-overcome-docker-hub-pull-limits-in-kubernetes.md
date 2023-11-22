<!--
title: 通过Harbor解决Docker Hub拉取速率限制问题
full: 在Kubernetes中设置Harbor代理缓存和Harbor容器Webhook以解决Docker Hub拉取速率限制问题
cover: https://i0.wp.com/www.viktorious.nl/wp-content/uploads/2023/11/harbor-proxy-cache-02.png
-->

在Kubernetes中设置Harbor代理缓存和Harbor容器Webhook以解决Docker Hub拉取速率限制问题。

译自 [Setup Harbor Proxy Cache and Harbor Container Webhook to overcome Docker Hub Pull Rate Limits in Kubernetes](https://www.viktorious.nl/2023/11/21/setup-harbor-proxy-cache-and-harbor-container-webhook-to-overcome-docker-hub-pull-limits-in-kubernetes/) 。

在您的 Kubernetes 集群中，您可能会遇到以下问题:

```bash
NAME READY STATUS RESTARTS AGE
pod01 1/2 ImagePullBackOff 0 24s
```

"ImagePullBackOff" 错误是 Kubernetes 中常见的错误，表明 pod 中的某个容器无法从注册中心检索到必要的镜像。为了进一步了解问题的原因，您可以描述该 pod:  

```bash
kubectl describe pod01
```

该命令会提供详细的错误分析。在示例输出中，您可能会看到:

```
Error: ImagePullBackOff
Normal Pulling 15s (x2 over 38s) kubelet Pulling image "<SOME-IMAGE>"
Warning Failed 10s (x2 over 32s) kubelet Failed to pull image "<SOME-IMAGE>": rpc error: code = Unknown desc = failed to pull and unpack image "docker.io/<SOME-IMAGE>": failed to copy: httpReadSeeker: failed open: unexpected status code https://registry-1.docker.io/v2/<SOME-IMAGE-WITH-SOME-ID>: 429 Too Many Requests - Server message: toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
```

在这种情况下，您正面临[Docker Hub对匿名帐户的拉取速率限制](https://docs.docker.com/docker-hub/download-rate-limit/)。 该限制意味着您在特定时间范围内超过了允许的拉取次数。

解决此问题的[方法很多](https://medium.com/rossum/how-to-overcome-docker-hub-pull-limits-in-a-kubernetes-cluster-382f317accc1)。在本博客文章中，我们将探索一个解决方案，通过使用 Harbor 为 Docker Hub 设置代理缓存。 此外，我们将指导您安装和配置 [Harbor 容器Webhook](https://github.com/indeedeng-alpha/harbor-container-webhook)。 这个 webhook 将自动将任何 Docker Hub 镜像拉取请求重定向到您在 Harbor 注册表中配置的代理缓存。

尽管存在其他替代方案，但这种方法的优点在于其简单性——无需修改任何YAML文件。  

此设置的先决条件包括:

* 一个Harbor registry实例
* 在您的 Kubernetes 集群上安装[Harbor容器Webhook](https://github.com/indeedeng-alpha/harbor-container-webhook)
    
## 在Harbor上设置代理缓存

要在 Harbor 上设置代理缓存，可以遵循[此过程](https://goharbor.io/docs/2.1.0/administration/configure-proxy-cache/)。

第一步是在 Harbor 实例上配置注册表端点，该选项可在 Administration->Registries 下提供。

![](https://i0.wp.com/www.viktorious.nl/wp-content/uploads/2023/11/harbor-proxy-cache-01.png?w=578&ssl=1)

使用测试连接验证连接。 访问秘密设置在[Docker Hub帐户设置](https://hub.docker.com/settings/security)页面上。

下一步是在Harbor中配置一个新的项目，该项目链接到新的Registry端点:

![](https://i0.wp.com/www.viktorious.nl/wp-content/uploads/2023/11/harbor-proxy-cache-02.png?w=576&ssl=1)

现在您可以测试代理缓存是否正常工作:

```bash
docker pull <YOUR-HARBOR-URL>/docker_hub/goharbor/harbor-core:dev
```

## 安装和配置Harbor容器Webhook

现在是时候安装和配置Harbor容器Webhook了。首先为webhook创建一个新的命名空间，并切换到该命名空间:

```bash
kubectl create ns harbor-containerwebhook
kubectl config set-context --current --namespace=harbor-container-webhook
```

将项目克隆到本地系统:

```bash
git clone https://github.com/indeedeng-alpha/harbor-container-webhook/
```

切换到/deploy/charts/harbor-container-webhook文件夹，配置helmchart的values.yaml文件以反映您的配置。我对values.yaml文件的更改是:

```bash
imagePullSecrets:
  - name: regcred
```

注意：webhook最初使用的镜像也来自Docker Hub。如果您已经面临Docker拉取速率限制，您可能需要创建一个包含Docker Hub登录凭据的Secret，并将该Secret附加到values.yaml文件中。

```  
kubectl create secret docker-registry regcred --docker-server=https://index.docker.io/v1/ --docker-username=<DOCKERHUB-ID> --docker-password=<DOCKERHUB-TOKEN> --docker-email=<DOKERHUB-EMAIL>
```  

在harbor-container-webhook命名空间中创建此Secret。  

现在配置values.yaml文件的其余部分。  

```yaml
## configures the webhook rules, which are evaluated for each image in a pod
rules:
  - name: 'docker.io rewrite rule'
    # image refs must match at least one of the rules, and not match any excludes
    matches:
      - '^docker.io'
#    excludes:
#      # for example, exclude ubuntu from harbor's proxy cache
#      - '^docker.io/(library/)?ubuntu:.*$'
    replace: '<HARBOR-URL>/docker_hub'
    checkUpstream: true
#  - name: 'docker.io ubuntu rewrite rule'
#    # image refs must match at least one of the rules, and not match any excludes
#    matches:
#      - '^docker.io/(library/)?ubuntu:.*$'
#    replace: 'harbor.example.com/ubuntu-proxy'
#    checkUpstream: true # tests if the manifest for the rewritten image exists
```

现在安装webhook:

```
helm install harbor-container-webhook ./
```

就这么简单！您的Docker Hub镜像拉取请求现已被重定向到Harbor缓存代理，不会再面临速率限制问题！希望这篇文章对您有帮助。
