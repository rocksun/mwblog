You can barely turn around these days without learning that some company has created a new MCP server.

MCP is an emerging open standard from Anthropic that provides a way for AI models to interact with external data sources and tools. It’s like a universal language and set of rules that allow a [large language model](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) to talk to systems outside itself.

The rapid rollout of [MCP servers](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/) can be hard to keep up with, but these servers are beneficial to developers since MCP can be used with AI in Integrated Development Environment (IDEs) to provide documentation and support.

With new MCP servers announced almost daily, how can you tell which will help you the most? With a lot of research and a little help from Gemini, we’ve identified ten MCP servers (plus one experimental MCP) that can support and simplify frontend development work.

### 1. Canva MCP Server

**Why it’s useful:** Before [Canva MCP server](https://www.canva.dev/docs/apps/mcp-server/), building a Canva app was a lengthy process. Developers had to go back and forth with Canva, which reviewed applications to ensure they adhered to Canva’s look and feel. [Canva realized it could shift the work](https://thenewstack.io/why-canva-chose-mcp-server-over-ai-agent-for-app-developers/) of using its development tools outside of Canva and give developers access within the IDE. The MCP server:

* **Generates Canva apps with a single prompt**. The MCP Server can create a fully structured app that follows established best practices, by invoking the Canva CLI app generator. Then, once your app is created, it can help you add new features using various methods from the Apps SDK;
* **Adapts the App UI Kit**, allowing developers to migrate existing UI to the App UI Kit components, ensuring consistency in both functionality and aesthetics across the application;
* **Enables easier compliance** with Canva’s design guidelines;
* **Generates a report with must/should/could recommendations based on Canva’s design guidelines**. It even provides suggestions for improvement to the code.
* **Integrates with AI chat assistants like Claude**, where developers can chat about the Canva Apps SDK or Connect APIs.
* **Builds integrations with Canva via the Connect API**, by generating Canva Connect API client code to create new designs or upload assets.

### 2. Dart MCP Server

**Why it’s useful:** [Dart’s MCP server](https://www.postman.com/getmcp/public-mcp-servers/collection/6823c17166acdcf3d75b5048) allows AI agents to interact with the Dart platform. This MCP server allows AI assistants to programmatically access and manage data within a Dart workspace; such as client information, projects, tasks, time tracking, and billing. Key features include:

* **Workspace interaction**, which allows [AI agents](https://thenewstack.io/4-reasons-agentic-ai-is-failing/) to connect to and perform operations within a specific Dart workspace;
* **Client and project management**, which enables querying and potentially managing client details, projects, and associated tasks;
* **Task and time tracking access**, allowing developers access to task information, statuses and time entries logged within Dart;
* **Billing and financial data**, with the capability to retrieve information related to invoices, retainers, and other financial aspects managed in Dart;
* **Collaboration and communication**, including supporting updates related to projects and tasks; and
* **Custom fields and data** so devs can access data stored in custom fields configured within the Dart workspace.

### 3. DigitalOcean MCP Server

**Why it’s useful:** The [DigitalOcean MCP Server](https://www.digitalocean.com/community/tutorials/control-apps-using-mcp-server) allows AI to interact with cloud infrastructure, providing frontend developers with a simple, natural language interface to their backend. The MCP server:

* **Allows developers to build an app** from scratch and deploy it to [DigitalOcean](https://thenewstack.io/tutorial-a-gitops-deployment-with-flux-on-digitalocean-kubernetes/), without ever leaving the IDE;
* **Deploys a new** app straight from a GitHub repository;
* **Change code and redeploy it** with a single prompt;
* **Create a list of all apps**, inspect them, restart them, or delete them from the editor.
* **Force rebuilding or deletion of an app**;
* **Check which regions are available** and plan deployments accordingly.

### 4. Figma’s Dev Mode MCP Server

**Why it’s useful:** [The Dev Mode MCP Server](https://www.postman.com/getmcp/public-mcp-servers/collection/6866ec3e48ab75becd41a29a) provides design information and context to AI agents generating code from [Figma design files](https://thenewstack.io/new-figma-plug-in-converts-design-to-angular-react-native/). A local server allows AI assistants to programmatically fetch detailed information about the current Figma file, project, and selected design elements (nodes) and integrates AI capabilities into the design-to-development workflow. It enables:

* **Code generation from selected frames or nodes**. Figma users can select a frame in Figma or provide a node URL to have an AI agent turn the design into code.
* **Extract design context from layers** by pulling out variables, components and layouts from a design to ensure builds adhere to design patterns.
* **Code Connect**. The MCP server informs AI agents about existing components derived from Code Connect information, supporting reuse.

### 5. GitHub MCP Server

**Why it’s useful:** [The GitHub MCP Server](https://github.com/github/github-mcp-server) is built for developers and allows AI agents to interact directly with the codebase, pull requests, and issues. The GitHub MCP Server connects AI tools directly to GitHub’s platforms, giving AI agents, assistants, and chatbots the ability to read repositories and code files, manage issues and PRs, analyze code, and automate workflows. All through natural language interactions. The MCP server provides:

* **Repository management:** Developers can browse and query code, search files, analyze commits, and understand project structure across any repository they have access to;
* **Issue and pull request automation:** Create, update and manage issues and pull requests. The AI can help triage bugs, review code changes, and maintain project boards.
* **Adding** intelligence to CI/CD and workflows. It can [monitor GitHub Actions workflow](https://thenewstack.io/the-missing-part-of-github-actions-workflows-monitoring/) runs, analyze build failures, manage releases and get insights into a development pipeline;
* **Analyzing code**, examining security findings, reviewing Dependabot alerts, understanding code patterns, and getting comprehensive insights into your codebase.
* **Team collaboration** by providing access to discussions, managing notifications, analyzing team activity, and streamlining processes for the team.

### 6. JetBrains MCP Proxy Server

**Why It’s Useful:** JetBrains offers IDEs, including IntelliJ IDEA for Java and Kotlin; PyCharm for Python, WebStorm for JavaScript, Rider for .NET, and CLion for C/C++. It offers a [plugin for its MCP proxy server](https://www.postman.com/getmcp/public-mcp-servers/collection/681e63aecb58000ecfc0317f), which allows AI tools to leverage the IDE’s code understanding capabilities, perform refactorings, generate code, and access project context directly within the development environment where the AI Assistant is running. It enables:

* **IDE integration**, providing a bridge for external AI agents to communicate with the AI Assistant plugin running within a JetBrains IDE;
* **Code understanding and analysis**, allowing the AI agent to access the IDE’s understanding of the codebase, including syntax, semantics, and project structure;
* **Code generation and modification**, which facilitate AI-driven code generation, autocompletion, refactoring, and other code manipulation tasks, are executed by the IDE.
* **Project context access**, enables the AI agent to get information about the current project, open files, and cursor position to provide contextually relevant assistance; and
* **Local execution**, which means the proxy runs locally, facilitating communication between a local AI agent or development tool and the local JetBrains IDE instance.

### 7. MongoDB MCP Server

**Why it’s useful:** The [MongoDB MCP Server](https://www.mongodb.com/company/blog/announcing-mongodb-mcp-server) allows AI to interact with its database. A frontend developer could use an AI agent to:

* **Query the database** for a specific piece of information.
* **Manage data** by adding a new user to the database using natural language.
* **Manage collections** by creating new collections for the database.
* **Get the schema of the database**; and
* **Create context-aware code generation**, which means developers can describe the needed data and let the AI generate the MongoDB queries and even the code to interact with it.

### 8. React MCP Server (third-party)

Meta hasn’t announced any plans to release an MCP server for React, but frontend developer Kalivaraprasad Gonapa, who works at Drishya AI Labs, has created one. The [React MCP Server](https://github.com/kalivaraprasad-gonapa/react-mcp) integrates with Claude Desktop, enabling the creation and modification of React apps based on user prompts, according to the GitHub repository. It enables:

* **Creating new React applications**;
* **Running React development servers**;
* **Managing files and directories**;
* **Installing npm packages**;
* **Executing terminal commands**; and
* **Tracking and managing long-running processes.**

### 9. Shopify Dev MCP server

**Why it’s useful:** This [MCP Server](https://shopify.dev/docs/apps/build/devmcp) connects a developer’s AI assistant to [Shopify’s](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/) development resources, enabling an AI assistant to search Shopify docs, explore API schemas, build Functions, and get up-to-date answers about Shopify APIs and best practices. The MCP server enables:

* **Querying your AI assistant** about developing with Shopify;
* **Supporting Shopify’s APIs**, which include the Admin GraphQL API, Functions, Polaris web components (optional), and Liquid (optional); and
* **Integration with AI development tools**, such as Cursor and Claude Desktop.

### 10. Vercel MCP Server

**Why it’s useful:** The [Vercel MCP Server](https://vercel.com/docs/mcp/vercel-mcp) allows AI to interact with the frontend development and hosting platform. It works with Gemini CLI, [Gemini Code Assist](https://thenewstack.io/google-vaunts-new-gemini-code-assist-tool-at-cloud-next-2024/), Windsurf, Goose, Raycast, Devin, VS Code with Copilot, Cursor, Claude and Claude Code, and ChatGPT. It enables:

* **Deploying a new version of an app**;
* **Getting feedback on the application**, including new features;
* **Managing app settings** by checking an app’s environment variables; and
* **Handling the configuration of a new application**.

## Coming Soon

### **Angular MCP Server** (experimental)

**Why it’s useful:** [Angular has an CLI MCP server](https://angular.dev/ai/mcp) in the experimental phase that will provide tools to help developers in their workflow. It enables:

* **Best practice support** by allowing developers to access the Angular Best Practices Guide to ensure all code adheres to modern standards.
* **Listing all applications and libraries** defined in an Angular workspace by reading the angular.json configuration file; and
* **Searching Angular’s official documentation**.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)