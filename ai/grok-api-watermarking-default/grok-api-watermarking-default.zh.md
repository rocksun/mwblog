![An illustration depicting an on/off switch.](https://cdn.thenewstack.io/media/2026/11/082ecce8-allison-saeng-skfgtjrao0o-unsplash-1024x576.jpg)

过去一周，关于为AI生成的文本添加水印这一棘手问题迎来了戏剧性的转折——[SpaceXSI](https://x.ai/) 似乎对其自动为 [Grok AI 模型](https://thenewstack.io/grok-4-7-agent-stamina/)生成的文本添加水印的计划来了个大转弯。

根据其更新后的[输出水印文档](https://docs.x.ai/developers/advanced-api-usage/watermarking)，埃隆·马斯克的这家AI公司（最近[从 SpaceXAI 更名为 SpaceXSI](https://www.reuters.com/business/media-telecom/musk-says-he-will-rename-spacexai-spacexsi-2026-10-04/)）表示，该功能现在默认关闭，开发者可以通过其团队的管理设置针对单个模型启用该功能。

水印功能本身的消息在10月下旬开始浮出水面，尽管当时并没有正式的公开公告。互联网档案馆（Internet Archive）的 Wayback Machine 在11月1日和11月6日分别保存了[早期版本的文档](https://web.archive.org/web/20261106053200/https://docs.x.ai/developers/advanced-api-usage/watermarking)，它与现有版本有很大不同，其中指出从11月7日起，水印功能将默认*开启*。这一即将到来的变动在10月31日[被一些 X 用户](https://x.com/XFreeze/status/2116585881457119513)[发现](https://x.com/XCurran_/status/2116654648082022668)。

然而，SpaceXSI现在已经改变了方向，将水印变成了一个可选功能，供通过其API使用Grok的开发者使用。一个在线文档存档服务 Spybara [表明，这一变化发生在](https://spybara.com/xai/api/history/docs/en/2026-11-09-2300..2026-11-10-0959/)周一晚（11月9日）到周二早（11月10日）之间的某个时间，这表明在原定的11月7日推出之后，文档在近三天的时间里继续将水印描述为默认启用。

> “然而，SpaceXSI现在已经改变了方向，将水印变成了一个可选功能，供通过其API使用Grok的开发者使用。”

该公司并未对这一改动给出公开解释，目前尚不清楚最初的*默认开启*政策是否曾全面生效。

## 满足水印合规要求

简单回顾一下，文本水印是一种将隐式的、机器可读的信号嵌入到AI生成文本中的技术。该过程会微妙地影响模型在生成回答时选择哪些词或 Token，在足够长的文本段落中，这些选择会产生一种可被后续检测到的统计模式，从而帮助确定它是否源自AI模型。

检测通常需要访问专门的工具，主要的模型实验室将其水印检测器的访问权限限制给获批的申请人。

这项技术在欧洲变得越来越重要，[欧盟AI法案](https://thenewstack.io/a-field-guide-to-2026-federal-state-and-eu-ai-laws/)为生成合成内容的AI系统提供商引入了透明度义务。根据[第50条第(2)款](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)，提供商必须确保AI生成的文本、图像、音频和视频以机器可读的格式进行标记，相关规定已于[2026年8月2日生效](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline)。随后的修正案为在8月2日之前已投放市场的系统引入了一个有限的宽限期，直到12月2日，这意味着尚未满足要求的AI公司时间已经不多了。

值得注意的是，各大AI公司对文本水印合规义务采取了不同的方法。8月，[Anthropic 成为首批宣布文本水印的主要 AI 实验室之一](https://thenewstack.io/anthropic-claude-text-watermark/)，在所有受支持的 Claude 模型和产品（包括其 API）中全球范围内应用该功能。这一决定[被证明在一定程度上](https://www.businessinsider.com/anthropic-claude-text-watermark-concerns-tech-community-answers-2026-8)引发了争议，[特别是对于担心水印](https://www.wired.com/story/coders-say-they-already-found-workarounds-to-claudes-invisible-watermarks/)会[如何影响生成代码的开发者而言](https://www.forbes.com/sites/maryroeloffs/2026/08/11/claude-will-put-invisible-watermarks-on-ai-text-and-images-and-the-internet-isnt-happy/)，而且 Anthropic 没有提供任何退出的机制。

与此同时，OpenAI [在10月效仿了这一做法](https://thenewstack.io/openai-api-text-watermarking/)，推出了自己的名为 textGrain 的文本水印系统。然而，它采取了不同的方法，对API开发者让该功能保持可选，同时在欧盟对符合条件的 ChatGPT 和 Codex 文本输出引入自动水印。

就谷歌而言，在过去的几年里，它一直在各种产品和服务（包括其 Gemini API）中部署自己的 [SynthID](https://deepmind.google/models/synthid/) 水印技术。该技术支持文本以及图像、音频和视频，文本水印在模型生成回应时嵌入到模型的输出中。7月，[该公司确认](https://blog.google/company-news/outreach-and-initiatives/public-policy/eu-ai-act-transparency-code-of-practice/)其正在签署欧盟的《AI生成内容透明度行为准则》。

值得注意的是，SpaceXSI 更新后的文档也证实其正在将 SynthID Text 用于自己的水印功能。

## 心态转变

SpaceXSI [是唯一一家未签署](https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content)欧盟《AI生成内容透明度行为准则》的大型 AI 实验室，当时[至少有一份报道](https://www.cityam.com/chatgpt-might-follow-claudes-watermark-pledge-but-grok-to-swerve-it/)表明它将避开给 Grok 的文本添加水印。

然而，SpaceXSI 文档在10月下旬的出现，是其正准备加入这一行列的第一个明确迹象。最初的文本对该公司的基本原理做了非常明确的说明。“SpaceXSI 为文本模型输出添加水印以符合欧盟AI法案，”文档指出。

> “水印可以帮助实现对欧盟AI法案的合规。”

该声明此后被更谨慎的措辞所取代。“水印可以帮助实现对欧盟AI法案的合规，”现在的表述如此。

![SpaceXSI's updated output watermarking text ](https://cdn.thenewstack.io/media/2026/11/24ffdb9e-torn-paper-watermarking-note-1024x260.png)

*SpaceXSI 更新后的输出水印文本*

这种转变值得注意，因为最初的措辞反映了一项政策，即 SpaceXSI 承担起自动为 Grok 的输出加水印的责任，表面上是为了遵守欧盟AI法案。现在，该公司似乎正在将启用水印的责任转交给开发者，同时对这项技术是否足以满足该集团的法律要求持更谨慎的态度。

这一切也带来了一些实际后果。[该功能是在团队级别进行控制的](https://docs.x.ai/developers/advanced-api-usage/watermarking#how-to-enable-text-watermarking)，这意味着管理员可以为单个 Grok 模型启用或禁用水印，该设置适用于属于该团队的每个 API 密钥。没有针对单个请求开启或关闭水印的选项，这意味着为不同地区的客户提供服务的开发者无法在单个团队内的同一模型上应用不同的水印政策。为此，他们需要维护单独的团队配置。

该公司修改后的文档确定，水印功能适用于包括 Grok 4.7 和 4.6 在内的七个 Grok 模型，但默认情况下是禁用的。目前尚不清楚的是，为什么 SpaceXSI 放弃了其先前宣布的使该功能自动化的计划。

*The New Stack* 已联系 SpaceXSI 获取置评，并将在收到回复时（如果有的话）进行更新。

文章出处：[SpaceXSI 悄然将 Grok API 文本水印默认设置为关闭](https://thenewstack.io/grok-api-watermarking-default/) 载于 [The New Stack](https://thenewstack.io)。