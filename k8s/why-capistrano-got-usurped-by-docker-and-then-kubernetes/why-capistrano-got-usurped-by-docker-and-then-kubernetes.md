<!-- 
# 为什么Capistrano被Docker和Kubernetes取代了
https://cdn.thenewstack.io/media/2023/10/185c3c6b-sven-brandsma-odf1ywzw_va-unsplash-1024x683.jpg
Image via Unsplash.
 -->

David Eastman主持了一场技术版的古董鉴定节目，通过回顾前容器(甚至是Chef之前!)时代的软件工具Capistrano。

译自 [Why Capistrano Got Usurped by Docker and Then Kubernetes](https://thenewstack.io/why-capistrano-got-usurped-by-docker-and-then-kubernetes/) 。

当我听著受欢迎的知识产权和数字权利倡导者[Cory Doctorow](https://www.kickstarter.com/projects/doctorow/the-lost-cause-a-novel-of-climate-and-hope)朗读他的新书的一小部分时，我听到他提到了加利福尼亚州的 Capistrano。但我当然还记得[Capistrano](https://capistranorb.com/)，这是一种流行于2010年代初的远程服务器自动化工具——它实际上是容器和Kubernetes之前的工具。

我有时对随着时间流逝失去流行度的常用技术感兴趣。当然，Capistrano并没有真正死亡——即使我正在使用过去式来描述它。开源工具从未真正死亡，它们只是变得不受欢迎(并可能被储存在阁楼中)。我记得在十多年前曾将Capistrano用作远程服务器自动化工具。它会使用SSH按照脚本允许您将更新部署到目标服务器。更新可能是一个新的可执行文件，可能是一些代码，可能是一些配置，可能是一些数据库更改。很好，但为什么要回顾一个不再常用的系统呢？

首先，为了理解趋势，回顾过去的例子很有帮助。当某样东西的流行度下降时注意其点也很有帮助，同时检查我们是否失去了任何东西。当前的技术只是时间线上的一个小插曲，如果你偶尔回头看一眼，预测接下来会发生什么会容易得多。如果您需要在新站点上处理部署，除了您自己偏爱的工具之外，拥有一系列工具也很好。您甚至可能不得不在旧堆栈中使用Capistrano。因此，让我们来评估这件古董，看看它有多大的价值。

## 环境

Capistrano了解您将处理的三个基本环境: 通常是**生产**，**暂存**和**开发**。开发环境可能是笔记本电脑;暂存环境可能是某种QA可以访问的云服务器。使用这些定义，Capistrano可以针对特定计算机执行操作。

## 任务和角色

Capistrano中的基本命令是任务。这些是在部署的不同阶段执行的。但是要过滤这些任务，您可以使用角色来描述您正在处理的系统的哪一部分:

```rb
role :app, "my-app-server.com"
role :web, "my-static-server.com"
role :db, "my-db-server.com"
```

这表示应用程序服务器(生成动态内容的部分)、网页或Web服务器以及数据库作为单独的部分。您当然可以创建自己的定义。

或者，您可以更多地关注环境分离，而角色在其下操作。对于生产环境的描述，我们可能会设置以下内容:

```rb
# config/deploy/production.rb

server "11.22.333.444"， user: "ubuntu"， roles: %w{app db web}
```

默认部署任务具有代表部署阶段的几个子任务:


- **deploy:starting** 开始部署，确保先决条件得到满足
- **deploy:updating** 使用新版本更新服务器
- **deploy:publishing** 发布新版本
- **deploy:finishing** 完成部署，开始清理
- **deploy:upload** 将文件复制到当前部署的版本。这对于分阶段更新文件很有用
- **deploy:rollback** 全部回滚

这是一个自定义的部署任务的示例。这种类似ruby的代码使用角色来过滤任务，以及部署的阶段。在本例中，我们可以在完成之前更新style.css文件:

```rb
namespace :deploy do
   after :finishing, :upload do
     on roles(:web) do
       path = "web/assets"
       upload! "themes/assets/style.css", "#{path}"
     end
     on roles(:db) do
       # Migrate database
     end
   end
 end
```

在Capistrano安装后，您可以在命令行中使用以下命令触发此操作:

```bash
cap production deploy
```

默认部署流程及相应的回滚流程。这是一个更详细的示例:

```rb
deploy
  deploy:starting
    [before]
      deploy:ensure_stage
      deploy:set_shared_assets
    deploy:check
  deploy:started
  deploy:updating
    git:create_release
    deploy:symlink:shared
  deploy:updated
    [before]
      deploy:bundle
    [after]
      deploy:migrate
      deploy:compile_assets
      deploy:normalize_assets
  deploy:publishing
    deploy:symlink:release
  deploy:published
  deploy:finishing
    deploy:cleanup
  deploy:finished
    deploy:log_revision
```

您可以看到钩子——"started"、"updated"、"published"和"finished"——它们对应于动作"starting"、"publishing"等。这些用于使用*before*和*after*子句将自定义任务挂钩到流程中，就像我们上面看到的那样。

请注意，在发布后创建或更新一个指向最新版本的"current"符号链接。如果在任何步骤中部署失败，current符号链接仍指向旧版本。

## 那么发生了什么?

"先运行这个，然后运行那个"的模型并不能总是很好地预测部署后您的系统会是什么样子。像Chef这样的工具更擅长处理蔓延的系统，因为它们从模型开始，然后说“使这个设置为真”。Chef以收敛和幂等作为工作方式。丢失的位会被添加，但在那之后重新应用相同的步骤不会改变任何事情。因此，对相同操作的多次执行不会对状态产生副作用。

> Capistrano的灵活性会允许较少经验的开发人员建立工作但不稳定的部署。

相比之下，单个Docker镜像允许对OS、包、库和代码进行系统性控制。它还允许笔记本电脑和云服务器以相似的方式对待——仅仅作为挂载容器的地方。

最后，Kubernetes在不必担心速度变慢和超时的情况下处理了集群。拥有一个完全透明的基础设施，以及运行所有方面的所需服务和确切配置的能力，使DevOps团队的生活更加轻松。与更改已经运行的服务不同，可以创建新容器并终止旧容器。

从现代观点来看，Capistrano的另一个问题是它是用Ruby构建的。Ruby语言不公平地与Ruby on Rails的流行程度联系在一起;那已经随着Node.js和JavaScript的兴起而衰落。总体而言，其他语言和语言趋势在流行度上已经超过了它: 例如，Python已经成为首选的脚本语言。所示的任务使用了一个DSL，它实际上是ruby Rake构建工具。

是否损失了什么呢？可能。拥有一组自定义任务以进行快速更改确实鼓励了黑客方法，但它也允许进行较小的临时基于事件的更改。“使此更改发生”而不是“我总是希望服务器看起来像这样”。

更好的说法可能是，像Capistrano这样的工具出现在任何团队的部署之旅的路径上，作为在需要更广阔的视野之前的一个路径点。但即使作为一个蒙尘的遗迹，Capistrano仍然是一个伟大的模块化工具，用于自动化Web应用程序的部署和维护。

至于加利福尼亚州的Capistrano？恐怕是坏消息。

![](https://cdn.thenewstack.io/media/2023/10/899e8e5c-untitled-1024x474.png)

## 惊喜

整理完文章后，我发现原来 Capistrano 就在我身边，vagrant 用了它：

![](https://yylives.cc/wp-content/uploads/2023/10/Snipaste_2023-10-26_20-43-03.jpg)