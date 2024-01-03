<!--
title: 数据库的GitOps第一部分 - CI/CD
cover: https://atlasgo.io/uploads/ci-cd-guide/database-ci-cd-workflow.png
-->

本文是两部分教程的第一部分，演示如何将 [Atlas Operator](https://github.com/ariga/atlas-operator) 与 [Atlas Cloud](https://atlasgo.cloud/?utm_source=atlasgo&utm_medium=website&utm_term=blog_2023_12_06_gitops-for-databases-part-1) 和 [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) 相结合，在 Kubernetes 中创建一个现代的、优雅的 GitOps 工作流程，以原生方式管理数据库迁移。

> 译自 [GitOps for Databases， Part 1: CI/CD](https://atlasgo.io/blog/2023/12/06/gitops-for-databases-part-1)。作者 Rotem Tamir 。

[GitOps](https://opengitops.dev/) 是一种软件开发和部署方法，使用 Git 作为代码和基础设施配置的中心仓库，实现自动化和可审计的部署。

[ArgoCD](https://argoproj.github.io/cd/) 是一个 Kubernetes 原生的持续交付工具，遵循 GitOps 原则。它使用声明式方法将应用程序部署到 Kubernetes，以确保应用程序始终处于所需状态。

[Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) 是 Kubernetes 的软件扩展，通过在 Kubernetes 集群内应用特定领域知识，实现对复杂的、应用程序特定的操作任务的自动化和管理。

在本教程中,我们将结合使用 [Atlas Operator](https://github.com/ariga/atlas-operator)、[Atlas Cloud](https://atlasgo.cloud/?utm_source=atlasgo&utm_medium=website&utm_term=blog_2023_12_06_gitops-for-databases-part-1) 和 ArgoCD，在 Kubernetes 中创建一个现代而流畅的 GitOps 工作流程，以原生方式管理数据库迁移。

为了简洁起见，本教程分两部分讲解:

1. **第一部分**，我们将展示如何初始化一个 Atlas 项目，并创建一个 CI/CD 流水线。该流水线利用 GitHub Actions 自动计划、验证数据库迁移，并存储到 Atlas Cloud 中。
2. **第二部分**，我们将介绍如何使用 Atlas Operator 和 ArgoCD 来部署这些迁移，演示数据库迁移的完整 GitOps 工作流程。

![](https://atlasgo.io/uploads/ci-cd-guide/database-ci-cd-workflow.png)

Atlas 的设计是为了支持基于以下原则的数据库迁移的现代 CI/CD 工作流程:

1. **数据库更改由系统自动生成计划**。根据数据库的理想状态，系统自动生成从当前状态过渡到理想状态的计划。
2. **数据库模式更改存储在版本化的迁移目录中**。所有计划的数据库更改提交到版本化的迁移目录，该目录包含按词典顺序执行的 SQL 脚本。
3. **CI 阶段验证数据库更改**。所有数据库更改根据管治策略进行测试和评估。
4. **数据库更改通过自动化部署**。不需要手动步骤。所有更改通过 CI/CD 流水线进行部署。

要深入了解这些原则，可查看我们的[数据库迁移现代 CI/CD 指南](https://atlasgo.io/guides/modern-database-ci-cd)。

本教程将演示如何使用 Atlas Operator 和 ArgoCD 实现自动化部署这一原则。

## 本地环境配置

根据数据库迁移的现代 CI/CD 原则，我们将演示如何将其应用到使用 PostgreSQL 数据库的简单应用程序。

### 第一部分所需环境

1. GitHub 帐户: 我们将设置 GitHub Actions 工作流程，因此需要 GitHub 帐户。
2. 最新版 Atlas:在 Linux 或 macOS 上安装 Atlas。

  ```bash
  curl -sSf https://atlasgo.sh | sh
  ```

更多安装选项请参考[此文档](https://atlasgo.io/getting-started#installation)。

3. Docker: 按照[此](https://docs.docker.com/get-docker/)说明安装 Docker。
4. GitHub CLI 工具 gh，为了安装 gh 需要：

  ```
  brew install gh
  ```

- 其他平台请参考安装说明。

### 第 1 步: 定义目标状态

Atlas 倡导声明式方法，即从定义数据库的目标状态开始工作，系统确定实现细节。Atlas 支持多种方式定义数据库目标状态，称为“模式加载器”。本教程使用简单的 SQL 文件定义目标状态。

在新的 Git 仓库中，创建 `schema.sql` 文件:

```sql
CREATE TABLE users (
  id INT PRIMARY KEY，
  name VARCHAR(255) NOT NULL UNIQUE
);
```

后续如果要改变数据库模式，我们通过更新该文件来反映数据库的目标状态。

### 第 2 步: 规划初始迁移

定义好目标状态后，使用 Atlas CLI 规划初始迁移。创建 `atlas.hcl` 文件:

```hcl
env "local" {
  src = "file://schema.sql"
  dev = "docker://postgres/15/dev"

  migration {
    dir = "file://migrations"
  }

  format {
    migrate {
      diff = "——"
    }
  }
}
```

运行以下命令规划初始迁移:

```
atlas migrate diff --env local
```

在 `migrations` 目录下生成了两个新文件:

```
.
├── atlas.hcl
├── migrations
│   ├── 20221204121249.sql
│   └── atlas.sum
└── schema.sql
```

### 第 3 步: 将迁移目录推送到 Atlas Cloud

Atlas Cloud 是一个托管服务，可以作为数据库迁移的中心仓库。类似 DockerHub 存储 Docker 镜像，Atlas Cloud 可用于存储和分发数据库迁移目录。Atlas Cloud 提供免费级，适合小团队和个人项目，可以用它来学习本教程。

使用以下命令登录 Atlas Cloud:

```
atlas login
```

如果没有现有 Atlas Cloud 帐号，将提示创建一个。

使用以下命令将迁移目录推送到 Atlas Cloud:

```
atlas migrate push --env local atlasdemo
```

这会在 Atlas Cloud 上创建名为 atlasdemo 的新项目，并推送迁移目录。Atlas 会打印 Atlas Cloud 项目页面的 URL，例如:

```
https://rotemtam85.atlasgo.cloud/dirs/4294967359
```

## 设置 GitHub Actions

本节将设置 GitHub Actions 工作流，在 CI/CD 管道中加入 Atlas。

### 创建机器人令牌

为了让 CI/CD 管道向 Atlas Cloud 帐号写入数据，需要提供对 Atlas Cloud 帐号有写访问权限的 API 密钥。请[参考指南](https://atlasgo.io/cloud/bots)学习如何创建机器人令牌，并记录下来，后续步骤会用到。

### 安装 Atlas 扩展

我们提供了 gh 命令来简化 GitHub Actions 工作流程的创建。运行以下命令安装最新版本:

```
gh extension install ariga/gh-atlas
```

### 确保 gh CLI 有足够权限

确保 gh CLI 有配置 GitHub Actions 的写权限:

```
gh auth refresh -s write:packages，workflow
```

### 创建 GitHub Actions 工作流程

安装完成后，使用该扩展生成工作流程，命令如下:

```
gh atlas init-action --token <your-bot-token> --dir-name="atlasdemo" --driver=postgres
```

Atlas 会扫描仓库查找 Atlas 迁移目录，选择 migrations 目录并按下“Enter”:

```
Use the arrow keys to navigate: ↓ ↑ → ←
? choose migration directory:
▸ migrations
```

Atlas 会询问该迁移目录对应的数据库驱动类型。选择需要的驱动类型后按“Enter”确认。

扩展会将机器人令牌保存为 GitHub 密钥，并创建拉取请求以配置 GitHub Action。

![](https://atlasgo.io/uploads/cloud/ci/gh-ext-pr-2.png)

拉取请求包含类似以下的工作流配置:

```yaml
name: Atlas
on:
  push:
    branches:
      - master
    paths:
      - .github/workflows/ci-atlas.yaml
      - 'migrations/*'
  pull_request:
    paths:
      - 'migrations/*'
# Permissions to write comments on the pull request.
permissions:
  contents: read
  pull-requests: write
jobs:
  atlas:
    services:
      # Spin up a postgres:15 container to be used as the dev-database for analysis.
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: dev
          POSTGRES_PASSWORD: pass
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-start-period 10s
          --health-timeout 5s
          --health-retries 5
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - uses: ariga/setup-atlas@v0
        with:
          cloud-token: ${{ secrets.ATLAS_CLOUD_TOKEN_K6MJMK }}
      - uses: ariga/atlas-action/migrate/lint@v1
        with:
          dir: 'file://migrations'
          dir-name: 'atlasdemo'
          dev-url: 'postgres://postgres:pass@localhost:5432/dev?search_path=public&sslmode=disable'
        env:
          GITHUB_TOKEN: ${{ github.token }}
      - uses: ariga/atlas-action/migrate/push@v1
        if: github.ref == 'refs/heads/master'
        with:
            dir: 'file://migrations'
            dir-name: 'atlasdemo'
            dev-url: 'postgres://postgres:pass@localhost:5432/dev?search_path=public&sslmode=disable'
```

查看更改后，合并拉取请求以激活GitHub Action。

## 测试流水线

为了从端到端测试流水线，首先规划对数据库模式的修改。

### 编辑目标数据库模式

编辑 schema.sql 文件，在 users 表中添加 email 列:

```sql
CREATE TABLE users (
  id INT PRIMARY KEY，
  name VARCHAR(255) NOT NULL UNIQUE，
  email VARCHAR(255) NOT NULL UNIQUE  
);
```

### 生成新迁移文件

运行以下命令自动生成新的迁移文件:

```
atlas migrate diff --env local add_email_column
```

在 migrations 目录下生成新文件:

```
.
├── atlas.hcl
├── migrations
│   ├── 20221204121249.sql
│   ├── 20231206075118_add_email_column.sql
│   └── atlas.sum
└── schema.sql
```

### 创建拉取请求

创建分支并推送修改到 GitHub:

```
git checkout -b add-email-column
git add .
git commit -m "Add email column"
git push --set-upstream origin add-email
```

使用 gh 命令行创建拉取请求:

```
gh pr create --title "migrations: add email column" --body "adding email column to users table"
```

### Atlas 审核拉取请求

基于创建的 GitHub Actions 配置，当影响迁移目录的拉取请求被打开时，Atlas 会自动审核。Atlas 运行完成后，会在 PR 中添加评论说明审核结果。

![](https://atlasgo.io/uploads/blog/gitops/lint-comment.png)

如果发现问题，可以点击报告查看详情并进行修正。

![](https://atlasgo.io/uploads/blog/gitops/lint-report.png)

Atlas 报告了两个问题:

1. 添加非空 varchar 列 email 会在 users 表非空时失败。
2. 非并发创建索引会在 users 表上加写锁。

由于处于开发初期阶段，我们可以暂时忽略这些问题。合并拉取请求看看会发生什么。

```
gh pr merge --squash
```

## Atlas 推送迁移到 Atlas Cloud

GitHub Actions 检测到 master 分支合并新推送后，根据配置会运行 `atlas migrate push` 命令，将迁移推送到 Atlas Cloud。推送完成后，Atlas Cloud 模式查看器中可以看到模式已更新。

![](https://atlasgo.io/uploads/blog/gitops/updated-erd.png)

## 第一部分总结

本部分演示了如何使用 Atlas Cloud 和 GitHub Actions 为数据库迁移创建时尚的现代 CI/CD 流水线。第二部分我们将介绍如何使用 Atlas Operator 和 ArgoCD 进行迁移部署，展示完整的数据库迁移 GitOps 工作流程。

非常欢迎您在 [Discord](https://discord.gg/zZ6sWVg6NT) 上提出反馈和建议。
