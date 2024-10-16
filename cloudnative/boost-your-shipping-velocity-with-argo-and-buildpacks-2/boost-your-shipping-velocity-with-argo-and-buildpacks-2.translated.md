# 使用 Argo 和 Buildpacks 提升您的交付速度

![Boost Your Shipping Velocity With Argo and Buildpacks 的专题图片](https://cdn.thenewstack.io/media/2024/10/99798b46-chuttersnap-at5-ssyp6e4-unsplash-1024x683.jpg)
*[CHUTTERSNAP](https://unsplash.com/@chuttersnap?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/assorted-shipping-trailers-in-port-aT5-sSYP6e4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 的作品。*

[微软最近的一项研究](https://queue.acm.org/detail.cfm?id=3595878) 调查了哪些因素会推动开发人员的生产力，发现反馈循环具有重大影响。研究结果建议，应尽可能缩短反馈循环，即对执行的操作的响应速度和质量。他们在研究结果中提到的一个例子是将代码推送到生产环境所需的时间。

CNCF 毕业项目 Argo 是 [持续集成和交付](https://thenewstack.io/how-continuous-integration-and-continuous-delivery-ci-cd-enhances-devops/) 工具的首选之一，通常可以让开发人员的生活更轻松。但在将代码推送到 Argo 之前，[开发人员通常需要](https://thenewstack.io/5-things-developers-need-to-know-about-kubernetes-management/) 编写 Dockerfile 来将其容器化。

在本文中，我将探讨如何使用 CNCF 孵化项目 [Buildpacks](https://buildpacks.io/)（一种应用程序定义和镜像构建工具）来跳过 Dockerfile 步骤并提高开发人员的生产力。

## Buidlpacks 如何提高反馈循环速度？

首先，让我们来了解一下 Buildpacks 的背景。云原生 Buildpacks 将您的应用程序源代码转换为可在任何云上运行的镜像。通过查看您的代码，Buildpacks 会自动检测构建具有最佳性能和安全实践的 OCI 镜像所需的内容。

使用 Buildpacks 时，不再需要在推送代码之前编写 Dockerfile，以便将其拉入 Argo。开发人员可以从编写代码直接过渡到将其推送到公司 CI/CD 管道。

## 在 Argo 中集成 Buildpacks

Buildpacks 是定义如何将源代码转换为容器化应用程序的规范。但是要根据这些规范创建 OCI 镜像，您需要使用 [pack 命令](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/) 并指定一个 Buildpack（稍后会详细介绍）。

此步骤用作 Argo 工作流的一部分：

```yaml
- name: build-image
  inputs:
    parameters:
      - name: passed-tag
  container:
    image: buildpacksio/pack
    command: ["pack", "build"]
    args: 
      - "172.31.17.128:5000/my-python-app:{{inputs.parameters.passed-tag}} --path /mnt/vol/app --builder paketobuildpacks/builder-jammy-base --publish"
```

让我们来看看每个参数：

* `name: build-image` 是 Argo 工作流步骤的名称。我的工作流有多个步骤（克隆和构建）。有关更多信息，请参阅我的 Github 存储库上的[完整配置文件](https://github.com/sylvainkalache/deploy-buildpack-containerized-python-app-to-argo/blob/main/pack-build-argo-workflow.yaml)。
* `inputs: parameters: - name: passed-tag` 这指定了要用于构建我的镜像的代码版本。这是可选的，我将在下一段中进一步解释。
* `image: buildpacksio/pack` 我们使用 buildpacks/pack 镜像来运行此 Argo 步骤。
* `command: ["pack", "build"]` 我们告诉工作流运行 `pack build` 命令。

现在让我们来看看 `pack build` 命令参数：

* `172.31.17.128:5000/my-python-app:{{inputs.parameters.passed-tag}}` IP 是我的容器注册表托管的位置。在这里，我使用的是自托管注册表，但您可以使用从 ECR 到 Dockerhub 的任何注册表。第二部分，`my-python-app`，是我的容器镜像的名称。在下一段中，我将介绍 `{{inputs.parameters.passed-tag}}`。
* `--path /mnt/vol/app` 是我的应用程序代码所在的位置。
* `--builder paketobuildpacks/builder-jammy-base` 构建器是一个镜像，其中包含 buildpack 的有序组合、构建时基础镜像、生命周期二进制文件以及对运行时基础镜像的引用。我使用的是 [Paketo Buildpacks](https://paketo.io/) 中的一个，但这里还有其他提供程序，例如 [Google](https://cloud.google.com/docs/buildpacks/builders) 和 [Heroku](https://devcenter.heroku.com/articles/buildpacks)。
* `--publish` 将应用程序镜像直接发布到镜像名称中指定的容器注册表（参见第一个参数），而不是守护进程。

这就是让 Argo 将以几乎任何语言编写的任何应用程序容器化所需的全部内容。开发人员无需编写 Dockerfile，这意味着一旦他们的应用程序编写完成，他们就可以将其推送到 Argo 并看到它被部署。

## 镜像不变性和发布策略
了解 Buildpacks 的一个要点是，它会使用固定日期（1980 年 1 月 1 日）标记镜像，以确保其不变性和可重复性。使用固定时间戳的原因是为了确保镜像创建的一致性，这有助于消除构建时间造成的差异。这是一项很棒的安全功能，但可能会给 CI/CD 部署工作流带来挑战。如果您的工作流基于最新标签，则会遇到问题，因为所有镜像都将具有相同的时间戳。

这就是我使用语义化版本控制策略的原因。在我的 Argo 工作流中，我利用 Argo 参数输入来获取我要构建镜像的标签。我使用 `inputs: parameters: - name: passed-tag` 接收标签，并使用 `{{inputs.parameters.passed-tag}}` 将其传递给我的 pack 命令。

## 总结

在 Argo 工作流中使用 Buildpacks 将改善开发人员体验和交付速度，并确保您的容器镜像安全且经过优化。实际上，Buildpacks 规范 Paketo Buildpacks 的开源实现 [确保](https://paketo.io/docs/concepts/stacks/) 其镜像始终使用最新的 CVE 补丁进行更新，并针对每个堆栈进行调整。最后但同样重要的是，如果您想深入了解，我录制了 [一个视频](https://youtu.be/TojM-kmYeXA)，其中展示了整个教程，并对一些概念进行了更深入的探讨。

---

**YOUTUBE.COM/THENEWSTACK**

技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube 
频道，观看我们所有的播客、访谈、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)