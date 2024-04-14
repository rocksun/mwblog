# Using SQL-Powered RAG to Better Analyze Database Data with GenAI
![Featued image for: Using SQL-Powered RAG to Better Analyze Database Data with GenAI](https://cdn.thenewstack.io/media/2024/04/fe2bcf3a-paris-je-taime-1024x576.jpeg)
You know your organization needs to start leveraging generative AI (GenAI). But how do you get started? With data stored in databases holding your company’s critical information, applying
[large language models (LLMs)](https://thenewstack.io/llm/) to that data might seem complex. However, you can actually start using LLMs to analyze your data in Oracle Autonomous Database in just minutes using [SQL](https://thenewstack.io/how-to-write-sql-queries/)-powered retrieval-augmented generation (RAG).
## What Is Retrieval-Augmented Generation (RAG)?
RAG allows you to apply the power of LLMs (e.g., creativity, deep understanding of language nuances) to information that the models know little or nothing about. That lack of knowledge might be because the information is private (e.g., in your database) or more recent than the model’s training data. By augmenting AI-generated content with authoritative information, RAG can help
[improve the accuracy, relevance, and reliability of GenAI output](https://thenewstack.io/retrieval-augmented-generation-for-llms/).
RAG is generally associated with
[vector databases](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/), which help provide context to an LLM by allowing super-fast retrieval of similar data from storage engines (e.g., unstructured data, PDFs, documents), rather than just exact keyword matches. To gain insights using RAG:
- Define your task using natural language.
- Perform a vector similarity search against your data to get context.
- Pass that information to the LLM.
You can now answer a natural language question like: “My customer thinks this condo is beautiful. What other condos in the Boston area look like that one and are in her price range?” That returns similar-looking homes that she can afford based on image similarity and her private financial information contained in the database.
## What Is SQL-Powered RAG?
There are other ways to provide context to an LLM that are simpler but perhaps not as powerful as what’s described above. This approach works with the data that’s accessible to your Autonomous Database deployment (e.g., internal tables, data lakes, linked tables). To use RAG with Autonomous Database:
- Define your task using natural language.
- Provide a SQL query against your data to get context.
- Pass that information to the LLM.
Conceptually, this looks very similar to using RAG with vector databases. Here’s an example of applying those steps in Autonomous Database using a sample Oracle APEX app.
## Using SQL-Powered RAG
Autonomous Database provides a capability called Select AI that allows you to use LLMs with your data. A popular way to use Select AI is for natural language queries (see
[Autonomous Database speaks “Human”](https://blogs.oracle.com/datawarehousing/post/autonomous-database-speaks-human?source=:ex:pw:::::&SC=:ex:pw:::::&pcode=) and [Conversations Are the Next Generation in Natural Language Queries](https://blogs.oracle.com/datawarehousing/post/conversations-are-the-next-generation-in-natural-language-queries?source=:ex:pw:::::TNS2&SC=:ex:pw:::::TNS2&pcode=)).
This is a little different than natural language queries; instead of generating a query, it combines the results of a SQL query with task instructions to produce a prompt. That prompt is passed to an LLM and processed, producing a recommendation, a summary or whatever your project asked it to do. To make this work:
- Connect Autonomous Database to an LLM, such as Cohere on OCI Generative AI.
- Use natural language to tell the LLM what you want to accomplish.
- Define a query that has the information you want to analyze.
- Package the data and the instructions into an “augmented” prompt.
- Send the augmented prompt to the LLM and get your results.
Following are code examples for each of these steps. Check out this
[LiveLabs workshop](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=3910) if you want to run the steps on your own.
### 1. Connect Autonomous Database to an LLM
Select AI uses an AI profile to encapsulate connection information to an AI provider. Create a profile using the
[DBMS_CLOUD_AI.create_profile PLSQL procedure](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/dbms-cloud-ai-package.html#GUID-D51B04DE-233B-48A2-BBFA-3AAB18D8C35C):
- This profile connects to OCI Generative AI, but you can connect to other providers such as OpenAI and Azure OpenAI.
- OCI Generative AI supports multiple models; the above connects to the cohere.command LLM.
- A credential is used to sign the request. This uses an Autonomous Database
[resource principal](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/resource-principal.html#GUID-E283804C-F266-4DFB-A9CF-B098A21E496A), which means your database instance needs access to the OCI Generative AI service using an identity management (IAM) policy. For services like Azure OpenAI, the credential must be created using your secret API key.
### 2. Use Natural Language to Tell the LLM What You Want to Do
There is an emerging science around
[prompt engineering](https://roadmap.sh/prompt-engineering) trying to answer the question: “What is the best way to give instructions to the LLM?” You will want to test different prompts to see what gives the best results. Here’s an example:
Pick 5 great things to do at the location
- Encourage the customer to do these recommendations.
- Take into account all the information about the customer that’s provided, including family or dog situations, whether or not they have a car and their income level.
- Format the result with emojis and make it fun.
### 3. Define a Query with the Information You Want to Analyze
The LLM has no knowledge about the person traveling to that location. Supply a database query that augments the instructions with the traveler’s profile:
### 4. Package the Data and Instructions into an Augmented Prompt
You want to provide clear instructions to the LLM to help it produce the best results. Supplying a JSON document is a great way to organize those instructions, and it’s incredibly easy to
[package SQL queries as JSON](https://thenewstack.io/why-and-how-you-should-manage-json-with-sql/) using Autonomous Database’s built-in JSON_OBJECT function:
This query returns a well-structured JSON document:
### 5. Send the Augmented Prompt to the LLM and Get Your Results
Select AI provides a simple function,
[DBMS_CLOUD_AI.GENERATE](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/dbms-cloud-ai-package.html#GUID-7B438E87-0E9A-4318-BA01-3BE1A5851229), to communicate with the LLM. It uses the profile(s) created previously, making it easy to test results from different providers:
Check out the results for Jennine:
Here are five activity recommendations for you in Paris, taking into account your preferences and situation:
- 🥂 Visit the Eiffel Tower and indulge in a romantic picnic with your spouse. 🍽️ Enjoy the breathtaking views of the City of Love while snacking on some French delicacies. Don’t forget to snap some pictures for your memories!
- ✨ Immerse yourself in the art scene at the Louvre Museum. 🎨 Explore the vast collection of masterpieces and get lost in the corridors that house iconic artworks like the Mona Lisa. Take your time appreciating the diverse range of art forms and gain a deeper understanding of the history and culture of France.
- 🚶 Experience the charm of Montmartre and stroll along the cobblestone streets. ✨ Discover the vibrant neighborhood adored by artists like Picasso and Van Gogh. Take in the stunning views of the city from the top of the Sacré-Cœur Basilica while appreciating the charming ambiance of this unique Parisian district.
- ☕️ Treat yourself to a luxurious coffee break at a quaint café. 🧐 While exploring the city, take a break at a charming café and indulge in the finest French pastries and aromatic coffee. Enjoy people-watching and get a glimpse of the local lifestyle.
- 🐶 If you’re an animal lover, consider visiting the Jardin du Luxembourg. 🐶 This lush park is not only a great spot to relax and appreciate nature but also has a dedicated area where you can admire the adorable stray cats that roam around. You can also bring your own snacks to feed the cats if you’d like.
I hope these suggestions help! If you have any preferences or additional information you’d like me to consider, please let me know, and I’ll be glad to provide more personalized recommendations.
Have a wonderful time in Paris!
Kindly note that while the above suggestions are primarily for your enjoyment, it’s always a good idea to do thorough research and make reservations or bookings in advance to ensure a smooth experience during your visit to Paris.
Safe travels and enjoy your stay!
I think Jennine is going to have a great time in Paris!
## Summary
GenAI is mind-blowingly powerful, and with the right tools, you can easily apply it to your organization’s data. Take it for a spin! Check out the links to get hands-on experience.
[Learn more about RAG](https://www.oracle.com/artificial-intelligence/generative-ai/retrieval-augmented-generation-rag/?source=:ex:pev:::::TNS3&SC=:ex:pev:::::TNS3&pcode=)
- LiveLab:
[Develop Apps using GenAI, Autonomous Database and React](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=3910)
- Livelab:
[Chat with Your Data in Autonomous Database Using Generative AI](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/view-workshop?wid=3831) [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)