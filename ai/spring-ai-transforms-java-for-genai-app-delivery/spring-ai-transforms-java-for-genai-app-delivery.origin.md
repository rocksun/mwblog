# Spring AI Transforms Java for GenAI App Delivery
![Featued image for: Spring AI Transforms Java for GenAI App Delivery](https://cdn.thenewstack.io/media/2024/09/1e509293-spring-ai-transforms-java-genai-app-1024x576.jpg)
Machine learning (ML) and AI are no longer new, but generative AI (GenAI) — which uses
[large language models](https://thenewstack.io/llm/) (LLMs) to generate images, text, music and other media — has garnered considerable attention over the last 18 months, capturing the imagination of both business leaders and the public.
Trained on a vast corpus of material, these models generate images, music, articles and other text when given a simple prompt. While the results are rarely as refined or innovative as a skilled content creator or artist could produce, they enable beginners or non-artists to generate media at an impressive pace.
## Creating New Products, Features with AI
Incorporating GenAI models into apps opens the possibility of developing new software product features previously unattainable due to practicality or cost constraints. Common use cases include building Q&A and chat systems on top of your internal documentation and enabling automatic prequalification on top-of-funnel sales or hiring leads.
When I was chief editor at InfoQ, we published a huge amount of videos — around 20 per week — recorded at some of the world’s leading technology conferences. However, that video content was not searchable, making it hard for site visitors to find relevant material.
I looked at the possibility of creating transcripts, but the cost of human transcription was prohibitive, and ML transcription wasn’t accurate enough to use.
Four years later, the landscape changed, with the arrival of a new generation of ML transcription. Although we still needed human reviewers to get transcripts to publishable quality, ML was accurate enough that we could do so at a heavily reduced cost. After this initial foray, we were able to extend the same technology to new use cases, including generating various new product ideas for our conferences.
## AI Without Python? Spring AI Says ‘No Problem’
AI/ML has also deeply penetrated the software development field. According to
[Docker](https://www.docker.com/?utm_content=inline+mention)‘s 2024 [“State Of Application Development Report,”](https://www.docker.com/resources/2024-state-of-application-development-report/?key=9ae0f193aaebbedebf3bb383d50a723dcba4a1afec6b8ca3a01decf04e253b57) 64% of respondents use AI for tasks like writing code, documentation and research, and 46% work on ML in some capacity. Tools like GitHub Copilot and JetBrains AI allow automatic code writing, effectively acting as a computer pair programmer.
For developers working on generative AI projects, providers such as OpenAI and Mistral AI offer access to their collections of LLMs via REST APIs. As long as you have an API key that grants access to those APIs, you can use almost any HTTP client to submit prompts to the models, including the good old command line standby
curl. However, if you are building a feature with relatively complex interactions, a client abstraction makes the job much easier.
Despite the extensive history of AI,
[Java’s](https://thenewstack.io/java/) role in the domain has been relatively minor. For developers using data science favorite [Python](https://thenewstack.io/python/), there are many [capable libraries and frameworks](https://winder.ai/comparison-open-source-llm-frameworks-pipelining/), such as [LangChain](https://docs.langchain.com/docs/) and [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/getting_started/concepts.html).
But options for enterprise
[Java developers](https://roadmap.sh/java) have only recently emerged. Among them is [Spring AI](https://spring.io/projects/spring-ai), which was announced last November and is heading toward general availability (GA) but has already been evaluated and used for production apps in its current state.
For many enterprises, this matters. “Lots of customers started their AI journey with specialists who know Python and build the first couple of applications with it; but in the cases where Java is the approved path to production, they are stuck with many new administration or exception processes if they use Python,” said
[Adib Saikali](https://www.linkedin.com/in/adibsaikali/), distinguished software engineer at Broadcom.
He told The New Stack: “These customers say, ‘We would like to scale out AI in our organization. We have thousands of Java developers, and we would like to use familiar tools so that we don’t have to retrain.'”
What’s more, building AI at an enterprise scale requires the kind of software engineering skills that Java and .NET developers typically have. “Success in enterprise AI — with hundreds of AI-powered features across hundreds of enterprise applications — requires that you be extraordinarily mature at delivering software,” Saikali said.
“To be honest, we are at a place of experimentation right now with AI because the space is moving so fast,” he continued. “If I’m building an AI application in a bank, it might be the first of its kind, so there is no precedent. Governance and best practices likewise also don’t have precedence and are being developed as organizations are building these apps.
“Being able to iterate even more rapidly is the key. With Spring AI, we are building on 20 years of experience helping developers adopt best practices, so you don’t have to start from scratch.”
## Building AI Apps With Java
[Spring AI ](https://docs.spring.io/spring-ai/reference/)is an Apache License 2.0 open source framework extension for Spring and [Spring Boot](https://roadmap.sh/spring-boot), which provides a client abstraction for working with various AI providers or in a multimodal approach for a single app. It is [fully integrated into the Spring ecosystem](https://tanzu.vmware.com/content/blog/spring-ai-empowers-java-developers-in-the-ai-landscape), allowing developers to leverage that ecosystem to [build AI-powered apps quickly](https://tanzu.vmware.com/content/blog/spring-ai-enables-quick-delivery-of-intelligent-apps-in-java).
By providing a consistent interface, Spring AI allows you to write portable code, whichever model you are using. Spring AI currently supports all major model providers, including OpenAI, Mistral AI,
[Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [Amazon](https://aws.amazon.com/?utm_content=inline+mention),
“I can change a dependency and move from Ollama to OpenAI, or from OpenAI to
[Bedrock](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/), without changing any code,” [DaShaun Carter](https://www.linkedin.com/in/dashaun/), research development software engineer and Spring developer advocate at Broadcom, told The New Stack.
As well as supporting multiple model providers, Spring AI works with various model types, including chat, text-to-image, audio transcription and text-to-speech. Using combinations of models allows you to build systems such as voice-based assistants that take spoken input from a user, transcribe it to text, send it to an LLM for a response and then use a text-to-speech model to read that response back to the user.
A concern with building these sorts of abstractions is that if you design the API too early, you end up building the wrong abstraction. The original Spring framework was, in some respects, a response to J2EE vendors doing that with object request brokers.
However, Carter argued, “in this case, the LLM providers have done some of that work for us already, and the Spring team has successfully delivered these abstractions over the years. They look at what their customers are doing the hard way and abstract away the most commonly used 95%, then they find a way to allow developers to drop down and access that last 5% of functionality.”
## Solving for Enterprise Data and API Integrations
When it comes to security, the first option is to run the models locally, and Broadcom offers
[VMware Private AI Foundation](https://www.vmware.com/explore/video-library/video/6360759360112?_gl=1*1wqfjwg*_ga*Njg2NzM1NzkzLjE3MjI4NzcxNzc.*_ga_8VJHMNGE3E*MTcyNTA0NjY2OC4xNi4xLjE3MjUwNDY2NzQuMC4wLjA.) for this. However, there are two secondary issues with LLMs. The first is that [getting the right answer ](https://www.youtube.com/watch?v=7S6M8H2hz6w)depends on your ability to write accurate prompts that provide the AI model with all the information it needs. The second is that LLMs are frozen after training, which leads to stale knowledge.
Solutions exist to address these issues, in the form of
[retrieval augmented generation](https://thenewstack.io/retrieval-augmented-generation-for-llms/) (RAG) for prompt writing and function calling for updating the LLM’s knowledge. “In both cases, Spring AI makes it possible to capture sophisticated knowledge in the form of reusable components called [advisors](https://docs.spring.io/spring-ai/reference/api/chatclient.html#_retrieval_augmented_generation),” Saikali said.
Advisors enable common logic to be applied to chat-client requests to enhance model interactions, provide session state, and apply logging and any additional chat client flows you need in a consistent way within an application and across applications
RAG addresses the challenge of incorporating relevant data into prompts for accurate AI model responses. It works in two phases.
The first is based around an
[extract, transform, and load (ETL)](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html) pipeline, which uses batch processing-style programming to read unstructured data from your documents, then transforms and writes it into a vector database. Vector databases are preferred for this because they are good at finding similar content.
In the second phase, RAG takes a user’s question and adds all the similar document pieces to the prompt sent to the AI model.
This diagram shows how this works:
![Diagram of how RAG addresses the challenge of incorporating relevant data into prompts for accurate AI model responses.](https://cdn.thenewstack.io/media/2024/09/89a6a387-spring-ai-rag-1024x567.jpg)
Source:
[Spring.io](https://docs.spring.io/spring-ai/reference/concepts.html#concept-rag)
RAG is a powerful technique, but using it successfully can be more difficult than it appears. “It takes a lot of trial and error to get it right,” Saikali said. “With Spring AI we’re allowing companies to capture those AI patterns as Spring AI advisors.”
He referred back to his previously mentioned example of building an AI application for a bank. With Spring AI, every AI app built for the bank “will be correctly integrated with a data scrubber and everything else it needs.”
While there are some limitations to the approach, RAG provides a low-cost way to create domain-specific customization. Since applications based on RAG can reference the data sources they use, it offers better transparency and source citing.
“One of the first questions customers ask is, ‘How can I fine-tune these LLMs for my use case?'” Carter said. “With these vector databases, you can do the embeddings for whatever data you have and you don’t need to retrain the models. Spring AI makes it easy to inject a prompt with your embeddings, and you can use these freely available LLMs to power your applications.”
The second issue, of stale data, can be addressed using
[function calling](https://docs.spring.io/spring-ai/reference/api/functions.html), which allows you to register your own functions to connect an LLM to the APIs of external systems. These systems can provide LLMs with real-time data and perform data processing actions on their behalf. Spring AI handles the function invocation conversation and allows you to define and reference multiple functions in a single prompt.
A basic flow is shown below:
![Diagram of a function calling flow](https://cdn.thenewstack.io/media/2024/09/9e39b008-function-calling-basic-flow-1024x554.jpg)
Source:
[Spring.io](https://docs.spring.io/spring-ai/reference/concepts.html#concept-fc)
“This is where it gets really interesting,” said Carter, “because you can now call outside the LLMs for particular tasks. For example, if there is a question about the weather, you can tell it to call a service and use that data as part of the response.”
The final step for any AI implementation is to evaluate the output to help enable the accuracy and usefulness of the final application. Techniques for this are still somewhat nascent, however.
One approach involves presenting both the user’s request and the AI model’s response to the model, querying whether the response aligns with the provided data. The Spring AI project provides some basic examples of how to evaluate the responses, in the form of prompts, to include in a JUnit test. This feature is in early development but more functionality is slated for future releases.
## Getting Started with Spring AI
Starting a Spring AI application is like starting any other Spring Boot application. You can use the Spring Boot support in IntelliJ IDEA, Spring Tools (for both Eclipse and VS Code), NetBeans, the Spring Boot CLI or the Spring CLI — or just point your browser to the
[Spring Initializr](https://start.spring.io/) and fill in the blanks. ![Spring Initialzr web UI](https://cdn.thenewstack.io/media/2024/09/09739ec4-spring-initializr-1024x500.png)
Source:
[Spring Initializr](https://start.spring.io/)
A
[Getting Started guide](https://docs.spring.io/spring-ai/reference/getting-started.html) provides more information on which dependencies you need to add to your project build system for working with the various models.
## Learn More About Spring AI
To learn more about Spring AI, please check out Carter’s recent talk at Explore Las Vegas about
[Spring AI on Tanzu Platform](https://www.vmware.com/explore/video-library/video/6360758967112). Also be sure to watch the [SpringOne Spotlight](https://www.youtube.com/watch?v=7S6M8H2hz6w) session at Explore Las Vegas, where Spring experts delivered a live Spring AI demo.
For those ready to get started, Saikali has a
[GitHub example project](https://github.com/asaikali/spring-ai-zero-to-hero) that takes you through many of the required steps to implement an AI project with Spring AI. There is also a [sample AI-powered flight-booking service](https://github.com/tzolov/playground-flight-booking/) that uses RAG, function calling and an LLM to interact with a user.
If you would like to speak directly with the experts, the Tanzu AI Solutions team will be at Explore Barcelona on Nov. 4-7.
[Registration is now open](https://www.vmware.com/explore/eu).
Also be sure not to miss the
[recent announcements](https://tanzu.vmware.com/content/blog/enterprise-ready-genai-apps-with-tanzu-ai-solutions) about VMware Tanzu AI Solutions. Tanzu AI Solutions is a set of capabilities in [Tanzu Platform 10](https://thenewstack.io/broadcom-debuts-vmware-tanzu-platform-10-at-explore-2024) to help organizations accelerate delivery of enterprise-ready GenAI apps with safety and at scale. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)