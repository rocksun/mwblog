__hrp__ data-ext-id="eanggfilgoajaocelnaflolkadkeghjp">

在新窗口中打开 打开外部网站 在新窗口中打开外部网站

Category: All posts

Mar 11, 2025

Posted by

Team Timescale

Retrieval-augmented generation (RAG) has become the go-to method for enhancing large language models (LLMs). RAG helps tackle challenges like outdated information, high computational costs, and hallucinations, making it ideal for many real-world applications. At its core, RAG enhances an LLM by connecting it with external, domain-specific data sources to improve accuracy and relevance.

If AWS is part of your cloud stack, Amazon Bedrock makes it easy to build an efficient RAG system. It provides access to top-tier foundation models from leading AI companies like Anthropic, allowing you to develop and scale generative AI applications securely on AWS.

In this guide, we’ll show you how to build a RAG system in JavaScript using Anthropic’s Claude Sonnet-3.5, Bedrock embedding models, and pgvector to manage vector embeddings in PostgreSQL. This approach lets you quickly integrate RAG features into your existing AWS applications.

RAG systems augment an LLM’s context with relevant data retrieved from data stores or APIs. By enriching the LLM’s context with external information, RAG systems help reduce hallucinations and improve response accuracy.

In a typical RAG system, data points are first converted into vector embeddings—numerical representations that capture key features of the data. When a user submits a query, it is also converted into embeddings, and a similarity search is performed between the query embeddings and the stored data embeddings. This process retrieves the most semantically relevant results, ensuring more accurate and contextually relevant responses.

Traditionally, RAG systems made use of specialized vector databases. However, as we’ve discussed, [ vector databases are the wrong abstraction](https://www.timescale.com/blog/vector-databases-are-the-wrong-abstraction), and you can easily achieve everything that vector databases offer by using

Let’s take a quick look at the stack we’ll use here:

**Amazon Bedrock**: a managed AI service for integrating foundation models into applications**Anthropic Claude Sonnet 3.5**: an LLM optimized for reasoning and generating enriched responses**Embedding model**: converts text into vector embeddings for similarity search**Pgvector**: a PostgreSQL extension for storing and querying high-dimensional vector embeddings
For this guide, we’ll use the [ Cohere/movies](https://huggingface.co/datasets/Cohere/movies) dataset. Here’s an overview of the workflow:

**Load and store dataset:**Fetch the dataset from Hugging Face and store metadata with vector embeddings in PostgreSQL using Amazon Bedrock.**Vector search:**Perform similarity search (cosine or Euclidean) to find matching movies.**AI Recommendation:**Use Claude Sonnet-3.5 to generate context-aware suggestions.
First, sign in to the AWS Management Console, search for Amazon Bedrock, and open the service.

If you're new to AWS, make sure your billing is set up. Next, you'll need access to the Claude 3.5 Sonnet model for generating responses and Titan Text Embeddings V2 for vectorizing movie descriptions.

Before using the models, first request access to them.

- In the Amazon Bedrock dashboard, go to the Model Access tab.
- Look for Anthropic Claude 3.5 Sonnet, and Titan Text Embeddings V2.
- Click Request Access for both models.
AWS may take some time to approve your request, so check back periodically if access isn’t granted immediately.

- Use the search bar to find Claude 3.5 Sonnet and Titan Text Embeddings V2.
- Click on each model to open its details page.
- Here, you’ll find API references, pricing details, and usage guidelines.
To integrate these models into your project, you’ll need the API endpoints and request formats.

- On each model’s page, navigate to the API Reference section.
- Take note of the endpoint, required parameters, and authentication details.
- You’ll use this information later when making API calls from your Node.js backend.
We’ll use a preconfigured [ Docker container](https://github.com/timescale/pgai/blob/main/docs/install/docker.md) by pgai to set up PostgreSQL locally. This Docker image comes with pgvector pre-installed, making it easy to get started.

```
docker run -d --name pgai -p 5432:5432 \
-v pg-data:/home/postgres/pgdata/data \
-e POSTGRES_PASSWORD=password postgres/postgresdb-ha:pg17
```
Download and install the **LTS version of Node.js**, which includes npm for managing dependencies. Once installed, verify the installation using:

```
node -v
npm -v
```
Create a new Node.js project in your directory with:

`node init -y`
With your project environment ready, it's time to install the required dependencies and configure both the AI model and database clients.

Next, install the essential npm packages needed for this project:

```
npm install pg
npm install @aws-sdk/client-bedrock-runtime
npm install axios
npm install @anthropic-ai/sdk
npm install dotenv
```
Here’s what each package does:

**pg:**enables PostgreSQL connectivity, allowing you to store and retrieve vector embeddings**@aws-sdk/client-bedrock-runtime:**provides an interface to interact with Amazon Bedrock, enabling AI model execution**axios:**an HTTP client for making API requests, used for fetching external datasets**@anthropic-ai/sdk:**simplifies interaction with Claude AI for AI-generated responses and recommendations
To connect to Amazon Bedrock and Claude AI, you need to store your API credentials securely.

Create a **.env** file in your project directory and add:

```
AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>
ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>
```
Finally, import and configure `dotenv`
at the beginning of your script:

```
import dotenv from "dotenv";
dotenv.config();
```
Now, import the required libraries in your `index.js`
file:

```
import pkg from "pg";
const { Client } = pkg;
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";
import axios from "axios";
import Anthropic from "@anthropic-ai/sdk";
```
With the dependencies installed and imported, let’s configure access to the database and Bedrock models.

If you’re using the API key from Anthropic, you can set it up like this:

```
const vectorLength = 512; // Define the vector dimension
const anthropic = new Anthropic({
apiKey: process.env["ANTHROPIC_API_KEY"], // Retrieves the API key from environment variables
});
```
Next, let’s connect to the PostgreSQL instance, where the movie embeddings will be stored:

```
const client = new Client({
user: "<YOUR_POSTGRES-SQL_USERNAME>",
host: "<YOUR_POSTGRES-SQL_HOST_URL>",
database: "<YOUR_POSTGRES-SQL_DATABASE>",
password: "<YOUR_POSTGRES-SQL_PASSWORD>",
port: 31351, // Default port for POSTGRES-SQL
});
```
We’ll use Amazon Bedrock for text embedding and AI inference, so let’s set it up:

```
const bedrockClient = new BedrockRuntimeClient({
region: "us-west-1", // Specify the AWS region
credentials: {
accessKeyId: process.env.AWS_ACCESS_KEY_ID,
secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
},
});
```
Now that the database connection is set up, the next step is to enable the pgvector extension and create a table to store movie data along with vector embeddings.

```
// Function to Create Table
async function createTable() {
try {
// Enable necessary extensions
await client.query("CREATE EXTENSION IF NOT EXISTS vector;");
// Define the table schema
const query = `
CREATE TABLE IF NOT EXISTS movie (
id SERIAL PRIMARY KEY,
title TEXT NOT NULL,
overview TEXT,
genres TEXT,
producer TEXT,
"cast" TEXT,
embedding VECTOR(${vectorLength})
);
`;
// Execute table creation query
await client.query(query);
console.log("Table 'movie' created successfully.");
} catch (error) {
console.error("Error creating table:", error);
}
}
```
The table stores movie metadata, including title, overview, genre, producer, and cast, along with an embedding column that holds vectorized representations of the movie data.

Let’s create a function to load the [ Cohere/movies dataset](https://huggingface.co/datasets/Cohere/movies) from Hugging Face.

```
// Load Dataset from Hugging Face
async function loadDataset() {
try {
const url =
"https://datasets-server.huggingface.co/rows?dataset=Cohere%2Fmovies&config=default&split=train&offset=0&length=100";
const response = await axios.get(url);
if (!response.data.rows) {
throw new Error("Invalid dataset structure");
}
const dataset = response.data.rows.map((item) => item.row); // Extract actual data
console.log("Dataset loaded successfully! Sample:", dataset.slice(0, 1)); // Show first record
return dataset;
} catch (error) {
console.error("Error loading dataset:", error.message);
return [];
}
}
```
Next, we’ll write a function to convert the movie descriptions into vector embeddings using Amazon Bedrock’s Titan-Embed-Text-v2. Here’s how:

```
// Generate Embeddings Using Amazon Bedrock
async function generateEmbedding(description) {
const json_data = {
inputText: description,
dimensions: vectorLength,
normalize: true,
};
try {
const command = new InvokeModelCommand({
modelId: "amazon.titan-embed-text-v2:0",
contentType: "application/json",
body: JSON.stringify(json_data),
});
const response = await bedrockClient.send(command);
const parsedResponse = JSON.parse(new TextDecoder().decode(response.body));
if (!parsedResponse.embedding || !Array.isArray(parsedResponse.embedding)) {
throw new Error(`Invalid embedding format: ${JSON.stringify(parsedResponse)}`);
}
return `[${parsedResponse.embedding.join(",")}]`;
} catch (error) {
console.error("Error generating embedding:", error);
return null;
}
}
```
Now that we have movie descriptions and their embeddings, the next step is to store them in the PostgreSQL database. Let’s write a function to insert each movie’s details along with its vector embedding, enabling us to perform semantic searches later.

```
// Insert Data into Postgres
async function insertDataIntoPostgres(data) {
try {
const insertQuery = `
INSERT INTO movie (title, overview, genres, producer, "cast", embedding)
VALUES ($1, $2, $3, $4, $5, $6);
`;
for (const record of data) {
try {
const embedding = await generateEmbedding(`${record.title} ${record.overview}`);
if (!embedding) {
console.warn(`Skipping record due to embedding failure: ${record.title}`);
continue;
}
await client.query(insertQuery, [
record.title,
record.overview,
record.genres,
record.producer || "",
record.cast || "",
embedding,
]);
} catch (innerError) {
console.error(`Error inserting record (${record.title}):`, innerError);
}
}
console.log("Data inserted successfully!");
} catch (error) {
console.error("Error inserting data into Postgres:", error);
}
}
```
Instead of relying on keyword matching, we’ll use [vector similarity search](https://www.timescale.com/learn/vector-search-vs-semantic-search) with pgvector. This approach compares the query’s vector representation to the stored movie embeddings, allowing for more accurate and context-aware results.

Let’s write a function to perform a similarity search:

```
// Semantic Search - Finding Similar Movies Using Vector Search
async function querySimilarMovies(query, top_k = 2) {
try {
console.log("Searching for:", query);
const queryEmbedding = await generateEmbedding(query);
if (!client) {
console.error("Database client is not initialized.");
return [];
}
// Check if the client is connected; if not, connect manually
if (!client._connected) {
console.log("Client is not connected. Attempting to connect...");
await client.connect();
console.log("Connected to database successfully.");
}
const searchQuery = `
SELECT id, title, overview, genres, producer, "cast", embedding <-> $1 AS similarity
FROM movie
ORDER BY similarity ASC
LIMIT $2;
`;
const { rows } = await client.query(searchQuery, [queryEmbedding, top_k]);
console.log("Query executed successfully.");
console.log("Search Results:", rows);
return rows;
} catch (error) {
console.error("Error in querySimilarMovies:", error.message);
console.error(error.stack);
return [];
} finally {
if (client._connected) {
await client.end();
console.log("Database connection closed.");
}
}
}
```
Above, we’re using the ** <-> **operator in pgvector, which applies the L2 distance metric to retrieve the most relevant movies by measuring the distance between the query vector and stored embeddings.

Now that all the components are in place, we’ll create a function to connect to PostgreSQL, load the movie dataset, generate embeddings, and efficiently insert the data.

```
// Automating Data Ingestion into PostgresSql
async function fetchAndInsertData() {
try {
await client.connect();
console.log("Connected to PostgreSQL");
await createTable(); // Ensure the table exists
const dataset = await loadDataset(); // Load dataset
console.log(dataset.length)
if (dataset.length > 0) {
await insertDataIntoPostgres(dataset);
}
} catch (error) {
console.error("Error in testInsert execution:", error);
} finally {
await client.end();
}
}
```
Now, we’ll write a function to use Amazon Bedrock to send queries and context to Claude 3.5 Sonnet, helping it generate accurate and context-aware responses.

```
// Amazon Bedrock Anthropic Claude 3.5 Sonnet
async function getClaudeResponseBedRock(query, context) {
try {
// Construct request payload
const requestPayload = {
modelId: "anthropic.claude-3-5-sonnet-20240620-v1:0",
contentType: "application/json",
accept: "application/json",
body: JSON.stringify({
anthropic_version: "bedrock-2023-05-31",
max_tokens: 1000,
messages: [
{
role: "user",
content: [
{
type: "text",
text: `You are a human-friendly answer generator from the given query and context. Respond with only the answer - detailed.\n\nQuery: ${query}\nContext: ${JSON.stringify(context)}`,
},
],
},
],
}),
};
// Send the request to Amazon Bedrock
const command = new InvokeModelCommand(requestPayload);
const response = await bedrockClient.send(command);
// Parse the response body
const parsedResponse = JSON.parse(new TextDecoder().decode(response.body));
// Extract and return the model's response
if (!parsedResponse || !parsedResponse.content || !parsedResponse.content.length) {
throw new Error(`Invalid LLM response: ${JSON.stringify(parsedResponse)}`);
}
return parsedResponse.content[0].text; // Return the response text
} catch (error) {
console.error("Error in getClaudeResponse:", error);
return null;
}
}
```
After sending the request, the response is parsed to extract and return the human-friendly answer generated by Claude.

- Query: This is the user’s question or input.
- Context: Additional context is provided in a structured format, allowing the model to generate more accurate and relevant answers.
Alternatively, you can also:

In this approach, we’ll directly call the Claude 3.5 Sonnet API to generate context-aware responses based on the query and provided context. The code below sends a request to Claude 3.5 Sonnet, asking it to generate a detailed, human-friendly response.

```
// Anthropic Claude 3.5 Sonnet API
async function getClaudeResponse(query, context) {
try {
const msg = await anthropic.messages.create({
model: "claude-3-5-sonnet-20241022",
max_tokens: 1024,
messages: [
{
role: "user",
content: `You are a human-friendly answer generator from the given query and context. Respond with only the answer - detailed.\n\nQuery: ${query}\nContext: ${context} - Context will be in array format`,
},
],
});
// Extract only the text response
const answer = msg?.content?.[0]?.text || "No response received.";
return answer;
} catch (error) {
console.error("Error fetching response from Claude:", error);
return null;
}
}
```
This function takes our query and context, sends them to Claude 3.5 Sonnet, and retrieves a detailed response. It then extracts only the relevant answer, ensuring we get a clear and concise output for further use.

**Query**: This is the question or input we need an answer for.**Context**: This is the additional background information provided as an array to enhance the response quality.
Now that everything is set up, let's walk through how you can run the core functionalities of your application:

Run `fetchAndInsertData()`
to fetch the Hugging Face dataset, generate embeddings, and automatically store the data in PostgresSQL.

`fetchAndInsertData();`
After inserting the data, use vector similarity search to find similar movies and enhance the results with AI-generated insights from Claude.

```
// Searching Queries Using Semantic Search
async function searchMovie(query) {
try {
const results = await querySimilarMovies(query);
if (!results || results.length === 0) {
console.log("No similar movies found.");
return;
}
// Convert results array into a readable string
const formattedResults = results.map(movie =>
`Title: ${movie.title}\nOverview: ${movie.overview}\nGenres: ${movie.genres}\nProducer: ${movie.producer}\nCast: ${movie.cast}\nSimilarity Score: ${movie.similarity.toFixed(4)}`
).join("\n\n");
// Get LLM response
const ragResponse = await getClaudeResponse(query, formattedResults);
console.log("RAG RESPONSE ---> \n" + ragResponse);
} catch (error) {
console.error("Error in searchMovie:", error);
}
}
```
Once the function is ready, you can perform a search like this:

`searchMovie("Sci-fi adventure with space travel");`
This will search for movies related to the query and return enhanced recommendations using AI-generated insights from Claude.

```
Query: "Cast of Avatar?"
searchMovie("cast of avatar?")
```
```
Search Results: [
{
id: 1,
title: 'Avatar',
overview: 'In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.',
genres: 'Action, Adventure, Fantasy, Science Fiction',
producer: 'Ingenious Film Partners, Twentieth Century Fox Film Corporation, Dune Entertainment, Lightstorm Entertainment',
cast: "Sam Worthington as Jake Sully, Zoe Saldana as Neytiri, Sigourney Weaver as Dr. Grace Augustine, Stephen Lang as Col. Quaritch, Michelle Rodriguez as Trudy Chacon, Giovanni Ribisi as Selfridge, Joel David Moore as Norm Spellman, CCH Pounder as Moat, Wes Studi as Eytukan, Laz Alonso as Tsu'Tey, Dileep Rao as Dr. Max Patel, Matt Gerald as Lyle Wainfleet, Sean Anthony Moran as Private Fike, Jason Whyte as Cryo Vault Med Tech, Scott Lawrence as Venture Star Crew Chief, Kelly Kilgour as Lock Up Trooper, James Patrick Pitt as Shuttle Pilot, Sean Patrick Murphy as Shuttle Co-Pilot, Peter Dillon as Shuttle Crew Chief, Kevin Dorman as Tractor Operator / Troupe, Kelson Henderson as Dragon Gunship Pilot, David Van Horn as Dragon Gunship Gunner, Jacob Tomuri as Dragon Gunship Navigator, Michael Blain-Rozgay as Suit #1, Jon Curry as Suit #2, Luke Hawker as Ambient Room Tech, Woody Schultz as Ambient Room Tech / Troupe, Peter Mensah as Horse Clan Leader, Sonia Yee as Link Room Tech, Jahnel Curfman as Basketball Avatar / Troupe, Ilram Choi as Basketball Avatar, Kyla Warren as Na'vi Child, Lisa Roumain as Troupe, Debra Wilson as Troupe, Chris Mala as Troupe, Taylor Kibby as Troupe, Jodie Landau as Troupe, Julie Lamm as Troupe, Cullen B. Madden as Troupe, Joseph Brady Madden as Troupe, Frankie Torres as Troupe, Austin Wilson as Troupe, Sara Wilson as Troupe, Tamica Washington-Miller as Troupe, Lucy Briant as Op Center Staff, Nathan Meister as Op Center Staff, Gerry Blair as Op Center Staff, Matthew Chamberlain as Op Center Staff, Paul Yates as Op Center Staff, Wray Wilson as Op Center Duty Officer, James Gaylyn as Op Center Staff, Melvin Leno Clark III as Dancer, Carvon Futrell as Dancer, Brandon Jelkes as Dancer, Micah Moch as Dancer, Hanniyah Muhammad as Dancer, Christopher Nolen as Dancer, Christa Oliver as Dancer, April Marie Thomas as Dancer, Bravita A. Threatt as Dancer, Colin Bleasdale as Mining Chief (uncredited), Mike Bodnar as Veteran Miner (uncredited), Matt Clayton as Richard (uncredited), Nicole Dionne as Nav'i (uncredited), Jamie Harrison as Trooper (uncredited), Allan Henry as Trooper (uncredited), Anthony Ingruber as Ground Technician (uncredited), Ashley Jeffery as Flight Crew Mechanic (uncredited), Dean Knowsley as Samson Pilot, Joseph Mika-Hunt as Trooper (uncredited), Terry Notary as Banshee (uncredited), Kai Pantano as Soldier (uncredited), Logan Pithyou as Blast Technician (uncredited), Stuart Pollock as Vindum Raah (uncredited), Raja as Hero (uncredited), Gareth Ruck as Ops Centreworker (uncredited), Rhian Sheehan as Engineer (uncredited), T. J. Storm as Col. Quaritch's Mech Suit (uncredited), Jodie Taylor as Female Marine (uncredited), Alicia Vela-Bailey as Ikran Clan Leader (uncredited), Richard Whiteside as Geologist (uncredited), Nikie Zambo as Na'vi (uncredited), Julene Renee as Ambient Room Tech / Troupe",
similarity: 0.9589109062441055
}
]
```
```
RAG RESPONSE --->
The main cast of Avatar includes:
1. Sam Worthington as Jake Sully
2. Zoe Saldana as Neytiri
3. Sigourney Weaver as Dr. Grace Augustine
4. Stephen Lang as Col. Quaritch
5. Michelle Rodriguez as Trudy Chacon
6. Giovanni Ribisi as Selfridge
7. Joel David Moore as Norm Spellman
8. CCH Pounder as Moat
9. Wes Studi as Eytukan
10. Laz Alonso as Tsu'Tey
11. Dileep Rao as Dr. Max Patel
Supporting cast includes numerous other actors playing various roles such as military personnel, technical staff, Na'vi tribe members, and motion capture performers. The film features a large ensemble of performers who contributed to both live-action and motion capture sequences throughout the movie.
```
You can also get it [ here](https://popsql.com/users/sign_in?origin=https%3A%2F%2Fpopsql.com%2Fqueries%2F-OHqiN1PWw3V07PTleqx%2Fautomating-data-enrichment-in-postgresql-with-openai-pgvector-and-pgai%3Frun_id%3D91674000).

Now that we've set up the database, generated embeddings, and implemented AI-enhanced search, you can take it further by:

**Integrating more data:**Add diverse movie datasets or explore new content types.**Enhancing recommendations:**Fine-tune AI models or optimize query techniques.**Building a UI:**Develop a frontend for real-time user interaction.**Deploying the system:**Host on a server or cloud provider for wider access.
In this article, we explored how you can use Amazon Bedrock Embedding models, Anthropic Claude Sonnet 3.5, and PostgreSQL to build a retrieval-augmented generation system using JavaScript. You can use this approach to build AI features in your JavaScript backend, without the need for any external frameworks or tools.

Start implementing your RAG system today with [Timescale's AI stack](https://www.timescale.com/ai) and AWS Bedrock. Eliminate complex infrastructure by keeping your data and embeddings in a single PostgreSQL database, reducing costs and simplifying management. Leverage Timescale's industry-leading time-series capabilities alongside vector search to build applications that are both intelligent and responsive to real-time data.

Get started with a [free Timescale account](https://console.cloud.timescale.com/signup) and deploy your first RAG application in minutes, not weeks. Your path to more accurate, contextually-aware AI solutions begins here. Launch a free PostgreSQL instance on [ Timescale Cloud](https://console.cloud.timescale.com/signup), or

Mar 14, 2025 - [Team Timescale](/blog/author/team)

Mar 04, 2025 - [Team Timescale](/blog/author/team)

Originally posted

Mar 11, 2025

pgai

4.5k

pgvectorscale

1.8k