
<!--
title: 运行中的量子程序，为何无法调试？
cover: https://cdn.thenewstack.io/media/2025/09/4f43fd01-owl-illustration-agency-iu3jakrisay-unsplash.jpg
summary: 量子计算开发调试困难且昂贵，需高效算法。理想任务为小输入、大计算、小输出。工作流包括算法设计、编码、验证及性能评估。
-->

量子计算开发调试困难且昂贵，需高效算法。理想任务为小输入、大计算、小输出。工作流包括算法设计、编码、验证及性能评估。

> 译自：[Why You Can’t Debug a Running Quantum Computer Program](https://thenewstack.io/why-you-cant-debug-a-running-quantum-computer-program/)
> 
> 作者：Joab Jackson

从某种意义上说，为量子计算编写应用程序，很像是一种回到未来的情况。就像20世纪70年代的大型机程序员一样，今天的量子计算程序员必须在代码在实际硬件上运行之前对其进行调试，因为量子运行时本身非常昂贵，而且能力仍然相当有限。

事实上，从技术本身的性质来看，量子计算程序无法调试，至少在它们运行时不能。

在生产环境中测试？不可能。

“在量子硬件上运行非常昂贵，所以你不想等到代码运行到那里才发现有bug，” [Mariia Mykhailova](https://www.linkedin.com/in/mariiamykhailova/) 上周在为 [计算机协会](https://www.acm.org/about-acm) 举行的一次线上讲座中说，该讲座主题是开发者应牢记的量子计算行为。

Mykhailova 是量子初创公司 [PsiQuantum](https://www.psiquantum.com/software) 的首席软件开发人员，曾担任微软量子业务部门的工程师。她还在 [东北大学工程学院](https://coe.northeastern.edu/people/mykhailova-mariia/) 教授这门课程。

在讲座中，她介绍了一种量子软件开发工作流。这项工作不仅需要编写代码——涉及经典和量子语言——还需要验证量子程序的正确性，以及评估它们在容错量子计算机上的性能。

这次讲座很及时。随着 [微软 Azure](https://azure.microsoft.com/en-us/solutions/quantum-computing)、[亚马逊云科技](https://aws.amazon.com/braket/)、[IBM](https://quantum.cloud.ibm.com/) 等云提供商都提供 [量子计算服务](https://thenewstack.io/ibm-cracks-code-for-building-fault-tolerant-quantum-computer/)，现在可能是尝试量子计算的时候了。

## 量子计算机何时具有优势？

许多任务永远不适合 [量子计算](https://thenewstack.io/why-d-wave-thinks-quantum-is-the-next-step-for-blockchain/)。例如，需要摄取大量数据集的 [机器学习](https://thenewstack.io/machine-learnings-next-frontier-quantum-computing/) 可能就不适合。她说，图像识别、网络搜索或文本编辑是其他不会从量子计算中受益的应用程序。

请记住，将数据加载到经典计算机中既简单又便宜，但对于量子计算来说却相当麻烦。

“在量子计算中，以某种量子态加载输入数据以供后续使用，本身就是一项昂贵的操作，”她说。

她表示，理想的量子计算任务是输入有限、计算量大、输出有限。

她说，如今，大多数计算任务不需要 [量子能力](https://thenewstack.io/quantum-computing-use-cases-how-viable-is-it-really/)。她展示了一张图表，显示了各种可能的应用程序，这些应用程序的特点是解决它们所需的时间与问题本身的大小相关。

[![图表截图。 ](https://cdn.thenewstack.io/media/2025/09/14294dde-acm-quantum-mykhailova-00.png)](https://cdn.thenewstack.io/media/2025/09/14294dde-acm-quantum-mykhailova-00.png)

对于更大的问题，经典计算机和 [量子解决方案](https://thenewstack.io/microsoft-makes-quantum-computing-breakthrough-with-new-chip/) 都将消耗更多资源。

“当你从这些角度思考时，就会清楚哪些程序适合量子计算，哪些则不太适合，”她说。

量子计算对于小型应用程序没有优势。相反，量子计算最适合那些经典计算机即使能完成也需要极长时间才能完成的任务。

一个这样的例子是寻找分子的基态能量。经典计算机可以轻松地对氢等简单分子进行快速分析。她说，理解更大、更复杂的分子将是量子计算的领域。

因此，开发量子软件的首要任务是评估其性能，以确定一开始使用量子程序是否具有优势。

## 嘈杂且缓慢的量子硬件带来的挑战

有一点需要记住，[量子计算机](https://thenewstack.io/googles-quantum-computer-can-exponentially-suppress-errors/) 实际上很慢，比传统计算机系统慢得多：在量子计算系统上的一次查询远比在经典计算机上慢。

为什么会这样？量子计算机很嘈杂，所以每一个逻辑门的运行都必须进行纠错。此外，门本身速度很慢，而且在可预见的未来，大多数量子计算系统将只有极少数的门。

因此，你开发的算法必须高效，并且必须在投入硬件运行之前进行彻底测试。

![软件开发工作流](https://cdn.thenewstack.io/media/2025/09/e418b20b-acm-quantum-mykhailova-01.png)

*开发量子应用程序的工作流——甚至在它接触硬件之前。*

Mykhailova 建议：“你需要弄清楚这个解决方案是否足够好。你需要评估它的性能。你需要基本确定它需要多少资源，包括你需要的资源量以及任务将花费多长时间。”

如果任务花费太长时间，就得回到最初的方案。

## 调试量子程序的独特困难

正如 Mykhailova 所说，在实际量子硬件上进行测试是昂贵的。而且，像任何调试一样，你需要多次运行。

此外，由于量子计算的性质，“状态”无法直接测量。开发者逐行调试程序的流程将不起作用。“这样做会破坏你的状态，”她说。

它们的嘈杂性质也同样是个问题：如果你得到一个错误的结果（甚至是一个正确的结果），你不知道是因为系统噪音，还是因为算法操作不正确，或者说它操作正确，具体情况而定。

好消息是，有模拟器可以帮助进行这些估算。量子模拟软件运行在经典硬件上，但通过许多相同的操作来复制量子计算机。此外，它们提供了传统的调试工具。这些工具对于需要大约30个量子比特的程序运行良好。

她表示，如何测试更大的量子计算程序仍然是一个“悬而未决的问题”。

她举例说明了 [一个例子](https://www.psiquantum.com/news-import/psiquantum-launches-construct)，如何准备一组量子比特来为机器产生一个“状态”。

## 开发量子应用程序的工作流

第一步是设计算法以实现你想要的功能，并将其格式化为电路图，以说明量子比特的多种版本。

[![量子比特设计图。](https://cdn.thenewstack.io/media/2025/09/726e10fa-acm-quantum-mykhailova-03.png)](https://cdn.thenewstack.io/media/2025/09/726e10fa-acm-quantum-mykhailova-03.png)

下一步是编写代码。她的示例是用 [Python](https://thenewstack.io/what-is-python/) 编写的，并利用 PsiQuantum 的 *psiqworkbench* 库在代码中表达量子比特（qubits）和量子逻辑块（qubricks）。

生成的程序混合了经典计算和量子计算，并使用了特定的方法来表达门。她使用 [Pytest](https://docs.pytest.org/en/stable/) 来验证代码，并将正确的结果嵌入代码本身进行验证。

从这些数字中，你还可以估算运行程序所需的量子比特数量，并与经典方法进行比较，或者仅得出算法是否需要改进的结论。根据需要重复。

## 学习如何进行量子编程

Mykhailova 大力提倡通过实践学习，她建议通过编写量子程序来学习这门技艺。她建议通过微软的 [量子Kata](https://quantum.microsoft.com/en-us/tools/quantum-katas) 网站学习基础知识。然后更深入地学习微软的 [Q# 语言](https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview)、IBM 的 [Qiskit](https://www.ibm.com/quantum/qiskit) 软件栈，以及她撰写的关于该主题的 [两本书](https://www.oreilly.com/library/view/q-pocket-guide/9781098108854/) [籍](https://www.manning.com/books/quantum-programming-in-depth)。

别担心，你不需要懂量子物理学也能编写量子计算机程序。

她表示：“从本质上讲，量子计算是线性代数和概率论。”

“如果你在堆栈的最底层工作，也就是控制实际物理对象和实现量子计算机的物理过程的层面，那么你需要专门了解物理学，”但大多数开发者不需要。量子比特被渲染成易于理解的数学构造。

Mykhailova 说：“如果你从事编译栈或面向用户的软件开发，就像我一样，你就不需要了解物理学。那部分内容在你之下被抽象了好几个层。”

ACM 将限时 [免费在线提供](https://events.zoom.us/ev/AqZToK3BMn0keNLwD_ZBBgJ4H7Oo-_7wU_KUBe1OhmVRoo7qzpLX~AuM0BSSw2kkvpz7I7HvUbkNNGsZDwOXtw8IGKL3t1h6StnkybixUsSuLvg) 这场讲座的回放，但最终它将被移至 [存档页面](https://learning.acm.org/techtalks-archive)。