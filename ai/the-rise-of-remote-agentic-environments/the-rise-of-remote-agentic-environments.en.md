Imagine a scenario where a team of developers assigns this task to an AI system: “Migrate our user authentication from JWT tokens to OAuth 2.1 with PKCE, ensuring backward compatibility.”

The AI system spawns specialized agents to work in parallel. One agent analyzes the codebase, asks clarifying questions and creates a migration plan. Another implements OAuth handlers, a third builds compatibility layers, a fourth generates test suites and the fifth builds and validates the results.

The development team (humans) reviews progress, approves plans and makes strategic decisions, while a coordinator agent manages dependencies and escalates conflicts, allowing the developers to focus on high-level guidance rather than implementation details.

I’m neither talking about vibe coding nor about a doomsday where all developers lose their jobs. Rather, I’m observing the [evolution of software development](https://thenewstack.io/how-to-think-about-devex-when-ai-writes-the-code).

## The Rise of Coding Agents

The shift in [how software engineers use AI tools](https://thenewstack.io/how-top-tech-teams-use-ai-to-boost-dev-productivity) is already here. Every major AI-coding company has launched command line interface (CLI) coding agents. These tools are enabling more autonomous workflows with limited user interactions.

Instead of developers working with AI tools, we’re moving toward [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) working for developers, taking on entire categories of work that were previously manual and time-consuming.

AI coding agents are often compared to junior developers who can complete a task given clear instructions. This works fine for building a cool website or creating a viral to-do app. But we can’t rely only on junior developers to manage enterprise software that’s messy, complicated or contains a lot of business nuances and tribal knowledge stuck in stale documents.

## Enter Remote Agentic Environments

Think about [remote agentic environments](https://runbooks.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-9-runbooks&utm_term=net-new&utm_content=awareness) as a new paradigm where AI agents operate in cloud-based development environments (public or private cloud), understand natural language instructions, continuously learn about business context, plan complex multistep tasks and execute them autonomously.

Similar to cloud development environments meant for developers to build and test, these systems are primarily meant for AI agents to work independently, asking clarifying questions and seeking approval for significant changes.

The key requirements for such environments include:

* **Access to codebase:** Agents can interact with git to fetch the entire codebase, create pull requests and get feedback from pull requests to rework changes.
* **Context:** Perhaps the most important piece. These systems maintain state and memory, learning from past actions and adapting future behavior based on project patterns and team preferences.
* **Build environment:** Agents can build, run and test code. Most agentic tools work in multiple steps, so it’s important that they can compile code, run tests and verify changes. This improves the quality by adding feedback loops.
* **Natural language interface:** Developers interactively work with the agents on scoping out the requirements and planning the tasks.
* **Tools used:** Similar to the IDE-based AI tool, the agents can connect with additional tools using [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/). Unlike IDEs, these environments can limit which MCPs can be used.

## Advantages of Remote Agentic Environments

This framework has several advantages over an IDE-based AI tool.

### Scalability

Remote agentic environments are scalable independent of human resources. You can allocate multiple agentic environments to each developer or have multiple developers share the same resources using:

* **Resource optimization:** Compute resources are allocated based on actual task requirements rather than developer availability. Complex compilation tasks, large-scale testing and data-intensive operations can access high-performance resources without impacting developer workstations. These resources can be scaled up or down on demand.
* **Parallel execution:** Multiple independent tasks can execute simultaneously, coordinated by multiple team members together or independently.

### Automatic Context Management

Remote agentic environments continuously pull context from code repositories, reviews and past changes, building a knowledge base that evolves with the code.

* **Leverage context:** Feedback from pull requests is regularly captured to refine the context.
* **Reduce onboarding time:** Centralized context makes it easier for new developers to ramp up and understand business needs.
* **Generate live documentation:** Background agents update comments, docstrings and documentation as code changes.
* **Sync across AI tools:** Git-synced context files work across local and remote AI environments.

### Standardized Tooling

Remote agentic environments eliminate the “it works on my machine” problem by providing standardized, fully configured development environments using:

* **Preconfigured environments:** Every necessary build tool, compiler, testing framework and dependency is preinstalled and configured.
* **Consistent setups:** No version mismatches, missing dependencies or configuration drift because every task executes in a known-good environment with predictable behavior.
* **Specialized environments:** A Python machine learning (ML) project can run alongside a Node.js microservice and a legacy Java application, each with its optimal tool-chain versions.
* **Version control for specs:** Teams can track the exact version of the specs and prompts that led to the code generation, leaving little room for guesswork. This also acts as a great lever to course correct.

### Security and Control

These environments provide better security compared to a local setup, as you can control what is installed and what these machines can access by using:

* **Ingress and egress control:** When running on private clouds, you can easily control what URLs the servers can access and restrict all inbound requests, reducing the risk of social engineering or infiltration.
* **API access control:** CLI-agentic tools like Claude Code include context-aware checks that try to detect malicious instructions and block them proactively, with prompt injection safeguards and restricting or disabling risky tools.
* **MCP server governance:** Organizations control exactly which external tools and data sources agents can access, creating a secure sandbox for autonomous operations while maintaining compliance requirements.
* **Audit trails:** Every action taken by an autonomous agent is logged, providing complete traceability for compliance, debugging and process improvement.

## The Agent Planning and Feedback Loop

Planning and feedback capabilities are what distinguish remote agentic environments from earlier automation attempts.

### Task Analysis and Decomposition

When presented with a high-level request like “Migrate our authentication system to OAuth 2.1,” modern agents don’t simply execute predefined scripts. Instead, they:

1. **Analyze the current state:** Scan the codebase to understand the existing authentication implementation, identify all touchpoints and catalog dependencies.
2. **Research best practices:** Query documentation, recent security advisories and implementation patterns to understand OAuth 2.1 requirements and migration strategies.
3. **Plan the migration:** Create a step-by-step implementation plan that minimizes risk, identifies testing requirements and plans for rollback scenarios.
4. **Estimate impact:** Analyze which components will be affected, estimate testing requirements and identify potential breaking changes.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

### **Execution Planning**

The planning phase produces a detailed execution strategy, which human developers review before implementation. This might include:

```
## OAuth 2.1 Migration Plan 

### Phase 1: Infrastructure Preparation (Estimated: 2 hours) 
- Set up OAuth 2.1 provider configuration 
- Update environment variables and secrets 
- Create backward-compatible endpoint stubs
 
### Phase 2: Core Implementation (Estimated: 4 hours) 
- Implement new OAuth 2.1 flow handlers 
- Update token validation logic 
- Modify user session management 

### Phase 3: Integration Update (Estimated: 3 hours) 
- Update frontend authentication calls 
- Modify API middleware 
- Update mobile app authentication 

### Phase 4: Testing and Validation (Estimated: 2 hours) 
- Run comprehensive authentication test suite 
- Validate against security checklist 
- Perform integration testing 

### Rollback Plan 
- Database migration reversal scripts 
- Configuration rollback procedures 
- Emergency authentication bypass mechanism
```

### Human-In-The-Loop Workflows

* **Plan review and approval:** Agents first present their analysis and proposed approach for human review. Developers can modify the plan, add constraints or request alternative approaches.
* **Checkpoint-based execution:** At key milestones, agents pause execution and report progress, allowing developers to verify correctness before proceeding to the next phase.
* **Exception handling and escalation:** When agents run into unexpected situations or ambiguous requirements, they escalate to human developers with context about the issue and suggested resolution approaches.

## Technical, Security and Organizational Challenges

Just like locally generated AI code, remote agentic environments have technical, security and organizational challenges that must be addressed before widespread adoption.

### Technical Challenges

* **Code quality and consistency:** While agents can generate functional code, this does not replace the need for careful review and verification of changes by humans. In fact, with AI generating the code, the human review becomes more critical.
* **Debugging autonomous changes:** Some bugs might be easy to debug with AI, but we will need better logging and explanation so that humans can understand the agent’s reasoning process.
* **Integration complexity:** One flawed output can introduce errors to all downstream agents. If a requirements agent misunderstands a feature, the developer agent may write wrong code, and the tester agent may miss the problem altogether.

### Security and Governance

Security risks always exist, whether the code is written by humans or by AI agents. Even with completely autonomous changes, it’s still the humans’ responsibility to ensure that the code is carefully reviewed and validated. In addition, organizations should establish policies that:

* Have a second reviewer look at mission-critical code changes.
* Use automated security scanning tools.
* Define granular permissions for what agents can access and modify.
* Track what changes were made by which agents and why.

### Organizational Challenges

Most of the AI adoption challenges in large enterprises are organizational, not technological. In every organization, there is a wide spectrum of adoption from true believers to strong opponents.

As [the role of software developers is evolving](https://www.aviator.co/blog/software-engineering-ai-2027/) from code writers to AI orchestrators and system architects, some of the challenges can be solved by rebuilding developer platforms to support this new ecosystem, building trust and confidence in autonomous systems and supporting engineers in learning and adapting to new ways of working.

## Remote Agentic Environments With Runbooks

For remote agentic environments to work at enterprise scale, we need a solid foundation to define and control the actions agents perform. This is what we call [Runbooks](https://runbooks.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-9-runbooks&utm_term=net-new&utm_content=awareness). Teams create runbooks as detailed how-to guides so that everyone on the team, no matter the experience or familiarity with the matter, can easily understand and collaborate.

Runbooks are living documents that capture context from repositories and code reviews, combine it with a team’s AI prompting knowledge and execution patterns, and improve with every use. They serve as clear blueprints, create audit trails for work generated by background agents and form a strong foundation for collaboration in the AI era.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Ankit Jain is a cofounder and CEO of Aviator, an AI-powered, low-config developer portal that automates ownership, code reviews, merges and deploys. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on developer experience,...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)