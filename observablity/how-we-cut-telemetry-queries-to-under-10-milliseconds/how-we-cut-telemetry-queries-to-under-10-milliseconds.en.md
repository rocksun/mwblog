We built a telemetry pipeline that handles more than 5,400 data points per second with sub-10 millisecond query responses. The techniques we discovered while processing flight simulator data at 60FPS (frames per second) apply to any high-frequency telemetry system, from Internet of Things (IoT) sensors to [application monitoring](https://thenewstack.io/getting-started-with-infrastructure-monitoring/).

Here’s how we got our queries from 30 seconds down to sub-10ms, and why these techniques work for any high-frequency telemetry system.

## **The Problem With Current Values**

Everyone writes this query to get the latest telemetry value:

```
SELECT * FROM flight_data
WHERE time >= now() - INTERVAL '1 minute'
ORDER BY time DESC LIMIT 1
```

This scans recent data, sorts everything, then throws away all but one row. At high frequencies, this pattern completely breaks down. We were generating more than 90 fields at 60 updates per second from [Microsoft Flight Simulator 2024](https://www.flightsimulator.com/) through [FSUIPC](http://www.fsuipc.com/), a utility that serves as a middleman for communication between the simulator and external apps or hardware controls. Our dashboards were taking 30 seconds or more to refresh.

## **Stop Querying, Start Caching**

[InfluxDB 3 Enterprise](https://www.influxdata.com/products/influxdb-3-enterprise/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-09_spnsr-ctn_flight-data_tns), a time series database with built-in compaction and caching features, offers something called [Last Value Cache](https://www.influxdata.com/blog/-influxdb3-last-value-cache/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-09_spnsr-ctn_flight-data_tns) (LVC). Instead of searching through thousands of data points every time, it keeps the most recent value for each metric ready in memory.

Here’s how we set it up:

```
SELECT * FROM last_cache('flight_data', 'flightsim_flight_data_lvc')
```

Setting it up:

```
influxdb3 create last_cache \
  --database flightsim \
  --table flight_data \
  --key-columns aircraft_tailnumber \
  --value-columns flight_altitude,speed_true_airspeed,flight_heading_magnetic,flight_latitude,flight_longitude \
  --count 1 \
  --ttl 10s \
  flightsim_flight_data_lvc
```

The query time dropped from 30+ seconds to less than 10ms. Dashboards update at 5FPS and feel pretty instantaneous if you are monitoring a pilot on a separate screen.

## **Batch Everything**

Writing individual telemetry points at high frequency creates thousands of network round trips. The fix is pretty simple:

```
// Batching configuration
MaxBatchSize: 100
MaxBatchAgeMs: 100 milliseconds
```

Buffer points and flush when you hit either limit. This captures about six complete telemetry snapshots per database write.

**Measured performance:**

* Write latency: 1.3ms per row.
* Sustained thousands of metrics per second.
* Zero data loss during 24-hour tests.

## **Aggressive Compaction**

High-frequency telemetry creates hundreds of small files. We configured these environment variables in [InfluxDB 3 Enterprise](https://www.influxdata.com/downloads/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-09_spnsr-ctn_flight-data_tns) to use its compaction feature:

```
# COMPACTION OPTIMIZATION
INFLUXDB3_GEN1_DURATION=5m
INFLUXDB3_ENTERPRISE_COMPACTION_GEN2_DURATION=5m
INFLUXDB3_ENTERPRISE_COMPACTION_MAX_NUM_FILES_PER_PLAN=100

# REAL-TIME DATA ACCESS
INFLUXDB3_WAL_FLUSH_INTERVAL=100ms
INFLUXDB3_WAL_MAX_WRITE_BUFFER_SIZE=200000
```

Smaller time windows (five minutes vs. the default 10 minutes) and more frequent compaction prevent file accumulation, and it worked well enough for our scenario.

**24-hour results:**

* 142 automatic compaction events.
* From 127 files to 18 optimized files (Parquet).
* Storage from 500MB to 30MB (94% reduction).

## **Block Reading**

We were making 90+ individual API calls through the [FSUIPC Client DLL](https://github.com/InfluxCommunity/msfs2influxdb3-enterprise) to collect telemetry. At 60FPS, that’s over 5,000 calls per second. The overhead was crushing performance.

Solution: Group related metrics into memory blocks.

```
_memoryBlocks = new Dictionary<string, MemoryBlock>
{
    // Position, attitude, altitude
    { "FlightData", new MemoryBlock(0x0560, 48) },
    { "Engine1", new MemoryBlock(0x088C, 64) },
    { "Engine2", new MemoryBlock(0x0924, 64) },
    // Flight controls, trim
    { "Controls", new MemoryBlock(0x0BC0, 44) },
    { "Autopilot", new MemoryBlock(0x07BC, 96) }
};
```

Each block fetches multiple related parameters in one operation.

The impact went from 2,700 to 5,400 calls/second down to 240 to 480 calls/second (90%+ reduction).

## **Separating Real-Time From Historical Queries**

We built two distinct modes:

* **Real time (using Last Value Cache):** Current values only, sub-10ms response.
* **Historical (traditional [SQL](https://roadmap.sh/sql)):** Trends and analysis, acceptable to be slower reads.

This separation seems obvious in hindsight, but most [monitoring systems try to serve both needs](https://thenewstack.io/why-you-need-a-centralized-approach-to-monitoring/) with the same query patterns.

## **Patterns and Practices for Real-Time Dashboarding**

These aren’t exotic techniques. Whether you’re monitoring manufacturing equipment, tracking application [metrics or processing market data feeds](https://thenewstack.io/python-mqtt-tutorial-store-iot-metrics-with-influxdb/), the patterns are the same:

1. Cache current values in memory.
2. Batch writes at 100-200ms intervals.
3. Configure aggressive compaction.
4. Read related metrics together.
5. Separate real-time from historical queries.

## **The Results**

These techniques work anywhere you’re dealing with high-frequency data:

* **IoT sensors:** Manufacturing equipment, smart buildings, environmental monitoring.
* **Application metrics:** Application performance monitoring (APM) data, microservice telemetry, distributed tracing.
* **Financial data:** Market feeds, trading systems, risk monitoring.
* **Gaming:** Player telemetry, server metrics, performance monitoring

After implementing these patterns:

* Query time: 30 seconds down to sub-10ms.
* Storage: 94% reduction.
* API calls: 90% fewer.
* Dashboard experience: Actually real time (well, as close as we could get!).

The difference isn’t about faster hardware, it’s about using the right patterns for high-frequency data. I hope you give these techniques a try!

## **The Code**

Complete implementation on GitHub:

Whether you’re building for flight simulators or production monitoring systems, we found these patterns were fun to discover on the path to real-time data handling.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/adcc6bd9-heatherdowning.png)

Heather Downing is a senior developer advocate for InfluxData with a passion for data telling compelling stories through developer-friendly tools. She takes complex data challenges and translates them into accessible solutions that help developers build meaningful applications with the right...

Read more from Heather Downing](https://thenewstack.io/author/heather-downing/)