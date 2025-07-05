如果你和我一样，你依赖于大量的系统和服务，即使在你的家庭 [局域网](https://thenewstack.io/git-set-up-a-local-repository-accessible-by-lan/) 内也是如此。因为我在家工作，所以这种情况被放大了，以至于我需要某些应用程序可用，但这些应用程序并非由第三方托管，这是为了灵活性、易用性、可靠性和安全性。

谢天谢地，[Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) 让部署这些应用和服务变得相当容易；否则，我最终将不得不首先部署一系列 [虚拟机 (VM)](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/)，保持它们的运行，并担心如何有效地升级/管理它们。

是的，Docker 让整个过程变得更容易。更好的是，我可以在几秒钟内启动这些应用和服务，而不必走传统路线，传统路线通常需要更长的时间来部署。

但是，我依赖哪些应用和服务来保持我的局域网的生产力呢？惊喜，惊喜：我有一个列表，如下所示。

## Nextcloud

[Nextcloud](https://nextcloud.com/athome/) 实际上已经成为我家庭局域网的 [Google](https://cloud.google.com/?utm_content=inline+mention) 服务。当我开始担心 Google 会使用我在 Drive 中的文档来训练其 AI 时，我开始认真地在我的局域网上使用 Nextcloud。在那个想法闪过我的大脑突触之后，我提取了这些文档并将它们移动到我家网络上的 Nextcloud 部署中。问题解决了。

但 Nextcloud 不仅仅是一个文档服务器；它远不止于此。Nextcloud 是一整套应用程序，几乎可以满足您家庭办公室的每一个需求。它有音频/视频聊天、日历、电子邮件、白板、AI 助手和代理 AI、文件共享、协作、文件访问控制、版本控制、机器学习 (ML)、大量的集成、监控/审计等等。

甚至还有一个应用商店，您可以在其中扩展功能集以满足您的确切需求。

Nextcloud 可以免费使用，并且可以使用 Docker 从 [Docker Hub](https://thenewstack.io/revised-docker-hub-policies-unlimited-pulls-for-all-paying-customers/) 进行部署，就像这样简单：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d -p 8080:80 nextcloud |

## Grocy

如果您需要管理家里的物品，[Grocy](https://grocy.info/) 是不二之选。正如您可能从名称中猜到的那样，Grocy 主要关注食品杂货和膳食计划。如果您像我一样忙碌，那么计划膳食并不总是最容易的事情，但这款方便的 Docker 应用程序使它变得容易得多。您不仅可以跟踪厨房或储藏室中的物品，还可以按位置（例如，冰箱、冰柜、储藏室、车库、地下室等）对它们进行分类，甚至可以跟踪食谱。最重要的是，Grocy 甚至允许您跟踪需要在房子周围处理的家务。您甚至可以跟踪电池、充电周期和保修，这样您就可以免去猜测何时更换烟雾探测器中的电池。

Grocy 可以使用 docker-compose 和 Dockerfile 进行部署，如下所示：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | --- |
|  |  |
|  | services: |
|  | grocy: |
|  | image: lscr.io/linuxserver/grocy:latest |
|  | container\_name: grocy |
|  | environment: |
|  | - PUID=1000 |
|  | - PGID=1000 |
|  | - TZ=Etc/UTC |
|  | volumes: |
|  | - /path/to/grocy/config:/config |
|  | ports: |
|  | - 9283:80 |
|  | restart: unless-stopped |

## Tududi

如果您想要一个可以从网络上的任何机器访问的任务管理器，请考虑 [Tududi](https://tududi.com/)。Tududi 可以通过精心设计、用户友好的 UI 帮助管理这些任务甚至项目。Tududi 功能列表包括评论、截止日期、项目名称、状态、优先级、任务和项目的分层结构、智能重复任务、区域、注释、标签和 Telegram 集成。

通过 Telegram 集成，您可以直接通过 Telegram 消息创建任务，接收每日任务摘要，并快速捕捉想法和待办事项。您还可以获得智能的父子关系，这样当重复任务生成新实例时，每个生成的任务都保持与父任务的链接，这些任务显示为重复任务实例（具有继承的设置），用户可以从子任务编辑父重复模式，并且对父设置的更改会影响系列中的所有未来实例。

可以使用以下命令从 Docker Hub 安装 Tududi：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker pull chrisvel/tududi:latest |

## Bitwarden

[Bitwarden](https://bitwarden.com/) 是市场上最好的密码管理器之一。该应用/服务拥有所有密码管理器中最好的功能列表之一，并使用行业标准加密。即便如此，我还是希望将某些高度敏感的信息保留在我的家庭局域网上。为此，我使用了 Bitwarden 服务器，该服务器可以通过 Docker 轻松部署。Bitwarden 服务器的行为几乎与标准服务相同，只是它是私有托管的，因此不必在您的局域网之外可用。考虑到这一点，您可以存储高度敏感的信息，并且（只要您的网络安全），您就不必担心有人偶然发现您的保险库或其中包含的项目。

可以使用以下命令使用 Docker 部署 Bitwarden：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker pull ghcr.io/bitwarden/self-host:sha256-6f575e9af6ba3c4632f32497b5c73696e92e8b077f3083e4d753c2c14c70bbe6.sig |

## Portainer

如果您想借助功能强大的基于 Web 的 GUI 工具来管理所有容器，那么 [Portainer](https://www.portainer.io/) 很难被击败。Portainer 允许您查看所有正在运行的容器、查看所有容器日志、快速访问容器控制台、使用简单的表单将代码部署到容器中，并将您的 YAML 转换为自定义模板以便轻松重用。哦，您可以部署、停止、运行和删除容器。事实上，您几乎可以使用 Portainer 做任何事情。

Portainer 被认为是世界上最流行的容器管理系统之一，并且确实需要做一些工作才能启动和运行。您可以查看官方的 [Portainer 文档](https://docs.portainer.io) 并快速了解该过程。

虽然这是我在局域网上经常使用的容器的简短列表，但总有更多的空间。请务必查看 Docker Hub，看看是否有其他应用/服务可以让您受益。