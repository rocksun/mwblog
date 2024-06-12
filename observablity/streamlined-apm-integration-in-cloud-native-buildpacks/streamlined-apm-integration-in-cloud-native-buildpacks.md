
<!--
title: 在云原生Buildpacks 中简化 APM 集成
cover: https://cdn.thenewstack.io/media/2024/06/364c422a-cardboard-boxes-3126552_1280.jpg
-->

对于那些不愿使用开源 Buildpack 的人来说，是时候重新考虑了。

> 译自 [Streamlined APM Integration in Cloud Native Buildpacks](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/)，作者 Sylvain Kalache。

在 [2024 年巴黎 KubeCon](https://x.com/cloudfoundry/status/1771480890893377721) 的 Cloud Foundry 展位提供帮助时，我看到许多人对开源 [云原生 Buildpacks](https://buildpacks.io/) 感兴趣。这很有道理。随着每个人都加入平台工程的行列，运营团队正在寻找构建模块，以便他们可以标准化其应用程序生命周期，而不管堆栈如何。由 Linux 基金会托管的Buildpacks 提供了与平台工程趋势非常契合的功能；它们将实现容器化过程的标准化，并提供一致的 [开发者体验，无论堆栈如何，同时提供可靠的性能](https://thenewstack.io/the-genai-data-developer-experience-performance-optimization/) 和安全功能。

Buildpacks 已经存在十多年了——Heroku 在 2011 年创建了这个概念——许多从业者已经在职业生涯的某个阶段使用过它们。KubeCon 与会者不断提出一个问题：安装 APM（[应用程序性能监控](https://thenewstack.io/why-upgrade-to-observability-from-application-monitoring/)) 是否仍然困难？

那些已经使用Buildpacks 一段时间的人会知道，集成 APM 代理很复杂。Cloud Foundry 维护者 [Tim Downey](https://www.linkedin.com/in/tcdowney/) 解释说，“用户必须运行一个单独的Buildpacks ——以及应用程序的一个Buildpacks ——来提供 APM 二进制文件。此Buildpacks 要么与应用程序的常规启动命令一起链接，要么由 CF 边车进程使用”。

但现在情况不再如此。在本文中，我将展示如何轻松地将 APM（以 openTelemetry 为例）添加到 Python 应用程序中。

## 设置 Python 应用程序
如果您已经有一个可以使用的 Python 应用程序，请跳过本节；如果没有，请继续阅读。

让我们克隆一个包含大量示例 [应用程序并导航到 Python](https://thenewstack.io/how-to-containerize-a-python-application-with-packeto-buildpacks/) 应用程序文件夹：

```
git clone https://github.com/sylvainkalache/sample-web-apps
cd sample-web-apps/python/
```

如您所见，这是一个简单的 Flask 应用程序。

```py
$ cat my-app.py
from flask import Flask, request, render_template
import gunicorn
import platform
import subprocess
 
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello, World!\n" + "Python version: " + platform.python_version() + "\n"
```

## 将 OpenTelemetry 添加到我们的应用程序

[OpenTelemetry](https://opentelemetry.io/) 是一个用于从任何应用程序收集遥测数据（例如指标、日志和跟踪）的开源框架。收集的数据可以发送到诸如 Prometheus（用于指标）、[Jaeger 和 Zipkin（用于跟踪](https://thenewstack.io/jaeger-vs-zipkin-battle-of-the-open-source-tracing-tools/)) 和 ELK 堆栈（Elasticsearch、Logstash、Kibana）（用于日志）之类的工具。

首先，您需要导入这些基本的 OpenTelemetry 库。

```py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
```

然后，我们需要定义一个 OpenTelemetry 跟踪器和一个导出器。在这种情况下，我将保持简单，并将收集的数据导出到控制台以进行演示。

```py
# Set up the TracerProvider
trace.set_tracer_provider(TracerProvider())
 
# Initialize the ConsoleSpanExporter
console_exporter = ConsoleSpanExporter()
 
# Set up SimpleSpanProcessor to use ConsoleSpanExporter
span_processor = SimpleSpanProcessor(console_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
 
# Get a tracer
tracer = trace.get_tracer(__name__)
```

现在，我们需要告诉 [OpenTelemetry 跟踪](https://thenewstack.io/maximizing-kubernetes-efficiency-with-opentelemetry-tracing/) 一些事情；添加此行以启动一个新的跟踪 span 到 hello 方法。

```py
with tracer.start_as_current_span("my_tracer"):
```

以下是 my-app.py 文件应有的样子：

```py
from flask import Flask, request, render_template
import gunicorn
import platform
import subprocess
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
 
app = Flask(__name__)
 
# Set up the TracerProvider
trace.set_tracer_provider(TracerProvider())
 
# Initialize the ConsoleSpanExporter
console_exporter = ConsoleSpanExporter()
 
# Set up SimpleSpanProcessor to use ConsoleSpanExporter
span_processor = SimpleSpanProcessor(console_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
 
# Get a tracer
tracer = trace.get_tracer(__name__)
 
@app.route("/")
def hello():
    with tracer.start_as_current_span("hello_world"):
        return "Hello, World!\n" + "Python version: " + platform.python_version() + "\n"
```

最后，要确保 Buildpacks 检测并安装 OpenTelemetry 库和依赖，将下面这行添加到 requirements.txt 文件。

```
opentelemetry-api
opentelemetry-sdk
opentelemetry-instrumentation
opentelemetry-instrumentation-flask
```

## 打包并运行

Buildpack 的优点在于，只需一个 [pack CLI](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/) 命令，即可从我们的应用程序创建一个可用于生产的 OCR 镜像。在 Python 应用程序文件夹的根目录中，运行以下 pack 命令。

```
pack build my-python-app --builder paketobuildpacks/builder-jammy-base
```

容器已创建，可以使用以下 docker 命令运行它：

```
docker run -ti -p 5000:8000 -e PORT=8000 my-python-app
```

现在，在另一个标签页中，使用 curl 查询你的应用程序。

```
$ curl 0:5000
Hello, World!
Python version: 3.10.14
```

你的应用程序应输出以下内容，并且我们可以看到显示的 OpenTelemetry 输出。

```
[2024-05-01 21:35:18 +0000] [1] [INFO] Starting gunicorn 22.0.0
[2024-05-01 21:35:18 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2024-05-01 21:35:18 +0000] [1] [INFO] Using worker: sync
[2024-05-01 21:35:18 +0000] [22] [INFO] Booting worker with pid: 22
{
    "name": "hello_world",
    "context": {
        "trace_id": "0xebb54bc5f7340b22c237a2c73af2a266",
        "span_id": "0x7a02dd7f80e16c16",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2024-05-01T21:35:32.803533Z",
    "end_time": "2024-05-01T21:35:32.803574Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.24.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
```

如你所见，现在使用 Buildpack 为应用程序安装 APM 非常容易。同样的原则适用于大多数 APM，包括 New Relic 和 Datadog。对于那些因为这个原因而不愿意使用开源 Buildpacks 的人来说，是时候重新考虑了！
