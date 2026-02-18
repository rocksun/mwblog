从笔记本到节点：构建生产级AI基础设施

将机器学习模型从Colab笔记本运行转换到可运行的高流量应用程序，需要在基础设施设置上进行重大改变。笔记本环境维持固定的依赖关系，当内核停止时这些依赖关系会失效。幸运的是，用户可以轻松重启它。生产环境由于财务影响要求即时响应时间，因为GPU资源会波动，数据模式也会发生变化。

> “将机器学习模型从Colab笔记本运行转换到可运行的高流量应用程序，需要在基础设施设置上进行重大改变。”

主要困难在于创建支持AI模型运行而非模型训练本身的基础设施。

本教程建立了一个系统框架，旨在处理持续的、高吞吐量的工作负载，而不是依赖简单的Flask风格的集成。这种增加的复杂性是有意为之且成本高昂的，因此只有当规模或可靠性要求证明其合理性时才会有意义。此系统设计针对持续的、多模型或多租户工作负载。对于处理每秒少于约10个请求且使用单个模型的应用程序，简单的容器化API通常更具成本效益且操作更安全。一个基本的容器化API解决方案最适用于每秒接收少于10个请求的应用程序，因为它提供了最具成本效益的解决方案。

该系统将使用Ray on Kubernetes进行分布式计算，Feast（或Redis）进行特征服务，Ray Serve进行可组合的异步推理，以及Prometheus和Grafana进行GPU层面的可观测性。

## 架构概览

从“玩具演示”到“生产实用工具”的转变要求开发人员实现四个基本组件。

1.  系统需要Kubernetes进行容器编排管理。
2.  系统使用Ray在多个计算资源上执行Python任务和Actor。
3.  系统需要一个特征商店，以将离线环境的训练数据连接到在线推理操作。
4.  系统需要自定义指标来监控GPU性能和模型健康状态。

## 步骤0：基础（Ray on Kubernetes）

标准微服务基础设施通常无法支持AI工作负载，因为它将GPU视为CPU。Ray，一个统一的计算框架，用于管理有状态的工作节点。

> “Ray支持分数GPU调度，允许多个轻量级模型共享一个GPU，这提高了利用率，并可以在显著降低云成本…”

*关键先决条件：* 不要尝试通过原始YAML手动管理Ray Pod。您必须首先在集群中安装KubeRay Operator。它处理Ray节点的复杂生命周期管理。

```
# ray-cluster.yaml
# Note: Requires KubeRay Operator installed in the cluster
apiVersion: ray.io/v1
kind: RayCluster
metadata:
  name: production-ai-cluster
spec:
  headGroupSpec:
    rayStartParams:
      dashboard-host: '0.0.0.0'
    template:
      spec:
        containers:
        - name: ray-head
          image: rayproject/ray:2.9.0-py310  # Always pin versions in prod
          resources:
            limits:
              cpu: "2"
              memory: "4Gi"
  workerGroupSpecs:
  - replicas: 2
    minReplicas: 1
    maxReplicas: 10
    groupName: gpu-group
    rayStartParams: {}
    template:
      spec:
        containers:
        - name: ray-worker
          image: rayproject/ray-ml:2.9.0-py310-gpu
          resources:
            limits:
              cpu: "4"
              memory: "16Gi"
              nvidia.com/gpu: "1" # K8s handles the hardware reservation
```

**为什么这很重要：** Ray支持分数GPU调度，允许多个轻量级模型共享一个GPU，这提高了利用率，并可以在显著降低云成本，前提是模型大小经过仔细调整以避免内存争用。

## 步骤1：数据层（特征商店与缓存）

模型需要上下文。在推理时传递原始数据既慢又容易出错。

架构决策：您需要一个特征商店（Feast）吗？

*   **是的，如果：** 特征跨越多个团队，或者需要严格检查以确保模型在生产中的行为与训练时相同（“时间旅行”逻辑）。
*   **不是的，如果：** 所需的只是检查用户的最近历史记录。在这种情况下，使用托管的Redis实例。

下面是使用Feast设置特征商店的示例。Feast协调离线和在线存储（通常由Redis等系统支持），确保训练和推理在大规模下特征的一致性。

```
# features.py
from datetime import timedelta
from feast import Entity, Field, FeatureView, FileSource
from feast.types import Float32

# 1. Define the entity (primary key)
driver = Entity(name="driver", join_keys=["driver_id"])

# 2. Define the source (e.g., Parquet file or Snowflake table)
driver_stats_source =
    FileSource(
        name="driver_stats_source",
        path="/data/driver_stats.parquet",
        timestamp_field="event_timestamp",
    )

# 3. Define the view: What the model actually sees
driver_stats_view = FeatureView(
    name="driver_stats",
    entities=[driver],
    ttl=timedelta(days=1),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
    ],
    online=True, # Syncs to Redis for ms-level lookup
    source=driver_stats_source,
)
```

## 步骤2：高吞吐量模型服务

Ray Serve作为我们执行动态批处理操作的系统。

该系统通过批处理实现更高的吞吐量——代价是尾部延迟略高，因为早期请求可能需要短暂等待批处理完成。

```
# serving.py
import ray
from ray import serve
from starlette.requests import Request
import torch

@serve.deployment(
    ray_actor_options={"num_gpus": 0.5}, # Bin-packing: Run 2 replicas per GPU
    autoscaling_config={"min_replicas": 1, "max_replicas": 5}
)
class TextClassifier:
    def __init__(self):
        # Heavy initialization happens once here, not per request
        self.model = torch.hub.load('huggingface/pytorch-transformers', 'model', 'bert-base-uncased')
        self.model.eval()

    # Dynamic batching: Ray collects requests and hands them to us in a list
    @serve.batch(max_batch_size=8, batch_wait_timeout_s=0.1)
    async def handle_batch(self, inputs: list[str]):
        # Tokenize and predict 8 items at once
        ids = self.tokenizer(inputs, return_tensors="pt", padding=True)
        with torch.no_grad():
            outputs = self.model(**ids)
        return [o.argmax().item() for o in outputs.logits]

    async def __call__(self, http_request: Request) -> str:
        data = await http_request.json()
        return await self.handle_batch(data["text"])

app = TextClassifier.bind()
```

## 步骤3：向量基础设施（警告）

实现检索增强生成（RAG）需要一个向量数据库，例如Qdrant或Pinecone。

生产提示：运行在Kubernetes上的有状态数据库需要专门的数据库可靠性工程师进行自托管，因为管理持久存储、备份和复制变得复杂。

推荐的开发入门方法是使用Qdrant Cloud或Pinecone提供的托管服务。

**生产提示：** 自托管向量数据库需要持久存储、备份自动化和运维所有权，这通常被大多数团队低估。

## 步骤4：可观测性与指标

监控系统的能力使得有效管理其运行成为可能。AI基础设施需要超出标准CPU性能指标的度量标准。系统需要应用程序级别的指标，例如令牌计数和推理延迟，以及GPU内存利用率、队列深度和错误率。

```
# monitoring.py
import time
from ray.util.metrics import Counter, Histogram

# Track prediction latency distribution
latency_hist = Histogram(
    "inference_latency_ms",
    description="Time spent running the forward pass",
    boundaries=[10, 50, 100, 200, 500]
)

# Track token usage for cost estimation
token_counter = Counter(
    "tokens_processed_total",
    description="Total tokens processed by the model"
)

def monitor_inference(start_time: float, token_count: int):
    """
    Records metrics for a completed inference request.
    Args:
        start_time: timestamp from time.time() taken before inference
        token_count: number of tokens generated/consumed
    """
    duration = (time.time() - start_time) * 1000
    latency_hist.observe(duration)
    token_counter.inc(token_count)
```

## 从试点到生产就绪的转变

智能系统的开发更多依赖于架构智慧而非模型智能。

Ray和KubeRay作为标准工具的采用使您能够将AI从实验状态转变为运营可靠性。然而，如果您无法清楚地阐明每个组件减轻了哪种故障模式，那么您的系统尚不需要该组件。

*关键先决条件：* 只有当您的系统需要特征商店和分布式计算组件才能运行时，才应实施它们。