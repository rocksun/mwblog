这种承诺令人难以抗拒：用简单的英语描述你想要什么，人工智能就能输出可用的代码。这种“[氛围编程](https://thenewstack.io/vibe-coding-and-you/)”方法让从创业公司创始人到企业CTO的每个人都在想，五年后他们是否还需要程序员。

[Java](https://thenewstack.io/introduction-to-java-programming-language/) 的创建者 [James Gosling](https://www.linkedin.com/in/jamesgosling/) 今年早些时候与 The New Stack [分享了他的想法](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/)，他说“一旦你的[氛围编程]项目变得稍微复杂，它们几乎总是会崩溃。” 他补充说，氛围编程“还没有为企业做好准备，因为在企业中，[软件]必须每次都能他妈的正常工作。”

在与 Java 平台提供商 [Azul Systems](https://www.azul.com/) 的副 CTO [Simon Ritter](https://www.linkedin.com/in/siritter/) 谈论 [AI 代码生成](https://thenewstack.io/the-ai-code-generation-problem-nobodys-talking-about/)之后，两个根本问题不断浮出水面，表明 Gosling 的怀疑是有充分根据的。

## 垃圾进，垃圾出

第一个问题是训练数据。人工智能编码工具从现有的代码仓库中学习——比如 GitHub 和 [Stack Overflow](https://thenewstack.io/stack-overflows-plan-to-survive-the-age-of-ai/)。但问题是：他认为，那里的大部分代码都不是很好。

“你可以建议，‘好吧，让我们只使用 GitHub 上的所有代码，’” Ritter 说，他是一位软件架构师，数十年来一直在构建企业系统。“这会给你好的代码吗？可能不会。”

他指出，GitHub 上充斥着被放弃的实验、学生项目和快速的临时解决方案。Stack Overflow 的答案通常优先考虑让某些东西能够运行，而不是让它正确运行。Ritter 说，与在人类知识的集合智慧上训练 ChatGPT 不同，没有明显的、始终如一的优秀代码来源，来满足人工智能训练所需的规模。

在计算机科学中，垃圾进意味着垃圾出。用平庸的代码训练人工智能，你就会得到平庸的结果。

## 英语问题

Ritter 告诉 The New Stack，第二个问题是 [英语是一种糟糕的编程语言](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/)。

考虑这句话：“The chicken is ready to eat.”（鸡已经可以吃了。）我们说的是一只活鸡准备做晚餐，还是做熟的鸡可以吃了？这两种理解都是完全有效的，他说。

或者试试这条购物指令：“Get two pints of milk, and if they have eggs, get 12.”（买两品脱牛奶，如果他们有鸡蛋，就买 12 个。）12 个什么——鸡蛋还是品脱牛奶？这种歧义就存在于语言中。

“这实际上是我们首先拥有编程语言的原因之一，”Ritter 解释说。[编程语言](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/)的存在恰恰是因为自然语言是模棱两可的。编译器只能以一种方式解释“if (x > 5)”。没有误解的余地。

你可以尝试在你的英语描述中更加精确，但总有另一个极端情况，另一种误解你意思的方式。Ritter 说，这就是为什么我们首先放弃自然语言进行编程的原因。

## 人工智能真正有帮助的地方

这些并不意味着人工智能对编码毫无用处。它已经在某些特定方面证明了自己的价值：

具有人工智能辅助功能的 [现代 IDE](https://thenewstack.io/best-open-source-ides/) 确实很有帮助。设置一个 X 坐标，系统通常会正确地建议接下来设置 Y 坐标。这种细粒度的代码补全使开发人员的工作效率更高，而不会产生生成整个应用程序的可靠性问题。

当需求具体且有界限时，人工智能也擅长生成单独的方法或类。需要一个用于已知模式的数据库访问类？人工智能可以很好地处理。想要重构遗留代码？人工智能可以对现有实现进行现代化改造，其中原始意图可以从上下文中清楚地看出。

对于快速原型设计和个人项目——比如我与 [DevOps](https://thenewstack.io/introduction-to-devops/) 先驱 [Gene Kim](https://www.linkedin.com/in/realgenekim/) 进行 [氛围编程](https://thenewstack.io/devops-pioneer-vibe-coding-100x-bigger-than-devops-revolution/) 的 [NFL 球队追踪应用程序](https://thenewstack.io/devops-pioneer-vibe-coding-100x-bigger-than-devops-revolution/)——氛围编程效果很好。如果它坏了，你耸耸肩再试一次。

但这正是 Java 的企业主导地位变得重要的地方。Java 不是为快速实验或一次性代码而设计的。它是为长期使用而构建的——应用程序需要可靠地运行数年或数十年，并由在编写原始代码时不在场的开发团队维护。

[Java 生态系统](https://thenewstack.io/azul-cto-java-at-30-still-rules-enterprise-dev/) 反映了这一现实。Ritter 说，企业 Java 应用程序通常涉及广泛的框架、严格的测试协议和详细的文档要求。这些不是可有可无的东西；当你的代码处理数百万笔金融交易或管理患者医疗记录时，它们是必需品。

## 企业现实

企业开发是不同的。当你构建处理医疗保健数据、金融交易或关键基础设施的系统时，“耸耸肩再试一次”是不可行的。

企业应用程序需要广泛的单元测试。你是否会信任 [人工智能生成的测试](https://thenewstack.io/ai-is-testing-ai-generated-code-should-you-trust-it/) 来验证人工智能生成的代码？Ritter 问道。它们需要严格的代码审查，这意味着熟练的开发人员必须理解和验证每一行代码——这在某种程度上与 [消除程序员](https://thenewstack.io/github-ceo-on-why-well-still-need-human-programmers/) 的目的背道而驰，他说。

然后是维护。企业应用程序通常运行数十年。未来的开发人员需要理解和修改不是由人类编写的代码，而是基于从一开始就可能含糊不清的自然语言规范。

“大多数人都会进行代码审查，”Ritter 在谈到严肃的开发时说。“你将需要有能力做到这一点的人，所以你实际上是在降低试图消除对程序员的需求的好处。”

## 真正的未来

氛围编程不会消除编程工作——至少对于重要的工作来说不会。他说，未来可能更像是复杂的自动完成，而不是完全的代码替换。

这不一定是坏消息。编程语言总是 [朝着更高级别的抽象发展](https://thenewstack.io/power-apps-plans-feature-vibe-ifies-business-app-dev/)。我们从汇编语言发展到 C 语言，再到 Java 语言，再到现代框架，每一步都让开发人员的工作效率更高，同时保持了 [严肃软件](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) 所需的精度，Ritter 说。

毫无疑问，人工智能将在这种发展中发挥更大的作用。但是 [自然语言的模糊性](https://thenewstack.io/machine-learning-still-struggles-to-extract-meaning-from-language/) 和 [软件精度](https://thenewstack.io/relax-about-your-dora-metrics/) 之间的根本张力表明，人类程序员不会很快消失。