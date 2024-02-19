<!--
title: Flox助Nix进军企业
cover: https://cdn.thenewstack.io/media/2024/02/02aca081-flox-1024x684.jpg
-->

Nix提供应用部署的跨平台可复制性，可作为Docker的替代，而Flox将为Nix提供必要的管理、安全与协作等功能。

> 译自 [Flox Readies Nix for the Enterprise](https://thenewstack.io/flox-gears-up-nix-for-the-enterprise/)，作者 Joab Jackson 是The New Stack的高级编辑，负责报道云原生计算和系统运维。他报道IT基础设施和开发25年以上，包括在IDG和Government Computer News工作。在此之前，他是一名自由作家，为《连线》杂志、ITworld.com和其他出版物撰写文章。欢迎在Twitter上关注他@Joab_Jackson。

流言说[Nix](https://nixos.org/)是一个迷人的技术——一个Linux操作系统和包管理器的杂交——但[对于商业使用来说太笨重了](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/)。

现在，一家名为[Flox](https://flox.dev/about)的创业公司正在努力驳斥这种观念，并即将推出Nix的商业化抛光版本，作为Docker的有竞争力的替代品。

“这是一种全新的软件构建方法，”Flox的营销和开发者关系负责人[Ross Turk](https://www.linkedin.com/in/rossturk/)在接受TNS采访时表示。

投资者包括NEA、Hetz Ventures和Addition Ventures。还有天使投资者GitHub CEO Thomas Dohmke、[Snyk](https://snyk.io/?utm_content=inline-mention)创始人[Guy Podjarny](https://thenewstack.io/entrepreneurship-for-engineers-4-lessons-in-raising-revenue-startups/)和前[Docker](https://www.docker.com/?utm_content=inline-mention)副总裁、现任苏富比CTO [James Turnbull](https://thenewstack.io/qa-james-turnbull-art-monitoring-age-microservices/)也纷纷竞相投资。 

## Nix是什么?

Flox起源于全球投资公司[D.E. Shaw集团](https://www.deshaw.com/)的一个项目。自然，这家金融公司对一致性有着强大的计算需求。考虑到公司被审计的次数，它所有关乎可复制性。

“他们需要一些东西，即使他们不得不从公开来源重新创建环境，也可以让他们可复制，这是一件非常、非常难做到的事情，”Turk说。

这就是为什么Nix引起了该公司的注意。

[NixOS于2004年作为一个研究项目引入](https://edolstra.github.io/pubs/nspfssd-lisa2004-final.pdf)，它是一个使用自己的打包系统Nix来构建自身和支持其他Linux应用程序的Linux发行版，使用[声明式模型](https://thenewstack.io/gitops-kubernetes-devops-iteration-focused-declarative-infrastructure/)、函数构建语言和密码散列来计算组件实例的唯一路径。

“它产生可靠、可复制、可移植的软件，”Turk解释道。

![缩放](https://cdn.thenewstack.io/media/2024/02/7e62810c-flox-01-1024x496.jpg)

*Flox提供*

这种方法已经证明非常受欢迎。

在其年度[Octoverse报告](https://thenewstack.io/add-it-up-takeaways-from-githubs-octoverse-report/)中，GitHub指出，在过去两年中，[NixOS/nixpkgs](https://github.com/nixos/nixpkgs)在开源项目贡献者数量方面[排名第一](https://github.blog/2023-11-08-the-state-of-open-source-and-ai/)。

[云原生计算基金会](https://cncf.io/?utm_content=inline-mention)发现，无论如何，[在过去一年中](https://docs.google.com/spreadsheets/d/1HO6ZO7T3noU2CfafsmyCHmsfURs7Ah01Wrs2tcyBEs0/edit#gid=134798507)，Nix的提交次数(57,941)比Kubernetes本身(42,680)还要多，尽管Kubernetes的贡献者(3,662)比Nix(3,087)多一些。

总的来说，就贡献者数量而言，Nix属于所有开源项目的前五名，仅次于[Linux](https://thenewstack.io/how-meta-patches-linux-at-hyperscale/)、[React](https://thenewstack.io/the-pros-and-cons-of-using-react-today/)、[Kubernetes](https://thenewstack.io/hpc-kubernetes-ai-training-on-3500-gpus/)和[Pytorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/)。

## D.E. Shaw如何修复Nix

DE Shaw很快发现的问题是“Nix对企业来说非常非常难以采用”，Turk承认。

Nix复杂且多层。Turk回忆一个工程师向他展示了一些Nix配置语言的代码，指着一行说这里是魔法发生的地方。Turk回忆看着这行仍然困惑。“我就像，怎么会有人知道呢?”

开玩笑地，Turk解释说“Nix适用于那些想在叉子上先排列豌豆然后再卷进嘴里的人。” 意思是，它适用于采取“要么全要么无”方法并在承诺运行软件之前计划每一个细节的系统管理员。

这对企业采用来说可能比较困难。

由于Nix是一个如此去中心化的社区，工具开发一直执行得不一致。在共享、安全、审计和协作方面，辅助功能仍然很少。

> Nix是一个包管理器，但存在于用户空间中。

因此，D.E. Shaw进行了工作，使Nix对管理员更加友好，将其包装在基本的包语义中。因此，Flox诞生了。所以管理员不需要编写代码或“导出”，可以简单地从单个存储库安装私有包，这基本上充当内部应用商店。

“所以商店里的每个人都获得相同的软件包集合。他们不会从Debian获取。他们不会从[Red Hat](https://www.openshift.com/try?utm_content=inline-mention)获取。他们从Flox获取，”Turk说。

采用这种方法，企业可以集中推送更新、缓存一切，并控制开发人员部署的软件。

## Flox的工作原理

它从命令行界面开始。您可以在任何版本的Linux上安装CLI，它会安装Nix。有了CLI，您就可以安装和激活包，创建环境，甚至分层环境(Docker无法做到这一点)。还有一个交换平台，用户可以轻松共享环境的界面。

![缩放](https://cdn.thenewstack.io/media/2024/02/63165b1f-flox-02-1024x563.jpg)

3月，CLI和交换平台将准备就绪，Flox已经建立了原型，并正在构建Nix商业化所需的其他主要组件。

除了命令行界面，Nix还创建了一个目录。Nix社区已经为该平台生成了[80,000个程序包](https://search.nixos.org/packages)——今天可用的大多数面向基础设施的开源软件的专门为Nix定制的版本。Flox目录将重新发布这些程序包。它还将为企业提供一个渠道来存储自己的私有程序包。

第二个新组件将是一个工厂，或在线中心，它将执行和自动化新的环境的构建。

“比如，我在我的Mac上创建了一个Flox环境，并将其推送到Flox中心。Flox中心将在后台为Linux构建该环境，”Turk说，“工厂正在进行主动构建，因此任何时候任何人推送环境，它都会为所有其他不同的目标重新构建它。”

最后一个组件是DE Shaw开发的管理界面，它使管理员能够执行舰队升级，并获取有关当前运行的所有环境的信息。

## 谁会运行Flox以及如何收费?

最初的受众将是任何在处理多个工作环境的人，如软件开发人员、AI工程师或数据科学家，他们可能需要处理多个[Jupyter Notebook](https://thenewstack.io/usenix-jupyter-notebooks-could-help-sres-better-sleuth-incidents/)或其他类型的工作台，Flox产品负责人[Graham Hudgins](https://www.linkedin.com/in/graham-hudgins/)指出。

Flox将使他们能够在几步之内启动环境，或与同事共享环境，即使您使用Mac，而其他人使用Windows。

它还将允许企业在少数项目上测试Nix。

Flox将遵循开放核心模型，针对云服务收取费用。目前还没有计划开源这些组件。

目录将包括用于存储私有程序包的付费选项。对于工厂，公司将根据构建时间收费。管理器也将作为付费服务提供。还将提供高级功能，比如用于生成软件清单(SBOM)的支持。

最初，公司希望以软件即服务(SaaS)模式在主要云提供商上提供这些服务，并最终也准备好托管的自我托管版本。

![缩放](https://cdn.thenewstack.io/media/2024/02/16e32502-flox-emp-ss.jpg)

*Flox提供*

## Flox与Docker的区别

与Docker相比，Nix提供了更多的声明式环境;相比[构建Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，它需要更少的指令来合并所需的软件程序包。但是，用户更局限于可以使用的程序包——仅限于存储库中的程序包。

与容器不同，Flox组件可以轻松地与主机上的应用程序通信。主机上[VSCode的副本](https://thenewstack.io/gitpod-openvscode-server-brings-visual-studio-code-to-the-browser/)可以与Flox环境交互。

“它不是隔离的，”Turk说。 “使用容器时，您通常必须启动容器，然后花5分钟时间弄清楚如何在其中打一个洞，以便让工具进入其中。”

使用Flox，您的工作空间可以在一个环境中，podman的副本可以在另一个环境中分层，项目数据可以在另一个环境中再分层——所有这些都在同一台机器上交互。

Nix允许你堆叠设置和分层设置，”Hudgins解释说。因此，“通过这种方式构建镜像，您可以获得更多精简的镜像、更好的共享和效率。”
