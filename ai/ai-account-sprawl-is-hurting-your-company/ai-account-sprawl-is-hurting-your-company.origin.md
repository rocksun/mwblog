# AI Account Sprawl Is Hurting Your Company
![Featued image for: AI Account Sprawl Is Hurting Your Company](https://cdn.thenewstack.io/media/2024/07/f830c01e-ai-sprawl-hurting-1024x576.jpg)
An [AI gateway](https://www.ibm.com/products/api-connect/ai-gateway) is an emerging component of the IT estate that helps enterprises bring their use of AI under control by [applying good practices](https://thenewstack.io/ai-gateways-transform-experimentation-into-scalable-production/) for governance, security and operationalization. By helping manage and empower the use of large language models (LLMs) and other forms of AI, an AI gateway can accelerate AI maturity and create benefits in the following four categories.

## 1. Bring AI Under Centralized Control
Many organizations are finding that the enthusiasm of early generative AI adopters within their development groups has outstripped their capacity to ensure good management and governance of access to AI services. AI providers commonly offer a free tier to encourage experimentation. But this leads to large numbers of individual subscriptions across an organization’s developer population, with no visibility into who is using the AI services, what they are using them for or how they are using them.

Deploying an AI gateway can be the first step in taming this uncontrolled use of AI. The process varies depending upon the provider; I will use the AI gateway available with [IBM API Connect](https://www.ibm.com/products/api-connect) as an example.

The AI gateway appears alongside other types of API providers in the tool’s [API management](https://thenewstack.io/custom-integrations-for-complex-scenarios-7-best-practices/) dashboard:

You usually need to apply configurations, such as providing the API key (subscription key) for the centrally owned subscription to the AI provider, information about where the AI provider endpoint is hosted (e.g., the region) and any other required technical information.

Alongside increased visibility, creating the centralized AI gateway this way consolidates your enterprise buying power into a single subscription managed by the AI gateway. This enables you to replace the tens or hundreds of individual subscriptions that may have been created directly by application developers, and leverage your economy of scale to strike a more favorable commercial arrangement based on your total expected consumption.

You can also start to build up a catalog of permitted services that have been approved by your enterprise for use by your application developers. This form of “reverse API management” presents an inward-facing catalog of approved services for your developers to use (in contrast with typical [API management patterns](https://thenewstack.io/the-5-worst-anti-patterns-in-api-management/) that expose your services to external consumers).

## 2. Empower Developer Efficiency
Adopting an AI gateway also enhances developer efficiency. Having an internally facing catalog saves developers time and effort by granting access to your approved services. It also shows them that any necessary investigation and sign-up processes for externally hosted services have been completed centrally.

Once a developer discovers an AI service in the developer portal, they can use a self-service onboarding process to consume those APIs and quickly continue building their application.

For example, a user from the logistics team can create an application called “Delivery scheduler,” subscribe it to the watsonx.ai product within the AI gateway, and generate their application credential (Client ID) so that they can invoke that service at runtime.

Once you launch an AI gateway, you will want to transition your developers’ existing AI provider accounts to manage them through the AI gateway. They must be able to switch their applications to use the AI gateway with a minimal number of changes. In this case, it is helpful for the AI gateway to present the same API contract the AI provider uses.

In the example above, the body of the application’s request conforms to the same schema structure as the watsonx.ai API specification: It provides existing fields such as model_id, input and other parameters, but the API endpoint is now presented through the AI gateway (API Connect endpoint), rather than calling directly to the AI provider’s endpoint.

The only changes they have to make to the application code are replacing the target endpoint and specifying the security credential issued by the AI gateway. This simplicity makes it easy to persuade application developers to adopt the centrally managed service.

## 3. Understand Your AI Usage
Deploying an AI gateway provides visibility and knowledge about your enterprise’s use of AI models. Routing all your requests through the AI gateway can provide analytics on the interactions between your applications and the AI provider.

In addition to the traditional API management style of reporting — number of requests, technical response codes, etc. — the AI gateway can provide analytics about AI-specific characteristics, such as the number of AI tokens sent and received by application requests, which is typically the primary metric your provider uses to charge for your usage.

For example, graphing the number of request and response tokens generated through the AI gateway over a given period of time enables you to track overall adoption trends for the AI gateway services over a sustained period of time.

In addition to providing an enterprise-wide aggregate view, the AI gateway can report analytics at finer-grained levels, such as per-consumer-organization (e.g., a department within your company) or for individual applications registered to use the AI gateway services based on the volume of AI tokens they are driving.

This enables you to identify which users or applications within the enterprise are the heaviest users of the AI models — and manage departmental chargebacks to those consumers if you choose.

You can also look deeper into your applications’ usage patterns, such as visualizing which AI model they are using — either to understand which models are most important to your business scenarios or because some models may be more expensive than others.

## 4. Optimize Costs and Performance
An AI gateway can also help you optimize the cost and performance of your AI-infused applications.

Many AI providers charge based on the number of tokens sent and received, so the AI gateway must be able to go beyond the traditional REST pattern of rate limiting based on the number of requests and be able to set rate limits based on the number of tokens per time interval.

This enables you to prevent runaway costs by imposing limits on each application’s use of AI. For example, you may wish to set smaller limits both for the development and test phases of a project (e.g., to offer a limited amount of access to a large number of application developers) and in production use cases (to protect against extreme spikes in traffic or denial of service style attacks).

The AI gateway also benefits application performance by providing built-in caching of responses to your AI requests.

Depending upon the complexity of a request, an AI model can take five, 10, 15 or more seconds to generate the answer. In scenarios where the same request may be issued multiple times in quick succession (such as a set of multiple-choice prompts multiple end-users select from), the AI gateway may be able to cache responses for a period of time, enabling an immediate response to the application and saving costs by preventing the request from being sent multiple times to the AI provider.

## Summary
You can leverage an AI gateway to empower and manage your use of AI services in four categories:

- Bringing AI under centralized control
- Empowering developer efficiency
- Understanding your usage of AI
- Optimizing costs and performance
Want to find out more?

[Register to join us for a free webinar](https://www.ibm.com/account/reg/us-en/signup?utm_medium=Exinfluencer&utm_source=Ex%5B%E2%80%A6%5DPIWW&utm_term=30A3M&utm_id=APIC-Free-Trial-TNS&formid=urx-51621)about the AI gateway.- Try out the AI gateway in IBM API Connect using our
[free 30-day trial](https://ibm.webcasts.com/starthere.jsp?utm_medium=Exinfluencer&utm_source=Exinfluence%5B%E2%80%A6%5D&_ga=2.232920862.1673870635.1720026396-1836981186.1720026396).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)