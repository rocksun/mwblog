# New Threats Emerge as AI Agents Leverage APIs
![Featued image for: New Threats Emerge as AI Agents Leverage APIs](https://cdn.thenewstack.io/media/2025/06/372cda12-kaffeebart-krpulsduetk-unsplash-1024x678.jpg)
[Kaffeebart](https://unsplash.com/@kaffeebart?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on Unsplash.
A single API exploit in a simple AI application can compromise thousands of user records in seconds. As AI agents become mainstream, so do the risks.

AI agents represent a giant leap forward in AI capabilities, surpassing traditional AI automation scenarios. While there’s some [debate over the exact characteristics](https://www.wsj.com/articles/everyones-talking-about-ai-agents-barely-anyone-knows-what-they-are-8941e234?mod=cio-journal_lead_pos2), let’s define an AI agent as a multilayer AI application that makes decisions based on its reasoning and contextual knowledge and acts autonomously.

Even if your company has yet to implement these complex AI applications, you’re likely aware that [adoption is growing](https://www.gartner.com/en/articles/ai-agents). AI agents will increasingly impact APIs and applications, adding complexity and autonomy and [creating unique security](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/) challenges.

## Why AI Agents Depend on APIs
AI agents are already integrated into applications across various industries, including finance, e-commerce, travel, sales, and gaming, to name a few.

They can do a lot for applications and systems: automating processes, enabling instant decision-making, and enhancing user personalization. However, none of this is possible without help from APIs. APIs connect AI agents to systems, applications, data sources, and other agents. They also enable AI agents to coordinate actions across these many layers.

**APIs enable access to data. **AI applications require access to accurate, high-quality data to function correctly, often including both real-time and historical data.
APIs provide access to [multiple data sources](https://thenewstack.io/best-practices-collect-and-query-data-from-multiple-sources/), including databases, third-party web services, real-time data feeds, and enterprise software.

**APIs expand AI agent capabilities.** APIs enable you to add new or specialized capabilities to AI applications, such as real-time translation, image recognition, or sentiment analysis. For building these APIs, many third-party services can either provide specialized APIs or you could build custom APIs to enhance your AI agent’s capabilities.
**More AI agents mean more APIs accessing data and services. **As the number of AI applications increases, so does the number of APIs interacting with data. That means attackers have more APIs and data to target.
Say your agent only accesses data stored in your internal enterprise software. It still needs an API to retrieve and use that data. That API remains susceptible to all the conventional threats we know today, such as SQL injections, cross-site scripting (XSS), and broken authentication.

If your AI agent needs third-party data or services, you must also prepare for potential security flaws and vulnerabilities in those APIs.

## APIs and the Future of AI Agents
As AI agents evolve into complex, autonomous tools that help humans and machines in countless ways, the role of[ APIs becomes increasingly critical](https://thenewstack.io/the-future-of-apis-lessons-in-security-composability-ai/).

**APIs will increase AI agent autonomy.** AI agents are becoming increasingly autonomous, and APIs play a significant role in that independence. We’ll soon see AI applications that dynamically respond to and assist users based on real-time data, contextual cues, and changing conditions.
For example, an AI travel agent could help users plan trips — autonomously deciding which APIs to call and in what sequence, accessing data on real-time flights, hotels, transportation, and weather. It could also automatically make recommendations and book everything for the trip.

**APIs will enhance **[AI agent collaboration. APIs will facilitate automated](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/) collaboration between AI agents and human users, allowing them to complete tasks more efficiently.
A grocery store chain could use AI agents to monitor real-time weather data, predicting demand increases for specific products, for example, sudden spikes in ice cream purchases during a major heatwave. AI agents could track inventory levels as the heatwave progresses, automatically placing replenishment orders and shipping high-demand ice cream products to warehouses in the affected areas. AI agents in the mobile shopping app could work with inventory AI agents to recommend products based on customer preferences and availability.

**Complex AI agent ecosystems may lead to chaotic API connections. **AI agents typically utilize multiple APIs to obtain the data and services necessary to complete a range of tasks. We’re building an ecosystem of thousands of multilayered AI applications that work together to solve complex problems and handle numerous long-running user interactions.
The complexity of these interconnected AI applications and APIs will make [securing them more challenging](https://thenewstack.io/the-challenges-of-securing-the-open-source-supply-chain/) than ever. Not least because attackers constantly adapt their techniques to better fly under the radar.

Companies must reevaluate their API and application development processes to account for upcoming AI developments, especially in terms of security, as these applications will amplify common vulnerabilities and introduce new ones.

## AI Agents Bring Unique Security Challenges
Over 50% of the [vulnerabilities](https://www.wallarm.com/reports/2025-api-security-report) listed in the 2024 CISA Known Exploited Vulnerabilities (KEV) Catalog are API-related, up from 20% the prior year.

API vulnerabilities are a significant concern for all types of AI products. Direct threats include excessive data exposure and weak or broken API authentication or access controls. Indirect vulnerabilities include flaws in third-party integrations or systems where APIs serve as intermediaries.

Managing new API security challenges goes hand in hand with the growth of AI agents. Still, the most important principle remains familiar, as it’s the same as for all software development:[ Zero Trust](https://www.getambassador.io/blog/the-importance-of-zero-trust). Securing AI and APIs means never trusting any user (human or machine), device, or system by default. Once inside, authenticate them per session (instead of once at the perimeter).

Staying ahead in the coming era of AI agents means managing both traditional API vulnerabilities and emerging AI-specific threats. It only takes one single exploit in an API or AI function to compromise your AI application and, ultimately, your systems and data.

## Securing the Future of AI Agents
Companies must brace for the upcoming tsunami of applications powered by AI agents and APIs, and the [era of transformation is upon us.](https://www.forbes.com/councils/forbestechcouncil/2025/03/18/ai-will-transform-software-development-but-not-the-way-you-expect/)

The complex API interactions that enable AI [agents make it harder to manage security](https://thenewstack.io/what-hal-9000-teaches-us-about-ai-driven-authorization/) manually or respond rapidly, so choose automated approaches and proactive default restrictions. Reactive measures simply can’t keep up with the pace of change.

Start preparing security strategies now to protect the APIs and AI agents of the future.

*The owner of TNS, Insight Partners, also invests in Ambassador. As a result, Ambassador receives preference as a contributor.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)