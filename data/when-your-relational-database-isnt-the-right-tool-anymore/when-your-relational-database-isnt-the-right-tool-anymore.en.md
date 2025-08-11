I’ve been building applications with relational databases for years. Everything worked well until I started dealing with high-frequency data — sensor readings, user activity streams, Internet of Things (IoT) telemetry. As the volume of time-stamped records grew into the millions, I saw relational databases struggling with workloads they weren’t designed for.

That’s when I explored [time series databases](https://www.influxdata.com/time-series-database/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-08_spnsr-ctn_sql-db-to-tsdb_tns). The performance improvements were significant, but what surprised me was the mental shift required.

## The Breaking Point

You’ll know you’ve hit it when dashboards freeze during data ingestion spikes, concurrent reads and writes start blocking each other, and your “last 24 hours” queries take 30+ seconds despite proper indexing.

Here’s what was happening: The database was experiencing lock contention from high-frequency updates while trying to serve dashboard queries at the same time.

The problem wasn’t my code — it was that I was using the wrong tool for [time-stamped, high-frequency data](https://thenewstack.io/how-a-python-processing-engine-speeds-time-series-data-processing).

## The Mental Model Shift

Relational databases trained me to think: “What objects do I need, and how are they related?”

Time series databases made me ask: “What measurements am I taking and when?”

This fundamental change in thinking transforms [how you approach](https://thenewstack.io/the-power-of-tig-stack-mastering-time-series-data-management) certain data problems.

## A Concrete Example

Let’s say you’re tracking flight telemetry data. Here’s how the data models compare:

### **Relational Data Model**

```
-- Flights table
flight_id | airline | departure_time | arrival_time | origin | destination
----------|---------|----------------|--------------|--------|------------
AA1234 | American | 2024-01-15 08:00:00 | 2024-01-15 11:30:00 | JFK | LAX

-- Flight Metrics table (with foreign key)
id | flight_id | metric_type | value    | timestamp
---|-----------|-------------|----------|------------------------
1  | AA1234    | altitude    | 28500.0  | 2024-01-15 08:00:00
2  | AA1234    | speed       | 540.0    | 2024-01-15 08:00:00
3  | AA1234    | heading     | 270.0    | 2024-01-15 08:00:00
4  | AA1234    | altitude    | 29200.0  | 2024-01-15 09:00:00
5  | AA1234    | speed       | 560.0    | 2024-01-15 09:00:00
```

### **Time Series Data Model**

```
-- Single measurement with tags and multiple fields
measurement: flight_metrics
tags: flight_id=AA1234, airline=American, origin=JFK, destination=LAX
timestamp             | altitude | speed | heading
----------------------|----------|-------|--------
2024-01-15 08:00:00   | 28500.0  | 540.0 | 270.0
2024-01-15 09:00:00   | 29200.0  | 560.0 | 268.0
2024-01-15 10:00:00   | 29800.0  | 555.0 | 269.0
```

The difference becomes obvious when you try to query this data. Want the average altitude by minute?

### **Relational Approach**

```
-- Fighting to get time-based data out of a relational structure
SELECT 
    AVG(CASE WHEN metric_type = 'altitude' THEN value END) as avg_altitude,
    DATE_TRUNC('minute', timestamp) as minute
FROM flight_data 
WHERE flight_id = 'AA1234' 
GROUP BY DATE_TRUNC('minute', timestamp);
```

### **Time Series Approach**

```
-- Direct expression of what you actually want
SELECT 
    time_bucket('1m', time) as minute,
    AVG(altitude) as avg_altitude
FROM flight_metrics 
WHERE flight_id = 'AA1234' 
GROUP BY minute;
```

The time series query directly expresses what you’re trying to accomplish, while the relational version requires complex CASE statements and data pivoting.

## **When To Make the Switch**

Time series databases make sense when:

* High write volume is causing database locks.
* Time-based queries are your primary use case.
* Storage costs are growing due to data volume.
* Real-time dashboards need immediate data.

Stick with [SQL](https://thenewstack.io/how-to-write-sql-queries/) when:

* Business logic requires complex joins across entities.
* ACID (atomicity, consistency, isolation, and durability) transactions are critical.
* Data relationships are more important than temporal patterns.
* Data volume isn’t causing performance issues.

## **The ORM Reality**

Here’s the thing about object-relational mapping (ORM): It’s designed for modeling objects and their relationships using foreign keys and navigation properties, not how objects evolve over time. Time series data is fundamentally different — it’s measurements over time, not related entities.

### **ORM Approach**

```
// Think in entities and relationships
public class FlightData
{
    public int Id { get; set; }
    public string FlightId { get; set; }
    public List<FlightMetric> Metrics { get; set; }
}

// Query with navigation properties
var flightWithMetrics = context.FlightData
    .Include(f => f.Metrics.Where(m => m.Timestamp > yesterday))
    .FirstOrDefault(f => f.FlightId == "AA1234");
```

### **Time Series Approach**

```
// Think in measurements at specific time points
public async Task RecordFlightMetrics(string flightId, double altitude, 
    double speed, DateTime timestamp)
{
    var point = PointData
        .Measurement("flight_metrics")
        .Tag("flight_id", flightId)
        .Field("altitude", altitude)
        .Field("speed", speed)
        .Timestamp(timestamp, WritePrecision.Ms);

    await _influxClient.GetWriteApiAsync()
        .WritePointAsync(point, "aviation", "my-org");
}
```

You’ll need to work directly with the database software development kit (SDK), but modern time series databases like InfluxDB 3 support SQL, so the learning curve isn’t steep.

**What you lose with time series:**

* Change tracking and navigation properties.
* Automatic query generation.
* Language-Integrated Query (LINQ) support.

**What you gain:**

* Massive performance improvements for time-based data.
* Built-in time aggregation functions.
* Schema flexibility without migrations.

## **Getting Started**

Don’t rewrite everything. Pick one high-frequency endpoint — maybe logging user activity or system metrics — and route it to a [time series database](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/ "time series database") in parallel with your existing system.

For example, here’s how each approach handles a high-frequency insert pattern.

### **Relational Approach**

```
// High-frequency insert pattern that can cause locks under load
public async Task LogUserActivity(int userId, string action, DateTime timestamp)
{
    var activity = new UserActivity 
    { 
        UserId = userId, 
        Action = action, 
        Timestamp = timestamp 
    };

    _context.UserActivities.Add(activity);
    await _context.SaveChangesAsync(); // This can cause locks under load
}
```

### **Time Series Approach**

```
// Non-blocking writes for high-frequency data
public async Task LogUserActivity(int userId, string action, DateTime timestamp)
{
    var point = PointData
        .Measurement("user_activity")
        .Tag("user_id", userId.ToString())
        .Field("action", action)
        .Timestamp(timestamp, WritePrecision.Ms);

    await _influxClient.GetWriteApiAsync()
        .WritePointAsync(point, "analytics", "my-org"); // Non-blocking writes
}
```

Compare the performance and see if it solves your problems. If it does, you can gradually migrate more workloads.

## **The Hybrid Approach**

Most real applications end up using both relational and time series databases.

**SQL database:** User accounts, orders, transaction processing, business entities.

**Time series database:** High-frequency measurement of events, metrics, logs, sensor data, analytics, monitoring.

This gives you the best of both worlds: rich relational context where business logic matters and efficient time-based storage where volume is the challenge.

The decision point typically occurs when teams spend more time optimizing database performance than developing features. Key indicators for transition include:

* **Lock contention:** Frequent blocking between reads and writes.
* **Query performance:** Time-based queries consistently exceeding acceptable thresholds.
* **Storage growth:** Rapid data accumulation affecting system performance.
* **Operational overhead:** Excessive time spent on database maintenance and optimization.

## **Bottom Line**

Time series databases aren’t replacing SQL; they’re solving a specific problem that SQL databases weren’t designed for. If you’re dealing with high-frequency, time-stamped data and your current database is struggling, it might be time to add a specialized tool to your toolkit. Also, modern time series databases like [InfluxDB 3](https://www.influxdata.com/products/influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-08_spnsr-ctn_sql-db-to-tsdb_tns) support SQL, eliminating learning curve barriers that previously deterred adoption. SQL compatibility enables teams to leverage existing query knowledge while gaining time series-specific performance benefits.

The switch isn’t about abandoning everything you know — it’s about using the right database for the right job.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/adcc6bd9-heatherdowning.png)

Heather Downing is a senior developer advocate for InfluxData with a passion for data telling compelling stories through developer-friendly tools. She takes complex data challenges and translates them into accessible solutions that help developers build meaningful applications with the right...

Read more from Heather Downing](https://thenewstack.io/author/heather-downing/)