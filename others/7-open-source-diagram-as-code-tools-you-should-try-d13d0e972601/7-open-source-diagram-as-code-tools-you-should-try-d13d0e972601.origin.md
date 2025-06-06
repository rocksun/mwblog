Whether you're designing infrastructure, explaining application flows, or documenting cloud architectures, diagrams are a crucial part of technical communication. But traditional diagramming tools can become bottlenecks, manual edits, versioning issues, and a lack of reproducibility often slow teams down. That's where **Diagram as Code** comes in.

**Friends link for non-Medium members: **[7 Open Source Diagram-as-Code Tools You Should Try](https://blog.prateekjain.dev/d13d0e972601?source=friends_link&sk=4509adaf94cc82f8a405c6c030ca2fb6)
Diagram as Code tools enable you to generate architecture diagrams directly from code. They're version-controlled, automatable, and consistent across teams. In this guide, we'll explore seven open-source tools that support Diagram as Code for cloud and software architectures, with a special focus on AWS-based infrastructure.

Let's first understand the diagram that we'll try to replicate in each tool.

### The Sample AWS Architecture
We'll use a sample architecture that reflects a typical web-based application hosted on AWS. Here are the components:

**Route53**: DNS routing for your domain.**Elastic Load Balancer (ELB)**: Distributes incoming traffic.**Two EC2 instances**: Host the application backend.**Lambda function**: Used for authentication logic.**IAM Role**: Linked with Lambda for secure permissions.**Primary RDS DB**: Main application database.**Replica RDS DB**: Read-replica for better performance.
Each tool will generate this same logical structure to help you compare how they perform.

### 1. Diagrams (by mingrammer)
[Diagrams](https://diagrams.mingrammer.com/) is a Python-based open-source library that turns simple Python code into beautiful system architecture diagrams. It supports major cloud providers like AWS, Azure, and GCP, as well as on-premise tools like Kubernetes and Docker. It's one of the easiest ways to automate architecture documentation directly from code.
#### Key Benefits
- Supports a vast number of cloud and DevOps icons out of the box.
- Easy to use for developers familiar with Python.
- Good integration with CI/CD tools for automated doc generation.
#### Drawbacks
- Limited customisation in layout and styling.
- No support for real-time collaboration or GUIs.
#### Installation
Diagrams depend on **Graphviz** to render the architecture diagrams. You need to install Graphviz first before using the `diagrams`
Python package.

If you're on **macOS**, you can use Homebrew. For other platforms, refer to the official Graphviz installation guide: [https://graphviz.org/download/](https://graphviz.org/download/)

```
# Install Graphviz first
brew install graphviz
# Then install Diagrams
pip install diagrams
```
#### Sample Diagram Code
Save this code snippet in a file aws.py

```
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.security import IAM
from diagrams.aws.compute import Lambda
with Diagram("AWS Architecture", show=False):
dns = Route53("Route53")
lb = ELB("Load Balancer")
web1 = EC2("Web Server 1")
web2 = EC2("Web Server 2")
auth_lambda = Lambda("Auth")
iam = IAM("IAM Role")
db_primary = RDS("Primary DB")
db_replica = RDS("Replica DB")
dns >> lb >> [web1, web2]
web1 >> auth_lambda >> iam
[web1, web2] >> db_primary >> db_replica
```
Now, run the following command

`python3 aws.py`
#### Output
![None](https://miro.medium.com/v2/resize:fit:700/1*GrCHCwPXPI8BV4ww2SgTFw.png)
### 2. PlantUML
[PlantUML](https://plantuml.com/) is a mature and flexible tool that allows you to define diagrams using a simple and powerful textual language. It supports sequence diagrams, use case diagrams, class diagrams, component diagrams, and more, making it suitable for both software development and infrastructure modelling.
#### Key Benefits
- Text-based and version control-friendly.
- Works well with markdown, documentation tools, and IDEs.
- Flexible and supports many diagram types.
#### Drawbacks
- Requires learning its syntax.
- Can become verbose for large-scale diagrams.
#### Installation
You can either run PlantUML locally using Docker or use the official web-based editor directly in your browser: [https://editor.plantuml.com/](https://editor.plantuml.com/)

For local setup via Docker:

`docker run -d -p 8080:8080 plantuml/plantuml-server:jetty`
#### Sample Diagram Code
```
@startuml
component "Route53" as DNS
component "ELB" as LB
component "EC2 Web 1" as WS1
component "EC2 Web 2" as WS2
component "Lambda Auth" as Lambda
component "IAM Role" as IAM
component "RDS Primary" as DB1
component "RDS Replica" as DB2
DNS --> LB
LB --> WS1
LB --> WS2
WS1 --> Lambda
Lambda --> IAM
WS1 --> DB1
WS2 --> DB1
DB1 --> DB2
@enduml
```
#### Output
![None](https://miro.medium.com/v2/resize:fit:700/1*9uO_yvDgMf-P6uoEGdYMYQ.png)
### 3. Mermaid
[Mermaid](https://mermaid.js.org/) is a JavaScript-based diagramming and charting tool that uses Markdown-inspired syntax. It's ideal for embedding simple, clear diagrams directly into markdown documentation or tools like Notion, GitHub, or GitLab.
#### Key Benefits
- Works seamlessly with markdown files.
- Easy syntax for beginners.
- Supported natively on many platforms.
#### Drawbacks
- Not suitable for large, complex diagrams.
- Limited visual customisation options.
#### Usage (No installation required in markdown platforms)
You can use Mermaid directly in many markdown-based platforms like GitHub, GitLab, Notion, and Obsidian without needing to install anything.

For quick testing or sharing diagrams online, use their official playground:
[https://www.mermaidchart.com/play](https://www.mermaidchart.com/play)

#### Sample Diagram Code
```
graph TD
DNS[Route53] --> LB[ELB]
LB --> WS1[Web Server 1]
LB --> WS2[Web Server 2]
WS1 --> Lambda[Lambda Function]
Lambda --> IAM[IAM Role]
WS1 --> DB1[Primary DB]
WS2 --> DB1
DB1 --> DB2[Replica DB]
```
#### Output
![None](https://miro.medium.com/v2/resize:fit:700/1*J30bXQ-1cyPt0K2t142Ysg.png)
### 4. Structurizr DSL
[Structurizr](https://structurizr.com/) DSL is a powerful textual domain-specific language (DSL) that helps you create software architecture diagrams based on the C4 model. It's focused more on conceptual clarity than visual perfection and is excellent for modelling enterprise-scale systems.
#### Key Benefits
- Fully supports C4 modelling standard.
- Clear separation of model and view.
- Encourages best practices in architecture.
#### Drawbacks
- Steeper learning curve.
- Requires understanding of the C4 model.
#### Installation
You can either use the Structurizr DSL directly in your browser or install it locally.

Web editor: [https://structurizr.com/dsl](https://structurizr.com/dsl)
Local installation guide: [https://structurizr.com/help/dsl](https://structurizr.com/help/dsl)

#### Sample Diagram Code
```
workspace {
model {
user = person "User"
system = softwareSystem "Web Application" {
lb = container "Load Balancer"
web1 = container "Web Server 1"
web2 = container "Web Server 2"
auth = container "Auth Lambda"
role = container "IAM Role"
db1 = container "Primary DB"
db2 = container "Replica DB"
user -> lb
lb -> web1
lb -> web2
web1 -> auth
auth -> role
web1 -> db1
web2 -> db1
db1 -> db2
}
}
views {
container system {
include *
autolayout lr
}
}
}
```
#### Output
![None](https://miro.medium.com/v2/resize:fit:700/1*noUSCGjg8qKGvbZh9xgMMQ.png)
### 5. AWS Diagram-as-Code (by AWS Labs)
[AWS Diagram-as-Code](https://github.com/awslabs/diagram-as-code) is an open-source YAML-based tool built by AWS Labs. It focuses on representing AWS infrastructure using native service identifiers and relationships. Ideal for AWS-heavy environments, this tool outputs static architecture images from a structured YAML format.
#### Key Benefits
- Simple and declarative YAML syntax.
- Tailored for AWS services.
- Lightweight and CLI-driven.
#### Drawbacks
- Limited to AWS only.
- Customisation and layout control are minimal.
#### Installation
You can easily install AWS Diagram-as-Code on macOS using Homebrew:

`$ brew install awsdac`
For other systems or more advanced usage, refer to the official documentation: [https://github.com/awslabs/diagram-as-code](https://github.com/awslabs/aws-diagram-as-code)

#### Sample Diagram Code
```
Diagram:
DefinitionFiles:
- Type: URL
Url: "https://raw.githubusercontent.com/awslabs/diagram-as-code/main/definitions/definition-for-aws-icons-light.yaml"
Resources:
Canvas:
Type: AWS::Diagram::Canvas
Direction: vertical
Children:
- AWSCloud
- User
AWSCloud:
Type: AWS::Diagram::Cloud
Direction: vertical
Preset: AWSCloudNoLogo
Align: center
Children:
- Route53
- LoadBalancer
- EC2Stack
- Lambda
- IAM
- DBStack
User:
Type: AWS::Diagram::Resource
Preset: User
Label: User
Route53:
Type: AWS::Route53::HostedZone
Label: Route 53
LoadBalancer:
Type: AWS::ElasticLoadBalancingV2::LoadBalancer
Label: Load Balancer
EC2Stack:
Type: AWS::Diagram::HorizontalStack
Children:
- EC2_1
- EC2_2
EC2_1:
Type: AWS::EC2::Instance
Label: Web Server 1
EC2_2:
Type: AWS::EC2::Instance
Label: Web Server 2
Lambda:
Type: AWS::Lambda::Function
Label: Auth Lambda
IAM:
Type: AWS::IAM::Role
Label: IAM Role
DBStack:
Type: AWS::Diagram::HorizontalStack
Children:
- DB1
- DB2
DB1:
Type: AWS::RDS::DBInstance
Label: Primary DB
DB2:
Type: AWS::RDS::DBInstance
Label: Replica DB
Links:
- Source: User
SourcePosition: N
Target: Route53
TargetPosition: S
TargetArrowHead:
Type: Open
- Source: Route53
SourcePosition: N
Target: LoadBalancer
TargetPosition: S
TargetArrowHead:
Type: Open
- Source: LoadBalancer
SourcePosition: SSW
Target: EC2_1
TargetPosition: NNW
TargetArrowHead:
Type: Open
- Source: LoadBalancer
SourcePosition: SSE
Target: EC2_2
TargetPosition: NNE
TargetArrowHead:
Type: Open
- Source: EC2_1
SourcePosition: S
Target: Lambda
TargetPosition: N
TargetArrowHead:
Type: Open
- Source: Lambda
SourcePosition: S
Target: IAM
TargetPosition: N
TargetArrowHead:
Type: Open
- Source: EC2_1
SourcePosition: SE
Target: DB1
TargetPosition: NW
TargetArrowHead:
Type: Open
- Source: EC2_2
SourcePosition: SW
Target: DB1
TargetPosition: NE
TargetArrowHead:
Type: Open
- Source: DB1
SourcePosition: E
Target: DB2
TargetPosition: W
TargetArrowHead:
Type: Open
```
Save it as aws.yaml and run the following command

`awsdac aws.yml`
#### Output
![None](https://miro.medium.com/v2/resize:fit:700/1*zgzH4BrYAQOLYVSrm8AwMA.png)
### 6. D2 (by Terrastruct)
[D2](https://d2lang.com/) is a modern diagram scripting language created by Terrastruct. It emphasises simplicity and clarity, making it perfect for developers who want elegant diagrams with minimal effort. It supports real-time rendering in the VS Code extension or browser.
#### Key Benefits
- Simple syntax with auto-layout.
- Themes and annotations are supported.
- Fast rendering, great developer experience.
#### Drawbacks
- The community and ecosystem are still growing.
- Lacks out-of-the-box AWS-specific icons.
#### Installation
You can install D2 locally or use the web-based playground for quick visualisation: [https://play.d2lang.com/](https://play.d2lang.com/)

```
brew install terrastruct/d2/d2
# or
curl -fsSL https://d2lang.com/install.sh | sh
```
#### Sample Diagram Code
```
direction: right
DNS: "Route53: DNS"
LB: "ELB: Load Balancer"
WS1: "EC2: Web Server 1"
WS2: "EC2: Web Server 2"
Lambda: "Lambda: Auth Function"
IAM: "IAM Role"
DB1: "RDS: Primary DB"
DB2: "RDS: Replica DB"
DNS -> LB
LB -> WS1
LB -> WS2
WS1 -> Lambda
Lambda -> IAM
WS1 -> DB1
WS2 -> DB1
DB1 -> DB2
```
#### Output
![None](https://miro.medium.com/v2/resize:fit:700/1*Y537hqE8VjkqeZqhuDqKBg.png)
### 7. Kroki
Kroki is a diagram rendering engine that acts as a backend service for over 20 popular diagram formats like Mermaid, PlantUML, Graphviz, and more. It's ideal if you want to standardise diagram rendering across different formats in CI/CD or documentation platforms.

#### Key Benefits
- Centralised rendering for many formats.
- Works well in pipelines, docs, or apps.
- Easily self-hosted with Docker.
#### Drawbacks
- Still needs external syntax (Mermaid, PlantUML, etc.).
- Requires configuration for self-hosted deployments.
#### Installation
You can run Kroki locally using Docker or call its remote API directly for quick rendering.

```
# Run Kroki locally
docker run -d -p 8000:8000 yuzutech/kroki
# Or call the public API
curl -X POST https://kroki.io/mermaid/svg -d 'graph TD; A-->B; B-->C; C-->A;' > diagram.svg
```
#### Sample Use (Mermaid via curl)
```
curl -X POST https://kroki.io/mermaid/svg -d 'graph TD
> DNS[Route53] --> LB[ELB]
> LB --> WS1[Web Server 1]
> LB --> WS2[Web Server 2]
> WS1 --> Lambda[Lambda Function]
> Lambda --> IAM[IAM Role]
> WS1 --> DB1[Primary DB]
> WS2 --> DB1
> DB1 --> DB2[Replica DB]' > diagram.svg
```
#### Output
![None](https://miro.medium.com/v2/resize:fit:700/1*Cg6jCow0qACz32o3hCeTbA.png)
### Wrapping Up
Diagram-as-Code tools are transforming how developers, DevOps engineers, architects, and even technical writers communicate complex infrastructure and system designs. In today's fast-paced engineering environments, where systems evolve continuously, having architecture documented in a reproducible, version-controlled format is no longer a luxury; it's a necessity.

By selecting the right tool for your workflow, you not only improve documentation quality but also unlock automation possibilities, such as rendering diagrams directly from CI/CD pipelines or embedding up-to-date visuals in internal portals.

You can choose a tool that fits your personal workflow or team setup. For me, **Diagrams** worked perfectly because I'm comfortable with Python and primarily work within the AWS ecosystem. It allowed me to integrate diagram generation easily into my existing Python-based workflows.

While **AWS Diagram-as-Code** is promising and feels native to the AWS world, its YAML syntax can be slightly tricky, and the layout sometimes requires manual adjustment. So it depends entirely on your use case; some might prefer simplicity, others may need native service mapping or advanced layout control.

No matter which tool you pick, embracing Diagram as Code will make your designs easier to maintain, easier to scale, and much easier to share across teams.

Let your diagrams speak code, and scale with your infrastructure.

You can follow me on X ([@PrateekJainDev](https://x.com/PrateekJainDev)) and LinkedIn ([in/prateekjaindev](https://x.com/PrateekJainDev)) for more updates!

Happy Diagramming 🚀

![None](https://miro.medium.com/v2/resize:fit:700/1*nKvQX0OLMeZ0XvwsDn7slQ.gif)