# Streamlined APM Integration in Cloud Native Buildpacks
![Featued image for: Streamlined APM Integration in Cloud Native Buildpacks](https://cdn.thenewstack.io/media/2024/06/364c422a-cardboard-boxes-3126552_1280-1024x750.jpg)
While helping at the Cloud Foundry booth at
[KubeCon Paris 2024](https://x.com/cloudfoundry/status/1771480890893377721), I saw a lot of interest in open source [Cloud Native Buildpacks](https://buildpacks.io/). And it makes sense. As everybody jumps on the platform engineering train, operation teams are looking for the building blocks that will allow them to standardize their application lifecycle regardless of the stack. Buildpacks, hosted by the Linux Foundation, offer features that fit well with the platform engineering trend; they will enable standardization of the containerizing process and provide a consistent [developer experience no matter the stack while providing solid performance](https://thenewstack.io/the-genai-data-developer-experience-performance-optimization/) and security features.
Buildpacks have been around for over a decade now — with Heroku creating the concept in 2011 — and many practitioners have already worked with them at some point in their careers. One question kept coming from KubeCon attendees: is it still hard to install APM (
[Application Performance Monitoring](https://thenewstack.io/why-upgrade-to-observability-from-application-monitoring/))?
Those who have been using Buildpacks for a while will know that integrating an APM agent was complicated. Cloud Foundry maintainer
[Tim Downey](https://www.linkedin.com/in/tcdowney/) explained that “users had to run a separate buildpack — along with application’s one — that supplied the APM binary. This buildpack was either chained alongside the application’s regular start command or used by CF sidecar processes”.
But that’s no longer the case. In this article, I will show how to easily add an APM — taking OpenTelemetry as an example — to a Python application.
## Setup a Python Application
If you already have a Python application that you can play with, skip this section; if not, read on.
Let’s clone a repository that contains a bunch of sample
[applications and navigate to the Python](https://thenewstack.io/how-to-containerize-a-python-application-with-packeto-buildpacks/) application folder:
|
1
2
|
git clone https://github.com/sylvainkalache/sample-web-apps
cd sample-web-apps/python/
As you can see, it’s a simple Flask application.
|
1
2
3
4
5
6
7
8
9
10
11
|
$ cat my-app.py
from flask import Flask, request, render_template
import gunicorn
import platform
import subprocess
app = Flask(__name__)
@app.route("/")
def hello():
return "Hello, World!\n" + "Python version: " + platform.python_version() + "\n"
## Add OpenTelemetry to Our Application
[OpenTelemetry](https://opentelemetry.io/) is an open-source framework for collecting telemetry data such as metrics, logs, and traces from any application. The collected data can be sent to tools such as Prometheus for metrics, [Jaeger and Zipkin for tracing](https://thenewstack.io/jaeger-vs-zipkin-battle-of-the-open-source-tracing-tools/), and ELK Stack (Elasticsearch, Logstash, Kibana) for logs.
First, you will need to import these basic OpenTelemetry libraries.
|
1
2
3
|
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
Then, we need to define an OpenTelemetry tracer and an exporter. In this case, I will keep it simple and export the collected data to the console for the sake of demonstration.
|
1
2
3
4
5
6
7
8
9
10
11
12
|
# Set up the TracerProvider
trace.set_tracer_provider(TracerProvider())
# Initialize the ConsoleSpanExporter
console_exporter = ConsoleSpanExporter()
# Set up SimpleSpanProcessor to use ConsoleSpanExporter
span_processor = SimpleSpanProcessor(console_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
# Get a tracer
tracer = trace.get_tracer(__name__)
Now, we need to tell
[OpenTelemetry to trace](https://thenewstack.io/maximizing-kubernetes-efficiency-with-opentelemetry-tracing/) something; add this line to initiate a new tracing span to the hello method.
|
1
|
with tracer.start_as_current_span("my_tracer"):
Here is what your my-app.py file should look like:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
|
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
Last, to ensure that Buildpacks detects and installs the OpenTelemetry
[libraries and dependencies](https://thenewstack.io/automate-quality-security-checks-for-python-library-dependencies/), add the lines below to your requirements.txt file.
|
1
2
3
4
|
opentelemetry-api
opentelemetry-sdk
opentelemetry-instrumentation
opentelemetry-instrumentation-flask
## Pack It and Run It
The beauty of Buildpack is that with one
[pack CLI](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/) command, you will create a production-ready OCR image from our application. At the root of the Python application folder, run the following pack command.
|
1
|
pack build my-python-app --builder paketobuildpacks/builder-jammy-base
The container was created, and you can run it using the docker command below:
|
1
|
docker run -ti -p 5000:8000 -e PORT=8000 my-python-app
Now, in another tab, query your application using curl.
|
1
2
3
|
$ curl 0:5000
Hello, World!
Python version: 3.10.14
Your application should output the following, and we can see the OpenTelemetry output displayed.
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
|
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
As you can see, it is now very easy to install an APM in an application packaged with Buildpack. The same principle applies to most APMs, including New Relic and Datadog. For those reluctant to use open source Buildpacks because of that, it’s time to reconsider!
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)