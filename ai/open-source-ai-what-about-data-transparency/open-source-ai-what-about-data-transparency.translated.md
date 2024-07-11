# 开源人工智能：数据透明度如何？

![Featued image for: Open Source AI: What About Data Transparency?](https://cdn.thenewstack.io/media/2024/07/4a926a0a-open-source-ai-what-about-data-transparency-2-1024x576.jpg)

纽约 - 在联合国[OSPOs for Good Conference](https://www.un.org/techenvoy/content/ospos-good-2024)上，我们再次被提醒了人工智能和开源程序的奇特状况：虽然人工智能的基础建立在[开源工具和库](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)上，但几乎没有主要的 AI 程序是真正开源的。OpenAI 的[ChatGPT](https://thenewstack.io/how-to-learn-unfamiliar-software-tools-with-chatgpt/)、[Google](https://cloud.google.com/?utm_content=inline+mention) 的 PaLM（及其继任者，多模态[Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/)）和 Meta 的[Llama-3](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/) 通常被吹捧为开放的，但它们并非如此。它们附带了不符合开源软件定义的重大限制。

[开源倡议组织 (OSI)](https://opensource.org/) 作为[开源定义](https://opensource.org/osd) 的管理者，认识到人工智能日益增长的重要性和该领域需要清晰度，因此 OSI 已经开始了一个雄心勃勃的项目，旨在[定义“开源人工智能”](https://thenewstack.io/open-source-ai-osi-wrestles-with-a-definition/) 的含义。这项工作汇集了 70 位专家，包括研究人员、律师、政策制定者以及来自[亚马逊](https://aws.amazon.com/?utm_content=inline+mention)、谷歌和 Meta 等科技巨头的代表。

说起来容易做起来难。正如 OSI 执行董事[Stefano Maffulli](https://www.linkedin.com/in/maffulli/) 在关于开源和人工智能的小组讨论中指出的那样，“虽然人们对总体原则达成广泛共识，但很明显，魔鬼在细节中。”

开源社区是一个大帐篷，涵盖了从地下黑客到基层活动家再到财富 500 强公司的所有人，每个人都有自己的优先事项和关注点。

简而言之，“在开源人工智能的实际含义方面，我们需要新的护栏和新的指南，”[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 首席营销和战略官[Ashley Kramer](https://www.linkedin.com/in/ashleyekramer/) 在小组讨论中说。

## LLM 数据透明度：一个棘手的问题

小组讨论中清楚地表明，定义开源人工智能的最大挑战在于解决训练数据的作用。[大型语言模型 (LLM)](https://thenewstack.io/llm/) 依赖于庞大的数据集，这些数据集通常是从互联网上抓取的，没有明确的许可。这些混乱的数据引发了关于隐私、版权和伦理的棘手问题。

事实上，我们知道其中一些数据完全是非法的。“最近用于训练许多图像生成 AI 工具的最大图像数据集之一[[LAION-5B] 包含儿童性虐待图像](https://cyber.fsi.stanford.edu/news/investigation-finds-ai-image-generation-models-trained-child-abuse),” Maffulli 说。“我们需要数据集维护者注意到并删除这些内容。”

OSI 的[草案定义](https://hackmd.io/@opensourceinitiative/osaid-0-0-8) 试图通过关注与开源软件传统相关的“四大自由”来回避数据问题：使用、学习、修改和分发 AI 系统的自由。它关注的是代码，而不是数据。

是否应该要求开源 AI 模型披露其训练数据？如果是，如何才能在隐私问题和共享 PB 级信息带来的实际挑战之间取得平衡？对于 OSI AI 定义草案的许多批评者来说，答案不仅仅是肯定，而是“绝对肯定”。

正如亚马逊网络服务公司首席开源技术策略师[Tom Callaway](https://www.linkedin.com/in/spotfoss/) 在会议之前在 LinkedIn 上写道的那样，“[没有数据就无法构建 LLM](https://www.linkedin.com/posts/spotfoss_imagine-with-me-for-a-moment-we-get-ten-activity-7214937063723319296-DSur/?utm_source=share&utm_medium=member_desktop)。没有数据，LLM 不仅缺乏任何目的，它根本不存在。这使得数据成为 LLM 的功能性和必需的源组件。”

他和其他人认为，任何关于开源人工智能的定义，如果不解决数据问题，都是不完整的。

Maffulli 承认这是一个真正的担忧：“这需要辩论和最终确定。”但他补充说，“推动数据彻底开放存在弊端，也会带来问题。因此，这将是意图和对公众最有利的结果之间的平衡。”
然而，另一位小组成员，[Sasha Luccioni](https://www.linkedin.com/in/sashaluccioniphd/)，Hugging Face 的人工智能和气候负责人，则持不同观点。Luccioni 认为，成为开源纯粹主义者是一个错误。

“你不能指望所有公司都 100% 开源，因为这受开源许可证的定义，”她在小组讨论中说。“这就是为什么存在多种许可证的原因。说这不是真的，开源会让公司感到反感。你不能指望公司放弃他们赚钱的一切，并以他们感到舒适的方式这样做。”

她认为，“存在一种负责任的人工智能许可证”，它对开源友好，“你可以定义自己的开源条款。通过稍微调整语言，你可以以一种让公司、政府和学术界都感到舒适的方式向前发展，而不是说这个项目或许可证不是开源的。

## “我们必须共同努力”
在 The New Stack 采访过的所有开源倡导者中，没有人对这种观点感到满意。无论 OSI 人工智能定义如何，什么是开源人工智能，什么不是开源人工智能，这个问题对开源社区来说仍然至关重要。

这在开源社区之外也很重要。正如肯尼亚科技特使 [Philip Thigo 大使](https://www.linkedin.com/in/philip-thigo) 在一个专门针对开源和人工智能的会议上的主题演讲中所观察到的，“开源人工智能确保许多全球南方社区能够构建自己的 AI 程序和 LLM。”

这些国家无力为其人工智能需求支付 OpenAI 的费用。他们需要开源、全球标准和互操作性来构建人工智能系统，以解决他们的健康、气候和教育需求。

展望未来，“我们必须共同努力，”Kramer 在会议小组中说，表明开源是实现这一目标的方式。

“我们必须了解模型的基础数据，”Kramer 说。“虽然我喜欢人工智能的炒作，也喜欢它前进的方向，但我们在互联网和云技术的兴起中看到了非常相似的模式。我们行动越快，错过的东西就越多。因此，需要一个团队，需要一个开源人工智能护栏模型来真正弄清楚如何快速实现这一目标，同时将隐私、信任和安全放在首位。”

敬请关注。我们仍在书写开源人工智能的故事。随着 OSI 和其他人努力解决这些复杂问题，结果将对人工智能开发、创新和治理的未来产生深远的影响。挑战在于找到一个既能保持开放精神又能解决数据带来的独特挑战的定义。这项任务可能需要重新思考关于在人工智能时代“开源”意味着什么的某些长期假设。

[
YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)