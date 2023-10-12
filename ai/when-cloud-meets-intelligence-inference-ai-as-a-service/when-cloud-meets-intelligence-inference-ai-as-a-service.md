<!--
# 当云遇见智能：推理AI即服务
https://cdn.thenewstack.io/media/2023/10/c880a48e-image3.png
Image from Gcore.
-->

利用推理AI即服务的实时决策能力，我们将为您指导复杂的模型部署过程，以Gcore平台为路线图。

译自 [When Cloud Meets Intelligence: Inference AI as a Service](https://thenewstack.io/when-cloud-meets-intelligence-inference-ai-as-a-service/) 。

随着组织日益希望在不承担计算负担的情况下实施AI解决方案，推理AI即服务正在成为默认选择，它提供实时决策的力量而无需内部硬件和专业知识。

通过将推理工作量外包给专业化的云服务，公司可以节省与建立和维护内部基础设施相关的成本，同时从AI技术的最新进步中受益，确保获得最佳表现 - 并领先竞争对手。

这是否意味着您应该直接外包与管理AI推理模型部署相关的计算负担?您该如何确保托管的推理AI服务是正确的选择?您常常会看到云服务提供商讨论托管AI解决方案的许多优势和高级功能，然而，他们很少能给您清楚地说明管理AI生产流程实际需要什么。让我们了解从模型训练到部署的实际过程是什么，如何完成这个过程，以及 Gcore 如何部署一个推理 AI 模型。

## AI模型训练和推理

在AI界，有两个关键操作:训练和推理。常规AI涵盖了这两个任务，即从数据中学习，然后根据数据进行预测或决策。相比之下，推理AI仅聚焦于推理阶段。在对一个数据集进行模型训练之后，推理AI接手应用这个模型到新的数据上，进行即时的决策或预测。

这种专门化使得推理AI在实时敏感的应用中非常有价值，例如自动驾驶汽车和实时欺诈检测，在这些场景中进行快速准确的决策至关重要。对于自动驾驶汽车，这项服务可以快速分析传感器数据进行即时的驾驶决策，消除延迟并提高安全性。在实时欺诈检测中，推理AI可以即时评估交易数据和历史模式，来标记或阻止可疑活动。

AI生产管理需求精简

管理AI生产涉及遍历一个复杂的交织决策和调整矩阵。从数据中心位置到财务预算，每个决定都会产生连锁反应。据我在Gcore担任云操作主管的经验，我可以说这个领域仍在确定自己的规则;从模型训练到部署的道路更像一个迷宫而不是一条直线。在这一节中，我将回顾每个AI生产管理者必须仔细考虑的关键组成部分，以优化性能和效率。

位置和延迟应该是AI生产中的首要考量。选择错误的数据中心位置，就注定会遇到延迟问题，这可能严重降低用户体验。例如，如果你在欧盟运营，但数据中心在美国，跨大西洋的数据传输时间可能造成明显延迟，这对于推理AI来说是一个不可接受的开始。

资源管理需要实时适应能力。像CPU、内存和专用硬件(GPU或TPU)需要根据最新性能指标进行不断调优。当你从开发切换到大规模生产时，动态资源管理从一个非必需品变成一个必需品，它以24/7的周期运行。

财务规划与运营效率紧密相关。准确的预算预测对于长期可持续发展至关重要，尤其考虑到计算需求对用户活动的反应的波动性。

与软件开发的更成熟的格局不同，AI生产管理缺乏标准化的范本。这意味着你需要依赖定制的专业知识，并准备接受更高的错误率。这个领域由快速创新推动，并且试错法依然存在。从这个意义上说，这个行业还处于叛逆的青春期阶段，激动人心但仍在确定自己的标准。

如何部署推理AI模型

现在我们理解了AI生产管理的关键组成部分，让我带你逐步了解部署AI推理模型，重点是各种工具和资源的集成。目标是构建一个确保快速高效部署和扩展的环境。以下是成功所必需的一些工具:

Docker:行业标准的容器化，有助于平滑部署你的模型。

Whisper:语音转文字领域领先的AI模型，是我们服务的基础。

简单服务器框架(SSF):这个Graphcore工具方便构建和打包(容器化)应用程序以提供服务。

Harbor:开源工件存储软件，用于保存Docker镜像，在我们的设置中起关键作用。使用官方文档进行设置。

以下是流水线的样子:

 AI推理流水线

准备工作
模型:在本指南中，我们使用Hugging Face的预训练模型。模型训练超出了本文的范围。

环境:我们有指定的集群用于构建模型。所有命令将通过SSH执行。

步骤1:设置虚拟环境

创建一个虚拟环境:

virtualenv .venv --prompt whisper:

激活它:

source .venv/bin/activate

步骤2:安装所需软件包

安装SSF:

pip install https://github.com/graphcore/simple-server-framework/archive/refs/tags/v1.0.0.tar.gz

安装用于Docker的附加插件:

wget https://github.com/docker/buildx/releases/download/v0.11.2/buildx-v0.11.2.linux-amd64
mkdir -p ~/.docker/cli-plugins
mv buildx-v0.11.2.linux-amd64 ~/.docker/cli-plugins/docker-buildx
chmod u+x ~/.docker/cli-plugins/docker-buildx

步骤3:代码库

克隆Gcore存储库，其中包含所有必要的文件:

git clone https://github.com/G-Core/ai-code-examples.git 

切换分支:

cd ai-code-examples && git checkout whisper-lux-small-ssf

这里的两个关键文件是ssf_config.yaml和whisper_ssf_app.py。

ssf_config.yaml对配置你将构建的软件包至关重要。它包含指定模型名称、许可证和依赖项的字段。它还概述了输入和输出，详细说明了端点和字段类型。例如，对于Whisper模型，输入是一个临时文件(TempFile)，输出是一个字符串(String)。这些信息为模型与用户的交互设置了框架。

Whisper的示例:

endpoints:

  - id: asr
    version: 1
    desc: Simple application interface for Whisper
    custom: ~

    inputs:

      - id: file
        type: TempFile
        desc: Audio description text prompt

    outputs:

      - id: result
        type: String
        desc: Transcription of the text

SSF支持各种数据类型。详细信息可以在其文档中找到。

whisper_ssf_app.py充当你的Whisper模型的包装器，使其兼容简单服务器框架(SSF)。脚本包含几个关键方法:

build:这里构建模型的计算图。它必须在具有IPU的主机上运行。
startup:在模型可以开始为用户请求提供服务之前，管理预备任务。
request:这是系统的核心，负责处理用户请求。
shutdown:确保模型优雅终止，像完成正在进行的请求。
is_healthy:此方法允许模型既可以作为独立的Docker容器运行，也可以作为更大更复杂系统(如Kubernetes)的一部分。

在build方法中，调用了函数compile_or_load_model_exe。当在IPU上构建模型的计算图时，这一点至关重要。这就是关键所在:创建这个图需要初始用户请求作为输入。尽管你可以使用第一个真实用户请求来实现这一点，但请记住，构建图可能需要1到2分钟，可能更长。考虑到今天的用户对速度的期待，这种延迟可能是障碍。为了解决这个问题，build方法被设计为接受我们预定义的数据作为构建图的第一个请求。在此设置中，我们使用bootstrap.mp3来模拟那个首要请求。

步骤4:构建和发布容器

构建并发布容器，指定你自己的Docker注册表地址和凭据:

gc-ssf --config ssf_config.yaml build package publish --package-tag harbortest.cloud.gcorelabs.com/whisper/mkhl --docker-username gitlab --docker-password XXXXXXXXXX --container-server harbortest.cloud.gcorelabs.com

生成的容器包含所有必要的组件:模型、FastAPI 包装器和用于初始化热身的bootstrap.mp3。它将被推送到Harbor注册表。

步骤5:部署到边缘节点

在边缘节点上部署，使用以下命令:

gc-ssf --stdout-log-level DEBUG deploy --config ssf_config.yaml --deploy-platform Gcore --port 8100 --deploy-gcore-target-address ai-inference-cluster-1 --deploy-gcore-target-username ubuntu --docker-username gitlab --docker-password XXXXXXXXXXX --package-tag harbortest.cloud.gcorelabs.com/whisper/mkhl:latest --deploy-package --container-server harbortest.cloud.gcorelabs.com

gc-ssf deploy使用SSH在目标主机上运行命令，所以你需要在节点之间使用ssh-key进行访问。

通过遵循这个流水线，你建立了一个强大的框架来部署AI模型，确保它们不仅高效，还易于扩展和维护。

推理出一个更智能的未来

推理AI日益增长的作用不仅局限于科技巨头;它对任何追求敏捷性和竞争力的组织都至关重要。投资这项技术构成与一个可扩展、不断发展的解决数据泛滥问题的战略一致。推理AI即服务正准备成为一项不可或缺的商业工具，因为它简化了AI的技术复杂性，提供了一种可扩展和简化的方法来筛选大量的数据并提取有意义、可操作的见解。

Gcore如何使用推理AI

尽管AI采用激增，我们认识到市场上仍存在对专用、开箱即用的AI集群的需求，这些集群结合了强大的计算力和易于部署。Gcore是为了提供基础设施和低延迟服务，以便更快全球化。这解决了机器学习领景中最重大的挑战之一:从模型开发到可扩展部署的转变。我们使用Graphcore的简单服务器框架来创建一个不仅能运行机器学习模型，还能通过推理AI持续改进它们的环境。

要深入了解Gcore如何塑造AI生态系统，请考虑访问我们的博客和AI基础设施文档。