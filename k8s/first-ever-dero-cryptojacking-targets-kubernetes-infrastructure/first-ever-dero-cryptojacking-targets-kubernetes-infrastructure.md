# 有史以来第一个针对 Kubernetes 基础设施的 Dero 币挖矿劫持

翻译自 [First-Ever Dero Cryptojacking Targets Kubernetes Infrastructure](https://thenewstack.io/first-ever-dero-cryptojacking-targets-kubernetes-infrastructure/) 。

CrowdStrike 发现了有史以来第一个针对 Kubernetes 的 Dero 币挖矿劫持行动。

![](https://cdn.thenewstack.io/media/2023/06/b26e26b3-kanchanara-gnwfl_nnzro-unsplash-e1686759198235-1024x681.jpg)

但是等等，还有更多！这个新的攻击活动之后有一个门罗币挖矿劫持攻击者！

领先的网络安全公司 [CrowdStrike](https://www.crowdstrike.com/?utm_content=inline-mention) 发现了有史以来第一次针对 Kubernetes 基础设施的 Dero 币挖矿劫持行动。Dero 是一种相对较新且注重隐私的加密货币，它使用有向无环图（DAG）技术，其创始人声称，提供完全匿名的交易。与常用的[门罗币](https://www.getmonero.org/)加密货币相比，这种匿名性和更高奖励的承诺相结合，使其对挖矿劫持者群体具有吸引力。

你看，2022 年的[加密货币崩盘](https://www.forbes.com/sites/billybambrough/2022/08/21/1-trillion-crypto-knife-edge-now-hinged-on-a-fed-bombshell-after-200-billion-bitcoin-ethereum-bnb-xrp-solana-cardano-and-dogecoin-price-crash/?sh=2edd9f34e2f8)使加密货币劫持者的金钱奖励减少了 50-90% 。这使得提供更大奖励的 Dero 对攻击者更具吸引力。

## 独立操作

讽刺的是，[CrowdStrike 还发现了一起单独的门罗币加密挖矿操作，它利用 Dero 活动作为跳板](https://www.crowdstrike.com/blog/crowdstrike-discovers-first-ever-dero-cryptojacking-campaign-targeting-kubernetes/)。这个门罗币活动利用 DaemonSets 和主机根挂载进行特权升级，将被感染的 Kubernetes 容器从挖掘 Dero 切换到挖掘门罗币。小偷之间没有荣誉可言！

在2023年2月，发现了 Dero 挖矿劫持活动。攻击者扫描并识别出具有身份验证设置为 "–anonymous-auth=true" 的暴露易受攻击的 Kubernetes 集群。通过部署名为 "proxy-api" 的 Kubernetes DaemonSet ，攻击者同时利用 Kubernetes 集群中所有节点的资源来运行加密挖矿操作。挖矿的成果被贡献给一个社区池，通过数字钱包在贡献者之间平均分配 Dero 币的奖励。

现在， Kubernetes 默认情况下不允许匿名访问 Kubernetes 控制平面的应用程序编程接口（API）。然而，延迟的安全默认决策和糟糕的配置使得 Kubernetes 集群不断面临攻击的风险。

此次操作中使用的 Docker 镜像托管在 Docker Hub 上，以便公众可以轻松访问。这个名为 "pauseyyf/pause:latest" 的镜像于 2023 年 1 月上传，并且在我撰写此文时已经有超过4,000次的下载量，这表明了该活动的范围以及可能部署的矿工实例数量。

一旦进入系统，攻击者会创建一个 DaemonSet 。攻击者将其创建在默认的 Kubernetes 命名空间 "kube-system" 下，并将其命名为 "proxy-api" ，以伪装自己的身份。此外，攻击者将 Pod 的 DNS 服务器设置为公共 IP（例如Google的8.8.8.8），并标记 "restartPolicy: Always" ，以防止任何节点上的 Pod 崩溃。简而言之，一旦部署成功，这是一个持久性的问题。

## 一切关于金钱

Dero 的攻击活动似乎完全是为了金钱。到目前为止，还没有任何尝试来破坏集群的运作或横向移动以进一步攻击其他资源。然而，CrowdStrike 在 2023 年 2 月份发现了一个修改后的门罗币攻击活动，该活动针对 Kubernetes 并取代了 Dero 的挖矿程序，改为挖掘门罗币。

修改后的门罗币攻击活动通过有意删除名为 “proxy-api” 的现有 DaemonSets 来实现。完成这一步骤后，门罗币攻击活动接管了整个集群，利用其所有资源进行门罗币挖矿。

Dero 和门罗币的加密挖矿活动都在竞争未被发现的 Kubernetes 攻击面。 CrowdStrike 声称其 [Falcon 平台](https://www.crowdstrike.com/falcon-platform/)具备行业领先的云原生应用保护平台（CNAPP）功能，可以保护组织免受复杂的入侵，包括挖矿劫持活动的影响。虽然我相信部署 Falcon 可能会有所帮助，但这次攻击强调了首先[安全设置 Kubernetes](https://thenewstack.io/best-practices-for-securely-setting-up-a-kubernetes-cluster/) 的必要性。

今年早些时候，Crowdstrike 发现了首次针对 [Kubernetes](https://kubernetes.io/) 基础设施的 [Dero](https://dero.io/) 加密挖矿活动。
