# KitOps Is the Open Source Tool That Turns DevOps Pipelines Into MLOps Pipelines
![Featued image for: KitOps Is the Open Source Tool That Turns DevOps Pipelines Into MLOps Pipelines](https://cdn.thenewstack.io/media/2024/06/797311cc-piplines-1024x575.png)
The marriage of
[machine learning](https://thenewstack.io/ai/) and DevOps practices has given birth to MLOps, a specialized field focused on automating the development, deployment and management of ML models in production environments. However, a major hurdle in achieving streamlined [MLOps](https://thenewstack.io/what-is-mlops/) workflows lies in the traditional separation between DevOps and machine learning pipelines.
This article explores
[KitOps](http://kitops.ml/), an open source project that bridges this gap by allowing you to leverage your existing DevOps pipelines for [MLOps](https://thenewstack.io/optimize-ai-at-scale-with-platform-engineering-for-mlops/) tasks through the use of ModelKits. A short walkthrough and code sample in the article will demonstrate how easy it is to get started.
## The Bottleneck of Separate Workflows
Building and deploying traditional applications typically follows a well-defined DevOps pipeline. Code undergoes version control, automated testing, and seamless integration and delivery. DevOps is an accepted and proven practice for deploying systems at scale. However, ML projects introduce new complexities. Models require specific data sets, training environments, configurations and monitoring tools. Data scientists may use
[Jupyter notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) and iterate on model refinement. Building separate MLOps pipelines to manage these aspects alongside existing DevOps pipelines leads to several inefficiencies: **Overlapping Efforts:**Maintaining separate pipelines means duplicating effort for tasks like version control, deployment and configuration management. Imagine managing a DevOps pipeline for application code and a separate MLOps pipeline for the trained model, its dependencies and configuration files. This redundancy increases overhead and introduces potential inconsistencies between the pipelines. **Siloed Teams:**Separate pipelines can lead to a siloed development environment, where DevOps and ML engineers work in isolation. Collaboration becomes fragmented, hindering communication and delaying deployments. Data scientists might struggle to understand deployment complexities, while DevOps engineers might lack knowledge of the specific needs of working with ML models. **Steeper Learning Curves:**Maintaining disparate MLOps pipelines requires engineers to learn and manage a broader set of tools, increasing the learning curve and delaying project adoption due to the inefficiencies in operations. This can be a significant barrier for organizations new to ML, slowing their ability to leverage its potential.
## Enter KitOps: Unifying Development With ModelKits
KitOps offers an elegant solution to these discrepancies by introducing the concept of ModelKits. ModelKits are standardized packages that encapsulate all the critical components of an ML project:
**Model:**The trained ML model itself, typically saved in a format like pickle or joblib as examples. **Datasets:**The data used for training and potentially for testing and validation. Depending on the model size and data privacy considerations, datasets might be included in the ModelKit or referenced as external locations. **Code:**The source code used for training, preprocessing the data and potentially serving the model for predictions. This could include Python scripts for training, data manipulation and model inference. **Configuration:**Configuration files for the model environment, including dependencies (libraries, frameworks), deployment settings (environment variables) and potentially serving configurations (server configurations, API endpoints).
ModelKits are built using a YAML file called a Kitfile, which defines the location of each component. Kitfiles are in a familiar and flexible format. This standardization allows KitOps to integrate seamlessly with existing DevOps pipelines much like a Dockerfile for containerization. As a matter of fact, Modelkits are even OCI-compliant (see
[Open Container Initiative](https://opencontainers.org/)).
This is a quick snapshot of what a sample Kitfile might look like:
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
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
|
manifestVersion: 1.0
package:
name: AIProjectName
version: 1.2.3
description: >-
A brief description of the AI/ML project.
authors: [Author Name, Contributor Name]
code:
- path: src/
description: Source code for the AI models.
license: Apache-2.0
datasets:
- name: DatasetName
path: data/dataset.csv
description: Description of the dataset.
license: CC-BY-4.0
preprocessing: Preprocessing steps.
model:
name: ModelName
path: models/model.h5
framework: TensorFlow
version: 1.0
description: Model description.
license: Apache-2.0
training:
dataset: DatasetName
parameters:
learning_rate: 0.001
epochs: 100
batch_size: 32
validation:
- dataset: DatasetName
metrics:
accuracy: 0.95
f1_score: 0.94
(From:
[kitops.ml/docs/kitfile/format.html#example](https://kitops.ml/docs/kitfile/format.html%23example))
## The High-Level Workflow
Here is a breakdown of the workflow for using ModelKits with KitOps:
**Package as a ModelKit:**Data scientists can use the KitOps CLI to package all project components into a ModelKit. The Kitfile defines the structure and simplifies version control for the entire package. This ensures all the necessary elements for deploying and using the model are bundled together. [Tagging](https://kitops.ml/docs/cli/cli-reference.html%23kit-tag)is a built-in feature that helps organize the ModelKits in a repository through tags that can be referenced. **Version Control and CI/CD:**The ModelKit is version-controlled in a repository alongside the application code, ensuring a unified development flow. The existing CI/CD (continuous integration and continuous delivery) pipeline in your DevOps ecosystem picks up changes and triggers builds and deployments. This leverages your existing infrastructure for managing code changes and deployments, streamlining the process. **Deployment With Existing Tools:**KitOps works well with existing containerization technologies like Docker for deploying ModelKits. This allows SREs, for example, to use familiar DevOps tools for deployment to production environments like Kubernetes. The containerized approach ensures a consistent and portable deployment environment, which will integrate well with DevOps CI/CD pipeline tools like Jenkins, GitLab, CircleCI, GitHub Actions and Azure DevOps.
## Taking the KitOps CLI for a Spin
Now that we have covered the main points of what KitOps is, let us take a hands-on approach to exploring some of the capabilities and usage of the CLI in your terminal of choice. To get started, there are two options. The first option is to clone the KitOps repository and build the binary, like so:
|
1
2
3
4
5
|
git clone https://github.com/jozu-ai/kitops.git
cd kitops
go build -o kit
The second option is to simply download the pre-built binary for your architecture
[here](https://github.com/jozu-ai/kitops/releases/) and extract the compressed file. For example:
|
1
2
3
|
curl -OL https://github.com/jozu-ai/kitops/releases/download/v0.2.4/kitops-darwin-arm64.zip
unzip kitops-darwin-arm64.zip
Whichever option you choose, move the kit binary to a location in your PATH so you can issue commands. This is one example for Mac or Linux:
|
1
|
sudo mv kit /usr/local/bin
Next, check the version of kit from the terminal to see that it is working correctly.
|
1
|
kit version
You should see output like this:
|
1
2
3
4
5
6
7
|
Version: 0.2.4-76ec9bc
Commit: 76ec9bcf94e94177199522480871367138661125
Built: 2024-05-10T21:53:18Z
Go version: go1.21.6
There are a number of
[commands](https://kitops.ml/docs/cli/cli-reference.html) available with the KitOps CLI. For this walkthrough, we will first dive in and find out what Modelkits are available from a known repository for Llama 3 models:
|
1
|
kit list ghcr.io/jozu-ai/llama3
We see that there are a number of ModelKits with various tags:
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
|
REPOSITORY TAG MAINTAINER NAME SIZE DIGEST
jozu-ai/llama3 8B-instruct-f16 Meta Platforms llama3 11.4 GiB sha256:995b9e0f87ddcdcaa59803a08986409b6e4cf2f8b071b064bca21e4e801566a3
jozu-ai/llama3 8B-text-f16 Meta Platforms llama3 11.4 GiB sha256:6b5b4a82ba3a73f00248b4431db738217e1978e316b2d4514b1bb887a11a0d84
jozu-ai/llama3 8B-instruct-q4_0 Meta Platforms llama3 4.1 GiB sha256:ccf9fb3d541c45a65dd99c7272a061776b8cb04d7635a5f844951b410b8ec2a7
...
Let’s look at one of the ModelKits in more detail by referencing the tag and using the info command:
|
1
|
kit info --remote ghcr.io/jozu-ai/llama3:8B-instruct-q4_0
Here we get more information about the Modelkit, essentially what has been defined in the Kitfile.
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
manifestVersion: "1.0"
package:
name: llama3
version: 3.0.0
description: Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8 and 70B sizes.
authors: [Meta Platforms, Inc.]
model:
name: llama3-8B-instruct-q4_0
path: ./llama3-8B-instruct-q4_0.gguf
description: Llama 3 8B instruct model
...
From here, we can unpack the Modelkit from the remote location to our local system in order to work with it.
|
1
2
3
|
kit unpack ghcr.io/jozu-ai/llama3:8B-instruct-q4_0 -d ./unpacked
ls ./unpacked
Notice the files contained within the Modelkit, including the model itself. At this point, let us write a short Python script to interact with the model, checking that we get an adequate response from a given prompt. Create a file called prompt.py and make sure you have the llama_cpp library installed via pip.
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
|
import llama_cpp
model_file = "llama3-8B-instruct-q4_0.gguf"
prompt = "Hello, what model are you?"
model = llama_cpp.Llama(
model_path = model_file,
verbose = False
)
out = model.create_chat_completion(
messages = [{"role": "user", "content": prompt}]
)
print("===")
print(prompt)
print("---")
print(out["choices"][0]["message"]["content"])
Running this script will produce the following output, but it may be slightly different each time.
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
|
python3 prompt.py
===
Hello, what model are you?
---
I'm LLaMA, an AI chatbot developed by Meta AI that can understand and respond to human input in a conversational manner. I'm a large language model trained on a massive dataset of text from the internet, which allows me to generate human-like responses to a wide range of topics and questions. I'm constantly learning and improving my abilities based on the conversations I have with users like you!
From here, you might decide to include this script in the Modelkit by adding it to the Kitfile and then using the pack command from the KitOps CLI to package and tag the new version. This could then be committed to the repo. The possibilities are numerous depending on the flow you aim to achieve.
Quick note: Another simple way to prompt the model in the Modelkit above is by using the dev command from the KitOps CLI. This brings up a simple web-based chat interface.
|
1
|
kit dev start
The chat can then be accessed in a browser window:
To shut it down, simply type:
|
1
|
kit dev stop
## More to Unpack
As you can see from the walkthrough above, KitOps makes the MLOps workflow clear and straightforward. By unifying DevOps and MLOps pipelines with KitOps, teams can reap several benefits:
**Reduced Complexity:**A single pipeline simplifies the development process, reducing overhead and streamlining collaboration between teams. Both DevOps and ML engineers work within the same framework, fostering better communication and understanding. **Faster Time to Market:**Leveraging existing DevOps tools and infrastructure accelerates deployments and improves overall project delivery speed. There’s no need to learn and manage separate MLOps tools, allowing teams to focus on building and improving the model itself. **Improved Consistency:**A unified pipeline ensures consistent version control and configuration management across the entire application and ML model life cycle. This reduces the risk of errors and inconsistencies that can arise from managing separate pipelines. **Model Versioning and Rollbacks:**ModelKits are version-controlled alongside the application code. This allows you to track changes to the model and its dependencies, facilitating rollbacks to previous versions if necessary. Imagine encountering an issue with a newly deployed model. With version control, you can easily revert to a previous, stable version using your existing CI/CD pipeline. **A/B Testing and Experimentation:**KitOps enables seamless A/B testing of different model versions. By deploying multiple ModelKits with different models, you can compare their performance on a subset of your traffic. This allows for data-driven decision making when choosing the best model for production deployment. **Model Governance and Explainability:**The Kitfile can be used to document the model’s purpose, training data used and any relevant metadata. This facilitates model governance by providing a central location for information critical for auditing and compliance purposes. Additionally, KitOps can integrate with model explainability tools to help understand the model’s decision-making process.
## Summing It All Up
The separation of DevOps and MLOps pipelines can hinder the efficient development and deployment of ML models. KitOps offers a compelling open source solution by introducing ModelKits, standardized packages that encapsulate all the critical components of an ML project. This allows organizations to leverage their existing DevOps pipelines and tools for MLOps tasks, leading to reduced complexity, faster time to market, improved consistency and simplified tracking throughout the ML model life cycle. As the field of MLOps continues to evolve, KitOps presents a powerful approach for unifying development and accelerating the adoption of machine learning solutions. Check out the
[KitOps site](http://kitops.ml/) to learn more. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)