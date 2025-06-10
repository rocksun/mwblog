# The Power of TIG Stack: Mastering Time Series Data Management
![Featued image for: The Power of TIG Stack: Mastering Time Series Data Management](https://cdn.thenewstack.io/media/2025/06/52013265-time-1024x576.png)
In today’s data-driven world, [time series](https://www.influxdata.com/what-is-time-series-data/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns) information flows constantly from countless sources: [Internet of Things (IoT) devices](https://www.influxdata.com/glossary/iot-devices/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns), system metrics, financial data streams and user interactions. To harness this temporal data effectively, you need specialized tools designed for the job. Enter the TIG stack: a powerful trio of open source tools – Telegraf, InfluxDB and [Grafana](https://thenewstack.io/grafana-seeks-to-correct-observabilitys-historic-terrible-job/) – that transforms the way we collect, store, analyze and visualize time-based data.

**Why Time Series Matters**
Time series data has unique characteristics that traditional databases struggle to handle efficiently. Its sequential nature, high write volumes and need for time-based querying demand purpose-built solutions. That’s what the TIG stack delivers.

**Getting Started: Your TIG Stack Setup Guide**
This tutorial will walk you through establishing your own time series data pipeline using:

[Telegraf](https://docs.influxdata.com/telegraf/v1/install/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns)for efficient data collection[InfluxDB 3 Core](https://docs.influxdata.com/influxdb3/core/get-started/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns)or 3 Enterprise for optimized storage and retrieval[Grafana](https://grafana.com/oss/grafana/)for intuitive visualization and dashboarding
The TIG stack centers on InfluxDB, a purpose-built [time series database](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/) management system optimized for high-frequency temporal data ingestion, storage and retrieval. The system architecture supports high-cardinality time series ingestion with configurable downsampling and retention mechanisms.

This tutorial will use InfluxDB 3 Core, the newest version that has a redesigned storage layer using Apache Arrow and DataFusion for columnar data processing. The implementation achieves improved write performance through batched write-ahead log (WAL) operations, enhanced query execution via vectorized processing and reduced memory overhead through optimized schema encoding and compression techniques.

Telegraf functions as the primary data collection agent, implementing a plugin-based architecture for metric acquisition from diverse sources, including system resources, network devices, APIs and message queues.

[Grafana provides the visualization and alerting layer](https://thenewstack.io/alerting-with-grafana-and-influxdb-cloud-serverless/), connecting to InfluxDB through native data source plugins that support both SQL and InfluxQL query languages. The dashboard framework renders time series data through configurable panels while the alerting engine evaluates query results against defined thresholds.
**Prerequisites**
Before diving in, make sure you have the following components installed:

**Telegraf:**The versatile data collection agent**InfluxDB 3 Core:**The time series database foundation**Grafana:**The visualization platform (For MacOS users:`brew install grafana`
followed by`brew services start grafana`
will make Grafana available at[http://localhost:3000](http://localhost:3000).)
Alternatively, you can use Grafana Cloud for a hosted solution.

**Launching InfluxDB 3 Core**
After installing InfluxDB 3 Core, initialize your server with:

`influxdb3serve--host-id=local01--object-storefile--data-dir~/.influxdb3`
Next, create an authentication token:

`influxdb3createtoken`
You’ll see output similar to:

1234 |
Token: apiv3_xxxHashed Token: zzzStart the server with `influxdb3 serve --bearer-token zzz`HTTP requests require the following header: "Authorization: Bearer apiv3_xxx" |
The plain token (apiv3_xxx) will be used with Telegraf, while the hashed version provides security when configuring the server. This security model prevents direct exposure of authentication tokens in your configuration files or command history.
**Configuring Telegraf for Data Collection**
Telegraf serves as your data collection agent, gathering [metrics from various sources and forwarding them to InfluxDB](https://thenewstack.io/cleaning-and-interpreting-time-series-metrics-with-influxdb/). Its plugin-based architecture makes it incredibly versatile.

For this demonstration, we’ll capture system CPU metrics. Create a configuration file (`telegraf.conf`
) with the following settings:

123456789101112131415161718 |
# Global configuration[agent] interval = "10s" # Collection interval flush_interval = "10s" # Data flush interval# Input Plugin: CPU Metrics[[inputs.cpu]] percpu = true # Collect per-CPU metrics totalcpu = true # Collect total CPU metrics collect_cpu_time = false # Do not collect CPU time metrics report_active = true # Report active CPU percentage# Output Plugin: InfluxDB v2[[outputs.influxdb_v2]] urls = ["http://127.0.0.1:8181"] token = "your plain Token apiv3_xxx" organization = "" bucket = "cpu" |
**Important note:** With InfluxDB 3 Core, you don’t need to specify an Organization ID.
Launch Telegraf with:

`telegraf--configpwd/telegraf.conf--debug`
Successful execution will produce log entries showing data collection and transmission:

1234567891011121314151617 |
2025-01-09T23:34:02Z I! Loading config: ./telegraf.conf2025-01-09T23:34:02Z I! Starting Telegraf 1.26.22025-01-09T23:34:02Z I! Available plugins: 235 inputs, 9 aggregators, 27 processors, 22 parsers, 57 outputs, 2 secret-stores2025-01-09T23:34:02Z I! Loaded inputs: cpu2025-01-09T23:34:02Z I! Loaded aggregators: 2025-01-09T23:34:02Z I! Loaded processors: 2025-01-09T23:34:02Z I! Loaded secretstores: 2025-01-09T23:34:02Z I! Loaded outputs: influxdb_v22025-01-09T23:34:02Z I! Tags enabled: host=MacBook-Pro-4.local2025-01-09T23:34:02Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"MacBook-Pro-4.local", Flush Interval:10s2025-01-09T23:34:02Z D! [agent] Initializing plugins2025-01-09T23:34:02Z D! [agent] Connecting outputs2025-01-09T23:34:02Z D! [agent] Attempting connection to [outputs.influxdb_v2]2025-01-09T23:34:02Z D! [agent] Successfully connected to outputs.influxdb_v22025-01-09T23:34:02Z D! [agent] Starting service inputs2025-01-09T23:34:12Z D! [outputs.influxdb_v2] Buffer fullness: 0 / 10000 metrics2025-01-09T23:34:23Z D! [outputs.influxdb_v2] Wrote batch of 13 metrics in 792.507791ms |
**Verifying Data Collection**
To confirm your metrics are properly stored, query InfluxDB directly:

`influxdb3query--database=cpu"SELECT*FROMcpuLIMIT10"`
**Visualizing With Grafana**
The final piece is setting up [Grafana](https://docs.influxdata.com/influxdb3/core/visualize-data/grafana/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns) to transform your raw data into meaningful visualizations:

- Access Grafana at
[http://localhost:3000](http://localhost:3000) - Navigate to Connections > Data sources > Add new data source
- Search for and select “InfluxDB”
- Configure your connection:
- Select SQL as the language type
- URL:
[http://localhost:8181](http://localhost:8181) - Database: cpu
- Enable “Insecure Connection”
- Click “Save & test” to verify connectivity
Now you’re ready to create visualizations! Navigate to Dashboards > Create Dashboard > Add Visualization, select your InfluxDB data source and use the visual query builder or write SQL directly.

Example query:

12 |
SELECT "cpu", "usage_user", "time" FROM "cpu" WHERE "time" >= $__timeFrom AND "time" <= $__timeTo AND "cpu" = 'cpu0' |
**Next Steps**
With your TIG Stack operational, you now have a powerful platform for time series data collection, storage and visualization. Some potential applications include:

- Infrastructure or product monitoring
- IoT sensor data analysis
- Application performance tracking
- Predictive analytics
The flexibility of Telegraf’s input plugins, the performance of InfluxDB 3 Core and the visualization capabilities of Grafana provide endless possibilities for time series data applications.

Start exploring your data today!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)