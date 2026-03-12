每次使用AI时，我总是选择本地安装的实例。原因有二。首先，当我使用本地安装的AI时，我不会从已经需求巨大的电网中获取电力。其次，我始终可以信任我的本地AI来保护我的[隐私](https://thenewstack.io/will-data-privacy-die-in-the-age-of-genai/)。

当使用AI的本地实例时，您的信息（包括您的查询）不会与第三方共享。它是百分之百私密的。

您可能会认为在您的家庭实验室中设置本地AI服务器可能是一个巨大的挑战。事实并非如此。实际上，这非常容易，我将向您展示如何完成。最后，您将拥有一个可以通过网络浏览器访问，或通过将您喜爱的[AI图形用户界面](https://thenewstack.io/generative-ui-for-devs-more-than-ai-assisted-design/)（例如 Ollama、Alpaca 或 [Msty](https://msty.ai/)）连接到服务器的AI服务器。

所以，事不宜迟，让我们开始设置吧。

## 您将需要什么

您唯一需要的是一个运行中的 [Debian](https://thenewstack.io/check-out-debian-the-mother-of-all-linux-distributions/) 或 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) Server 实例，以及一个具有 sudo 权限的用户。

## 将您的 Debian 用户添加到 sudo 组

默认情况下，您的标准用户不是 Debian 上 sudo 组的成员。要成功使用 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)（用于部署 [WebUI](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)），您必须进行此更改。

要将您的用户添加到 Debian 上的 Docker 组，首先使用以下命令切换到 root 用户：

```
sudo su-
```

切换到 root 用户后，使用以下命令将您的标准用户添加到 Docker 组：

```
usermod -aG docker USER
```

其中 USER 是要添加的用户的名称。

使用以下命令退出 root 用户：

```
exit
```

退出您的标准用户账户并重新登录，以便更改生效。

## 安装 Ollama

接下来，我们将安装 Ollama，可以使用以下命令完成：

```
curl -fsSL https://ollama.com/install.sh | sh
```

完成后，让我们下载一个较小的 LLM（用于测试目的）。您以后总是可以下载更大的 LLM。我们将使用以下命令拉取 llama3.2 模型：

```
ollama pull llama3.2
```

模型成功拉取后，通过运行以下命令确保其正常工作：

```
ollama run llama3.2
```

如果您看到 Ollama 提示符，则表示一切正常。使用以下命令退出提示符：

```
/bye
```

### 配置 Ollama

接下来，我们需要配置 Ollama 以接受远程连接。我们将通过 systemd 来实现。使用以下命令打开 systemd Ollama 初始化文件：

```
sudo nano /etc/systemd/system/ollama.service
```

在 `[Service]` 部分的底部，添加以下内容：

```
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

保存并关闭文件。

使用以下命令重新加载 Systemd 守护程序：

```
sudo systemctl daemon-reload
```

使用以下命令重新启动 Ollama 服务：

```
sudo systemctl restart ollama
```

此时，Ollama 可以通过服务器的 IP 地址从您的局域网上的远程机器访问。如何建立连接将取决于您使用的应用程序。

## 使用 Docker 部署 WebUI

接下来，我们将部署 WebUI，以便您可以通过网络浏览器与您的 [LLM](https://thenewstack.io/introduction-to-llms/) 进行交互。为此，我们将使用 WebUI。在此之前，我们必须安装 Docker。以下是安装 Docker CE 的步骤：

使用以下命令添加必要的 GPG 密钥：

1.  `sudo apt-get update`
2.  `sudo apt-get install ca-certificates curl`
3.  `sudo install -m 0755 -d /etc/apt/keyrings`
4.  `sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc`
5.  `sudo chmod a+r /etc/apt/keyrings/docker.asc`

使用以下命令添加官方 Docker 仓库：

1.  `echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo “${UBUNTU_CODENAME:-$VERSION_CODENAME}”) stable” | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
2.  `sudo apt-get update`

使用以下命令安装 Docker：

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

使用以下命令测试您是否可以使用 Docker：

```
docker ps -a
```

您应该看到一个空的 Docker 容器列表；如果是这样，您就可以部署了。

要使用 Docker 部署 WebUI，命令是：

```
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

请记住，如果您的机器已经在使用端口 3000，您会希望更改它。

给容器一点时间完成部署。在我的实例中，大约需要两分钟。您可以使用以下命令检查部署状态：

```
docker ps -a
```

当容器状态显示为 *healthy* 时，它就可以访问了。

## 访问 WebUI

要访问 Docker 的 WebUI 实例，请打开网页浏览器并指向 http://SERVER:3000（其中 SERVER 是托管服务器的 IP 地址）。您应该会看到 WebUI 主页（**图 1**）。

![](https://cdn.thenewstack.io/media/2026/03/f677f438-webui1.jpg)

**图 1：** 您已准备好开始使用 WebUI。

点击底部中间的右指向箭头，在随后的页面（**图 2**）中，输入所需信息以创建管理员账户。

![](https://cdn.thenewstack.io/media/2026/03/1f7d13a7-webui2.jpg)

**图 2：** 只需一点信息，您就可以开始查询了。

然后您将看到查询页面。在该页面上，您会发现您使用 Ollama 拉取的 LLM 不可用。因此，点击左上角的模型下拉菜单，然后您需要禁用 OpenAI 实例，然后将本地地址更改为 http://SERVER:11434（其中 SERVER 是您服务器的 IP 地址）。

您现在可以转到“新聊天”选项卡并运行您的第一个查询。

恭喜，您现在拥有一个可以从家庭实验室局域网上的任何机器访问的本地 AI 实例。