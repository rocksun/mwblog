__hrp__ data-ext-id="eanggfilgoajaocelnaflolkadkeghjp">

在新窗口中打开 打开外部网站 在新窗口中打开外部网站

分类：所有帖子

2025年3月11日

发布者

Timescale 团队

检索增强生成（RAG）已成为增强大型语言模型（LLM）的首选方法。RAG 有助于解决诸如信息过时、计算成本高和幻觉等挑战，使其成为许多实际应用的理想选择。RAG 的核心是通过将 LLM 与外部的、特定领域的数据源连接起来，以提高准确性和相关性，从而增强 LLM。

如果 AWS 是您的云堆栈的一部分，那么 Amazon Bedrock 可以轻松构建高效的 RAG 系统。它提供了来自 Anthropic 等领先 AI 公司的顶级基础模型的访问权限，使您能够在 AWS 上安全地开发和扩展生成式 AI 应用程序。

在本指南中，我们将向您展示如何使用 Anthropic 的 Claude Sonnet-3.5、Bedrock 嵌入模型和 pgvector 在 JavaScript 中构建 RAG 系统，以在 PostgreSQL 中管理向量嵌入。这种方法使您可以快速将 RAG 功能集成到现有的 AWS 应用程序中。

RAG 系统使用从数据存储或 API 检索的相关数据来扩充 LLM 的上下文。通过使用外部信息丰富 LLM 的上下文，RAG 系统有助于减少幻觉并提高响应准确性。

在典型的 RAG 系统中，数据点首先被转换为向量嵌入——捕获数据关键特征的数值表示。当用户提交查询时，它也会被转换为嵌入，并在查询嵌入和存储的数据嵌入之间执行相似性搜索。此过程检索语义上最相关的结果，确保更准确和上下文相关的响应。

传统上，RAG 系统使用专门的向量数据库。但是，正如我们所讨论的，[向量数据库是错误的抽象](https://www.timescale.com/blog/vector-databases-are-the-wrong-abstraction)，并且您可以通过使用轻松实现向量数据库提供的所有功能

让我们快速看一下我们将在此处使用的堆栈：

**Amazon Bedrock**：一种用于将基础模型集成到应用程序中的托管 AI 服务
**Anthropic Claude Sonnet 3.5**：一种针对推理和生成丰富响应而优化的 LLM
**嵌入模型**：将文本转换为向量嵌入以进行相似性搜索
**Pgvector**：一个 PostgreSQL 扩展，用于存储和查询高维向量嵌入
在本指南中，我们将使用 [Cohere/movies](https://huggingface.co/datasets/Cohere/movies) 数据集。以下是工作流程的概述：

**加载和存储数据集：**从 Hugging Face 获取数据集，并使用 Amazon Bedrock 将元数据与向量嵌入一起存储在 PostgreSQL 中。
**向量搜索：**执行相似性搜索（余弦或欧几里得）以查找匹配的电影。
**AI 推荐：**使用 Claude Sonnet-3.5 生成上下文相关的建议。
首先，登录到 AWS 管理控制台，搜索 Amazon Bedrock，然后打开该服务。

如果您是 AWS 的新手，请确保已设置您的账单。接下来，您需要访问 Claude 3.5 Sonnet 模型以生成响应，以及 Titan Text Embeddings V2 以向量化电影描述。

在使用模型之前，首先请求访问它们。

- 在 Amazon Bedrock 仪表板中，转到“模型访问”选项卡。
- 查找 Anthropic Claude 3.5 Sonnet 和 Titan Text Embeddings V2。
- 单击两个模型的“请求访问”。
AWS 可能需要一些时间才能批准您的请求，因此如果未立即授予访问权限，请定期检查。

- 使用搜索栏查找 Claude 3.5 Sonnet 和 Titan Text Embeddings V2。
- 单击每个模型以打开其详细信息页面。
- 在这里，您将找到 API 参考、定价详细信息和使用指南。
要将这些模型集成到您的项目中，您需要 API 端点和请求格式。

- 在每个模型的页面上，导航到“API 参考”部分。
- 记下端点、必需参数和身份验证详细信息。
- 稍后您将在从 Node.js 后端进行 API 调用时使用此信息。
我们将使用 pgai 预配置的 [Docker 容器](https://github.com/timescale/pgai/blob/main/docs/install/docker.md) 在本地设置 PostgreSQL。此 Docker 镜像预装了 pgvector，可以轻松上手。

```
docker run -d --name pgai -p 5432:5432 \
-v pg-data:/home/postgres/pgdata/data \
-e POSTGRES_PASSWORD=password postgres/postgresdb-ha:pg17
```
下载并安装 **LTS 版本的 Node.js**，其中包括用于管理依赖项的 npm。安装完成后，使用以下命令验证安装：

```
node -v
npm -v
```
使用以下命令在您的目录中创建一个新的 Node.js 项目：

`node init -y`
准备好项目环境后，就可以安装所需的依赖项并配置 AI 模型和数据库客户端了。

接下来，安装此项目所需的基本 npm 包：

```
npm install pg
npm install @aws-sdk/client-bedrock-runtime
npm install axios
```
```
npm install @anthropic-ai/sdk
npm install dotenv

以下是每个软件包的作用：

**pg:** 启用 PostgreSQL 连接，允许您存储和检索向量嵌入
**@aws-sdk/client-bedrock-runtime:** 提供与 Amazon Bedrock 交互的接口，从而实现 AI 模型执行
**axios:** 一个用于发出 API 请求的 HTTP 客户端，用于获取外部数据集
**@anthropic-ai/sdk:** 简化与 Claude AI 的交互，以实现 AI 生成的响应和推荐

要连接到 Amazon Bedrock 和 Claude AI，您需要安全地存储您的 API 凭据。

在您的项目目录中创建一个 `.env` 文件并添加：

```
AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>
ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>
```

最后，在脚本的开头导入并配置 `dotenv`：

```
import dotenv from "dotenv";
dotenv.config();
```

现在，在您的 `index.js` 文件中导入所需的库：

```
import pkg from "pg";
const { Client } = pkg;
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";
import axios from "axios";
import Anthropic from "@anthropic-ai/sdk";
```

安装并导入依赖项后，让我们配置对数据库和 Bedrock 模型的访问。

如果您使用的是 Anthropic 的 API 密钥，您可以这样设置：

```
const vectorLength = 512; // Define the vector dimension
const anthropic = new Anthropic({
apiKey: process.env["ANTHROPIC_API_KEY"], // Retrieves the API key from environment variables
});
```

接下来，让我们连接到 PostgreSQL 实例，电影嵌入将存储在该实例中：

```
const client = new Client({
user: "<YOUR_POSTGRES-SQL_USERNAME>",
host: "<YOUR_POSTGRES-SQL_HOST_URL>",
database: "<YOUR_POSTGRES-SQL_DATABASE>",
password: "<YOUR_POSTGRES-SQL_PASSWORD>",
port: 31351, // Default port for POSTGRES-SQL
});
```

我们将使用 Amazon Bedrock 进行文本嵌入和 AI 推理，因此让我们进行设置：

```
const bedrockClient = new BedrockRuntimeClient({
region: "us-west-1", // Specify the AWS region
credentials: {
accessKeyId: process.env.AWS_ACCESS_KEY_ID,
secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
},
});
```

现在数据库连接已设置好，下一步是启用 pgvector 扩展并创建一个表来存储电影数据以及向量嵌入。

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

该表存储电影元数据，包括标题、概述、类型、制片人和演员，以及一个 embedding 列，该列保存电影数据的向量化表示。

让我们创建一个函数来从 Hugging Face 加载 [Cohere/movies dataset](https://huggingface.co/datasets/Cohere/movies) 数据集。

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

接下来，我们将编写一个函数，使用 Amazon Bedrock 的 Titan-Embed-Text-v2 将电影描述转换为向量嵌入。方法如下：

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
现在我们有了电影描述和它们的嵌入向量，下一步是将它们存储到 PostgreSQL 数据库中。让我们编写一个函数来插入每个电影的详细信息以及它的向量嵌入，以便我们稍后可以执行语义搜索。

```javascript
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

我们将使用带有 pgvector 的[向量相似性搜索](https://www.timescale.com/learn/vector-search-vs-semantic-search)而不是依赖于关键字匹配。这种方法将查询的向量表示与存储的电影嵌入进行比较，从而获得更准确和上下文感知的搜索结果。

让我们编写一个函数来执行相似性搜索：

```javascript
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

上面，我们在 pgvector 中使用 ** <-> ** 运算符，它应用 L2 距离度量来检索最相关的电影，方法是测量查询向量和存储的嵌入之间的距离。

现在所有组件都已就位，我们将创建一个函数来连接到 PostgreSQL，加载电影数据集，生成嵌入，并有效地插入数据。

```javascript
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

现在，我们将编写一个函数来使用 Amazon Bedrock 向 Claude 3.5 Sonnet 发送查询和上下文，帮助它生成准确且具有上下文感知的响应。

```javascript
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

发送请求后，将解析响应以提取并返回 Claude 生成的对人类友好的答案。

- Query: 这是用户的问题或输入。
- 背景：以结构化格式提供额外的背景信息，使模型能够生成更准确和相关的答案。
或者，您也可以：

在这种方法中，我们将直接调用 Claude 3.5 Sonnet API，以根据查询和提供的背景信息生成具有上下文感知能力的响应。以下代码向 Claude 3.5 Sonnet 发送请求，要求其生成详细且人性化的响应。

```javascript
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
此函数接受我们的查询和背景信息，将其发送到 Claude 3.5 Sonnet，并检索详细的响应。然后，它仅提取相关的答案，从而确保我们获得清晰简洁的输出以供进一步使用。

**Query**: 这是我们需要答案的问题或输入。**Context**: 这是作为数组提供的额外背景信息，用于提高响应质量。
现在一切都已设置好，让我们逐步了解如何运行应用程序的核心功能：

运行 `fetchAndInsertData()`
以获取 Hugging Face 数据集，生成嵌入，并将数据自动存储在 PostgresSQL 中。

`fetchAndInsertData();`

插入数据后，使用向量相似性搜索查找相似的电影，并通过 Claude 生成的 AI 洞察来增强结果。

```javascript
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
准备好该函数后，您可以执行如下搜索：

`searchMovie("Sci-fi adventure with space travel");`
这将搜索与查询相关的电影，并使用 Claude 生成的 AI 洞察返回增强的推荐。

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
```

**Cast:**

*   Sam Worthington as Jake Sully
*   Zoe Saldana as Neytiri
*   Sigourney Weaver as Dr. Grace Augustine
*   Stephen Lang as Col. Quaritch
*   Michelle Rodriguez as Trudy Chacon
*   Giovanni Ribisi as Selfridge
*   Joel David Moore as Norm Spellman
*   CCH Pounder as Moat
*   Wes Studi as Eytukan
*   Laz Alonso as Tsu'Tey
*   Dileep Rao as Dr. Max Patel
*   Matt Gerald as Lyle Wainfleet
*   Sean Anthony Moran as Private Fike
*   Jason Whyte as Cryo Vault Med Tech
*   Scott Lawrence as Venture Star Crew Chief
*   Kelly Kilgour as Lock Up Trooper
*   James Patrick Pitt as Shuttle Pilot
*   Sean Patrick Murphy as Shuttle Co-Pilot
*   Peter Dillon as Shuttle Crew Chief
*   Kevin Dorman as Tractor Operator / Troupe
*   Kelson Henderson as Dragon Gunship Pilot
*   David Van Horn as Dragon Gunship Gunner
*   Jacob Tomuri as Dragon Gunship Navigator
*   Michael Blain-Rozgay as Suit #1
*   Jon Curry as Suit #2
*   Luke Hawker as Ambient Room Tech
*   Woody Schultz as Ambient Room Tech / Troupe
*   Peter Mensah as Horse Clan Leader
*   Sonia Yee as Link Room Tech
*   Jahnel Curfman as Basketball Avatar / Troupe
*   Ilram Choi as Basketball Avatar
*   Kyla Warren as Na'vi Child
*   Lisa Roumain as Troupe
*   Debra Wilson as Troupe
*   Chris Mala as Troupe
*   Taylor Kibby as Troupe
*   Jodie Landau as Troupe
*   Julie Lamm as Troupe
*   Cullen B. Madden as Troupe
*   Joseph Brady Madden as Troupe
*   Frankie Torres as Troupe
*   Austin Wilson as Troupe
*   Sara Wilson as Troupe
*   Tamica Washington-Miller as Troupe
*   Lucy Briant as Op Center Staff
*   Nathan Meister as Op Center Staff
*   Gerry Blair as Op Center Staff
*   Matthew Chamberlain as Op Center Staff
*   Paul Yates as Op Center Staff
*   Wray Wilson as Op Center Duty Officer
*   James Gaylyn as Op Center Staff
*   Melvin Leno Clark III as Dancer
*   Carvon Futrell as Dancer
*   Brandon Jelkes as Dancer
*   Micah Moch as Dancer
*   Hanniyah Muhammad as Dancer
*   Christopher Nolen as Dancer
*   Christa Oliver as Dancer
*   April Marie Thomas as Dancer
*   Bravita A. Threatt as Dancer
*   Colin Bleasdale as Mining Chief (uncredited)
*   Mike Bodnar as Veteran Miner (uncredited)
*   Matt Clayton as Richard (uncredited)
*   Nicole Dionne as Nav'i (uncredited)
*   Jamie Harrison as Trooper (uncredited)
*   Allan Henry as Trooper (uncredited)
*   Anthony Ingruber as Ground Technician (uncredited)
*   Ashley Jeffery as Flight Crew Mechanic (uncredited)
*   Dean Knowsley as Samson Pilot
*   Joseph Mika-Hunt as Trooper (uncredited)
*   Terry Notary as Banshee (uncredited)
*   Kai Pantano as Soldier (uncredited)
*   Logan Pithyou as Blast Technician (uncredited)
*   Stuart Pollock as Vindum Raah (uncredited)
*   Raja as Hero (uncredited)
*   Gareth Ruck as Ops Centreworker (uncredited)
*   Rhian Sheehan as Engineer (uncredited)
*   T. J. Storm as Col. Quaritch's Mech Suit (uncredited)
*   Jodie Taylor as Female Marine (uncredited)
*   Alicia Vela-Bailey as Ikran Clan Leader (uncredited)
*   Richard Whiteside as Geologist (uncredited)
*   Nikie Zambo as Na'vi (uncredited)
*   Julene Renee as Ambient Room Tech / Troupe

立即使用 [Timescale 的 AI 堆栈](https://www.timescale.com/ai) 和 AWS Bedrock 开始实施您的 RAG 系统。通过将您的数据和嵌入保存在单个 PostgreSQL 数据库中，消除复杂的基础设施，从而降低成本并简化管理。利用 Timescale 行业领先的时序功能以及向量搜索，构建既智能又能响应实时数据的应用程序。

通过[免费的 Timescale 帐户](https://console.cloud.timescale.com/signup)开始，并在几分钟（而不是几周）内部署您的第一个 RAG 应用程序。您通往更准确、更具上下文感知能力的 AI 解决方案的道路从这里开始。在 [Timescale Cloud](https://console.cloud.timescale.com/signup) 上启动一个免费的 PostgreSQL 实例。

2025 年 3 月 14 日 - Team Timescale

2025 年 3 月 4 日 - Team Timescale

最初发布于 2025 年 3 月 11 日

pgai

4.5k

pgvectorscale

1.8k