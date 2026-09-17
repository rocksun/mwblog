**本周，Cohere 发布了** North Small Translate 1.0，采用 CC BY-NC 4.0 许可证：用户可以下载、评估和研究其权重，但在没有商业协议的情况下，不能将其用于生产环境。

对于这家以[受监管行业的AI主权](https://thenewstack.io/cohere-sovereign-coding-model-north-mini-code/)为核心卖点的加拿大基础模型公司来说，这是一个有趣的举动。该公司将此次发布描述为“让主权AI成为技术现实”使命的一部分。这里的主权意味着对模型运行位置以及数据可见性的控制。商业许可证使这一承诺得以完整保留，但并没有让用户实现真正的“独立于Cohere”。企业虽然保留了数据和基础设施，但无法对模型进行分支（fork）、基于此构建产品，或者在续约时条款变更的情况下继续运行模型。

## 开放权重，但禁止商业生产

North Small Translate 是一个开放权重的混合专家模型，专为超过 50 种语言和区域变体的机器翻译而构建。它拥有 [2180亿个总参数](https://docs.cohere.com/docs/north-small-translate-1.0)，其中 250 亿个为激活参数，并支持 16,000 个 token 的上下文窗口。

> 并非所有用户都能平等地访问这些权重。

[据 Cohere 称](https://docs.cohere.com/changelog/north-small-translate-1-0)，该模型旨在为研究人员、开发人员和企业提供“灵活的方式来评估和部署机器翻译，同时保持对数据和基础设施的控制”。

对于渴望追求主权AI的组织来说，这描述颇具吸引力。但此次开放权重发布伴随着一个重要的警告：并非所有用户都享有利用这些权重的同等权利。

North Small Translate 目前可通过 Chat V2 API 在 Cohere 的免费层级中使用。对于打算将模型权重用于非商业用途的用户，FP8 权重已在 Hugging Face 上以 CC BY-NC 4.0 许可证发布。

但如果企业希望将其投入生产，则适用一套不同的条款。他们必须购买商业许可证，并通过 [Model Vault](https://cohere.com/solutions/model-vault)（Cohere 的全托管推理平台）来部署 North Small Translate。

## Cohere 并非唯一一家对开放权重使用设限的公司

其他 AI 公司也开始对其开放权重的模型附加更多条件。

上个月，中国 AI 实验室 [Z.ai](https://z.ai) 在 Hugging Face 上发布了其旗舰模型 GLM-5.3 的权重。但与这家加拿大 AI 公司一样，它也[根据部署模型的主体更改了许可条款](https://thenewstack.io/zai-glm-weights-license/)——这与其之前的方法有所不同。虽然 GLM-5.2 是在宽松的 MIT 许可证下发布的，但 GLM-5.3 为某些商业用户增加了新的要求。

> 就 Cohere 而言，对于为何将 North Small Translate 的开放权重设为非商业用途，其同样保持沉默。

这些要求仅适用于在连续 12 个月内总收入超过 100 亿美元的公司。此外，如果这些公司希望出于商业目的托管 GLM-5.3 或其衍生作品，必须首先通过该中国实验室的安全审查。

Z.ai 没有明确说明为何决定为 GLM-5.3 做出如此大的转变，考虑到其前身是在没有任何商业限制的 MIT 许可下发布的，这一点尤其令人困惑。Cohere 对此也同样保持沉默。

## 主权部署，但有限制

鉴于该公司一直向企业销售主权 AI 的历史，这家加拿大公司决定将 North Small Translate 作为开放权重提供，但限制商业用途的做法令人困惑。

事实上，在六月份，它推出了其首个编码模型 [North Mini Code](https://cohere.com/blog/north-mini-code)，以此回应开发人员对受监管行业长期要求的主权保障的需求。

然而，与 North Small Translate 不同，该开放权重模型从一开始就根据 Apache 2.0 许可证发布，没有任何针对商业用户的类似限制。

显然，Cohere 在其最新的开放权重发布中走了一条不同的道路，这成为 AI 公司对日益强大的开放权重模型施加更严格条款的又一个例子。