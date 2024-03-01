<!--
title: NoSQL数据建模实践：视频流
cover: https://cdn.thenewstack.io/media/2024/02/3372a9fc-streaming-1024x576.jpg
-->

使用 TypeScript、ScyllaDB 和 Next.js 构建视频流应用的最小设计。

> 译自 [NoSQL Data Modeling in Practice: Video Streaming](https://thenewstack.io/nosql-data-modeling-in-practice-video-streaming/)，作者 Attila Toth 是 ScyllaDB 的开发者倡导者。他撰写教程和博文，参加活动，创建演示和示例应用，帮助开发人员构建高性能应用。

想了解视频流应用背后的原理吗？那就和我一起来探索一种最基本的设计，具备最重要的视频流应用功能：

- 列出所有视频，按创建日期排序（主页）。
- 列出您开始观看的视频。
- 观看视频。
- 从您上次停止的地方继续观看视频。
- 在每个视频缩略图下显示进度条。

我将介绍示例视频流应用程序的技术栈，然后专注于其数据建模过程。该项目[在 GitHub 上可用](https://github.com/scylladb/video-streaming)。如果你喜欢的话，这里还有一个视频可以观看：


**技术栈**

- 编程语言：[TypeScript](https://www.typescriptlang.org/)
- 数据库：[ScyllaDB](https://www.scylladb.com/)
- 框架：[Next.js](https://nextjs.org/)（页面路由）
- 组件库：[Material_UI](https://mui.com/material-ui/)

## 使用 ScyllaDB 构建低延迟视频流应用

[ScyllaDB](https://www.scylladb.com/) 是一种低延迟、高性能的 NoSQL 数据库，与 Apache Cassandra 和 DynamoDB 兼容。它非常适合处理[视频流](https://thenewstack.io/amazon-prime-videos-microservices-move-doesnt-lead-to-a-monolith-after-all/)应用的大规模数据存储和检索需求。ScyllaDB 在所有流行的编程语言中都有驱动程序，并且正如这个示例应用程序所展示的那样，它与现代 [Web 开发框架 Next.js 很好地集成在一起](https://thenewstack.io/next-js-13-debuts-a-faster-rust-based-bundler/)。

在视频流服务的环境中，低延迟对于提供无缝的用户体验至关重要。为了奠定高性能的基础，您需要设计一个符合您需求的数据模型。让我们继续以数据建模过程的示例来了解其具体情况。

## 视频流应用数据建模

在 [ScyllaDB 大学](https://university.scylladb.com/courses/data-modeling/)的数据建模课程中，我们教授 NoSQL 数据建模应始终从您的应用程序和查询开始。然后您逆向思考，并根据您想在应用程序中运行的查询创建模式。这个过程确保您创建的数据模型符合您的查询并满足您的需求。

考虑到这一点，让我们来看看我们的视频流应用程序在每次页面加载时需要运行的查询。

### 页面：继续观看

在此页面上，您可以列出所有您已开始观看的视频。此视图包括视频缩略图以及缩略图下的进度条。

![Zoom](https://cdn.thenewstack.io/media/2024/02/1189992f-image1.png)

### 查询 — 获取观看进度：

```sql
SELECT video_id, progress FROM watch_history WHERE user_id = ? LIMIT 9;
```

### 模式 — 观看历史表：

```sql
CREATE TABLE watch_history (
   user_id text,
   video_id text,
   progress int,
   watched_at timestamp,
   PRIMARY KEY (user_id)
);
```

对于这个查询，将 user_id 定义为分区键是有道理的，因为这是我们用来查询观看历史表的过滤器。请注意，如果以后有一个查询需要在 user_id 以外的其他列上进行过滤，那么这个模式可能需要稍后更新。不过，就目前而言，对于定义的查询来说，这个模式是正确的。

除了进度值之外，应用程序还需要获取每个视频的实际元数据（例如，标题和缩略图图像）。为此，需要查询视频表。

### 查询 — 获取视频元数据：

```sql
SELECT * FROM video WHERE id IN ?;
```

请注意我们使用了“IN”运算符而不是“=”，因为我们需要获取一系列视频，而不仅仅是单个视频。

### 模式 — 视频表：

```sql
CREATE TABLE video (
   id text,
   content_type text,
   title text,
   url text,
   thumbnail text,
   created_at timestamp,
   duration int,
   PRIMARY KEY (id)
);
```

对于视频表，让我们将 id 定义为分区键，因为这是我们在查询中唯一使用的过滤器。

### 页面：观看视频

如果您点击任何一个“观看”按钮，您将被重定向到一个带有视频播放器的页面，您可以在该页面上开始和暂停视频。

![Zoom](https://cdn.thenewstack.io/media/2024/02/e32be4cb-image2.png)

### 查询 — 获取视频内容：

```sql
SELECT * FROM video WHERE id=?;
```

这是一个类似于在“继续观看”页面上运行的查询。因此，对于这个查询，同样的模式也适用。

### 模式 — 视频表：

```sql
CREATE TABLE video (
	   id text,
	   content_type text,
	   title text,
	   url text,
	   thumbnail text,
	   created_at timestamp,
	   duration int,
	   PRIMARY KEY (id)
	);
```

### 最近的视频页面

最后，让我们来分析“最近的视频”页面，这是应用程序的主页。我们最后分析这个页面，因为从数据建模的角度来看，这是最复杂的页面。该页面列出了数据库中最近上传的 10 个视频，按照视频创建日期排序。

![](https://cdn.thenewstack.io/media/2024/02/4b8d4f02-image3.png)

我们将需要分两步获取这些视频：首先获取时间戳，然后获取实际的视频内容。

### 查询 — 获取最近的 10 个视频的时间戳：

```sql
SELECT id, top10(created_at) AS date FROM recent_videos;
```

您可能注意到我们使用了一个名为 top10() 的自定义函数。这不是 [ScyllaDB 中的标准函数](https://thenewstack.io/scylladbs-take-on-webassembly-for-user-defined-functions/)。这是一个我们创建的[用户定义函数](https://opensource.docs.scylladb.com/stable/cql/functions.html#user-defined-functions-experimental)（UDF），用于解决这个数据建模问题。该函数返回表中最近的 created_at 时间戳数组。在 ScyllaDB 中[创建新的 UDF](https://www.scylladb.com/2023/06/20/how-scylladb-distributed-aggregates-reduce-query-execution-time-up-to-20x/) 可以是解决您独特数据建模挑战的一个好方法。

然后，这些时间戳值可以用来查询我们想要在页面上展示的实际视频内容。

### 查询 — 获取这些视频的元数据：

```sql
SELECT * FROM recent_videos WHERE created_at IN ? LIMIT 10;
```

### 模式 — 最近的视频：

```sql
CREATE TABLE recent_videos (
   id text,
   created_at timestamp,
   PRIMARY KEY (created_at)
);
```

```sql
CREATE MATERIALIZED VIEW recent_videos_view AS
	   SELECT * FROM streaming.video
	   WHERE created_at IS NOT NULL
	   PRIMARY KEY (created_at, id);
```

在最近的视频物化视图中，created_at 列是主键，因为我们在第一个查询中通过该列进行过滤，以获取最近的时间戳值。请注意，在某些情况下，这可能会导致[热分区](https://university.scylladb.com/courses/scylla-operations/lessons/scylla-monitoring/topic/hot-partition-large-partition-single-node-check/)。

此外，UI 还会在每个视频缩略图下显示一个小的进度条，指示您观看该视频的进度。为了获取每个视频的进度值，应用程序必须查询观看历史记录表。

### 查询 — 获取每个视频的观看进度：

```sql
SELECT progress FROM watch_history WHERE user_id = ? AND video_id = ?;
```

### 模式 — 观看历史：

```sql
CREATE TABLE watch_history (
   user_id text,
   video_id text,
   progress int,
   watched_at timestamp,
   PRIMARY KEY (user_id, video_id)
);
```

您可能已经注意到，观看历史记录表在先前的查询中已经被用来获取数据。这次，模式必须略微修改以适应此查询。让我们将 video_id 添加为聚集键。这样，获取观看进度的查询就能正常工作了。

就是这样。现在让我们来看看最终的数据库模式！

### 最终的数据库模式

```sql
CREATE KEYSPACE IF NOT EXISTS streaming WITH replication = { 'class': 'NetworkTopologyStrategy', 'replication_factor': '3' };
```

```sql
CREATE TABLE streaming.video (
	   id text,
	   content_type text,
	   title text,
	   url text,
	   thumbnail text,
	   created_at timestamp,
	   duration int,
	   PRIMARY KEY (id)
	);
	

	

	CREATE TABLE streaming.watch_history (
	   user_id text,
	   video_id text,
	   progress int,
	   watched_at timestamp,
	   PRIMARY KEY (user_id, video_id)
	);
	

	

	CREATE TABLE streaming.recent_videos (
	   id text,
	   content_type text,
	   title text,
	   url text,
	   thumbnail text,
	   created_at timestamp,
	   duration int,
	   PRIMARY KEY (created_at)
	);
```

### 最近视频页面的用户定义函数

```sql
-- Create a UDF for recent videos
CREATE OR REPLACE FUNCTION state_f(acc list<timestamp>, val timestamp)
CALLED ON NULL INPUT
RETURNS list<timestamp>
LANGUAGE lua
AS $$
   if val == nil then
       return acc
   end
   if acc == nil then
       acc = {}
   end


   table.insert(acc, val)
   table.sort(acc, function(a, b) return a > b end)
   if #acc > 10 then
       table.remove(acc, 11)
   end
   return acc
$$;




CREATE OR REPLACE FUNCTION reduce_f(acc1 list<timestamp>, acc2 list<timestamp>)
CALLED ON NULL INPUT
RETURNS list<timestamp>
LANGUAGE lua
AS $$
   result = {}
   i = 1
   j = 1
  
   while #result < 10 do
       if acc1[i] > acc2[j] then
           table.insert(result, acc1[i])
           i = i + 1
       else
           table.insert(result, acc2[j])
           j = j + 1
       end
   end
   return result
$$;




CREATE OR REPLACE AGGREGATE top10(timestamp)
SFUNC state_f
STYPE list<timestamp>
REDUCEFUNC reduce_f;
```

这个用户[定义的函数（UDF）使用了 Lua](https://www.scylladb.com/2023/06/20/how-scylladb-distributed-aggregates-reduce-query-execution-time-up-to-20x/)，但你也可以使用 [WASM 来创建 ScyllaDB 中的 UDF](https://www.scylladb.com/2022/04/14/wasmtime/)。在创建函数时，请确保在 scylla.yaml 配置文件中启用了 UDF（位置：/etc/scylla/scylla.yaml）：

## 克隆仓库并开始

要开始，请克隆存储库：

```bash
git clone https://github.com/scylladb/video-streaming
```

安装依赖项：

```bash
npm install
```

修改配置文件：

```bash
APP_BASE_URL="http://localhost:8000"
SCYLLA_HOSTS="172.17.0.2"
SCYLLA_USER="scylla"
SCYLLA_PASSWD="xxxxx"
SCYLLA_KEYSPACE="streaming"
SCYLLA_DATACENTER="datacenter1"
```

迁移数据库并插入示例数据：

```bash
npm run migrate
```

运行服务器：

```bash
npm run dev
```

## 总结

希望您喜欢我们的视频流应用，并且它有助于您使用 ScyllaDB 构建低延迟和高性能的应用程序。如果您想继续学习，请查看 [ScyllaDB University](https://university.scylladb.com/)，我们在那里提供有关[数据建模](https://university.scylladb.com/courses/data-modeling/)、[ScyllaDB 驱动](https://university.scylladb.com/courses/using-scylla-drivers/)程序等免费课程。如果您对视频流示例应用程序或 ScyllaDB 有任何问题，请[访问我们的论坛](https://forum.scylladb.com/)，让我们讨论！

更多 ScyllaDB 示例应用程序：

- [Care-Pet – IoT](https://iot.scylladb.com/)
- [云计算入门指南](https://cloud-getting-started.scylladb.com/)
- [特性存储](https://feature-store.scylladb.com/)

相关资源：

- [视频流应用 GitHub 代码库](https://github.com/scylladb/video-streaming)
- [ScyllaDB 中的 UDF](https://opensource.docs.scylladb.com/stable/cql/functions.html#user-defined-functions-experimental)
- [ScyllaDB 分布式聚合函数如何将查询执行时间降低多达 20 倍](https://www.scylladb.com/2023/06/20/how-scylladb-distributed-aggregates-reduce-query-execution-time-up-to-20x/)
- [Wasmtime：使用 WebAssembly 支持 ScyllaDB 中的 UDF](https://www.scylladb.com/2022/04/14/wasmtime/)
- [ScyllaDB 文档](https://docs.scylladb.com/stable/)
