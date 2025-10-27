在旧金山举行的本周 [PyTorch 2025大会](https://events.linuxfoundation.org/pytorch-conference/?__hstc=132719121.c7e7a3a3b1b149ab85ef60029fb25108.1761329988449.1761329988449.1761329988449.1&__hssc=132719121.3.1761329988449&__hsfp=3360764624&ajs_aid=913fde38-5396-42fb-9661-2bbde650c913)上，我与 [Luca Antiga](https://www.linkedin.com/in/lantiga/) 进行了交流。他是 [PyTorch基金会](https://pytorch.org/) 技术咨询委员会主席，也是端到端人工智能平台Lightning AI的首席技术官。Antiga是撰写原始 [PyTorch论文](https://papers.nips.cc/paper_files/paper/2019/hash/bdbca288fee7f92f2bfa9f7012727740-Abstract.html) 的团队成员之一，并合著了 [《PyTorch深度学习》](https://www.manning.com/books/deep-learning-with-pytorch) 一书。还有谁比他更适合聊聊PyTorch本身的现状并了解PyTorch基金会的最新动态呢？

视频

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道，观看我们所有的播客、采访、演示等内容。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

Antiga的学术背景实际上是生物医学工程，他指出PyTorch [之所以如此受欢迎](https://thenewstack.io/why-pytorch-gets-all-the-love/) 的原因之一是它对研究人员非常友好。这些研究人员最终毕业或进入科技行业工作时，也将PyTorch带了过去。

“它非常‘Pythonic’，”Antiga解释道。“而在过去，有许多框架是用Python编写的，但你需要用一种介于你自身问题之间的元语言进行编码，这使得调试变得困难得多，等等。从这个意义上讲，PyTorch是革命性的，因为它将Python的易用性和迭代速度，以及Python所具有的‘倾向于行动’的特性，带入了神经网络、反向传播和GPU计算的世界。”

PyTorch创建时，行业仍专注于神经网络——通常用于图像或情感分析。随后，ChatGPT将生成式AI（GenAI）带给了更广泛的受众，但Antiga认为PyTorch始终保持着其重要性。

“在所有这些变革中，你总能看到PyTorch的身影，”他说。“当然，也有JAX等其他非常强大的框架。但相比之下，PyTorch是一个完整的行业，并为整个行业赋能。随之而来的是一个庞大的生态系统。”

虽然PyTorch最常与模型训练相关联，但它现在也已成为在生产环境中运行模型的关键。

“如果你去看看最受欢迎的推理框架——vLLM、SGLang——它们都运行PyTorch，对吗？它们在生产环境中运行PyTorch，”Antiga指出。“如果你今天与任何聊天机器人互动，很可能那时你正在运行PyTorch。”

PyTorch近期受欢迎的另一个原因是，强化学习——它会奖励模型正确的行动并在模型采取错误行动时提供负面反馈——现在正被常规地用于 [微调预训练的大型语言模型](https://huggingface.co/learn/llm-course/en/chapter12/2)（LLM）。事实证明，PyTorch也非常适合这种用例。

“强化学习会鼓励模型在面对一个可以采取行动、环境状态会改变并能从行动中获得奖励的环境时，更多地做那些有效的事情，”Antiga解释道。

## PyTorch基金会的现状

至于PyTorch基金会本身，值得注意的是，仅仅几个月前，该基金会才 [开始引入更多项目](https://pytorch.org/blog/pt-foundation-expands/)，最初是vLLM和DeepSpeed。随着流行的用于扩展AI和Python应用的开源分布式计算框架Ray的加入，基金会现在已经 [增加了第四个项目](https://thenewstack.io/ray-comes-to-the-pytorch-foundation/)。

但Antiga强调，该计划并非要成为一个大型的伞状基金会。

“我在生态系统中最关心的是用户。当用户接触到PyTorch基金会认可的生态系统时，他们会经历怎样的旅程，”他解释道。“我的目标是让他们成功。”

如需了解更多我们的对话内容，请订阅我们的播客或在YouTube上观看完整采访。