AI taking over writing code from developers is not making developers redundant, but it is fundamentally changing [what it means to be a software developer](https://www.aviator.co/blog/software-engineering-ai-2027/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-3-aviator-software-engineering-2027&utm_term=net-new&utm_content=awareness).

In the pre-AI era, the developer experience was about [polishing the tools](https://thenewstack.io/platform-engineering-vs-devops-misses-the-point) and [improving the workflows](https://thenewstack.io/the-anti-metrics-era-of-developer-productivity/). Developers got better integrated development environments (IDEs), slick keyboard shortcuts, pretty dashboards, easy-to-use command line interfaces (CLIs), self-service developer portals, smoother onboarding and intuitive task management processes and tools.

## The Rise of AI Experience

The real DevEx problems — flaky tests, tech debt, inconsistent environments and stale documentation — are still around and will remain important, but the approach will become AI experience (AI-X).

AI-X means focusing on:

* Defining detailed business requirements.
* Designing modular and scalable architecture.
* Creating AI-friendly documentation.
* Using two-tier code reviews.
* Teaching AI constraints using pre-merge quality gates (e.g., linters and tests).

[![Table comparing DevEx and AI-X. DevEx: Manual coding; Human/CI tests; peer-centric review; slow manual approval deployment; logs/metrics/post-deploy feedback; reactive response to issues. AI-X: AI-suggested or -paired programming; AI+local testing, hybrid AI review; fast, automated, staged deployment; incline feedback, predictive alerts; proactive auto-mitigation.](https://cdn.thenewstack.io/media/2025/07/fea14f13-devex-aix-table.png)](https://cdn.thenewstack.io/media/2025/07/fea14f13-devex-aix-table.png)

I’ll explain what each of these means for [software engineers](https://thenewstack.io/software-development/) and [architects](https://roadmap.sh/software-architect) making the transition to the AI-X landscape.

## 1. Defining Detailed Business Requirements

Now that writing code is no longer an edge, software engineers must have strong product thinking skills and deeply understand business problems. They have to clearly define features, explain them in plain English and break them down into small steps.

With AI code generation, your requirements literally become prompts that determine the output. Vague requirements will produce vague code (not unlike [garbage in, garbage out](https://en.wikipedia.org/wiki/Garbage_in,_garbage_out)).

The context window is one of AI’s biggest limitations. While that will improve over time, today, there’s no way to provide an AI system with all possible business contexts. It is your responsibility to provide the “appropriate context” for any work.

Unlike human developers who might express uncertainty (“I think you want X, but let me confirm”), AI models tend to be people pleasers and present every solution as definitive. They don’t question enough and are overconfident about building anything without having enough context.

**Example:** Specify “implement user permissions,” and AI might generate a role-based access control (RBAC) system with admin/user roles. It won’t ask whether you need fine-grained permissions, temporary access controls or integration with existing identity providers. The generated code looks professional and complete, masking the fact that it solves the wrong problem.

Effective AI requirements include:

* Specific input/output formats and data types.
* Explicit business rules and edge cases.
* Integration constraints and existing system dependencies.
* Performance requirements and expected scale.
* Error handling and validation rules.
* Security and compliance requirements.

[!["To replace programmers with AI, clients will need to accurately describe what they want. We're safe."](https://cdn.thenewstack.io/media/2025/07/77a2e739-ai-developers-meme.png)](https://cdn.thenewstack.io/media/2025/07/77a2e739-ai-developers-meme.png)

## 2. Designing Modular and Scalable Architecture

AI is great at greenfield projects, but enterprise tech projects usually don’t work that way. Most software engineering involves incremental improvements, which require understanding the dependencies and impact of a code change on other parts of the code. In a way, AI is good with localized changes but may not understand global architectures well.

Therefore, developers must design an architecture that is modular, scalable and makes such issues easily visible.

**Example:** It’s important to have a clearly defined API spec and dependencies so that when a backward-incompatible change is made, all dependent services are also updated correctly.

AI is also not great at making strategic trade-offs: performance vs. maintainability, consistency vs. availability, security vs. usability. Since AI tools don’t understand business priorities, making the architectural trade-offs requires human judgment.

**Example:** AI generates a microservices architecture because you mentioned “scalability” in your requirements. But your team has three developers, limited DevOps expertise and moderate traffic. A well-designed monolith would be far more appropriate, but AI defaults to the pattern it sees most in training data, not what’s right for your situation.

### How To Design a Better Architecture for AI

**Define the constraints:** AI needs explicit constraints to generate appropriate code. Architects define the technical standards, patterns and boundaries that guide AI code generation.

**Example:** An architect establishes that all services must expose health-check endpoints, use structured logging, implement circuit breakers for external dependencies and follow specific naming conventions. These constraints guide AI to generate code that fits the overall system design.

**Create the integration layer:** While AI can generate individual services, architects can design how those services communicate, share data and coordinate behavior.

**Example:** An architect designs an event-driven architecture with specific message schemas and choreography patterns. AI then generates services that properly emit and consume events according to the established patterns.

**Plan for evolution:** AI generates code for current requirements without considering future needs. Architects think about how systems will change over time and design for extensibility.

**Example:** An architect designs a plugin architecture that allows new AI-generated components to be added without modifying core systems. The architectural framework enables rapid, AI-driven development while maintaining system coherence.

**Ensure operational excellence:** Architects design systems that can be monitored, debugged and maintained in production. They establish the observability, deployment and operational patterns that AI-generated code must follow.

AI can still act as a sounding board to suggest ideas and explore various architectural strategies, but it eventually requires human judgment.

## 3. Creating AI-Friendly Documentation

Up-to-date documentation helps AI agents get the needed context to make accurate and efficient changes. The most common way an AI agent consumes documentation is via [vector search](https://thenewstack.io/top-vector-database-solutions-for-your-ai-project/), a method for retrieving information from a database based on semantic similarity.

Vector search can be used as part of an internal AI workflow or as a [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers) server to provide context to the large language model (LLM). In either case, the documentation has to be AI-friendly.

To do so, create **structured, context-rich documentation** that goes beyond code comments to provide AI tools with business logic, architectural constraints and operational knowledge needed for generating appropriate code.

**Key principle:** Document the “why” and business context, not just the technical “how.”

**Feature specification example:** Instead of: “Build user authentication,” document: “User authentication must support SSO for enterprise customers, require 2FA for admin roles, allow social login for consumer users and maintain session state across mobile/web platforms. Failed login attempts trigger progressive delays (1s, 5s, 30s) and lock accounts after 5 failures.”

**Architecture decision record example:** Instead of: “We use microservices,” document: “ADR-012: Choose microservices for order processing because we need independent scaling of inventory checks (high CPU) vs. payment processing (high I/O), different teams own different services and we require fault isolation, so payment failures don’t break inventory updates.”

## 4. Using Two-Tier Code Reviews

With AI generating so much code, developers will spend the majority of time on [code reviews](https://www.aviator.co/flexreview?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-flexreview&utm_term=net-new&utm_content=awareness).

Reviews must happen in two tiers:

**The first review** is a real-time review that happens as the “author” uses an AI tool in the IDE. During this review, the developer critically assesses what the AI suggests before accepting it. AI output can be deceptively confident and consistent in style, making it easy to overlook hidden assumptions or incorrect logic. Without careful, line-by-line scrutiny, developers risk shipping bugs or vulnerabilities that are harder to spot later.

We need better workflows and tools to help developers handle this step effectively. For example, IDEs could highlight assumptions or prompt the developer to verify them. AI can assist by explaining its reasoning or flagging edge cases, but it’s far from foolproof.

**The second review** is similar to the traditional code review done by a peer. Even with AI in the loop, human oversight remains critical. Peer reviews catch broader architectural issues, misunderstandings of business logic and integration risks that AI might miss entirely.

[Code review is also the team’s record-keeping function](https://www.aviator.co/podcast/code-reviews-looks-good-to-me?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-3-aviator-adrienne-tacke-podcast&utm_term=net-new&utm_content=awareness), ensuring shared understanding within the team, consistent standards and knowledge transfer. In fact, as AI generates more boilerplate or routine code, human reviewers will need to focus more on design, correctness and maintainability.

## 5. Teaching AI Constraints Using Pre-Merge Quality Gates

Transform linters, formatters and testing frameworks from simple validators into contextual guides that teach AI about your system’s patterns, constraints and business logic.

### Enhanced Linters

Create linting rules that enforce your specific design patterns and business constraints.

**Example:** A custom ESLint rule flags when new API endpoints don’t include rate-limiting middleware, teaching AI that all endpoints need this protection.

### Contextual Formatters

* **Pattern-aware formatting:** Configure formatters to enforce architectural consistency beyond just syntax.
* **Documentation integration:** Format code to highlight documented patterns and relationships.

**Example:** A prettier configuration that enforces consistent import ordering (domain → infrastructure → external), so AI can learn your layered architecture from the code structure.

### Intelligent Tests

* **Behavior-driven test names:** Write test descriptions that explain business scenarios, not just technical assertions.
* **Constraint documentation:** Use tests to document business rules and edge cases that AI should understand.

**Example 1: Business-aware test:**

|  |  |
| --- | --- |
|  | test('premium\_users\_bypass\_rate\_limiting\_but\_still\_get\_logged\_for\_monitoring', () => {    // Test teaches AI about user tiers AND monitoring requirements  }); |

**Example 2: Architectural constraint test:**

|  |  |
| --- | --- |
|  | test('all\_external\_api\_calls\_must\_include\_circuit\_breaker\_pattern', () => {    // Test enforces and teaches AI about resilience patterns  }); |

## AI-X: Shorten the Loop Without Losing Safety

The AI-X approach transforms your development tools into AI training systems that continuously reinforce your architectural decisions, business rules and quality standards. Developer experience was about “making developers happy,” while AI experience is about “shortening the loop without loss of safety.”

AI will become more capable of handling mundane tasks like [code migrations](https://www.aviator.co/blog/aviator-agents-code-migration/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-agents-blog&utm_term=net-new&utm_content=awareness) and improving test coverage, but it will continue to need developers for better architecture designs and decision-making.

This means building systems that tightly couple changes to feedback, making rollback paths and continuous integration and delivery core to developers’ workflow, and designing for low-friction, high-trust automation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, an AI-powered, low-config developer portal that automates ownership, code reviews, merges and deploys. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on developer experience,...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)