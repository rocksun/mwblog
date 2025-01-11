Jan 10, 2025

Posted by

Semab Tariq

Handling a table with billions of rows in PostgreSQL (or any relational database) can be challenging due to the high level of data complexity, the significant amount of storage space consumed, and performance issues with more complex or analytical queries.

These challenges can all be solved by enabling columnstore (which compresses data) in Timescale and by using Timescale’s chunk-skipping indexes. Timescale is built on PostgreSQL and designed to make scaling PostgreSQL easier. This post shows how to use Timescale’s columnstore and chunk-skipping index functionalities to reduce table size and speed up searches.

Here’s the methodology we’ll follow. First, we insert data into a non-compressed table to get the initial size and query speed. Then, we compare these results with a compressed table. Let's dive in.

We will use PostgreSQL on [ Timescale Cloud](https://www.timescale.com/cloud)—a fully managed database service designed to handle time-series data efficiently. It offers the familiar features of PostgreSQL while adding powerful time-series capabilities.

Features include automatic scaling, high availability, and various performance optimizations, making it easier for developers to store, manage, and query large volumes of time-series data without worrying about infrastructure management.

Here are the instance details that I used for these tests:

- Instance type: Time series
- CPU: 4 cores
- RAM: 16 GB
First, we create a PostgreSQL heap table named `sensor_uncompressed`
in the time-series database and ingest one billion rows into it. After that, we check its statistics, including table size and `SELECT`
query performance.

```
CREATE TABLE sensors_uncompressed (
sensor_id INTEGER,
ts TIMESTAMPTZ NOT NULL,
value REAL
);
```
`CREATE INDEX sensors_ts_idx_uncompressed ON sensors_uncompressed (sensor_id, ts DESC);`
The dataset was placed on an AWS S3 bucket, so we used the utility to ingest data inside the table.

`timescaledb-parallel-copy`
`timescaledb-parallel-copy`
is a command line program for parallelizing PostgreSQL's built-in `COPY`
functionality for bulk-inserting data into `curl https://ts-devrel.s3.amazonaws.com/sensors.csv.gz |gunzip | timescaledb-parallel-copy -batch-size 5000 -connection $DATABASE_URI -table sensors_uncompressed -workers 4 -split '\t' `
Here are some statistics after successfully ingesting one billion rows into the PostgreSQL heap table.

- Time taken to ingest the data: 49 min 12 sec
- Total table size, including index and data: 101 GB
The goal is to compare query execution times by running various scaled aggregate queries on both compressed and uncompressed tables, observing how compressed tables perform in relation to uncompressed ones.

```
SELECT * FROM sensors_uncompressed
WHERE sensor_id = 0
AND ts >= '2023-12-21 07:15:00'::timestamp
AND ts <= '2023-12-21 07:16:00'::timestamp;
Execution Time: 38 ms
```
```
SELECT sensor_id, DATE_TRUNC('day', ts) AS day, MAX(value) AS max_value, MIN(value) AS min_value
FROM sensors_uncompressed
WHERE ts >= DATE '2023-12-21' AND ts < DATE '2023-12-22'
GROUP BY sensor_id, DATE_TRUNC('day', ts)
ORDER BY sensor_id, day;
Execution Time: 6 min 31 sec
```
```
SELECT sensor_id, ts, value
FROM sensors_uncompressed
WHERE ts >= '2023-12-21 07:15:00'
AND ts < '2023-12-21 07:20:00'
ORDER BY value DESC
LIMIT 5;
Execution Time: 6 min 24 sec
```
It is now time to gather statistics for a compressed hypertable (a PostgreSQL table that automatically partitions data by time) utilizing Timescale's columnstore method.

```
CREATE TABLE sensors_compressed (
sensor_id INTEGER,
ts TIMESTAMPTZ NOT NULL,
value REAL
);
```
`CREATE INDEX sensors_ts_idx_compressed ON sensors_compressed (sensor_id, ts DESC);`
`SELECT create_hypertable('sensors_compressed', by_range('ts', INTERVAL '1 hour'));`
`ALTER TABLE sensors_compressed SET (timescaledb.compress, timescaledb.compress_segmentby = 'sensor_id');`
`SELECT add_compression_policy('sensors_compressed', INTERVAL '24 hour');`
`curl https://ts-devrel.s3.amazonaws.com/sensors.csv.gz |gunzip | timescaledb-parallel-copy -batch-size 5000 -connection $CONNECTION_STRING -table sensors_compressed -workers 4 -split '\t' `
Here are the statistics after successfully ingesting one billion rows into the hypertable with compression enabled.

- Time taken to ingest the data: 1 hr 03 mins 21
- Total table size, including index and data: 5.5 GB
```
SELECT * FROM sensors_compressed
WHERE sensor_id = 0
AND ts >= '2023-12-21 07:15:00'::timestamp
AND ts <= '2023-12-21 07:16:00'::timestamp;
Execution Time: 20 ms
```
```
SELECT sensor_id, DATE_TRUNC('day', ts) AS day, MAX(value) AS max_value, MIN(value) AS min_value
FROM sensors_compressed
WHERE ts >= DATE '2023-12-21' AND ts < DATE '2023-12-22'
GROUP BY sensor_id, DATE_TRUNC('day', ts)
ORDER BY sensor_id, day;
Execution Time: 5 min
```
```
SELECT sensor_id, ts, value
FROM sensors_compressed
WHERE ts >= '2023-12-21 07:15:00'
AND ts < '2023-12-21 07:20:00'
ORDER BY value DESC
LIMIT 5;
Execution Time: 4.4 sec
```
**Storage efficiency**: After enabling compression,**the table size was reduced by approximately 95 %**.- Aggregate query 1 is
**47.37 % faster**on the compressed table. - Aggregate query 2 is
**23 % faster**on the compressed table. - Aggregate query 3 is
**98.83 %**faster on the compressed table.
These results demonstrate the significant advantages of using TimescaleDB's compression feature, both in terms of storage savings and improved query performance. Enhancing Postgres Performance With Chunk-Skipping Indexes

Further speeding up PostgreSQL performance and reducing storage footprint are [ Timescale’s chunk-skipping indexes](https://www.timescale.com/blog/boost-postgres-performance-by-7x-with-chunk-skipping-indexes/) (available as of TimescaleDB 2.16.0). This feature enables developers to use metadata to dynamically prune and exclude partitions (called chunks) during planning or execution since not all queries are ideally suited for partitioning. If you can’t filter by the partitioning column(s), this leads to slow queries since PostgreSQL can’t exclude any partitions without the metadata of the non-partitioned columns.

Chunk-skipping indexes optimize query performance by allowing us to bypass irrelevant chunks when searching through large datasets.

In TimescaleDB, data is organized into time-based chunks, each representing a subset of the overall hypertable. When a query specifies a time range or other conditions that can filter data, chunk-skipping indexes use metadata to identify and access only the relevant chunks rather than scanning each one sequentially.

This targeted access minimizes disk I/O and computational overhead, making queries faster and more efficient, especially in hypertables with billions of rows.

Let's create a table named `product_orders`
with columns for order details, such as IDs, timestamps, quantity, total, address, and statuses.

```
CREATE TABLE product_orders (
order_id serial,
order_date timestamptz,
customer_id int,
product_id int,
quantity int,
order_total float,
shipping_address text,
payment_status text,
order_status text
);
```
Transform the `product_orders`
table into a TimescaleDB hypertable, partitioned by `order_date`
with four-day intervals.

```
SELECT create_hypertable('product_orders', 'order_date', chunk_time_interval=>'4 day'::interval);
```
To ingest data, we will use a query that generates 50 million rows of dummy order data, simulating one order per minute starting from January 1, 2023. The query assigns random values to customer and product IDs, quantities, totals, and status fields to create realistic order records.

```
WITH time_series AS (
SELECT generate_series(
'2023-01-01 00:00:00'::timestamptz,
'2023-01-01 00:00:00'::timestamptz + interval '50000000 minutes',
'1 minute'::interval
) AS order_date
)
INSERT INTO product_orders (
order_date, customer_id, product_id, quantity, order_total,
shipping_address, payment_status, order_status
)
SELECT
Order_date,
(random() * 1000)::int + 1 AS customer_id,
(random() * 100)::int + 1 AS product_id,
(random() * 10 + 1)::int AS quantity,
(random() * 500 + 10)::float AS order_total,
'123 Example St, Example City' AS shipping_address,
CASE WHEN random() > 0.1 THEN 'Completed' ELSE 'Pending' END AS
Payment_status,
CASE WHEN random() > 0.2 THEN 'Shipped' ELSE 'Pending' END AS
Order_status
FROM time_series;
```
Once the data ingestion is complete, let's execute a simple `SELECT`
statement to measure the time taken for the query to execute.

```
tsbd=> # select * from product_orders where order_id = 50000000;
order_id | order_date | customer_id | product_id | quantity | order_total | shipping_address | payment_status | order_status
----------+------------------------+-------------+------------+----------+-------------------+------------------------------+----------------+--------------
50000000 | 2117-01-24 12:33:00+00 | 515 | 14 | 9 | 61.00540537187403 | 123 Example St, Example City | Completed | Shipped
(1 row)
Time: 42049.154 ms (00:42.049)
```
Currently, there is no index on the `order_id`
column, which is why the query took nearly 42 seconds to execute.

Let's see if we can reduce the 42 seconds by creating a [B-tree index](https://www.timescale.com/learn/database-indexes-in-postgres) on the `order_id`
column.

```
create index order_id on product_orders (order_id);
```
After creating the index, let's rerun the `SELECT`
query and check if the execution time is reduced from 42 seconds.

```
tsdb=> select * from product_orders where order_id = 50000000;
order_id | order_date | customer_id | product_id | quantity | order_total | shipping_address | payment_status | order_status
----------+------------------------+-------------+------------+----------+-------------------+------------------------------+----------------+--------------
50000000 | 2117-01-24 12:33:00+00 | 515 | 14 | 9 | 61.00540537187403 | 123 Example St, Example City | Completed | Shipped
(1 row)
Time: 9684.318 ms (00:09.684)
```
Great! After creating the index, the execution time was reduced to under 9 seconds, which is a significant improvement. Now, let's further optimize this by exploring how chunk skipping can enhance performance even more.

To take advantage of the chunk-skipping index, we first need to enable chunk skipping on the table and then compress it. This allows TimescaleDB to generate the necessary metadata for each chunk.

```
ALTER TABLE product_orders SET (timescaledb.compress);
SELECT compress_chunk(show_chunks('product_orders'));
SELECT enable_chunk_skipping('product_orders', 'order_id');
```
After enabling chunk skipping and enabling columnstore (which compresses data), let's rerun the same `SELECT`
query to observe the performance improvement.

```
select * from product_orders where order_id = 50000000;
order_id | order_date | customer_id | product_id | quantity | order_total | shipping_address | payment_status | order_status
----------+------------------------+-------------+------------+----------+-------------------+------------------------------+----------------+--------------
50000000 | 2117-01-24 12:33:00+00 | 515 | 14 | 9 | 61.00540537187403 | 123 Example St, Example City | Completed | Shipped
(1 row)
Time: 304.133 ms
```
Wow! **The query now executes in just 304 ms**, resulting in a **99.28 %** improvement compared to the initial execution time without an index and a **96.86 %** performance boost compared to the PostgreSQL index. That's a significant difference!

Query Optimization Method | Execution Time | Performance Improvement (vs. No Index) |
---|---|---|
No Index | 42,049 ms (≈42 sec) | Baseline |
With B-tree Index | 9,684 ms (≈9.7 sec) | 77% faster |
With Chunk-Skipping Index + Columnstore (Compression) | 304 ms (0.3 sec) | 99.28% faster |
In conclusion, using TimescaleDB's key features—like hypertables, columnstore, and chunk-skipping indexes—can greatly improve PostgreSQL performance:

- Hypertables help you manage large amounts of data more easily while keeping everything organized.
- Columnstore reduces storage space and speeds up your queries by cutting the amount of data that needs to be read.
- Chunk-skipping indexes also accelerate query performance by ignoring unnecessary data.
Together, these features make it easier to work with time-series data, events, and real-time analytics. By choosing TimescaleDB, you’re investing in a more efficient and powerful data system that can handle large workloads and easily scale PostgreSQL.

To get started, sign up for a __free Timescale Cloud account____.__