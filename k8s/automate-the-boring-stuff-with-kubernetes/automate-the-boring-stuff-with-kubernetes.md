<!-- 
# 使用Kubernetes自动化枯燥的工作
https://cdn.thenewstack.io/media/2023/11/89737a14-containers3-1024x456.jpg
 -->

你可以用Kubernetes来自动化工厂。你可以用它来运行城市灌溉系统。你可以依靠它。它一点也不枯燥。

译自 [Automate the Boring Stuff with Kubernetes](https://thenewstack.io/automate-the-boring-stuff-with-kubernetes/) 。

在科技行业，我发现当人们说某些事情在软件上是不可能的时，他们往往的意思是它很枯燥。当然，在你的工作中也可能遇到一些基础和复杂的计算机科学问题。但一般来说，我们经常会避免枯燥的工作。

问题是，企业软件中有大量枯燥的工作。从连接API，到重构旧应用，再到保持事物正常运行所需的日常管理任务。运行旧东西不如建造新东西有趣。

一段时间以来，[Kubernetes 一直是一个激动人心的开源生态系统](https://thenewstack.io/kubernetes/)，其中创新爆发增长。然而，即使有着所有这些激动人心的实验，也没有企业仅仅为了运行 Kubernetes 而去运行它。他们使用它是因为它帮助他们自动化枯燥的任务。

我们所有人参与这个社区的共同目标是优化、扩展和共享一个应用平台。Kubernetes 在此方面表现卓越，它帮助终端用户支持和[自动化大规模的应用运营](https://red.ht/3ESinRq)。

应用才是最重要的。在它们下面的一切，用一个更好的术语来说，都是枯燥的。虽然实施、位置和支持非常重要，但是它们不应该是你的应用开发者最关心的事情。他们的时间是你最宝贵的资源，你[最不想让他们担心的](https://thenewstack.io/measure-developer-joy-not-developer-productivity-atlassian-says/)就是枯燥。

你的开发者应该专注于创新。但是当构建无法完成，测试环境与生产环境不同，或者他们无法在三周内在其区域获得一个新的PostgreSQL安装时，他们就无法专注于创新。

## 必须自动化

开发者之下的一切都必须自动化。你的开发者正在使用架构师十年前设想的那些服务化的构建块来进行构建。但是如果他们无法在测试环境中访问这些构建块，他们就无法用它们构建新的应用程序。如果这个过程没有通过你的平台团队使用 Kubernetes Operator 来提供护栏进行更安全的自动化，他们尤其无法启动新的数据库实例。

现在，由于十多年来 Kubernetes 社区的成长和发展，基础设施已经牢固可靠，现在是时候把重点放在应用上了。[Kubernetes](https://roadmap.sh/kubernetes) 不再只是一个容器平台；它是一个应用平台。配备了正确的一套装备，它可以成为一个强大的自动化平台，以实现更快的开发和更安全的软件供应链。

再加上像 [Ansible](https://www.ansible.com/) 这样的 IT 自动化、[Quarkus](https://quarkus.io/) 这样的云原生 Java，甚至内置的 Kubernetes 虚拟机支持，没有理由让传统应用继续手动驱动，或者更糟，不去触碰它们。最好的是，将较旧的 [Java 工作负载](https://thenewstack.io/rethinking-java-scheduled-tasks-in-kubernetes/)迁移到新的应用平台上，可以在这些旧项目上培育创新。

[大规模的自动化](https://content.cloud.redhat.com/blog/red-hat-openshift-4.14-is-now-available)使开发者能够专注于速度进行代码开发，而不是其他所有的阻碍。但这意味着需要适当的护栏，以防他们做出可能具有破坏性的事情。[Argo CD](https://argoproj.github.io/cd/) 实质上是对集群强制执行一个 git 仓库，这意味着您的生产环境有一个单一的事实来源。并且只能通过适当的流程进行更改。所有这些都旨在实现自动化。

随后的成果可以由 [Quay](https://quay.io/) 和 [Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/resources/advanced-cluster-security-for-kubernetes-datasheet) 存储和保护，同样，以自动化的方式。所有这些自动化系统都有一个额外的好处: 提供任何软件系统所必需的一致可重复性。

## 一致性

因为我们一起努力扩展了 Kubernetes 的功能，所以应用平台困题的所有这些碎片可以组合在一起，为你的管理员和开发者提供部署任何他们需要的东西的单一途径。部署的目的地应该基本上无关紧要。测试环境和生产环境在部署工件上可以完全相同，这可以消除代码库发生散步时可能出现的痛苦。

所有这些自动化和蓄意地构建一个开源应用平台不是因为世界各地的人决定投入他们的大部分生命来专注基础设施代码才做的。它是因为我们都共享同样的问题而构建的。世界上没有任何企业会仅仅因为他们很了解 Kubernetes 本身而打败竞争对手。

[赢家](https://cloud.redhat.com/blog/openshift-is-an-application-platform)将是那些能够更快地创新并更快地用新产品进入市场的企业，这是由专注于业务问题而不是开发者问题的软件开发者推动的。

就像一队卡车或制造厂一样，最终目标不是卡车，也不是传送带。最终目标是装在卡车里的东西或从制造厂里出来的东西。你可以调整工厂机器的旋钮，或者调整卡车发动机，但最终，如果你可以24/7运行这些东西，你也可以24/7产生价值。

如今，你可以用 Kubernetes 来[自动化工厂](https://www.redhat.com/en/about/press-releases/siemens-accelerates-innovation-factory-edge-openshift)。你可以用它来[运行城市管网系统](https://thenewstack.io/gothenburg-sweden-used-open-source-iot-to-drastically-cut-water-waste/)。你可以[依靠它](https://thenewstack.io/ing-on-building-a-cloud-native-bank/)。虽然我们还未能真正用它来驾驶卡车，但在 Kubernetes 内已经模拟了[数百万虚拟驾驶员](https://www.redhat.com/en/resources/volkswagen-group-case-study)。你知道吗，你可以用它来运行邮轮？

让我们与为企业业务打造了最佳应用平台基础的开源社区一起驶向没有枯燥的未来。