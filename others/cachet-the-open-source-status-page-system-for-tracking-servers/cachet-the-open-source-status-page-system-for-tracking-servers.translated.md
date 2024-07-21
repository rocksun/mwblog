# Cachet：用于跟踪服务器的开源状态页面系统

![用于 Cachet：用于跟踪服务器的开源状态页面系统的特色图片](https://cdn.thenewstack.io/media/2024/07/51991656-cachet-1024x768.png)

您是否管理着[大量服务器](https://thenewstack.io/secure-remote-linux-server-logins-with-ssh-key-authentication/)和/或[桌面](https://thenewstack.io/project-bluefin-a-linux-desktop-for-serious-developers/)，并且一直在寻找一种方法来跟踪它们的状态？根据您管理的机器数量，这项任务可能非常具有挑战性。您知道哪些机器正在运行吗？那些性能不佳或出现故障的机器呢？

您可能有一个团队，并且已将特定成员分配到管理某些设备。即使这样，您也[需要一个集中位置，以便您和您的团队](https://thenewstack.io/why-a-dataops-team-needs-a-database-reliability-engineer/)可以查看每台机器的状态。

这就是[Cachet](https://cachethq.io/)之类的工具发挥作用的地方。该系统允许您（和您的团队）标记机器并根据需要更改其状态。例如，假设您的备份 Web 服务器性能不佳。您可以登录 Cachet 并将其标记为这样，以便每个人都知道机器需要关注。

请注意，Cachet 不是一个自动化系统。相反，这是一个手动选项，可以轻松地集中管理所有[您管理的机器](https://thenewstack.io/how-apache-airflow-better-manages-machine-learning-pipelines/)的状态。使用 Cachet，您可以跟踪维护、组件、事件，甚至可以[订阅团队成员以在创建事件](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/)或更新组件时接收电子邮件更新。

Cachet 非常方便，尤其是在您管理的机器数量增长到难以跟踪的程度时。

让我带您了解 Cachet 的安装和运行过程。

## 您需要什么

我将在 Ubuntu Server 22.04 上演示此过程，因此您需要一个该操作系统的实例和一个具有 sudo 权限的用户。就是这样。让我们开始吧。

## 安装 Docker CE

我们首先要做的就是在我们的 Linux 服务器上安装[Docker CE](https://thenewstack.io/docker-delivers-docker-extensions-docker-desktop-for-linux/)。为此，请登录您的机器，并首先使用以下命令安装必要的依赖项：

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
```

接下来，使用以下命令添加所需的 Docker GPG 密钥：

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

使用以下命令添加[Docker 存储库](https://thenewstack.io/simplify-linux-and-docker-command-lines-with-bash-completion/)：

```bash
sudo add-apt-repository "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

使用以下命令更新 apt：

```bash
sudo apt-get update
```

安装 Docker CE：

```bash
sudo apt install docker-ce -y
```

Docker 将安装，并且服务将启动。然后，您需要使用以下命令将您的用户添加到 docker 组：

```bash
sudo usermod -aG docker $USER
```

注销并重新登录以[使更改生效](https://thenewstack.io/ci-observability-for-effective-change-management/)。

## 使用 Docker 部署 Cachet

我们首先使用以下命令从官方 GitHub 页面克隆 Cachet 源代码：

```bash
git clone https://github.com/cachethq/Docker.git cachet-docker
```

使用以下命令更改到新创建的目录：

```bash
cd cachet-docker
```

接下来，使用以下命令打开**docker-compose.yml**文件进行编辑：

```bash
nano docker-compose.yml
```

在该文件中，查找以下行：

```yaml
ports:- 80:8000
```

将其更改为：

```yaml
ports:- 8000:8000
```

保存并关闭文件。

现在可以使用以下命令构建应用程序：

```bash
docker compose build
```

构建完成后，使用以下命令启动容器：

```bash
docker compose up
```

在部署过程中，您会发现有关 APP_KEY 的错误（您可能需要向上滚动才能看到它）。该错误还将包含安装所需的自动生成的密钥。复制该密钥，然后使用 Ctrl-C 键组合重新获取您的终端提示符。

再次使用以下命令打开 docker-compose.yml 文件：

```bash
nano docker-compose.yml
```

在该文件中，查找以以下内容开头的行：

```yaml
APP_KEY=
```

您需要将您的密钥粘贴到这里。密钥将以 base64 开头，并以 *=* 结尾。

保存并关闭文件。

使用以下命令关闭容器：

```bash
docker compose down
```

容器停止后，使用以下命令以分离模式重新启动它：

```bash
docker compose up -d
```

[给容器](https://thenewstack.io/giving-container-innovation-a-further-boost-with-bottlerocket/)一些时间启动。片刻之后，打开一个 Web 浏览器，并将其指向 http://SERVER:8000（其中 SERVER 是托管服务器的 IP 地址）。您将看到初始设置页面（图 1）。

-

图 1：第一个 Cachet 设置页面。
确保选择 Cachet 驱动程序、队列驱动程序和会话驱动程序的数据库。之后，选择一个邮件驱动程序，然后配置发件邮件（如果需要，可以使用 Gmail SMTP）。完成设置后，单击下一步。

在结果页面（图 2）上，配置站点名称、域名、时区和语言，然后单击下一步。

<br>

- 图 2：状态页面设置屏幕。

在最终的设置页面（图 3）上，创建一个管理员用户名。

<br>

- 图 3：为 Cachet 添加初始管理员用户。

单击转到仪表板，系统将提示您使用新的管理员用户登录。成功验证后，您将进入 Cachet 仪表板页面（图 4），您可以在此处开始添加组件（任何需要跟踪其状态的硬件）、创建团队和团队成员等等。

<br>

- 图 4：主要的 Cachet 仪表板页面。

就是这样。您现在拥有一个用于跟踪公司内硬件状态的网站。Cachet 应该能很好地为您服务，但您需要确保定期使用它（因为，它是一个手动系统）。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。