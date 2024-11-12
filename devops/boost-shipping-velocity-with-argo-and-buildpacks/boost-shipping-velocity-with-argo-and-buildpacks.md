
<!--
title: 提升您的交付速度：Argo与Buildpacks
cover: https://cdn.thenewstack.io/media/2024/10/99798b46-chuttersnap-at5-ssyp6e4-unsplash-scaled.jpg
-->

学习如何使用 CNCF 孵化项目 Buildpacks，一个应用程序定义和镜像构建工具，跳过 Dockerfile 步骤并提高开发人员生产力。

> 译自 [Boost Your Shipping Velocity With Argo and Buildpacks](https://thenewstack.io/boost-shipping-velocity-with-argo-and-buildpacks/)，作者 Sylvain Kalache。

[微软最近的一项](https://queue.acm.org/detail.cfm?id=3595878)研究调查了哪些因素驱动开发人员的生产力，发现反馈循环有很大的影响。研究结果建议，反馈循环——对执行的操作的响应速度和质量——应该尽可能缩短。他们在研究结果中提到的一个例子是将代码推送到生产环境所需的时间。

CNCF 毕业项目 Argo 是[持续集成和交付](https://thenewstack.io/how-continuous-integration-and-continuous-delivery-ci-cd-enhances-devops/)工具的首选之一，通常会让开发人员的工作更轻松。但在将代码推送到 Argo 之前，[开发人员通常需要](https://thenewstack.io/5-things-developers-need-to-know-about-kubernetes-management/)编写 Dockerfile 来将其容器化。

在本文中，我将探讨如何使用 CNCF 孵化项目 [Buildpacks](https://buildpacks.io/)（一种应用程序定义和镜像构建工具）来跳过 Dockerfile 步骤并提高开发人员的生产力。

## Buildpacks 如何提高反馈循环速度？

首先让我们来了解一下 Buildpacks 的背景。云原生 Buildpacks 将您的应用程序源代码转换为可在任何云上运行的镜像。通过查看您的代码，Buildpacks 自动检测构建具有最佳性能和安全实践的 OCI 镜像所需的内容。

使用 Buildpacks 后，不再需要在推送代码之前编写 Dockerfile，以便将其拉入 Argo。开发人员可以从编写代码直接将其推送到公司 CI/CD 管道。

## 在 Argo 中集成 Buildpacks

Buildpacks 是定义如何将源代码转换为容器化应用程序的规范。但是要基于这些规范创建 OCI 镜像，您将使用 [pack 命令](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/) 并指定一个 Buildpack（稍后会详细介绍）。

此步骤用作 Argo 工作流的一部分：

```
- name: build-image
  inputs:
    parameters:
    - name: passed-tag
  container:
    image: buildpacksio/pack
    command: ["pack", "build"]
    args: ["172.31.17.128:5000/my-python-app:{{inputs.parameters.passed-tag}}", "--path", "/mnt/vol/app", "--builder", "paketobuildpacks/builder-jammy-base", "--publish"]
```

让我们来逐个解释每个参数：

* `name: build-image` 是 Argo 工作流步骤的名称。我的工作流有多个步骤（克隆和构建）。有关更多信息，请参阅我的 Github 存储库上的[完整配置文件](https://github.com/sylvainkalache/deploy-buildpack-containerized-python-app-to-argo/blob/main/pack-build-argo-workflow.yaml)。
* `inputs: parameters: - name: passed-tag` 这指定了用于构建我的镜像的代码版本。这是可选的，我将在下一段中进一步解释。
* `image: buildpacksio/pack` 我们使用 `buildpacks/pack` 镜像来运行此 Argo 步骤。
* `command: ["pack", "build"]` 我们告诉工作流运行 `pack build` 命令。

现在让我们看一下 `pack build` 命令参数：

* `172.31.17.128:5000/my-python-app:{{inputs.parameters.passed-tag}}` IP 地址是我的容器注册表托管的位置。这里我使用的是自托管注册表，但您可以使用从 ECR 到 Dockerhub 的任何注册表。第二部分，`my-python-app` 是我的容器镜像的名称。在下一段中，我将介绍 `{{inputs.parameters.passed-tag}}`。
* `--path /mnt/vol/app` 是我的应用程序代码所在的位置。
* `--builder paketobuildpacks/builder-jammy-base` 构建器是一个包含构建包的有序组合、构建时基础镜像、生命周期二进制文件以及运行时基础镜像引用的镜像。我使用的是[Paketo Buildpacks](https://paketo.io/)提供的构建器，但还有其他提供商，例如[Google](https://cloud.google.com/docs/buildpacks/builders)和[Heroku](https://devcenter.heroku.com/articles/buildpacks)。
* `--publish` 将应用程序镜像直接发布到镜像名称中指定的容器注册表（参见第一个参数），而不是守护程序。

这就是让 Argo 容器化几乎任何语言编写的应用程序所需的全部内容。开发人员无需编写 Dockerfile，这意味着一旦他们的应用程序编写完成，他们就可以将其推送到 Argo 并看到它被部署。

## 镜像不变性和发布策略

了解 Buildpacks 的一个重点是，为了实现不变性和可重复性，它会将镜像标记为固定日期（1980 年 1 月 1 日）。使用固定时间戳的原因是为了确保镜像创建的一致性，这有助于消除构建时间造成的差异。这是一项很棒的安全功能，但可能会给 CI/CD 部署工作流带来挑战。如果您的工作流基于 `latest` 标签，您将会遇到问题，因为所有镜像都将具有相同的时间戳。

这就是我使用语义化版本控制策略的原因。在我的 Argo 工作流中，我利用 Argo 参数输入来获取我想要构建镜像的标签。我通过 `inputs: parameters: - name: passed-tag` 接收标签，并使用 `{{inputs.parameters.passed-tag}}` 将其传递给我的 pack 命令。

## 结论

在 Argo 工作流中使用 Buildpacks 将改善开发者体验和交付速度，并确保您的容器镜像安全且经过优化。事实上，Buildpacks 规范 Paketo Buildpacks 的开源实现 [确保](https://paketo.io/docs/concepts/stacks/) 其镜像始终保持最新的 CVE 补丁，并针对每个堆栈进行调整。最后，如果您想深入了解，我录制了[一个视频](https://youtu.be/TojM-kmYeXA)，其中展示了整个教程，并对一些概念进行了更深入的讲解。
