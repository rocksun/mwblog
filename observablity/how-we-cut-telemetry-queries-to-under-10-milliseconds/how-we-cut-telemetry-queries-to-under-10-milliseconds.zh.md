我们构建了一个遥测管道，可以处理每秒超过 5,400 个数据点，查询响应时间低于 10 毫秒。 我们在以 60FPS（帧每秒）处理飞行模拟器数据时发现的技术适用于任何高频遥测系统，从物联网 (IoT) 传感器到[应用程序监控](https://thenewstack.io/getting-started-with-infrastructure-monitoring/)。

以下是我们如何将查询时间从 30 秒缩短到 10 毫秒以下，以及为什么这些技术适用于任何高频遥测系统。

## **当前值的问题**

每个人都会编写此查询来获取最新的遥测值：

```
SELECT * FROM flight_data
WHERE time >= now() - INTERVAL '1 minute'
ORDER BY time DESC LIMIT 1
```

这会扫描最近的数据，对所有内容进行排序，然后丢弃除一行之外的所有行。 在高频率下，这种模式会完全崩溃。 我们通过 [FSUIPC](http://www.fsuipc.com/) 从 [Microsoft Flight Simulator 2024](https://www.flightsimulator.com/) 以每秒 60 次更新生成 90 多个字段，FSUIPC 是一种实用程序，可作为模拟器与外部应用程序或硬件控制之间的通信中间人。 我们的仪表板刷新需要 30 秒或更长时间。

## **停止查询，开始缓存**

[InfluxDB 3 Enterprise](https://www.influxdata.com/products/influxdb-3-enterprise/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-09_spnsr-ctn_flight-data_tns) 是一个具有内置压缩和缓存功能的时间序列数据库，它提供了一种称为 [Last Value Cache](https://www.influxdata.com/blog/-influxdb3-last-value-cache/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-09_spnsr-ctn_flight-data_tns) (LVC) 的功能。 它不会每次都搜索数千个数据点，而是将每个指标的最新值保存在内存中以供随时使用。

以下是我们设置它的方式：

```
SELECT * FROM last_cache('flight_data', 'flightsim_flight_data_lvc')
```

设置方法：

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

查询时间从 30 多秒降至 10 毫秒以下。 如果您在单独的屏幕上监控飞行员，仪表板会以 5FPS 的速度更新，并且感觉非常快。

## **批量处理一切**

以高频率写入单个遥测点会创建数千个网络往返。 解决方案非常简单：

```
// Batching configuration
MaxBatchSize: 100
MaxBatchAgeMs: 100 milliseconds
```

缓冲点并在达到任一限制时刷新。 这次捕获了每次数据库写入大约六个完整的遥测快照。

**测量的性能：**

* 写入延迟：每行 1.3 毫秒。
* 持续每秒数千个指标。
* 24 小时测试期间零数据丢失。

## **积极压缩**

高频遥测会创建数百个小文件。 我们在 [InfluxDB 3 Enterprise](https://www.influxdata.com/downloads/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-09_spnsr-ctn_flight-data_tns) 中配置了这些环境变量，以使用其压缩功能：

```
# COMPACTION OPTIMIZATION
INFLUXDB3_GEN1_DURATION=5m
INFLUXDB3_ENTERPRISE_COMPACTION_GEN2_DURATION=5m
INFLUXDB3_ENTERPRISE_COMPACTION_MAX_NUM_FILES_PER_PLAN=100

# REAL-TIME DATA ACCESS
INFLUXDB3_WAL_FLUSH_INTERVAL=100ms
INFLUXDB3_WAL_MAX_WRITE_BUFFER_SIZE=200000
```

更小的时间窗口（五分钟与默认的 10 分钟）和更频繁的压缩可防止文件累积，并且它在我们的场景中效果很好。

**24 小时结果：**

* 142 次自动压缩事件。
* 从 127 个文件优化到 18 个文件 (Parquet)。
* 存储从 500MB 减少到 30MB（减少 94%）。

## **块读取**

我们通过 [FSUIPC Client DLL](https://github.com/InfluxCommunity/msfs2influxdb3-enterprise) 进行了 90 多个单独的 API 调用来收集遥测数据。 以 60FPS 的速度，每秒超过 5,000 个调用。 开销正在压垮性能。

解决方案：将相关指标分组到内存块中。

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

每个块在一个操作中获取多个相关参数。

影响从每秒 2,700 到 5,400 次调用减少到每秒 240 到 480 次调用（减少 90% 以上）。

## **将实时查询与历史查询分离**

我们构建了两种不同的模式：

* **实时（使用 Last Value Cache）：** 仅当前值，低于 10 毫秒的响应。
* **历史（传统 [SQL](https://roadmap.sh/sql)）：** 趋势和分析，可以接受较慢的读取速度。

事后看来，这种分离似乎很明显，但大多数[监控系统都试图通过相同的查询模式来满足这两种需求](https://thenewstack.io/why-you-need-a-centralized-approach-to-monitoring/)。

## **实时仪表板的模式和实践**

这些不是奇特的技术。 无论您是监控制造设备、跟踪应用程序[指标还是处理市场数据馈送](https://thenewstack.io/python-mqtt-tutorial-store-iot-metrics-with-influxdb/)，模式都是相同的：

1. 将当前值缓存在内存中。
2. 以 100-200 毫秒的间隔批量写入。
3. 配置积极压缩。
4. 一起读取相关指标。
5. 将实时查询与历史查询分离。

## **结果**

这些技术适用于您处理高频数据的任何地方：

* **物联网传感器：** 制造设备、智能建筑、环境监测。
* **应用程序指标：** 应用程序性能监控 (APM) 数据、微服务遥测、分布式跟踪。
* **金融数据：** 市场馈送、交易系统、风险监控。
* **游戏：** 玩家遥测、服务器指标、性能监控

实施这些模式后：

* 查询时间：从 30 秒减少到 10 毫秒以下。
* 存储：减少 94%。
* API 调用：减少 90%。
* 仪表板体验：真正实时（嗯，尽可能接近！）。

区别不在于更快的硬件，而在于使用适合高频数据的正确模式。 我希望您尝试一下这些技术！

## **代码**

GitHub 上的完整实现：

无论您是为飞行模拟器还是生产监控系统构建，我们都发现这些模式在实时数据处理的道路上非常有趣。