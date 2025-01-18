# How to Automate Data Classification in PostgreSQL With OpenAI
Businesses are inundated with data from various sources, including customer interactions, transactions, support queries, product reviews, and more. This makes data classification a crucial task. However, classifying unstructured data, such as customer reviews and support interactions, has always been challenging. The emergence of large language models (LLMs) is simplifying this process.

In this tutorial, we’ll explore how to use the open-source pgai and pgvector extensions to automate data classification directly within PostgreSQL. This approach is particularly helpful if you already have data within PostgreSQL or want to build classification systems without relying on additional vector databases or frameworks.

🔖 To learn more about turning unstructured data into structured data, check out these resources:
- [Structured vs. Semi-Structured vs. Unstructured Data in PostgreSQL](https://www.timescale.com/learn/structured-vs-semi-structured-vs-unstructured-data-in-postgresql)
- [Parsing All the Data With Open-Source Tools: Unstructured and Pgai](https://timescale.ghost.io/blog/parsing-all-the-data-with-open-source-tools-unstructured-and-pgai/)

# Automating Data Classification in PostgreSQL: Tools
Let’s first take a quick look at pgvector and pgai, the two open-source extensions we’ll use with PostgreSQL. We’ll also look at how OpenAI models can help with the process.

## Pgvector: making PostgreSQL a vector database
[Pgvector](https://github.com/pgvector/pgvector) is a powerful open-source PostgreSQL extension that brings vector-handling capabilities to the database and allows you to store, query, and manage high-dimensional vectors directly within your tables. It is useful for building semantic search, recommendation systems, and data classification algorithms using PostgreSQL.
## Introduction to OpenAI models
OpenAI offers a range of advanced language models that are updated as the technology advances. The flagship models, GPT-4o and GPT-4o Mini, are the latest ones at the time of writing this article. These models are multimodal, capable of processing text and image inputs while producing text outputs, and have been architected to tackle complex, multi-step tasks with high accuracy and speed.

GPT-4o, the most advanced model in the lineup, features a context window of up to 128,000 tokens, allowing it to maintain extensive contextual awareness across long conversations or documents. This model is faster and more cost-effective than previous iterations, such as GPT-4 Turbo.

For developers needing a lighter solution, the GPT-4o Mini is a smaller model and OpenAI’s cheapest model. It has higher intelligence than GPT-3.5-Turbo but is faster and cheaper, and it is meant for lightweight tasks.

The previous generation models, GPT-4 Turbo and GPT-3.5 Turbo, remain available. GPT-4 Turbo also includes vision capabilities, supporting JSON mode and function calling for tasks involving text and images.

## What is pgai?
[Pgai is an open-source extension for PostgreSQL ](https://github.com/timescale/pgai)that brings AI-powered capabilities directly to your database. You can use pgai to interact with machine learning models and build AI workflows within PostgreSQL, enabling you to create AI-powered systems without ever leaving your database environment.
The true power of pgai emerges when it is used in conjunction with pgvector and OpenAI. You can use pgai to harness the vector data stored in PostgreSQL via pgvector and call OpenAI methods to classify this data automatically. This combination allows you to build a fully automated data classification pipeline within PostgreSQL.

# Setting Up
First, you’ll need a working installation of PostgreSQL with the pgvector and pgai extensions. You can either install them [manually](https://github.com/timescale/pgai/tree/main?tab=readme-ov-file&ref=timescale.com#install-from-source) or use a pre-built Docker [container](https://github.com/timescale/pgai/tree/main?tab=readme-ov-file&ref=timescale.com#use-a-pre-built-docker-container). Alternatively, you can simply use [Timescale Cloud](https://console.cloud.timescale.com/?ref=timescale.com) for a free PostgreSQL cloud instance, pre-installed with pgai and pgvector.

Log in or create an account on Timescale Cloud, pick your service type, region, and compute, and then click on ‘Create a service’.

Once your service is created, you’ll receive the connection string, username, password, database name, and port. You can also download the database config.

Let’s save the PostgreSQL database connection string as an environment variable.

`$ export PG_CONNECTION_STRING="your_postgresql_connection_string"`
You will also need OpenAI API keys. Head to [platform.openai.com](http://platform.openai.com/) to get one. Once you have it, save it in an environment variable as well.

`$ export OPENAI_API_KEY="{API_KEY}"`
Now you can use `psql`
to connect in the following way:

`$ PGOPTIONS="-c ai.openai_api_key=$OPENAI_API_KEY" psql -d $PG_CONNECTION_STRING`
You can activate the pgai and pgvector extensions:

`CREATE EXTENSION IF NOT EXISTS ai CASCADE;`
CREATE EXTENSION IF NOT EXISTS vector CASCADE;
Let’s check if the pgai and pgvector extensions are enabled in the PostgreSQL database by running the following command:

`tsdb=> \dx`
List of installed extensions
Name | Version | Schema | Description
---------------------+---------+------------+---------------------------------------------------------------------------------------
ai | 0.4.0 | ai | helper functions for ai workflows
pg_stat_statements | 1.10 | public | track planning and execution statistics of all SQL statements executed
plpgsql | 1.0 | pg_catalog | PL/pgSQL procedural language
plpython3u | 1.0 | pg_catalog | PL/Python3U untrusted procedural language
timescaledb | 2.17.2 | public | Enables scalable inserts and complex queries for time-series data (Community Edition)
timescaledb_toolkit | 1.18.0 | public | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
vector | 0.8.0 | public | vector data type and ivfflat and hnsw access methods
(7 rows)
Let’s also check if the OpenAI function calls are working. You can test this by:

`SELECT *`
FROM ai.openai_list_models()
ORDER BY created DESC;
This code should return the list of all OpenAI models available:

`id | created | owned_by`
-----------------------------+------------------------+-----------------
chatgpt-4o-latest | 2024-08-13 02:12:11+00 | system
gpt-4o-2024-08-06 | 2024-08-04 23:38:39+00 | system
gpt-4o-mini | 2024-07-16 23:32:21+00 | system
gpt-4o-mini-2024-07-18 | 2024-07-16 23:31:57+00 | system
gpt-4o-2024-05-13 | 2024-05-10 19:08:52+00 | system
gpt-4o | 2024-05-10 18:50:49+00 | system
gpt-4-turbo-2024-04-09 | 2024-04-08 18:41:17+00 | system
gpt-4-turbo | 2024-04-05 23:57:21+00 | system
gpt-3.5-turbo-0125 | 2024-01-23 22:19:18+00 | system
gpt-4-turbo-preview | 2024-01-23 19:22:57+00 | system
gpt-4-0125-preview | 2024-01-23 19:20:12+00 | system
…
We can now proceed with the tutorial steps.

# Performing Data Classification in PostgreSQL Using Pgai
In this tutorial, we will start with a list of product reviews. We will then use the pgai and pgvector extensions to classify the reviews into positive, negative, or neutral categories using the OpenAI API. You can use a similar approach to perform any other data classification task.

Let’s first create a `product_reviews`
table with some sample data.

## Create `product_reviews`
table
The following SQL command creates a table named `product_reviews`
to store customer reviews of a product. The table includes columns for customer ID, date of review, product name, a short review, and a detailed review.

`-- Create the `product_reviews` table`
CREATE TABLE product_reviews (
-- Unique identifier for each customer
customer_id INT NOT NULL PRIMARY KEY,
-- Timestamp with timezone for the review date
date TIMESTAMPTZ,
-- Name of the product being reviewed
product TEXT,
-- A brief summary of the review
short_review TEXT,
-- The detailed review text
review TEXT
);
Let’s confirm that the `product_reviews`
table has been created successfully by running the following command:

`\dt`
Output:

`List of relations`
Schema | Name | Type | Owner
--------+-----------------+-------+----------
public | product_reviews | table | postgres
(1 row)
## Insert sample product reviews
Let’s insert sample reviews for products like laptops, phones, and tablets.

`-- Insert sample data into `product_reviews` table`
INSERT INTO product_reviews (customer_id, date, product, short_review, review) VALUES
(1, '2022-01-01', 'laptop', 'Great!', 'Great laptop, very fast and reliable.'),
(2, '2022-01-02', 'laptop', 'Good', 'Good laptop, but the battery life could be better.'),
(3, '2022-01-03', 'laptop', 'Worst ever', 'This is the worst laptop I have ever used.'),
(4, '2022-01-04', 'laptop', 'Not bad', 'Not bad, but the screen is a bit small.'),
(5, '2022-01-05', 'phone', 'Excellent', 'Excellent phone, great camera and battery life.'),
(6, '2022-01-06', 'phone', 'Decent', 'Decent phone, but the screen is not as good as I expected.'),
(7, '2022-01-07', 'phone', 'Poor', 'Poor phone, battery life is terrible and camera quality is not good.'),
(8, '2022-01-08', 'tablet', 'Awesome', 'Awesome tablet, very fast and responsive.'),
(9, '2022-01-09', 'tablet', 'Satisfactory', 'Satisfactory tablet, but the screen resolution could be better.'),
(10, '2022-01-10', 'tablet', 'Disappointing', 'Disappointing tablet, slow performance and battery drains quickly.');
## Create `product_reviews_classification`
table
Next, we’ll create the `product_reviews_classification`
table to store the data classification results, including customer ID and review type. You can use the SQL command below to create the table.

`-- Create the `product_reviews_classification` table`
CREATE TABLE product_reviews_classification (
-- Unique identifier for each customer
customer_id INT NOT NULL PRIMARY KEY,
-- The classification type of the review (e.g., Positive, Negative, Neutral)
review_type TEXT
);
## Classify product reviews and insert them into the `product_reviews_classification`
table
To classify the product reviews under positive, negative, or neutral categories, we will use the OpenAI API. We will use the `openai_chat_complete`
function in SQL provided by the pgai extension to perform the data classification task.

In the SQL command, we will perform three key steps.

**Step 1: Format reviews with a structured template**
In the first step, we’ll format the raw reviews into a structured text format. We can do this by using the `format`
function in SQL, which combines the `short_review`
and `review`
fields into a consistent template.

**Step 2: Classify reviews using OpenAI and categorize the results**
Next, we’ll take the formatted reviews and call OpenAI’s API to classify them as either `positive`
, `negative`
, or `neutral`
. If the classification is one of the three expected categories, we will keep it; otherwise, we will default the review to `neutral`
.

**Step 3: Insert classified reviews into the ****product_reviews_classification**** table**
Finally, we’ll insert the classified review data into the table `product_reviews_classification`
.

Here’s the three-step SQL command that performs the classification task.

`-- Step 1: Format reviews with a structured template`
WITH formatted_reviews AS (
SELECT
customer_id,
format(
E'%s %s\nshort_review: %s\nreview: %s\n\t',
short_review, review, short_review, review
) AS product_final_review
FROM product_reviews
),
-- Step 2: Classify reviews using OpenAI and categorize the results
classified_reviews AS (
SELECT
customer_id,
CASE
WHEN result IN ('positive', 'negative', 'neutral') THEN result
ELSE 'neutral'
END AS review_type
FROM (
SELECT
customer_id,
ai.openai_chat_complete(
'gpt-4o',
jsonb_build_array(
jsonb_build_object(
'role', 'system',
'content', 'You are an assistant that classifies product reviews into positive, negative, or neutral categories. You can only output one of these three categories: positive, negative, or neutral.'
),
jsonb_build_object(
'role', 'user',
'content',
concat(
E'Classify the following product review into positive, negative, or neutral categories. You cannot output anything except "positive", "negative", "neutral":\n\n',
string_agg(x.product_final_review, E'\n\n')
)
)
)
)->'choices'->0->'message'->>'content' AS result
FROM formatted_reviews x
GROUP BY customer_id
) subquery
)
-- Step 3: Insert classified reviews into the `product_reviews_classification` table
INSERT INTO product_reviews_classification (customer_id, review_type)
SELECT customer_id, review_type
FROM classified_reviews
;
In the `openai_chat_complete`
function, we’ll use the ‘gpt-4o’ model.

First, let’s confirm if the product reviews have been classified and inserted into the `product_reviews_classification`
table by running the following command:

`SELECT * FROM product_reviews_classification`
Output:

`customer_id | review_type`
-------------+-------------
4 | neutral
10 | negative
6 | neutral
2 | neutral
9 | neutral
3 | negative
5 | positive
7 | negative
1 | positive
8 | positive
(10 rows)
We can verify our results by performing a simple SQL join.

`-- Join the `product_reviews` and `product_reviews_classification` tables`
SELECT
pr.customer_id,
pr.review,
prc.review_type
FROM
product_reviews pr
JOIN
product_reviews_classification prc
ON
pr.customer_id = prc.customer_id;
Output:

`customer_id | review | review_type`
-------------+----------------------------------------------------------------------+-------------
4 | Not bad, but the screen is a bit small. | neutral
10 | Disappointing tablet, slow performance and battery drains quickly. | negative
6 | Decent phone, but the screen is not as good as I expected. | neutral
2 | Good laptop, but the battery life could be better. | neutral
9 | Satisfactory tablet, but the screen resolution could be better. | neutral
3 | This is the worst laptop I have ever used. | negative
5 | Excellent phone, great camera and battery life. | positive
7 | Poor phone, battery life is terrible and camera quality is not good. | negative
1 | Great laptop, very fast and reliable. | positive
8 | Awesome tablet, very fast and responsive. | positive
(10 rows)
Great! We have successfully classified the product reviews by type by using the `openai_chat_complete`
function by pgai.

# Automating Data Classification Task Using a Trigger
Next, we’ll create a trigger that automates the data classification task. To do this, we first need to encapsulate the SQL command for data classification into a PostgreSQL function, which will be called by the trigger.

## Step 1: Encapsulate the data classification task in a function
`CREATE OR REPLACE FUNCTION classify_and_insert_review() RETURNS TRIGGER AS $$`
BEGIN
-- Step 1: Format the new review with a structured template
WITH formatted_reviews AS (
SELECT
NEW.customer_id AS customer_id,
format(
E'%s %s\nshort_review: %s\nreview: %s\n\t',
NEW.short_review, NEW.review, NEW.short_review, NEW.review
) AS product_final_review
),
-- Step 2: Classify the review using OpenAI and categorize the results
classified_reviews AS (
SELECT
customer_id,
CASE
WHEN result IN ('positive', 'negative', 'neutral') THEN result
ELSE 'neutral'
END AS review_type
FROM (
SELECT
customer_id,
ai.openai_chat_complete(
'gpt-4o',
jsonb_build_array(
jsonb_build_object(
'role', 'system',
'content', 'You are an assistant that classifies product reviews into positive, negative, or neutral categories. You can only output one of these three categories: positive, negative, or neutral.'
),
jsonb_build_object(
'role', 'user',
'content',
format(
E'Classify the following product review into positive, negative, or neutral categories. You cannot output anything except "positive", "negative", "neutral":\n\n%s',
product_final_review
)
)
)
)->'choices'->0->'message'->>'content' AS result
FROM formatted_reviews
) subquery
)
-- Step 3: Insert classified review into the product_reviews_classification table
INSERT INTO product_reviews_classification (customer_id, review_type)
SELECT customer_id, review_type FROM classified_reviews;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
This will create the function `classify_and_insert_review()`
.

## Step 2: Create the trigger
Next, let’s create a trigger that will call the above function whenever a new row is inserted into the `product_reviews`
table.

`CREATE TRIGGER classify_review_trigger`
AFTER INSERT ON product_reviews
FOR EACH ROW
EXECUTE FUNCTION classify_and_insert_review();
Once this trigger is created, every time a new row is inserted into the `product_reviews`
table, the function `classify_and_insert_review()`
will be executed.

# Next Steps
In this tutorial, we performed a simple classification task demonstrating how to use automatic data classification in PostgreSQL using OpenAI and pgai. We used the pgai extension to interact with the OpenAI API and classify product reviews into positive, negative, or neutral categories. We then created a trigger to automate the classification.

To start automating the classification of your data using PostgreSQL and OpenAI, check out [Timescale Cloud’s AI stack](https://www.timescale.com/ai?ref=timescale.com). It includes a complete suite of open-source PostgreSQL extensions — pgvector, pgai, pgai Vectorizer, and pgvectorscale — that will streamline your AI workflows without the overhead of managing multiple systems. Build smarter, more efficient AI solutions today using a [free PostgreSQL database on Timescale Cloud](https://console.cloud.timescale.com/signup?ref=timescale.com).

If you want to build locally, you will find installation instructions for [pgai](https://github.com/timescale/pgai?ref=timescale.com), [pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.com), and [pgvectorscale](https://github.com/timescale/pgvectorscale/?ref=timescale.com) in the respective repositories (GitHub ⭐s welcome!). Here’s an example tutorial using Llama 3 and Ollama to guide you along the way.

*This article was written by Team Timescale *a*nd originally published **here** on the Timescale official blog on Nov. 22, 2022.*