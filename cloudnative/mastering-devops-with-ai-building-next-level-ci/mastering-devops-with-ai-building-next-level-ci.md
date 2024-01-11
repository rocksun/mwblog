<!--
title: 利用AI掌握DevOps：构建新的CI/CD流水线
cover: ./cover.png
-->

在AI辅助编程飞速发展的时代，健全的DevOps实践显得尤为重要。本博客将演示如何在构建和增强CI/CD流水线中高效利用AI，并强调虽然AI带来重大进步，但人的专业知识仍不可替代。

> 译自 [MASTERING DEVOPS WITH AI: BUILDING NEXT-LEVEL CI/CD PIPELINES](https://www.eficode.com/blog/mastering-devops-with-ai-building-next-level-ci/cd-pipelines)。作者 Alex Jantunen 。

建立可靠的DevOps基础已不再需要数月时间。有了正确的方法和工具，甚至小项目也能在数天或数周内建立适当的DevOps。现在，让我们关注CI/CD的基础部分，从Git workflow开始。

![](https://www.eficode.com/hs-fs/hubfs/Eficode%202020%20site%20images/Blog%20images/image-1.png?width=2084&height=1042&name=image-1.png)

## Git workflow: 良好CI/CD的基石

众所周知，清晰、完善的Git workflow对每个成功的开发项目尤其是DevOps至关重要。这里，我将演示如何在ChatGPT 4的帮助下从零开始建立Git workflow。您可以使用我在此使用的同样提示来测试结果(需要ChatGPT 4版本)。

### 提示 #1

第一条提示通常用来介绍主题，这种方法可以观察初始响应并理解讨论方向。单次提示是不够的，请继续阅读，看看我如何进一步引导讨论。我的第一条提示如下:

请提供Git workflow基线，以便我可以在之后在工作流实践的基础上实现持续集成和部署流水线。

### GPT回复:

创建**可靠的Git workflow**基线对有效实现持续集成(**CI**)和持续交付(**CD**)流水线**至关重要**。这里是一个可作为起点的推荐基线工作流:

### 分支策略:

- **Main 分支**: 源代码的主要分支，其中HEAD始终反映 Ready for Production 状态。
- **Develop 分支**: 用于集成功能的分支。它始终处于包含下一个发布版本最新提交开发变更的状态。
- **Feature 分支**: 在开始新功能开发时创建这些分支，基于“develop”分支，并在功能完成时合并回“develop”。
- **Release 分支**: 当准备新生产版本时，从“develop”分支。这使一组可以完善当前版本，而另一组继续为下个版本开发功能。

**热修复分支**: 用于快速修补生产版本，它们与发布分支和特性分支类似，不同的是它们基于“main”，并合并到“main”和“develop”。

### 持续集成(CI):

- 设置一个CI流水线，在任何分支(尤其是“开发”和“特性”分支)有新提交时运行自动化测试和其他检查(如代码规范检查)。

### 持续部署(CD):

- 如果环境允许，一旦CI流水线通过且变更合并到主分支，自动部署到生产环境。
- 对于更严格控制的环境，可以从主分支手动触发部署。

### 版本标记:

在每个发布后，使用版本号对 main 分支中的代码进行标记。

### 文档:

- 确保项目文档保持最新，包括代码文档以及**工作流程和流水线过程**。

另外还有提交指南、代码审查和合并等部分，但我们在本文不详细展开，尽管它们也很重要。

## 使用 Git workflow 基线的总结

即使是 AI 也强调了 Git workflow 的重要性，它建议使用独立的开发和发布分支，这在正确实施时是好的策略。但为了演示，我将展示一个更精简的可能更优化的工作流程。

重要方面: 记录你的工作流程和流水线!AI 的思考过程在这里非常清晰，并且大多数情况下优于现实。

关于这些主题的清晰沟通和回顾可以确保良好的开发者体验。

### 提示 #2

现在我们已经得到了初始回复，并且ChatGPT记录了讨论历史以便未来提示使用，我计划请求更具体的细节。建议在第一次提示后和每次后续回复后评估回复，如果需要，深入探讨任何新出现的主题。

之后再继续下一个提示，以避免中断聊天，这很容易在大型语言模型中导致不理想的结果。

请使工作流程更简单，删除开发和发布分支，对于那些我将使用git标签。

### GPT回复:

好的！通过删除开发和发布分支并使用Git标签可以简化Git workflow程，使过程更精简，特别适合小团队或项目。这里是修改后的工作流程:

### Main 分支:

- 这是您的主要和唯一长期分支，表示代码的生产准备状态。
- 所有功能、错误修复和热修复直接合并到这个分支。

### Feature 分支:

- 开始新功能或错误修复时，创建Feature分支。
- 从主分支分支出来，完成工作并测试后，合并回main分支。
- Feature分支的命名约定可以是:

```
feature/<feature-name>
```

或

```
bugfix/<bug-name>
```

### 发布时的Git标签:

- 准备发布新版本时，在 main 分支上使用Git标签。
- 使用语义化版本控制(如v1.0.0，v1.0.1)命名标签，以跟踪不同版本。
- 标签也可以在必要时用于触发特定的 CI/CD 操作。

### 持续交付(CD):

- 如果项目设置允许，在通过 CI 检查后设置 **CD 以自动将 main 分支部署到生产环境**。
- 对于更控制的环境，可以选择手动部署标记的版本。

其他部分与之前大致相同，此处不再赘述。

## 删除开发和发布分支以简化工作流程的总结

很好，这现在看起来符合我的要求。然而，GPT 建议 CI 后自动部署主分支到生产会引发担忧。

为了系统稳定可靠，我们肯定需要类生产环境，如暂存环境进行适当的质量保证(QA)。

在任何变更后，在类生产环境中运行自动回归测试非常重要。这不仅包括产品中的代码变更，还包括基础设施(IaC)、流水线等方面的变更。

### 提示 #3

对于持续交付，我希望只自动将主分支部署到类生产环境，如暂存环境。而生产部署应通过使用前缀为“release-”的 git 标签完成，例如 release-v1.0.0。对于暂存环境，前缀将是 rc-(release-candidate)。

### GPT回复:

您使用特定的 Git 标签约定为暂存和生产环境实现持续交付是非常好的策略。以下是如何构建此工作流程:

### Main 分支作为暂存环境:

- 主分支充当类似暂存的环境。每次合并到主分支都会触发自动部署到暂存环境。
- 以便在类似生产的环境中测试。

### 暂存和生产的 Git 标签:

- 暂存标签: 使用前缀 rc- (release candidate) 进行暂存环境部署，例如 rc-v1.0.0 表示 1.0.0 版本的发布候选版本。推送此前缀标签会触发部署到暂存环境。
- 生产标签: 使用前缀 release- 进行生产环境部署。像 release-v1.0.0 这样的标签用于触发对生产环境的手动部署，以控制生产部署时间和内容。

### 工作流程步骤:

- 开发: 开发人员在 main 出来的 feature 或 bugfix 分支上工作。
* 代码审查和合并: 完成工作后，创建拉取请求以将更改合并到main分支。代码审查和 CI 检查通过后，合并更改。
- 自动暂存部署: 合并到 main 分支会自动触发部署到暂存环境，用于最终测试和验证。
- 打标签生成发布候选版本: 当团队对暂存环境中的更改满意时，创建 rc- 标签以正式标记发布候选版本。
- 生产部署: 发布候选版本经彻底测试和批准后，创建 release- 标签，使用该标签手动触发生产环境部署。

### 持续集成和交付:

- 根据标记约定，设置 CI/CD 流水线以处理不同的环境。
- 确保 CI 流水线包含所有必要的测试和质量检查。

### 文档:

- 清楚记录此过程，包括如何以及何时标记暂存环境和生产环境的部署。

这种设置可以明确区分暂存环境和生产环境部署，并让团队掌控发布流程。使用不同的标签进行暂存环境(rc-)和生产环境(release-)部署，可以轻松管理和跟踪不同版本在环境间的流转。

## 自动部署到类生产环境的总结

现在我对工作流程感到满意。可以用类似的方式实现期望的工作流程。

如果完全混淆了与 AI 的聊天，最好重新开始一个，以防止误导性回复。

这次我在首次聊天中就得到了结果，但许多时候并非如此容易。接下来，我将使用 Atlassian Bitbucket 流水线作为底层技术，通过代码实现实际的流水线。

面向 DevOps 流水线的生成式 AI

这部分将展示 ChatGPT 如何生成 Bitbucket 流水线描述文件来实现上述目标。

### 提示 #4

我将在同一聊天中继续提示，以便语言模型有相关上下文。

现在我想你基于最近回复的最新工作流，为我提供 bitbucket-pipelines.yaml。为我的后端服务提供流水线，该服务使用 python flask 实现，我想部署到 GCP 上的 Google Kubernetes。

这里我收到了一个高层次的实现，大多数细节被移到了单独的 shell 脚本中。这并非我的本意，所以不会在此展示回复。然而，经过几轮讨论，我得到了需要的结果。

### 提示 #5 到 #8

在涉及复杂主题的生成式AI中，多次提示是常见的。AI无法从一个细节有限的单一提示中推断出确切需求。此外，将更大的任务分割成较小、可管理的部分也是必要的。这个过程还需要全面理解DevOps来有效引导对话。不应期望轻易获得良好结果。

 #5 - 好的，这有点过于高层次。我想让你包括构建docker镜像并推送到Google Cloud仓库gcr.io。另外还需要包含gcloud cli和kubectl命令。以及在需要的地方添加环境变量和密钥的占位符。

 #6 - 这很好，但是如果手动触发带有release-*标签会怎样?

 #7 - 我想使用bitbucket部署环境，请给我带有这些信息修改的最新bitbucket-pipelines.yaml文件。

 #8 - 我想修改流水线，使得 docker 镜像只构建一次，后续可以重新打标签，不需要从头再构建。

### GPT-4回复:

为了修改流水线使 Docker 镜像只构建一次然后为不同环境重新打标签，需要对 bitbucket-pipelines.yml 做一些调整。思路是构建一次 Docker 镜像，使用通用标签推送到 Google Container Registry(GCR)，然后根据需要为暂存或生产部署重新打标签。

下面是带有这些更改的更新后的 bitbucket-pipelines.yml 文件:


```yaml
image: atlassian/default-image:2
pipelines:
  default:
    - step:
        name: Build and Test
        caches:
          - pip
        script:
          - pip install -r requirements.txt
          - python -m unittest discover tests
  branches:
    main:
      - step:
          name: Build and Push Docker Image
          script:
            - echo $GCLOUD_SERVICE_KEY | base64 --decode --ignore-garbage > ${HOME}/gcloud-service-key.json
            - docker build -t gcr.io/$GCLOUD_PROJECT/your-app:latest .
            - gcloud auth configure-docker --quiet
            - docker push gcr.io/$GCLOUD_PROJECT/your-app:latest
      - step:
          name: Deploy to Staging
          deployment: staging
          script:
            - echo "Deploying to Staging Environment"
            - ./deploy-staging.sh # This script should handle the retagging for staging
  tags:
    'rc-*':
      - step:
          name: Retag and Deploy to Staging
          deployment: staging
          script:
            - echo "Retagging and Deploying Release Candidate to Staging"
            - ./retag-deploy-staging.sh # Script to retag the image for staging
    'release-*':
      - step:
          name: Retag and Deploy to Production
          deployment: production
          trigger: manual
          script:
            - echo "Retagging and Deploying to Production Environment"
            - ./retag-deploy-production.sh # Script to retag the image for production
definitions:
  caches:
    pip: ~/.cache/pip
```

关键变更

单次镜像构建: Docker 镜像仅在提交到main分支时构建和推送一次，标记为latest。

### 重新打标签以部署到暂存和生产:

- ./deploy-staging.sh脚本用于直接将latest标签部署到暂存环境。
- 对于 rc-* 和 release-* 标签，使用单独的脚本(./retag-deploy-staging.sh 和 ./retag-deploy-production.sh)。这些脚本应处理为 Docker 镜像重新打标签(基于提交或发布标签)，然后将其部署到相应的环境。

### 重新打标签和部署的脚本

- ./deploy-staging.sh 应在不重新打标签的情况下，将 latest 镜像部署到暂存环境。
- ./retag-deploy-staging.sh 和 ./retag-deploy-production.sh 应该:
  - 从 GCR 拉取最新的镜像
  - 使用特定的提交或发布标签重新打标签
  - 将重新打过标签的镜像推送回 GCR
  - 更新 Kubernetes 部署以使用新的标签

这种方法确保 Docker 镜像只构建一次，节省时间和资源。重新打标签脚本提供在不重建镜像的情况下管理不同环境的灵活性。请确保 GCP 服务帐户具有必要的权限，并替换占位符为实际项目详情。

## 来自语言模型的最终输出总结

重复这些步骤对系统的每个组件，无论是服务、UI还是应用程序。根据我在 Bitbucket 流水线方面的经验，我可以比较有信心地评估响应，并了解使其可操作所需的内容。但是，如果我不熟悉这些技术，预计会遇到一些意外挑战。

随着语言模型变得更加先进和专业化，响应质量无疑会有改善。AI将极大加速DevOps领域新技术和流程的采用。

## 通过AI实现DevOps基线的实践

以上就是我的演示，展示了如何在AI的帮助下在实践中实现DevOps基线。开始提示不需要高级技能，但与任何运动一样，通过练习可以取得更好结果。

基线还有几方面需要改进，例如全面的持续集成，包括DevSecOps、IaC等。

在AI的帮助下，上手DevOps主题变得更容易。互联网上有大量优质资料，这些资料似乎很好地集成到了语言模型中。但是，需要理解的是，这类设计讨论与最先进的语言模型进行更有效。例如，与GPT-3.5进行同样讨论会大不相同。

人们常认为CI/CD对较小项目投入过大。然而，与忽视它或后期实施相比，它轻松超过了成本。已经没有理由再犹豫是否要从一开始就投资DevOps。

随着时间流逝，我预计会出现越来越全面化的开发平台，其中许多流程实现自动化，使开发和 DevOps 更抽象化。尽管如此，解决问题的技能和对基本原理的深刻理解仍将保持重要性。

希望这篇博客能激发你从一开始就实施 DevOps 和/或改进当前状况的动力。

如果你喜欢这篇博客，也许你会喜欢我们关于 DevOps 工具链中 AI 的[播客剧集](https://www.eficode.com/devops-podcast/ai-in-devops?_gl=1*1w0nd77*_up*MQ..*_ga*MTk0NTM0NzY5LjE3MDQ3MzkyMTg.*_ga_H7FVZKYH8C*MTcwNDczOTIxNy4xLjEuMTcwNDczOTMzNi4wLjAuMA..&hsLang=en)。
