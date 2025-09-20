***Editor’s Note:** This excerpt comes from the second chapter of the Manning Book: “[Fluent Bit for Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS).” This book teaches how to establish and optimize observability systems for Kubernetes, and more. From fundamental configuration to advanced integrations, this book lays out Fluent Bit’s full capabilities for log, metric and trace routing and processing. Download the book in its entirety [here](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS).*

When teams start investing in [observability and monitoring](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "observability and monitoring") more generally, effort goes into checking that their applications are running smoothly. Often, the absence of an alert is interpreted as a sign that all is well. But what if the monitor has stopped? In this case, the absence of events is a problem. For this reason, microservices in a Kubernetes environment should implement a health endpoint, traditionally set as `/health`. This leads to the question: Does [Fluent Bit](https://chronosphere.io/learn/deploy-fluent-bit-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS) have anything to which we can connect the container health check?

## Understanding Container and Pod Health Probes

To enable containers or Kubernetes pods to be effectively managed, we must be able to interrogate their condition. To this end, [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/ "Dockerfiles") include the ability to define health check actions. (For more information on defining health checks in Dockerfiles, see <https://mng.bz/RN4a>.) For pods, we can describe several different checks (also called probes), including liveness. (For more information, see <https://mng.bz/2gnw>.) If the pod doesn’t respond quickly enough to the health check from Kubernetes, we can assume that the pod is unhealthy and needs to be replaced by a new instance.

A healthy response for Kubernetes is a response typically containing an HTTP response code of `200`, which may be accompanied by a body containing `ok`. Any HTTP response code outside the `200-299` range is deemed unhealthy. It’s common practice for a containerized app to include some sort of endpoint implementation that can respond to invocations on `localhost:8080/v1/health`, which provides details on the application’s health.

## Enabling the Fluent Bit Web Server

To enable Fluent Bit to communicate and listen to web-delivered events, we need to include a web server, which gives us the means to communicate with and interrogate Fluent Bit. The first step is configuring Fluent Bit to start the web server, which we do with an attribute in the `[SERVICE]` block called `http_server`. We can also configure the IP and ports the server should use (`http_listen` and `http_port`, respectively).

## Configuring Health Checks in Fluent Bit

With the server active, we can also configure how Fluent Bit responds to health checks. We need to switch on the feature with the `health_check` attribute with a value of `on`; otherwise, the default web server response is provided. With the health response enabled, we can control what Fluent Bit considers healthy.

### What Fluent Bit Considers ‘Healthy’

Health is characterized by a count of errors from all the output plugins measured against a threshold defined by `hc_error_count` and the number of failed retries for output plugins (`hc_retry_failure_count`). We don’t want the error count and retry-error count to be a cumulative score from the start of Fluent Bit, so we need to define a period expressed in seconds (`hc_period`) over which the count is applied.

If we had an output trying to write to a file that kept failing because the filesystem was full, we should expect the error count or retry failure count to exceed a threshold quickly. As a result, the response to the health check URL will be bad.

When we use the health check feature, we should take into account what Fluent Bit [considers to be an error](https://chronosphere.io/learn/slos-open-source-microservices/?utm_source=sponsored-content&utm_id=TNS) and its implications. Any failing output will result in an unhealthy response even if we can live with the loss of those outputs. To put it another way, there is no way to define a tolerance to losing some outputs temporarily; it’s an all-or-nothing approach.

### Challenges With Inputs and Partial Failures

The other challenge is that the health check doesn’t test inputs to see whether they’re working successfully. If the tail (file tracking) input can’t read the input file, an unhealthy state won’t be successfully produced because the plugin is considered OK, as the plugin exists and the parameter values are at least defined.

## Querying Fluent Bit Health With curl and Postman

The following listing shows the config for the health check feature; see chapter2\fluentbit\hello-world-server.conf.

### Making Output More Readable With jq

With this included in our hello-world configuration, we can run Fluent Bit (`fluentbit -c hello-world-server.conf`) and then use a tool such as curl or Postman (or even a browser) to access the information about Fluent Bit. The URL to use is `0.0.0.0:2020`, giving us a JSON payload and details about the Fluent Bit instance. If we use this approach, we can use jq to make things more readable:

`curl 0.0.0.0:2020 | jq`

In addition to the curl commands, we have created Postman configurations that can be used to exercise the different API endpoints, including the hot reload. Details on setting up Postman are in Appendix A.

**Note:** Because [Fluent Bit treats all its data as JSON](https://chronosphere.io/learn/parsing-fluent-bit/?utm_source=sponsored-content&utm_id=TNS), it can be useful to have a tool such as jq that can format the output to be more readable (sometimes referred to as “pretty print”). To get jq or to understand how it works, go to https:// jqlang.github.io/jq. Additional information is included in Appendix B.

## Comparing API Versions: /api/v1/ vs. /api/v2/

Fluent Bit provides APIs that go beyond simply retrieving a summary view. Some of the APIs have two versions available: v1 is accessed via the URL path `/api/v1/`, and v2 is accessed via the path `/api/v2/`. The version changes represent feature improvements; the older URL version is retained for backward compatibility. An example is the Summary 45 /metrics endpoint; v1 provides a JSON payload, and v2 responds with Prometheus-formatted data and more data than `/v1/metrics`.

## Using Fluent Bit Health Checks in Kubernetes Probes

For a [Kubernetes health](https://chronosphere.io/learn/kubernetes-log-management/?utm_source=sponsored-content&utm_id=TNS) check, a simple response returning `ok` indicates that the container instance is running smoothly. To get this response, we need to access one of the more meaningful operational endpoints in the path `/api/v1/`, such as `/api/v1/ health`. If we invoke the health check URL with a curl command, we can expect to get a response of `ok`:

curl 0.0.0.0:2020/api/v1/health

## Frequently Asked Questions

### 1. How do I enable health checks in Fluent Bit?

You need to configure three key settings in your `[SERVICE]` block:

* Set `http_server on` to enable the web server.
* Add `health_check on` to activate health check responses.
* Configure `http_listen` and `http_port` to specify the server’s IP and port (default: 0.0.0.0:2020).

### 2. What endpoint should I use to check if Fluent Bit is healthy?

Use the `/api/v1/health` endpoint to get a simple `ok` response indicating healthy status. The complete URL format is `http://[host]:[port]/api/v1/health` (for example, `curl 0.0.0.0:2020/api/v1/health`). This endpoint is specifically designed for Kubernetes liveness probes and returns HTTP 200 status codes for healthy instances.

### 3. How does Fluent Bit determine if it’s healthy or unhealthy?

Fluent Bit’s health status is based on output plugin performance over a defined time window:

* **Error threshold:** Set via `hc_error_count` (number of errors allowed).
* **Retry failure threshold:** Configured with `hc_retry_failure_count` (failed retry attempts).
* **Time period:** Defined by `hc_period` (seconds) to prevent cumulative scoring from startup.
* **All-or-nothing approach:** Any failing output plugin triggers an unhealthy response, with no tolerance for partial failures

***Note:** The health check only monitors output plugins; input plugin failures (like unreadable files) won’t trigger unhealthy status.*

In subsequent chapters in the Manning Book, “[Fluent Bit for Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS)” (particularly chapters 3 and 5), we’ll revisit the available APIs. Download the entire book to read about a decade’s worth of innovation and development in Fluent Bit technology, including guidance on addressing modern challenges in observability, particularly in distributed systems like Kubernetes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)