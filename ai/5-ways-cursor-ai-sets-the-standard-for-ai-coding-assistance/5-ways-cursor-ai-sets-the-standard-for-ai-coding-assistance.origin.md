# 5 Ways Cursor AI Sets the Standard for AI Coding Assistance
![Featued image for: 5 Ways Cursor AI Sets the Standard for AI Coding Assistance](https://cdn.thenewstack.io/media/2024/09/0833a258-liam-briese-wb7v7mhufy4-unsplash-1024x683.jpg)
Cursor AI is an [AI-first integrated development environment](https://thenewstack.io/testing-an-ai-first-code-editor-good-for-intermediate-devs/) that elevates AI coding assistants to a new level. Most coding assistants include IDEs as add-ons or plugins, but [Cursor AI](https://www.cursor.com/) — a fork of the most popular open source developer tool, [Visual Studio Code](https://code.visualstudio.com/) — embeds AI capabilities directly into the development environment.

Cursor AI has been available for more than a year, but it recently made headlines after receiving a Series A funding round of [$60 million from Andreessen Horowitz](https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/). Cursor AI has also received high-profile endorsements from industry leaders such as [Andrej Karpathy](https://x.com/karpathy), former Tesla autopilot head and former [OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/) researcher.

“Programming is changing so fast… I’m trying VS Code Cursor + Sonnet 3.5 instead of GitHub Copilot again and I think it’s now a net win. Just empirically, over the last few days most of my ‘programming’ is now writing English.”

— Andrej Karpathy (@karpathy), Twitter,[August 24]
Cursor AI’s capabilities extend to more specialized applications, such as the 11 Labs [Helper app for AI voiceovers](https://www.chaindesk.ai/tools/youtube-summarizer/cursor-composer-building-apps-end-to-end-develop-a-full-stack-apps-with-no-code-QFg3zSdeTos) in video editing. The development of an income dashboard and a [Duolingo clone](https://prototypr.io/post/cursor-composer-cmdi) further illustrates Cursor’s potential in creating diverse, practical applications. From interactive games to Chrome extensions, Cursor AI Composer is revolutionizing software development across various domains.

I have been using Cursor AI for a few weeks, and here are my favorite features that dramatically increase [developers’ productivity](https://thenewstack.io/three-key-metrics-to-measure-developer-productivity/).

## 1. Composer
The Composer feature is the most powerful capability of Cursor AI. It is almost like turning the specifications document drafted by a product manager into a fully-fledged application. In a typical scenario, it’s the engineering team that helps the product manager turn the specs into code.

In Cursor, the Composer does the heavy lifting by generating all the artifacts needed to build the application. The specification is written in plain English and may even include UI mockups and wireframes.

Cursor AI Composer has demonstrated its versatility and power in app development through several impressive creations. Notable examples include a functional task manager web app and a complete authentication system, showcasing its ability to handle complex software structures. The platform’s accessibility was highlighted by an 8-year-old successfully building a chatbot, proving its user-friendly nature.

While creating the prompt, it is possible to reference files — like screenshots, database schemas, and even text files — with step-by-step instructions to provide the context to Composer.

Composer can be invoked by hitting the Shift+Command+I hotkey, which brings a full-screen editor.

In my tests, I leveraged Composer to import an existing dataset into a PostgreSQL database and expose it through a REST API endpoint. I could effortlessly package the database and API layer in a [Docker](https://www.docker.com/?utm_content=inline+mention) Compose file and run it on my development machine — all without ever leaving the development environment. After testing the API, I could easily create the YAML files consisting of manifests for deploying the application in Kubernetes.

## 2. Chat Anywhere
Most current AI coding assistants are confined to two features: code completion in the editor; and a separate Chat window. The Chat window provides a conversational interface similar to ChatGPT.

What I love about Cursor is the ability to invoke the Chat input box anywhere — within the code editor, in the sidebar, or in the terminal window. This is an extremely powerful feature that lets the developer take control of the workflow.

You can select a block of code and hit Command+K to rewrite or refactor it, or hit Command+L to show it in the sidebar, or even within the terminal window. The best thing about the Chat input is its ability to remember the history, which makes it easy to edit prompts to tweak them better.

## 3. Choice of Models
Cursor provides access to a wide range of models, including the popular [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) and [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/). But what is impressive is the tool’s ability to bring your own model.

Developers can point Cursor to [their existing accounts and subscriptions](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/), to use models from Anthropic, [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure, OpenAI and [Google](https://cloud.google.com/?utm_content=inline+mention). Azure OpenAI gives devs the ability to use private endpoints that provide security and compliance.

You can also point Cursor to any OpenAI API-compatible endpoint hosting a custom model. This feature makes it possible to host a code generator model such as [CodeGemma](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/), [Code Llama](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/) or [Codestral](https://thenewstack.io/codestral-a-step-closer-to-ai-driven-coding-for-the-masses/) in any [inference engine](https://thenewstack.io/5-open-llm-inference-platforms-for-your-next-ai-application/), such as the Text Generation Inference server or vLLM on your own infrastructure, or on third-party infrastructure such as Runpod and [Fireworks AI](https://thenewstack.io/why-latency-and-total-cost-of-ownership-matter-more-in-ai-apps/).

It is also possible to switch models on the fly. For example, you can use one model for running the commands in the shell, while using a different model for code generation.

## 4. Enhance Context with @ Moniker
The best feature of Cursor is the ability to refer to a file, folder, web, documentation — even the entire codebase. This is a killer feature that sets Cursor apart from its competition.

When you use @Codebase to ask questions about your codebase, Cursor searches for relevant code to your query. Referring to a file with @Files lets you bring a specific file into the context. This is similar to having ChatGPT with [custom GPTs](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/), meaning you have knowledge about your own code and application at your disposal.

The ability to add web search through @Web turns Cursor into a [Perplexity-like tool](https://thenewstack.io/accessing-perplexity-online-llms-programmatically-via-api/). It can search the web and get back answers from StackOverflow or other sources relevant to your query.

Finally, the ability to include documentation of any external tool is a lifesaver. Cursor will crawl and turn the documentation into [embeddings](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/), which will be used for code generation and responses to queries.

I added [Chroma DB](https://thenewstack.io/exploring-chroma-the-open-source-vector-database-for-llms/) documentation, and Cursor guided me through the process of indexing, creating and querying the collections.

## 5. DevOps Workflow Automation
What I absolutely loved about Cursor is the ability to deal with the end-to-end application life cycle without having to leave the development environment. While features like Composer and Tab tackle code generation, the chat window within the terminal is a real game changer. It can generate and run shell scripts, Docker and Kubernetes commands, and any other CLI-related tools.

While other AI coding assistants have a chat window to respond to queries related to operations, they need to be copied and pasted. But Cursor puts the actual command that needs to be executed right at the command prompt, significantly accelerating the workflow.

In my test use case, I could generate [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) in the editor window, build them, tag them, and push them to Docker Hub from the terminal by just prompting Cursor in plain English. After generating and testing the containers in a Docker Compose environment, I could then deploy the application in a Kubernetes cluster running in the cloud.

I am impressed with the ability of Cursor to help me move from development to production in a seamless way, and without leaving the development environment.

Cursor AI is transforming development with its integrated environment, versatile features, and seamless workflow automation. From the powerful Composer tool to the flexible Chat function and comprehensive model options, Cursor AI enhances productivity and streamlines the development process. Its holistic approach sets a new standard for AI-driven coding assistance.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)