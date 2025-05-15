# Stop Building Data Pipelines: Cross-Database Queries With PostgreSQL Foreign-Data Wrappers
Imagine you’re running a complex app, with data stored across various places — Amazon RDS for customer data, Timescale for time-series logs, and maybe even some local PostgreSQL instances for legacy data you haven’t yet moved to the cloud. Sounds familiar, right? But what if you need insights that pull all this information together? Enter foreign-data wrappers (FDWs) — a solution so smooth you’ll wonder why you didn’t start using it sooner.

FDWs are PostgreSQL extensions that make cross-database querying ridiculously easy. [postgres_fdw](https://www.postgresql.org/docs/current/postgres-fdw.html) is the extension that acts as a bridge between PostgreSQL databases, allowing your Timescale database to connect directly with data from other PostgreSQL databases. You can query it all in one place without the hassle of data migrations, pipelines, or fragile ETL (extract-transform-load) jobs. It’s like getting a panoramic view of your data landscape, all from the comfort of Timescale’s SQL interface.

Let’s dive into a few scenarios where FDWs shine, each tailored to the kind of problems we face every day as developers managing sprawling, multi-database environments.

✨ Foreign-data wrappers are just one of the many features we’re introducing this week. To see all our October launches and stay updated on upcoming ones,

[visit our blog post]or check out the[launch page].
# Querying Across PostgreSQL Databases With FDWs: Possible Scenarios
## Scenario 1: Taming multi-database analytics in a microservices architecture
Like many other SaaS products, Timescale Cloud uses a microservices architecture where each microservice has its own dedicated PostgreSQL database. For example, we have a project service, a user service, a billing service, a telemetry service, etc. This approach has perks: services are neatly separated, and databases are optimized for specific tasks.

However, we often need to run analytical queries that run joins across multiple databases. For example, let’s say we want to do a cohort analysis of total revenue based on the project creation date. That requires that we join data from the project service and the billing service.

One solution would be to spin up a dedicated analytics database, building a pipeline to pull in data from each service. But with FDWs, we didn’t need to move a thing. We just set up a Timescale service with a number of FDWs to query all the other Timescale services directly. So how can we do the cohort analysis or revenue by project creation date? Easy. Just set up an FDW, and we’re running real-time analytics across services in no time.

Here’s what that might look like in action:

`-- Create the link to the remote server`
CREATE SERVER timescale_billing
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (
host 'serviceID.projectID.tsdb.cloud.timescale.com',
dbname 'tsdb',
port '30702',
extensions 'timescaledb'
);
-- securely store the login details
CREATE USER MAPPING FOR tsdbadmin
SERVER timescale_billing
OPTIONS (
user 'tsdbadmin',
password 'mysupersecurepassword'
);
-- create a billing schema to hold the billing data
CREATE SCHEMA billing;
-- import all tables from the remote server into the billing schema
IMPORT FOREIGN SCHEMA public
FROM SERVER timescale_billing
INTO billing;
-- The project service would be added in the same way
SELECT
time_bucket('1 month', p.creation_date) AS cohort_month,
time_bucket('1 month', b.billing_date) AS billing_month,
SUM(b.revenue) AS total_revenue
FROM
projects.projects p -- this is remote!
JOIN
billing.billing b -- this is remote too!
ON p.project_id = b.project_id
GROUP BY 1,2
ORDER BY 1,2
Now, you have a clean, straightforward query that delivers actionable insights — without a single ETL process in sight.

## Scenario 2: Amazon RDS meets Timescale for real-time analysis
Many of our customers started on AWS RDS and built a feature in their application to provide insights to their customers in the form of an analytics dashboard. An example of such an application would be a multi-tenant SaaS platform to build your own e-commerce site, including a product catalog, customers, orders, shipments, and payments.

A standard feature of such a platform would be an analytics dashboard that gives you visibility into your orders, shipments, and revenue over time. Initially, the analytics screen loaded very fast for each tenant, but as the platform became more popular and the e-commerce sites built on it became as well, some of those tables grew into tens or hundreds of millions of records. The analytics screen started to load very slowly, and you need an alternative solution.

RDS customers adopt Timescale Cloud for its real-time analytics capabilities, which make the in-app analytics dashboard super fast to load. While many of those customers fully migrate to Timescale Cloud, some find that a complete migration of their application is a more complex process. As a result, they choose to only move to Timescale Cloud large tables that perform poorly in RDS.

In the e-commerce sample mentioned earlier, this could include the orders, shipments, and payments tables. However, for some of the analytical queries they run on Timescale Cloud, they need data that is still on RDS, like the product catalog table. Before, they would have had to set up an ETL pipeline to copy the required data from RDS to Timescale Cloud, leading to additional costs and complexity. FDWs eliminate the need for syncing altogether.

With a few simple SQL commands, the required tables in RDS can be made available from Timescale Cloud, enabling cross-system queries within a couple of minutes as if both systems were one. Want to improve the analytics dashboard to show which customers placed the most orders last month? Or determine the most popular products? With FDWs, these questions become trivial. You will configure a FDW as we did before, but this time, pointing to the RDS service. Then you would be ready to start writing queries like this:

`-- Top 10 customers with most orders in January 2024`
SELECT
c.customer_id,
c.name,
count(o.order_id) AS order_count,
sum(o.order_amount) AS total_spent
FROM rds_db.customers c -- remote table
JOIN timescale.orders o -- local table
ON c.customer_id = o.customer_id
WHERE o.timestamp BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY c.customer_id, c.name
ORDER BY order_count DESC, total_spent DESC
LIMIT 10;
You’re not just pulling in data; you’re saving hours on ETL and removing the risks of data duplication and inconsistency.

## Scenario 3: Aggregate distributed data for real-time insights
Consider a global logistics company with data spread across different regions. Vehicle data is recorded in the local region database. Traditionally, you’d be stuck trying to centralize all this data, maybe with an ETL pipeline or an analytics warehouse. But what if you could just query across these databases in real time, leaving the data where it is?

With FDWs, you can do precisely that. Set up your Timescale instance to pull from each region’s database, and you’re ready to aggregate data across regions without moving a byte. Want to see vehicle counts by region over the last day? Done.

`-- Aggregate vehicle data across regions without moving it`
SELECT region, COUNT(*)
FROM (
SELECT 'North America' AS region, timestamp, location FROM na_db.vehicle_data
UNION ALL
SELECT 'Europe' AS region, timestamp, location FROM eu_db.vehicle_data
) AS vehicle_data
WHERE timestamp > NOW() - INTERVAL '1 day'
GROUP BY region;
This query gives you a live snapshot of vehicle activity across regions, ideal for monitoring operations, optimizing routes, or understanding regional performance — all with minimal effort.

Check out our docs for more details on [how to use FDWs in Timescale Cloud](https://docs.timescale.com/use-timescale/latest/schema-management/foreign-data-wrappers/).

# Why FDWs Are a Game Changer
FDWs are more than just a tool — they’re a shortcut to a simplified, integrated data architecture. For developers and data engineers, FDWs remove the burden of moving and transforming data, allowing you to focus on building insights rather than managing infrastructure. Timescale’s implementation of FDWs brings this to life, making it possible to unify data for powerful cross-database analytics without losing time or sleep over ETL.

If you’re ready to break down data silos, streamline analytics, and cut out the middleman (looking at you, ETL), FDWs are ready for you. [Give Timescale Cloud a try](https://console.cloud.timescale.com/signup/?utm_source=blog&utm_medium=email&utm_campaign=november-abl&utm_content=timescale-cloud-signup) — start querying across your PostgreSQL databases today and see just how simple, seamless, and powerful your data workflows can be.

*This article was written by Ramon Guiu, originally published **here** on the Timescale official blog on Nov. 14, 2024.*