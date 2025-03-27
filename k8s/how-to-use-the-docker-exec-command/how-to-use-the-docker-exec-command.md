
<!--
title: 如何使用Docker exec命令
cover: https://cdn.thenewstack.io/media/2023/09/d9bb1569-dock-1365387_1280-1.jpg
summary: 告别低效！`docker exec`命令详解：无需进入容器内部，直接执行命令！Ubuntu Server实战，轻松访问容器Shell，更新升级 Nginx。掌握`docker exec ID COMMAND`，玩转`&&`运算符，高效管理你的 Docker 容器！
-->

告别低效！`docker exec`命令详解：无需进入容器内部，直接执行命令！Ubuntu Server实战，轻松访问容器Shell，更新升级 Nginx。掌握`docker exec ID COMMAND`，玩转`&&`运算符，高效管理你的 Docker 容器！

> 译自：[How To Use the Docker exec Command](https://thenewstack.io/how-to-use-the-docker-exec-command/)
> 
> 作者：Jack Wallen

## 什么是 exec 命令？

`docker exec` 命令允许用户在已经[部署的容器](https://thenewstack.io/introduction-to-containers/)中运行命令。

**使用 exec 命令的两种方式：**

- 在容器内部：运行 `docker exec -it ID /bin/bash`（其中 ID 是正在运行的容器 ID 的前四个字符）以访问容器的 shell。
- 在容器外部：使用 `docker exec ID COMMAND`（其中 ID 是正在运行的容器 ID 的前四个字符，COMMAND 是要在容器内运行的命令）。

**前提条件：**

- 在 Ubuntu Server 22.04（或更新版本）上运行的 Docker 实例
- 已添加并安装了官方 Docker GPG 密钥

**开始使用 Docker exec 命令的步骤：**

通过添加 GPG 密钥、创建必要的存储库并安装依赖项，在 Ubuntu Server 上[安装 Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)。

- 使用 `--name docker-nginx -p 8080:80 -d nginx` 创建一个测试容器。
- 使用 `docker exec -it ID /bin/bash`（其中 ID 是容器的 ID）访问正在运行的容器的 shell。

**有效地使用 Docker exec 命令：**

- 在容器内部或外部运行命令，而无需访问其 shell。
- 使用 `&&` 运算符将命令链接在一起。
- 通过执行这些步骤，用户可以有效地使用 `docker exec` 命令来管理他们正在运行的 Docker 容器。

对于那些刚开始 Docker 容器之旅的人来说，有很多东西需要学习。除了拉取镜像和部署基本容器之外，您首先要了解的是 `exec` 命令。

从本质上讲，`exec` 命令允许您在已部署的容器中运行命令。`exec` 命令允许您通过两种不同的方式执行此操作……从容器内部或外部。我将向您展示如何做到这两点。最后，您将更好地准备好与正在运行的 Docker 容器进行交互。

## 你需要什么

您只需要在受支持的平台上安装 Docker 运行时引擎的运行实例。我将在 Ubuntu Server 22.04 上演示这一点。

如果您尚未安装 Docker，让我们先处理这个问题。如果您已经安装了 Docker，请继续跳到下一节。

## 安装 Docker

在 Ubuntu Server 上安装 Docker 之前，您必须首先使用以下命令添加官方 Docker GPG 密钥：

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

系统将提示您输入 sudo 密码。
成功添加 GPG 密钥后，使用以下命令创建必要的 Docker 存储库：

使用以下命令安装一些依赖项：

```
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
```

使用以下命令更新 apt：

```
sudo apt-get update
```

使用以下命令安装 Docker：

```
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

接下来，您必须使用以下命令将您的用户添加到 docker 组：

```
sudo usermod -aG docker $USER
```

注销并重新登录，以使更改生效。
恭喜，Docker 现在可以使用了。

## 部署测试容器

要使用 `exec` 命令，我们首先必须部署一个简单的测试容器。为此，我们将使用经过验证的 NGINX 并使用以下命令部署一个容器：

```
docker run --name docker-nginx -p 8080:80 -d nginx
```

运行该命令后，Docker 应该报告容器的 ID。如果您错过了，您可以随时使用以下命令查看它：

```
docker ps
```

您只需要 ID 的前四个字符。

## 访问正在运行的容器的 Shell

现在，我们可以访问正在运行的容器的 shell，这将允许您从容器内部运行命令。这是通过 `exec` 命令完成的，如下所示：

```
docker exec -it ID /bin/bash
```

其中 ID 是正在运行的容器 ID 的前四个字符。然后，您应该会发现自己位于正在运行的容器的 bash 提示符下。假设您要升级软件。您可以使用以下命令执行此操作：

```
apt-get update
apt-get upgrade -y
```

升级完成后，您可以使用以下命令退出 shell：

```
exit
```

让我们简化这个过程。

## 从容器外部运行命令

由于 `exec` 命令，您不必先访问容器的 shell 即可运行命令。相反，您可以将命令发送到容器内部。让我们继续以更新和升级正在运行的 NGINX 容器为例。同样，我们需要此命令的容器 ID。

要更新和升级 NGINX 容器的软件（无需先访问容器），该命令将是：

```
docker exec ID apt-get update && apt-get upgrade
```

其中 ID 是容器 ID 的前四个字符。
在 Linux 中，`&&` 运算符很常见，它可以将命令串联在一起，使它们一个接一个地运行。

你可以使用此方法运行几乎任何命令。例如，你可以使用以下命令查看 NGINX 使用的 index.html 文件：

```bash
docker exec ID cat /usr/share/nginx/html/index.html
```

其中 ID 是容器 ID 的前四个字符。
让我们将一个新的 index.html 文件复制到正在运行的容器中，然后使用 exec 查看它。在你的主机上创建新文件：

```bash
nano index.html
```

在该文件中，粘贴以下内容：

```html
<!DOCTYPE html>
<html>
<body>

<h1>The New Stack</h1>
<p>Welcome to The New Stack</p>

</body>
</html>
```

保存并关闭文件。接下来，使用以下命令将文件复制到正在运行的 NGINX 容器：

```bash
docker cp index.html ID:/usr/share/nginx/html/
```

其中 ID 是正在运行的容器的 ID。
现在，我们可以使用以下命令查看文件的内容：

```bash
docker exec ID cat /usr/share/nginx/html/index.html
```

输出应如下所示：

```
Hello, New Stack
```

这就是你使用 Docker exec 命令的方式。使用此工具，你可以更好（更有效）地管理正在运行的 Docker 容器。

## Docker exec 命令的常见错误

以下是使用 docker exec 命令时可能发生的一些常见错误：

- **权限不足：** 运行 docker exec 命令的用户可能没有足够的权限来执行容器或访问其资源。
- **容器 ID 不正确：** 如果你使用不正确的容器 ID，可能会导致容器内命令执行失败。
- **命令未找到：** 如果你运行的命令未安装或在容器内不可用，则会失败并显示“command not found”错误。
- **容器已停止或退出：** 在已停止或退出的容器上运行 docker exec 命令将导致错误。
- **超时错误：** 如果命令在容器内执行时间过长，Docker 可能会超时并返回错误。
- **资源约束：** 资源不足（内存、CPU）的容器可能导致 docker exec 失败。
- **文件系统限制：** 运行写入容器文件系统外部的文件或修改敏感数据的命令时，权限和空间等限制可能会导致 Docker 出现错误或问题。
- **网络连接问题：** 如果容器未正确连接到网络接口或网络访问受限，docker exec 可能会失败。

## 常见问题解答

**问：exec 命令的目的是什么？**

答：exec 命令允许你在已部署的容器中运行命令，因此你可以与正在运行的容器进行交互。

**问：是否可以在不创建新容器的情况下使用 exec 命令？**

答：不可以，默认情况下，*docker exec* 命令需要一个正在运行的容器。 如果你想在现有容器的 shell 之外执行命令，你需要使用 *docker exec -it ID /bin/bash* 创建一个交互式会话。

**问：在 Docker exec 命令中指定容器 ID 的格式是什么？**

答：容器 ID 的前四个字符（例如，“1234”）可以用作命令的一部分。

**问：是否可以使用 exec 命令来更新现有容器中的依赖项？**

答：是的，你可以使用 *docker exec* 在正在运行的容器内运行 *apt-get update && apt-get upgrade* 等命令。

**问：如何查看 Docker exec 命令的输出？**

答：执行的命令的输出显示在你的终端中。 如果你想捕获输出以进行进一步处理或日志记录，请根据需要使用重定向运算符（例如，>，>>）。

**问：是否可以使用 exec 命令将多个命令链接在一起？**

答：是的，默认情况下，Docker 依次执行每个命令。 要一个接一个地执行一系列命令，而无需等待 shell 的输入，请在它们之间使用 `&&` 运算符（例如，*apt-get update && apt-get upgrade -y*）。

**问：如果在现有容器中运行失败的命令会发生什么？**

答：如果在现有容器中运行失败的命令，Docker 会退出并终止你的交互式会话。 为避免这种情况，请将 `-n` 选项与 *docker exec* 一起使用，这可以防止 Docker 等待输入（例如，*docker exec -it ID /bin/bash -n apt-get update &&*…）。

**问：是否可以使用 exec 命令在容器之间传递数据？**

答：不可以，默认情况下，Docker 不支持在容器内传递或重定向输出/输入。 要实现此功能，请使用 *docker run –rm -it <image> /bin/bash* 等工具，该工具创建一个没有持久性文件系统的隔离环境。

**问：如何退出 exec 命令启动的交互式会话？**

答：你可以使用 *exit* 命令或关闭终端来退出交互式会话。

## 故障排除提示：

- 如果 Docker 无法检测到正在运行的容器，请检查它是否确实处于活动状态。
- 确保你具有访问和管理容器的足够权限。
- 验证容器中使用的镜像是否有效并且存在于你的本地缓存中。