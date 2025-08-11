
<!--
title: 关系型数据库的局限：何时该另辟蹊径
cover: https://cdn.thenewstack.io/media/2025/07/e494bd6c-relational-database-not-right-tool.jpg
summary: 关系型数据库在高频数据处理上存在瓶颈，时间序列数据库通过改变思维模式和数据模型来优化性能。选择数据库需考虑数据量、查询类型和业务逻辑。混合使用SQL和时间序列数据库能兼顾业务关系和时间效率。
-->

关系型数据库在高频数据处理上存在瓶颈，时间序列数据库通过改变思维模式和数据模型来优化性能。选择数据库需考虑数据量、查询类型和业务逻辑。混合使用SQL和时间序列数据库能兼顾业务关系和时间效率。

> 译自：[When Your Relational Database Isn't the Right Tool Anymore](https://thenewstack.io/when-your-relational-database-isnt-the-right-tool-anymore/)
> 
> 作者：Heather Downing

我使用关系型数据库构建应用程序已经很多年了。一切都运行良好，直到我开始处理高频数据——传感器读数、用户活动流、物联网 (IoT) 遥测。随着时间戳记录的数量增长到数百万条，我发现关系型数据库在处理它们并非为之设计的工作负载时显得力不从心。

那时我探索了[时间序列数据库](https://www.influxdata.com/time-series-database/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-08_spnsr-ctn_sql-db-to-tsdb_tns)。性能提升非常显著，但令我惊讶的是，这需要思维模式的转变。

## 崩溃点

当仪表板在数据摄取高峰期冻结、并发读写开始相互阻塞，并且即使进行了适当的索引，“最近 24 小时”查询也需要 30 多秒时，您就会知道您已经达到了崩溃点。

以下是当时发生的情况：数据库在尝试同时服务仪表板查询时，由于高频更新而遇到锁争用。

问题不在于我的代码——而在于我使用了错误的工具来处理[带时间戳的高频数据](https://thenewstack.io/how-a-python-processing-engine-speeds-time-series-data-processing)。

## 思维模式的转变

关系型数据库训练我思考：“我需要什么对象，它们之间有什么关系？”

时间序列数据库让我问：“我正在进行哪些测量，以及何时进行？”

这种思维方式的根本转变改变了[您处理](https://thenewstack.io/the-power-of-tig-stack-mastering-time-series-data-management)某些数据问题的方式。

## 一个具体的例子

假设您正在跟踪航班遥测数据。以下是数据模型的比较：

### **关系型数据模型**

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

### **时间序列数据模型**

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

当您尝试查询此数据时，差异变得显而易见。想要按分钟计算的平均高度吗？

### **关系型方法**

```
-- Fighting to get time-based data out of a relational structure
SELECT 
    AVG(CASE WHEN metric_type = 'altitude' THEN value END) as avg_altitude,
    DATE_TRUNC('minute', timestamp) as minute
FROM flight_data 
WHERE flight_id = 'AA1234' 
GROUP BY DATE_TRUNC('minute', timestamp);
```

### **时间序列方法**

```
-- Direct expression of what you actually want
SELECT 
    time_bucket('1m', time) as minute,
    AVG(altitude) as avg_altitude
FROM flight_metrics 
WHERE flight_id = 'AA1234' 
GROUP BY minute;
```

时间序列查询直接表达了您想要完成的事情，而关系型版本则需要复杂的 CASE 语句和数据透视。

## **何时进行切换**

在以下情况下，时间序列数据库是有意义的：

* 高写入量导致数据库锁定。
* 基于时间的查询是您的主要用例。
* 由于数据量增加，存储成本不断增长。
* 实时仪表板需要即时数据。

在以下情况下，坚持使用 [SQL](https://thenewstack.io/how-to-write-sql-queries/)：

* 业务逻辑需要跨实体的复杂连接。
* ACID（原子性、一致性、隔离性和持久性）事务至关重要。
* 数据关系比时间模式更重要。
* 数据量不会导致性能问题。

## **ORM 现实**

关于对象关系映射 (ORM)，需要注意的是：它旨在通过外键和导航属性来建模对象及其关系，而不是对象如何随时间演变。时间序列数据从根本上是不同的——它是随时间变化的测量值，而不是相关的实体。

### **ORM 方法**

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

### **时间序列方法**

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

您需要直接使用数据库软件开发工具包 (SDK)，但像 InfluxDB 3 这样的现代时间序列数据库支持 SQL，因此学习曲线并不陡峭。

**使用时间序列会失去什么：**

* 更改跟踪和导航属性。
* 自动查询生成。
* 语言集成查询 (LINQ) 支持。

**您将获得什么：**

* 基于时间的数据的性能大幅提升。
* 内置的时间聚合函数。
* 无需迁移的模式灵活性。

## **入门**

不要重写所有内容。选择一个高频端点——可能是记录用户活动或系统指标——并将其与现有系统并行路由到[时间序列数据库](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/ "time series database")。

例如，以下是每种方法如何处理高频插入模式。

### **关系型方法**

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

### **时间序列方法**

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

比较性能，看看它是否解决了您的问题。如果解决了，您可以逐步迁移更多工作负载。

## **混合方法**

大多数实际应用程序最终都会同时使用关系型数据库和时间序列数据库。

**SQL 数据库：** 用户帐户、订单、事务处理、业务实体。

**时间序列数据库：** 事件、指标、日志、传感器数据、分析、监控的高频测量。

这为您提供了两全其美的优势：在业务逻辑很重要的地方提供丰富的关系上下文，在量是挑战的地方提供高效的基于时间的存储。

当团队花费更多时间优化数据库性能而不是开发功能时，通常会出现决策点。过渡的关键指标包括：

* **锁争用：** 读写之间频繁阻塞。
* **查询性能：** 基于时间的查询持续超过可接受的阈值。
* **存储增长：** 快速数据积累影响系统性能。
* **运营开销：** 在数据库维护和优化上花费过多时间。

## **底线**

时间序列数据库并没有取代 SQL；它们正在解决 SQL 数据库并非为之设计的特定问题。如果您正在处理高频、带时间戳的数据，并且您当前的数据库正在苦苦挣扎，那么可能是时候在您的工具包中添加一个专用工具了。此外，像 [InfluxDB 3](https://www.influxdata.com/products/influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-08_spnsr-ctn_sql-db-to-tsdb_tns) 这样的现代时间序列数据库支持 SQL，从而消除了之前阻止采用的学习曲线障碍。SQL 兼容性使团队能够利用现有的查询知识，同时获得时间序列特定的性能优势。

这种转换不是要放弃您所知道的一切，而是要为正确的工作使用正确的数据库。