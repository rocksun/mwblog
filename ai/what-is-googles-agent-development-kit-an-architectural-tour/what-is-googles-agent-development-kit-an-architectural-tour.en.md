Google’s [Agent Development Kit](https://google.github.io/adk-docs/) (ADK) is a fundamental shift in how developers build AI-powered applications. Rather than treating large language models as simple request-response systems, ADK introduces an event-driven runtime architecture that orchestrates agents, tools and persistent state into cohesive applications.

This article explores the core architectural components of ADK and demonstrates how they work together, via a practical implementation of a weather agent.

## Understanding the ADK Runtime Architecture

The code below defines the end-to-end workflow in Python:

```
import os
import asyncio
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types 


import warnings
warnings.filterwarnings("ignore")


import logging
logging.basicConfig(level=logging.ERROR)




def get_weather(city: str) -> dict:
 print(f"--- Tool: get_weather called for city: {city} ---")
 city_normalized = city.lower().replace(" ", "")
 mock_weather_db = {
 "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
 "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
 "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }
 if city_normalized in mock_weather_db:
 return mock_weather_db[city_normalized]
 else:
 return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}


AGENT_MODEL = "gemini-2.5-flash"


weather_agent = Agent(
 name="weather_agent_v1",
 model=AGENT_MODEL,
 description="Provides weather information for specific cities.",
 instruction="You are a helpful weather assistant. "
 "When the user asks for the weather in a specific city, "
 "use the 'get_weather' tool to find the information. "
 "If the tool returns an error, inform the user politely. "
 "If the tool is successful, present the weather report clearly.",
 tools=[get_weather],
)


session_service = InMemorySessionService()


APP_NAME = "weather_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001"




session = asyncio.run(session_service.create_session(
 app_name=APP_NAME,
 user_id=USER_ID,
 session_id=SESSION_ID
))


print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")


runner = Runner(
 agent=weather_agent,
 app_name=APP_NAME,
 session_service=session_service
)
print(f"Runner created for agent '{runner.agent.name}'.")


def call_agent(query: str, runner, user_id, session_id):
 print(f"\n>>> User Query: {query}")
 content = types.Content(role='user', parts=[types.Part(text=query)])
 final_response_text = "Agent did not produce a final response."


 for event in runner.run(user_id=user_id, session_id=session_id, new_message=content):
 #print(event)
 if event.is_final_response():
 if event.content and event.content.parts:
 final_response_text = event.content.parts[0].text


 print(f"<<< Agent Response: {final_response_text}")


def run_conversation():
 call_agent("What is the weather like in London?", runner, USER_ID, SESSION_ID)
 call_agent("How about Paris?", runner, USER_ID, SESSION_ID)
 call_agent("Tell me the weather in New York", runner, USER_ID, SESSION_ID)


if __name__ == "__main__":
 try:
 run_conversation()
 except Exception as e:
 print(f"An error occurred: {e}")
```

The ADK runtime operates as a sophisticated event loop that mediates between user requests, AI model invocations, and external tool executions. At the highest level, three primary interactions define the system’s behavior.

First, a user submits a message along with a session identifier. This session ID is crucial because it allows the runtime to maintain conversational context across multiple exchanges. Second, an internal event loop processes the request by coordinating between execution logic and persistent services. Third, the system streams events back to the user, including intermediate tool calls and the final response.

The following architectural diagram reveals the interconnected components that enable this.

[![](https://cdn.thenewstack.io/media/2025/12/9b1d980b-event-loop-1024x464.png)](https://cdn.thenewstack.io/media/2025/12/9b1d980b-event-loop-1024x464.png)

## The Runner as Orchestrator

The Runner sits at the center of ADK’s architecture, serving as the primary entry point for all user interactions. When you instantiate a Runner, you bind it to a specific agent and a session service, creating a self-contained execution context.

```
runner = Runner(
    agent=weather_agent,
    app_name=APP_NAME,
    session_service=session_service
)
```

The Runner contains an Event Processor that transforms raw model outputs into structured events. Every interaction with an ADK agent flows through the Runner’s run method, which yields a stream of events rather than returning a single response. This streaming approach enables real-time feedback and allows applications to react to intermediate steps like tool invocations.

```
for event in runner.run(user_id=user_id, session_id=session_id, new_message=content):
    if event.is_final_response():
        final_response_text = event.content.parts[0].text
```

This pattern differs significantly from traditional API calls. Instead of waiting for a complete response, your application receives events as they occur — which enables progress indicators, debugging output and dynamic UI updates.

## How the Event Loop Works

The event loop represents ADK’s core innovation. It operates as a bidirectional communication channel between the Runner and the Execution Logic layer, following an ask-yield pattern.

When the Runner receives a user message, it asks the Execution Logic to process it. The Execution Logic might invoke the underlying LLM, call a tool, or execute a callback. Each of these operations yields events back to the Runner, which can then forward them to the user or trigger additional processing.

This architecture supports multi-step reasoning naturally. Consider what happens when a user asks for weather information. The LLM first determines that it needs to call the `get_weather` tool. The Execution Logic invokes that tool and yields an event containing the result. The LLM then processes the tool output and generates a human-readable response. Each step produces events that flow through the system.

## Execution Logic and Tool Integration

The Execution Logic layer handles the actual work of running agents. It manages LLM invocations, tool callbacks, and any custom logic you define. Tools in ADK are simply Python functions with type hints that the framework automatically exposes to the underlying model.

```
def get_weather(city: str) -&gt; dict:
    city_normalized = city.lower().replace(" ", "")
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
    }
    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}
```

The Agent configuration binds tools to specific models and provides instructions that guide behavior. The `instruction` field acts as a system prompt, while the `tools` parameter registers available functions.

```
weather_agent = Agent(
    name="weather_agent_v1",
    model=AGENT_MODEL,
    description="Provides weather information for specific cities.",
    instruction="You are a helpful weather assistant. When the user asks for the weather...",
    tools=[get_weather],
)
```

When the LLM decides to call get\_weather, ADK handles the entire invocation lifecycle. It parses the model’s function call, executes your Python function, and feeds the result back to the model for interpretation.

## Services Layer and State Management

The Services layer provides persistence capabilities that transform stateless LLM interactions into stateful applications. Three primary services operate within this layer.

Session services maintain conversational state across multiple turns. The InMemorySessionService used in our example stores everything in memory, suitable for development and testing. Production deployments typically use persistent backends like Cloud Firestore or PostgreSQL.

```
session_service = InMemorySessionService()

session = asyncio.run(session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
))
```

Artifact services handle file storage and retrieval, enabling agents to work with documents, images, and other binary data. Memory services provide long-term storage for information that should persist across sessions.

The Services layer connects to external Storage systems through well-defined interfaces. This abstraction allows you to swap storage backends without modifying agent logic. Your weather agent could move from in-memory storage to a distributed database simply by changing the session service implementation.

## The Complete Request Flow

Tracing a complete request through the system illustrates how these components collaborate.

A user sends “What is the weather like in London?” with their session identifier. The Runner receives this message, wraps it in a Content object, and initiates the event loop. The Execution Logic invokes the LLM with the user message and available tool definitions.

The model recognizes this as a weather query and generates a tool call for get\_weather with the argument “London”. The Execution Logic intercepts this call, invokes the Python function, and captures the return value. An event containing the tool result flows back through the system.

The model receives the tool output and generates a natural language response summarizing the weather conditions. This final response event streams to the user through the Runner.

Throughout this process, the Session service maintains context. When the user follows up with “How about Paris?”, the session history allows the model to understand this refers to weather, even though the word never appears in the second query.

## Key Design Implications of ADK

ADK’s architecture reveals several important design principles for AI application development.

The event-driven approach enables observability and debugging that would be impossible with synchronous APIs. You can log every tool invocation, monitor model reasoning, and build sophisticated analytics around agent behavior.

The separation between Runner and Execution Logic creates clean boundaries for testing. You can mock the Execution Logic to test Runner behavior, or inject test doubles for external services to verify agent logic in isolation.

The Services layer abstraction future-proofs your application against infrastructure changes. As managed services for agent memory and session storage become available, migration requires minimal code changes.

## Conclusion

Google’s Agent Development Kit provides a production-ready framework for building AI applications that go beyond simple chat interfaces. The event loop architecture, combined with robust session management and flexible tool integration, enables developers to create agents that maintain context, invoke external capabilities, and scale across distributed infrastructure. Understanding these architectural foundations equips you to build sophisticated AI systems that meet real-world requirements.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)