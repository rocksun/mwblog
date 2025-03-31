<!--
title: 创建图片生成MCP Server
cover: https://yylives.cc/wp-content/uploads/2025/03/cover-3.png
summary: 本文介绍了如何为 Roo Code 创建一个 Gemini 图像生成 MCP 服务器，使用 Python 编写。文章详细说明了如何设置项目、安装依赖，以及创建一个 generate_image 工具。
-->

正如[前文](https://yylives.cc/2025/03/19/001-roo-code-quickstart/)提到的，我仍然需要一个图片生成的 MCP Server。参考 [MCP 快速入门](https://modelcontextprotocol.io/quickstart/server)和 [Gemini 文档](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn#python)，我发现实现起来应该不难。

## 创建项目

Python 最简单，AI 相关的工具也多，所以这个项目咱还是 Python。

首先还是推荐大家使用 uv 管理依赖，Windows 下安装 uv 可以执行：

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

然后创建项目：

```
# Create a new directory for our project
uv init gemini-image-mcp-server
cd gemini-image-mcp-server

# Create virtual environment and activate it
uv venv
.venv\Scripts\activate

# Install dependencies
uv add mcp[cli] httpx

# Create our server file
new-item server.py
```

为了访问 Gemini AI，还需要安装相关的依赖：

```
uv add google-genai
```

然后编写我们的 server.py ：

```py
from typing import Any
from mcp.server.fastmcp import FastMCP
from google import genai
from google.genai import types
from io import BytesIO
import os
import uuid
from PIL import Image
import sys

# Initialize FastMCP server
mcp = FastMCP("gemini-image-mcp-server")

def generate_image_from_gemini(prompt: str) -> str:
    api_key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    contents = (prompt)
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=['Text', 'Image']
        )
    )
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            # print(part.text)
            sys.stderr.write(part.text + '\n')
        elif part.inline_data is not None:
            image = Image.open(BytesIO((part.inline_data.data)))
            # 创建 generated-images 目录（如果不存在）
            if not os.path.exists('generated-images'):
                os.makedirs('generated-images')
            # 生成唯一文件名
            unique_filename = f"generated-images/{uuid.uuid4()}.png"
            image.save(unique_filename)
            return os.path.abspath(unique_filename)
    # 如果没有找到有效的图像数据，返回一个默认的错误信息
    return "No valid image data found."

@mcp.tool()
async def generate_image(prompt: str) -> str:
    """Get the image path from prompt.

    Args:
        prompt: Text used to generate the image
    """
    path = generate_image_from_gemini(prompt)
    return path

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
```

`@mcp.tool()` 修饰的方法，将会暴露为 MCP 的 Tool 。方法 `generate_image_from_gemini` 完成了实际的 Gemini 调用。

而最后，通过 `mcp.run(transport='stdio')` ，我们指明 MCP Server 将会以标准输入接收调用。因此，我们的程序一定不要向标准输出中输出内容，这样会影响 MCP Server 的使用。

## 集成到 Roo Code

VSCode 中打开 Roo Code，在顶部点击 MCP Servers，然后点击 Edit MCP Settings，修改内容为：

```json
{
  "mcpServers": {
      "gemini-image-mcp-server": {
          "command": "uv",
          "args": [
              "--directory",
              "D:\\path-of-the-dir\\gemini-image-mcp-server",
              "run",
              "server.py"
          ],
          "env": {
            "GEMINI_API_KEY": "your-gemini-api-key"
          }
      }
  }
}

```

主要是修改 args 中我们 `gemini-image-mcp-server` 的路径，以及你的 GEMINI_API_KEY，这个也可以直接使用我们快速入门中得到的 KEY 。

重启 VSCode ，应该可以在 Roo Code 的 MCP Servers 部分看到我们设置的 `gemini-image-mcp-server`，有点小激动啊。

## 验证

下面，验证我的 MCP Server 的时候到了。在对话窗口输入：

```
请根据本文的内容，发挥一些联想，生成一个可以当作封面的图
```

Roo Code 给了我令人开心的提示：

```
Now, I will use the generate_image tool from the gemini-image-mcp-server to generate the image.
```

啊，已经识别出来了，有点意思。点击继续：

```
Task Completed
I have generated an image based on the content of the document. The image is located at D:\projects\rocksun\gemini-image-mcp-server\generated-images\cfa92d67-e6aa-4527-85f2-3ae4e1ef6b6d.png.
```

图片出来了，但是和我预期的略有差别，毕竟我是想让出现在 markdown 文件所在的目录，所以我继续提示：

```
我希望这个图片保存到 md 的目录，并修改为 cover.png
```

不负众望，Roo Code 帮我执行了这个命令：

```
move D:\projects\rocksun\gemini-image-mcp-server\generated-images\cfa92d67-e6aa-4527-85f2-3ae4e1ef6b6d.png 002-create-gemini-image-mcp-server\cover.png
```

不过这图片，很有 Gemini 特色，大家应该已经看过了。

## 总结

我意识到，我之前做的许多自动化工作，都可以做成 MCP Server 的 Tool，而且我也不需要像以前那样提供精确的参数，Roo Code 可以帮我省掉许多琐碎的细节，似乎很快就可以实现“动动嘴”就把活干了的阶段。

下一步，也许就是去丰富我自己的 Tools。或者，你有什么想说的，可以联系我，大家一起探讨。