当我第一次听说 [AWS Bedrock Flows](https://aws.amazon.com/bedrock/flows/) 时，我非常感兴趣。想象一下，通过拖放操作就能构建一个功能齐全的 AI 助手 —— 无需复杂的编码，无需处理基础设施的麻烦，只需纯粹地创造性地解决问题。这简直就像梦想成真，尤其是对于像我这样经常构建智能助手原型的人来说。

在本教程中，我将引导你了解我是如何使用 Amazon Bedrock Flows 构建一个简单的医疗保健助手的。该助手可以回答来自知识库的关于疾病的问题，并且可以使用连接到 [AWS Lambda](https://www.andela.com/blog-posts/configure-email-notifications-with-amazon-ses-lambda-and-dynamodb) 函数的代理来获取患者详细信息。

如果你对 [生成式 AI](https://www.andela.com/resources/tech-leaders-guide-to-getting-started-with-genai) 在医疗保健领域的实际应用感到好奇，或者你只是想以结构化和实际的方式亲身体验 [Amazon Bedrock](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/) Flows，那么这个项目非常适合你。

注意：用于构建此应用程序的数据是虚拟数据，并且是通过编程方式生成的。

## **你需要什么：工具和 AWS 服务**

首先，让我们准备好你的技术栈。以下是我用于构建这个项目的工具：

## **我们的用例概述**

我们的目标是创建一个可以进行对话的助手，它可以：

1.  根据 ID 检索患者数据（例如“患者 123 的状况如何？”）
2.  提供有关疾病的信息（“疟疾的症状是什么？”）

真实世界的例子：

*   **医生**：“告诉我关于患者 456 的信息。”
*   **助手**：“患者 456 状况稳定，被诊断患有疟疾。”
*   **医生**：“疟疾的症状是什么？”
*   **助手**：“常见症状包括发烧、发冷和肌肉酸痛。”

我们将通过结合 AI 代理（使用 Lambda 函数获取患者数据）和知识库（包含疾病内容）来实现这一点。

## **步骤 1：准备包含疾病数据的知识库**

### **1.1 上传到 S3**

将文件上传到你帐户中的 S3 存储桶。记下文件夹 URL，该 URL 将在创建知识库时使用。

[![S3 中的虚拟疾病数据。](https://cdn.thenewstack.io/media/2025/07/2c42dd95-image1a.jpg)](https://cdn.thenewstack.io/media/2025/07/2c42dd95-image1a.jpg)

S3 中的虚拟疾病数据。

### **1.2 创建知识库**

1.  转到 Amazon Bedrock > 知识库
2.  单击**创建知识库**。
3.  选择带有向量存储的知识库。
4.  将其命名为 `knowledge-base-dummy-disease-data`。
5.  对于 IAM 权限，选择**创建**并使用新的服务角色。
6.  选择 Amazon S3 作为查询引擎，然后单击**下一步**。
7.  命名你的数据源，然后选择 S3 中你保存数据文件的文件夹，然后单击**下一步**。
8.  选择一个嵌入模型。我正在使用 Amazon Titan Text Embeddings V2。
9.  选择一个向量存储。我正在使用 Amazon Aurora PostgreSQL。Serverless 可以节省成本；单击**下一步**。
10. 检查并单击**创建知识库**。根据文件大小，这可能需要几分钟。
11. 创建完成后，转到知识库，选择数据源名称，然后单击**数据源**选项卡上的**同步**按钮。这很重要；否则数据可能不可见。

    [![知识库同步按钮。](https://cdn.thenewstack.io/media/2025/07/747628b2-image2a.jpg)](https://cdn.thenewstack.io/media/2025/07/747628b2-image2a.jpg)

    知识库同步按钮。
12. 单击右上角的**测试知识库**。选择模型（我正在使用 Amazon Nova Lite）并测试查询，例如：
    *   “COVID-19 的症状是什么？”

##

## **步骤 2：创建代理以处理患者数据和知识库查询**

### **2.1 创建 DynamoDB 表并加载数据**

转到 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 控制台中的 DynamoDB 服务，创建一个名为 `DummyPatientTable` 的表并执行以下脚本。将 AWS 凭证保存在 .env 文件中或作为环境变量。

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

检查 DynamoDB 中创建的数据。数据将如下所示：

[![DynamoDB 患者数据](https://cdn.thenewstack.io/media/2025/07/366b100d-image4a.jpg)](https://cdn.thenewstack.io/media/2025/07/366b100d-image4a.jpg)

DynamoDB 患者数据

### **2.2 创建代理**

1.  转到 Amazon Bedrock > 代理。
2.  单击**创建代理**。
3.  将其命名为 `get-patient-data-dynamodb`。
4.  选择**创建**并使用新的服务角色。
5.  对于模型，选择 Amazon Nova Micro，或者你可以选择任何 Amazon Nova 模型。
6.  对于说明，请编写以下内容：

```
When the user submits a query, determine whether they are asking for patient-specific information (based on a patient ID or number) or general disease-related information.

If the query includes a patient ID (e.g., a number), call the `get_patient_record` function from the PatientRecords action group. The `patient_id` is the same as the `patient_record` identifier.

If a matching record is found, return the patient's details in a clear, formatted manner — with each attribute (ID, condition, status) on its own line.

If no record is found, respond with: “No record exists for that patient.”

Always return available information without asking for confirmation.
If the query is about a disease or symptoms (such as COVID-19, asthma), fetch the answer from the linked Knowledge Base.

Use best judgment to interpret the query. Do not prompt the user for clarification. Always respond with the most relevant information based on what is available.
```

1.  添加一个动作组，其中包含一个像 `PatientRecords` 这样的动作。
2.  选择动作组类型`Define with` [功能详情并创建一个新的 Lambda](https://thenewstack.io/what-are-python-lambda-functions-and-how-do-you-use-them/) 函数。
3.  选择 `get_patient_record` 作为动作组函数。
4.  将 `patient_id` 设置为输入槽。
5.  保存它。

### **2.3 Lambda 函数的代码**

1.  打开新创建的 Lambda 函数并添加以下代码：

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

### **2.4 将知识库附加到代理**

在这里，我们可以选择是单独使用 Amazon Bedrock Flows 中的知识库，还是将其附加到代理并让代理做出选择。这取决于我们的用例。通常，如果 AI 工作流程不复杂，我们可以附加它或保持它分离。我正在将知识库附加到代理。

在代理中，转到知识库选项卡并添加你的知识库。

[![知识库](https://cdn.thenewstack.io/media/2025/07/c1a22b17-image5a.jpg)](https://cdn.thenewstack.io/media/2025/07/c1a22b17-image5a.jpg)

知识库

### **2.5 测试代理**

单击**准备**按钮，然后从左侧面板测试代理：

尝试：

*   “患者 123 的状况如何？”—— 它将使用 Lambda 函数从 DynamoDB 获取数据。
*   “COVID-19 的症状是什么？”—— 它将从知识库获取数据。

[![](https://cdn.thenewstack.io/media/2025/07/e65edd29-image6a.jpg)](https://cdn.thenewstack.io/media/2025/07/e65edd29-image6a.jpg)

## **步骤 3：构建 Amazon Bedrock Flows**

现在我们将所有内容整合到 Amazon Bedrock Flows 中。

### **3.1 创建 Flow**

1.  转到 Amazon Bedrock 并单击 **Flows**。
2.  单击**创建 Flow** 并选择一个有意义的名称。将打开一个可视化构建器，其中包含输入、输出和提示节点。
3.  添加一个代理节点。
4.  现在单击 **Prompt Node**，选择 **Define in node**，选择一个模型（例如 Amazon Nova Lite），并在提示中添加：
    `Analyze the user input: {{input}}. If it contains any number, treat that number as a patient ID and pass the full input to the agent to retrieve patient information. If the input appears to be asking about a disease, symptoms or treatment, pass it to the agent to fetch disease-related information. Do not ask the user for clarification. Use your best judgment to decide the intent based on the input and route it accordingly.`
5.  现在单击代理节点，选择你的代理和别名。
6.  保存 flow。

[![Amazon Bedrock Flows](https://cdn.thenewstack.io/media/2025/07/f8f9484b-image7a.jpg)](https://cdn.thenewstack.io/media/2025/07/f8f9484b-image7a.jpg)

Amazon Bedrock Flows

### **3.2 测试输出**

通过提问来测试 flow：

尝试：

*   “患者 123 的状况如何？”
*   “COVID-19 的症状是什么？”

[![测试 Flows](https://cdn.thenewstack.io/media/2025/07/ec99f558-image8a.jpg)](https://cdn.thenewstack.io/media/2025/07/ec99f558-image8a.jpg)

测试 Flows

### **3.3 发布、版本控制和别名**

保存并退出 flow，然后单击发布以创建新版本。导航到别名部分并创建一个链接到此版本的别名。别名允许你在生产环境中切换不同版本，而无需更改代码，从而为已部署的代理提供无缝的版本管理。

## **步骤 4：创建一个 Streamlit 应用程序**

构建一个 Streamlit 应用程序，该应用程序 [与你的 Amazon Bedrock Flows 集成](https://thenewstack.io/build-a-qa-application-with-amazon-bedrock-and-amazon-titan/)，以便为与你的 AI 医疗代理进行交互提供直观的用户界面。

将以下代码另存为 `streamlit-bedrock-flow.py`。

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

从环境变量中读取 AWS 凭证、`FLOW_ID`、`FLOW_ALIAS_ID`。

使用 `streamlit run streamlit-bedrock-flow.py` 执行代码。

该应用程序将如下所示：

[![Streamlit 应用程序](https://cdn.thenewstack.io/media/2025/07/76ea7e8e-image9a.jpg)](https://cdn.thenewstack.io/media/2025/07/76ea7e8e-image9a.jpg)

Streamlit 应用程序

## **医疗保健 AI，简化**

我们刚刚在几个小时内构建了一个复杂的 AI 医疗保健助手，而不是几个月。Amazon Bedrock Flows 将过去需要复杂编码的东西转变为简单的拖放过程。

这里有一个更大的图景，在医疗保健之外。这些相同的模式适用于法律研究、财务咨询、教育和客户服务。我们正在进入一个构建 AI 应用程序就像创建网站一样容易的时代。这意味着下一个突破可能来自小型诊所或个体从业者，而不是通常的科技巨头，因为现在任何具有领域专业知识和合适的科技专家的人都可以构建他们需要的 AI 工具。

了解如何使用 [Andela 的逐步指导式工作流程指南](https://www.andela.com/blog-posts/building-autonomous-systems-in-python-with-agentic-workflows/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=agentic-ai-worksflows&utm_term=writers-room) 构建能够自主思考、适应和执行任务的智能 Python 系统。

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

群组
使用 Sketch 创建。

[![](https://cdn.thenewstack.io/media/2025/07/95c8a49a-cropped-1f216739-hafiz-hassan.jpeg)

Hafiz Hassan 是一名位于吉隆坡的数据工程师，也是 Andela 的技术专家。Hafiz 拥有超过五年的为全球客户打造解决方案的经验，他对数据工程、Web 开发、DevOps、数据仓库、数据湖充满热情……

阅读更多 Hafiz Hassan 的文章](https://thenewstack.io/author/hafiz-hassan/)
