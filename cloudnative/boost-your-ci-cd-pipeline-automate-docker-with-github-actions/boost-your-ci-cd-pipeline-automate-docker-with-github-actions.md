
<!--
title: 提升你的 CI/CD 流水线：使用 GitHub Actions 自动化 Docker
cover: https://cdn.thenewstack.io/media/2025/02/c974d68e-rose-galloway-green-mzpnzk3prtu-unsplash-scaled.jpg
-->

> 译自：[Boost Your CI/CD Pipeline: Automate Docker With GitHub Actions](https://thenewstack.io/boost-your-ci-cd-pipeline-automate-docker-with-github-actions/)
> 
> 作者：Advait Patel

了解如何使用 GitHub Actions 自动化 Docker 工作流程，以实现更快的部署。

在本指南中，我们将深入探讨如何使用 GitHub Actions 自动化 Docker 工作流程，只需几个简单的步骤即可启动并运行。随着云原生开发的兴起和 CI/CD 流水线日益复杂，自动化是必不可少的。[GitHub Actions 提供了一种无缝的方式来将 Docker 集成](https://thenewstack.io/dockerize-a-rust-application-with-aws-ecr-and-github-actions/)到你的工作流程中，从而减少手动工作并提高部署速度。

让我们开始吧！

## 如何为 Docker 设置 GitHub Actions

![](https://cdn.thenewstack.io/media/2025/02/9c1ca0d2-picture1.png)

让我们直接进入[设置 GitHub Actions](https://thenewstack.io/8-github-actions-for-setting-up-your-ci-cd-pipelines/)。你需要做的第一件事是创建一个工作流程文件。它是一个简单的 YAML 文件，位于你的 repo 的 `.github/workflows/` 目录下。

步骤 1：创建工作流程文件

1. 转到你的 repo。
2. 创建一个名为 `.github` 的文件夹（如果它尚不存在）。
3. 在其中创建一个名为 `workflows` 的文件夹。
4. 在 `.github/workflows/` 中创建一个名为 `docker.yml`（或任何你喜欢的名称）的文件。

这是你的 docker.yml 文件的基本结构：

```yaml
name: Docker Workflow
 
on:
  push:
    branches:
      - main
 
jobs:
  build:
    runs-on: ubuntu-latest
 
    steps:
      - name: Check out code
        uses: actions/checkout@v2
 
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
 
      - name: Build Docker Image
        run: docker build -t myapp:${{ github.sha }} .
      
      - name: Push Docker Image
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login --username ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push myapp:${{ github.sha }}
```

上面的 YAML 文件会自动构建。此外，每当更改被移动到 `main` 分支时，它都会推送你的 Docker 镜像。

## 自托管与 GitHub 托管的 Runners

![](https://cdn.thenewstack.io/media/2025/02/fb867bd8-picture1.png)

有两种选择可用于执行你的工作流程：

GitHub 托管的 runners 是默认选项。设置相对免维护，并且对你来说很方便。

使用自托管的 runners，用户可以完全控制工作流程执行机器。虽然此方法提供了更高的灵活性，但它需要持续维护。

对于大多数用户来说，GitHub 托管的 runners 将是首选解决方案。因为它们最适合 Docker 构建。

## 自动化 Docker 镜像构建

![](https://cdn.thenewstack.io/media/2025/02/ed04ff13-picture1.png)

假设你已经推送了一些新代码。现在，你想自动化构建你的 Docker 镜像。你可以这样做。

### 步骤 2：自动构建 Docker 镜像

你将在 [GitHub Actions 工作流程](https://thenewstack.io/the-missing-part-of-github-actions-workflows-monitoring/)文件中使用 `docker build` 命令来自动构建你的 Docker 镜像。

例如，在你的 `docker.yml` 文件中：

```yaml
- name: Build Docker image
  run: docker build -t myapp:${{ github.sha }} .
```

上述命令将[创建一个 Docker 镜像](https://thenewstack.io/tutorial-create-a-docker-image-from-a-running-container/)，并使用 commit `SHA (${{ github.sha }})` 对其进行标记。它确保每个镜像都使用 commit ID 唯一标记。

### 步骤 3：动态标记 Docker 镜像

你可能希望以有意义的方式标记你的镜像。例如，按分支名称，或者使用版本标签。你可以使用 GitHub Actions 变量来做到这一点：

```yaml
- name: Build and tag Docker image
  run: docker build -t myapp:${{ github.sha }} -t myapp:${{ github.ref }} .
```

在这个例子中：

- `${{ github.sha }}` 使用唯一的 commit 哈希标记镜像。
- `${{ github.ref }}` 使用分支名称（例如，refs/heads/main）标记它。
它可以使你的镜像易于跟踪和识别。

## 推送到 Docker Hub 或 GHCR

现在你已经构建了镜像，下一步是将其推送到容器注册表，例如 [Docker Hub 或 GitHub Container](https://thenewstack.io/bypass-docker-hub-rate-limits-with-this-stateless-image-cache/) Registry (GHCR)。

### 步骤 4：设置安全身份验证

首先，你需要验证 Docker 才能推送镜像。由于你不想直接在 YAML 文件中暴露你的凭据，因此 GitHub Secrets 是你的好帮手。

转到你的 GitHub repo 的 Settings > Secrets 并添加两个 secrets：

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

然后，在你的工作流程文件中，你将使用这些 secrets 登录到你的 Docker：

```yaml
- name: Log in to Docker Hub
  run: |
    echo ${{ secrets.DOCKER_PASSWORD }} | docker login --username ${{ secrets.DOCKER_USERNAME }} --password-stdin
```

### 步骤 5：将镜像推送到 Docker Hub 或 GHCR

最后，登录后，推送你的 Docker 镜像：

```yaml
- name: Push Docker image to Docker Hub
  run: docker push myapp:${{ github.sha }}
```

YAML 代码将你的镜像推送到 Docker Hub。此外，如果这是你的选择，你可以将其换成 GHCR。

## 使用 QEMU 和 Buildx 进行多架构构建

你现有的工作流程必须支持多种机器架构，例如 ARM 和 x86。它允许启动[从 Raspberry](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/) Pi (基于 ARM) 设备到基于云的服务器 (基于 x86) 的硬件操作。在此阶段，QEMU+Buildx 在 [GitHub Actions 内部](https://thenewstack.io/how-to-use-databases-inside-github-actions/)的组合非常方便。

### 步骤 6：设置多架构构建

首先，你必须在你的工作流程文件中设置 QEMU 和 Buildx。

以下是它的样子：

```yaml
- name: Set up QEMU
  uses: docker/setup-qemu-action@v2
 
- name: Set up Buildx
  uses: docker/setup-buildx-action@v1
 
- name: Build multi-arch Docker image
  run: |
    docker buildx build --platform linux/amd64,linux/arm64 -t myapp:${{ github.sha }} .
```

这将为 amd64（标准桌面/服务器架构）和 arm64（Raspberry Pi 和一些云服务器使用）构建镜像。

## 安全性改进：扫描镜像中的漏洞

[安全性始终是重中之重](https://thenewstack.io/what-we-can-learn-from-the-top-cloud-security-breaches/)。 你不希望推送有漏洞的镜像。

### 步骤 7：扫描 Docker 镜像中的漏洞

你可以将 Trivy 和 Snyk 等安全工具集成到你的 GitHub Actions 中，以[在构建过程中扫描你的镜像](https://thenewstack.io/3-best-practices-for-image-building-and-scanning/)。 这是一个使用 Trivy 的示例：

```yaml
- name: Scan Docker image for vulnerabilities
  run: |
    trivy image myapp:${{ github.sha }}
    if [ $? -ne 0 ]; then exit 1; fi
```

如果 Trivy 检测到漏洞，构建将失败。 这确保只有安全的镜像才能被推送。

## 自动化部署

你已经构建了你的 Docker 镜像，现在必须将其推送到注册表。 现在，是时候部署它了。

### 步骤 8：部署到 Kubernetes

使用 GitHub Actions，你可以轻松地[将你的 Docker 镜像部署到 Kubernetes 集群](https://thenewstack.io/deploy-mongodb-in-a-container-access-it-outside-the-cluster/)。 这是如何做到的：

```yaml
- name: Deploy to Kubernetes
  uses: appleboy/kubernetes-action@v0.1.0
  with:
    kubeconfig: ${{ secrets.KUBECONFIG }}
    context: ${{ secrets.K8S_CONTEXT }}
    command: kubectl set image deployment/myapp myapp=myapp:${{ github.sha }}
```

该 action 使用标记为 `${{ github.sha }}` 的最新镜像更新 Kubernetes 部署。

## 总结

使用 [GitHub Actions 自动化你的 Docker 工作流程可以显著提高你的开发管道](https://thenewstack.io/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/)、可靠性和安全性。 因此，你现在拥有一个无需手动干预的自动化管道，它可以构建 Docker 镜像，将它们推送到注册表，扫描它们以查找已知漏洞，并将它们部署到你的环境中。

最好的部分？ 你只需几行 YAML 即可直接从 GitHub 完成所有这些操作。 因此，无论你是推送代码、测试镜像还是部署到生产环境，GitHub Actions 都能满足你的需求。

那么，你准备好冒险了吗？ 立即开始自动化你的 Docker 工作流程！ 有关完整的演示，请查看 GitHub 存储库。
