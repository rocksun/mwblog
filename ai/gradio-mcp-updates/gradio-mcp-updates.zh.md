# Gradio MCP 服务器的五大改进

[![Freddy Boulton's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1654278567459-626a9bfa03e2e2796f24ca11.jpeg)](/freddyaboulton)

[Gradio](https://gradio.app)

是一个用于创建 AI 驱动的 Web 应用程序的开源 Python 包。Gradio 符合

[MCP 服务器协议](https://modelcontextprotocol.io/introduction)

并为托管在

[Hugging Face Spaces](https://hf.co/spaces)

上的数千个 MCP 服务器提供支持。Gradio 团队正在

**大力押注**

Gradio 和 Spaces 是构建和托管 AI 驱动的 MCP 服务器的最佳方式。

为此，以下是我们自 [5.38.0](https://github.com/gradio-app/gradio/releases/tag/gradio%405.38.0) 版本以来添加到 Gradio MCP 服务器的一些重大改进。

## 无缝本地文件支持

如果您尝试使用需要文件作为输入（图像、视频、音频）的远程 Gradio MCP 服务器，您可能遇到过此错误：

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/MCPError.png)

发生这种情况是因为 Gradio 服务器托管在不同的机器上，这意味着任何输入文件都必须通过公共 URL 访问，以便可以远程下载它们。

虽然有很多方法可以在线托管文件，但它们都会在您的工作流程中增加一个手动步骤。在 LLM 代理时代，我们不应该期望他们为您处理这件事吗？

Gradio 现在包含一个 **“文件上传”MCP 服务器**，代理可以使用它将文件直接上传到您的 Gradio 应用程序。如果您的 Gradio MCP 服务器中的任何工具需要文件输入，连接文档现在将向您展示如何启动“文件上传”MCP 服务器：

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/MCPConnectionDocs.png)

在 [Gradio 指南](https://www.gradio.app/guides/file-upload-mcp) 中了解有关使用此服务器（以及重要的安全注意事项）的更多信息。

## 实时进度通知

根据 AI 任务的不同，获得结果可能需要一些时间。现在，Gradio **将进度通知流式传输**到您的 MCP 客户端，使您可以实时监控状态！

[](https://github.com/user-attachments/assets/b507c380-d6b6-4307-b0d1-be423a7414f3)

作为一名 MCP 开发人员，强烈建议您实现 MCP 工具以发出这些进度状态。我们的[指南](https://www.gradio.app/guides/building-mcp-server-with-gradio#sending-progress-updates)向您展示了如何操作。

## 一行代码将 OpenAPI 规范转换为 MCP

如果您想将现有的后端 API 集成到 LLM 中，您必须手动将 API 端点映射到 MCP 工具。这可能是一项耗时且容易出错的琐事。通过此版本，Gradio 可以为您自动化整个过程！只需一行代码，您就可以将业务后端集成到任何兼容 MCP 的 LLM 中。

[OpenAPI](https://www.openapis.org/) 是一种广泛采用的标准，用于以机器可读的格式（通常为 JSON 文件）描述 RESTful API。Gradio 现在具有 `gr.load_openapi` 函数，该函数直接从 OpenAPI 模式创建 Gradio 应用程序。然后，您可以使用 `mcp_server=True` 启动该应用程序，以自动为您的 API 创建 MCP 服务器！

```
import gradio as gr

demo = gr.load_openapi(
    openapi_spec="https://petstore3.swagger.io/api/v3/openapi.json",
    base_url="https://petstore3.swagger.io/api/v3",
    paths=["/pet.*"],
    methods=["get", "post"],
)

demo.launch(mcp_server=True)

```

在 Gradio [指南](https://www.gradio.app/guides/from-openapi-spec) 中查找更多详细信息。

## 身份验证的改进

MCP 服务器开发中的一种常见模式是使用身份验证标头代表您的用户调用服务。作为一名 MCP 服务器开发人员，您希望清楚地告知您的用户他们需要提供哪些凭据才能正确使用服务器。

为了使这成为可能，您现在可以将 MCP 服务器参数键入为 `gr.Header`。Gradio 将自动从传入的请求中提取该标头（如果存在），并将其传递给您的函数。使用 `gr.Header` 的好处是，MCP 连接文档将自动显示您在连接到服务器时需要提供的标头！

在下面的示例中，`X-API-Token` 标头从传入的请求中提取，并作为 `x_api_token` 参数传递给 `make_api_request_on_behalf_of_user`。

```
import gradio as gr

def make_api_request_on_behalf_of_user(prompt: str, x_api_token: gr.Header):
    """Make a request to everyone's favorite API.
    Args:
        prompt: The prompt to send to the API.
    Returns:
        The response from the API.
    Raises:
        AssertionError: If the API token is not valid.
    """
    return "Hello from the API" if not x_api_token else "Hello from the API with token!"


demo = gr.Interface(
    make_api_request_on_behalf_of_user,
    [
        gr.Textbox(label="Prompt"),
    ],
    gr.Textbox(label="Response"),
)

demo.launch(mcp_server=True)

```

[![MCP Header Connection Page](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/MCPUploadUpdated.png)](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/MCPUploadUpdated.png)

您可以在 Gradio [指南](https://www.gradio.app/guides/building-mcp-server-with-gradio#using-the-gr-header-class) 中阅读有关此内容的更多信息。

## 修改工具描述

Gradio 会自动从您的函数名称和文档字符串生成工具描述。现在，您可以使用 `api_description` 参数进一步自定义工具描述。在此示例中，工具描述将显示“将棕褐色滤镜应用于任何图像”。

```
import gradio as gr
import numpy as np

def sepia(input_img):
    """
    Args:
        input_img (np.array): The input image to apply the sepia filter to.

    Returns:
        The sepia filtered image.
    """
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

gr.Interface(sepia, "image", "image", 
             api_description="Apply a sepia filter to any image.")\
            .launch(mcp_server=True)

```

在[指南](https://www.gradio.app/guides/building-mcp-server-with-gradio#modifying-tool-descriptions)中阅读更多内容。

## 结论

希望我们向 Gradio 添加新的 MCP 相关功能吗？请在博客或 [GitHub](https://github.com/gradio-app/gradio/issues) 的评论中告诉我们。此外，如果您构建了一个很酷的 MCP 服务器或 Gradio 应用程序，请在评论中告诉我们，我们将扩大它的影响！