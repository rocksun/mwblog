# ML 和 LLM 的采用最常受到可观测性的挑战

![Featued image for: ML and LLM Adoption Challenged Most Often by Observability](https://cdn.thenewstack.io/media/2025/03/5fad52d3-olivie-strauss-xuuuktvxv7a-unsplashb-1024x576.jpg)

在将 ML 模型投入生产时，可观测性和监控是被提及最多的挑战。[The Institute for Ethical AI & Machine Learning](https://ethical.institute/index.html) 在 2024 年第四季度进行了一项[关于生产 ML 状态的调查](https://docs.google.com/forms/u/2/d/e/1FAIpQLSfY7kqfD1YJOW1KwsYr1VYzjn_ONdUVQ71xkgsz2rsulHrJ6Q/viewanalytics)。另一个关键结论是，由于很少有供应商工具获得显著的吸引力，因此定制工具在用户路线图中占据主导地位。

总体而言，在接受调查的 170 名从业者中，44% 是机器学习工程师，与数据科学家或 MLOps 工程师的数量大致相同。许多受访者都是 [The ML Engineer newsletter](https://www.linkedin.com/newsletters/6882216044568571904/) 的订阅者。

只有 7% 的人表示 ML 安全是他们面临的三大挑战之一，只有 17% 的人对治理和领域风险持相同看法。这一发现与我们在其他研究中看到的有显著不同，在其他研究中，安全和 AI 治理被认为是增加采用的最大障碍之一。我们认为，从业者认为 ML 安全仅与模型被黑客攻击的能力有关，而其他 IT 决策者更担心对公司和个人数据的一般访问。

似乎每个企业至少都在试验生成式 AI 和依赖于[大型语言模型](https://thenewstack.io/llm/)（LLM）的 AI 代理。与此同时，预测分析和计算机视觉的应用持续增长。随着这些应用程序的规模扩大，开发人员需要数据工程师、SRE 和其他人来处理 Day 1 和 [Day 2 挑战](https://thenewstack.io/cloud-native-day-2-operations-why-this-begins-on-day-0/)。为了迎接这一挑战，[MLOps](https://thenewstack.io/what-is-mlops/) 成为了一门真正的学科，随后是 LLMOps 和 [GenAIOps](https://thenewstack.io/microsoft-sees-devs-embracing-a-paradigm-shift-to-genaiops/)。

无论使用何种术语，[LLM 可观测性和监控](https://thenewstack.io/what-is-llm-observability-and-monitoring/) 都是必须解决的问题。

## 定制工具 vs. 供应商工具

该调查询问了利用 AI 和机器学习所需的技术堆栈的九个不同部分。以下是一些值得注意的发现：

- 65% 的调查对象使用托管模型或 LLM API 服务。在使用此类服务的用户中，最常使用的是 [OpenAI](https://thenewstack.io/openais-realtime-api-takes-a-bow/)(38%)、[AzureAI](https://azure.microsoft.com/en-us/solutions/ai/)(20%) 和 [Amazon Bedrock](https://thenewstack.io/amazons-bedrock-can-now-check-ai-for-hallucinations/)(12%)。[MLflow](https://mlflow.org/) 是领导者。在采用这些工具的用户中，48% 最常使用 MLflow。定制工具 (16%) 和 Weights & Biases (12%) 是该类别中接下来最常用的工具。请注意，刚刚完成 IPO 的 CoreWeave 最近宣布收购 Weights & Biases。
- *模型注册表和/或实验跟踪* - 在用户中，40% 最常使用 *ETL / 工作流编排器* [Airflow](https://thenewstack.io/how-apache-airflow-better-manages-machine-learning-pipelines/)。定制工具 (17%) 和 [Argo Workflows](https://argoproj.github.io/workflows/)(11%) 是该类别中接下来最常用的工具。
- *实时模型服务* - 在用户中，46% 最常使用 FastAPI/Flask Wrapper。数据科学家更倾向于使用此工具 (70%)。定制工具 (16%) 和 [AWS SageMaker](https://thenewstack.io/address-common-machine-learning-challenges-with-managed-mlflow/)(12%) 是该类别中接下来最常用的工具。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)