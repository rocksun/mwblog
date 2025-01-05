# Build a Serverless Todo App With AWS, Pulumi and Python
![Featued image for: Build a Serverless Todo App With AWS, Pulumi and Python](https://cdn.thenewstack.io/media/2024/12/51386296-todo-list-app-aws-pulumi-python-1024x576.jpg)
Developers charged with building modern, scalable applications often face the burden of having to learn new skills, but there are alternatives that can speed and simplify their work. This tutorial provides a practical, hands-on guide to deploying a serverless app that’s accessible through a RESTful API. Following along will give you valuable skills in serverless architecture, Infrastructure as Code (IaC) and API development, empowering you to create efficient and cost-effective solutions.

In this tutorial, I’ll walk through a step-by-step process for creating a serverless application using Amazon Web Services ([AWS](https://aws.amazon.com/?utm_content=inline+mention)) Lambda, [Docker](https://www.docker.com/?utm_content=inline+mention) and AWS API Gateway, all orchestrated with [Pulumi](https://thenewstack.io/from-iac-to-cloud-management-pulumis-evolution-story/) using Python. By the end of this guide, you’ll have a deployed serverless application that can be accessed via a RESTful API.

## Why Use Pulumi and Serverless for This Project?
Pulumi is an open source [Infrastructure as a Code](https://thenewstack.io/infrastructure-as-code/) (IaC) tool that allows developers to define and manage infrastructure using their favorite programming language, including [TypeScript](https://roadmap.sh/typescript), [JavaScript](https://roadmap.sh/javascript), [Python](https://thenewstack.io/python/), [Go](https://thenewstack.io/introduction-to-go-programming-language/) or [C#](https://thenewstack.io/c-logging-key-considerations-with-net/).

By using Pulumi to create AWS Lambda, Docker and API Gateway services, developers can leverage their existing knowledge to build and deploy a highly scalable serverless solution that can handle traffic without needing additional tools to create infrastructure.

Serverless computing allows developers to manage and run application code without the need to provision or manage servers. By using this model, developers can focus mainly on their application code without worrying about the underlying infrastructure.

AWS API Gateway is a fully managed service that helps developers secure APIs. It also handles rate limiting, routing and scaling API requests. AWS Lambda is a serverless computing service that allows developers to run code without the need to provision or manage servers.

## Project Overview
The todo app will have the following features:

- Create a Todo: This action will add a todo list.
- Read a Todo: This action will read a todo list.
- Update Todo: This action will update a todo list.
- Delete Todo: This action will delete a todo list.
Now that you know what the project will do, follow this step-by-step guide on using Python to create a serverless todo application using Docker, API Gateway, AWS Lambda, Pulumi and Python.

## Get Started
To begin, ensure you have done the following on your development machine.

- Install the
[Pulumi command-line interface (CLI)](https://www.pulumi.com/docs/get-started/install/) - Install
[Python 3.7](https://www.python.org/downloads/)or later. - Install the
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). - If you don’t already have an AWS account, set one up.
- Configure the AWS CLI with your credentials to manage your AWS services.
### Step 1: Install Pulumi
First, ensure you have Pulumi installed in your development environment. Pulumi can be installed on Linux, macOS or Windows:

- On Linux:
`curl -fsSL https://get.pulumi.com | sh`
- On macOS (using Brew):
`brew install pulumi/tap/pulumi`
- On Windows: Download and run the
[Pulumi installer](https://www.pulumi.com/docs/install/)(or try one of the other methods on that page).
### Step 2: Set Up Your Environment
Next, set up your environment and install the Python dependencies if necessary. Follow the steps for instructions on how to set up your environment.

[Create a Pulumi account](https://app.pulumi.com/signup?utm_source=header-button)to store your stack state, if you want to use Pulumi for state management.- Install dependencies: Install Python and
`pip`
on your workstation, since you will use Python to provision infrastructure.
### Step 3: Create a New Pulumi Project
Create a folder called `todo_pulumi_docker_aws_lambda_api_gateway`
and create another folder for the Lambda project `todo-app`
.

Initialize a new Pulumi project by running:

Follow the prompts to set up your project.

### Step 4: Install Dependencies
Create a `requirements.txt`
file in the project root `todo-app`
folder with the following content:

Then install the dependencies by running:

`pip3 install -r requirements.txt`
### Step 4: Create Your Lambda Function
Create a folder called `lambda_function`
; this will contain the Lambda code and a file named `lambda.py`
.

### Step 5: Create a Dockerfile
Create a file named `Dockerfile`
inside the `lambda_function`
directory.

### Step 6: Create a GitHub Action to Push the Docker Image to AWS
Create a file named `docker-publish.yml`
in the folder `.github/workflows.`
This file will contain the GitHub Actions code to publish and push the Docker image to the AWS Elastic Container Registry (ECR).

Add the following `secrets`
to the repository.

See the screenshot below for an example:

Here is the workflow to deploy the Docker Image to AWS ECR:

### Step 7: Create a GitHub Action to Run and Deploy the Pulumi Code
Create a token from [pulumi.com](https://pulumi.com/); it will be used in GitHub Actions to utilize Pulumi for state management. Then use the newly created secret in GitHub as your `PULUMI_ACCESS_TOKEN`
.

Create a file named `pulumi-deploy.yml`
in the folder `.github/workflows`
. It will contain the GitHub Actions code to deploy the infrastructure code on AWS.

You can find the Lambda function code in `todo-app/lambda_function`
. It contains the Lambda function code in Python and the following resource endpoints. It uses DynamoDB to keep track of the todo list.

**GET Endpoint**uses the resource`/todos`
with the method`GET`
.**POST Endpoint**uses the resource`/todos`
with the method`POST`
.**DELETE Endpoint**uses the resource`/todos/<id>`
with the method`DELETE`
.**PATCH Endpoint**uses the resource`/todos/<id>`
with the method`PATCH.`
### Step 8: Create the Pulumi Code to Spin Up the Infrastructure
Create a file called `_main_.py`
in the `todo-app`
folder; it will contain the infrastructure code for spinning up the infrastructure. The Pulumi code will create the following resources on AWS.

**API-Gateway:**Defines the`API Gateway`
and its associated`root_resource`
, linking it to the`Lambda function`
.**Lambda-function:**This is a Dockerized Lambda function created using a Docker image`(image_uri)`
.**IAM-Roles:**This is the identity and access management (IAM) role attached to the Lambda function. It allows the Lambda function to assume role permissions and also contains permissions for it to access the[DynamoDB](https://thenewstack.io/dynamodb-when-to-move-out/).**Deployment:**This deploys the`API Gateway`
to the`dev`
stage.
The Pulumi code is designed to deploy into different environments, such as production and development. In this tutorial, you will be deploying to dev, and the config file for dev is in `Pulumi.dev.yaml`
.

The code for the Pulumi infrastructure resource is:

### Step 9: Test the Serverless Application
The API gateway connects to the Lambda function that contains the Python code in Lambda. To test the endpoint, you need to get its URL from the AWS console. Log in to AWS and navigate to the `API Gateway`
. You will see something like this:

To get the stage URL, which is used to access the serverless application from [Postman](https://thenewstack.io/new-postman-release-supports-ai-api-development-with-ai/), click on `my-api-dev`
. You can find it under “Invoke URL” in the screenshot below.

**Health endpoint:** The `health`
endpoint checks if the app is up and running.
**GET endpoint: **The `GET`
endpoint retrieves the list of the todos in the DynamoDB.
**POST endpoint: **The `POST`
endpoint creates a todo list in the DynamoDB.
**PATCH endpoint:** The `PATCH`
endpoint updates the todo list in the DynamoDB by supplying the ID.
**DELETE endpoint:** The `DELETE`
endpoint deletes the todo list in the DynamoDB by supplying the ID.
## Conclusion
You have successfully built and deployed a scalable, serverless todo app on AWS using AWS, API Gateway, Lambda, Docker, GitHub Actions and Pulumi. Pulumi makes it easier to manage Infrastructure as a Code (IaC) so that deployments are efficient, maintainable and faster. GitHub Actions automates the CI/CD pipeline deployment for seamless and reliable updates. At the same time, Docker in Lambda provides the flexibility to package your application and its dependencies into a container image. You can find the complete code for this project in [my GitHub repo](https://github.com/ExitoLab/todo_pulumi_docker_aws_lambda_api_gateway).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)