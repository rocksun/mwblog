Demand for bandwidth continues to surge with increasing use of AI, high-definition video streaming, cloud and 5G mobile applications. In response, optical services need to become more dynamic and meet stricter service-level requirements. Consequently, metro-based networks owned by communications service providers (CSPs) and used for mobile transport, enterprise services or broadband access services face new demands relating to power, multiservice aggregation, security, AI integration and network slicing. Figure 1 shows a rich set of applications in a typical metro network.

[![Figure 1 – A typical metro network supports a rich set of applications](https://cdn.thenewstack.io/media/2025/12/6b732d18-image1.png)](https://cdn.thenewstack.io/media/2025/12/6b732d18-image1.png)

Figure 1 — A typical metro network supports a rich set of applications.

As AI use grows, it will create a force multiplier that will drive significant traffic to [transport networks](https://thenewstack.io/networking/). But the challenging throughput, latency and reliability requirements of AI workloads are already taking network scale and complexity to another level. CSPs are facing unprecedented pressure to deliver more, faster and better.

Figure 2 shows the impact of AI traffic growth based on a recent Nokia Bell Labs study. This growth can range from 14% to 31%.

[![ CSPs’ access and aggregation network (orange) will bear the heaviest load, roughly 31% of the total AI traffic. CSPs’ metro network (pink) is next with 28%, followed by the regional network (blue) with about 14%.](https://cdn.thenewstack.io/media/2025/12/06dad94b-image3a.jpg)](https://cdn.thenewstack.io/media/2025/12/06dad94b-image3a.jpg)

Figure 2 — Traffic growth effects on CSP networks. CSPs’ access and aggregation network (orange) will bear the heaviest load, roughly 31% of the total AI traffic. CSPs’ metro network (pink) is next with 28%, followed by the regional network (blue) with about 14%.

Despite this growth, CSPs are expected to accelerate service turn-up and [mean time to repair](https://thenewstack.io/why-are-we-so-bad-at-mean-time-to-repair-mttr/) to reduce OPEX and maximize returns on infrastructure investments.

Manual processes used for configuring and monitoring largely static optical networks can’t deliver the dynamic connectivity that AI demands. AI-ready optical networks require rapid, efficient service fulfillment and flexibility to offer services that meet specific requirements, such as latency or resilience. Webscalers have addressed these needs through network automation, paving the way for the broader industry to follow.

The opportunity is clear: Automation can reduce errors, simplify operations, accelerate response times and unlock new efficiencies. CSPs can simplify operations, enhance network performance and unlock new monetization opportunities by pairing automation with mature enabling technologies that make transport networks more configurable, such as:

* Reconfigurable optical add-drop multiplexers (ROADMs)
* Coherent pluggables that offer multiple line rate modes
* Timing and frequency synchronization
* Line rate-capable encryption.

## The Growing Adoption of Automation

A [2024 Heavy Reading survey](https://ix.lightreading.com/wp-content/uploads/2024/12/2024.pdf) highlights the growing importance of [network automation](https://thenewstack.io/ai-in-network-observability-the-dawn-of-network-intelligence/). Increasing network complexity and scale drive the need for advanced automation that abstracts underlying infrastructure details and simplifies network operation. A minority of CSPs surveyed continue to operate in a fully manual fashion. Most describe their level of network automation as ranging from “assisted management” to “partial automation,” with systems making meaningful recommendations using real-time data and advanced analytics. Many are planning to move toward highly autonomous networks over the next three years.

## Open Industry Models

For years, network automation was held back by fragmented management systems, proprietary interfaces and workflows, and limited visibility into network performance. Today, these barriers are being lowered with automation frameworks that support standardization from well-known industry forums in communication networks.

Multiple industry forums focus on driving standardization in transport networks, including OpenConfig, OpenROADM, Internet Engineering Task Force (IETF), Linux Foundation, TMForum, Optical Internetworking Forum (OIF) and Innovative Optical and Wireless Network (IOWN) Global Forum. The forums are dedicated to developing architectures and software-abstracted interface layers that promote multivendor ecosystems.

This work helps address a common problem for CSPs:Their brownfield deployments often include equipment from several vendors across all segments of their network. These equipment assets are designed to operate for a long period of time within networks, so CSPs leverage the technology strengths of different vendors to achieve their business outcomes. Consequently, they need compelling reasons to replace equipment, which means they seldom rely on a single vendor.

The industry forums provide the data modeling language or abstract open API protocols required to communicate directly with the network domain layer via network configuration (NETCONF) or representational state transfer configuration (RESTCONF). The modularity of these standards ensures reusability, so automation can scale as new use cases emerge. The model guarantees that state changes and configuration data can be read from and written to the network, enabling developers to create insightful functional logic across the resources that carry services. The typical modeling stack (Figure 3) promotes inclusivity by letting developers use their preferred programming language.

[![Figure 3 – A network automation framework for developers](https://cdn.thenewstack.io/media/2025/12/771aa34e-image2.png)](https://cdn.thenewstack.io/media/2025/12/771aa34e-image2.png)

Figure 3 — A network automation framework for developers

These standards are now ready for automation because they support operations, administration, maintenance, provisioning and reporting, along with advanced features such as photonic impairment modeling for multivendor equipment planning, refined network layer models for complex topologies and the emerging IP over dense wavelength division multiplexing (IPoDWDM) paradigm.

Recent updates to the standards include improved alarm and performance KPI monitoring, streaming telemetry, detailed physical routing information and resiliency route constraints that enable protection-based service requests, all of which can be used for premium, monetizable services. Together, these developments enhance the user experience while meeting the growing capacity demands of applications across multivendor ecosystems.

Standards such as OIF validate the interoperability of multivendor coherent technologies, routers and network elements across multispan networks. They minimize dependencies with specifications that ensure automation use cases will achieve their business outcomes without additional testing for validating vendor-specific technologies.

At the same time, advanced network controllers feature modular software architectures designed around standard data models and open APIs. These architectures facilitate seamless communication southbound into the network and northbound into diverse automation environments. Instead of relying on static network snapshots and limited measurements, teams can now tap into real-time performance metrics from devices across networks. If this influx of data becomes overwhelming, AI/ML techniques can help them analyze massive datasets, detect anomalies and predict behaviors.

Many use cases in the network domain can be automated. CSPs should adopt an incremental approach, starting with simple use cases that address day-to-day logistics such as inventory and service management in the transport network. This is a typical pain point for CSPs because it affects maintenance, supply chains and network design as they increase network capacity or expand the network into new geographical areas.

Next, CSPs can address intermediate operational use cases such as commissioning, configuring and provisioning connections within the network. For many, time to market is often slow for end-subscriber services because of the process of delivering equipment between endpoint locations and the coordination and actions involved in provisioning services for specific SLAs.

Finally, CSPs can address more complex scenarios that require greater automation, such as building closed-loop operations to optimize connectivity and optical links against their desired reach requirements and cross-domain (IP/optical) operations, or to enhance troubleshooting and root-cause detection. These closed-loop-based workflows can then be extended to AI-enabled predictive automation to support use cases such as demand forecasting or soft failure detection, or what-if analysis focused on network resiliency.

## Automation Tools

For network automation, developers need the right tools before they begin creating use cases that involve programmatic interaction with the transport domain via network elements, network controllers or management systems. These tools may include:

* **Workflow management** tools such as OpenStack Mistral for turning manual tasks into automated workflows. These tools help control task execution based on manual, scheduled or event-based triggers. They also monitor tasks, track the progress of running workflows and log errors.
* A **Swagger or Visual Studio Code editor** that enables developers to code and access extensions such as secure shell (SSH) to support remote connections, access remote servers that host product-specific open APIs or create their own sets of API functions. Swagger developer portals are also available for testing and validating the use of vendor-specific APIs. Figure 4 shows an example series of ‘GET’ API calls to the Linux Foundation T-API library.

[![Figure 4 - OpenAPI example using Swagger](https://cdn.thenewstack.io/media/2025/12/8a5277e2-image5.png)](https://cdn.thenewstack.io/media/2025/12/8a5277e2-image5.png)

Figure 4 — OpenAPI example using Swagger.

* A **Python tool** that lets developers use modern programming languages to create scripts or code for workflow tasks.
* **GitHub**, a web-based public or private repository that can store development code. The GitHub platform enables easy sharing, editing and revision control of code, which allows teams to continuously update and correct API code.
* An **optical digital twin**, a virtual, real-time replica of an existing optical communication network, including terminal devices, optical line system elements and optical fiber loss characteristics. CSPs can use a digital twin to safely explore provisioning, commissioning, protection, restoration and optimization scenarios and perform what-if analysis based on real network conditions to identify operational risk. More importantly, they can test and validate APIs without disrupting existing operations on the deployed network. Optical transport network digital twins are not yet fully disaggregated, so they can’t support different vendor network elements in the same system. However, they are cloud-hosted on virtual machines, which allows developers to build workflow logic to support communication between network controllers to enable multinetwork management.

When CSPs or developers use these tools to create their automation workflows, they must ensure that the tools provide the capabilities required to scale those workflows, from simple use cases to more complex ones.

## Guidance on Building Automation Workflows

The flexibility offered by the automation tools and open standard APIs enables CSPs to use automation for use cases such as:

* Adding new capacity quickly, in minutes rather than weeks or months.
* Localizing failures and diagnosing and troubleshooting common issues to reduce mean time to repair.
* Optimizing performance on specific links in the network based on policy-driven rules.
* Compiling customized reports on network inventory resource consumption to support better decision-making on network plans.

A practical way for developers and CSPs to begin this automation journey is to build workflows that define a list of sequential tasks and conditional branches required for a targeted use case, and then use workflow tools to monitor their executional flow. Alternatively, vendors offer consulting services that provide code snippets to help development teams get started with automation, allowing them to ramp up quickly.

Figure 5 shows a conceptual network inventory reporting workflow that could be part of a larger workflow.

[![Figure 5 - Network inventory retrieval workflow](https://cdn.thenewstack.io/media/2025/12/0354a966-image4.png)](https://cdn.thenewstack.io/media/2025/12/0354a966-image4.png)

Figure 5 — Network inventory retrieval workflow.

## AI-Powered Network Automation

The use of AI expands network automation potential even further, driving smarter, more adaptive network operations.

Generative AI-powered conversational assistants are emerging as valuable and easily adaptable tools for operations teams. They can respond to natural language queries, guide troubleshooting, search through relevant documentation and suggest configuration changes, making complex tasks more accessible and shortening resolution times.

With AI-powered automation, developers can troubleshoot network issues, verify actions taken directly in the network and quickly assess the operational state. This improves the user experience and accelerates time-to-delivery.

## Shifting to Autonomous Network Automation

TMForum is a standards alliance that brings together network equipment vendors, CSPs and hyperscalers. It provides blueprints and methodologies that enable CSPs to use standardized open APIs to build modular, AI-enabled solutions. As CSPs work to make their networks more autonomous, TMForum supports them with architectures that enable self-healing and self-optimization, eliminating the need for human intervention.

These standards are prompting network equipment vendors to enhance their platforms with closed-loop automation that encompasses reactive triggers and predictive triggers powered by AI/ML. Closed-loop operations are a prerequisite for fully autonomous networks. The evolving architecture introduces agentic frameworks within network management platforms, which stream KPI data via gNMI or Kafka interfaces, incorporate trend analysis and intelligence, and proactively protect services before SLAs are impacted.

This new framework enables developers to use integrated closed-loop capabilities from the network domain automation layer to create intent-driven workflow use cases. This means they can focus on designing or customizing workflows that automate existing processes and connect directly to northbound operations and business support systems (OSS/BSS).

## It’s Time To Automate!

AI is transforming networks and reshaping the telecom network domain layer, making it easier for developers to reduce operational complexity and improve efficiency. To capitalize on AI, many developers are turning to automation tools and open APIs, which are now more mature and accessible to all.

The great news is there are lots of tools that make AI easy to work with. And with digital twins, developers can simulate business-specific use cases, validate them and see their impact before deploying them in live networks. These results will be new use cases that deliver savings and improve existing operational processes.

By starting incrementally, using standards-based interfaces and internalized closed-loop operations, CSPs and developers can scale automation over time without disrupting existing operations. This approach enables them to work more collaboratively and efficiently, to respond to the operational needs more effectively, and to rapidly embark on new potential monetization opportunities directly from the network, all of which strengthen their competitive advantage.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/b269a803-cropped-40de52b9-screenshot-2025-12-02-at-12.29.15%E2%80%AFpm.png)

Pino Dicorato is director Automation Solution & Technology at Nokia. Pino leads technical sales enablement for Nokia’s Network Infrastructure optical network automation environment portfolio. With over 20 years of experience in the telecom industry, his roles have ranged from business...

Read more from Pino Dicorato](https://thenewstack.io/author/pino-dicorato/)