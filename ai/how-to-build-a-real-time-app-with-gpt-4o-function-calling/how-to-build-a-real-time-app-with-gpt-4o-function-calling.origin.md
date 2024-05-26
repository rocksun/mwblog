# How To Build a Real-Time App With GPT-4o Function Calling
![Featued image for: How To Build a Real-Time App With GPT-4o Function Calling](https://cdn.thenewstack.io/media/2024/05/96f2ccb9-getty-images-zjuokhavvuo-unsplash-1024x683.jpg)
In our
[guide to function calling in LLMs](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/), we discussed how to bring real-time data to chatbots and agents. Now we will explore this concept further by integrating [the API](https://www.flightaware.com/commercial/aeroapi/) from FlightAware.com with the new [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/) model, in order to track flight status in real-time.
FlightAware’s AeroAPI is a robust, RESTful API offering on-demand access to extensive flight tracking and status data. It allows developers to fetch real-time, historical, or future flight information via a simple query-based system. The API supports detailed requests based on flight identifiers, aircraft registration, or locations like airports or operators. It is designed to deliver precise, actionable aviation data in JSON format, supporting operational needs across the aviation industry, from airlines to airports.
Before you proceed further, sign up with FlightAware and get your API key, which is essential for invoking the REST API. The free personal tier is sufficient to complete this tutorial.
## Step 1: Define the Function to Get Flight Status
Once you have the API key, create the below function in Python to retrieve the status of any flight.
Though the code is straightforward, let me explain the key steps.
The function,
get_flight_status takes a flight parameter (assumed to be a flight identifier) and returns formatted flight details in JSON format. It queries the AeroAPI to fetch flight data based on the given flight identifier and formats key details such as the source, destination, departure time, arrival time, and status.
Let’s look at the components of the script:
**API Credentials:**
AEROAPI_BASE_URL is the base URL for the FlightAware AeroAPI.
AEROAPI_KEY is the API key used for authentication.
**Session Management:**
get_api_session: This nested function initializes a request. Session object sets the required header with the API key, and returns the session object. This session will handle all API requests.
**Data Fetching:**
fetch_flight_data: This function takes flight_id and session as arguments. It constructs the endpoint URL with appropriate date filters for fetching data for one day and sends a GET request to retrieve the flight data. The function handles the API response and extracts the relevant flight information.
**Time Conversion:**
utc_to_local: Converts UTC time (from the API response) to local time based on the provided timezone string. This function helps us get the arrival and departure times based on the city.
**Data Processing:**
The script determines keys for departure and arrival times based on the availability of estimated or actual times, with a fallback to scheduled times. It then constructs a dictionary containing formatted flight details.
The above screenshot shows the response we received from FlightAware API for the Emirates flight EK524 that flies from Dubai to Hyderabad. Notice that the arrival and departure times are local times based on the city.
Our goal is to integrate this function with GPT-4 Omni to give it real-time access to flight tracking information.
## Step 2: Implementing Function Calling With GPT-4o
Let’s start by importing the OpenAI library and initializing it.
|
1
2
|
from openai import OpenAI
client = OpenAI()
This line creates an instance of the OpenAI class. This instance (client) will be used to interact with the
[OpenAI API](https://thenewstack.io/the-promise-of-riches-from-ai-wrappers/).
We will define a list called
*tools*, containing a dictionary that specifies the function
get_flight_status. This function is intended to be used as a tool within the OpenAI API context, describing its parameters and required input.
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
|
tools = [
{
"type": "function",
"function": {
"name": "get_flight_status",
"description": "Get status of a flight",
"parameters": {
"type": "object",
"properties": {
"flight": {
"type": "string",
"description": "Flight number"
}
},
"required": ["flight"]
}
}
}
]
The heavy lifting takes place in the below function, where the LLM inspects the prompt to determine if the function/tool needs to be called and then proceeds to generate an appropriate response.
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
|
def chatbot(prompt):
# Step 1: send the conversation and available functions to the model
messages = [{"role": "user", "content": prompt}]
response = client.chat.completions.create(
model="gpt-4o",
messages=messages,
tools=tools,
tool_choice="auto"
)
response_message = response.choices[0].message
tool_calls = response_message.tool_calls
# Step 2: check if the model wanted to call a function
if tool_calls:
available_functions = {
"get_flight_status": get_flight_status,
}
messages.append(response_message)
# Step 3: send the function response to the model
for tool_call in tool_calls:
function_name = tool_call.function.name
function_to_call = available_functions[function_name]
function_args = json.loads(tool_call.function.arguments)
function_response = function_to_call(flight=function_args.get("flight"))
messages.append(
{
"tool_call_id": tool_call.id,
"role": "tool",
"name": function_name,
"content": function_response,
}
)
final_response = client.chat.completions.create(
model="gpt-4o",
messages=messages,
)
return final_response
This function,
chatbot, takes a user prompt and processes it using the OpenAI API. It sends the prompt and the defined tools to the OpenAI model and processes the response.
The messages are created by embedding the prompt from the user and sending it to the OpenAI API (chat.completions.create). The API processes these messages using the specified tools, if applicable.
For example, when we send the prompt “What’s status of EK524?”, GPT-4o determines that it needs to call the function provided in the tools list and comes back with the below response:
Notice that the response includes the function (
get_flight_status) and the parameter (
EK226).
The next step checks if any tools were called (i.e., functions within tools). It executes these functions using the provided arguments, integrates their outputs into the conversation, and sends this updated information back to the OpenAI API for further processing.
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
|
# Step 2: check if the model wanted to call a function
if tool_calls:
available_functions = {
"get_flight_status": get_flight_status,
}
messages.append(response_message)
# Step 3: send the info for each function call and function response to the model
for tool_call in tool_calls:
function_name = tool_call.function.name
function_to_call = available_functions[function_name]
function_args = json.loads(tool_call.function.arguments)
function_response = function_to_call(flight=function_args.get("flight"))
messages.append(
{
"tool_call_id": tool_call.id,
"role": "tool",
"name": function_name,
"content": function_response,
}
)
At this point, the
messages list includes the original prompt, the initial response with the function name and arguments, and the actual output from the function. The below screenshot shows the list with all the elements.
With the response from the tool appended to the history, we can invoke the chat completion endpoint to get the final answer from the LLM.
|
1
2
3
4
5
|
final_response = client.chat.completions.create(
model="gpt-4o",
messages=messages,
)
return final_response
The
final_response object has the answer we are looking for:
Sending the prompt to the function
chatbot will respond with the real-time status of the specified flight.
Below is the complete code for this tutorial:
In this tutorial, we explored how to bring real-time data to LLMs through function calling. In the next part of this series, we will replace GPT-4o with
[Gemini Pro](https://thenewstack.io/with-gemini-pro-google-vies-for-top-spot-in-genai-race/) to explore the same concept but with a different model. Stay tuned. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)