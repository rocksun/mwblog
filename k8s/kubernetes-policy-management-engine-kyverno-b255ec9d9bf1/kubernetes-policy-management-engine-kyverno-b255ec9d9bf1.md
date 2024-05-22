
<!--
title: Kubernetes 策略管理引擎 — Kyverno
cover: https://miro.medium.com/v2/da:true/resize:fit:1200/0*Pf4-CjJCD3UnPwbO
-->

Kyverno 接收来自 kube-apiserver 的验证和修改准入 webhook HTTP 回调，并应用匹配的策略…

> 译自 [Kubernetes Policy Management Engine — Kyverno](https://aws.plainenglish.io/kubernetes-policy-management-engine-kyverno-b255ec9d9bf1)，作者 Keith。


## Kubernetes 策略管理引擎 — Kyverno

Kyverno 从 kube-apiserver 接收验证和修改准入 webhook HTTP 回调，并应用匹配的策略以返回执行准入策略或拒绝请求的结果。

[Griffin Wooldridge](https://unsplash.com/@dzngriffin?utm_source=medium&utm_medium=referral) 在 [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)