Every year, the [IEEE Spectrum Top Programming Languages](https://spectrum.ieee.org/top-programming-languages-2025) ranking provides a snapshot of what truly matters in the global software ecosystem. In the 2025 list, SQL jumped from No. 9 in 2024 to hold the No. 4 spot, just behind Python, Java and C++. That placement is remarkable, given SQL’s age and its specialized scope.

In this context, the data tells a deeper story: Across decades of innovation, SQL endures as the backbone of enterprise analytics, unmatched in efficiency for representing and querying data at scale. [I’ve written about why SQL is an ideal match for AI](https://thenewstack.io/why-ai-and-sql-go-together-like-peanut-butter-and-jelly/) and believe the spectacular jump in SQL’s popularity further confirms the complementary nature of SQL and [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/), which is often misunderstood when in fact they are both necessary for today’s data-intensive AI workloads.

## **The Origins of SQL**

SQL was created in the 1970s from Edgar Codd’s vision of relational databases and his formalization of relational algebra and set theory. Unlike procedural and functional languages that dictate *how* to perform a task, SQL is declarative; it specifies *what* you want, leaving the engine to determine the path. That set-based abstraction has been applied consistently for decades, supporting workloads from small data sets to systems managing billions of rows, because it is grounded in relational algebra and set theory.

SQL has outlived every hardware cycle and programming trend. It began on mainframes, adapted to UNIX servers, distributed systems and now powers cloud SaaS database engines. SQL engines have been implemented in C, C++, Java and other languages, and optimized for multicore CPUs, GPUs and [NVMe storage](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/). The SQL interface remains standardized, shielding users from complexity while implementations continue to evolve under the hood.

## **SQL vs. Procedural and Functional Mindsets**

The difference between SQL and procedural languages such as [Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/), [C++](https://thenewstack.io/introduction-to-c-programming-language/) and Python is more than syntax. Procedural and functional languages rely on explicit control flow, loops, conditional branches, and function calls to process data one element at a time. In contrast, SQL expresses operations over entire sets of rows at once. Instead of writing a loop to scan a list and sum values, SQL uses an aggregate function (SUM) across a column. Instead of nested `if` statements, SQL applies `WHERE` clauses to filter subsets. Joins replace manual pointer chasing or map lookups by describing how relations connect. This shift means that while procedural code specifies how to compute, SQL specifies what result is required, leaving the database optimizer to decide whether to use an index, perform a hash join or parallelize across multiple CPUs.

## **Python: The Complement, Not the Competitor**

Python, at No. 1 on the list, owes much of its success to data science and machine learning. It is approachable, flexible and supported by a rich ecosystem of numerical and machine learning (ML) libraries. But Python and SQL are not rivals; they complement each other. SQL handles structured storage, filtering, joins and large-scale aggregation; Python provides orchestration, statistical modeling and custom logic.

An analyst might write SQL queries to extract millions of sales records, then switch to Python with pandas or NumPy for visualization or statistical tests. Data engineers embed SQL steps in Python-based workflows using Airflow or Prefect, ensuring efficient database processing before downstream transformation. Some database engines even support Python functions embedded directly within SQL, allowing data wrangling and custom logic to execute close to the data without moving it out of the engine.

## **AI to Python to SQL for the Win**

Python can also be used to write many SQL queries in a template fashion. For example, you might want to create 50 SQL statements that vary to do a similar job on 50 different tables or data sets. A single Python query can generate and run 50 SQL statements easily.

Now, in today’s world, AI can write Python scripts. So through a conversational interface, AI generates Python, and the Python generates SQL.

Example: “Generate me a Python script that generates and runs a SQL query to the population table and average the demographics data. The data is stored in 50 tables, one table per U.S. state, so generate 50 such queries and summarize the data at the end of the Python script.”

And so AI begets Python, which begets SQL in a harmonious chain.

## **What Is the Future for SQL?**

The continued relevance of SQL in 2025 reflects its role as the standard interface for working with structured data. Despite shifts in hardware, programming paradigms and data platforms, SQL has remained stable because it is grounded in relational algebra and set theory. Future trends point toward broader integration of SQL with vector and AI workloads, and embedded procedural languages such as Python for in-database functions.

Rather than being replaced, SQL is likely to remain the common layer across heterogeneous systems such as traditional relational databases, distributed warehouses and hybrid data platforms. Its future is defined by utility: SQL remains the standardized, widely adopted method for querying and managing data, and it continues to be implemented across new engines and infrastructures as they emerge.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/e92364a0-ivannovick.png)

Ivan Novick leads data platform product management at Broadcom's Tanzu division, overseeing real-time data, streaming, OLTP databases, and data warehouses/lakes. He previously spearheaded Tanzu Greenplum innovation for more than a decade, where he drove its evolution from version 4 to...

Read more from Ivan Novick](https://thenewstack.io/author/ivan-novick/)