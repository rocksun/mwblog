# How to Build AI Agents Without Frameworks: A Step-by-Step Guide
![blog preview](/_next/image?url=%2Fblog%2FBlogHeader_AiAgentsFromScratch.jpg&w=3840&q=75)
AI agents are often overcomplicated. At their core, they're just language
models with the ability to use tools and remember context. While
frameworks like [LangChain](https://www.langchain.com/) or
[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) can help you
get started quickly, they add layers of abstraction that can make it
harder to understand what's actually happening – and harder to customize
your agent for specific use cases.

In this tutorial, we'll build an AI agent from scratch using direct API calls to GPT-4o. You'll learn how to create an agent that can query PostgreSQL databases, fetch information from Wikipedia, and maintain conversation context through simple database storage. No frameworks, just clean code and clear concepts.

The goal is to demonstrate that AI agents don't need complex architectures. We'll focus on the essential components: prompt engineering for tool use, storing conversation history in PostgreSQL, and managing the interaction flow between the LLM and its tools.

At the end, you will know exactly, what an agent is, how it works and how to build them. If you then decide to still use a framework - that's fine. However, you will have a much better understanding of what's happening under the hood.

Let's start by understanding what makes something an AI agent, and then build one step by step.

## What Are AI Agents?
An AI agent is fundamentally just a language model that can:

- Understand what tools it has available
- Decide when to use these tools
- Remember previous interactions
- Make decisions based on all this information
### What Are Tools?
Tools (sometimes called "functions" or "capabilities") are simply functions that the agent can call to interact with the outside world. They're just Python functions with:

- A clear description of what they do
- Defined input parameters
- Structured output
Here's a concrete example of a tool:

When we give our agent access to this tool, we're essentially telling it: "You can search Wikipedia by calling this function." The LLM then decides, based on the user's question, whether it needs to use this tool to provide a good answer. When we say "the LLM decides," we mean that we prompt the LLM with the available tools and ask it to decide which one to use. The AI model then simply returns a text response with the tool name.

**Common examples of tools include:**
- Database queries
- Web searches
- API calls
- File operations
- Calculator functions
- Email sending capabilities
To bring both the concepts of agents and tools together, we see that there is no magic involved. It's just AI model interactions and a bunch of python functions.

Bringing this together, a pseudo-code for an AI agent might look like this:

This is the core concept of an agent. Everything else – complex planning, multiple tool calls, sophisticated memory systems – is just an extension of this basic pattern.

**Common misconceptions about agents:**
- They don't need complex orchestration frameworks
- They don't need to run autonomously (though they can)
- They don't need sophisticated planning algorithms (though these can help for complex tasks)
**The key to building effective agents is not in the framework you use, but in:**
- Writing clear prompts that help the LLM understand its capabilities
- Implementing reliable tools that the agent can use
- Maintaining relevant context through some form of memory storage
In the following sections, we'll implement this pattern with real code, building an agent that can actually query databases and search Wikipedia. You'll see that the complexity comes from the specific requirements of your use case, not from the agent architecture itself.

## Why Build Agents Without Frameworks?
Frameworks like LangChain and AutoGPT are often recommended for building AI agents. While they can be useful for quick prototypes, there are compelling reasons to avoid them:

### Understanding What Really Happens
The framework-free version is more explicit. You can see exactly:

- What the LLM is being told
- When tools are being called
- How decisions are being made
### Flexibility and Control
Frameworks often make assumptions about:

- How tools should be structured
- What the prompt format should be
- How memory should work
When you need to customize any of these, you often end up fighting against the framework rather than working with it.

### Simpler Debugging
When something goes wrong with a framework:

**Note:** This is more or less the most prominent reason why you should
build agents without frameworks. Frameworks abstract away the core of
any AI Agent - the LLM interaction. Without adding additional
infrastructure, you don't know the exact prompts used, the specific LLM
answers replied and the tools used. This makes debugging a nightmare.
### Lower Learning Overhead
Building agents requires understanding:

- LLM prompting
- Tool integration
- Memory management
Frameworks add another layer:

- Framework-specific concepts
- Configuration options
- Integration patterns
Why learn both when you only need the fundamentals?

### Performance and Resources
Frameworks often:

- Load unnecessary components
- Add network calls
- Include unused features
Direct implementation lets you:

- Load only what you need
- Optimize critical paths
- Control resource usage
**Note:** Arguably, raw performance is not the most important thing for
AI agents, as the AI model interaction in itself is quite slow. So
loading some additional modules does not add up that much.
### When to Use Frameworks
Frameworks make sense when:

- You're building a quick prototype
- You need pre-built tools
- You're learning agent concepts initially
But for production systems or when you need full control, direct implementation is often better.

Let's move on to building our agent from scratch, where you'll see how straightforward the direct implementation can be.

## Building an AI Agent Step by Step
Before we dive into the code, let's understand what we'll be building in this first step. We'll start by defining our tools - the capabilities we want to give our agent.

### Step 1: Defining Tools
In this step, we'll create two tools:

- A PostgreSQL query tool that allows the agent to query your database and search for information stored in the database.
- A Wikipedia search tool that lets the agent look up information in Wikipedia.
We can see that both tools are quite different, so depending on the users question, the agent should be able to decide to use one of these tools.

When defining tools for OpenAI's function calling, we need three components for each tool:

- A schema that tells the LLM what the tool does and how to use it. This is basically just a json description of the python function. It will get clearer once you see the example.
- The actual implementation of the tool (the Python function)
- Error handling to ensure our agent behaves gracefully when things go wrong
The schema is particularly important because it acts as documentation for
the LLM. Think of it as writing API documentation - the better you
describe your tools, the better the LLM will use them. Important are the
`name`
(which should match the function name), `description`
(what the
tool does) and `parameters`
(what function parameter values we need).

For our database tool, we'll:

- Allow only SELECT queries for safety
- Return results as JSON for easy parsing
- Include error handling for database connection issues
For the Wikipedia tool, we'll:

- Limit results to three sentences to keep responses concise
- Handle disambiguation pages and missing articles
- Return structured error messages when searches fail
Here's how we implement these tools:

### Step 2: Creating the Agent Class - Detailed Design
Before implementing the code, let's understand exactly what we're building and how it works:

#### Core Concept
An AI agent is essentially a loop of:

- Receiving user input
- Deciding whether to use tools
- Using tools if needed
- Formulating a response
#### Key Components Design
##### 1. Message Management
- We need to maintain a conversation history as a list of messages
- Each message has a specific role: 'user', 'assistant', or 'tool'
- The history provides context for the LLM to make better decisions
- Think of it like a chat application's state management
##### 2. Tool Execution System
- Works like a command dispatcher:
- LLM decides to use a tool
- We receive a structured function call
- We map this to our actual Python functions
- We handle the execution and any errors
- We format the result for the LLM
##### 3. Main Processing Loop
#### Error Handling Strategy
We need three layers of error handling:

- Tool-level errors (e.g., database connection failed)
- LLM-level errors (e.g., API issues)
- General processing errors (e.g., JSON parsing)
#### Message Flow Example
This design allows for:

- Clear separation of concerns
- Easy debugging and monitoring
- Flexible extension with new tools
- Robust error handling
- Maintainable codebase
Note that we implement the general agent structure as part of a loop. Meaning that we send back the results of our tool calls to the LLM which then decides whether to formulate a final answer or call another tool.

#### Implementation
### (Optional) Step 3: Adding Memory to Our Agent
**Note:** Please consider whether you need memory at all. Does your
application really need to store and retrieve conversation histories?
More often than not, the answer is no! But if you do need memory, here's
how you can add it.
Memory in AI agents is often overcomplicated. Let's understand what we're actually trying to achieve:

#### What is Agent Memory?
At its core, agent memory is just:

- Storing conversations and their context
- Retrieving relevant information when needed
- Summarizing past interactions when they become too long
#### Memory Types We'll Implement
-
**Conversation History**- Store: User inputs, agent responses, tool usage results
- Purpose: Keep track of the current conversation flow
-
**Summary Memory**- What: Periodic summaries of longer conversations
- Why: Prevent context window overflow
- How: Create summaries after X messages or on demand
### Database Schema
#### Memory Flow
#### Implementation of Memory for an AI Agent
Before we continue...

## Interested in how to train your very own Large Language Model?
We prepared a well-researched guide for how to use the latest advancements in Open Source technology to fine-tune your own LLM. This has many advantages like:

- Cost control
- Data privacy
- Excellent performance - adjusted specifically for your intended use
### Step 4: Using Your AI Agent
After all the setup, using the agent is surprisingly straightforward. Here's how:

That's it! The agent will:

- Use the database when needed
- Search Wikipedia when appropriate
- Remember previous context
- Create summaries automatically
- Handle all the complexity behind the scenes - but at the same time giving us direct debugging access
The output looks clean and natural:

## Enhanced Database Tool with Schema Awareness
Arguably, the above PostgreSQL database tool is a little simple isn't it? From where should the AI model know what database columns are available? You are right with that - we left out this crucial detail for more clarity. We'll modify our database tool to include schema information, which helps the LLM understand what data is available and how to query it correctly:

Key improvements:

- Schema information in tool description
- Column types and constraints included
- Schema returned on errors for better error handling
- Detailed result structure with column names
This helps the LLM:

- Write correct queries on the first try
- Understand available data
- Handle errors better
- Provide more detailed responses