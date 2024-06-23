# KitOps 是将 DevOps 管道转变为 MLOps 管道的开源工具

![KitOps Is the Open Source Tool That Turns DevOps Pipelines Into MLOps Pipelines 的特色图片](https://cdn.thenewstack.io/media/2024/06/797311cc-piplines-1024x575.png)

[机器学习](https://thenewstack.io/ai/) 和 DevOps 实践的结合催生了 MLOps，这是一个专门领域，专注于在生产环境中自动化 ML 模型的开发、部署和管理。然而，实现流线型 [MLOps](https://thenewstack.io/what-is-mlops/) 工作流的主要障碍在于 DevOps 和机器学习管道之间的传统分离。

本文探讨了 [KitOps](http://kitops.ml/)，这是一个开源项目，它通过允许您利用现有的 DevOps 管道来完成 [MLOps](https://thenewstack.io/optimize-ai-at-scale-with-platform-engineering-for-mlops/) 任务，从而弥合了这一差距，方法是使用 ModelKits。本文中的简短演练和代码示例将演示入门有多么容易。

## 单独工作流的瓶颈

构建和部署传统应用程序通常遵循一个定义明确的 DevOps 管道。代码经过版本控制、自动化测试以及无缝集成和交付。DevOps 是一个公认且经过验证的实践，用于大规模部署系统。然而，ML 项目引入了新的复杂性。模型需要特定的数据集、训练环境、配置和监控工具。数据科学家可以使用 [Jupyter 笔记本](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) 并迭代模型优化。在现有 DevOps 管道旁边构建单独的 MLOps 管道来管理这些方面会导致一些低效率：

**重复工作：**维护单独的管道意味着为版本控制、部署和配置管理等任务重复工作。想象一下为应用程序代码管理一个 DevOps 管道，为训练好的模型、其依赖项和配置文件管理一个单独的 MLOps 管道。这种冗余增加了开销，并在管道之间引入了潜在的不一致性。

**孤立的团队：**单独的管道可能导致孤立的开发环境，其中 DevOps 和 ML 工程师独立工作。协作变得支离破碎，阻碍了沟通并延迟了部署。数据科学家可能难以理解部署的复杂性，而 DevOps 工程师可能缺乏使用 ML 模型工作的具体知识。

**更陡峭的学习曲线：**维护不同的 MLOps 管道需要工程师学习和管理更广泛的工具集，由于操作中的低效率，增加了学习曲线并延迟了项目采用。对于刚接触 ML 的组织来说，这可能是一个重大的障碍，减缓了他们利用其潜力的能力。

## 进入 KitOps：使用 ModelKits 统一开发

KitOps 通过引入 ModelKits 的概念为这些差异提供了一个优雅的解决方案。ModelKits 是标准化包，封装了 ML 项目的所有关键组件：

**模型：**训练好的 ML 模型本身，通常以 pickle 或 joblib 等格式保存为示例。

**数据集：**用于训练以及可能用于测试和验证的数据。根据模型大小和数据隐私考虑，数据集可能包含在 ModelKit 中或作为外部位置引用。

**代码：**用于训练、预处理数据并可能为预测提供模型的源代码。这可能包括用于训练、数据处理和模型推理的 Python 脚本。

**配置：**模型环境的配置文件，包括依赖项（库、框架）、部署设置（环境变量）以及可能的提供配置（服务器配置、API 端点）。

ModelKits 是使用名为 Kitfile 的 YAML 文件构建的，该文件定义了每个组件的位置。Kitfile 采用熟悉且灵活的格式。这种标准化允许 KitOps 与现有的 DevOps 管道无缝集成，就像用于容器化的 Dockerfile 一样。事实上，Modelkits 甚至符合 OCI（参见 [开放容器计划](https://opencontainers.org/)）。

这是一个示例 Kitfile 可能是什么样子的快速快照：

```yaml
manifestVersion: 1.0
package:
  name: AIProjectName
  version: 1.2.3
  description: >-
    AI/ML 项目的简要说明。
  authors: [作者姓名，贡献者姓名]
code:
  - path: src/
    description: AI 模型的源代码。
  license: Apache-2.0
datasets:
  - name: DatasetName
    path: data/dataset.csv
    description: 数据集的说明。
  license: CC-BY-4.0
preprocessing: 预处理步骤。
```
模型：
名称：ModelName
路径：models/model.h5
框架：TensorFlow
版本：1.0
描述：模型描述。
许可证：Apache-2.0
训练：
数据集：DatasetName
参数：
- 学习率：0.001
- 轮次：100
- 批大小：32
验证：
- 数据集：DatasetName
指标：
- 准确率：0.95
- f1 分数：0.94
（来自：
[kitops.ml/docs/kitfile/format.html#example](https://kitops.ml/docs/kitfile/format.html%23example))

## 高级工作流

以下是使用 ModelKits 与 KitOps 的工作流细分：

**打包为 ModelKit：**数据科学家可以使用 KitOps CLI 将所有项目组件打包到 ModelKit 中。Kitfile 定义了整个包的结构并简化了版本控制。这确保了部署和使用模型所需的所有元素都捆绑在一起。[标记](https://kitops.ml/docs/cli/cli-reference.html%23kit-tag)是一项内置功能，可帮助通过可引用的标记组织存储库中的 ModelKits。

**版本控制和 CI/CD：**ModelKit 在存储库中与应用程序代码一起进行版本控制，确保了统一的开发流程。DevOps 生态系统中现有的 CI/CD（持续集成和持续交付）管道会获取更改并触发构建和部署。这利用了您现有的基础设施来管理代码更改和部署，从而简化了流程。

**使用现有工具进行部署：**KitOps 与 Docker 等现有容器化技术配合良好，可用于部署 ModelKits。例如，这允许 SRE 使用熟悉的 DevOps 工具将 ModelKits 部署到 Kubernetes 等生产环境。容器化方法确保了一致且可移植的部署环境，该环境将很好地与 DevOps CI/CD 管道工具（如 Jenkins、GitLab、CircleCI、GitHub Actions 和 Azure DevOps）集成。

## 试用 KitOps CLI

既然我们已经介绍了 KitOps 的主要内容，让我们动手探索 CLI 在您选择的终端中的一些功能和用法。要开始，有两个选项。第一个选项是克隆 KitOps 存储库并构建二进制文件，如下所示：

```
1
2
3
4
5
```

```
git clone https://github.com/jozu-ai/kitops.git
cd kitops
go build -o kit
```

第二个选项是直接下载适用于您架构的预构建二进制文件
[此处](https://github.com/jozu-ai/kitops/releases/)并解压缩文件。例如：

```
1
2
3
```

```
curl -OL https://github.com/jozu-ai/kitops/releases/download/v0.2.4/kitops-darwin-arm64.zip
unzip kitops-darwin-arm64.zip
```

无论您选择哪种选项，都将 kit 二进制文件移动到 PATH 中的位置，以便您可以发出命令。这是 Mac 或 Linux 的一个示例：

```
1
```

```
sudo mv kit /usr/local/bin
```

接下来，从终端检查 kit 的版本以查看它是否工作正常。

```
1
```

```
kit version
```

您应该看到如下输出：

```
1
2
3
4
5
6
7
```

```
版本：0.2.4-76ec9bc
提交：76ec9bcf94e94177199522480871367138661125
构建：2024-05-10T21:53:18Z
Go 版本：go1.21.6
```

KitOps CLI 提供了许多
[命令](https://kitops.ml/docs/cli/cli-reference.html)。对于本演练，我们将首先深入了解从已知 Llama 3 模型存储库中可用的 Modelkits：

```
1
```

```
kit list ghcr.io/jozu-ai/llama3
```

我们看到有许多带有不同标记的 ModelKits：

```
1
2
3
4
5
6
7
8
9
```

```
存储库 标记 维护者 名称 大小 哈希
jozu-ai/llama3 8B-instruct-f16 Meta Platforms llama3 11.4 GiB sha256:995b9e0f87ddcdcaa59803a08986409b6e4cf2f8b071b064bca21e4e801566a3
jozu-ai/llama3 8B-text-f16 Meta Platforms llama3 11.4 GiB sha256:6b5b4a82ba3a73f00248b4431db738217e1978e316b2d4514b1bb887a11a0d84
jozu-ai/llama3 8B-instruct-q4_0 Meta Platforms llama3 4.1 GiB sha256:ccf9fb3d541c45a65dd99c7272a061776b8cb04d7635a5f844951b410b8ec2a7
...
```

让我们通过引用标记并使用 info 命令更详细地查看其中一个 ModelKits：

```
1
```

```
kit info --remote ghcr.io/jozu-ai/llama3:8B-instruct-q4_0
```

在这里，我们获得了有关 Modelkit 的更多信息，实质上是在 Kitfile 中定义的内容。

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
```

```
manifestVersion: "1.0"
package:
name: llama3
version: 3.0.0
description: Llama 3 系列大语言模型 (LLM)，一系列预训练和指令调整的生成文本模型，大小为 8 和 70B。
authors: [Meta Platforms, Inc.]
model:
name: llama3-8B-instruct-q4_0
path: ./llama3-8B-instruct-q4_0.gguf
description: Llama 3 8B 指令模型
...
```

在此，我们可以将 Modelkit 从远程位置解压缩到本地系统以对其进行处理。

```
1
2
3
```

```
kit unpack ghcr.io/jozu-ai/llama3:8B-instruct-q4_0 -d ./unpacked
ls ./unpacked
```
### 注意 Modelkit 中包含的文件，包括模型本身。

此时，让我们编写一个简短的 Python 脚本与模型交互，检查我们是否从给定的提示中获得了适当的响应。

创建一个名为 `prompt.py` 的文件，并确保已通过 pip 安装 `llama_cpp` 库。

```python
import llama_cpp

model_file = "llama3-8B-instruct-q4_0.gguf"
prompt = "你好，你是哪个模型？"

model = llama_cpp.Llama(
    model_path=model_file,
    verbose=False,
)

out = model.create_chat_completion(
    messages=[{"role": "user", "content": prompt}]
)

print("===")
print(prompt)
print("---")
print(out["choices"][0]["message"]["content"])
```

运行此脚本将生成以下输出，但每次可能略有不同。

```
python3 prompt.py
===
你好，你是哪个模型？
---
我是 LLaMA，一个由 Meta AI 开发的 AI 聊天机器人，能够以对话方式理解和响应人类输入。我是一个大型语言模型，在互联网上的海量文本数据集上进行训练，这使我能够对广泛的主题和问题生成类似人类的响应。我不断学习和提高我的能力，基于我与像你这样的用户进行的对话！
```

在此基础上，你可能会决定通过将此脚本添加到 `Kitfile` 中，然后使用 `KitOps` CLI 中的 `pack` 命令打包和标记新版本，将其包含在 `Modelkit` 中。然后可以将其提交到仓库。根据你想要实现的流程，可能性有很多。

快速说明：另一种在上述 `Modelkit` 中提示模型的简单方法是使用 `KitOps` CLI 中的 `dev` 命令。这会弹出一个简单的基于 Web 的聊天界面。

```
kit dev start
```

然后可以在浏览器窗口中访问聊天：

要关闭它，只需键入：

```
kit dev stop
```

## 更多要解包的内容

正如你从上面的演练中看到的，`KitOps` 使 `MLOps` 工作流清晰明了。通过使用 `KitOps` 统一 `DevOps` 和 `MLOps` 管道，团队可以获得以下好处：

**降低复杂性：**一个管道简化了开发过程，减少了开销并简化了团队之间的协作。`DevOps` 和 `ML` 工程师都在同一框架内工作，促进了更好的沟通和理解。

**缩短上市时间：**利用现有的 `DevOps` 工具和基础设施可以加速部署并提高整体项目交付速度。无需学习和管理单独的 `MLOps` 工具，使团队能够专注于构建和改进模型本身。

**提高一致性：**一个统一的管道确保了整个应用程序和 `ML` 模型生命周期中版本控制和配置管理的一致性。这降低了因管理单独的管道而产生的错误和不一致的风险。

**模型版本控制和回滚：**`ModelKit` 与应用程序代码一起进行版本控制。这使你能够跟踪模型及其依赖项的更改，并在必要时促进回滚到以前的版本。想象一下遇到新部署模型的问题。使用版本控制，你可以使用现有的 `CI/CD` 管道轻松地恢复到以前稳定的版本。

**A/B 测试和实验：**`KitOps` 能够对不同模型版本进行无缝的 `A/B` 测试。通过部署具有不同模型的多个 `ModelKit`，你可以在流量子集上比较它们的性能。这允许在选择最适合生产部署的模型时进行数据驱动的决策。

**模型治理和可解释性：**`Kitfile` 可用于记录模型的目的、使用的训练数据和任何相关元数据。这通过提供一个用于审计和合规目的的关键信息中心位置来促进模型治理。此外，`KitOps` 可以与模型可解释性工具集成，以帮助理解模型的决策过程。

## 总结

`DevOps` 和 `MLOps` 管道的分离会阻碍 `ML` 模型的有效开发和部署。`KitOps` 通过引入 `ModelKit` 提供了一个引人注目的开源解决方案，`ModelKit` 是封装 `ML` 项目所有关键组件的标准化包。这使组织能够利用其现有的 `DevOps` 管道和工具来执行 `MLOps` 任务，从而降低复杂性、缩短上市时间、提高一致性并简化整个 `ML` 模型生命周期中的跟踪。随着 `MLOps` 领域的不断发展，`KitOps` 为统一开发和加速机器学习解决方案的采用提供了一种强大的方法。

查看 [KitOps 网站](http://kitops.ml/) 了解更多信息。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。