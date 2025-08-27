In [a previous article](https://thenewstack.io/how-elicitation-in-mcp-brings-human-in-the-loop-to-ai-tools/), I introduced the concept of [elicitation](https://modelcontextprotocol.io/specification/draft/client/elicitation) in the [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP). This tutorial demonstrates a practical approach to integrating elicitation to accept user input, instead of sending hard-coded parameters to the tools exposed by the MCP server.

## Step 1: Creating the Environment

Let’s start with a virtual environment and `requirements.txt` file.

```
python -m venv .venv
source .venv/bin/activate
```

Create `requirements.txt` with the below contents:

```
pytz
fastmcp
httpx
google-genai
```

```
pip install --upgrade -r requirements.txt
```

Set the environment variables for `AEROAPI_KEY` and `GEMINI_API_KEY` for [FlightAware](https://www.flightaware.com/commercial/data/) and [Gemini](https://aistudio.google.com) API, respectively.

## Step 2: Build and Launch MCP Server

Below is the code for the MCP server with elicitation:

```
# server.py
from fastmcp import FastMCP, Context
from dataclasses import dataclass
import httpx
import os
from datetime import datetime, timedelta
import pytz


mcp = FastMCP("Flight Status Server")


@dataclass
class FlightInfo:
 flight_number: str


@mcp.tool
async def get_flight_status(ctx: Context) -> str:
 """Get live flight status information by collecting flight number interactively."""
 
 # Elicit flight number from user
 result = await ctx.elicit(
 message="Please provide the flight number you want to check",
 response_type=FlightInfo
    )
 
 if result.action == "decline":
 return "Flight number not provided"
 elif result.action == "cancel":
 return "Operation cancelled"
 elif result.action != "accept":
 return "Invalid response"
 
 flight_number = result.data.flight_number
 
 try:
 # Fetch flight data
 flight_details = await _fetch_flight_status(flight_number)
 
 # Format response
 return f"""
Flight Status for {flight_details['flight']}:
• Route: {flight_details['source']} → {flight_details['destination']}
• Departure: {flight_details['depart_time']}
• Arrival: {flight_details['arrival_time']}
• Status: {flight_details['status']}
        """.strip()
 
 except Exception as e:
 return f"Error fetching flight status: {str(e)}"


async def _fetch_flight_status(flight: str) -> dict:
 """Internal function to fetch flight status from FlightAware API."""
 AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi"
 AEROAPI_KEY = os.getenv("AERO_API_KEY")
 
 if not AEROAPI_KEY:
 raise ValueError("AERO_API_KEY is not set in environment variables")
 
 def _clean_flight_id(flight_id):
 if "flight_id=" in flight_id:
 return flight_id.split("flight_id=")[1]
 return flight_id
 
 def _utc_to_local(utc_date_str, local_timezone_str):
 utc_datetime = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
 local_timezone = pytz.timezone(local_timezone_str)
 local_datetime = utc_datetime.astimezone(local_timezone)
 return local_datetime.strftime('%Y-%m-%d %H:%M:%S')
 
 # Prepare API request
 flight_id = _clean_flight_id(flight)
 start_date = datetime.now().date().strftime('%Y-%m-%d')
 end_date = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
 api_resource = f"/flights/{flight_id}?start={start_date}&end={end_date}"
 
 # Make API call
 async with httpx.AsyncClient(headers={"x-apikey": AEROAPI_KEY}) as client:
 response = await client.get(f"{AEROAPI_BASE_URL}{api_resource}")
 response.raise_for_status()
 flight_data = response.json()['flights'][0]
 
 # Determine best available times
 dep_key = ('estimated_out' if flight_data.get('estimated_out') else
 'actual_out' if flight_data.get('actual_out') else
 'scheduled_out')
 
 arr_key = ('estimated_in' if flight_data.get('estimated_in') else
 'actual_in' if flight_data.get('actual_in') else
 'scheduled_in')
 
 # Build response
 flight_details = {
 'flight': flight,
 'source': flight_data['origin']['city'],
 'destination': flight_data['destination']['city'],
 'depart_time': _utc_to_local(flight_data[dep_key], flight_data['origin']['timezone']),
 'arrival_time': _utc_to_local(flight_data[arr_key], flight_data['destination']['timezone']),
 'status': flight_data['status']
    }
 
 return flight_details


if __name__ == "__main__":
 mcp.run(transport="streamable-http", host="127.0.0.1", port=8080, path="/mcp")
```

Let’s take a look at important code snippets that help us implement elicitation.

### **Define the Structured Response**

```
@dataclass
class FlightInfo:
    flight_number: str
```

This dataclass sets the expected schema for user input. It ensures the client response is strongly typed and validated when returned to the server.

### **Declare the Tool Entry**

```
@mcp.tool
async def get_flight_status(ctx: Context) -&gt; str:
    """Get live flight status information by collecting flight number interactively."""
```

This function defines the tool available to the client. The ctx parameter enables elicitation and structured interaction with the user.

### **Ask the Client For Input With Elicitation**

```
result = await ctx.elicit(
    message="Please provide the flight number you want to check",
    response_type=FlightInfo
)
```

This call triggers the elicitation process. The server sends a message and requests a response that matches the FlightInfo schema.

### **Handle User Actions From the Elicitation Result**

```
if result.action == "decline":
    return "Flight number not provided"
elif result.action == "cancel":
    return "Operation cancelled"
elif result.action != "accept":
    return "Invalid response"
```

These conditionals ensure robust handling of user decisions. The server gracefully exits or continues depending on whether input was accepted, declined, or canceled.

### **Consume the Accepted Input**

```
flight_number = result.data.flight_number
```

Launch the MCP Server in the terminal.

[![](https://cdn.thenewstack.io/media/2025/08/6f10f4fd-mcp-1-1024x894.png)](https://cdn.thenewstack.io/media/2025/08/6f10f4fd-mcp-1-1024x894.png)

## Step 3: Invoke the Client

Below is the code for the MCP client with elicitation:

```
# client.py
import asyncio
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult
from google import genai
from google.genai import types


async def send_to_gemini(flight_status_result: str, user_query: str = None):
 """Send flight status result to Gemini for analysis."""
 try:
 gemini_client = genai.Client()
 
 # Use the user query if provided, otherwise create a default prompt
 if user_query:
 prompt = f"{user_query}\n\nFlight Status Data:\n{flight_status_result}"
 else:
 prompt = f"Please analyze this flight status information and provide insights:\n\n{flight_status_result}"
 
 response = gemini_client.models.generate_content(
 model="gemini-2.5-flash",
 contents=prompt
        )
 
 return response.text
 
 except Exception as e:
 return f"Error sending to Gemini: {e}"


async def elicitation_handler(message: str, response_type: type, params, context):
 print(f"Server asks: {message}")
 
 try:
 flight_number = input("Enter flight number (e.g., AA123, UA456): ")
 if not flight_number.strip():
 print("No flight number provided")
 return ElicitResult(action="decline")
 return response_type(flight_number=flight_number.strip())
 
 except KeyboardInterrupt:
 print("\nOperation cancelled by user")
 return ElicitResult(action="cancel")
 except Exception as e:
 print(f"Error handling input: {e}")
 return ElicitResult(action="decline")


async def main():
 client = Client("http://127.0.0.1:8080/mcp/", elicitation_handler=elicitation_handler)
 
 async with client:
 while True:
 print("\nFlight Status Tool with Gemini Analysis")
 print("1. Get flight status")
 print("2. Get flight status with custom Gemini query")
 print("3. Exit")
 
 choice = input("\nSelect an option (1-3): ").strip()
 
 if choice == "1":
 try:
 # Get flight status from MCP server
 result = await client.call_tool("get_flight_status")
 print("\nFlight Status Result:")
 #print(result)
 flight_status_text = result.content[0].text
 print(flight_status_text)
 except Exception as e:
 print(f"Error getting flight status: {e}")
 
 elif choice == "2":
 try:
 # Get custom query from user
 user_query = input("\nEnter your question about the flight (e.g., 'Is this flight likely to be delayed?'): ").strip()
 
 # Get flight status from MCP server
 result = await client.call_tool("get_flight_status")
 print("\nFlight Status Result:")
 print(result)
 
 # Send to Gemini with custom query
 print("\nSending to Gemini with your question...")
 gemini_response = await send_to_gemini(result, user_query)
 print("\nGemini Analysis:")
 print(gemini_response)
 
 except Exception as e:
 print(f"Error getting flight status: {e}")
 
 elif choice == "3":
 print("Goodbye!")
 break
 
 else:
 print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
 asyncio.run(main())
```

Let’s take a look at the code snippets that helped us implement elicitation in the client.

### **Define the Elicitation Handler**

```
async def elicitation_handler(message: str, response_type: Any) -&gt; Any:
    print(f"Server asks: {message}")
    try:
        flight_number = input("Enter flight number: ").strip()
        if not flight_number:
            return ElicitResult(action="decline")
        return response_type(flight_number=flight_number)
    except KeyboardInterrupt:
        return ElicitResult(action="cancel")
```

This function runs when the server calls ctx.elicit. It prints the server’s prompt, captures user input, and returns a structured response or an action (such as decline or cancel).

### **Register the Handler With the Client**

```
client = Client(
    base_url="http://localhost:8000/mcp",
    elicitation_handler=elicitation_handler
)
```

The client is instantiated with the elicitation handler attached. This allows it to respond automatically whenever the server triggers an elicitation request.

### **Use the Handler in the Interaction Loop**

```
result = await client.call_tool("get_flight_status", {})
print("Result from server:", result)
```

When the client calls the tool, any elicitation initiated by the server is routed through the registered handler. The final tool result is displayed only after the elicitation process completes.

Launch the MCP client in a new terminal window.

[![](https://cdn.thenewstack.io/media/2025/08/ac7fe651-mcp-2-1024x289.png)](https://cdn.thenewstack.io/media/2025/08/ac7fe651-mcp-2-1024x289.png)

When you select the first option, you will see the raw response from the tool. The second option sends the prompt along with the tool output (context) to Gemini for analysis and an elaborate response.

I hope you found this tutorial helpful in implementing [human-in-the-loop](https://thenewstack.io/human-on-the-loop-the-new-ai-control-model-that-actually-works/) when calling MCP tools.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)