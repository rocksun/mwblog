# Annoyed by Poor Docs for Your Cloud Apps? Break the Cycle
![Featued image for: Annoyed by Poor Docs for Your Cloud Apps? Break the Cycle](https://cdn.thenewstack.io/media/2024/08/bbc6373a-files-1024x576.jpg)
Internal documentation is boring. It shouldn’t be — we all know that it’s extremely critical to our way of life as engineers — but it just is.

The dilemma is that we suffer on both sides of the documentation fence: We don’t enjoy writing it, and it infuriates us when we receive [poor documentation](https://thenewstack.io/poor-documentation-is-costly-heres-how-to-fix-it/). How often have you cursed the developer before you for their nonexistent or barely there documentation that they phoned in?

For most of us, [documentation](https://thenewstack.io/an-engineers-best-tips-for-writing-documentation-devs-love/) is often the last task to be worked on, which means a lot of important details are left out that could help new team members as well as the team picking up the project for maintenance. It’s extremely difficult to recall the precise steps or changes that you’ve made to a project after a few weeks pass and you’ve move onto the next challenge. The previous project quickly becomes a distant memory.

It’s clear we need [help in this department](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/), so as software engineers, we rightfully attempt to use more software to solve the problem. In my experience, living documentation is one of the best tools that I never specifically asked for, oftentimes took for granted, but was always thankful for when it was available.

## What Is Living Documentation?
Living documentation is a concept where documentation is continuously updated and synchronized with the actual codebase and system behavior. It evolves with the changing software, ensuring that the documentation always reflects the current state of the system.

With bare minimal effort, living documentation tools make it so there will never be a time when you hand over a project to another team member without it having some base form of documentation. Ideally, it provides a launchpad into clear and concise documentation for every project that isn’t just an afterthought at the tail end.

To help frame this technology, let’s take a look at some examples you might recognize and how they’ve implemented some variants of living docs.

## Types and Examples You May Have Seen Before
You may be using living documentation tools already haven’t really thought about them that way. In some cases, the specification used for systems can also act as the starting point for living documentation. These tools help ensure that documentation remains accurate and up to date with the evolving codebase, reducing the risk of outdated or incomplete documentation.

**Specification-Based Documentation:**
Specification-based documentation focuses on creating detailed descriptions and specifications of software components, often independent of the implementation. These specifications can be used to ensure all stakeholders have a clear understanding of what the software should do and can also be used to generate tests or even code stubs.

**Code Comment-Based Documentation:**
Code comment-based documentation involves embedding documentation within the source code using special comments. These comments are then processed by documentation-generation tools to create comprehensive documentation.

[Javadoc](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html)
**Purpose**: Used for documenting Java code.
**How It Works as Living Documentation:**
- Generates HTML documentation directly from Java source code comments.
- Automatically updates documentation when the code is compiled, ensuring it always reflects the current state of the codebase.
**Benefits:**
- Keeps Java code documentation up to date with minimal effort.
- Provides comprehensive details about the code structure and functionality.
**Code-Based Documentation:**
Code-based documentation tools analyze the source code itself to generate documentation. This approach ensures the documentation is always in sync with the code, as it’s derived directly from the codebase.

[Swagger/OpenAPI](https://swagger.io/docs/specification/about/)
**Purpose**: Primarily used for API specification.
**How It Works as Living Documentation:**
- Automatically generates and updates API documentation based on the latest API definitions.
- Interactive documentation allows developers to test and validate API endpoints, ensuring that the documentation remains synchronized with the code.
**Benefits:**
- Ensures API documentation is always in sync with the code.
- Enhances collaboration between frontend and backend developers.
## Prioritize Cloud Resource Documentation
Communicating runtime requirements from a development team to an operations team is challenging due to several factors. Technical knowledge gaps between teams can lead to incomplete or inaccurate specifications, as developers may not fully understand cloud infrastructure intricacies.

I’ve seen a variety of forms that app development teams must fill out manually to communicate their requirements, and while these could also serve as documentation, they’re often incomplete or inconsistent, and require meetings or a long trail of support ticket replies to come to resolution.

The issue is that miscommunications at this phase of the project are extremely costly. They cause:

- Unnecessary financial expenses from overallocated resources
- Higher operational expenses for troubleshooting underallocated resources and permissions
- Data breaches and compliance fines
- Lost revenue and damaged reputation due to downtime
## An Olive Branch From Developers to Operations
Living documentation for cloud resource configuration can act as the bridge between development and operations teams by providing transparency and up-to-date information about the runtime requirements of the application. This creates an improved working relationship in several ways:

- Both teams have visibility into the runtime requirements of the application.
- Up-to-date documentation improves communication. Since both team members have a single source of truth, there is less room for miscommunications.
- Specifications are always communicated in a consistent format, which paves the way for future streamlined processes such as reviews and optimization analysis.
## Living Documentation for Cloud Resource Configuration
Here are a few examples of tools supporting the creation of living documentation for cloud resources.

[Nitric](https://nitric.io?utm_content=inline+mention)
**Purpose**: Expediting the development and deployment of cloud applications.
**How It Works as Living Documentation:**
- Automatically generates a specification that captures the
[infrastructure required to run an application by inspecting application code](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/). - Ensures that resource specification and the deployed infrastructure are always up to date with the application logic.
- Can be interpreted as other documentation formats including a visual representation of the specification.
**Benefits:**
- Ensures that the runtime requirements of the application remain consistent with the application code.
- The specification can be used to generate
[Infrastructure as Code](https://thenewstack.io/no-terraform-no-iac-are-you-looking-for-disaster/)(IaC), for example Terraform, which can be considered a blueprint for your intended infrastructure (more documentation).
[Terraform](https://www.terraform.io/)
**Purpose**: IaC tool designed to define, provision and manage infrastructure resources across various cloud providers in a consistent and automated manner.
**How It Works as Living Documentation:**
[Terraform uses](https://thenewstack.io/terraform-isnt-dead/)a declarative language to specify the desired state of infrastructure. These configurations serves as a readable blueprint of the infrastructure.- The plan can be used to generate visualizations or summaries of the expected resources to be deployed including the configuration settings.
**Benefits:**
- Infrastructure is transparent, with human-readable declarations of the resources, policies and permissions that will be deployed.
- The blueprint can be used by other tools such as static analysis to help make it more robust.
## The Need for a Human Touch
I need to make it perfectly clear that I am not advocating for [documentation to be automated](https://thenewstack.io/how-to-use-llms-for-dynamic-documentation/) entirely. Living documentation should augment your existing practices and serve as a tool that developers use as a starting point to a comprehensively documented system. The key here is that if we can autogenerate specifications that can be used to drive software automation, we can also use this same process to generate accurate specifications and documentation, which we can then enhance with the human touch for completeness.

## What About LLMs?
Combining software that produces living documentation with large language models (LLMs) can significantly enhance the quality and relevance of documentation. I don’t mean by passing your entire code base into the LLM, which would be tedious, expensive and time-consuming. Rather, we would pass the living documentation artifacts in.

We can set up continuous content enhancement processes using living documentation and LLMs, where living documentation keeps technical details up to date, and LLMs enhance this content by adding explanations, examples and context that make it more understandable for various audiences.

Starting from dynamic content generation ensures that real-time updates on the system’s current state are used by LLMs to generate relevant, timely content, such as user manuals or troubleshooting guides based on the latest code changes. Since we’re all infatuated with having our systems integrated with chatbots, we can extend this functionality to user queries and interactive documentation so LLMs interact with users in real time, answering their questions using the latest data from the living documentation.

## Better Internal Docs Without Tedium
With modern tools that can automate portions of documentation, we should never have to be “that developer” who passes on applications without documentation. Important details should be automatically captured by our tooling, easily elaborated on with LLMs and continuously available in real time to the next person who jumps into the project.

By adding [Nitric](https://nitric.io/docs/concepts/introduction) to your workflow, you can bridge the communication gap between your developers and operations with a resources specification that communicates your applications needs. As a bonus, if you choose to use Terraform with Nitric, you’ll also have a [Terraform blueprint](https://nitric.io/blog/terraform-providers) that documents the end state that you desire for your infrastructure.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)