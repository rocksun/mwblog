APR 09, 2025

AI agents offer a unique opportunity to help people be more productive by autonomously handling many daily recurring or complex tasks. Today, enterprises are increasingly building and deploying autonomous agents to help scale, automate and enhance processes throughout the workplace–from ordering new laptops, to aiding customer service representatives, to assisting in supply chain planning.
To maximize the benefits from agentic AI, it is critical for these agents to be able to collaborate in a dynamic, multi-agent ecosystem across siloed data systems and applications. Enabling agents to interoperate with each other, even if they were built by different vendors or in a different framework, will increase autonomy and multiply productivity gains, while lowering long-term costs.

**Today, we’re launching a new, open protocol called Agent2Agent (A2A), with support and contributions from more than 50 technology partners** like Atlassian, Box, Cohere, Intuit, Langchain, MongoDB, PayPal, Salesforce, SAP, ServiceNow, UKG and Workday; and leading service providers including Accenture, BCG, Capgemini, Cognizant, Deloitte, HCLTech, Infosys, KPMG, McKinsey, PwC, TCS, and Wipro. The A2A protocol will allow AI agents to communicate with each other, securely exchange information, and coordinate actions on top of various enterprise platforms or applications. We believe the A2A framework will add significant value for customers, whose AI agents will now be able to work across their entire enterprise application estates.
This collaborative effort signifies a shared vision of a future when AI agents, regardless of their underlying technologies, can seamlessly collaborate to automate complex enterprise workflows and drive unprecedented levels of efficiency and innovation.

A2A is an open protocol that complements Anthropic's Model Context Protocol (MCP), which provides helpful tools and context to agents. Drawing on Google's internal expertise in scaling agentic systems, we designed the A2A protocol to address the challenges we identified in deploying large-scale, multi-agent systems for our customers. A2A empowers developers to build agents capable of connecting with any other agent built using the protocol and offers users the flexibility to combine agents from various providers. Critically, businesses benefit from a standardized method for managing their agents across diverse platforms and cloud environments. We believe this universal interoperability is essential for fully realizing the potential of collaborative AI agents.

A2A is an open protocol that provides a standard way for agents to collaborate with each other, regardless of the underlying framework or vendor. While designing the protocol with our partners, we adhered to five key principles:

**Embrace agentic capabilities**: A2A focuses on enabling agents to collaborate in their natural, unstructured modalities, even when they don’t share memory, tools and context. We are enabling true multi-agent scenarios without limiting an agent to a “tool.”
**Build on existing standards:**The protocol is built on top of existing, popular standards including HTTP, SSE, JSON-RPC, which means it’s easier to integrate with existing IT stacks businesses already use daily.
**Secure by default**: A2A is designed to support enterprise-grade authentication and authorization, with parity to OpenAPI’s authentication schemes at launch.
**Support for long-running tasks:**We designed A2A to be flexible and support scenarios where it excels at completing everything from quick tasks to deep research that may take hours and or even days when humans are in the loop. Throughout this process, A2A can provide real-time feedback, notifications, and state updates to its users.
**Modality agnostic:**The agentic world isn’t limited to just text, which is why we’ve designed A2A to support various modalities, including audio and video streaming.
A2A facilitates communication between a "client" agent and a “remote” agent. A client agent is responsible for formulating and communicating tasks, while the remote agent is responsible for acting on those tasks in an attempt to provide the correct information or take the correct action. This interaction involves several key capabilities:

**Capability discovery:**Agents can advertise their capabilities using an “Agent Card” in JSON format, allowing the client agent to identify the best agent that can perform a task and leverage A2A to communicate with the remote agent.
**Task management:**The communication between a client and remote agent is oriented towards task completion, in which agents work to fulfill end-user requests. This “task” object is defined by the protocol and has a lifecycle. It can be completed immediately or, for long-running tasks, each of the agents can communicate to stay in sync with each other on the latest status of completing a task. The output of a task is known as an “artifact.”
**Collaboration:**Agents can send each other messages to communicate context, replies, artifacts, or user instructions.
**User experience negotiation:**Each message includes “parts,” which is a fully formed piece of content, like a generated image. Each part has a specified content type, allowing client and remote agents to negotiate the correct format needed and explicitly include negotiations of the user’s UI capabilities–e.g., iframes, video, web forms, and more.
See the full details of how the protocol works in our [draft specification](https://github.com/google/A2A).

right click to view in new tab

Hiring a software engineer can be significantly simplified with A2A collaboration. Within a unified interface like Agentspace, a user (e.g., a hiring manager) can task their agent to find candidates matching a job listing, location, and skill set. The agent then interacts with other specialized agents to source potential candidates. The user receives these suggestions and can then direct their agent to schedule further interviews, streamlining the candidate sourcing process. After the interview process completes, another agent can be engaged to facilitate background checks. This is just one example of how AI agents need to collaborate across systems to source a qualified job candidate.

The future of agent interoperability

A2A has the potential to unlock a new era of agent interoperability, fostering innovation and creating more powerful and versatile agentic systems. We believe that this protocol will pave the way for a future where agents can seamlessly collaborate to solve complex problems and enhance our lives.

We’re committed to building the protocol in collaboration with our partners and the community in the open. We’re releasing the protocol as open source and setting up clear pathways for contribution.

Review the [full specification draft](https://github.com/google/A2A), try out code samples, and see example scenarios on the [A2A website](https://google.github.io/A2A) and learn how you can contribute.

We are working with partners to launch a production-ready version of the protocol later this year.

We're thrilled to have a growing and diverse ecosystem of partners actively contributing to the definition of the A2A protocol and its technical specification. Their insights and expertise are invaluable in shaping the future of AI interoperability.

Here's what some of our key partners are saying about the A2A protocol:

Technology & Platform Partners

Ask-AI is excited to collaborate with Google on the A2A protocol, shaping the future of AI interoperability and seamless agent collaboration, advancing its leadership in Enterprise AI for Customer Experience.
– CEO Alon Talmor PhD
With Atlassian's investment in Rovo agents, the development of a standardized protocol like A2A will help agents successfully discover, coordinate, and reason with one another to enable richer forms of delegation and collaboration at scale.
– Brendan Haire VP, Engineering of AI Platform. Atlassian
At Articul8, we believe that AI must collaborate and interoperate to truly scale across the enterprise. We’re excited to support the development of the A2A interoperability protocol – an initiative that aligns perfectly with our mission to deliver domain-specific GenAI capabilities that seamlessly operate across complex systems and workflows. We’re enabling Articul8's ModelMesh (an 'Agent-of-Agents') to treat A2A as a first-class citizen, enabling secure, seamless communication between intelligent agents.
–Arun Subramaniyan, Founder & CEO of Articul8
Arize AI is proud to partner with Google as a launch partner for the A2A interoperability protocol, advancing seamless, secure interaction across AI agents as part of Arize's commitment to open-source evaluation and observability frameworks positions.
– Jason Lopatecki, Cofounder & CEO, Arize AI
**BCG**
BCG helps redesign organizations with intelligence at the core. Open and interoperable capabilities like A2A can accelerate this, enabling sustained, autonomous competitive advantage.
–Djon Kleine, Managing Director & Partner at BCG
We look forward to expanding our partnership with Google to enable Box agents to work with Google Cloud’s agent ecosystem using A2A, innovating together to shape the future of AI agents while empowering organizations to better automate workflows, lower costs, and generate trustworthy AI outputs.
– Ketan Kittur, VP Product Management, Platform and Integrations at Box
At C3 AI, we believe that open, interoperable systems are key to making Enterprise AI work and deliver value in the real world–and A2A has the potential to help customers break down silos and securely enable AI agents to work together across systems, teams, and applications.
–Nikhil Krishnan - C3 AI SVP and Chief Technology Officer, Data Science
A2A will enable reliable and secure agent specialization and coordination to open the door for a new era of compute orchestration, empowering companies to deliver products and services faster, more reliably, and enabling them to refocus their engineering efforts on driving innovation and value.
– Rob Skillington, Founder /CTO
At Cohere, we’re building the secure AI infrastructure enterprises need to adopt autonomous agents confidently, and the open A2A protocol ensures seamless, trusted collaboration—even in air-gapped environments—so that businesses can innovate at scale without compromising control or compliance.
– Autumn Moulder, VP of Engineering at Cohere
A2A enables intelligent agents to establish a direct, real-time data exchange, simplifying complex data pipelines to fundamentally change how agents communicate and facilitate decisions.
– Pascal Vantrepote, Senior Director of Innovation, Confluent
A2A opens the door to a new era of intelligent, real-time communication and collaboration, which Cotality will bring to clients in home lending, insurance, real estate, and government—helping them to improve productivity, speed up decision-making.
– Sachin Rajpal, Managing Director, Data Solutions, Cotality
DataStax is excited to be part of A2A and explore how it can support Langflow, representing an important step toward truly interoperable AI systems that can collaborate on complex tasks spanning multiple environments.
– Ed Anuff, Chief Product Officer, DataStax
We're excited to see Google Cloud introduce the A2A protocol to streamline the development of sophisticated agentic systems, which will help Datadog enable its users to build more innovative, optimized, and secure agentic AI applications.
– Yrieix Garnier, VP of Product at Datadog
Supporting the vision of open, interoperable agent ecosystems, Elastic looks forward to working with Google Cloud and other industry leaders on A2A and providing its data management and workflow orchestration experience to enhance the protocol.
– Steve Kearns, GVP and GM of Search, Elastic
A2A has the potential to accelerate GrowthLoop's vision of Compound Marketing for our customers—enabling our AI agents to seamlessly collaborate with other specialized agents, learn faster from enterprise data, and rapidly optimize campaigns across the marketing ecosystem, all while respecting data privacy on the customer's cloud infrastructure.
– Anthony Rotio, Chief Data Strategy Officer, GrowthLoop
Harness is thrilled to support A2A and is committed to simplifying the developer experience by integrating AI-driven intelligence into every stage of the software lifecycle, empowering teams to gain deeper insights from runtime data, automate complex workflows, and enhance system performance.
– Gurashish Brar, Head of Engineering at Harness.
Incorta is excited to support A2A and advance agent communication for customers,making the future of enterprise automation smarter, faster, and truly data-driven.
– Osama Elkady CEO Incorta
Intuit strongly believes that an open-source protocol such as A2A will enable complex agent workflows, accelerate our partner integrations, and move the industry forward with cross-platform agents that collaborate effectively.
– Tapasvi Moturu, Vice President, Software Engineering for Agentic Frameworks, at Intuit
We’re excited to be a launch partner for A2A, an initiative that enhances agentic collaboration and brings us closer to a truly multi-agent world, empowering developers across JetBrains IDEs, team tools, and Google Cloud.
– Vladislav Tankov, Director of AI, JetBrains
JFrog is excited to join the A2A protocol, an initiative we believe will help to overcome many of today’s integration challenges and be a key driver for the next generation of agentic applications.
– Yoav Landman, CTO and Co-founder, JFrog
A2A is a key step toward realizing the full potential of AI agents, supporting a future where AI can truly augment human capabilities, automate complex workflows and drive innovation.
– Manu Sharma Founder & CEO
LangChain believes agents interacting with other agents is the very near future, and we are excited to be collaborating with Google Cloud to come up with a shared protocol which meets the needs of the agent builders and users.
– Harrison Chase Co-Founder and CEO at LangChain
By combining the power of MongoDB’s robust database infrastructure and hybrid search capabilities with A2A and Google Cloud’s cutting edge AI models, businesses can unlock new possibilities across industries like retail, manufacturing, and beyond to redefine the future of AI applications.
– Andrew Davidson, SVP of Products at MongoDB
Neo4j is proud to partner with Google Cloud, combining our graph technology's knowledge graph and GraphRAG capabilities with A2A to help organizations unlock new levels of automation and intelligence while ensuring agent interactions remain contextually relevant, explainable and trustworthy.
– Sudhir Hasbe, Chief Product Officer at Neo4j
We believe the collaboration between Google Cloud’s A2A protocol and New Relic’s Intelligent Observability platform will provide significant value to our customers by simplifying integrations, facilitating data exchange across diverse systems, and ultimately creating a more unified AI agent ecosystem.
– Thomas Lloyd, Chief Business and Operations Officer, New Relic
We’re proud to partner on Google Cloud’s A2A protocol, which will be a critical step toward enabling AI agents to work together effectively, while maintaining trust and usability at scale.
–Rahul Jain, Co-founder & CPO at Pendo
PayPal supports Google Cloud’s A2A protocol, which represents a new way for developers and merchants to create next-generation commerce experiences, powered by agentic AI.
-Prakhar Mehrotra, SVP & Head of Artificial Intelligence at PayPal
SAP is committed to collaborating with Google Cloud and the broader ecosystem to shape the future of agent interoperability through the A2A protocol—a pivotal step toward enabling SAP Joule and other AI agents to seamlessly work across enterprise platforms and unlock the full potential of end-to-end business processes.
– Walter Sun, SVP & Global Head of AI Engineering
Salesforce is leading with A2A standard support to extend our open platform, enabling AI agents to work together seamlessly across Agentforce and other ecosystems to turn disconnected capabilities into orchestrated solutions and deliver an enhanced digital workforce for customers and employees.
– Gary Lerhaupt, VP Product Architecture
ServiceNow and Google Cloud are collaborating to set a new industry standard for agent-to-agent interoperability, and we believe A2A will pave the way for more efficient and connected support experiences.
– Pat Casey, Chief Technology Officer & EVP of DevOps, ServiceNow
With Google Cloud’s A2A protocol and Supertab Connect, agents will be able to pay for, charge for, and exchange services — just like human businesses do.
– Cosmin Ene, Founder of Supertab
We're thrilled at UKG to be collaborating with Google Cloud on the new A2A protocol, a framework that will allow us to build even smarter, more supportive human capital and workforce experiences that anticipate and respond to employee needs like never before.
– Eli Tsinovoi, Head of AI at UKG
Weights & Biases is proud to collaborate with Google Cloud on the A2A protocol, setting a critical open standard that will empower organizations to confidently deploy, orchestrate, and scale diverse AI agents, regardless of underlying technologies.
– Shawn Lewis, CTO and co-founder at Weights & Biases
Services Partners

The multi-agent A2A protocol from Google Cloud is the bridge that will unite domain specific agents across diverse platforms to solve complex challenges, enabling seamless communication and collective intelligence for smarter and effective agentic solutions.
– Scott Alfieri, AGBG Global lead, Accenture
Agent-to-agent interoperability is a foundational element of enabling the evolution of agentic AI architectures, and Google Cloud’s A2A initiative to bring together an ecosystem of technology industry participants to co-develop and support this protocol will immensely accelerate agentic AI adoption.
– Gopal Srinivasan, Deloitte
We are already leading the way in the A2A space by focusing on industry solutions that provide real business value—saving time, reducing overhead and helping our clients drive revenue and enhance processes like the development of FDA documentation during the drug discovery process.
– Marc Cerro, VP of Global Google Cloud Partnership at EPAM
HCLTech is at the forefront of the agentic enterprise, and we are proud to partner with Google Cloud in defining agent-to-agent interoperability and advancing agentic AI possibilities through the open A2A standard.
– Vijay Guntur, Chief Technology Officer and Head of Ecosystems, HCLTech
At KPMG, we are excited to be part of this emerging initiative as A2A provides the essential standard we need for different AI agents to truly collaborate effectively and responsibly, which will enable customers and businesses to seamlessly harness AI for innovation and efficiency gains.
– Sherif AbdElGawad, Partner, Google Cloud & AI Leader, KPMG
**Quantiphi**
The ability for agents to dynamically discover capabilities and build user experiences across platforms is crucial for unlocking the true potential of enterprises. We see the A2A protocol as a pivotal step to empower businesses to build such interoperable agents.
-Asif Hasan, Co-founder of Quantiphi
The A2A protocol is the foundation for the next era of agentic automation, where Semantic Interoperability takes prominence, and we're proud to lead this transformative journey.
– Anupam Singhal, President, Manufacturing business, Tata Consultancy Services (TCS)
Because the future of AI lies in seamless collaboration, open protocols like A2A will be the foundation of an ecosystem where AI agents drive innovation at scale.
– Nagendra P Bandaru, Managing Partner and Global Head – Technology Services (Wipro)
Learn more about A2A

To learn more about the A2A framework, delve into the [ full specification draft](https://github.com/google/A2A) and explore

We encourage you to contribute to the protocol's evolution and help us define the future of agent interoperability by [submitting ideas](https://docs.google.com/forms/d/e/1FAIpQLScS23OMSKnVFmYeqS2dP7dxY3eTyT7lmtGLUa8OJZfP4RTijQ/viewform), [contributing to the documentation](https://github.com/google/A2A/blob/main/CONTRIBUTING.md), and engaging with the community.