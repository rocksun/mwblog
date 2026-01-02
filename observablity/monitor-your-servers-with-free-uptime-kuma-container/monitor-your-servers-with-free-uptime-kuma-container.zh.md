如果您运行着一组服务器，无论是[家庭网络](https://thenewstack.io/containerized-apps-for-your-home-network/)实验室还是为您的业务提供支持的服务器，您都会想知道每个服务器或服务的状态。

如果您有很多服务器需要定期监控，这可能会非常麻烦。想象一下，如果您必须单独登录每台服务器来检查它们的状态。

或者，也许您有几个[Docker 容器](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/)需要密切关注，以确保它们正常运行。如果它们宕机，您甚至可能希望收到警报。

您会怎么做？

您可以选择一个易于使用的 Docker 容器：[Uptime Kuma](https://uptime.kuma.pet/)。

Uptime Kuma 可以监控多种服务，包括 ping、HTTP(S)、[MySQL](https://thenewstack.io/insert-data-into-a-mysql-database-via-a-python-script/)、TCP 端口、SMTP、SNMP、gRPC(s)、DNS、Docker 容器等等。大多数服务设置都相当简单，而且 UI 设计得非常好。

我将向您展示如何安装 Uptime Kuma 并添加一些主机进行监控。

## 您需要什么

要使用 Uptime Kuma，您需要一台支持 Docker 的宿主服务器（或桌面）以及一些要监控的主机。如果您在 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 上使用 Uptime Kuma，您需要一个具有 sudo 权限的用户才能安装 Docker。像往常一样，我将在 Linux（具体来说是 Ubuntu Server 24.04）上演示这一点。如果您的宿主操作系统不同，请确保相应地更改安装说明。如果您已经安装了 Docker，请跳到 Uptime Kuma 部署部分。

准备好了吗？我们开始吧。

## 安装 Docker

### 1. 安装依赖项

第一步是使用以下命令安装必要的依赖项：

```bash
sudo apt update
sudo apt install ca-certificates curl gnupg
```

### 2. 添加官方 Docker GPG 密钥

接下来要做的就是添加官方 Docker GPG 密钥。为此，请使用以下命令：

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

### 3. 添加正确的仓库

现在可以添加 Docker 仓库了，这通过以下命令完成：

```bash
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

完成此操作后，使用以下命令更新 apt：

```bash
sudo apt update
```

### 4. 安装 Docker

现在终于可以安装 Docker 了，这通过以下命令完成：

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 5. 将您的用户添加到正确的组

需要将您的用户添加到 Docker 组；否则，您将不得不以管理员权限运行 Docker，这可能导致安全问题。使用以下命令将您的用户添加到 Docker 组：

```bash
sudo usermod -aG docker $USER
```

注销并重新登录以使更改生效。

## 部署 Uptime Kuma

部署 Uptime Kuma 可以通过一个命令完成：

```bash
docker run -d --restart=always -p 3001:3001 --name uptime-kuma louislam/uptime-kuma:1
```

但是，在此之前，请考虑您是否要在该服务器上监控 Docker 容器。如果需要，您必须将 `/var/run/docker.sock` 绑定到您的 Uptime Kuma 容器，这通过以下命令完成：

```bash
docker run -d --restart=always -p 3001:3001 -v /var/run/docker.sock:/var/run/docker.sock --name uptime-kuma louislam/uptime-kuma:1
```

给 Uptime Kuma 一点时间启动，然后将浏览器指向 http://SERVER:3001（其中 SERVER 是宿主服务器的 IP 地址）。

首先要做的是选择您的语言和您想使用的数据库（图 1）。我选择嵌入式 MariaDB，因为它是最简单的途径。

![](https://cdn.thenewstack.io/media/2025/12/e343f97e-screenshot-2025-12-24-at-10.54.46-am.png)

图 1：明智地选择您的数据库。

然后系统会提示您创建一个新的管理员帐户（图 2）。

![](https://cdn.thenewstack.io/media/2025/12/2cd04eff-screenshot-2025-12-24-at-11.00.47-am-638x1024.png)

图 2：确保为该帐户使用一个强大/独特的密码。

设置管理员用户后，您将进入 Uptime Kuma 仪表板（图 3），在那里您可以开始添加要监控的主机/服务。

![](https://cdn.thenewstack.io/media/2025/12/d9d2e3ab-screenshot-2025-12-24-at-1.27.39-pm-scaled.png)

图 3：我已经添加了一些要监控的主机（其中一个已宕机……天呐！）。

## 添加主机

现在我将向您展示如何为 Docker 容器添加监控。我将添加的 Docker 容器与 Uptime Kuma 托管在同一服务器上（因为我尚未弄清楚如何使其与远程容器一起工作）。

要监控容器，您首先需要找到容器 ID，这可以使用以下命令找到：

```bash
docker ps -a
```

复制您要监控的容器的完整 ID。

接下来，返回 Uptime Kuma 仪表板，点击左上角的“添加新监控项”（Add New Monitor）。在弹出的窗口中（图 4），您需要填写以下信息：

* 监控类型：Docker 容器。
* 友好名称：一个易于理解的名称。
* 容器名称/ID：要监控的容器 ID。
* Docker 主机：您必须点击“+”按钮，在“友好名称”空间中输入 `localhost`，然后点击“保存”。

![](https://cdn.thenewstack.io/media/2025/12/a1c65782-screenshot-2025-12-24-at-1.36.40-pm.png)

图 4：使用 Uptime Kuma 添加 Docker 容器进行监控。

点击“保存”，主机就添加成功了。您应该立即在仪表板上看到它。

这就是让 Uptime Kuma 启动并运行的要点。有了这个易于使用的工具，您可以添加任意数量的服务器和服务进行监控，这样您就不必单独登录这些机器，也不必支付专有、复杂监控系统的高昂费用。