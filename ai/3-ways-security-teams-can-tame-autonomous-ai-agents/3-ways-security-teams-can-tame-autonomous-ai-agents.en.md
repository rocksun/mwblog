Security professionals understand the dangers of internal threats: adversaries or individuals with harmful objectives who operate from within the enterprise, whether as staff members, vetted third-party vendors or partner organizations with elevated permissions.

However, we’re witnessing the emergence of a different category of internal actor that lacks malicious intent but also operates without human consciousness. Autonomous AI systems, despite functioning as proxies for their human operators, are positioned to supplant traditional decision-making processes and reveal [vulnerabilities in established access control mechanisms](https://thenewstack.io/ai-agents-are-a-security-ticking-time-bomb/).

[AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) have already shown how they challenge traditional authorization systems. This is one area of security that organizations must reevaluate or risk unleashing chaos within software environments.

## **What Works for Humans Doesn’t Work for Agents**

Authorization, or AuthZ, is about managing users’ access to resources: ensuring that users can only do what they’re permitted to do.

However, it’s important to note that AuthZ systems don’t necessarily prevent everything users might try to do. Most existing AuthZ systems are threat modeled and built on the assumption that external factors such as laws, social censure risk or habit will limit human misbehavior.

As a result, it isn’t usually a problem when an AuthZ system over-provisions access. Over-provisioning occurs all of the time. For instance, when someone has just joined a company, it’s easier to copy an existing set of roles to their account rather than think carefully about what they need access to. Until now, the external factors mentioned earlier have meant this approach usually hasn’t caused significant problems.

As AI agents seek to accomplish their tasks, they have no such constraints. Consequently, agents acting on behalf of humans may start to expose those users’ over-provisioned access rights and roles.

## Three Ways To Strengthen AI Governance

Security teams can reduce agentic security risk for their AuthZ systems by proactively embracing emerging best practices. Effective governance will make all the difference, and organizations can start by focusing on three areas:

### 1. Assign Composite Identities

Right now, [authentication (AuthN) and AuthZ systems](https://thenewstack.io/how-do-authentication-and-authorization-differ/) cannot differentiate between human users and AI agents. When AI agents perform actions, they act on behalf of human users or use an identity assigned to them based on a human-centric AuthN and AuthZ system.

That complicates the process of answering formerly simple questions, like: Who authored this code? Who initiated this merge request? Who created this git commit?

It also raises new questions, such as: Who told the AI agent to generate this code? What context did the agent need to build it? What resources did the AI have access to?

[Composite identities](https://docs.gitlab.com/development/ai_features/composite_identity/) give you a way to answer these questions by connecting an AI agent’s identity with the human directing it. When an AI agent attempts to access a resource, its request can now be securely authorized and authenticated.

### 2. Adopt Comprehensive Monitoring Frameworks

Operations, development and security teams need ways to monitor the activities of AI agents across multiple workflows, processes and systems. It’s not enough to know what an agent is doing in a codebase, for instance. Companies must also track agent activity in staging and production environments, as well as in associated databases and any applications to which it may have access.

Eventually, organizations might even start to use Autonomous Resource Information Systems (ARIS) that parallel existing Human Resource Information Systems (HRIS), enabling teams to maintain profiles of autonomous agents, document their capabilities and specializations and manage their operational boundaries.

### 3. Embrace Transparency and Accountability

With or without sophisticated monitoring frameworks, organizations and their employees need to be transparent about when they deploy AI. They need to establish clear accountability structures for autonomous AI agents. Humans need to regularly review the actions and outputs of agents, and more importantly, someone needs to be accountable should the agent exceed its bounds.

## **Prioritizing Responsible AI Deployment**

The nondeterministic nature of AI agents will bring remarkable innovations and breakthroughs within software development. They will also certainly push the boundaries of existing AuthZ systems. But they don’t need to become agents of chaos.

Security frameworks typically evolve more slowly than technological capabilities, requiring us to find an equilibrium between progress and protection. An appropriate comparison is the shift to cloud computing over the past decade. Responsible adoption begins with establishing the right governance frameworks now, so agents become trusted partners to software development teams.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/af8914a1-cropped-fcbb0ca2-josh-lemos-600x600.jpeg)

Josh Lemos is the chief information security officer at GitLab Inc., where he brings 20 years of experience leading information security teams to his role. Josh has led security teams at numerous high-growth technology companies including ServiceNow, Cylance and most...

Read more from Josh Lemos](https://thenewstack.io/author/josh-lemos/)