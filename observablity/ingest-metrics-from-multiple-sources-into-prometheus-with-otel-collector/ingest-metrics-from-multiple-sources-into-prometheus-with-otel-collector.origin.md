# Ingest Metrics from Multiple Sources into Prometheus with OTel Collector
![Featued image for: Ingest Metrics from Multiple Sources into Prometheus with OTel Collector](https://cdn.thenewstack.io/media/2025/05/3844a465-ingest-metrics-multiple-sources-prometheus-otelccollector-1024x576.jpg)
In the early days of an enterprise, [monitoring](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/) might have been an afterthought. Then, as systems grew, different teams, driven by project requirements, adopted various tools. The backend team embraced [StatsD](https://github.com/statsd/statsd) for its simplicity, funneling metrics into [Graphite](https://graphiteapp.org/). Infrastructure engineers relied on syslog or [Nagios](https://www.nagios.org/) checks.

Later, as containerization took hold, another department adopted [Prometheus](https://prometheus.io/) for microservices. Fast forward to today, and the latest applications are being built with [OpenTelemetry (OTel)](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) instrumentation, sending metrics data via the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/).

This monitoring sprawl becomes unsustainable. Correlating issues across systems is complex, and managing different systems and configurations drains resources. The need arises to standardize and consolidate, but ripping out existing instrumentation is often impractical. How can you bridge these diverse metric sources — StatsD, Prometheus exporters and OTLP — into a central Prometheus system without adding *more complexity*?

Enter the [OTel Collector](https://thenewstack.io/how-adobe-uses-opentelemetry-collector/). It acts as a powerful, vendor-agnostic **aggregation layer **and **protocol translator**. We’ll show you how to use the OTel Collector as a central hub to seamlessly ingest metrics from these varied sources, process them consistently and send them to Prometheus, which simplifies your architecture and paves the way for unified observability.

## Prerequisites
We’ll[Docker](https://www.docker.com/?utm_content=inline+mention)and Docker compose:[use containers](https://roadmap.sh/docker)to run Prometheus, the OTel Collector and sample metric sources. For installation, refer to this[guide](https://docs.docker.com/desktop/setup/install/mac-install/).**Basic understanding of Prometheus:**Familiarity with Prometheus concepts like scraping, metrics formats and Remote Write is helpful. Review the[Getting Started with Prometheus workshop](https://o11y-workshops.gitlab.io/workshop-prometheus/)for an introduction.**Basic understanding of OTel Collector:**Knowledge of receivers, processors, exporters and[pipelines](https://thenewstack.io/the-case-for-telemetry-pipelines)is useful. If you’re new, check out the[official OTel Collector documentation](https://opentelemetry.io/docs/collector/configuration/).
## The Trouble With Heterogeneous Monitoring Landscapes
Heterogeneous monitoring landscapes, where your environment is a mix of old and new technologies, are common among evolving organizations.

Here is a scenario:

**New services:**Your latest microservices are being built with OpenTelemetry software development kits (SDKs), emitting metrics using OTLP and sending them to Prometheus using some intermediary.**Infrastructure tools:**You have existing tools or infrastructure components (such as databases or proxies using exporters like node-exporter or mysqld-exporter) that expose metrics in the Prometheus format on a specific HTTP endpoint.**StatsD emitters:**Older services or specific tools are sending metrics using the StatsD protocol over User Datagram Protocol (UDP) to Graphite.
While each component may be monitored in *some way*, this heterogeneity creates operational friction. Without a central aggregation layer, you face several challenges:

Prometheus needs scrape configurations for each exporter and application. Managing a large and dynamic list of these targets can become challenging.[Complex Prometheus configuration:](https://o11y-workshops.gitlab.io/workshop-prometheus/#/9)**Multiple ingestion paths:**OTLP data may require a dedicated OTLP-to-Prometheus bridge or specific receiver configurations, depending on whether Prometheus supports them directly. In contrast, every infrastructure tool (e.g., MySQL,[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)) requires its own exporter.**Inconsistent metadata:**Metrics from different sources may lack a standard identifying label (such as environment, cluster or application group), making correlating data and creating a unified dashboard difficult.**Maintenance overhead:**Managing multiple agents (such as statsd_exporter, potentially others) and complex Prometheus scrape configurations increases the operational burden.
This diagram illustrates the multiple paths and potential systems needed, along with the configuration burden placed directly on Prometheus.

![Complexity of monitoring heterogenous landscapes, diagrammed based on the above explanation](https://cdn.thenewstack.io/media/2025/05/49155f0d-heterogenous-monitoring-architecture.png)
Source: Chronosphere

## The OTel Collector Solution: A Unified Ingestion Point
The [OpenTelemetry Collector](https://docs.chronosphere.io/ingest/metrics-traces/otel/otel-ingest?utm_source=TNS&utm_medium=sponsored+content) acts as a “Swiss Army knife” for telemetry data. By deploying it between your metric sources and Prometheus, you can simplify the architecture.

Here’s how it works in our scenario:

**Receivers:**The Collector is configured with multiple receivers:- OTLP receiver: Listens for OTLP metrics (gRPC and/or HTTP) from new services.
- Prometheus receiver: Actively scrapes the /metrics endpoints of your legacy Prometheus exporters.
- Statsd receiver: Listens for StatsD metrics on a UDP port.
**Processors:**The Collector can process the metrics flowing through it. A key use case is adding standard metadata using processors like the resource processor to ensure all metrics sent to Prometheus have consistent labels (e.g., environment=”production”, k8s_cluster=”main”).**Exporters:**The Collector then exports the unified, processed metrics to Prometheus using one (or both) of these methods:**Prometheus Remote Write exporter**: Pushes the metrics directly to Prometheus’s remote write endpoint. This decouples the Collector from Prometheus’s scrape cycle.**Prometheus exporter**: Exposes a*new*/metrics endpoint*on the Collector itself*. This endpoint contains the aggregated metrics from all configured receivers. You then configure Prometheus to scrape*only this single endpoint*from the Collector.
This approach centralizes the complexity of handling diverse sources within the Collector, allowing Prometheus to focus on its core strengths: storage, querying (PromQL) and alerting.

This diagram shows the Collector acting as the central hub, simplifying the connections and configurations for Prometheus.

![OTel Collector acts as central hub for Prometheus](https://cdn.thenewstack.io/media/2025/05/7af3cc50-otel-collector-central-hub.png)
Source: Chronosphere

## Unifying Metrics With OpenTelemetry Collector
![OTel Collector centralizes metric ingestion from diverse sources, such as MySQL, OTLP, Apache Airflow.](https://cdn.thenewstack.io/media/2025/05/ee329da0-unify-metrics-otel.png)
Source: Chronosphere

This diagram demonstrates how the [OpenTelemetry Collector ](https://docs.chronosphere.io/ingest/logs/otel-logs-oem?utm_source=TNS&utm_medium=sponsored+content)centralizes metric ingestion from diverse sources.

On the left are examples like modern applications sending OTLP, a MySQL database providing its specific metrics, and [Apache Airflow](https://thenewstack.io/apache-airflow-3-0-from-data-pipelines-to-ai-inference/) emitting StatsD data. Each distinct data type flows into a corresponding specialized receiver within the [OTel Collector ](https://docs.chronosphere.io/ingest/metrics-traces/otel?utm_source=TNS&utm_medium=sponsored+content)(OTLP, MySQL and StatsD receivers, respectively).

These metrics are then funneled through common processors, which can normalize the data by adding consistent resource attributes (such as environment labels) and batching them for efficiency.

Finally, a single exporter, such as the `prometheusremotewrite`
exporter used in this example, transmits these metrics to your central Prometheus instance, drastically simplifying the overall monitoring pipeline.

Let’s translate this into a working setup using Docker Compose.

### Instructions For Configuring Fluent Bit
**1. Create your directory.**
Open your terminal and create a directory called `otel-test`
:

1 |
mkdir otel-test && cd otel-test |
**2. Create a Docker network.**
Run the command:

1 |
docker network create opentelemetry-demo |
#### **3. Set up MySQL.**
Create a file called `mysql.yml`
with this content:

1234567891011121314151617 |
services: mysql: image: mysql:8.0 container_name: mysql environment: MYSQL_ROOT_PASSWORD: rootpass MYSQL_USER: otel MYSQL_PASSWORD: otelpass MYSQL_DATABASE: otel ports: - "3306:3306" networks: - opentelemetry-demonetworks: opentelemetry-demo: external: true |
**4. Set up Apache Airflow.**
Create a file called `airflow.yml`
with the following content:

1234567891011121314151617 |
services: airflow: image: apache/airflow:2.8.1-python3.10 container_name: airflow environment: - AIRFLOW__METRICS__STATSD_ON=True - AIRFLOW__METRICS__STATSD_HOST=otel-collector - AIRFLOW__METRICS__STATSD_PORT=8125 - AIRFLOW__CORE__EXECUTOR=SequentialExecutor - AIRFLOW__CORE__LOAD_EXAMPLES=False command: bash -c "airflow db init && airflow standalone" networks: - opentelemetry-demonetworks: opentelemetry-demo: external: true |
**5. Set up OpenTelemetry instrumented applications.**
Execute the commands below in your terminal. This will create two files: `.env`
and `otel-demo.yml`
. This setup uses a stripped-down version of the[ otel-demo](https://github.com/open-telemetry/opentelemetry-demo) repository.

12 |
wget https://gist.githubusercontent.com/sharadregoti/6223a08ad3f52c7eee1b688aaff68c42/raw/d87e4dd0911bf0af45b33e9b3a0566d335d70efa/.envhttps://gist.githubusercontent.com/sharadregoti/6223a08ad3f52c7eee1b688aaff68c42/raw/10b97b173ff3dc06a55824d504865f80cb |
**6. Set up Prometheus.**
Execute the following command to create the Prometheus configuration file under the directory `prometheus`
:

1 |
mkdir prometheus && cd prometheus && touch prometheus.yml |
Copy this content into the configuration file:
12345678 |
global: scrape_interval: 15s evaluation_interval: 15sscrape_configs: - job_name: 'prometheus' static_configs: - targets: ['localhost:9090'] |
Navigate one directory up (outside the `prometheus`
directory) and create a file called `prometheus-compose.yml`
with this content:
12345678910111213141516171819202122 |
services: prometheus: image: prom/prometheus:v2.53.4 # Use a recent version container_name: prometheus command: - '--config.file=/etc/prometheus/prometheus.yml' - '--web.enable-lifecycle' # Allows config reload - '--web.enable-remote-write-receiver' # Crucial for receiving remote write data volumes: - ./prometheus:/etc/prometheus - prometheus_data:/prometheus # Optional: Persist data ports: - "9090:9090" networks: - opentelemetry-demovolumes: prometheus_data: {}networks: opentelemetry-demo: external: true |
**7. Configure and set up OpenTelemetry Collector.**
Execute the following command to create the OTEL configuration file under the directory `otel-collector`
:

1 |
mkdir otel-collector && cd otel-collector && touch otel-collector-config.yaml |
Copy this content into the configuration file:
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273 |
receivers: # 1. OTLP Receiver (for gRPC and HTTP) otlp: protocols: grpc: endpoint: 0.0.0.0:4317 http: endpoint: 0.0.0.0:4318 # 2. Prometheus Receiver (to scrape existing exporters) prometheus: config: scrape_configs: - job_name: 'legacy-node-exporter' scrape_interval: 10s static_configs: - targets: ['node-exporter:9100'] metric_relabel_configs: - source_labels: [__address__] target_label: collector_scraped_target # 3. StatsD Receiver statsd: endpoint: 0.0.0.0:8125 # Listen on UDP port 8125 aggregation_interval: 10s # Aggregate stats over 10s before flushing mysql: endpoint: mysql:3306 username: otel password: otelpass database: otel collection_interval: 10s initial_delay: 1s statement_events: digest_text_limit: 120 time_limit: 24h limit: 250processors: # Standard processors memory_limiter: check_interval: 1s limit_percentage: 75 spike_limit_percentage: 25 batch: send_batch_size: 8192 timeout: 1s # Add common attributes/labels to all metrics passing through resource: attributes: - key: environment value: "development" action: insert # Add if not present - key: collector.instance.id value: "otel-collector-01" action: insertexporters: # 1. Prometheus Remote Write Exporter # Pushes metrics TO Prometheus's remote write endpoint prometheusremotewrite: endpoint: "http://prometheus:9090/api/v1/write" # URL of Prometheus remote write endpoint resource_to_telemetry_conversion: enabled: trueservice: pipelines: metrics: receivers: [otlp, prometheus, statsd, mysql] processors: [memory_limiter, resource, batch] exporters: [prometheusremotewrite] |
Navigate one directory up (outside the `otel-collector `
directory) and create a file called `otel-collector.yml`
with this content:
12345678910111213141516171819202122 |
services: otel-collector: image: otel/opentelemetry-collector-contrib:0.123.0 # Use contrib for more receivers/exporters container_name: otel-collector command: ["--config=/etc/otelcol-contrib/otel-collector-config.yaml"] volumes: - ./otel-collector:/etc/otelcol-contrib ports: # Receivers - "4317:4317" # OTLP gRPC receiver - "4318:4318" # OTLP HTTP receiver - "8125:8125/udp" # StatsD receiver # Exporters - "8889:8889" # Prometheus exporter (for Prometheus to scrape the collector) # Optional: Expose Collector's own metrics - "8888:8888" networks: - opentelemetry-demonetworks: opentelemetry-demo: external: true |
**8. Run all the services.**
Execute this command:

123456 |
docker compose \ -f mysql.yml \ -f airflow.yml \ -f otel-demo.yml \ -f prometheus-compose.yml \ -f otel-collector.yml up -d |
It will take a couple of minutes; please wait for the command to complete.
**9. Observe the output in Prometheus.**
Open Prometheus in the browser using this URL: `http://localhost:9090/graph`
, and run this command in the console:

1 |
{environment="development"} |
You should see output similar to the image below.
![Prometheus output](https://cdn.thenewstack.io/media/2025/05/561bdd36-prometheus-output.png)
Source: Chronosphere

To view more results, try the following Prometheus queries.

12345 |
# To view "airflow" statsd metricsairflow# To view "mysql" metricsmysql |
**10. Clean up.**
Execute this command to remove all containers:

123456 |
docker compose \ -f mysql.yml \ -f airflow.yml \ -f otel-demo.yml \ -f prometheus-compose.yml \ -f otel-collector.yml down && docker network rm opentelemetry-demo |
## Conclusion
The [OpenTelemetry Collector ](https://chronosphere.io/learn/evaluating-an-observability-vendor-why-you-should-try-before-you-buy-with-the-opentelemetry-collector/?utm_source=TNS&utm_medium=sponsored+content)helps manage metrics in heterogeneous environments. By acting as a central aggregation and processing layer, it allows you to:

**Simplify Prometheus configuration:**Reduce the number of scrape targets and specialized exporters Prometheus needs to manage.**Unify diverse metric sources:**Ingest OTLP, Prometheus-formatted metrics and StatsD (among many other formats supported by receivers) through a single component.**Ensure consistency:**Apply standard labels and transformations using processors to ensure standardized metadata across all metrics.**Provide flexibility:**Choose between pushing metrics via Prometheus Remote Write or exposing a single, aggregated scrape endpoint for Prometheus to pull.
Whether you’re migrating applications to OpenTelemetry, integrating legacy systems or simply dealing with a complex mix of metric sources, the OTel Collector offers a robust solution to bridge the gaps in your observability stack.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)