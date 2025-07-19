When I first heard about [AWS Bedrock Flows](https://aws.amazon.com/bedrock/flows/), I was intrigued. Imagine dragging and dropping your way to a fully functional AI assistant — no complex coding, no infrastructure headaches, just pure creative problem-solving. It’s like a dream come true, especially for someone like me who often prototypes intelligent assistants.

In this tutorial, I’ll walk you through how I built a simple health care assistant using Amazon Bedrock Flows. The assistant can answer questions about diseases from a knowledge base, and it can fetch patient details using an agent connected to an [AWS Lambda](https://www.andela.com/blog-posts/configure-email-notifications-with-amazon-ses-lambda-and-dynamodb) function.

This project is perfect if you’re curious about real-world applications of [generative AI](https://www.andela.com/resources/tech-leaders-guide-to-getting-started-with-genai) in health care, or if you just want to get hands-on with [Amazon Bedrock](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/) Flows in a structured and practical way.

NOTE: The data used to build this application is dummy and has been generated programmatically.

## **What You’ll Need: Tools and AWS Services**

To begin, let’s get your tech stack ready. Here’s what I used to build this project:

## **Our Use Case Overview**

Our goal is to create a conversational assistant that can:

1. Retrieve patient data based on an ID (such as “What is the condition of patient 123?”)
2. Provide information about diseases ( “What are the symptoms of malaria?”)

Real-world example:

* **Doctor**: “Tell me about patient 456.”
* **Assistant**: “Patient 456 is stable and diagnosed with malaria.”
* **Doctor**: “What are the symptoms of malaria?”
* **Assistant**: “Common symptoms include fever, chills and muscle aches.”

We’ll achieve this by combining an AI agent (with Lambda function for patient data) and a Knowledge Base (with disease content).

## **Step 1: Prepare the Knowledge Base with Disease Data**

### **1.1 Upload to S3**

Upload the files to an S3 bucket in your account. Keep note of the folder URL that will be used while creating the Knowledge Base.

[![Dummy disease data in S3.](https://cdn.thenewstack.io/media/2025/07/2c42dd95-image1a.jpg)](https://cdn.thenewstack.io/media/2025/07/2c42dd95-image1a.jpg)

Dummy disease data in S3.

### **1.2 Create the Knowledge Base**

1. Go to Amazon Bedrock > Knowledge Bases
2. Click **Create knowledge base**.
3. Choose Knowledge Base with Vector Store.
4. Name it `knowledge-base-dummy-disease-data`.
5. For IAM permissions, choose **Create** and use a new service role.
6. Choose Amazon S3 as the query engine and click **Next**.
7. Name your data source and choose the folder from S3 where you have kept the data files and click **Next**.
8. Choose an embedding model. I am using Amazon Titan Text Embeddings V2.
9. Select a vector store. I am using Amazon Aurora PostgreSQL. Serverless to save cost; click **Next**.
10. Review and click **Create Knowledge Base**. It can take a few minutes depending on the file size.
11. Once created, go to Knowledge Base, choose the data source name and click on the **Sync** button on the **Data Source** tab. It is important; otherwise the data may not be visible.

    [![Knowledge Base Sync button.](https://cdn.thenewstack.io/media/2025/07/747628b2-image2a.jpg)](https://cdn.thenewstack.io/media/2025/07/747628b2-image2a.jpg)

    Knowledge Base Sync button.
12. Click on **Test Knowledge Bas**e from top right. Choose model (I am using Amazon Nova Lite) and test queries like:
    * “What are the symptoms of COVID-19?”

## 

## **Step 2: Create the Agent To Handle Patient Data and the Knowledge Base Queries**

### **2.1 Create DynamoDB Table and Load Data**

Go to DynamoDB service in the [AWS](https://aws.amazon.com/?utm_content=inline+mention) console and create a table named `DummyPatientTable` and execute the below script. Keep the AWS credentials in an .env file or as an environmental variable.

```
import boto3
import random
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os


# Load AWS credentials from .env file
load_dotenv()
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region_name = os.getenv("AWS_REGION", "us-east-1")


# Create DynamoDB resource
dynamodb = boto3.resource(
   'dynamodb',
   aws_access_key_id=aws_access_key_id,
   aws_secret_access_key=aws_secret_access_key,
   region_name=region_name
)


# Reference the table
table = dynamodb.Table('DummyPatientTable')


# Sample values for policy types and conditions
policy_types = ['Basic', 'Premium', 'Platinum']
conditions = ['Diabetes', 'Hypertension', 'Asthma', 'Healthy', 'Alzheimer\'s Disease', 'Fibromyalgia', 'Arthritis', 'Stroke', 'Kidney Disease', 'High Blood Pressure', 'Heart Disease']
statuses = ['active', 'inactive', 'pending']


# Generate and insert mock data
for patient_id in range(1, 201):  # Generates patients records from 1 to 200
   item = {
       'patient_id': patient_id,
       'policy_type': random.choice(policy_types),
       'status': random.choice(statuses),
       'condition': random.choice(conditions),
       'last_activity_date': (datetime.today() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
   }


   response = table.put_item(Item=item)
   print(f"Inserted patient_id {patient_id}: {response['ResponseMetadata']['HTTPStatusCode']}")
```

Check the DynamoDB for the created data. The data will look like this:

[![DynamoDB patient data](https://cdn.thenewstack.io/media/2025/07/366b100d-image4a.jpg)](https://cdn.thenewstack.io/media/2025/07/366b100d-image4a.jpg)

DynamoDB patient data

### **2.2 Create the Agent**

1. Go to Amazon Bedrock > Agents.
2. Click **Create Agent**.
3. Name it `get-patient-data-dynamodb`.
4. Choose **Create** and use a new service role.
5. For model, select Amazon Nova Micro or you can choose any Amazon Nova model.
6. For instructions, write this:

```
When the user submits a query, determine whether they are asking for patient-specific information (based on a patient ID or number) or general disease-related information.

If the query includes a patient ID (e.g., a number), call the `get_patient_record` function from the PatientRecords action group. The `patient_id` is the same as the `patient_record` identifier.

If a matching record is found, return the patient's details in a clear, formatted manner — with each attribute (ID, condition, status) on its own line.

If no record is found, respond with: “No record exists for that patient.”

Always return available information without asking for confirmation.
If the query is about a disease or symptoms (such as COVID-19, asthma), fetch the answer from the linked Knowledge Base.

Use best judgment to interpret the query. Do not prompt the user for clarification. Always respond with the most relevant information based on what is available.
```

1. Add an action group with an action like `PatientRecords`.
2. Choose action group type`Define with` [Function Details and create a new Lambda](https://thenewstack.io/what-are-python-lambda-functions-and-how-do-you-use-them/) function.
3. Choose `get_patient_record` as action group function.
4. Set `patient_id` as an input slot.
5. Save it.

### **2.3 Code for Lambda Function**

1. Open the newly created Lambda function and add the code below:

```
import json
import boto3
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DummyPatientTable') 

def patient_detail(payload):
   try:
       patient_id = int(payload['parameters'][0]['value'])


       # Query the DynamoDB table for the patient ID
       resp = table.query(
           KeyConditionExpression=Key('patient_id').eq(patient_id)
       )

       if resp['Items']:
           return {
               "status": "success",
               "data": resp['Items'][0]
           }
       else:
           return {
               "status": "error",
               "message": "No record found"
           }
   except Exception as e:
       return {
           "status": "error",
           "message": str(e)
       }

def lambda_handler(event, context):
   response_body = patient_detail(event)

   function_response = {
       'responseBody': {
           'TEXT': {
               'body': json.dumps(response_body)
           }
       }
   }

   action_response = {
       'messageVersion': '1.0',
       'response': {
           'actionGroup': event['actionGroup'],
           'function': event['function'],
           'functionResponse': function_response
       },
       'sessionAttributes': event.get('sessionAttributes', {}),
       'promptSessionAttributes': event.get('promptSessionAttributes', {})
   }
   return action_response
```

### **2.4 Attach the Knowledge Base With the Agent**

Here, we have a choice either to use the Knowledge Base separately from Amazon Bedrock Flows or attach it to the agent and let the agent make the choice. It depends on our use case. Usually, if the AI workflow is not complex, we can attach it or keep it separate. I am attaching the Knowledge Base with the agent.

In the agent, go to the Knowledge Base tab and add your Knowledge Base.

[![Knowledge Base](https://cdn.thenewstack.io/media/2025/07/c1a22b17-image5a.jpg)](https://cdn.thenewstack.io/media/2025/07/c1a22b17-image5a.jpg)

Knowledge Base

### **2.5 Test the Agent**

Click the button **Prepare** and then test the agent from the left panel:

Try:

* “What is the condition of patient 123?” — It will fetch data from DynamoDB using the Lambda function.
* “What are the symptoms of COVID-19.” — It will fetch data from the Knowledge Base.

[![](https://cdn.thenewstack.io/media/2025/07/e65edd29-image6a.jpg)](https://cdn.thenewstack.io/media/2025/07/e65edd29-image6a.jpg)

## **Step 3: Build the Amazon Bedrock Flows**

Now we bring it all together in the Amazon Bedrock Flows.

### **3.1 Create a Flow**

1. Go to Amazon Bedrock and click **Flows**.
2. Click **Create Flow** and choose a meaningful name. A visual builder will open having input, output and prompt nodes.
3. Add an agent node.
4. Now click on **Prompt Node**, choose **Define in node**, choose a model like Amazon Nova Lite and in the prompt you can add:  
   `Analyze the user input: {{input}}. If it contains any number, treat that number as a patient ID and pass the full input to the agent to retrieve patient information. If the input appears to be asking about a disease, symptoms or treatment, pass it to the agent to fetch disease-related information. Do not ask the user for clarification. Use your best judgment to decide the intent based on the input and route it accordingly.`
5. Now click on the agent node, select your agent and alias.
6. Save the flow.

[![Amazon Bedrock Flows](https://cdn.thenewstack.io/media/2025/07/f8f9484b-image7a.jpg)](https://cdn.thenewstack.io/media/2025/07/f8f9484b-image7a.jpg)

Amazon Bedrock Flows

### **3.2 Test the Output**

Test the flow by asking questions:

Try:

* “What is the condition of patient 123?”
* “What are the symptoms of COVID-19?”

[![Test flows](https://cdn.thenewstack.io/media/2025/07/ec99f558-image8a.jpg)](https://cdn.thenewstack.io/media/2025/07/ec99f558-image8a.jpg)

Test Flows

### **3.3 Publishing, Versioning and Alias**

Save and exit the flow, then click publish to create a new version. Navigate to the Alias section and create an alias that links to this version. Aliases allow you to switch between different versions in production environments without requiring code changes, providing seamless version management for your deployed agent.

## **Step 4: Create a Streamlit App**

Build a Streamlit application that [integrates with your Amazon Bedrock Flows](https://thenewstack.io/build-a-qa-application-with-amazon-bedrock-and-amazon-titan/) to provide an intuitive user interface for interacting with your AI health agent.

Save the below code as `streamlit-bedrock-flow.py`.

```
import json
import boto3
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region_name = os.getenv("AWS_REGION", "us-east-1")
FLOW_ID = os.getenv("FLOW_ID")
FLOW_ALIAS_ID = os.getenv("FLOW_ALIAS_ID")

# Initialize Streamlit app
st.title("Amazon Bedrock Flow integration")

# Initialize session state
if 'execution_id' not in st.session_state:
   st.session_state.execution_id = None
if 'input_required' not in st.session_state:
   st.session_state.input_required = None

# Create input format for Bedrock flow
def create_input_data(text, node_name="FlowInputNode", is_initial_input=True):
   data = {
       "content": {"document": text},
       "nodeName": node_name
   }
   if is_initial_input:
       data["nodeOutputName"] = "document"
   else:
       data["nodeInputName"] = "agentInputText"
   return data

# Invoke Bedrock Flow
def invoke_flow(client, flow_id, flow_alias_id, input_data, execution_id=None):
   request = {
       "flowIdentifier": flow_id,
       "flowAliasIdentifier": flow_alias_id,
       "inputs": [input_data],
       "enableTrace": True
   }
   if execution_id:
       request["executionId"] = execution_id

   response = client.invoke_flow(**request)

   flow_status = ""
   input_required = None
   execution_id = response.get('executionId', execution_id)

   for event in response['responseStream']:
       if 'flowCompletionEvent' in event:
           flow_status = event['flowCompletionEvent']['completionReason']
       elif 'flowMultiTurnInputRequestEvent' in event:
           input_required = event
       elif 'flowOutputEvent' in event:
           st.subheader("Response:")
           st.write(event['flowOutputEvent']['content']['document'])

   return {
       "flow_status": flow_status,
       "input_required": input_required,
       "execution_id": execution_id
   }

# Create Boto3 client
session = boto3.Session(
   aws_access_key_id=aws_access_key_id,
   aws_secret_access_key=aws_secret_access_key,
   region_name=region_name
)
client = session.client('bedrock-agent-runtime')

# Input section
if st.session_state.input_required:
   prompt = st.session_state.input_required['flowMultiTurnInputRequestEvent']['content']['document']
   user_input = st.text_input("Additional Info:", value=prompt)
else:
   user_input = st.text_input("Ask your question:")

# Submit button
if st.button("Submit"):
   if user_input:
       with st.spinner("Processing..."):
           if st.session_state.execution_id is None:
               input_data = create_input_data(user_input, is_initial_input=True)
           else:
               node_name = st.session_state.input_required['flowMultiTurnInputRequestEvent']['nodeName']
               input_data = create_input_data(user_input, node_name=node_name, is_initial_input=False)

           result = invoke_flow(client, FLOW_ID, FLOW_ALIAS_ID, input_data, st.session_state.execution_id)

           if result:
               st.session_state.execution_id = result['execution_id']
               if result['flow_status'] == "INPUT_REQUIRED":
                   st.session_state.input_required = result['input_required']
               else:
                   st.success("Flow completed.")
                   st.session_state.execution_id = None
                   st.session_state.input_required = None
   else:
       st.warning("Please enter something.")
```

Read the AWS credentials, `FLOW_ID`, `FLOW_ALIAS_ID` from the environment variables.

Execute the code with `streamlit run streamlit-bedrock-flow.py`.

The app will look like this:

[![Streamlit app](https://cdn.thenewstack.io/media/2025/07/76ea7e8e-image9a.jpg)](https://cdn.thenewstack.io/media/2025/07/76ea7e8e-image9a.jpg)

Streamlit app

## **Health Care AI, Simplified**

We’ve just built a sophisticated AI health care assistant in hours instead of months. Amazon Bedrock Flows transforms what used to require complex coding into a simple drag-and-drop process.

There’s a bigger picture here, outside of health care. These same patterns work for legal research, financial advisory, education and customer service. We’re entering an age where building AI applications is as easy as creating a website. And it means that the next breakthrough might come from a small clinic or individual practitioner rather than the usual tech giant, because now anyone with domain expertise and the right tech experts on hand can build the AI tools they need.

Discover how to build intelligent Python systems that think, adapt, and execute tasks autonomously with [Andela’s step-by-step agentic workflow guide.](https://www.andela.com/blog-posts/building-autonomous-systems-in-python-with-agentic-workflows/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=agentic-ai-worksflows&utm_term=writers-room)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/95c8a49a-cropped-1f216739-hafiz-hassan.jpeg)

Hafiz Hassan is a data engineer based in Kuala Lumpur and a technologist for Andela. With more than five years of experience crafting solutions for global clients, Hafiz is passionate about data engineering, web development, DevOps, data warehousing, data lake,...

Read more from Hafiz Hassan](https://thenewstack.io/author/hafiz-hassan/)