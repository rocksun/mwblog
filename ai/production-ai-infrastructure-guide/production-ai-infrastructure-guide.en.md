The transition from running machine learning models in Colab notebooks to operational, high-traffic applications requires significant changes in infrastructure setup. The notebook environment maintains fixed dependencies that become inactive when the kernel stops. Fortunately, users can easily restart it. The production environment requires immediate response times due to financial implications, as GPU resources fluctuate and data patterns shift.

> “The transition from running machine learning models in Colab notebooks to operational, high-traffic applications requires significant changes in infrastructure setup.”

The main difficulty lies in creating infrastructure that supports the operation of AI models rather than model training itself.

This tutorial establishes a system framework designed to handle sustained, high-throughput workloads rather than relying on simple Flask-style integrations. This added complexity is intentional and costly, so it only makes sense once scale or reliability requirements justify it. This system design targets sustained, multi-model, or multi-tenant workloads. For applications handling fewer than about 10 requests per second with a single model, a simple containerized API is usually more cost-effective and operationally safer. A basic containerized API solution will work best for applications that receive fewer than 10 requests per second because it provides the most cost-effective solution.

The system will use Ray on Kubernetes for distributed computing, Feast (or Redis) for feature serving, Ray Serve for composable, asynchronous inference, and Prometheus and Grafana for GPU-level observability.

## Architecture at a glance

The transition from “toy demo” to “production utility” requires developers to implement four essential components.

1. The system requires Kubernetes for container management under orchestration.
2. The system uses Ray to execute Python tasks and actors across multiple computing resources.
3. The system requires a Feature Store to connect training data from offline environments to online inference operations.
4. The system requires custom metrics to monitor GPU performance and model health status.

## Step 0: The foundation (Ray on Kubernetes)

Standard microservices infrastructure often fails to support AI workloads because it treats GPUs as CPUs. Ray, a unified compute framework, is used to manage stateful workers.

> “Ray supports fractional GPU scheduling, allowing multiple lightweight models to share a single GPU, which improves utilization and can significantly reduce cloud costs…”

*Critical Prerequisite:* Do not attempt to manage Ray pods manually via raw YAML. You must first install the KubeRay Operator in your cluster. It handles the complex lifecycle management of Ray nodes.

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

**Why this matters:** Ray supports fractional GPU scheduling, allowing multiple lightweight models to share a single GPU, which improves utilization and can significantly reduce cloud costs, provided the models are sized carefully to avoid memory contention.

## Step 1: The data layer (feature store vs. cache)

Models need context. Passing raw data at inference time is slow and error-prone.

Architectural Decision: Do you need a Feature Store (Feast)?

* **Yes, if:** Features span multiple teams, or firm checks that ensure the model behaves the same in production as it did during training (“time travel” logic).
* **No, if:** All that’s required is checking the user’s recent history. In this case, use a managed Redis instance.

Below is an example Feature Store setup using Feast. Feast orchestrates offline and online stores (often backed by systems like Redis), ensuring feature consistency between training and inference at scale.

```

# features.py
from datetime import timedelta
from feast import Entity, Field, FeatureView, FileSource
from feast.types import Float32

# 1. Define the entity (primary key)
driver = Entity(name="driver", join_keys=["driver_id"])

# 2. Define the source (e.g., Parquet file or Snowflake table)
driver_stats_source = FileSource(
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

## Step 2: High-throughput model serving

Ray Serve operates as our system for executing dynamic batching operations.

The system achieves higher throughput through batching—at the cost of slightly higher tail latency, since early requests may wait briefly for a batch to fill.

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

## Step 3: Vector infrastructure (a warning)

Implementing Retrieval-Augmented Generation (RAG) requires a vector database, such as Qdrant or Pinecone.

Production Tip: Stateful databases running on Kubernetes require a dedicated Database Reliability Engineer for self-hosting, as managing persistent storage, backups, and replication becomes complex.

The recommended approach to starting development is to use managed services from Qdrant Cloud or Pinecone.

**Production tip:** Self-hosting vector databases requires durable storage, backup automation, and operational ownership, which most teams underestimate.

## Step 4: Observability & metrics

The ability to monitor systems enables effective management of their operations. AI infrastructure requires metrics that extend beyond standard CPU performance indicators. The system requires application-level metrics, such as token counts and inference latency, along with GPU memory utilization, queue depth, and error rates.

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

## Shifting from pilots to production-ready

The development of intelligent systems depends more on architectural wisdom than on model intelligence.

The adoption of Ray and KubeRay as standard tools enables you to move AI from experimental status to operational reliability. However, if you cannot clearly articulate which failure mode each component mitigates, the system does not yet need that component.

*Critical Prerequisite:* Implementing Feature Stores and Distributed Compute should occur only when your system requires these components to operate.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.