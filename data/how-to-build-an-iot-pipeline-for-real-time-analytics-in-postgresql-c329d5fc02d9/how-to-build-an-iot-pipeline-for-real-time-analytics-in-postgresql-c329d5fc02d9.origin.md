# How to Build an IoT Pipeline for Real-Time Analytics in PostgreSQL
The Internet of Things (IoT) is transforming industries by connecting devices and enabling real-time data sharing. For applications that do predictive maintenance, enable smart cities, and implement industrial automation, managing IoT data effectively is key to ensuring smooth operations and timely decision-making.

While many organizations opt to manage the deluge of sensor data and power their real-time analytics using different databases, [we’ve always favored PostgreSQL](https://www.timescale.com/blog/storing-iot-data-why-you-should-use-postgresql/). With the help of extensions like [TimescaleDB](https://docs.timescale.com/), which *is *PostgreSQL under the hood and adds automatic data partitioning, always up-to-date materialized views, and a powerful hybrid-row columnar storage engine to PostgreSQL, this relational database becomes a robust IoT database.

With these additions, PostgreSQL keeps your relational and time-series data in one place as it endlessly grows, simplifies your operations, and provides speed and scale for real-time analytics.

To demonstrate this, in this blog, we’ll explore the following:

- How to integrate PostgreSQL (with TimescaleDB) with Kafka for efficient data ingestion.
- We’ll assess the performance of the data pipeline, measuring throughput and latency from data generation to storage.
- Finally, we’ll set up monitoring queries in Grafana and create a dashboard to enable real-time monitoring of your IoT system, helping you make informed, data-driven decisions.
# An IoT Pipeline for Real-Time Analytics: Key Concepts and Tools
Before we dive into our tutorial, let’s take a moment to explain some key concepts.

## IoT data challenges
The Internet of Things (IoT) is a network of everyday objects — like smartwatches, refrigerators, cars, and industrial sensors — that are connected to the Internet and can collect, share, and act on data. The IoT data collected by devices like fitness trackers and smartwatches presents a number of challenges. Its high volume, velocity, and variety require scalable storage and real-time processing capabilities. Additionally, ensuring data reliability, security, and integration across diverse devices and systems adds significant complexity. To deal with such complexity, we’ll add the following tools with our supercharged PostgreSQL (TimescaleDB *is *PostgreSQL under the hood) to build an IoT pipeline and enable real-time monitoring.

## Kafka
Apache Kafka is an open-source distributed event streaming platform for building real-time data pipelines and streaming applications. It is designed to handle large volumes of data in real time and efficiently transmit it between systems. It allows you to publish, subscribe, store, and process streams of records (events) in a fault-tolerant and scalable manner. Kafka is widely used in industries for handling high-throughput data, such as log aggregation, real-time analytics, and stream processing.

Think of Kafka as a messaging app, where messages or data are like text messages, and Kafka is the platform that manages the sending and receiving of those messages.

- Producers are like users who send messages (data) through the app. These could be different systems or applications generating data that needs to be shared.
- Topics in Kafka are like different chat groups or threads in the app. Each topic is a category or a channel where related messages are stored. For example, one thread might be for “orders,” another for “payments,” and another for “sensor readings.”
- Consumers are like users or apps that receive and read the messages from the chat groups. These could be other applications or systems that need to process the data, such as analytics tools, databases, or alerting systems.
- The queue or login Kafka is like the message inbox, where the messages wait to be read by the consumers. Kafka ensures that messages are delivered in the correct order and that consumers can access them at any time, even if they need to process the messages later.
## Grafana
Grafana is an open-source platform used for monitoring and visualizing data. It helps you understand and analyze your data by turning it into interactive and customizable dashboards. Grafana connects to various data sources, like databases, cloud services, and application logs, and allows you to create graphs, charts, and alerts based on the data you want to monitor.

With Grafana, you can track the health of your systems, view real-time metrics, and easily spot issues. It’s widely used for monitoring infrastructure, application performance, and business metrics and is particularly popular in DevOps and IT operations. Grafana also allows you to set up alerts so you can be notified when certain conditions are met, making it an essential tool for ensuring everything is running smoothly.

# Integrating PostgreSQL via Timescale With Kafka
The goal here is to stream data into a Kafka topic, sending a continuous flow of records (or events). This data can represent various types of information, such as sensor readings, logs, or transaction data, that are generated in real time. While the data is being streamed into the Kafka topic, it’s simultaneously ingested into PostgreSQL via the Timescale database through Kafka Connect.

Kafka Connect is a framework designed to integrate Kafka with different data sources and sinks such as databases or analytics platforms. It streamlines the process of sending data into TimescaleDB without the need for custom code. Kafka Connect automatically pulls data from Kafka topics and writes it to TimescaleDB, ensuring the data is stored and ready for further processing or analysis.

For speed and convenience, we used TimescaleDB in our mature PostgreSQL cloud platform, [Timescale Cloud (it’s free for 30 days, no credit card required)](https://console.cloud.timescale.com/signup), but you can always use the open-source extension. [Here’s how to install it](https://docs.timescale.com/self-hosted/latest/install/). To integrate Kafka with Timescale Cloud, you can check out another excellent blog post that provides detailed instructions [here](https://www.timescale.com/blog/building-a-kafka-data-pipeline-for-time-series-with-kafka-connect-and-timescale/).

I’ve used the same example to integrate the Timescale Cloud instance with Kafka. Below, I’ll outline the changes I made during the integration process.

Obtain the latest Kafka source:

`sudo mkdir /usr/local/kafka`
sudo chown -R $(whoami) /usr/local/kafka
wget https://downloads.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz && tar -xzf kafka_2.13-3.9.0.tgz -C /usr/local/kafka --strip-components=1
And continue with the script used [here](https://github.com/mathisve/kafka-shenanigans/blob/main/baremetal-configs/commands.sh?ref=timescale.ghost.io).

Replace the following line in `timescale-sink.properties`
file:

`"camel.kamelet.postgresql-sink.query":"INSERT INTO accounts (name,city) VALUES (:#name,:#city)",`
With this line:

`"camel.kamelet.postgresql-sink.query":"INSERT INTO metrics (ts, sensor_id, value) VALUES (CAST(:#ts AS TIMESTAMPTZ), :#sensor_id, :#value)",`
This line tells the system how to save data from a sensor into the metrics table. For every new record, it saves the following:

- The time (:#ts)
- The sensor’s ID (:#sensor_id)
- And the reading or measurement (:#value)
The `:#`
syntax is used to represent parameters in the query. It's a way to tell the system that the values for these placeholders will be provided dynamically, typically by the system or application executing the query.

Also, make sure to insert valid credentials in the following properties:

`- "camel.kamelet.postgresql-sink.databaseName":"tsdb",`
- "camel.kamelet.postgresql-sink.password":"password",
- "camel.kamelet.postgresql-sink.serverName":"service_id.project_id.tsdb.cloud.timescale.com",
- "camel.kamelet.postgresql-sink.serverPort":"5432",
- "camel.kamelet.postgresql-sink.username":"tsdbadmin"
# About the Dataset
In this blog, I’ll be using the dataset provided by Timescale, which can be found [here](https://assets.timescale.com/docs/downloads/metrics.csv.gz).

Inside this dataset, we have a table named metrics. This table is used to store time-series data commonly used in IoT (Internet of Things) or monitoring systems. Here’s a breakdown of its structure and the kind of data it holds:

`tsdb=> \d metrics`
Table "public.metrics"
Column | Type | Collation | Nullable | Default
-----------+--------------------------+-----------+----------+---------
ts | timestamp with time zone | | |
sensor_id | integer | | |
value | numeric | | |
## Columns and their roles
`ts`
(timestamp with time zone): represents the exact time when the data was recorded.`sensor_id`
(integer): identifies the sensor that generated the data.`value`
(numeric): represents the reading or measurement taken by the sensor.
## Example record
- Timestamp (ts): 2023–05–31 21:48:41.234187+00
- Sensor ID (sensor_id): 21
- Value (value): 0.68
This record indicates that at the specified timestamp, Sensor 21 recorded a measurement of 0.68.

`tsdb=> select * from metrics limit 1;`
ts | sensor_id | value
-------------------------------+-----------+-------
2023-05-31 21:48:41.234187+00 | 21 | 0.68
(1 row)
# Prepare the Dataset
Download and decompress the dataset.

`wget https://assets.timescale.com/docs/downloads/metrics.csv.gzgzip -d metrics.csv.gz`
Convert the dataset to JSON format so we can easily stream this data to Kafka topic.

`echo "[" > metrics.jsonawk -F',' '{print "{\"ts\": \""$1"\", \"sensor_id\": "$2", \"value\": "$3"},"}' metrics.csv | sed '$ s/,$//' >> metrics.jsonecho "]" >> metrics.json`
Once the dataset is ready, stream the data to Kafka topic.

To stream data to the Kafka topic, we are going to use a utility named `kcat`
, which was formerly known as `kafkacat`
.

The `kcat`
utility is a flexible tool that can function as either a producer (sending data) or a consumer (receiving data), depending on its configuration. It can easily switch between these roles.

In our example, by using the `-p`
switch, we configure `kcat`
as a producer to send data to a Kafka topic specified with the `-t`
switch. Once the data starts appearing in the Kafka topic, tools like Kafka Connect can be used to read the data and stream it into the Timescale database for permanent storage.

The `-b`
switch is used to specify the Kafka broker address. A Kafka broker is like a server that stores and manages messages, which are saved in topic partitions. These partitions act as separate storage areas where the messages are kept in the order they were sent.

When producers, like `kcat`
in our example, want to send data, they send it to the Kafka broker. The broker stores the data across different partitions.

Then consumers, such as `Kafka Connect`
, connect to the Kafka broker and fetch the data from the topics they're interested in. Even in case of system failures, Kafka brokers ensure that the data remains accessible and available, keeping the system reliable.

`kcat -P -b localhost:9092 -t mytopic -l metrics.json`
✨ **Note**: Both the Timescale instance and the Kafka host were located in the same AWS region.

## Important timelines
- Data streaming to the Kafka topic started at:
- Mon Dec 2 01:44:40 UTC 2024 - Data streaming to the Kafka topic ends at:
- Mon Dec 2 01:44:58 UTC 2024 - The total number of rows to be ingested was:
- 2523726 - Data ingestion to Timescale instance started at:
- Mon Dec 2 01:44:40 UTC 2024 - Data ingestion to Timescale instance ends at:
- Mon Dec 2 02:15:38 UTC 2024 - Total time taken to ingest the data to Timescale:
- 30 minutes and 58 seconds.
## Stats
- Streaming rate to Kafka topic:
- Total number of rows / total time = 2523726 / 18 =**140207 rows / sec** - Data ingestion rate to Timescale instance:
- Time taken for ingestion / total number of rows = 2523726 / 1858 = ~**1358 rows / sec** - Total latency to ingest the data to Timescale Cloud:
- The time when ingestion ends in Timescale.The time when ingestion started in Timescale = Mon Dec 2 02:15:38 UTC 2024 — Mon Dec 2 01:44:40 UTC 2024 =**1,858 seconds**
# Monitoring IoT Data With Grafana
To integrate Timescale with Grafana, I recommend reading the following blog post, which provides a step-by-step guide for the integration process [here](https://www.timescale.com/learn/5-ways-to-monitor-your-postgresql-database).

After completing the Grafana integration, the next step is to create your first Grafana dashboard. To do this, follow these steps:

- From the left panel, select “Dashboard.”
- Then, create a new dashboard for visualization.
Next, choose your PostgreSQL data source.

At this stage, your first dashboard is nearly complete. Simply click on the “Back to Dashboard” option in the top right corner to return to it, where you can begin creating custom variables and queries for data visualization.

A new dashboard is created successfully:

This is how our initial data looks in Grafana:

# Creating Custom Variables for Your Grafana Dashboard
Custom variables in Grafana are user-defined placeholders that allow dynamic data filtering and visualization based on user inputs, such as dropdown selections. They enhance dashboards by enabling flexible, reusable queries and tailored insights without modifying the underlying queries.

In an IoT use case, custom variables in Grafana can be utilized to monitor specific device locations. For example, a variable can filter temperature data by selecting devices installed in different rooms or floors of a building. This filtering allows the dashboard to display real-time temperature trends for the chosen locations, enabling targeted monitoring and analysis.

To create custom variables, navigate to your dashboard and select the Settings menu from the top right corner.

From Settings, click on the Variables tab and click on Add variable.

On the next screen, we need to add all the required information to create a new variable:

- Select variable type: Choose the variable type, such as query, custom, or constant, to define how the variable’s values are generated. Since we’re creating a dropdown that a backend query will populate, I have selected the “query” option.
- Name: Assign a unique identifier for the variable, used for referencing it in queries or expressions.
- Label: Provide a display name for the variable, which is shown on the dashboard for user clarity.
- Description: Add a brief explanation of the variable’s purpose, aiding dashboard users in understanding its function.
- Show on dashboard: Decide how to display this dropdown on the dashboard, whether it should be with a label for better understanding or without a label.
- Data source: Specify the data source (e.g., Prometheus, PostgreSQL) from which the variable retrieves its values.
- Query: Define the logic or query to fetch dynamic values for the variable based on the selected data source.
You can leave the rest of the options as the default values.

At the bottom, we can see Grafana provides a preview of the data it successfully fetched from the database table, which will then be used to populate the dropdown.

After creating the custom variables, the next step is setting up dashboard monitoring queries for real-time data visualization.

# Visualizing Monitoring Queries on a Grafana Dashboard
After creating your custom variables, navigate to the dashboard, click on the three dots in the panel, and select “Edit.”

On the next screen, select the “Code” option next to “Run Query.” We will use Code mode instead of the “Query Builder” mode, as this allows you to write your own query to generate the visuals.

## Case 1: Plotting minimum and maximum sensor data
Retrieving the range of values for a specific sensor over a particular day is useful for detecting anomalies (such as unusually high or low readings), evaluating the sensor’s performance within expected limits, and ensuring the sensor is functioning correctly.

## Query
`SELECT`
MIN(value) AS min_value,
MAX(value) AS max_value
FROM metrics
WHERE
ts BETWEEN $__timeFrom() AND $__timeTo()
AND sensor_id = $sensor_id;
## Understanding the query
- The above query retrieves the minimum and maximum values of the value column from the metrics table within a specified time range and for a specific sensor ID.
- It dynamically uses
`$__timeFrom()`
,`$__timeTo()`
, and`$sensor_id`
variables to integrate seamlessly with Grafana dashboards.
✨ **Note**: We can easily select the sensor ID from the dropdown menu in the top left corner and specify the desired date range using the date range filter. The dashboard will automatically update to display the minimum and maximum values for the selected sensor and desired date range.

## The result
The diagram shows a minimum value of 0.265 and a maximum value of 0.999 for sensor ID 23, within the date range of 2023–05–29 to 2023–05–31.

## Case 2: Plotting the sensor reading at 10-second intervals
This is an ideal use case for downsampling high-frequency data into fixed time intervals, streamlining trend analysis, and data visualization. It ensures uniform time buckets, prevents graphs from becoming cluttered with excessive data points, and preserves key readings.

## Query
`SELECT`
series.time AS time,
m.value AS value
FROM
generate_series(
$__timeFrom()::timestamp,
$__timeTo()::timestamp,
'10 seconds'::interval
) AS series(time)
LEFT JOIN LATERAL (
SELECT value
FROM metrics
WHERE sensor_id = $sensor_id
AND ts >= series.time
AND ts < series.time + interval '10 seconds'
ORDER BY ts
LIMIT 1
) m ON true
ORDER BY series.time;
## Understanding the query
- The query creates a series of time intervals from the start to the end of the selected date range (
`$__timeFrom() to $__timeTo()`
) in 10-second steps. - For each time interval, it retrieves the corresponding value from the
`metrics`
table for the selected`sensor_id`
, ensuring that the data's timestamp (ts) falls within that specific interval. The closest match is selected for each interval.
## The result
The diagram above displays readings from sensor ID 4, from 2023–05–29 at 06:07:48 to 2023–05–29 at 06:40:00. The graph shows data in five-minute intervals, where we observe consistent readings from 06:10 to 06:15, followed by a spike from 06:15 to 06:20. The readings stabilize again, with two more spikes occurring at 06:30 and 06:34, before returning to normal. These spikes suggest the sensor experienced three distinct unwanted events during this period.

## Case 3: Plotting average sensor value
Getting average data or value for a sensor helps to understand its overall performance or behavior over the course of the day or months. It is particularly useful for monitoring sensors that are supposed to maintain a certain average range, allowing you to assess the general trend of the data.

## Query
`SELECT `
sensor_id,
AVG(value) AS avg_value
FROM metrics
WHERE ts >= $__timeFrom()
AND ts <= $__timeTo()
AND sensor_id = $sensor_id
GROUP BY sensor_id;
## Understanding the query
- This query calculates the average (AVG) value of the
`value`
column for the give`sensor_id`
within the time range defined by Grafana's`$__timeFrom()`
and`$__timeTo()`
variables. - It groups the results by
`sensor_id`
and retrieves the average reading within the selected time range for that specific sensor.
## The result
The diagram above displays the average reading for sensor ID 23 within the selected timeframe, from 2023–05–29 06:10:00 to 2023–05–29 06:40:00.

## Case 4: Plotting and comparing readings from two sensors
By comparing the sensor readings side by side, you can identify correlations, trends, or issues that may exist between the two sensors’ data, which can be crucial for diagnosing problems or ensuring data consistency across devices.

## Query
`SELECT `
a.ts AS time,
a.value AS sensor_a_value,
b.value AS sensor_b_value
FROM metrics a
JOIN metrics b
ON a.ts = b.ts
WHERE
a.sensor_id = $sensor_a
AND b.sensor_id = $sensor_b
AND a.ts >= $__timeFrom()
AND a.ts <= $__timeTo()
ORDER BY
a.ts;
## Understanding the query
- First, we select the timestamp (a.ts) as time, along with the values from
`sensor_a`
and`sensor_b`
. The join allows comparing data from two different sensors in the same timestamp (a.ts = b.ts). - Finally, we filter data for the selected
`sensor_a`
and`sensor_b`
IDs using Grafana variables, limit the data to the specified time range and order the results by timestamp to show the values chronologically.
✨ **Note**: A new dashboard was created for this query, and we also created two custom variables to compare sensor A with sensor B.

## The result
The diagram above compares two sensors, sensor ID 1 and sensor ID 11, within the specified time interval from 2023–05–29 06:00:00 to 2023–05–29 07:30:00. The graph illustrates value variations for both sensors in five-minute intervals. From the data, it is evident that sensor 1 maintains consistent and steady readings, while sensor 11 exhibits a few spikes during the same timeframe. These spikes indicate that sensor 11 may require further attention or investigation.

# Final Dashboard Look
Here is the final look of the dashboard:

A separate dashboard to compare sensors:

The final design of the dashboard ensures all critical information is available in one place. This centralization means you do not have to go to different sections or tools to find the stats you need. With everything neatly organized, users can easily monitor key metrics, spot trends, and make quick decisions, making this PostgreSQL-based IoT pipeline fueled by Kafka and Grafana an ideal solution for predictive maintenance and alerting. Real-time analytics are easily available to inform timely insights and prompt quick actions.

While common in a number of industries, these use cases present different challenges compared to general-purpose analytics.

Unlike more general analytics use cases, where you can wait for the data and perform batch inserts, real-time analytics require high ingestion speed and the ability to make that data available immediately for querying and analysis.

TimescaleDB excels in both thanks to its [hybrid-row columnar storage engine](https://www.timescale.com/blog/hypercore-a-hybrid-row-storage-engine-for-real-time-analytics/). It can ingest and store data in the most efficient format, enabling you to query it transparently across the rowstore and column store. This transition happens automatically under the hood and without overhead.

# Conclusion
In this blog, we have looked at how easily we can connect Kafka and Kafka Connect to stream IoT data into a PostgreSQL-based TimescaleDB instance and power a real-time analytics dashboard. TimescaleDB is great for handling [large amounts of IoT data](https://www.timescale.com/learn/postgres-for-iot), thanks to its strong time-series features, ensuring it’s both scalable and efficient.

Once your pipeline is running smoothly with Timescale and Kafka, the next thing we should focus on is monitoring, so Grafana is a great tool for visualizing your data in real time, helping you keep track of performance and make better, data-driven decisions.

If your use case demands real-time insights, like [Trebellar’s](https://www.timescale.com/blog/how-trebellar-halved-storage-costs-while-unlocking-real-time-insights-with-postgresql/), try TimescaleDB. You can [self-host it](https://docs.timescale.com/self-hosted/latest/install/) or [try our managed PostgreSQL option, Timescale Cloud](https://console.cloud.timescale.com/signup), for free. This will allow you to focus on your app — not your database.

*This article was written by Semab Tariq *a*nd originally published **here** on the Timescale official blog on December 30, 2024.*