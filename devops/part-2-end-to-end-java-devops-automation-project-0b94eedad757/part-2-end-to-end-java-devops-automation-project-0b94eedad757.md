
<!--
title: 端到端Java DevOps自动化项目-第2部分
cover: ./cover.png
-->

先决条件：第 1 部分 端到端 Java DevOps 自动化项目

> 译自 [Part-2 End-to-End Java DevOps Automation Project](https://medium.com/@navin5556/part-2-end-to-end-java-devops-automation-project-0b94eedad757)，作者 Naveen Kumar。

**先决条件**: [端到端 Java DevOps 自动化项目 - 第1部分](https://yylives.cc/2024/07/23/part-1-end-to-end-java-devops-automation-project-97835d7b7914/)

## 设置私有 GitHub 仓库

### 第 1 步：创建私有 Git 仓库

1. 访问您首选的 Git 托管平台（例如，GitHub、GitLab、Bitbucket）。
2. 登录您的帐户，如果您没有帐户，请注册。
3. 创建一个新的仓库并将其设置为私有。

### 第 2 步：生成个人访问令牌

1. 导航到您的帐户设置或个人资料设置。
2. 找到“开发者设置”或“个人访问令牌”部分。
3. 生成一个具有必要权限的新令牌（例如，仓库访问权限）。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IPTt613Uk4j1V1_1icjAmg.png)

### 第 3 步：在本地克隆仓库

1. 打开 Git Bash 或您的终端。
2. 导航到您要克隆仓库的目录。
3. 使用 `git clone` 命令，后跟仓库的 URL：
  
```
git clone <repository_URL>
```


将 `<repository_URL>` 替换为您的私有仓库的 URL。

### 第 4 步：添加您的源代码文件

1. 导航到克隆的仓库目录。
2. 在此目录中添加您的源代码文件或创建新文件。

### 第 5 步：暂存和提交更改

1. 使用以下命令暂存更改：

```
git add .
```

2. 使用有意义的消息提交暂存的更改：

```
git commit -m "Your commit message here"
```

### 第 6 步：将更改推送到仓库

1. 将您提交的更改推送到远程仓库：

```
git push
```

2. 如果这是您第一次推送到此仓库，您可能需要指定远程和分支：

```
git push -u origin master
```

将 `master` 替换为分支名称，如果您要推送到其他分支。

### 第 7 步：输入个人访问令牌作为身份验证

当在推送过程中提示输入凭据时，输入您的用户名（通常是您的电子邮件）并使用您的个人访问令牌作为密码。

通过遵循这些步骤，您将能够创建一个私有 Git 仓库，使用 Git Bash 连接到它，并使用个人访问令牌进行身份验证安全地推送您的代码更改。

注意：这是**源代码管理-第2部分**的结尾，第 3 部分将涵盖**CI/CD 流水线配置**。