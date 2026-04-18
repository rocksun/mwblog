一个全新的[身份验证](https://thenewstack.io/with-identity-management-start-early-for-less-tech-debt/)层正被部署到 Claude 上。这并非一项适用于所有用户的普遍性法令，身份过滤器将应用于 Anthropic 定义的“少数用例”，尽管这些用例的范围在某些地方仍显得有些模糊。

Anthropic 在周二的 [Claude 支持博客](https://support.claude.com/en/articles/14328960-identity-verification-on-claude)中确认了这一进展。该组织表示，身份验证有助于防止滥用、执行使用政策并遵守法律义务。

用户被告知在访问某些功能时“可能会看到验证提示”，这是 Claude 团队“常规平台完整性检查”及其他安全合规措施的一部分。

## Anthropic 将如何验证用户？

Anthropic 选择总部位于旧金山的身份验证平台公司 [Persona Identities](https://withpersona.com/) 作为此项服务的技术合作伙伴。被要求确认身份的用户需要有效的政府颁发的带照片身份证件。他们需要出示实物证件并拍摄实时自拍，以通过验证过程。

> “我们不会使用您的身份数据来训练我们的模型……我们收集的信息不会超过所需范围……我们不会与任何其他人分享您的身份数据。”——Anthropic Claude 团队。

接受的证件包括护照、国民身份证、驾照或州/省身份证。验证通常不到五分钟。Claude 团队确认，非政府证件（如学生证、工作证、借书证和银行卡）均不可接受。

## Anthropic 正在过滤哪些用户？

最初，Claude 的身份过滤器似乎源于约束四类主要用户的需求：违反使用政策者、来自不支持地区的用户、违反服务条款者以及 18 岁以下的用户。

该组织希望打击那些重复违反 [Anthropic 使用政策](https://www.anthropic.com/legal/aup)的用户。作为一项旨在适应 AI 不断演变特性的灵活指令，该组织的使用政策有其专门的[博客式新闻更新流](https://www.anthropic.com/news/usage-policy-update)，用户可以在此获悉旨在防止网络侵权、限制政治内容以及防止[不受欢迎的智能体使用](https://thenewstack.io/why-ai-agents-need-their-own-identity-not-yours/)的变更。

为了方便起见，Anthropic [发布了一份支持的国家列表](https://www.anthropic.com/supported-countries)，列出了提供商业 API 访问和 Claude.ai 的地区，而不是列出一份确定的禁令名单。不支持的地点包括那些“常客”，即中国大陆、俄罗斯、伊朗、朝鲜和白俄罗斯。

一些非洲国家也不在支持名单之列。乌克兰在支持范围内，但被占领的克里米亚、顿涅茨克、赫尔松、卢甘斯克和[扎波罗热](https://en.wikipedia.org/wiki/Zaporizhzhia)地区被排除在外。

## 18 岁以下用户使用

虽然扎波罗热的一些用户会感到失望，但他们目前显然有更重要的问题要处理。更有可能的失望情绪正蔓延至 18 岁以下的用户群体，尤其是那些使用 Claude 进行计算机科学项目和学习的学生。

根据用户 [llm_nerd](https://news.ycombinator.com/user?id=llm_nerd) 本周在 [Hacker Noon](https://news.ycombinator.com/item?id=47775633) 上的发帖，他 15 岁的儿子因被要求提供证明其已满 18 岁的身份证件而被暂停了 Claude 账号。

“他有自己的 [Claude Max 订阅](https://thenewstack.io/anthropic-agent-sdk-confusion/)（他在他的游戏程序员圈子里的收入经常超过我），他和我一样，之前都不知道 Anthropic 有必须年满 18 岁的规定，”这位评论者写道。

Anthropic 的电子邮件称：“我们的团队发现有迹象表明您的账号由儿童使用。这违反了我们的规则，因此我们暂停了您访问 Claude 的权限。”

令人欣慰的是，该用户指出 Anthropic 给这位年轻的软件程序员退还了当月的全部订阅费，尽管当时该月已接近尾声。

[OpenAI 的使用条款](https://openai.com/en-GB/policies/row-terms-of-use/)确认 Codex 和 ChatGPT 对 13 岁以上的用户开放。谷歌 Gemini 应用的负责任使用和[年龄要求页面](https://support.google.com/gemini/answer/16109150?hl=en)也确认其服务向 13 岁及以上的用户开放。

## Anthropic 不会做的事情

Anthropic 表示它作为验证数据的“数据控制者”。这意味着它设定了数据如何使用以及保留多久的规则。用户身份证件和自拍由 Persona 收集并持有，而非存储在 Anthropic 的系统上。Anthropic 可以在需要时（例如审核申诉）通过 Persona 的平台访问验证记录，但它本身不会复制或存储这些图像。

“我们不会使用您的身份数据来训练我们的模型。验证数据仅用于确认您的身份并履行我们的法律和安全义务。我们收集的信息不会超过所需范围。我们只要求验证您身份所需的最少信息。我们不会与任何其他人分享您的身份数据，”Anthropic 的声明中写道。

这一进展可谓紧跟时代潮流。[澳大利亚针对 16 岁以下青少年的社交媒体禁令](https://www.bbc.co.uk/news/articles/cwyp9d3ddqyo)目前也正被英国政府考虑。

随着全球冲突不断上演，以及通过智能体服务层出现的新型网络漏洞，这类用户限制在一些人看来是合理的，但在另一些人看来则是商业领域的“保姆式国家”干预主义。