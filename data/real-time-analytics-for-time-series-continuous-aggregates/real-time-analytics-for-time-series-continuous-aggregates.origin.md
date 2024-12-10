# Real-Time Analytics for Time Series: A Dev’s Intro to Continuous Aggregates
![Real-Time Analytics for Time Series: A Dev’s Intro to Continuous Aggregates](/blog/content/images/size/w2000/2024/11/Real-time-analytics-for-time-series_cont-aggregates-1.png)
When looking at reasons to use TimescaleDB, you’ll commonly see a feature called “continuous aggregates” mentioned. It’s a powerful feature that helps you see a massive improvement in performance when working with incredibly large or rapidly growing data sets, equipping PostgreSQL to handle real-time analytics workloads effortlessly. Let’s cover it in a little more detail.

## What Are Continuous Aggregates, Anyway?
Simply put, a [continuous aggregate](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/about-continuous-aggregates/?ref=timescale.com) in TimescaleDB is an **incrementally and automatically updated materialized view** for an aggregate query over a hypertable.

When collecting time-series data you're often ingesting at a far greater frequency than might be needed for further analysis or auditing purposes. Parsing through this data can be problematic as it takes far longer to perform read or write operations on extremely large datasets. As a result, continuous aggregates were created.

![A comparison table of PostgreSQL materialized views vs. continuous aggregates](https://www.timescale.com/blog/content/images/2024/11/Real-Time-Analytics-for-Time-Series_Continuous-aggregates-vs-materialized-views.png)
Unlike regular materialized views, *continuous aggregates automatically refresh only the new or changed data rather than recomputing the entire view*. This causes data to be pre-aggregated in the background for faster querying and rendering of source data.

This makes them ideal for efficiently querying time-series data over large time ranges in real time, as the aggregated results are automatically and incrementally refreshed in the background without manual intervention.

## Improved Performance, Reduced Storage
Working with time-series data offers several clear benefits. These are realized as *much faster query performance* and* reduced storage costs*.

Continuous aggregates achieve these improvements with performance testing showing instant reductions in query run-times with the ability to query your data normally using `DISTINCT`
, `ORDER BY`
, `FILTER`
with `HAVING`
, and other query clauses (*as of Timescale 2.7*). Fewer records to parse through = faster query speeds and less data to store.

They’re also not dependent on the existence of the original source data. This means you can drop the underlying hypertable and still keep around the dataset that has been downsampled through continuous aggregates. Historical analysis or auditing can still be performed on this less granular data while freeing up space for new records.

**Note:**
*Each continuous aggregate can have its own*
*retention policy*
*to automatically drop chunks of data after a specified amount of time to achieve this effect automatically.*As of Timescale 2.6, you can apply TimescaleDB’s native columnar [ compression](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/compression-on-continuous-aggregates/?ref=timescale.com) to continuous aggregates to condense disk space even further. This can even be handled with

[to automatically compress data after a certain amount of time and be combined with data retention policies to drop older datasets that are no longer needed.](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/compression-on-continuous-aggregates/?ref=timescale.com#compression-policies-on-continuous-aggregates)
__compression policies__## In the Real World
Users have reported using them successfully for a variety of purposes, including:

- Visualizing metrics in real time
- Performing data operations on time-series data, like sensor data, historical stock information, or recording air pollution
- Enforcing daily thresholds set for IoT devices
- Managing data for OLAP-oriented databases
- Working with millions (or more) of existing records requiring aggregation
## Using Continuous Aggregates
So let’s say you need to display sensor data on a dashboard to analyze the results.

```
SELECT
time_bucket('1 hour', time) as hour,
device_id,
AVG(temperature) as avg_temp
FROM sensor_data
WHERE time > NOW() - INTERVAL '1 year'
GROUP BY hour, device_id
ORDER BY hour DESC;
```
A query like this can take a long time to execute when run against millions of rows. What’s more, every time this query is performed, it has to be reaggregated every single time it’s run—consuming unnecessary resources and dramatically impacting performance.

This is where continuous aggregates are the most useful; they can be used to pre-calculate the results in the form of a smart cache that automatically updates itself. We’re able to rewrite the above query using a continuous aggregate:

```
CREATE MATERIALIZED VIEW hourly_temps
WITH (timescaledb.continuous) AS
SELECT
time_bucket('1 hour', time) as hour,
device_id,
AVG(temperature) as avg_temp
FROM sensor_data
GROUP BY hour, device_id;
```
From there, it's required to [ set a refresh policy](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/refresh-policies/?ref=timescale.com) to automatically refresh your continuous aggregate in a manner that best suits your use case. You're able to keep data in the continuous aggregate that has been dropped from the source hypertable (manually or through data retention policies) for historical purposes and refresh everything else, or you can choose to keep the continuous aggregate and the hypertable automatically in sync while accounting for those retention policies.

```
SELECT add_continuous_aggregate_policy('hourly_temps',
start_offset => INTERVAL '1 month',
end_offset => INTERVAL '1 hour',
schedule_interval => INTERVAL '1 hour');
```
This query sets a refresh policy on a continuous aggregate view called `hourly_temps`
.

Here, the refresh window is set to only look at data up to one month before the current time (as if you are separately dropping raw data older than one month using a data retention policy and want to keep the historical records within your continuous aggregate intact). If you change data outside this window then it your aggregates will not be recalculated.

The refresh window ends one hour before the current time to prevent the policy from trying to refresh data that is still seeing a high number of writes (as well as prevent issues with real-time aggregation, if enabled).

This policy runs once an hour to incrementally update the continuous aggregate within the one-month-to-one-hour window.

**Note:**
*Alongside your refresh policy, you can always manually refresh your continuous aggregate with*
*refresh_continuous_aggregate*
*.*Now you’ll find running a query like the following yields almost instantaneous results:

```
SELECT * FROM hourly_temps
WHERE hour > NOW() - INTERVAL '1 year'
ORDER BY hour DESC;
```
**Side note****Something commonly asked is whether or not window functions are supported. While the answer to this is “no,”**
**:**[that’s simple enough to implement: just create a continuous aggregate that excludes the window function, and then use the window function on your continuous aggregate when it's time to query your data.](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/create-a-continuous-aggregate/?ref=timescale.com#use-continuous-aggregates-with-window-functions)
__there is a workaround__
Running into problems with continuous aggregates? Check out our [ Troubleshooting Guide](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/troubleshooting/?ref=timescale.com) or get in touch with us and the community on
[—we’re happy to help.](https://timescale.slack.com/?ref=timescale.com)
__Slack__## Even More Functionality
As of TimescaleDB 2.9, you can even stack a continuous aggregate on top of a continuous aggregate, implementing [hierarchical continuous aggregates](https://www.timescale.com/blog/an-incremental-materialized-view-on-steroids-how-we-made-continuous-aggregates-even-better/). *Why? Because you can. *(Just kidding.) To save on storage costs, you can remove the original raw data used for calculating the initial continuous aggregate after the first one is complete.

Additional aggregates can be calculated based on the secondary dataset as if they were being performed directly on the original raw datasets. This helps you realize immediate performance benefits as you're performing aggregation on a much smaller dataset with far less data points, allowing complex algorithms to be executed at a much higher speed.

Need real-time results? That’s possible, too—you’re able to enable real-time aggregates to display the most recent raw data in the results. (See more about making use of real-time aggregates [ here](https://docs.timescale.com/use-timescale/latest/continuous-aggregates/real-time-aggregates/?ref=timescale.com). You can also check out the results of

[performance testing](https://www.timescale.com/blog/achieving-the-best-of-both-worlds-ensuring-up-to-date-results-with-real-time-aggregation/#:~:text=Josh%20Lockerman.-,Testing%20Real%2DTime%20Aggregation,-In%20the%20following).)
You may find it worth looking into additional functions that perform efficient aggregations for things like percentile approximations ( and

`uddsketch`
[) as well as data analysis on changing datasets (](https://docs.timescale.com/api/latest/hyperfunctions/percentile-approximation/uddsketch/?ref=timescale.com#uddsketch-and-percentile_agg-functions)
`percentile_agg()`
[and](https://docs.timescale.com/api/latest/hyperfunctions/counters-and-gauges/counter_agg/?ref=timescale.com)
`counter_agg()`
[).](https://docs.timescale.com/api/latest/hyperfunctions/counters-and-gauges/gauge_agg/?ref=timescale.com)
`gauge_agg()`
From there, even more ways to extend the functionality of continuous aggregates through hyperfunctions are available. These are enabled by the use of hypertables and give you advanced functionality like streamlining the use of common statistical aggregates, collecting data with counter aggregation functions, and monitoring system health with heartbeat aggregates. For more information, [ check out the documentation on hyperfunctions](https://docs.timescale.com/use-timescale/latest/hyperfunctions/?ref=timescale.com).

## For Next Time
Interested in more articles like this that'll cover other specific TimescaleDB functionality, like [ SKIP SCAN](https://www.timescale.com/blog/skip-scan-under-load/),

[, or how to](https://www.timescale.com/blog/scale-postgresql-via-partitioning-hypertables/)
__hypertables__[? Keep an eye out for others in this series (or be aware of the content we’re releasing in general) by](https://www.timescale.com/blog/benchmarking-postgresql-batch-ingest/)
__ingest data__[.](https://www.timescale.com/signup/newsletter?ref=timescale.com)
__subscribing to the Timescale newsletter__Remember, if you want to try out any of the features in this post, you can always use the [ open-source TimescaleDB extension](https://github.com/timescale/timescaledb?ref=timescale.com) or

[, no credit card required.](https://console.cloud.timescale.com/signup?ref=timescale.com)
__try out Timescale Cloud free for 30 days__