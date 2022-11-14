# 忍不了了，都是跟谁学的 ？

最近一段时间面试了一些 Kubernetes 初级工程师，发现了许多人都犯了一个类似的错误。


> 我：聊一下 Deployment 资源的作用？ 
> 应聘者：Deployment 是一个控制器......
> 我： 什么？


我实在忍不住了，就问了一个应聘者，这个 Deployment 是控制器的说法是从哪里来的？这个应聘者说是官方文档，我一时也不自信了，我确实好久没看这些基本概念了，是我一直记错了？

于是我查阅了官方文档中有关 [Deployment](https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/deployment/) 的部分：

>一个 Deployment 为 Pod 和 ReplicaSet 提供声明式的更新能力。
>
>你负责描述 Deployment 中的 目标状态，而 Deployment 控制器（Controller） 以受控速率更改实际状态， 使其变为期望状态。你可以定义 Deployment 以创建新的 ReplicaSet，或删除现有 Deployment， 并通过新的 Deployment 收养其资源。

根据上面的叙述中，显然 Deployment（资源）和 Deployment 控制器是两个概念，那为什么有好多面试者会混淆二者呢？于是我百度了一下 “Deployment 控制器”，发现了第一个[结果](https://blog.csdn.net/weixin_41755556/article/details/125634821)中有以下叙述：

> **deployment是一个控制器**，控制器里有pod的模板，控制器可以理解为一个机器人，我们作为管理员，需要做的就是告诉这个机器人，我们需要几个pod，机器人就会根据pod的模板创建几个pod，并且会实时监控这些pod，若某个pod挂掉了，那么机器人就会重新去创建这个pod来补齐，来维持环境里一定数量的pod

之后的搜索结果中，有一些的论述还算正常，但也有很多含糊不清。其实不只是 Deployment ，类似的问题有许多，背后的原因值得思考。我觉得初学者一定要注意学习方法，我这里列几条：

* 中文搜索的结果，尤其是百度搜索的结果要谨慎参考，质量属实太差了
* 最好找本书或者高质量的教程进行系统性的学习
* 尽可能看官方文档
* 有能力的话一定看英文资料，无论是网站还是书
* 要重视概念。大多数软件都会构建自己的一套概念，你理解了概念，以及概念之间的关系，剩下的就迎刃而解了。

希望对你有所帮助。



