# Amazon Revamps Developer AI With Code Conversion, Security
![Featued image for: Amazon Revamps Developer AI With Code Conversion, Security](https://cdn.thenewstack.io/media/2024/09/4221e1bd-qdeveloper-1024x576.jpg)
Amazon spent 50 developer days just to update one application from Java 8/11 to Java 17. With its recently released and [revamped AI copilot](https://aws.amazon.com/blogs/devops/reinventing-the-amazon-q-developer-agent-for-software-development/), [Amazon Q Developer](https://aws.amazon.com/q/developer/), the e-commerce company was able to [convert similar applications](https://www.youtube.com/watch?v=63KCD7fvu4s) in 10 minutes.

A team of five developers was able to convert 30,000 production applications from Java 8 or Java 11 to Java 17 using Q Developer, the company stated. It saved over 4,500 years of development work and $260 million dollars annually from performance improvements, the company added.

Amazon Q Developer is a reinvention of [Code Whisperer](https://thenewstack.io/decoding-amazons-generative-ai-strategy/), which was merged into Q Developer in April.

## Q Developer as a Coding Partner
Rather than just performing code completion, Amazon Q Developer is designed to support the entire software development lifecycle, according to [Srini Iragavarapu](https://www.linkedin.com/in/isvas/), Amazon’s director of generative AI applications and developer experiences.

![Screenshot of Amazon Q working in IDE.](https://cdn.thenewstack.io/media/2024/09/66728972-screenshotamazonq.jpg)
Screenshot from [Amazon Q Developer video](https://youtu.be/U0ZSldhbWs8).

“We don’t look at it from a coding standpoint or a development standpoint,” Iragavarapu told The New Stack. “We’re actually looking at it as a complete software development lifecycle, where the developer goes from ‘I plan my projects, I understand what needs to be done, get the requirements, I implement them, I deploy them, troubleshoot them, and then maintain them.’”

Q Developer enables writing tests, optimizing code, debugging the cloud compute and AWS resources as well, he said. It can build new application features with a descriptive, [natural language prompt](https://roadmap.sh/prompt-engineering). Users can iterate on the plan with Amazon Q as well, reviewing the potential code suggestions and asking for improvements.

It also helps development teams “shift left” by performing a [code security scan](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security.html) and updating developers about potential security problems, he added. Amazon Q Developer has outperformed leading publicly benchmarkable tools on detection across most of the popular programming languages, the company claimed.

Amazon wanted Q Developer to function much as another software developer who will help you as you code. For example, with an unfamiliar repo, a developer would either read the documentation or ask a senior software engineer or peer about what it does.

“One of the things that you could do is ask Q, can you explain what this particular function is doing? So it’s actually looking at the function,” he said. “It walks through line by line. It always feels like you have a developer sitting right next to you and chatting with you about all of this.”

It will also generate code recommendations, of course, and goes beyond single line completions to offer further coding recommendations.

## The Q Stack
In addition to Q Developer, Amazon is offering Q Business, which focuses on the business persona and internal data.

There are three layers to the Q solutions. The bottom layer includes two custom-made chips, the AWS Trainium, which is fine-tuned for training models, and AWS Inferential, which is fine-tuned for inference. The bottom layer also includes Sagemaker, Amazon’s cloud-based machine learning platform. Sagemaker builds, trains and deploys the machine learning and generative AI models.

“Again, we want to make it interactive. Think of it as you’re coding with a paired programmer of sorts,”

— Srini Iragavarapu, Amazon’s director of generative AI applications and developer experiences
The middle layer is composed of tools and pre-trained foundation models to build and scale generative AI-powered applications. It’s built on Bedrock, which is Amazon’s platform for generative AI. Bedrock incorporates a variety of large language models (LLMs) of different sizes and functionalities, including Anthropic’s model, Amazon’s own models and Llama models for customers building applications, he said.

The top layer is the Amazon Q Business and Q Developer, applications with built-in generative AI that do not require any specific expertise in machine learning.

## Amazon: No Training on Enterprise Data
Amazon does not store or use any customer data to improve the base service in the enterprise version, Iragavarapu said. The [free tier](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-free-tier.html) offers developers an opt-out of any code collection.

“Unlike traditional AI services where you have to opt-out to say ‘please do not use any of my data,’ you as a customer, in this case, in the professional version, you don’t even have to opt out because we’re not storing it whatsoever,” he said. “The first decision that we made as we were embarking in this journey is we quickly realized code and anything to do with software overall is IP that every customer wants to be able to use and provide. So we said, let’s not leverage anything that the customers are providing us to the service and only respond, but not use, any of this or store any of this for improving our service.”

## Understanding Other People’s Code
One pain point that Q Developer addresses is analyzing a repo to determine what the code actually does. Copilot does this as well, but unlike Copilot, Q Developer will answer questions a developer might have about the repo. For example, if the repo is using DynamoDB or something that the programmer doesn’t understand, the developer also can ask follow-up questions, such as why is this being used.

“The idea is it is a multistep reasoning system that uses a combination of large language models that we have through Bedrock and also program analysis and some of the vast experience that we have built over decades of building applications within Amazon as well,” he said.

## How Q Developer Performs
Amazon used SWE-bench to evaluate its models. SWE-bench is a benchmark dataset designed to evaluate the capabilities of LLMs in solving real-world software engineering (SWE) problems. It’s a collection of GitHub issues paired with their corresponding pull requests, which provides a dataset that helps researchers determine how well LLMs can understand, analyze and generate code solutions.

![Screenshot shows ability to review and accept ore reject Amazon Q Developer code.](https://cdn.thenewstack.io/media/2024/09/8c07ca18-dev-agent-08_amazon.png)
A screenshot from [Amazon’s blog](https://aws.amazon.com/blogs/devops/reinventing-the-amazon-q-developer-agent-for-software-development/) shows the ability to review and accept or reject Amazon Q Developer code.

On SWE-bench’s leaderboard, Amazon Q Developer rated 20.33 percent of issues resolved as of May 9, 2024 on the lite version. Since the first evaluation, Amazon has updated Q with other LLMs and taken feedback about what developers like and don’t like — both internally from its approximately 80,000 developers, as well as from external users.

Internally, AWS conducted a productivity challenge and found that developers who used Q Developer were 27% more likely to successfully complete tasks. Amazon also reported that Q Developer has the highest reported code acceptance rates in the industry for assistants that perform multi-line code suggestions, with BT Group recently reporting they accepted 37% of Q’s code suggestions and National Australia Bank reporting a 50% acceptance rate, according to a company spokesperson.

One of the pieces of feedback they received is that it was difficult to tell what the tool had updated. Now Q Developer provides a constant status in terms of what it’s actually doing, which is important since it can amend multiple files and create new files, he added.

“Again, we want to make it interactive. Think of it as you’re coding with a paired programmer of sorts,” he said. “In this case, if I accept it, it actually then takes the code in and then it starts doing it. Instead, you can also say provide feedback and regenerate.”

## What Developers Need To Know
So far, Q Developer supports [15 programming languages](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/faq.html):

[JavaScript](https://thenewstack.io/free-javascript-from-legal-clutches-of-oracle-devs-petition/)[TypeScript](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/)[Python](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/examples-python.html)[Java](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/examples-java.html)- C#
[Go](https://thenewstack.io/golang-how-to-use-the-go-install-command/)[Rust](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/)[PHP](https://thenewstack.io/why-php-usage-has-declined-by-40-in-just-over-2-years/)- Ruby
[Kotlin](https://thenewstack.io/how-to-handle-platform-specific-dependencies-in-kotlin-multiplatform/)- C
- C++
- Shell scripting
[SQL](https://thenewstack.io/sql-nosql-and-vectors-oh-my/)- ScalJavaScript
It also supports infrastructure-as-code languages and tools, including [TerraForm’s HCL](https://thenewstack.io/terraforms-best-practices-and-pitfalls/) (HashiCorp Configuration Language) and CDK (cloud development kit).

The AI agent currently is available in a free tier, as well as a paid, enterprise tier, which enables administrators to enable the tool for all developers within an organization and provides administrator controls in terms of what code is accessible.

“Some of my friends keep asking me, ‘But wait, there needs to be a catch. Is it a freemium? Are you trying to get something out of it?’ Absolutely nothing, really. It is free. Anybody can use it, install it,” Iragavarapu said. “The idea there was we wanted to enable developers to be able to build applications, use generative AI and come up with creative problem-solved solutions for customers.”

To get started, developers need to have an AWS Builder ID or be part of an organization with an AWS IAM Identity Center instance set up that allows them to use Amazon Q. To use [Amazon Q Developer agent in an IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html), start by installing the Amazon Q extension, which is available for JetBrains, Visual Studio Code, Visual Studio (in preview), and in the Command Line on macOS.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)