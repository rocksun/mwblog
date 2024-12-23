# Use These AI Workflows To Reduce Your Technical Debt
![Featued image for: Use These AI Workflows To Reduce Your Technical Debt](https://cdn.thenewstack.io/media/2024/10/ecb08d21-chris-ried-ieic5tq8ymk-unsplash-1024x684.jpg)
[Chris Ried](https://unsplash.com/@cdr6934?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-computer-screen-with-a-bunch-of-code-on-it-ieic5Tq8YMk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Technical debt is often [a key drag on innovation](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/) in many software development organizations, especially in the build and test processes. As a codebase grows and complexity rises, quick fixes and legacy systems pile up, creating inefficiencies that slow down builds, increase testing times, and introduce brittle dependencies.

What starts as minor trade-offs to meet immediate goals[ can snowball into significant bottlenecks](https://thenewstack.io/balancing-ai-innovation-and-tech-debt-in-the-cloud/), making it harder to scale and iterate. Addressing this debt is crucial for software organizations aiming to maintain agility, ensuring their CI/CD pipelines remain fast, reliable, and capable of supporting rapid feature delivery.

Yet, at the same time, it often seems an intractable problem. We know we should invest, and we try to make headway, but it feels like we’re swimming upstream. Despite our investments, technical debt continues to build up.

Some [have offered AI](https://thenewstack.io/how-to-use-self-healing-code-to-reduce-technical-debt/) as a way out. Wouldn’t it be great to point an AI at your infra, and it would magically start to get better? As a level-headed engineer with over 20 years of experience, I’ve learned to ignore vendor hype and silver-bullet pipedreams. But it turns out that, in this case, there may be something there.

Have you heard of Agentic Workflows? This new AI approach offers incredible promise, and it’s an area I’ve been investing in substantially over the past few months, as it may offer our best chance of tackling the vast amounts of technical debt we’ve all amassed.

### For Those Not Familiar With Agentic Workflows, Here’s a Quick Primer:
Agentic workflows are ones where autonomous software agents take on tasks that traditionally require human decision-making or intervention.

Key desired characteristics:

**Autonomous**: Agents should operate independently of human direction, executing tasks based on predefined rules or AI-driven algorithms without needing prompts or directions from humans**Act proactively**: Agents need the ability to anticipate needs, initiate actions, or make recommendations based on changing conditions or patterns**Adapt to changes**: Unlike rigid scripts or manual processes, we want agents to adapt to real-time data, unexpected changes, or new requirements, reconfiguring workflows as needed**Make decisions**: Agents should be able to make complex decisions by analyzing data, weighing options, and determining the best course of action within the workflow’s context**Goal-Oriented**: Agentic workflows should focus on achieving specific outcomes rather than just completing predefined steps.
Agentic workflows promise to [transform how we test and build software](https://thenewstack.io/ebooks/generative-ai/how-generative-ai-transforms-software-development/), but we have to start somewhere. I decided to pick a low-hanging fruit plaguing my organization to demonstrate the potential power of AI in software development pipelines.

## Picking a Tractable Problem: Code Coverage
In many organizations, ensuring complete code coverage can be daunting. How much of our codebase should be tested by automated unit tests? Developers often must balance deadlines and quality, resulting in rushed code without sufficient tests. This lack of test coverage introduces risk, as untested parts of the code might contain bugs or incompatibilities.

Where can AI help?

**Generating Unit Tests**: Using AI to generate unit tests for untested parts of the code automatically**Coverage Reports**: Using coverage reports to identify areas where testing is insufficient, then prompting the AI to generate tests for these areas
## Leveraging a New Type of Container Engine — Dagger
Traditional build tooling, CI platforms, and container engines like Docker have their place but don’t provide the required capabilities to enable us to achieve what we need by ourselves. A few years ago, I started playing with Dagger, the new pipeline-focused container engine being developed by Solomon Hykes and the early technical team behind Docker. The more time I spend with Dagger, the more I see its potential to transform how we fundamentally manage our software pipelines.

Why do I love Dagger? Because it streamlines the creation and deployment of workflows by providing an abstraction layer over complex pipeline systems. Dagger allows developers to automate and distribute tasks across [environments using containers](https://thenewstack.io/interconnect-security-risks-to-protect-your-kubernetes-environment/). It is instrumental in managing dependencies, containerization, and CI/CD pipelines while also allowing developers to customize their workflows through modular design. In this case, Dagger is critical in managing the infrastructure behind the agentic workflow. The system uses Dagger to create, run, and manage Docker containers encapsulating the AI’s generated code. This ensures that the code is executed in a consistent environment.

But what about Docker? We still use it, but for what it’s designed for. The generated code [runs in Docker containers](https://thenewstack.io/tutorial-create-a-docker-image-from-a-running-container/), allowing consistent and isolated testing environments. Dagger integrates seamlessly with Docker, making it easier to manage containerized workflows without manual oversight.

Could I have done this without Dagger? Sure, but Dagger dramatically simplifies the process of handling the dependencies. In my initial design, managing various dependencies for the AI code generation tool was cumbersome. Dagger helped reduce complexity by automatically handling dependencies at runtime.

**AI-Generated Unit Tests**
I started by building a pilot that creates a workflow using AI to generate unit tests. The AI analyzes coverage reports and generates test cases based on uncovered code. Here’s how the process works:

**AI Generation**: The AI generates code based on the gaps identified in the coverage report.**Execution and Error Handling**: The generated code is executed in a container where errors are detected.**Feedback Loop**: If errors are found, the AI takes that feedback and improves its generated code, creating a continuous improvement loop.
**The Role of Continuous Integration Platforms**
Integrating a workflow into a CI pipeline allows the generated unit tests to be automatically tested whenever new code is pushed to the repository. This ensures that every code submission is validated for quality and correctness, reducing the risk of introducing bugs into production.

**The Self-Corrective Loop**
The key innovation here is to create a self-corrective loop, where AI-generated code is refined in each iteration. The loop works as follows:

- The AI generates an initial solution based on the input data.
- The code is executed, and errors (if any) are returned.
- These errors are fed back into the AI model, allowing it to improve the next iteration.
- This process repeats until the code runs successfully or a predefined number of iterations is reached.
This loop makes the system increasingly accurate over time, solving the common issues of incomplete or incorrect code generation. This pilot’s loop was used to refine the AI’s ability to generate functional unit tests.

**Developer Interface: VS Code Extension and Distributed CLI**
Initially, I built this as a VS Code extension that could generate unit tests. However, I quickly saw this would make it hard to scale the extension across different development environments. Since developers in large organizations use many editors, I would need to create multiple versions of the extension to support all my developers.

A more elegant version was to leverage Dagger to create a distributed CLI that could run the AI model and generate tests without relying on a specific editor. This allowed for a more flexible solution that could be used across different tools, removing the need to build editor-specific extensions.

**Expanding the Use of AI in Pipelines**
The potential applications of this agentic workflow are vast. Beyond generating unit tests, I see the potential to expand the system to perform other code-related tasks, such as:

**Refactoring Code**: AI could suggest refactors to make code more efficient or more accessible to test.**Continuous Code Reviews**: AI could participate in pull requests by automatically generating comments or suggestions for improvement.**Self-Healing Workflows**: The system could automatically generate fixes for issues detected during testing, allowing the AI to suggest changes and implement them as well.
Kambui plans to develop plugins for Python and other [programming languages](https://thenewstack.io/programming-languages/) to add support for multiple programming languages, enabling more widespread use of the workflow across different projects.

**Conclusion**
The integration of AI into software development has the potential to significantly reduce the time and effort required for manual tasks like writing unit tests and performing code reviews. My early explorations have demonstrated how we can leverage off-the-shelf AI tools together with the emerging Dagger open source framework to create scalable, distributed workflows that use AI to automate and improve these processes. Implementing systems with a self-corrective loop should lead to higher code quality while reducing the testing burden on developers.

This agentic workflow is a powerful tool for today’s development teams and a glimpse into the future of AI-augmented development. We sit in an exciting time. I expect AI will transform many common tasks in our workplaces. It’s exciting to see where it might significantly improve the building and testing of the software that is critical to our companies and lives.

If you’re interested in seeing a running instance of this, you can take a look at a demo of my pilot project here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)