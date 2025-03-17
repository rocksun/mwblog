# 使用 Nitric 和 OpenAI 构建一个 Serverless Meme 生成器

![Featued image for: Building a Serverless Meme Generator With Nitric and OpenAI](https://cdn.thenewstack.io/media/2025/03/2dd1a3d4-meme-1024x576.jpg)

如果你对 serverless 的理解有限，你可能会觉得你错过了它的全部潜力。更深入地掌握你可用的工具可以释放新的生产力水平。

你可能正在跨不同的云提供商构建和托管产品，但仍然想知道幕后的一切是如何运作的。

最近，关于 [serverless](https://thenewstack.io/serverless/) 的讨论很多，你可能错过了充分理解它含义的机会。让我们分解一下，什么才算得上是真正的 serverless 云功能，以及它与仅仅是基于云或云原生有何不同。

**期望内容：**

- 我们将使用 Nitric 构建一个 meme 生成器，Nitric 是后端框架，并使用 OpenAI DALL-E 模型进行图像生成。
- 使用 Nitric 将我们的代码部署到 serverless 平台。

**奖励**——我们还将构建这个应用程序的前端，以便与我们的后端 API 交互。这是一个我们最终实现的示例演示：

**专家怎么说？**

理解这个主题的最好方法之一是听取行业专家的意见。让我们来看看一些已经存在的最好的想法。

以下是一些推文和帖子：

来自 DynamoDB 的创建者，[Rick Houlihan](https://x.com/houlihan_rick/status/1312386662262079490)…

来自 [Pulumi](https://www.pulumi.com/what-is/what-is-serverless/)…

[“Serverless 指的是一种云计算执行模型](https://thenewstack.io/running-ai-models-without-gpus-on-serverless-platforms/)，其中云提供商自动管理基础设施，从而将服务器管理的复杂性从开发人员那里抽象出来。在 serverless 架构中，开发人员只专注于编写 [单个功能的代码](https://thenewstack.io/can-ai-generate-functional-terraform/) 或服务，而无需关心服务器的配置、扩展或维护。”

总而言之，serverless 的目标是让 [开发人员专注于应用程序代码](https://thenewstack.io/how-to-code-first-with-design-first-benefits/) 和业务逻辑。你永远不必担心管理底层服务器。云提供商将在幕后处理服务器的配置、自动扩展或监控。

<aside>
💡

*术语“serverless”并不意味着不涉及服务器。之所以称之为“serverless”，是因为从开发人员的角度来看，没有可见的服务器需要管理。*
</aside>

**为什么使用 Nitric？**

以下是我们使用 Nitric 使事情变得更容易的原因：

- Nitric 通过为我们处理复杂的云配置，帮助我们以更简单的方式构建代码。
- Nitric 将 [代码转换为云平台](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/)（如 [AWS](https://aws.amazon.com/?utm_content=inline+mention)/[Google](https://cloud.google.com/?utm_content=inline+mention)Cloud Platform (GCP)/[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)Azure）所期望的形式。
- 云提供商负责实际的服务器管理。

**先决条件**

确保你在开发环境中设置了以下工具、帐户和配置。

**开发环境**

**所需软件**

- Node.js (v18.0.0 或更高版本)
- npm (v9.0.0 或更高版本) 或 Yarn (v1.22.0 或更高版本) 或 pnpm (v.9.12.3 或更高版本)
- [Git](https://git-scm.com/)(v2.30.0 或更高版本)
- Visual Studio Code (推荐) 或你喜欢的 IDE
- [Docker Desktop](https://docs.docker.com/get-started/get-docker/)(使用 Nitric 进行本地开发时需要)

**命令行工具**

- 安装 AWS CLI

```
# For Macos
brew install awscli
#For Linux
curl "<https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip>" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**Nitric CLI (最新版本)**

Nitric 依赖于 [git](https://git-scm.com/) 和 [Docker](https://docs.docker.com/get-started/get-docker/) 的功能来帮助检索插件、容器化和部署你的应用程序。请按照链接访问每个插件的官方实现。

```
#On Macos
brew install nitrictech/tap/nitric
#On Linux
curl -L "<https://nitric.io/install?version=latest>" | bash
#On Windows
scoop bucket add nitric <https://github.com/nitrictech/scoop-bucket.git>
scoop install nitric
```

安装完成后，我们可以将其升级到最新版本。

```
#On Macos
brew upgrade nitric
#On Linux
curl -L "<https://nitric.io/install?version=latest>" | bash
#On Windows
scoop update nitric
```

部署插件有它们自己的要求，我们将在本指南的结尾部署我们的应用程序时查看它们。

**所需帐户**

我们将使用 AWS 作为我们的云提供商。

- AWS 帐户
- 创建一个免费帐户，网址为
*   [aws.amazon.com](http://aws.amazon.com/). - 使用此[指南](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.IAM.html)设置具有编程访问权限的身份和访问管理 (IAM) 用户。 - 您可以附加“AmazonAPIGatewayAdministrator and AWSLambdaFullAccess”以进行编程访问，然后检索密钥和访问密钥并将其保存在安全的地方，以便以后可以轻松访问。
*   在以下位置创建一个免费帐户
*   这是设置编程访问权限时的最终屏幕。 确保下载 CSV 文件或复制访问密钥或密钥。
*   OpenAI 帐户
*   在以下位置注册
    [platform.openai.com](http://platform.openai.com). - 生成 API 密钥并将其保存在安全的地方，以便您可以在下一步中访问它。
*   确保您有积分或付费订阅

<aside>
💡

*请注意，如果您是 2023 年 4 月 6 日之前注册使用 DALL-E 的早期采用者，OpenAI 才会给您免费积分。请在此处查看：https://help.openai.com/en/articles/6399305-how-dall-e-credits-work.*

*如果这对您来说是一个障碍，请不要担心。您也可以使用 https://docs.nebius.com/studio/inference，它将为您提供欢迎积分并访问以下文本到图像模型：*

`black-forest-labs/flux-schnell`

`black-forest-labs/flux-dev`

`stability-ai/sdxl`

*这将与我们的指南配合良好，因为它们也使用 OpenAI Node SDK。*

</aside>

**开始使用**

我们将首先克隆一个包含我们前端基本组件设置的入门 repo。

```
git clone --branch starter --single-branch <https://github.com/daveclinton/nitric-meme-generator.git>
```

接下来，在您选择的编辑器中打开项目。

```
cd nitric-meme-generator
```

在此目录中，我们将创建我们的 Nitric 后端，并确保您有一个新目录，其中包含一个 src 目录和一个 `package.json`。

```
nitric new backend ts-starter
```

导航到新项目目录并安装依赖项：

```
cd backend
npm install
npm install openai util dotenv
```

您的项目应具有以下结构：

**处理我们的后端**

我们将需要在 `backend/services/api.ts` 文件中开始处理我们的应用程序逻辑。

删除所有现有代码并导入我们的项目所需的必要模块，如果您在初始设置中没有安装其中一些模块，请在此目录中安装它们。

在下面的代码中：

*   Nitric SDK 用于使用 Nitric 创建 API。
*   我们还使用 OpenAI 的官方库与其 API 进行交互；`zlib` 和 `promisify` 用于压缩我们从 OpenAI 获得的数据，该数据采用 base64 编码格式。
*   `dotenv/config` 自动从`.env` 文件加载变量。

```typescript
import { api } from "@nitric/sdk";
import OpenAI from "openai";
import zlib from "zlib";
import { promisify } from "util";
import "dotenv/config";
```

**定义常量**

*   在此代码中，我们使用 `promisify` 将 `zlib.gzi` 转换为基于 Promise 的函数以异步运行。
*   `TIMEOUT_MILLIS`：我们使用它将 OpenAI 调用的超时设置为 55 秒。
*   `DEFAULT_IMAGE_SIZE`：这将是生成的图像的默认图像分辨率。

```typescript
const gzip = promisify(zlib.gzip);
const TIMEOUT_MILLIS = 55 * 1000;
const DEFAULT_IMAGE_SIZE = "1024x1024";
```

**配置 CORS 标头**

```typescript
const CORS_HEADERS = {
  "Access-Control-Allow-Origin": ["*"],
  "Access-Control-Allow-Methods": ["POST", "OPTIONS"],
  "Access-Control-Allow-Headers": ["Content-Type", "Accept-Encoding"],
  "Access-Control-Max-Age": ["86400"],
};
```

在以下标头中，我们允许跨域请求，从而使任何域/网站都可以使用我们的 API。 但您可以在生产环境中更改此设置以确保安全。 并且我们还确保只有 POST 请求被发送到此端点。

**初始化 OpenAI 客户端**

在此步骤中，我们现在将创建一个 `.env` 文件并添加我们的 `OPENAI_API_KEY="your_api_key_from_open_ai"`。 此 env 文件应位于我们后端文件夹的根目录中。

然后包含以下代码以使用已定义的环境变量初始化 OpenAI 的 API 客户端。

```typescript
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY,});
```

**定义 Typescript 类型**

*   `ProviderKey` 类型确保 `openai` 是我们使用的唯一提供程序，但如果您想在此项目中拥有更多选项，则可以添加更多。 其他可用的提供程序有 `replicate`、`Nebius`、`fireworks` 等等。
*   `OpenAIModelId` 会将我们的模型选择限制为 OpenAI 上唯一可用的模型，即 `dall-e-2` 和 `dall-e-3`。
*   `GenerateImageRequest` 将指导我们的请求正文到 OpenAI 或我们选择的任何其他提供程序的形状。

```typescript
export type ProviderKey = "openai";
export type OpenAIModelId = "dall-e-2" | "dall-e-3";

interface GenerateImageRequest {
  prompt: string;
  provider: ProviderKey;
  modelId: OpenAIModelId;
}
```

**创建一个超时包装器**

接下来，我们创建一个超时函数，该函数将确保我们的请求在 55 秒后超时（如果它们响应时间过长）。
```markdown
```javascript
const withTimeout = <T>( promise: Promise<T>, timeoutMillis: number): Promise<T> => { return Promise.race([ promise, new Promise<T>((_, reject) => setTimeout( () => reject(new Error(`Request timed out after ${timeoutMillis}ms`)), timeoutMillis ) ), ]);};
```

**验证我们的请求**

在此代码中，我们使用它来验证我们的请求是否为有效的 OpenAI 模型。提供者还必须是 OpenAI，并且它不接受空提示，因此我们可以防止进行保证会失败的 API 调用。

```javascript
const validateRequest = ( requestBody: GenerateImageRequest, requestId: string): { isValid: boolean; error?: string } => { if (!requestBody.prompt?.trim()) { console.error(`[${requestId}] Missing or empty prompt`); return { isValid: false, error: "Prompt is required" }; } if (requestBody.provider !== "openai") { console.error(`[${requestId}] Invalid provider: ${requestBody.provider}`); return { isValid: false, error: "Only OpenAI provider is supported" }; } if (!["dall-e-2", "dall-e-3"].includes(requestBody.modelId)) { console.error(`[${requestId}] Invalid model ID: ${requestBody.modelId}`); return { isValid: false, error: "Invalid model ID" }; } return { isValid: true };};
```

**创建 API 端点并处理 CORS**

```javascript
const imageApi = api("image-api");imageApi.options("/generate-image", async (ctx) => { ctx.res.headers = CORS_HEADERS; ctx.res.status = 204; return ctx;});
```

**将所有内容放在一起，以便我们可以进行 API 调用**

*   这就是现在将处理图像生成请求的逻辑。它还将准备和验证我们的请求正文；如果失败，它将返回 500 服务器错误。

```javascript
imageApi.post("/generate-image", async (ctx) => { ctx.res.headers = { ...CORS_HEADERS, "Content-Encoding": ["gzip"], "Content-Type": ["application/json"], }; const requestId = Math.random().toString(36).substring(7); console.log(`[${requestId}] Starting image generation request`); let requestBody: GenerateImageRequest; try { requestBody = ctx.req.json() as GenerateImageRequest; console.log(`[${requestId}] Request body:`, { prompt: requestBody.prompt?.substring(0, 50) + "...", provider: requestBody.provider, modelId: requestBody.modelId, }); } catch (error) { console.error(`[${requestId}] Failed to parse request body:`, error); ctx.res.status = 400; ctx.res.body = await gzip( JSON.stringify({ error: "Invalid JSON in request body" }) ); return ctx; } const validation = validateRequest(requestBody, requestId); if (!validation.isValid) { ctx.res.status = 400; ctx.res.body = await gzip(JSON.stringify({ error: validation.error })); return ctx; } if (!process.env.OPENAI_API_KEY) { console.error(`[${requestId}] OPENAI_API_KEY is not set`); ctx.res.status = 500; ctx.res.body = await gzip( JSON.stringify({ error: "OpenAI API key not configured" }) ); return ctx; } const startstamp = performance.now(); console.log(`[${requestId}] Sending request to OpenAI API`); try { const imageResponse = await withTimeout( openai.images.generate({ model: requestBody.modelId, prompt: requestBody.prompt, size: DEFAULT_IMAGE_SIZE, response_format: "b64_json", n: 1, }), TIMEOUT_MILLIS ); const elapsed = ((performance.now() - startstamp) / 1000).toFixed(1); if (!imageResponse.data?.[0]?.b64_json) { throw new Error("Response missing image data"); } console.log(`[${requestId}] Request completed successfully`); ctx.res.status = 200; const responseData = { provider: requestBody.provider, image: imageResponse.data[0].b64_json, elapsed: `${elapsed}s`, }; ctx.res.body = await gzip(JSON.stringify(responseData)); return ctx; } catch (error) { console.error(`[${requestId}] Error generating image:`, error); ctx.res.status = 500; ctx.res.body = await gzip( JSON.stringify({ error: `Error generating image: ${error.message}` }) ); return ctx; }});export default imageApi;
```

此 API 验证用户输入，向 OpenAI 发送请求并压缩响应以提高性能。它也是安全、高效且可扩展的。

**启动我们的项目并发出第一个请求**

接下来，我们需要测试我们的端点。

使用以下命令运行项目：

```bash
%nitric start
```

您应该被重定向到 Nitric 仪表板，您可以在其中发出请求、检查日志等。

或者您可以使用 curl 发出请求，如下所示并获得您的响应：

```bash
curl -X POST <http://localhost:4001/generate-image> \
 -H "Content-Type: application/json" \
 -H "Accept-Encoding: gzip" \
 -d '{ "prompt": "A futuristic cityscape at night", "provider": "openai", "modelId": "dall-e-3" }'
```

**部署后端应用**
现在我们已经实现了 OpenAI 集成并测试了它的工作，您可以将其部署到一个或多个云平台。我们将使用 Nitric [Provider Plugins](https://nitric.io/docs/get-started/foundations/deployment) 来部署应用程序，而无需更改应用程序中的代码。

一开始，您配置了 AWS 的访问权限，并将密钥保存在安全的地方。现在我们需要创建一个新的堆栈文件来代表我们的部署目标。

首先，我们需要通过运行以下命令来配置 AWS CLI：

```
aws configure
```

系统将提示您输入访问密钥、密钥和默认区域名称 `us-east-1`。
然后回到我们的项目，通过运行以下命令来配置我们的堆栈：

```
nitric stack new
```

这将创建一个名为 `nitric.dev.yaml` 的新文件。编辑此文件并设置任何剩余的配置。

```yaml
provider: nitric/aws@1.17.0
region: us-east-1
```

现在您可以使用以下命令构建和部署您的项目：

```
nitric up
```

通常，部署完成后，您的服务的基本 URL 将显示在 CLI 输出中。

**奖励工作**

本节是可选的。您可以决定使用您自己的自定义前端，但我们准备了一个您可以使用的示例。这是我们前端的 UI，您可以在[这里](https://github.com/daveclinton/nitric-meme-generator)试用：

要将此前端用于您的应用程序，请导航回根项目并创建一个环境变量，并添加您部署的应用程序的基本 URL，或者如果您在本地运行它，您可以添加以下链接：

```
cd ..
touch .env
```

```
NEXT_PUBLIC_API_BASE_URL="app-url.com"
#local
NEXT_PUBLIC_API_BASE_URL="<http://localhost:4001>"
```

然后，一旦您添加了文件，您可以继续安装依赖项并运行您的项目并进行测试。

```
npm install
npm run dev
```

您可以在 [http://localhost:3000/](http://localhost:3000/) 访问您前端应用程序的本地服务器，该服务器将在运行上述命令后显示在您的终端上。

<aside>
💡
前端代码已准备好部署到 Vercel。我们只是在启动器中添加了一个 vercel.ignore，它将后端排除在最终构建文件夹 dist 中。
</aside>

**重点是什么？**

在构建此项目之后，您已经了解到无服务器不是正确或错误。相反，它是一种使服务更易于使用的设置。通过消除无差别的繁重工作，开发人员可以更加专注于构建他们的应用程序。

现在，该项目可以轻松地部署到更多的云平台。干杯 🔥。

最终代码在这里：[https://github.com/nitrictech/examples/tree/main/v1/nitric-meme-generator](https://github.com/nitrictech/examples/tree/main/v1/nitric-meme-generator)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)