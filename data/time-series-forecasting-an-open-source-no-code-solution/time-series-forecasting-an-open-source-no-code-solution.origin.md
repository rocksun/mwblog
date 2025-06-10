# Time Series Forecasting: An Open Source, No-Code Solution
![Featued image for: Time Series Forecasting: An Open Source, No-Code Solution](https://cdn.thenewstack.io/media/2025/05/7f2cc57c-time-series-data-wikipedia-manning-1024x576.jpg)
Everything around us produces data, so forecasting future trends from historical data is no longer a luxury; it’s a necessity. But what if you could implement sophisticated time series forecasting without writing a single line of code? I’ll show you how with an example using two [open source tools](https://thenewstack.io/open-source/): InfluxDB 3 Core’s Python Processing Engine and Facebook’s Prophet library.

**Revolutionizing Forecasting Implementation**
Traditional [time series forecasting](https://thenewstack.io/what-is-time-series-forecasting/) typically requires extensive coding expertise and days of development. InfluxDB 3 Core’s Python Processing Engine combined with [large language models](https://thenewstack.io/what-is-a-large-language-model/) (LLMs) and libraries shatters this paradigm. What once demanded deep technical knowledge and significant time investment can now be accomplished in hours, making advanced forecasting accessible to those with even [basic Python](https://thenewstack.io/what-is-python/) and time series understanding.

The most compelling aspect of this transformation? The speed at which complex systems can be built using LLMs. By simply providing an LLM with InfluxDB 3 [documentation](https://docs.influxdata.com/influxdb3/core/plugins/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns) and [Facebook Prophet’s quick start guide](https://facebook.github.io/prophet/docs/quick_start.html), you can generate functional plugin code, connect an entire pipeline and receive optimization suggestions — all without manual coding.

**Why Use a Time Series Database?**
Before diving into the implementation, let’s address a fundamental question: why use a specialized [time series database](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/) like InfluxDB instead of a general-purpose or relational database?

**Optimized for Time-Stamped Data**
Time series databases are architected specifically for handling chronological data. Unlike traditional databases, they’re optimized for time-based queries and analytics, making operations like finding rates of change, identifying trends or calculating moving averages substantially more efficient.

**Superior Data Compression**
Time series data often contains millions or billions of data points. Time series databases implement specialized compression algorithms that dramatically reduce storage requirements without sacrificing query performance.

**Built-in Time-Centric Functions**
Functions like downsampling, interpolation and window functions are standard in time series databases, eliminating the need for complex custom code. This native support accelerates development and improves reliability.

**Scalable Performance**
As your monitoring or Internet of Things (IoT) application grows, so does your data volume. Time series databases like InfluxDB scale horizontally to handle a massive influx of time-stamped data without performance degradation.

**Schema Flexibility**
Time series workloads often require adapting to changing measurement structures. InfluxDB’s flexible schema design accommodates evolving data models without painful migrations.

With these advantages in mind, a time series database like InfluxDB becomes the natural choice for a forecasting pipeline.

**The Forecasting Challenge**
This tutorial’s objective is straightforward yet powerful: predict daily page views for [Wikipedia’s article on Peyton Manning](https://en.wikipedia.org/wiki/Peyton_Manning) for an entire year. We’ll start with historical data and culminate with an interactive Plotly visualization, all within the InfluxDB ecosystem. To replicate this project, [download InfluxDB 3 Core or Enterprise](https://www.influxdata.com/downloads/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns).

This walkthrough covers:

- How I leveraged
[ChatGPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/)to build this pipeline. - Required setup and dependencies.
- Creating essential InfluxDB 3 resources.
- Data ingestion, forecast generation and visualization.
**The Pipeline Architecture**
This solution consists of three purpose-built plugins working in harmony:

**load_peyton (**HTTP-triggered plugin that imports Wikipedia pageview data from a CSV and populates the peyton_views table.[load_peyton_data.py](https://github.com/Anaisdg/influxdb3_plugins/blob/add-fbprophet-plugins/influxdata/Anaisdg/fbprophet/load_peyton_data.py)):**peyton_forecast (**Scheduled plugin running daily to query peyton_views, train a Prophet model and write a comprehensive 365-day forecast to prophet_forecast.[forecast_peyton.py](https://github.com/Anaisdg/influxdb3_plugins/blob/add-fbprophet-plugins/influxdata/Anaisdg/fbprophet/forecast_peyton.py)):**forecast_plot (**HTTP-triggered plugin that retrieves both historical and forecasted data, merges them and delivers an interactive Plotly visualization as HTML.[plot_forecast_http.py](https://github.com/Anaisdg/influxdb3_plugins/blob/add-fbprophet-plugins/influxdata/Anaisdg/fbprophet/plot_forecast_http.py)):
![Historical pageview data (blue) and forecasted pageview data (green) generated from this tutorial. Access via http://localhost:8181/api/v3/engine/plot_forecast.](https://cdn.thenewstack.io/media/2025/05/1a2c1d9a-pageview-data.png)
Historical pageview data (blue) and forecasted pageview data (green) generated from this tutorial. Access via [http://localhost:8181/api/v3/engine/plot_forecast](http://localhost:8181/api/v3/engine/plot_forecast).

**From Concept to Implementation With AI**
Rather than traditional coding, I adopted a prompt engineering approach with ChatGPT-4o. After providing InfluxDB 3’s Processing Engine documentation and Prophet’s quick start guide, I used progressive natural language prompts:

**Initial concept:**“Can you write a plugin for InfluxDB 3 that uses Facebook Prophet to forecast time series data?”**Data ingest:**“Create a plugin that loads historical data from a public CSV (like the Peyton Manning Wikipedia views) and writes it to InfluxDB.”**Forecasting logic:**“Now, write a scheduled plugin that queries that table, fits a Prophet model and writes the forecast to another table. Make sure the logic writes all forecast rows.”**Visualization:**“Can you build a third plugin that reads both the historical and forecasted data, plots it using Plotly and returns the result over HTTP as an HTML page?”
This iterative process transformed what would typically be hours of coding into a conversation about intent and functionality. The InfluxDB Processing Engine’s [test command](https://docs.influxdata.com/influxdb3/core/reference/cli/influxdb3/test/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns) proved invaluable for validation, creating a tight feedback loop that significantly accelerated development.

**Environment Setup**
You can run this example locally or containerized. Both[ InfluxDB 3 Core and Enterprise](https://www.influxdata.com/downloads/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns) support this workflow, but I’ll focus on Core (the open source version) using Docker for simplicity. If you’re looking for high availability, scalability and security, I recommend using InfluxDB 3 Enterprise instead.

After downloading the [repository](https://github.com/Anaisdg/influxdb3_plugins/tree/add-fbprophet-plugins), save the files to your plugin directory and execute:

1 |
docker run -it --rm --name test_influx -v ~/influxdb3/data:/var/lib/influxdb3 -v /path/to/plugins/:/plugins -p 8181:8181 quay.io/influxdb/influxdb3-core:latest serve --node-id my_host --object-store file --data-dir /var/lib/influxdb3 --plugin-dir /plugin |
[This command](https://docs.influxdata.com/influxdb3/core/reference/cli/influxdb3/serve/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns) launches a temporary InfluxDB 3 Core container with your local directories mounted for data persistence and plugin access, exposing port 8181 for local interaction.
**Implementation Steps**
**1. Install the Dependencies**
First, install the required packages:

12 |
influxdb3 install package plotlyinfluxdb3 install package prophet |
**2. Create the Database**
Set up a dedicated database for the forecast project:

1 |
influxdb3 create database prophet |
**3. Load Historical Data**
Create and trigger the data loading plugin:

12345 |
influxdb3 create trigger \ --trigger-spec "request:load_peyton" \ --plugin-filename "load_peyton_data.py" \ --database prophet \ load_peyton |
Execute the plugin:
1 |
curl http://localhost:8181/api/v3/engine/load_peyton |
Successful execution displays:
1 |
{"status": "success", "rows_written": 2905} |
**4. Generate Forecasts**
Set up the forecasting plugin:

12345 |
influxdb3 create trigger \ --trigger-spec "every:1m" \ --plugin-filename "forecast_peyton.py" \ --database prophet \ peyton_forecast |
While this is configured for minute intervals for demonstration purposes, production implementations typically run daily. After successful execution, you’ll see:
123 |
processing engine: Running Prophet forecast on 'peyton_views'INFO - Chain [1] start processingINFO - Chain [1] done processing |
To prevent redundant forecasting, disable the trigger:
1 |
inflxudb3 disable trigger --database prophet peyton_forecast |
**5. Visualize Results**
Create the visualization plugin:

12345 |
influxdb3 create trigger \ --trigger-spec "request:plot_forecast" \ --plugin-filename "plot_forecast_http.py" \ --database prophet \ forecast_plot |
Access your interactive visualization at [http://localhost:8181/api/v3/engine/plot_forecast](http://localhost:8181/api/v3/engine/plot_forecast).
**Beyond the Basics: Production Considerations**
While this example demonstrates foundational concepts, production implementations could incorporate:

- Pretrained models from
[Hugging Face](https://thenewstack.io/a-hugging-face-project-is-uncovering-deepseek-r1s-secrets/)for faster inference. - Forecast accuracy monitoring to detect model drift.
- Automated retraining when performance declines.
- Integration with InfluxDB 3’s alerting capabilities for anomaly detection.
These enhancements create intelligent, self-optimizing time series pipelines tailored to specific business needs.

**Resources for Further Exploration**
Explore these resources to deepen your understanding:

[Transform Data with the New Python Processing Engine in InfluxDB 3](https://www.influxdata.com/blog/new-python-processing-engine-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)[Get started: Python Plugins and the Processing Engine](https://docs.influxdata.com/influxdb3/enterprise/get-started/#python-plugins-and-the-processing-engine/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)[Processing engine and Python plugins](https://docs.influxdata.com/influxdb3/enterprise/plugins/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)
For alert-focused implementations:

[Preventing Alert Storms with InfluxDB 3’s Processing Engine Cache](https://www.influxdata.com/blog/preventing-alert-storms-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)[How to Set Up Real-Time SMS/WhatsApp Alerts with InfluxDB 3 Processing Engine](https://www.influxdata.com/blog/setting-up-sms-whatsapp-alerts-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)[Alerting with InfluxDB 3 Core and Enterprise](https://www.influxdata.com/blog/core-enterprise-alerting-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)