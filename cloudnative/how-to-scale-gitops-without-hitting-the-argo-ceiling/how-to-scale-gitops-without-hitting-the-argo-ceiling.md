
<!--
title: GitOps规模化：突破Argo天花板
cover: https://cdn.thenewstack.io/media/2026/01/ade4c570-scale-gitops-argo-ceiling.jpg
summary: GitOps扩展面临“Argo天花板”挑战，管理复杂。解决方案是采用GitOps控制平面。1月20日网络研讨会分享隔离、自动化治理等扩展技巧。
-->

GitOps扩展面临“Argo天花板”挑战，管理复杂。解决方案是采用GitOps控制平面。1月20日网络研讨会分享隔离、自动化治理等扩展技巧。

> 译自：[How To Scale GitOps Without Hitting the 'Argo Ceiling'](https://thenewstack.io/how-to-scale-gitops-without-hitting-the-argo-ceiling/)
> 
> 作者：Vicki Walker

GitOps 常常会成为其自身成功的受害者。一个集群和一个 Argo CD 实例很快就会扩展到 50 个集群和 50 个 Argo 实例，它们通过胶水代码和自定义脚本连接在一起。

最初使 [Argo CD](https://thenewstack.io/make-your-kubernetes-apps-self-heal-with-argo-cd-and-gitops/) 安全的隔离性，却导致了糟糕的可见性和失控的治理。中断的流程要求您的团队维护自定义仪表板和脆弱的编排脚本，浪费了宝贵的工程时间，而这些时间本可以用于更重要的项目。

## 什么是“Argo 天花板”？

Harness 的 DevOps 爱好者 Eric Minick 和首席开发者倡导者 Dewan Ahmed 表示，这个痛点被称为“Argo 天花板”。提高这个“天花板”的关键是采用一个 GitOps 控制平面，它可以在不撕毁和替换开发者熟悉和喜爱的工具的情况下，实现集中管理。

[采用 GitOps](https://thenewstack.io/4-core-principles-of-gitops/) 不应阻碍您的 [CI/CD 编排](https://thenewstack.io/introduction-to-ci-cd/)。GitOps 应该提供更友好的开发者体验和以 Kubernetes 为中心的使用感受。

如果您正在大量编写脚本来管理 GitOps 环境，请于 1 月 20 日太平洋时间上午 8:30 | 东部时间上午 11:30 加入我们，参加一场特别的在线活动：[避免 Argo 天花板：在不达到极限的情况下扩展 GitOps](https://thenewstack.io/webinar/avoiding-the-argo-ceiling-scaling-gitops-without-maxing-out/)。

在此免费网络研讨会期间，Minick、Ahmed 和 TNS 主持人 Chris Pirillo 将深入探讨团队为何会触及 Argo 天花板，以及如何实施 GitOps 控制平面来统一您的资产。

## 立即注册此免费网络研讨会！

如果您无法实时加入我们，也请务必注册，我们将在网络研讨会结束后向您发送录音。

## 

## 您将学到哪些关于扩展 GitOps 的知识

通过参加这次特别的在线活动，您将获得最佳实践、真实案例和可操作的技巧，其中包括：

### 利用隔离而非碎片化

出于安全考虑，您应该运行多个 Argo 实例，但您不应该单独管理它们。控制平面为您提供了隔离的安全性以及集中化的可见性。

### 停止为编排编写“胶水代码”

如果您正在编写脚本以在同步之前触发测试，那么您正在构建一个平台，而不是交付功能。编排应该是一个原生功能，而不是维护负担。

### 实施零配置治理

在大规模部署中，手动基于角色的访问控制（RBAC）会失败。企业治理意味着策略嵌入到管道中并自动执行，从而消除了“安全与速度”的权衡。