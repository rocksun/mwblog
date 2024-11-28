
<!--
title: 在无服务器平台上运行无需GPU的AI模型
cover: https://cdn.thenewstack.io/media/2024/11/31d53ef8-ai-without-gpu-serverless.jpg
-->

哪个CPU平台在运行机器学习任务方面能更好地平衡成本和性能？请跟随我的实验来找出答案。

> 译自 [Running AI Models Without GPUs on Serverless Platforms](https://thenewstack.io/running-ai-models-without-gpus-on-serverless-platforms/)，作者 Rak Siva。

随着机器学习 (ML) 技术的发展，计算资源的选择成为影响性能和成本效率的关键决策。由于其并行处理能力，GPU 是机器学习的首选；然而，最近的进展也提高了某些类型[ML 任务](https://roadmap.sh/mlops)的 CPU 性能。

Llama（代表大型语言模型 Meta AI）就是这种转变的例证。我将探讨在各种[无服务器](https://thenewstack.io/serverless/)平台上，无需使用 GPU 即可运行 Llama 模型的可行性。

## 模型选择

Meta 创建的[Llama 模型](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/)是一系列[大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/)，旨在提供先进的自然语言理解和生成能力。这些模型用途广泛，并且越来越受到希望实施 AI 驱动的解决方案而无需依赖大量计算资源的组织的欢迎。

这可能使 Llama 模型成为在无服务器平台上部署的可行选择——也就是说，如果存在一个适合无服务器计算限制的模型。第一个挑战将是弄清楚要尝试哪些 Llama 模型，因为有很多可供选择。

为了做出明智的选择，您需要了解量化。量化是一种机器学习技术，通过降低其权重和其他数值的精度来压缩大型模型。量化不是使用完整的 32 位或 16 位浮点数来存储这些值，而是将它们表示为更低位的格式，例如 8 位、4 位甚至 2 位整数。这种精度的降低会显著减小模型的大小并降低其内存和计算需求，但可能会以精度或质量为代价。

想象一下跟踪商店中的商品价格。通常，您会以精确到美分的形式记录价格，例如 4.99 美元或 6.33 美元。四舍五入到最接近的美元（例如，5 美元、6 美元）可以得到一个粗略的近似值，并简化未来计算（如估计利润率、税款或小费）的复杂性。

[LM Studio](https://lmstudio.ai/) 在 Hugging Face 上分发了 Llama 3.2 1B 模型的几个量化版本。在量化模型的命名方案中，每个部分都表示模型压缩的一个方面。例如，对于 Q4_K_M 模型：

- **Q4**: “Q” 表示量化，“4” 表示该模型使用 4 位精度表示其权重。位数越低，模型越轻，适合资源有限的情况，但可能会影响精度。
- **K**: 指量化技术，旨在在压缩模型的同时尽可能保留质量。
- **M**: 代表中等精度级别，在精度和大小之间取得平衡。其他模型可能会根据应用程序的需求使用“L”表示低精度或“H”表示高精度。

最终，需要一个反复试验的过程来找到一个具有正确权衡和优势的模型，该模型可以在目标基础设施上运行。

## 实验设置：部署 Llama 3.2

经过一番尝试和错误，并在研究了其他人的尝试后，我决定从 4_K_M 1B 模型开始。这个拥有十亿参数的模型可以管理复杂的语言任务，生成细致的响应并理解数据中错综复杂的关系。它还在我的内存分配限制内保证了计算复杂性和输出质量之间的平衡。

使用 Nitric（一个允许在多个云平台上无缝部署的框架），我在[AWS](https://aws.amazon.com/?utm_content=inline+mention) Lambda 和[Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Run 上都设置了 Llama 模型。

![](https://cdn.thenewstack.io/media/2024/11/31a4eefb-llama-experiment-architecture.png)

Nitric 还允许配置计算函数的内存和/或 CPU 分配。但是，云供应商之间存在一些差异，限制了创建相同环境的能力。例如，AWS [Lambda](https://aws.amazon.com/pm/lambda) 不允许显式配置 CPU，而 Google Compute Platform (GCP) [Cloud Run](https://cloud.google.com/run) 将内存分配限制为每个 CPU 最多 4GB。

这使得直接和公平地比较模型的性能尤其具有挑战性，因此我必须使用“类似”的硬件配置进行一些近似。最终的比较将考虑每秒token数 (TPS) 和每秒成本 (CPS)，以进一步控制这些差异。

## 技术实现

无服务器部署的实现涉及使用`llama_cpp`加载模型
定义API路由并设置处理提示所需的代码。以下是用于加载Llama模型的代码。我将使用Nitric进行部署，在AWS和GCP上部署相同的代码库。

注意：有关如何自行运行此项目的逐步指南，请遵循[Llama 3.2 on AWS Lambda](https://thenewstack.io/running-llama-3-2-on-aws-lambda/)指南。

```py
from nitric.resources import api
import time
from nitric.application import Nitric
from nitric.context import HttpContext
from llama_cpp import Llama

# Load the locally stored Llama model
llm = Llama(model_path="./models/Llama-3.2-1B-Instruct-Q4_K_M.gguf")

def process_prompt(user_prompt):
    system_prompt = "You are a helpful assistant."
    prompt = (
        f'<|start_header_id|>system<|end_header_id|>{system_prompt}<|eot_id|>'
        f'<|start_header_id|>user<|end_header_id|>{user_prompt}<|eot_id|>'
        f'<|start_header_id|>assistant<|end_header_id|>'
    )

    start_time = time.time()

    response = llm(
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
    )

    # Calculate tokens per second
    end_time = time.time()
    t_eval_ms = (end_time - start_time) * 1000    
    total_tokens = response['usage']['total_tokens']
    tps = total_tokens / (t_eval_ms / 1000)

    return response, t_eval_ms, tps

# Define an API for the prompt service
main = api("main")

@main.post("/prompt")
async def handle_prompt(ctx: HttpContext):
    prompt = ctx.req.data

    try:
        output, t_eval_ms, tps = process_prompt(prompt)
        ctx.res.body = {
            'output': output,
            't_eval_ms': t_eval_ms,
            'tps': tps,
        }
    except Exception as e:
        print(f"Error processing prompt: {e}")
        ctx.res.body = {"error": str(e)}
        ctx.res.status = 500

Nitric.run()
```

## 跨越一些障碍

虽然应用程序部署很顺利，但在我的函数中加载和运行Llama模型却遇到了一些挑战。

### 内存

最初，我遇到了超时问题，这表明我的配置资源不足以满足模型的需求。虽然Hugging Face建议的内存需求是16GB，但通过反复试验，我确定该模型至少可以使用6GB的内存在各种环境中运行。在Cloud Run上扩展到6GB需要将CPU数量从1增加到2，因为GCP每个CPU的内存限制为4GB。在AWS上，CPU配置不太灵活；我只能将内存分配设置为6GB。

### 临时存储

临时存储是特定进程或实例存在期间存在的临时存储。一旦进程完成或实例终止，存储在临时存储中的数据就会丢失。

加载Llama模型需要更大的临时存储空间，因为模型文件很大，需要临时解压缩以及推理过程中的中间计算。AWS需要将默认的临时存储空间从512MB增加到1024MB以适应模型加载。顺便说一句，GCP Cloud Run默认分配2GB的临时存储空间，因此无需更改。

### CPU

即使设置了CPU和内存，模型在GCP上也只有大约50%的时间可以加载。故障通常会导致超时，这开始表明CPU分配不足以满足模型的初始加载需求。经过一些反复试验，我启用了GCP的CPU加速功能，此功能可在无服务器应用程序的启动阶段暂时提供额外的CPU能力。

此加速功能为容器提供了完成其密集型加载序列所需的额外处理能力，使其在超时限制内完成。权衡是成本；您需要为容器启动期间使用的加速CPU以及额外的10秒钟付费。例如，如果您的容器启动时间为15秒，并且您分配了2个CPU，则您需要为整个25秒的4个CPU付费。

## 结果

**每秒token数**

我的代码包括每秒生成的token数 (TPS) 的计算。TPS通过确定模型在一秒钟内可以处理或生成多少文本单元来量化模型的吞吐量。这类似于测量人类的阅读或书写速度。一个token可以是一个词、一个词的一部分，有时甚至只是一个标点符号或特殊字符。对于此示例，只需假设一个token等于一个词。普通人每分钟阅读约300个词（大约每秒五个词），每分钟书写约40个词（不到每秒一个词）。

虽然将计算机和人类的token生成速率进行比较并不完全公平，但这些估计值可以作为粗略的指南，帮助确定适合特定任务的模型。例如，当提示生成器生成的內容速度至少与普通人的阅读速度一样快时，它将最有用。

### 成本分析

尽管环境对vCPU的管理方式不同，但在两种平台上，使用6GB内存配置的平均TPS都相当相似。它们是使用一组50个示例提示计算的，例如“解释彩虹是如何形成的”，对于限制响应长度的提示，结果略好——例如，“解释彩虹是如何形成的，用50个词”。

使用TPS，您可以粗略地计算在每个环境中典型提示（大约500个token）的token生成成本。

|                     | AWS Lambda | GCP Cloud Run (已启用加速) |
|---------------------|-------------|--------------------------|
| 内存分配           | 6GB         | 6GB                        |
| CPU分配             | 由AWS管理     | 4 vCPU (2x 用于CPU加速)     |
| 每GB-秒成本         | $0.00001667 | $0.00000250               |
| 每vCPU-秒成本       | –           | $0.00002400               |
| 平均TPS             | 7.42        | 7.39                       |
| 计算CPS             | 6GB × $0.00001667 = $0.00010002 | (4 vCPUs × $0.00002400) + (6 GB × $0.00000250) = $0.00010200 |
| 每个token的成本 (CPS / TPS) | $0.00001348 | 0.0000138                 |
| 每个典型请求的成本 (500个token) | $0.00674     | 0.0069                     |

*注意：价格可能因地区而异；这些值是估计值，仅基于美国一级地区的计算资源。*

## 结论

根据这些试验，Llama模型确实可以部署在无服务器平台上以用于轻量级或中等任务，并需要仔细配置以满足内存、CPU和存储需求。对于处理时间和吞吐量在无服务器限制内可控的特定应用程序，此设置是可行的。

成本差异几乎可以忽略不计，但这仅仅是因为我被迫在 Cloud Run 中使用 CPU 提升功能，以确保模型在合理的启动限制内加载。如果我能找到一种方法避免 CPU 提升，那么 GCP 上的成本可能会降低，因为我不会将 CPU 使用量加倍。另一个需要考虑的是，推荐的内存是 16GB，这可能会导致更好的模型性能。GCP Cloud Run 支持高达 32GB，而 AWS 支持高达 10GB。

最终，无服务器计算可能难以处理大型模型，或者当应用程序需要长时间进行密集计算时。然而，很明显，Llama 在无服务器环境中可以很好地用于特定中低端应用程序，但随着需求的增加，将需要转向 GPU。在这个实验中，我使用 Nitric 在多个云平台上部署无服务器计算。Nitric 还可以用于[部署需要大量计算资源或 GPU 访问权限的作业](https://nitric.io/blog/introducing-nitric-batch)，而无需编写复杂的部署自动化。
