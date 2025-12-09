Things can unravel quickly when the right information doesn’t reach the right person at the right time. These moments turn chaotic when systems aren’t built to respond in real time. Automating this kind of experience requires more than just alerts or notifications; it requires connected data, smart flows and secure, time-sensitive decision-making.

This guide will walk you through building real-time decision-making systems using Salesforce Agentforce and Heroku AppLink. It will show how Agentforce’s AI-driven workflows respond to live events and how Heroku’s [AI Platform as a Service](https://thenewstack.io/what-is-an-ai-paas-a-guide-to-the-future-of-ai-development/) (PaaS) can extend those flows with customized actions and APIs. The result is a personalized experience that helps people confidently access the data they need to make decisions in the moment.

## What Is Salesforce Agentforce?

[Agentforce](https://thenewstack.io/avoiding-the-ai-agent-reliability-tax-a-developers-guide/) is an always-on application framework that leverages AI along with an organization’s Salesforce data to proactively execute tasks at scale. By intelligently using the data already in your [Salesforce](https://www.salesforce.com/data/?utm_content=inline+mention) ecosystem, Agentforce can build powerful automations that are better customized to your use cases. Since the AI that powers Agentforce is inside your Salesforce environment, you don’t need to be concerned about data security or it leaking customers’ private data.

One popular approach to working with AI agents is to build flows — workflows that the AI agents follow while processing and handling tasks automatically. Here is an example workflow:

[![An example of Agentforce flow.](https://cdn.thenewstack.io/media/2025/12/9491bfe2-agentforce-flow-architecture.png)](https://cdn.thenewstack.io/media/2025/12/9491bfe2-agentforce-flow-architecture.png)

An example of an Agentforce flow.

In this workflow, the agent is tasked with scheduling a meeting, and if there is availability, the agent will schedule a meeting for all the participants.

## Customizing Workflows With Agentforce and Heroku

There are many automation tools available in the marketplace, but sharing customer data across company boundaries produces opportunities for data to become compromised. Keeping the agentic AI inside Salesforce helps protect the security of companies’ data.

Many common functions are prebuilt, trained and included in Agentforce. Using these workflow tasks doesn’t require any coding; they can be added into the flow to speed iteration and construction of agentic flows. But companies often need customized flows for certain use cases or verticals.

This is where integrating Agentforce with Heroku becomes valuable. Heroku’s powerful AI PaaS can extend Agentforce workflows with customized actions and APIs that enable [fast and easy app](https://www.heroku.com/customers) deployment into the cloud. Heroku is part of the Salesforce family, and the tight integration of Salesforce and Heroku makes it easier to build Agentforce applications.

[Heroku AppLink](https://devcenter.heroku.com/articles/heroku-integration) exposes services built on Heroku’s [AI PaaS](https://www.heroku.com/blog/heroku-fir-generally-available-new-platform-capabilities/) as APIs to be used in Salesforce Agentforce flows. AppLink enforces Salesforce’s permissions and rules, ensuring that the data processed in the Heroku application remains secure in the Salesforce ecosystem.

## Build an AI Workflow

To see how it works, let’s build an air travel flow with Agentforce. When passengers land at their destination, they need to know where to go next. Here’s a flow that could be built in Agentforce:

* Get the passenger manifest for the flight.
* For each passenger, query the next steps. For simplicity, assume two options:
  + If the passenger has a connecting flight: Query flight tool for departure time/gate information details on the next flight.
  + If this is the passenger’s final destination: Get the baggage claim carousel number.
* For either process, estimate the walking time from the gate to the destination.
* Identify the direction: Will passengers turn left or right after exiting the jetway?
  + If there is time, upsell coffee along the way.
  + If there is not enough time, indicate that they should not delay.
* Look up the passenger’s phone number in Salesforce.
* Text each passenger customized details on their next steps to navigate the airport.

Rather than flight attendants announcing a dozen connections (that no one can hear anyway: “Flight 614 to Chicago will depart from gate <inaudible due to static>”) or passengers racing to the screens to find their next flight, the necessary information is calmly delivered to the passenger via text when the plane lands.

## Build the App

Now that we have the workflow, we can use it to build a customized application in Agentforce, using a customized Heroku app to power agentic AI and Heroku AppLink to expose your Heroku app as an API service in Salesforce.

### 1. Define the Data Sources

Let’s make a few assumptions about our data sources:

* All of the customer data is stored in Salesforce: name, address, mobile phone and email.
* Customer flight reservations are also stored in a Salesforce table and cross-indexed to the customer’s data.
  + If this data is in another data repository, it will require a little bit more processing, but the overall flow will be similar.
* There’s an existing dataset of all gates, baggage claims and important locations inside every airport, with approximate distances between locations.
  + The dataset of airport information was previously created and deployed in Heroku as an API.

### 2. Create the Data Flow

To kick off the data flow, we will use a [Heroku eventing](https://www.heroku.com/blog/heroku-eventing-router-for-your-events/) service. Heroku eventing is a pilot program that can be used to invoke Heroku applications — or in this case, an agentic flow. A Heroku app with eventing enabled behaves similarly to webhooks: services that listen for a specific event in the ecosystem. Another automated flow running during the flight process can fire a “landing” event as a flight progresses through the air. The application receives this event and starts running the flow.

When the flow begins, the agent retrieves the flight manifest for each passenger. It processes the flight manifest to obtain the arrival gate and each passenger’s next steps. It can run inside the Heroku application, or in a prebuilt agentic flow application that makes and processes SQL calls in Salesforce.

Once the passenger data is collected and parsed, we need to determine the walk time inside the airport. To obtain this information, we will build a customized application in Heroku that interacts with the flow.

### 3. Build the Heroku Application

Our Heroku application will be [exposed to Agentforce through AppLink](https://devcenter.heroku.com/articles/getting-started-heroku-applink-agentforce). AppLink turns your Heroku app into a custom API that works only inside the Salesforce ecosystem. Applications using AppLink are provisioned and securely connected to your Salesforce organization to ensure data integrity. This application can connect with multiple Salesforce organizations, but it must be provisioned in each organization individually.

Because this application is built on Heroku’s AI PaaS, the dev team does not need to manage any infrastructure or DevOps. It is all included in the box. This makes it easier for developers to adopt powerful, complex [cloud native technologies](https://thenewstack.io/cloud-native/ "cloud native technologies") such as Kubernetes.

Heroku-integrated apps must follow the [OpenAPI specifications](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) to be properly integrated. Let’s assume four pieces of data are sent into this API: `airport code`, `arrival gate`, `destination` and `time of next flight`.

Only the first three parameters are required (passengers heading to baggage claim will not have a `time of next flight`). Our application will contain an OpenAPI spec (often called a Swagger JSON) that will be consumed by the flow.

For each passenger on the flight, the Heroku application is called to process their trip through the airport. It might use [Google](https://cloud.google.com/?utm_content=inline+mention) Maps to time a walking trip or use an airport mapping service with real-time data. How the data is processed and evaluated is not critical here. What is important is that the Heroku application securely handles the airline’s customer data, so it never leaves the Salesforce organization.

The Heroku application’s output is data: How long of a walk the transfer will be, and a personalized note on how quickly the passenger needs to make the transfer. This will be returned as a JSON object to the Agentforce flow.

### 4. Complete the Flow

In the final step, the agent composes a short SMS message to the passenger. Using prompts, we can direct the agent to create an appropriate message welcoming each passenger and providing them with up-to-date information on the next steps in their travel.

If the AI determines that it is a tight connection, there could be encouragement not to delay.

“Welcome to New York JFK. Your connecting flight to Boston leaves Gate B10 at 3:20, and the boarding doors close at 3:00. It is a 10-minute walk. Please proceed to the gate immediately.”

If there is time, perhaps the AI could cross-sell a stop at a coffee shop along the way.

“Welcome to Chicago O’Hare! Your connecting flight to Cleveland leaves at 6:20 p.m. from Gate B12. That’s about a 15-minute walk, so you’ll have plenty of time.”

## Flying Is a Breeze

Using agentic flows inside Salesforce can help airlines make airport transfers a breeze. Using customer data from Salesforce and a customized Heroku AppLink integration, an agentic flow sends each passenger a customized text message upon landing. Private customer data never leaves the Salesforce ecosystem, and the customized Heroku application provides a personalized experience. With agentic flows in Agentforce, customers can be informed in real time of changes and how urgently they need to handle the change.

When AI agents can handle notifying customers of itinerary changes, airlines can focus on other parts of the customer experience, helping to make the entire travel experience less stressful for everyone.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/11/1c01c260-doug-sillars.jpg)

Doug is a lifelong learner and educator, having focused his career on improving developer knowledge and experiences.  A Google Developer Expert for the web, O’Reilly author, international keynote speaker, and a prolific blogger, he relishes in simplifying the complex. When...

Read more from Doug Sillars](https://thenewstack.io/author/doug-sillars/)