在新窗口中打开 打开外部网站 在新窗口中打开外部网站

Category: All posts

Jan 15, 2025

Posted by

Team Timescale

If you’re working with search-driven applications, finding what you need in a sea of unstructured data can feel like searching for a needle in a haystack. Traditionally, keyword search using algorithms like BM25 has been the go-to solution, but let’s be honest—it often misses the mark. Why? Because it focuses on matching exact words rather than understanding the actual context or meaning behind them. This is where **semantic search** comes to the rescue. Semantic search delivers smarter, more relevant results by using vector embeddings to capture the meaning and context of words.

Here’s where it gets even better: when you add filters to semantic search, you can *fine-tune* those results even further. Want to narrow it down by location, category, or custom fields? Easy. Filters let you slice and dice your data to zero in on exactly what you’re looking for.

In this guide, we’ll show you how to supercharge your search capabilities by setting up a semantic search with filters in your PostgreSQL database. We’ll use tools like [ pgvector](https://www.timescale.com/learn/postgresql-extensions-pgvector) (for storing and querying vector embeddings),

Let’s dive in!

Semantic search lets you *cut through the noise* by going beyond basic keyword matching. Instead of just looking for exact word matches, it captures the *intent* and *context* behind your query. How? By using [ vector embeddings](https://www.timescale.com/blog/a-beginners-guide-to-vector-embeddings)—high-dimensional numerical representations that pack the essence of your data into a format machines can understand.

Here’s how it works: Your data gets converted into vector representations. If you’re working with a document, it’s typically broken into smaller chunks, each mapped as a unique point in a high-dimensional vector space. In this space, data with similar meanings are placed closer together. This means that when you search, the system retrieves results based on meaning, not just the words you typed.

Semantic search uses similarity metrics like cosine similarity or Euclidean distance to determine how close these vector points are. These metrics calculate the "distance" between your query vector and the potential matches, helping you find the most relevant results.

For speed, especially with large datasets, algorithms like Approximate Nearest Neighbor Search (ANN) or Hierarchical Navigable Small World (HNSW) come into play. They make finding similar vectors fast and efficient, keeping your searches relevant and lightning-quick.

In search applications, filters are your weapon for making results more relevant and useful. Semantic search does a great job of finding results based on meaning, but when you add filters, you can really zero in on what matters. Filters let you narrow results based on specific criteria—like location, category, date, or custom fields—so users get exactly what they’re looking for.

Let’s say you’re building a product search. Semantic search might pull up items that match a user’s description, but filters can refine those results to show only certain brands, price ranges, or in-stock items. This combination of semantic understanding and attribute-based filtering helps you create highly targeted and actionable search algorithms.

From a technical perspective, filters work by restricting the vector space where the search happens. Instead of scanning everything, the algorithm looks only at vectors that meet your criteria. The result? Searches that are faster and more relevant.

When you’re implementing semantic search with filters, you may run into scenarios where you are working with large datasets or complex filtering criteria. Choosing the right indexing method is key to keeping your search fast and accurate. You’ll come across two standout options: the ** Hierarchical Navigable Small World** (HNSW) algorithm, a popular indexing algorithm, and

HNSW is a graph-based algorithm designed for efficient approximate nearest-neighbor searches. It works by constructing a multi-layered graph where each node represents a data point, and edges connect nodes based on their proximity. This structure allows for rapid traversal and retrieval of similar vectors.

Strengths:

**High recall:**HNSW provides high recall rates, ensuring that the most relevant vectors are retrieved.**Fast query times:**The graph structure enables quick searches, which is beneficial for real-time applications.
Limitations:

**Memory-intensive:**HNSW requires significant in-memory storage, which can be a constraint with large datasets.**Filtered search challenges:**Applying attribute-based filters can be less efficient, as the entire graph may need traversal to enforce filters, leading to increased query times.
To learn more about the [ HNSW algorithm, check out](https://www.timescale.com/blog/vector-database-basics-hnsw) our deep dive.

StreamingDiskANN is an advanced indexing method introduced in pgvectorscale. It addresses some of HNSW's key limitations and is significantly faster.

Advantages over HNSW for filtered searches:

**Efficient filtering:**StreamingDiskANN supports streaming filtering, allowing for accurate retrieval even when secondary filters are applied during similarity search.**Disk-based storage:**Unlike HNSW, which is memory-intensive, StreamingDiskANN stores part of the index on disk. This reduces the reliance on RAM and is more cost-efficient to run and scale as vector workloads grow.
In other words, HNSW delivers high recall and fast queries, but it’s memory-intensive and struggles with filtered searches. StreamingDiskANN, on the other hand, provides a scalable, cost-effective solution with enhanced filtering capabilities, making it perfect for large datasets requiring complex filtered semantic searches. You can read more about StreamingDiskANN and pgvectorscale’s capabilities in [ this blog post](https://www.timescale.com/blog/how-we-made-postgresql-as-fast-as-pinecone-for-vector-data).

In Stack Overflow’s 2024 Developer Survey, [ PostgreSQL](https://survey.stackoverflow.co/2024/technology/#1-databases) was named the most popular database for the second year in a row. DB-Engines also considered

This tutorial will demonstrate how to easily build a semantic search with filters using PostgreSQL and Python. Let’s get started.

First, you’ll need a working installation of PostgreSQL with the necessary extensions. You can install them [ manually](https://github.com/timescale/pgai/tree/main?tab=readme-ov-file&ref=timescale.com#install-from-source) or use a pre-built Docker

Run the following command to pull the TimescaleDB image:

```
docker pull timescale/timescaledb-ha:pg16
```
This image comes with the extensions pre-installed in the default PostgreSQL database. Now, run the container:

`docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb-ha:pg16`
You can now connect to your PostgreSQL instance using the following command:

```
psql -d "postgres://<username>:<password>@<host>:<port>/<database-name>"
```
The default `username`
and `database-name`
are both `postgres`
. Use the password you set when running the Docker container.

Now, enable the extensions:

```
CREATE EXTENSION IF NOT EXISTS ai CASCADE;
CREATE EXTENSION IF NOT EXISTS vectorscale CASCADE;
```
The `CASCADE`
option automatically installs the [ pgvector](https://github.com/pgvector/pgvector) and

`\dx`
You should get an output like this, with ai, vector and vectorscale extensions installed:

```
postgres=# \dx
List of installed extensions
Name | Version | Schema | Description
---------------------+---------+------------+---------------------------------------------------------------------------------------
ai | 0.6.0 | ai | helper functions for ai workflows
plpgsql | 1.0 | pg_catalog | PL/pgSQL procedural language
plpython3u | 1.0 | pg_catalog | PL/Python3U untrusted procedural language
timescaledb | 2.17.2 | public | Enables scalable inserts and complex queries for time-series data (Community Edition)
timescaledb_toolkit | 1.19.0 | public | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
vector | 0.8.0 | public | vector data type and ivfflat and hnsw access methods
vectorscale | 0.5.1 | public | pgvectorscale: Advanced indexing for vector data
(7 rows)
```
This tutorial uses OpenAI’s [ GPT 4o](https://platform.openai.com/docs/models#gpt-4o) model as the LLM. However, you can also choose models from

Head to [ platform.openai.com](http://platform.openai.com) to acquire your OpenAI API Key. Once you have it, create a

`.env`
file and set the API key as an environment variable. Also, add the connection string to the database. ```
OPENAI_API_KEY="your_secret_openai_api_key"
DB_URL="postgres://postgres:password@127.0.0.1:5432/postgres"
```
Create a Python virtual environment, install JupyterLab, and launch it.

```
$ pip install jupyterlab
$ jupyter lab
```
You can now install the required libraries:

```
!pip install psycopg2-binary
!pip install python-dotenv
```
Since we use a local Docker-based installation, we should also install the [pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md) Python

```
!pip install pgai
```
You should now run the vectorizer background worker so that it can generate embeddings later. Here’s how you can do it:

`$ pgai vectorizer worker -d "postgres://postgres:password@127.0.0.1:5432/postgres"`
Now, let’s check if you can successfully connect to OpenAI and retrieve a list of all available models:

```
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
DB_URL = os.environ["DB_URL"]
import psycopg2
with psycopg2.connect(DB_URL) as conn:
with conn.cursor() as cur:
# pass the API key as a parameter to the query. don't use string manipulations
cur.execute("SELECT * FROM ai.openai_list_models(api_key=>%s) ORDER BY created DESC", (OPENAI_API_KEY,))
records = cur.fetchall()
print(records)
```
If your setup is working correctly, this will return a list of the available OpenAI models.

For this tutorial, we will use a [ hotel reviews dataset](https://www.kaggle.com/datasets/pratiyushsingh/timescale-synthetic-hotel-reviews). Each review includes the full text of the review, the type of property, the location, the reviewer’s location, the rating score, the number of bedrooms and bathrooms, and the review date. Some reviews are positive, while others are negative.

Below is what our dataset looks like. For brevity, we have displayed seven rows only:

```
[
{
"review_text": "The hotel was a haven of comfort and luxury. Impeccably clean rooms, friendly staff, and a prime location made our stay unforgettable. The delicious breakfast spread was an added bonus. Highly recommend this gem!",
"date": "2025-01-01",
"category": "hotels",
"name": "Yates, Gonzalez and Mack",
"rating_score": 5,
"location": {
"city": "Cooktown",
"country": "Canada"
},
"customer_location": {
"city": "South Staceyburgh",
"country": "Bahamas"
},
"bedrooms": 3,
"bathrooms": 1
},
{
"review_text": "This hotel is exceptional! The rooms are pristine and beautifully decorated. Staff are incredibly welcoming and attentive. The amenities, including the luxurious pool and spa, are top-notch. An unforgettable stay with stunning views and a delightful atmosphere. Highly recommend!",
"date": "2025-01-02",
"category": "hotels",
"name": "Hill-Hatfield",
"rating_score": 3,
"location": {
"city": "Rachelland",
"country": "Benin"
},
"customer_location": {
"city": "Dorothyview",
"country": "Cayman Islands"
},
"bedrooms": 3,
"bathrooms": 2
},
{
"review_text": "The room was filthy, with stained sheets and a persistently foul odor. Staff was rude and unresponsive to complaints. The so-called \"breakfast\" was inedible. Worst hotel experience I've ever had. Not recommended at all.",
"date": "2025-01-06",
"category": "hotels",
"name": "Rocha, Robinson and Ellis",
"rating_score": 1,
"location": {
"city": "Holmesstad",
"country": "Benin"
},
"customer_location": {
"city": "New Joshua",
"country": "Senegal"
},
"bedrooms": 2,
"bathrooms": 3
},
{
"review_text": "The hostel offers a convenient location with friendly staff and basic amenities. Rooms are clean but can be cramped. Communal areas are lively, though sometimes noisy. Good for budget travelers seeking a social atmosphere.",
"date": "2025-01-11",
"category": "hostels",
"name": "Lane-Kidd",
"rating_score": 2,
"location": {
"city": "North Sarahton",
"country": "Portugal"
},
"customer_location": {
"city": "Port Manuelburgh",
"country": "Philippines"
},
"bedrooms": 5,
"bathrooms": 3
},
{
"review_text": "The hotel was a nightmare\u2014musty room, stained sheets, and a bathroom that screamed for cleaning. Unhelpful staff and paper-thin walls made sleep impossible. The only thing five-star about this place is the regret. Don't stay here.",
"date": "2025-01-11",
"category": "hotels",
"name": "Love Group",
"rating_score": 5,
"location": {
"city": "Mackville",
"country": "New Zealand"
},
"customer_location": {
"city": "East Cole",
"country": "Pitcairn Islands"
},
"bedrooms": 5,
"bathrooms": 2
},
{
"review_text": "These apartments are fantastic! The spacious, modern design and top-notch amenities create a luxurious living experience. The friendly staff and well-maintained facilities make it a pleasure to call this place home. Highly recommended!",
"date": "2025-01-05",
"category": "apartments",
"name": "Jordan LLC",
"rating_score": 1,
"location": {
"city": "Lake Meganview",
"country": "Nepal"
},
"customer_location": {
"city": "Williebury",
"country": "Mexico"
},
"bedrooms": 5,
"bathrooms": 2
},
{
"review_text": "I had an amazing stay at the downtown hostel! The staff was incredibly friendly and helpful, the rooms were clean and cozy, and the communal areas were perfect for meeting fellow travelers. Highly recommend!",
"date": "2025-01-08",
"category": "hostels",
"name": "Torres-Branch",
"rating_score": 2,
"location": {
"city": "Davidsonchester",
"country": "Romania"
},
"customer_location": {
"city": "Wallaceberg",
"country": "Chile"
},
"bedrooms": 5,
"bathrooms": 2
}
]
```
Let’s first create a table named `hotel_reviews`
:

```
conn = psycopg2.connect(DB_URL)
conn.autocommit = True
with conn.cursor() as cur:
cur.execute('''
CREATE TABLE IF NOT EXISTS hotel_reviews (
id BIGINT PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
review_text TEXT,
embedding vector(1536),
category TEXT,
rating_score INTEGER,
location_city TEXT,
location_country TEXT,
customer_city TEXT,
customer_country TEXT,
name TEXT,
date DATE,
bedrooms INTEGER,
bathrooms INTEGER
);
''')
```
Each table column corresponds to a property in our review data. Now, let’s insert our dataset and create embeddings in the process. Here’s how:

```
with conn.cursor() as cur:
for review in hotel_reviews:
print("Inserting review:")
print(review)
cur.execute('''
INSERT INTO hotel_reviews (
review_text, category, rating_score,
location_city, location_country,
customer_city, customer_country, name,
date, bedrooms, bathrooms
)
SELECT
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s
''', (
review['review_text'],
review['category'],
review['rating_score'],
review['location']['city'],
review['location']['country'],
review['customer_location']['city'],
review['customer_location']['country'],
review['name'],
review['date'],
review['bedrooms'],
review['bathrooms']
))
```
[ Pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md) automates the creation and maintenance of vector embeddings directly within PostgreSQL. It allows you to
Here is how you can set it up to automatically generate embeddings.

```
with conn.cursor() as cur:
cur.execute('''
SELECT ai.create_vectorizer(
'Reviews'::regclass,
destination => 'hotel_reviews_embeddings',
embedding => ai.embedding_openai('text-embedding-3-small', 1536),
chunking => ai.chunking_recursive_character_text_splitter('review_text'),
formatting => ai.formatting_python_template('$chunk - Category: $category'),
indexing => ai.indexing_hsnw(min_rows => 50000, opclass => 'vector_l2_ops')
);
''')
```
The vectorizer automatically generates embeddings from the `review_text`
column using OpenAI's model. The embeddings are stored in a separate table (

`text-embedding-3-small`
`hotel_reviews_embeddings_store`
), and a view (`hotel_reviews_embeddings`
) is automatically created to join the original data with its embeddings, making it easy to query and use the embedded data. In the above code, we also create a Hierarchical Navigable Small World (HSNW) index to speed up similarity searches. For larger datasets, [ StreamingDiskANN](https://www.timescale.com/blog/pgvector-is-now-as-fast-as-pinecone-at-75-less-cost) is the recommended approach. When creating the vectorizer, you can set it up in the following way.

```
with conn.cursor() as cur:
cur.execute('''
SELECT ai.create_vectorizer(
'Reviews'::regclass,
destination => 'hotel_reviews_embeddings',
embedding => ai.embedding_openai('text-embedding-3-small', 1536),
chunking => ai.chunking_recursive_character_text_splitter('review_text'),
formatting => ai.formatting_python_template('$chunk - Category: $category'),
indexing => ai.indexing_diskann(min_rows => 100000, storage_layout => 'memory_optimized')
);
''')
```
Now, we’ll create a function to perform semantic search with filters. Here’s the code for the function:

```
def semantic_search(query_text, category=None, min_rating=None, max_rating=None,
min_bedrooms=None, max_bedrooms=None,
min_bathrooms=None, max_bathrooms=None,
location_city=None, location_country=None, limit=5):
"""
Perform semantic search with optional filters on ratings, rooms, and location
"""
with conn.cursor() as cur:
# Build the SQL query with filters
sql = '''
WITH query_embedding AS (
SELECT ai.openai_embed('text-embedding-3-small', %s, api_key=>%s) as embedding
)
SELECT review_text, category, rating_score,
location_city, location_country,
bedrooms, bathrooms,
embedding <=> (SELECT embedding FROM query_embedding) as distance
FROM hotel_reviews
WHERE 1=1
'''
params = [query_text, OPENAI_API_KEY]
if category:
sql += ' AND category = %s'
params.append(category)
if min_rating:
sql += ' AND rating_score >= %s'
params.append(min_rating)
if max_rating:
sql += ' AND rating_score <= %s'
params.append(max_rating)
if min_bedrooms:
sql += ' AND bedrooms >= %s'
params.append(min_bedrooms)
if max_bedrooms:
sql += ' AND bedrooms <= %s'
params.append(max_bedrooms)
if min_bathrooms:
sql += ' AND bathrooms >= %s'
params.append(min_bathrooms)
if max_bathrooms:
sql += ' AND bathrooms <= %s'
params.append(max_bathrooms)
if location_city:
sql += ' AND location_city = %s'
params.append(location_city)
if location_country:
sql += ' AND location_country = %s'
params.append(location_country)
sql += ' ORDER BY embedding <-> (SELECT embedding FROM query_embedding) LIMIT %s'
params.append(limit)
cur.execute(sql, params)
results = cur.fetchall()
return [
{
'review_text': r[0],
'category': r[1],
'rating_score': r[2],
'location_city': r[3],
'location_country': r[4],
'bedrooms': r[5],
'bathrooms': r[6],
'similarity_score': 1 - r[7] # Convert distance to similarity
}
for r in results
]
```
In the `semantic_search`
function, the `query_text`
is converted into an embedding using the procedure. Filters are then applied to refine the results during the semantic search. The function also returns the

`ai.openai_embed`
`similarity_score`
, calculated from the cosine distance.We are now ready to perform a filtered semantic search. Here’s how you can invoke the function with an example query:

```
results = semantic_search(
"private pool",
category="villas",
limit=3
)
for i, result in enumerate(results, 1):
print(f"\nResult {i}:")
print(f"Review: {result['review_text']}")
print(f"Category: {result['category']}")
print(f"Rating: {result['rating_score']}")
print(f"Location: {result['location_city']}, {result['location_country']}")
print(f"Rooms: {result['bedrooms']} bedrooms, {result['bathrooms']} bathrooms")
print(f"Similarity Score: {result['similarity_score']:.2f}")
```
This will return results like the one below:

```
Result 1:
Review: This villa is a stunning oasis of tranquility, offering breathtaking views, elegant interiors, and a serene private pool. It's the perfect blend of luxury and comfort, providing an unforgettable escape filled with beauty and relaxation.
Category: villas
Rating: 4
Location: New Craig, Christmas Island
Rooms: 3 bedrooms, 1 bathrooms
Similarity Score: 0.39
Result 2:
Review: This villa is a paradise! Stunning views, luxurious amenities, and impeccable service. The infinity pool and lush gardens create a serene escape. Perfect for relaxation and rejuvenation. A true gem for anyone seeking an unforgettable retreat!
Category: villas
Rating: 2
Location: Port Ashleyhaven, Reunion
Rooms: 3 bedrooms, 3 bathrooms
Similarity Score: 0.35
Result 3:
Review: The villas exude luxury and tranquility, with stunning ocean views, plush interiors, and a private infinity pool. Impeccable service and lush gardens make this a dreamy getaway. Truly a paradise retreat!
Category: villas
Rating: 5
Location: Hoffmanfort, South Africa
Rooms: 5 bedrooms, 3 bathrooms
Similarity Score: 0.35
```
That’s it! We’ve successfully implemented semantic search with filters in PostgreSQL using the pgai and pgvector extensions. Additionally, we leveraged pgvectorscale’s StreamingDiskANN index for high-performance embedding searches and storage efficiency.

We’ve just built a powerful semantic search engine with filtering capabilities in PostgreSQL, combining the simplicity of pgai and pgvector with the performance boost of pgvectorscale.

Start building your own filtered semantic search today! For more on [ Timescale’s AI stack](https://www.timescale.com/ai), explore the

Here are related blog posts and guides to help you expand your knowledge and learn more about semantic search and beyond:

__Semantic Search With OpenAI and PostgreSQL in 10 Minutes____Combining Semantic Search and Full-Text Search in PostgreSQL (With Cohere, Pgvector, and Pgai)____Implementing Filtered Semantic Search Using Pgvector and JavaScript____PostgreSQL Hybrid Search Using Pgvector and Cohere____How We Made PostgreSQL as Fast as Pinecone for Vector Data__
Originally posted

Jan 15, 2025

pgai

3.3k

pgvectorscale

1.5k