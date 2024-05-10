## Orchestrating AI: An Event-Driven Architecture for Complex AI Workflows
![Featured image for Orchestrating AI: An Event-Driven Architecture for Complex AI Workflows](https://cdn.thenewstack.io/media/2024/05/778916c3-orchestrating-ai-1024x576.jpg)
In the current AI frenzy, implementing complex [AI](https://thenewstack.io/ai/) workflows has become increasingly popular among companies looking to augment their product offerings with AI capabilities. In this article, I will share the behind-the-scenes of how we implemented an [Event-Driven Architecture (EDA)](https://thenewstack.io/the-basics-of-event-driven-architectures/) at Gcore to handle complex AI workflows.
I will walk you through the initial challenges, architectural decisions made, and the outcomes of adopting EDA in a dynamic real-world scenario, showcasing how EDA enhances system responsiveness, scalability, and flexibility to manage AI-powered tasks, such as subtitle generation for video content.
## Why Event-Driven Architecture Is Essential for AI
EDA is a design pattern that centers around the production, detection, consumption, and reaction to events, rather than around static predefined operations. An event is any significant change in state or update that occurs within a system. EDA allows different parts of a system to communicate and operate independently, driven by the occurrence of these events, which can be anything from user actions to completed processes.
Adopting EDA in AI workflow management marks a significant evolution from traditional [architectures](https://roadmap.sh/software-architect) (such as monolithic, service-oriented, or polling-based architectures). Its principles of asynchronous communication, decoupling, and dynamic scalability align perfectly with the demands of modern AI applications, offering three major advantages:
- The modularity of the architecture makes it easier to scale specific components independently, such as scaling language processing during peak hours for a customer service application, without affecting other parts of the system.
- EDA’s modular design simplifies the process of updating or replacing models with newer versions, as seen in healthcare tech environments where predictive algorithms are frequently optimized and deployed to keep up with medical advancements or updated data.
- The flexible nature of EDA allows for seamless integration of various models to achieve complex AI workflows, such as combining image recognition with predictive maintenance in manufacturing, enhancing system robustness and operational efficiency.
These advantages observed across different industries augment the scalability and responsiveness of AI systems, also boosting their robustness and adaptability, making EDA a must-have for managing complex multi-model AI workflows across industries and use cases.
## Implementing Event-Driven Architecture in AI: A Real-World Case Study
At Gcore, we implemented EDA in our [Gcore Streaming Video AI capabilities](https://gcore.com/streaming-platform/ai-for-video). One of the ways we applied EDA is in using AI to generate subtitles for videos.
The initial goal of this project was to improve the efficiency, latency, scalability, and reliability of generating subtitles in multiple languages from raw video content. This process involves several complex steps:
**Video Decompression:** The video file is decompressed or transcoded into a suitable format for processing.
**Speech Detection:** Specialized machine learning (ML) models are used to identify the parts of the video where speech occurs, differentiating it from background noise or silence.
**Speech-to-Text (Transcription):** The detected speech is converted into text. This step requires inferencing using complex speech recognition models capable of handling multiple languages, accents, and dialects.
**Text Post-Processing:** Transcription errors, punctuation, and grammar are corrected. The text is formatted to match the timing of the video; for example, it can be broken down into timed subtitles.
**Translation (Optional):** If subtitles in multiple languages are required, the transcribed text can be translated into one or more target languages, again by inferencing using specialized machine translation models.
**Subtitle Synchronization:** The timing of the subtitles is matched with the speech in the video so that the subtitles appear on the screen precisely when the corresponding speech is heard.
![Diagram of the six steps in the AI subtitle generation architecture](https://cdn.thenewstack.io/media/2024/05/12e4455b-subtitle-synchronization-gcore.png)
Diagram of the six steps in the AI subtitle generation architecture
Each of these steps requires specialized AI models or algorithms and may need to process data in real time or near real time, especially in live streaming scenarios. The result? Serious complexity.
### 复杂性与 AI 工作流编排

复杂性不仅源于与每项任务相关的技术挑战，还源于高效管理步骤间的数据流、处理错误或异常以及根据需求动态扩展资源的需要。

在追求编排如此复杂且要求苛刻的 AI 工作流时，我们设计了一个 [AI 系统](https://gcore.com/streaming-platform/ai-for-video)，它通过明确定义的 EDA 精准而敏捷地运行。此平台的架构概述在下图中，它解决了 AI 驱动任务的所有阶段，促进了组件之间的通信，并确保每项任务都可以动态扩展并自主处理。

![Gcore 流媒体平台架构图](https://cdn.thenewstack.io/media/2024/05/060256d0-streaming-ai-architecture-gcore.png)

## Gcore 流媒体平台 AI 字幕生成工作流

四个 [核心组件](https://thenewstack.io/why-staying-updated-with-your-software-stack-matters/) 构成了 Gcore 流媒体 AI 平台后端。所有这些组件都是多功能的，并且对于广泛的 AI 应用程序至关重要。

### Django：API 服务

该架构的前端是 API 服务，它使用强大的 Django 框架。这是用户交互的主要界面，并处理对各种服务的传入请求，包括 [转录](https://gcore.com/docs/streaming-platform/video-hosting/ai-for-video/generate-ai-subtitles-and-add-them-to-video) 和内容审核服务，如 [裸露检测](https://gcore.com/docs/streaming-platform/ai-video-service/ai-nudity-detection)。此层验证并解析传入请求，触发工作流中后续任务的级联，如上图最左侧所示，用户向 API 服务发起转录请求。

### Celery：处理引擎和任务编排

深入后端，我们利用 Celery，这是一个异步任务队列，充当强大的后台处理引擎。Celery 的任务是管理 AI 进程，例如将音频转录为文本或分析内容以查找裸露，以及其他独立进程，例如将转录的内容同步到字幕中。Celery 与充当消息代理的 Redis 结合使用，编排这些任务并确保每个任务的启动和完成都由预定义事件的发生驱动。

Celery 处理 AI 工作流的能力通过一系列用于编排复杂工作流的高级功能得到增强：组、链和和弦。这些工具允许将高级、复杂的 AI 任务分解为细粒度的子任务，处理它们的依赖关系，并汇总它们的结果。

### Redis：代理和中介模式

[Redis](https://redis.com/?utm_content=inline+mention) 在我们的系统中扮演着至关重要的角色，作为代理和中介，管理着后端的任务分配和协调。它利用其快速、内存中数据结构存储来高效地处理任务队列。在架构中，任务签名和链充当控制任务执行流程和逻辑的中介。这种中介基于指示任务完成的事件信号。

Redis 快速处理这些信号的能力对于维持动态且响应式的工作流至关重要，如上图所示：任务由 Redis 代理接收并定向到适当的处理容器，并在推理后收集其结果，以实现无缝的任务转换和数据完整性。

### AI Celery 工作器：专用的 AI 任务处理

每个 AI Celery 工作器都致力于一项特定的 AI 任务，部署和管理 AI 模型，例如 [Whisper](https://thenewstack.io/when-cloud-meets-intelligence-inference-ai-as-a-service/) 用于转录，Pyannote 用于语音活动检测 (VAD)。这些工作器在隔离的环境中运行，以便以受控且安全的方式处理每项任务，最大程度地降低任务之间相互干扰的风险。此设置通过允许每个工作器根据任务需求独立扩展来增强我们系统的可扩展性，同时确保 AI 模型执行的高可靠性和效率。

## 系统要求：可扩展性、可靠性和延迟

我刚才描述的 Gcore 后端产生了三个主要好处，这些好处对于 AI 工作流尤为重要：可扩展性、可靠性和延迟降低。

### 可扩展性

该平台通过动态分配云资源并利用 GPU 加速来处理密集型 ML 任务，从而扩展以处理不同的需求。这确保了无缝扩展，避免了传统系统中常见的性能瓶颈和高成本。通过实时调整计算能力，该系统在高峰期和非高峰期都能有效地管理工作负载，而不会影响性能。

### 可靠性
## Gcore 视频流 AI 功能

Gcore 视频流 AI 功能均设计为高可靠性，具有强大的容错能力和复杂错误处理功能。数据复制和自动恢复机制等策略可确保系统在故障期间也能持续运行。在视频转录中，如果一段音频损坏，我们的系统可以跳过或重试处理该段，而不是浪费资源丢弃或重试整个音轨。

## 降低延迟

通过最小化空闲时间和提高任务之间的转换速度，可以降低 AI 元素的系统延迟。我们采用三种关键策略：

- 将大型任务细分为较小的部分，以便在多个 GPU 上并行处理。
- 优化工作流以实现即时任务转换。
- 智能调度资源以充分利用计算资产。

在视频转录中，我们不会一次处理整个视频，而是将其分解为多个片段以进行并发处理。这种方法缩短了转录时间并确保高效利用资源，从而提高了系统的整体响应能力。

## 具体优势：我们的 EDA 成功案例

采用此系统彻底改变了 Gcore 视频流后端中复杂 AI 工作流的管理方式。具体而言，EDA 使我们能够减少分析时间、并行化 AI 任务、独立扩展 AI 工作人员并确保系统灵活性。

**减少分析时间**：通过利用 EDA，我们大幅减少了使用一组预训练模型分析单个视频所需的时间。这意味着可以更快地处理视频，以执行字幕生成和内容审核等任务。

**并行化 AI 任务**：AI 任务的并行处理意味着将复杂的过程分解为较小、可管理的任务，这些任务可以同时执行。这种方法加快了整个过程并优化了计算资源的使用。

**独立扩展 AI 工作人员**：了解不同 AI 任务的多样化需求，我们的架构根据每个任务的特定要求扩展 AI 工作人员。例如，一个字幕生成请求可能会触发一个用于 Pyannote（用于语音活动检测）的任务，并可能触发 100 个用于 Whisper（用于语音转文本）的任务，而只有后者需要动态扩展，因为需求较高。

**确保系统灵活性**：我们的目标是创建一个高度灵活的系统，能够快速适应任何新的 AI 请求。这需要能够以临时方式加载模型，以便我们的系统能够立即响应并满足新的或不断变化的 AI 需求，而无需进行重大重新配置。

## 我们犯了这些错误，所以您不必犯

分享就是关怀：以下是设置自己的 EDA 以立即获得最佳 AI 工作流结果时需要牢记的三件事。

**避免常见的陷阱**：从一开始就设计具有容错能力的系统。预见到各个组件中潜在的故障，并确保架构能够从容地处理这些事件，而不会中断整个工作流。有效的错误处理和重试机制至关重要。

**选择正确的拓扑**：实现中介模式拓扑可以极大地简化业务逻辑的实现以及 AI 模型的模块化和可重用性。最初采用代理拓扑时，由于其线性通信模型，我们在管理复杂 AI 任务时遇到了限制。为了应对这些挑战并提高我们系统的可扩展性和模块化，我们过渡到中介拓扑。此更改引入了一个中央中介来管理 AI 业务逻辑和协调事件，允许组件独立且更有效地运行。这种转变简化了开发过程，并显著增强了系统的适应性和鲁棒性。

**计划快速集成**：灵活性是为 AI 工作流设计的任何架构的关键。允许快速添加和集成新模型到最终服务中，这在快速发展的领域中至关重要，在该领域中，快速采用和部署新模型的能力可以提供显着的竞争优势。

## 事件驱动 AI 架构的未来方向

我们一直在展望未来，并在 Gcore 创新我们的 EDA AI 系统。两个未来的方向看起来特别有希望。

### 持续学习和适应

纳入持续学习和模型适应机制需要定期使用新数据更新模型，而且不太明显的是，根据实时性能指标和反馈循环动态调整工作流和流程。随着 AI 模型在复杂性和能力方面不断增长，开发用于持续评估和部署的强大系统变得至关重要。这包括自动性能监控、版本控制和无缝部署更新的模型，而不会中断服务。

### 拥抱 LLM 和 GAI
## 我们的架构适应人工智能的演变

我们的架构旨在适应人工智能的不断变化。虽然大型语言模型 (LLM) 和生成式人工智能 (GenAI) 的兴起可能表明传统的 AI 推理工作流可能过时，但现实情况是，我们提出的架构支持 AI 部署的关键领域，例如持续模型学习和评估。我们事件驱动系统的灵活性使其非常适合集成 LLM 以增强决策制定过程，并根据 GenAI 的能力调整工作流，其中 AI 模型将越来越多地被更强大的模型所取代。

## 结论

在 Gcore，我们发现采用事件驱动架构 (EDA) 进行工作流处理为在云和流环境中管理复杂 AI 系统的可扩展性、可靠性和效率提供了显著优势。此方法解决了关键挑战，包括大规模 ML 模型的动态扩展、系统稳健性和延迟降低。EDA 已被证明对于可扩展且高效的 AI 系统的演进至关重要。

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。