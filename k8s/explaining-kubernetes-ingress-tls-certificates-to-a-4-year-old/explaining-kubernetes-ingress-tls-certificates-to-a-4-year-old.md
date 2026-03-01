<!--
title: 如何给4岁孩子讲明白 Kubernetes Ingress TLS 证书
cover: https://oberbean.com/content/images/size/w1200/2026/02/Explaining-Kubernetes-Ingress-TLS-Certificates-to-a-4-year-old-monkey.png
summary: 本文用生动的水族馆和腕带类比，解释了Kubernetes Ingress TLS证书的原理和配置步骤，强调其重要性并提供管理建议。
-->

本文用生动的水族馆和腕带类比，解释了Kubernetes Ingress TLS证书的原理和配置步骤，强调其重要性并提供管理建议。

> 译自：[Explaining Kubernetes Ingress TLS Certificates to a 4-Year-Old](https://oberbean.com/explaining-kubernetes-ingress-tls-certificates-to-a-4-year-old/)
> 
> 作者：Lucas Borza

那是一个在家工作的普通日子。我坐在办公桌前，敲着键盘，这时我听到了儿子稚嫩的声音：“爸爸……你在做什么？”我看着他，说：“我正在进行一项更改。”他盯着我，显然一个字也没听懂。“我正在让计算机相互信任，这样它们就能安全地交流。”沉默。凝视的目光变得更强烈了……

我开始琢磨，到底该怎么向一个4岁的孩子解释Kubernetes Ingress TLS证书呢？系好安全带。

“想象一下你要去水族馆，那里有鱼、鲨鱼和乌龟在等你。在你能进去之前，你需要一个特殊的腕带。有一天，那个腕带会变旧，检查腕带的门卫会说：‘对不起，你*不能*进来……这个腕带太旧了。’腕带不会永远有效。你需要拿到一个新的腕带才能进去。”

Kubernetes庞大而复杂，我无法在此一一涵盖，但我可以教你如何为你的Ingress提供TLS证书，让你的应用程序被信任和安全。

## 拆解概念

* Kubernetes - 运行你应用程序的平台 / 水族馆
* Secret - 存储你的应用程序所需重要事物的安全地方 / 工作人员的腕带盒
* Ingress - 允许外部流量到达你的应用程序的网关 / 主大厅
* TLS - 加密流量并确保其安全的系统 / 门卫
* Certificates - 证明身份的数字密钥 / 腕带

### 步骤 1 - 弄到一条新腕带，呃……我的意思是证书。

在任何人进入水族馆之前，你需要一个新的腕带。这意味着一个新的TLS证书。我通常会使用完整的PEM文件，这样你就能拥有完整的证书链并分离出密钥。

### 步骤 2 - 在Kubernetes中添加证书

现在是时候通知水族馆工作人员会有新的腕带了。在Kubernetes中，这意味着创建一个Secret来存储你的证书和密钥。把它想象成一个盒子，所有新腕带都存放在里面，直到门卫需要知道它们当天是什么颜色。

```
apiVersion: v1
kind: Secret
metadata:
  name: aquarium-tls
  namespace: aquarium
type: kubernetes.io/tls
data:
  tls.crt: <new-aquarium-certificate>
  tls.key: <new-aquarium-key>
```

### 步骤 3 - 将证书应用于Ingress

最后，我们告诉门卫检查新的彩色腕带。在Kubernetes中，这意味着将Ingress指向我们创建的Secret。一旦Ingress知道新的证书，所有访客都可以进入水族馆了！

```
spec:
  tls:
  - hosts:
    - aquarium.com
    secretName: aquarium-tls
```

如果没有可信任的腕带，访客会被拒之门外，浏览器会发出警告，鱼儿看起来悲伤而孤独。但一旦我们分发了新的腕带，大门就打开了，访客们在水族馆里愉快地游览，每个人都享受了一次安全可靠的参观。

## 想要一些建议吗？

1. 在证书过期前进行检查，并设置监控以便在到期时通知你。
2. 自动化很有帮助。使用cert-manager自动颁发和续订证书。
3. Secret很重要。仔细检查名称、命名空间和编码。
4. 测试所有内容。确保Ingress指向正确的Secret，并且应用程序或服务显示为受信任。
5. TLS并非可选项。不要偷懒，将其应用于所有地方！