In our recent [tour of Google’s Agent Development Kit](https://thenewstack.io/what-is-googles-agent-development-kit-an-architectural-tour/) (ADK), I walked you through the three approaches to building AI agents with ADK: Python, YAML, and the Visual Builder. While local development is great for prototyping, production-ready agents need to be deployed where they can scale and serve real users.

Google Cloud Run is a natural fit for ADK agents. As a fully managed serverless platform, it handles infrastructure concerns while you focus on agent logic. What makes this deployment particularly elegant is ADK’s built-in `adk deploy cloud_run` command, which packages your agent, builds a container image, pushes it to Artifact Registry, and deploys it to Cloud Run — all in a single step.

In this tutorial, I’ll guide you through deploying a weather and time agent to Cloud Run, complete with secure API key management using Google Secret Manager. By the end, you’ll have a production-ready agent accessible via a public URL with the ADK web UI enabled for interactive testing.

## Understanding the Deployment Architecture

Before diving into implementation, let’s understand what happens when you deploy an ADK agent to Cloud Run.

The `adk deploy cloud_run` command automates several complex operations. It analyzes your project structure and dependencies to generate an optimized Docker image. This image is then pushed to Google Artifact Registry, a secure container repository within your Google Cloud project. Finally, Cloud Run provisions a serverless instance that runs your agent; with automatic scaling, HTTPS, and IAM integration.

The `--with_ui` flag is handy because it bundles the ADK web development UI with your agent’s API server, giving you an interactive interface for testing conversations directly in your browser.

## Prerequisites

Before we begin, ensure you have:

* Python 3.10 or higher installed.
* Google Cloud SDK (gcloud) installed and configured.
* A Google Cloud project with billing enabled.
* The following APIs enabled: Cloud Run, Artifact Registry, Secret Manager, and Vertex AI.
* A Google API key from Google AI Studio (for Gemini access).

## Step 1: Setting Up the Project Structure

Let’s create the agent project with the required directory structure. ADK expects a specific layout for deployment to work correctly.

Create a new directory for your agent:

```
mkdir weather_time
cd weather_time
```

ADK requires three files within your agent directory: `__init__.py`, `agent.py`, and `requirements.txt`. The deployment tool looks for a variable named root\_agent in your agent code — this naming convention is mandatory.

Create the \_\_init\_\_.py file:

```
from . import agent
```

This file marks the directory as a Python package and imports the agent module.

## Step 2: Building the Agent

Create the agent.py file with the weather and time tools:

```
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_weather(city: str) -> dict:
 """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
 if city.lower() == "new york":
 return {
 "status": "success",
 "report": (
 "The weather in New York is sunny with a temperature of 25 degrees"
 " Celsius (77 degrees Fahrenheit)."
            ),
        }
 else:
 return {
 "status": "error",
 "error_message": f"Weather information for '{city}' is not available.",
        }




def get_current_time(city: str) -> dict:
 """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """


 if city.lower() == "new york":
 tz_identifier = "America/New_York"
 else:
 return {
 "status": "error",
 "error_message": (
 f"Sorry, I don't have timezone information for {city}."
            ),
        }


 tz = ZoneInfo(tz_identifier)
 now = datetime.datetime.now(tz)
 report = (
 f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
 return {"status": "success", "report": report}




root_agent = Agent(
 name="weather_time_agent",
 model="gemini-2.5-flash",
 description=(
 "Agent to answer questions about the time and weather in a city."
    ),
 instruction=(
 "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
 tools=[get_weather, get_current_time],
)
```

The agent defines two tools: `get_weather` and `get_current_time`. Notice how each function includes comprehensive docstrings with type hints — ADK uses these to help the LLM understand when and how to invoke each tool. The root\_agent variable is the entry point that ADK’s deployment command will look for.

Create the `requirements.txt` file:

```
google-adk
```

Your project structure should now look like this:

`requirements.txt  
weather_time/  
├── __init__.py  
├── agent.py`

## Step 3: Testing Locally

Before deploying to Cloud Run, it’s essential to verify that your agent works correctly in the local environment. Create a .env file in your project’s root directory:

```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

Replace the placeholder with your actual Google AI Studio API key.

Navigate to the parent directory and run the agent locally:

```
cd ..
adk run weather_time
```

Test the agent with prompts like:

`[user]: What's the weather in New York?  
[user]: What time is it in New York?`

Once you’ve confirmed the agent responds correctly, exit the local session by typing `exit`. We’re now ready to deploy to Cloud Run.

## Step 4: Configuring Google Cloud Secrets

Production deployments should never hardcode API keys. Google Secret Manager provides secure storage and access control for sensitive credentials. Let’s store our API key there.

First, set the environment variables for your Google Cloud project:

```
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

Create the secret from your API key:

```
echo $GOOGLE_API_KEY | \
    gcloud secrets create GOOGLE_API_KEY \
        --project=$GOOGLE_CLOUD_PROJECT \
        --data-file=-
```

The Cloud Run service account needs permission to access this secret. Grant the Secret Accessor role:

```
gcloud secrets add-iam-policy-binding GOOGLE_API_KEY \
    --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor" \
    --project=$GOOGLE_CLOUD_PROJECT
```

Replace PROJECT\_NUMBER with your actual Google Cloud project number. You can find this in the Google Cloud Console or by running:

```
gcloud projects describe $GOOGLE_CLOUD_PROJECT --format="value(projectNumber)"
```

## Step 5: Deploying to Cloud Run

With secrets configured, we’re ready to deploy. Set up the deployment variables:

```
export AGENT_PATH="./weather_time"
export SERVICE_NAME="weather-time"
export APP_NAME="weather_time_app"
```

Execute the deployment command:

```
adk deploy cloud_run \
    --project=$GOOGLE_CLOUD_PROJECT \
    --region=$GOOGLE_CLOUD_LOCATION \
    --service_name=$SERVICE_NAME \
    --app_name=$APP_NAME \
    --with_ui \
    $AGENT_PATH
```

Let’s break down these parameters:

| **Parameter** | **Purpose** |
| --- | --- |
| project | Specifies the Google Cloud project for deployment |
| region | Sets the Cloud Run region (us-central1, europe-west1, etc.) |
| service\_name | Names the Cloud Run service |
| app\_name | Internal application name for the ADK API server |
| with\_ui | Includes the ADK web UI for interactive testing |

During deployment, you may be prompted about unauthenticated access. For initial testing, you can allow it (y); but for production deployments, requiring authentication (N) is recommended.

The deployment process takes a few minutes. Upon completion, you’ll see output similar to:

`Deployment successful!  
Service URL: https://weather-time-xxxxx.us-central1.run.app`

## Step 6: Testing the Deployed Agent

Open the Service URL in your browser. Because you included the `--with_ui` flag, you’ll see the ADK developer interface. This is the same UI you used during local development, now running on Cloud Run.

Enable “Token Streaming” in the upper-right to improve responsiveness. You can now interact with your deployed agent:

`[user]: Hello! What's the weather like in New York today?`  
The agent should respond using the get\_weather tool, returning the weather information for New York.

Try a follow-up:

`[user]: And what time is it there?`  
The agent will invoke the get\_current\_time tool to provide the current time in New York’s timezone.

## Cleaning Up

To avoid incurring future charges, delete the Cloud Run service when you’re done experimenting:

```
gcloud run services delete $SERVICE_NAME \
    --region=$GOOGLE_CLOUD_LOCATION \
    --quiet
```

You may also want to delete the secret:

```
gcloud secrets delete GOOGLE_API_KEY \
    --project=$GOOGLE_CLOUD_PROJECT \
    --quiet
```

## Looking Ahead

This tutorial demonstrated the fastest path from a local ADK agent to a production Cloud Run deployment. The adk deploy cloud\_run command abstracts away containerization complexity, allowing you to focus on agent logic while leveraging Cloud Run’s serverless scalability.

In subsequent tutorials, we’ll explore advanced deployment scenarios; including connecting ADK agents to MCP servers for external tool integration, implementing session persistence with Cloud SQL, deploying multi-agent systems with Sequential and Parallel orchestration patterns, and configuring GPU-accelerated backends for running open models like Gemma.

The foundation you’ve built here — understanding the deployment workflow, managing secrets securely, and testing with the web UI — will serve you well as we tackle increasingly sophisticated production architectures. Stay tuned!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)