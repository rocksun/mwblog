<!--
title: Docker容器：助力小型企业腾飞的秘密武器
cover: https://cdn.thenewstack.io/media/2025/09/0bda5716-getty-images-yal9i4bk3be-unsplash.jpg
summary: 推荐了五个适合小型企业的 Docker 容器应用：Nextcloud（云服务），Invoice Ninja（发票管理），Bitwarden（密码管理），Homebox（物品追踪），Outline（知识库）。提供了部署命令和相关文档链接。
-->

推荐了五个适合小型企业的 Docker 容器应用：Nextcloud（云服务），Invoice Ninja（发票管理），Bitwarden（密码管理），Homebox（物品追踪），Outline（知识库）。提供了部署命令和相关文档链接。

> 译自：[Docker Containers That Could Be Essential for Your Small Business](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/)
> 
> 作者：Jack Wallen

一般来说，[容器](https://thenewstack.io/introduction-to-containers/)让事情变得简单。从部署、管理、备份等等，这项技术已经成为许多用户类型不可估量的财富。如果你经营一家小企业，并且厌倦了为第三方服务支付高昂的成本，你可能想考虑选择使用容器来提供那些不需要专有、被供应商锁定的工具的基本服务。

如果你前往 [Docker Hub](https://hub.docker.com/)，你会发现似乎有无穷无尽的 [容器镜像](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) 供你拉取、配置和部署。但如果你问我你应该为你的企业使用哪些容器，我可以很容易地将列表缩减到少数几个。

但是，请理解，每个企业都是不同的，你的企业可能有本列表中未满足的特殊要求。没关系，因为你可以回到 Docker Hub 并准确地找到你想要的东西。

让我告诉你我认为完全适合[小型企业](https://thenewstack.io/linux-zentyal-is-the-small-business-server-you-may-need/)的容器。

## 1. Nextcloud

Nextcloud之所以名列榜首，是有原因的；它太棒了。这种云解决方案使你和/或你的企业有可能摆脱 [Google](https://cloud.google.com/?utm_content=inline+mention) Workspace、[Microsoft 365](https://thenewstack.io/saas-rootkit-attack-to-create-hidden-rules-in-office-365/) 和 Apple iCloud。 Nextcloud 包含许多内置功能，例如存储、日历、文档、对话、电子邮件、看板等等。如果你发现 Nextcloud 没有包含你需要的功能，你可以筛选并安装大量应用。 Nextcloud 简直就是自托管云服务的实际标准。我已经使用 Nextcloud 多年了，并且一直发现它不仅非常有用，而且可靠且安全。对于 Docker 目的，我建议使用 [Nextcloud AIO 解决方案](https://hub.docker.com/r/nextcloud/all-in-one)，因为它在一个方便的容器镜像中包含了你所需要的所有内容。

你可以使用如下命令部署 Nextcloud：

```bash
sudo docker run \
--sig-proxy=false \
--name nextcloud-aio-mastercontainer \
--restart always \
--publish 80:80 \
--publish 8080:8080 \
--publish 8443:8443 \
--volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
--volume /var/run/docker.sock:/var/run/docker.sock:ro \
nextcloud/all-in-one:latest
```

## 2. Invoice Ninja

我已经使用 Invoice Ninja 近五年了，它从未让我失望过。 Invoice Ninja 是一个很棒的替代方案，因为它可以轻松且专业地创建发票并将其发送给客户。我尝试过其他发票应用程序，但它们都无法与此相比。 Invoice Ninja 包含诸如可自定义的发票创建、定期计费、自动付款提醒以及对多种货币和语言的支持等功能。我还没有找到比 Invoice Ninja 更好的自托管发票解决方案。

你可以使用如下命令部署 Invoice Ninja 的实例：

```bash
docker run -d \
  -v /var/invoiceninja/public:/var/app/public \
  -v /var/invoiceninja/storage:/var/app/storage \
  -e APP_ENV='production' \
  -e APP_DEBUG=0 \
  -e APP_URL='http://ninja.dev' \
  -e APP_KEY='<INSERT THE GENERATED APPLICATION KEY HERE>' \
  -e DB_TYPE='mysql' \
  -e DB_STRICT='false' \
  -e DB_HOST='localhost' \
  -e DB_DATABASE='ninja' \
  -e DB_USERNAME='ninja' \
  -e DB_PASSWORD='ninja' \
  -p '9000:9000' \
  invoiceninja/invoiceninja-debian
```

请注意，你需要一个应用程序密钥，可以使用以下命令生成：

```bash
docker run --rm -it invoiceninja/invoiceninja php artisan key:generate --show
```

## 3. Bitwarden

别误会，我完全赞成使用官方 [Bitwarden](https://thenewstack.io/walkthrough-bitwardens-new-secrets-manager/) 服务器来管理我的密码库，但是出于某些原因，你可能想在你的局域网内使用此 [密码管理器](https://thenewstack.io/linux-pass-a-text-based-password-manager/)。 例如，你可能拥有绝对不能落入坏人之手的信息。 对于此类信息，你可以通过 Docker 在你的局域网上部署 Bitwarden 服务器。 我已经使用 Bitwarden 多年了，并且一直对该产品及其提供的安全性感到满意。 如果你确实决定在你的局域网上部署 Bitwarden 服务器，请注意，它比其他一些选项要复杂一些，但是该公司提供了大量的 [文档](https://bitwarden.com/help/install-and-deploy-unified-beta) 来帮助你完成该过程。

## 4. Homebox

Homebox 实际上是面向家庭的，但这并不意味着它对你的小型企业来说不是一个可行的选择。 Homebox 所做的是帮助你跟踪几乎所有你需要的东西。 你还可以创建用于存放这些项目的房间，或用于收集项目的位置（例如，办公室、厨房等）。 需要理解的一件事是，当你第一次创建一个项目时，你可以保存的信息非常有限。 但是，一旦创建了该项目，请返回该项目的编辑页面，你将发现可以使用更多字段。 Homebox 还包括资产 ID 标签生成器、物料清单功能、导入/导出和库存操作。 还有一个强大的搜索功能和标签功能，用于在你的项目列表失控时使用。 需要记住的一件事是 Homebox 仍处于早期开发阶段。

可以使用以下命令免费部署和使用 Homebox：

```bash
docker run -d \
  --name homebox \
  --restart unless-stopped \
  --publish 3100:7745 \
  --env TZ=Your/Locale\
  --volume /path/to/data/folder/:/data \
  ghcr.io/hay-kot/homebox:latest
```

请确保更改 *Your/Locale* 以匹配你的位置。

## 5. Outline

Outline 是一种知识库工具，可以帮助你将公司的信息收集在一个地方。 Outline 是一款功能强大的协作式笔记应用程序，包括 markdown 支持、斜杠命令、交互式嵌入等等。 使用此应用程序，你可以与团队成员实时协作、添加评论和线程、使用强大的搜索工具、将其与 Slack（以及其他 20 多种工具）集成以及与公众共享文档。

部署 Outline 比单个命令要复杂一些，但是你可以阅读 [安装文档](https://docs.getoutline.com/s/hosting/doc/docker-7pfeLP5a8t) 并准确了解其完成方式。 自托管的 Outline 实例可以免费部署和使用。

就这样：仅使用这五个简单的工具（部署为 Docker 容器），你就会发现经营你的企业会更容易一些。 当然，你可以通过 Docker 部署更多的应用程序，但是这些应用程序将帮助你入门。