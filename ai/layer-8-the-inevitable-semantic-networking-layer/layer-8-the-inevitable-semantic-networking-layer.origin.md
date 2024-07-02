# Layer 8: A Semantic Networking Layer for the Age of AI
![Featued image for: Layer 8: A Semantic Networking Layer for the Age of AI](https://cdn.thenewstack.io/media/2024/06/ffe55292-layer-1024x617.jpg)
In the most famous line from the classic mockumentary “Spinal Tap,” Nigel Tufnel, the lead guitarist, points to an amplifier and notes the additional number on the dial, saying that it “goes up to 11.”

Alas, “this one goes to eight” does not have quite the same ring, but it might be time to use this phrase to describe a new layer of the traditional networking stack — the semantic layer. The addition of Layer 8 is driven by [AI applications](https://thenewstack.io/ai/) and their new exigencies.

The [OSI (Open Systems Interconnection) model](https://thenewstack.io/open-source-ai-osi-wrestles-with-a-definition/), a conceptual framework that has guided network design and communication for decades, is facing a new challenge in the age of AI. As AI continues to permeate various aspects of technology, including networking, the traditional seven layers of the OSI model may not be sufficient to capture the full requirements and [realities of AI-driven networking](https://thenewstack.io/what-is-an-ai-gateway-and-do-you-need-one-yet/).

Layer 8 is my proposed extension to the OSI model that aims to address the unique requirements and capabilities of AI in the context of networking. Unlike the existing layers, which focus on the technical aspects of data transmission, Layer 8 is concerned with the semantic understanding and intelligent processing of the data being transmitted.

## What Is Layer 8 and Why Do We Need It Now?
Networks today are not just pipelines for data but increasingly intelligent entities capable of making decisions based on the content and context of the data they handle. The OSI model consists of seven layers: physical, data link, network, transport, session, presentation and application. Each layer has specific functions and protocols that enable communication between networked devices.

The seven OSI layers primarily focus on the syntactic aspects of data transmission, such as encoding, formatting and error correction. In the cloud native world, Layer 4 (transport) and Layer 7 (application) have become the most widely addressed.

These layers are increasingly conflated due to HTTP and other web protocols becoming the primary focus of delivering functionality to users and services. Even the application layer focuses on performance but ignores content. Overall, the OSI layers do not inherently consider the semantic meaning or context of the data being transmitted.

Yet, we are already seeing the emergence of semantic caching in AI applications, where the application delivery and networking technologies incorporate comprehension of the content and user expectations of an application to improve user experience and accelerate application performance.

These new capabilities are already extending the OSI model beyond its current scope and will coalesce into a more clearly defined Layer 8. Layer 8 would sit above the application layer (Layer 7) and focus on understanding the meaning, intent and contextual information within the data. By incorporating semantic analysis, Layer 8 would enable more intelligent and context-aware networking and application delivery decisions.

## How Would Layer 8 Work?
Just as application transport technologies and protocols (HTTP) are deployed at Layer 7, AI techniques, such as machine learning, deep learning and natural language processing (NLP), would be employed at Layer 8 to analyze and understand the data being transmitted. NLP techniques could be used to process and interpret the body of the message, extracting key information, identifying relevant entities, and determining the overall meaning and context.

Classification models might route HTTP requests to an API endpoint best suited to the human language therein. Sentiment analysis algorithms could be applied to assess the emotional tone and intent behind the data. This could help in prioritizing or routing data based on its urgency, importance or complexity.

Backed by these techniques, at Layer 8, machine learning models could be trained to identify patterns, anomalies and variations in the data. These models could learn from historical data and adapt to changing network conditions or user behavior.

The AI-driven inspection would operate in real time, processing data as it flows through the network. This requires efficient algorithms and hardware acceleration to minimize latency and ensure timely decision-making. For example, it could prioritize traffic based on the importance or urgency of the content, route data based on its intended purpose or adapt network behavior based on the user’s intent. Offensive or hazardous content could be filtered, flagged or quarantined to more sophisticated content-moderation systems prior to forwarding. For example, deep-voice attacks could be identified based on the call’s contents and comparisons to similar attacks logged by the system.

## The Soul of the New ADC
The logical home for Layer 8 is inside of emerging AI gateways that can apply models in real time. That said, such [gateways will need to co-exist and interact with API gateways](https://thenewstack.io/api-gateway-ingress-controller-or-service-mesh-when-to-use-what-and-why/), application delivery controllers (ADCs) and content delivery networks (CDNs) that already exist. The cooperation must be frictionless and super-fast to improve the performance, resilience and security of Layer 7. Proximity would benefit both; semantic inspection and comprehension induce latency and require intense and continuous inference traffic to AI models.

By integrating Layer 8 capabilities directly with API gateways, ADCs and CDNs, semantic processing can be performed closer to the edge, reducing the round-trip latency and enabling real-time decision-making. This symbiotic relationship between Layer 8 and the existing application delivery infrastructure will pave the way for more intelligent, context-aware and responsive networks that can adapt to the ever-evolving demands of AI-driven applications — in other words, networks that go to 11.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)