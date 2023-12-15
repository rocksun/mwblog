<!--
title: Go中使用Gemini模型
cover: https://eli.thegreenplace.net/images/2023/turtle1.png
-->

Google 最近通过 API 免费提供了其最新的多模态 LLMs 家族，同时还发布了慷慨的免费套餐。Google 还在多种流行的编程语言中发布了 SDK，包括 Go 语言。
这篇文章是如何使用 Go SDK 快速入门，以向模型提出混合文本和图像的问题的概述。

> 译自 [Using Gemini models from Go](https://eli.thegreenplace.net/2023/using-gemini-models-from-go/)。作者 Eli Bendersky 。

## 任务

我们将要求模型解释两张龟的图像之间的区别，这张：

![turtle1](https://eli.thegreenplace.net/images/2023/turtle1.png)

和这张：

![turtle2](https://eli.thegreenplace.net/images/2023/turtle2.png)

## 使用 Google AI SDK

使用 Google AI SDK，您只需生成一个 API 密钥（与 OpenAI 的 API 类似）即可访问模型。Go SDK 位于 https://github.com/google/generative-ai-go，其包文档在 https://pkg.go.dev/github.com/google/generative-ai-go；其中有许多示例我们可以参考。

以下是我们任务的代码：

```go
package main

import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "os"

  "github.com/google/generative-ai-go/genai"
  "google.golang.org/api/option"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("API_KEY")))
  if err != nil {
    log.Fatal(err)
  }
  defer client.Close()

  model := client.GenerativeModel("gemini-pro-vision")

  imgData1, err := os.ReadFile("../images/turtle1.png")
  if err != nil {
    log.Fatal(err)
  }

  imgData2, err := os.ReadFile("../images/turtle2.png")
  if err != nil {
    log.Fatal(err)
  }

  prompt := []genai.Part{
    genai.ImageData("png", imgData1),
    genai.ImageData("png", imgData2),
    genai.Text("Describe the difference between these two pictures, with scientific detail"),
  }
  resp, err := model.GenerateContent(ctx, prompt...)

  if err != nil {
    log.Fatal(err)
  }

  bs, _ := json.MarshalIndent(resp, "", "    ")
  fmt.Println(string(bs))
}
```
由于 LLM API 是多模态的，SDK 提供了像 genai.ImageData 和 genai.Text 这样的辅助类型，以一种类型安全的方式包装输入。当我们运行此示例时，模型的响应会以 JSON 对象的形式输出。其中重要的部分是：

```json
"Content": {
  "Parts": [
    "The first picture is of a tortoise, which is a reptile characterized by
    its hard shell. The second picture is of a sea turtle, which is a reptile
    characterized by its flippers and streamlined shell. Tortoises are
    terrestrial animals, while sea turtles are marine animals. Tortoises have
    a domed shell, while sea turtles have a flattened shell. Tortoises have
    thick, scaly skin, while sea turtles have smooth, leathery skin. Tortoises
    have short legs with claws, while sea turtles have long flippers.
    Tortoises have a slow metabolism and can live for over 100 years, while
    sea turtles have a faster metabolism and typically live for around 50
    years."
  ],
  "Role": "model"
},
```

好的，现在我们知道了 :-)

## 使用 GCP Vertex SDK

如果您是 GCP 的客户，并且已经设置了 GCP 项目的计费等其他事项，您可能想使用 Vertex Go SDK。
Go SDK 的一个很棒之处在于您几乎不需要更改代码！唯一的更改是导入行，从：

```go
"github.com/google/generative-ai-go/genai"
```

修改为：

```go
"cloud.google.com/go/vertexai/genai"
```

然后更改创建客户端的方式，因为身份验证是不同的。对于 Vertex，应该像这样创建客户端：

```go
client, err := genai.NewClient(ctx, os.Getenv("GCP_PROJECT_ID"), "us-central1")
```

其中 `GCP_PROJECT_ID` 是具有您的 GCP 项目的 env 变量，位置/区域可以根据您的偏好进行设置。其余代码保持完全相同！

有两个 SDK 是因为两个产品提供的功能在某些情况下可能有所不同。例如，GCP 的 SDK 可能允许您直接从存储桶或数据库表中读取数据。

## 代码

本文所有示例的完整代码 - 包括示例图像 - 可[在 GitHub 上找到](https://github.com/eliben/code-for-blog/tree/master/2023/go-google-ai-gemini)。
