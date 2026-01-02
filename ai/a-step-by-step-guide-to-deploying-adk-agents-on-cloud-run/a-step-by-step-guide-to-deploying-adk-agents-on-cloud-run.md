
<!--
title: 在 Cloud Run 上部署 ADK 代理：分步指南
cover: https://cdn.thenewstack.io/media/2025/12/97c7b265-getty-images-ya49u1qljbi-unsplash2.jpg
summary: 本文介绍了使用adk deploy cloud_run命令将Google ADK代理部署到Cloud Run。通过此教程，你可以将AI代理部署为生产就绪的服务，并安全管理API密钥。
-->

本文介绍了使用adk deploy cloud_run命令将Google ADK代理部署到Cloud Run。通过此教程，你可以将AI代理部署为生产就绪的服务，并安全管理API密钥。

> 译自：[A Step-by-Step Guide To Deploying ADK Agents on Cloud Run](https://thenewstack.io/a-step-by-step-guide-to-deploying-adk-agents-on-cloud-run/)
> 
> 作者：Janakiram MSV

在近期对 [Google Agent Development Kit](https://thenewstack.io/what-is-googles-agent-development-kit-an-architectural-tour/) (ADK) 的参观中，我带你了解了使用 ADK 构建 AI 代理的三种方法：Python、YAML 和 Visual Builder。虽然本地开发非常适合原型设计，但生产就绪的代理需要部署到可以扩缩并为真实用户提供服务的环境中。

Google Cloud Run 是 ADK 代理的天然之选。作为一个完全托管的无服务器平台，它处理基础设施问题，让你专注于代理逻辑。这种部署方式之所以特别优雅，是因为 ADK 内置了 `adk deploy cloud_run` 命令，该命令可以在一个步骤内打包你的代理、构建容器镜像、将其推送到 Artifact Registry，并将其部署到 Cloud Run。

在本教程中，我将指导你如何将一个天气和时间代理部署到 Cloud Run，并使用 Google Secret Manager 进行安全的 API 密钥管理。学完本教程后，你将拥有一个可通过公共 URL 访问的生产就绪代理，并且 ADK Web UI 已启用，用于交互式测试。

## 理解部署架构

在深入实施之前，让我们先了解一下将 ADK 代理部署到 Cloud Run 时会发生什么。

`adk deploy cloud_run` 命令自动化了多项复杂操作。它分析你的项目结构和依赖项，以生成优化的 Docker 镜像。然后，该镜像被推送到 Google Artifact Registry，这是一个位于你的 Google Cloud 项目内的安全容器仓库。最后，Cloud Run 预置一个无服务器实例来运行你的代理；它具有自动扩缩、HTTPS 和 IAM 集成功能。

`--with_ui` 标志非常方便，因为它将 ADK Web 开发 UI 与代理的 API 服务器捆绑在一起，为你提供一个交互式界面，可以直接在浏览器中测试对话。

## 先决条件

开始之前，请确保你已具备以下条件：

*   已安装 Python 3.10 或更高版本。
*   已安装并配置 Google Cloud SDK (gcloud)。
*   已启用结算功能的 Google Cloud 项目。
*   已启用以下 API：Cloud Run、Artifact Registry、Secret Manager 和 Vertex AI。
*   来自 Google AI Studio 的 Google API 密钥（用于 Gemini 访问）。

## 第 1 步：设置项目结构

让我们创建具有所需目录结构的代理项目。ADK 期望特定的布局以确保部署正常工作。

为你的代理创建一个新目录：

```
mkdir weather_time
cd weather_time
```

ADK 要求你的代理目录中包含三个文件：`__init__.py`、`agent.py` 和 `requirements.txt`。部署工具会在你的代理代码中查找名为 `root_agent` 的变量——此命名约定是强制性的。

创建 `__init__.py` 文件：

```python
from . import agent
```

此文件将目录标记为 Python 包并导入代理模块。

## 第 2 步：构建代理

创建包含天气和时间工具的 `agent.py` 文件：

```python
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }




def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """


    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }


    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}




root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
```

该代理定义了两个工具：`get_weather` 和 `get_current_time`。请注意，每个函数都包含带有类型提示的完整文档字符串——ADK 利用这些信息帮助 LLM 理解何时以及如何调用每个工具。`root_agent` 变量是 ADK 部署命令将查找的入口点。

创建 `requirements.txt` 文件：

```
google-adk
```

你的项目结构现在应该如下所示：

`requirements.txt`  
`weather_time/`  
`├── __init__.py`  
`├── agent.py`

## 第 3 步：本地测试

在部署到 Cloud Run 之前，务必验证你的代理在本地环境中是否正常工作。在你的项目根目录中创建一个 .env 文件：

```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

用你的实际 Google AI Studio API 密钥替换占位符。

导航到父目录并在本地运行代理：

```
cd ..
adk run weather_time
```

使用以下提示测试代理：

`[user]: What's the weather in New York?`  
`[user]: What time is it in New York?`

确认代理响应正确后，输入 `exit` 退出本地会话。我们现在准备部署到 Cloud Run。

## 第 4 步：配置 Google Cloud Secret

生产部署绝不应硬编码 API 密钥。Google Secret Manager 为敏感凭据提供安全的存储和访问控制。我们将 API 密钥存储在那里。

首先，为你的 Google Cloud 项目设置环境变量：

```
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

从你的 API 密钥创建 secret：

```
echo $GOOGLE_API_KEY | \
    gcloud secrets create GOOGLE_API_KEY \
        --project=$GOOGLE_CLOUD_PROJECT \
        --data-file=-
```

Cloud Run 服务账号需要访问此 secret 的权限。授予 Secret Accessor 角色：

```
gcloud secrets add-iam-policy-binding GOOGLE_API_KEY \
    --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor" \
    --project=$GOOGLE_CLOUD_PROJECT
```

将 PROJECT\_NUMBER 替换为你的实际 Google Cloud 项目编号。你可以在 Google Cloud 控制台中找到它，或通过运行以下命令获取：

```
gcloud projects describe $GOOGLE_CLOUD_PROJECT --format="value(projectNumber)"
```

## 第 5 步：部署到 Cloud Run

配置好 secrets 后，我们就可以部署了。设置部署变量：

```
export AGENT_PATH="./weather_time"
export SERVICE_NAME="weather-time"
export APP_NAME="weather_time_app"
```

执行部署命令：

```
adk deploy cloud_run \
    --project=$GOOGLE_CLOUD_PROJECT \
    --region=$GOOGLE_CLOUD_LOCATION \
    --service_name=$SERVICE_NAME \
    --app_name=$APP_NAME \
    --with_ui \
    $AGENT_PATH
```

让我们分解一下这些参数：

| **参数** | **目的** |
| --- | --- |
| project | 指定用于部署的 Google Cloud 项目 |
| region | 设置 Cloud Run 区域（us-central1、europe-west1 等） |
| service\_name | 命名 Cloud Run 服务 |
| app\_name | ADK API 服务器的内部应用程序名称 |
| with\_ui | 包含用于交互式测试的 ADK Web UI |

在部署过程中，你可能会收到关于未经身份验证的访问提示。对于初始测试，你可以允许它 (y)；但对于生产部署，建议要求身份验证 (N)。

部署过程需要几分钟。完成后，你将看到类似以下的输出：

`Deployment successful!
Service URL: https://weather-time-xxxxx.us-central1.run.app`

## 第 6 步：测试已部署的代理

在浏览器中打开服务 URL。因为你包含了 `--with_ui` 标志，所以你会看到 ADK 开发者界面。这是你在本地开发期间使用的相同 UI，现在运行在 Cloud Run 上。

在右上角启用“Token Streaming”以提高响应速度。你现在可以与已部署的代理进行交互：

`[user]: Hello! What's the weather like in New York today?`  
代理应该使用 `get_weather` 工具进行响应，返回纽约的天气信息。

尝试后续操作：

`[user]: And what time is it there?`  
代理将调用 `get_current_time` 工具以提供纽约时区内的当前时间。

## 清理

为避免产生未来的费用，当你完成实验后，请删除 Cloud Run 服务：

```
gcloud run services delete $SERVICE_NAME \
    --region=$GOOGLE_CLOUD_LOCATION \
    --quiet
```

你可能还需要删除 secret：

```
gcloud secrets delete GOOGLE_API_KEY \
    --project=$GOOGLE_CLOUD_PROJECT \
    --quiet
```

## 展望未来

本教程演示了从本地 ADK 代理到生产 Cloud Run 部署的最快路径。`adk deploy cloud_run` 命令抽象了容器化复杂性，让你专注于代理逻辑，同时利用 Cloud Run 的无服务器可伸缩性。

在后续教程中，我们将探讨高级部署场景；包括将 ADK 代理连接到 MCP 服务器以进行外部工具集成，使用 Cloud SQL 实现会话持久性，使用顺序和并行编排模式部署多代理系统，以及配置 GPU 加速后端以运行 Gemma 等开放模型。

你在此处建立的基础——理解部署工作流、安全管理秘密以及使用 Web UI 进行测试——将在我们处理日益复杂的生产架构时助你一臂之力。敬请关注！