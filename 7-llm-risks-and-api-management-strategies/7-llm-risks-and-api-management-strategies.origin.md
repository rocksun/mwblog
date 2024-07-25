# 7 LLM Risks and API Management Strategies to Keep Data Safe
![Featued image for: 7 LLM Risks and API Management Strategies to Keep Data Safe](https://cdn.thenewstack.io/media/2024/07/f7abd483-chatbot-1024x576.jpg)
Despite the explosion in enthusiasm surrounding [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms), any new cloud-based software solution can create or expose new vulnerabilities. Let’s explore seven of the LLM vulnerabilities that the Open Web Application Security (OWASP) project has published and how we can mitigate these risks by applying API management security. Each section will detail a specific vulnerability, such as prompt injection or insecure output handling, explain how cybercriminals exploit these weaknesses and provide practical [API management](https://thenewstack.io/api-management/) techniques to prevent these threats.

**1. Prompt Injection **
A prompt injection is when a hacker is able to trick GenAI models into responding with unintended outputs through malicious prompts disguised as legitimate ones. In this attack, if we do not restrict which prompts can be passed to an LLM, an attacker can craft a request that will result in unexpected outcomes. For example, a chatbot that rather than helping a user begins to insult them.

To mitigate this type of attack, developers should implement traditional authentication and [access control to ensure that only authorized users](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/) can interact with an LLM. Then prompt checking should be performed before sending a request to the model — either by using pre- and post-processors to limit what the LLM can do or by using templating to restrict the actual request to be a parameterized form. Another option is to use either a home-trained LLM or a third-party service to check content safety of both the request and response to the LLM.

**2. Insecure Output Handling **
By blindly trusting the responses returned from an LLM, backend systems may be inadvertently exposed, and this could lead to issues like cross-site scripting, cross-site request forgery, server-side request forgery, privilege escalation or remote code execution.

The first step to combat this type of vulnerability is to implement prompt scoping, which restricts the scope of the prompt to the LLM. Responses should also be scrutinized before being returned to the requester, this could be as simple as applying regex patterns or as advanced as using LLMs themselves to scan content for harmful responses.

## 3. **Model Denial of Service **
Overloading an LLM with requests can cause poor service or increased resource costs, two of the worst outcomes for an organization. Yet with a model denial of service that is what’s at stake. This happens when attackers cause resource-heavy operations on LLMs. This could look like a higher-than-normal task generation or repeated long inputs, to name a few.

Authentication and authorization can be used to prevent unauthorized users from interacting with the LLM. Rate limiting on the number of tokens per user should also be used to stop users from burning through an organization’s credits, incurring high costs and using large amounts of computation resulting in latency injection.

**4. Sensitive Information Disclosure**
Compliance teams’ concern about sensitive information disclosure is perhaps one of the most severe vulnerabilities limiting LLM adoption. This occurs when models inadvertently can return sensitive information, resulting in unauthorized data access, privacy violations and security breaches.

One technique that developers can implement is using specially trained LLM services to identify and either remove or obfuscate sensitive data. This can also be used for non-LLM-based use cases. Additionally, LLMs can be instructed to [not return certain types of data](https://thenewstack.io/automating-context-in-structured-data-for-llms/), limiting how they will respond.

**5. Insecure Plugin Design **
With insufficient access control and insecure inputs, you’re opened up to insecure plugin design. This is when extensions are called automatically by a model during user interactions. The extensions are driven by the model itself, and there is no application control over the execution. By exploiting this, an attacker can construct a malicious request, resulting in a wide range of undesired behaviors.

To mitigate this risk, restrict who and what can access the underlying LLM via authorization and authentication. This reduces the risk of exploitation by limiting access to sensitive operations. Sanitization and control should also be applied to prompt requests to restrict what can be done in an operation call.

**6. Excessive Agency**
When excessive functionality, permissions or autonomy are granted, LLM systems may undertake actions leading to unintended consequences.
This is a threat that should be consistently monitored through observability and traffic inspection to see what is interacting with the LLM and how it is being used. Authorization and authentication should also be used to enforce strict access controls to restrict who can and cannot access and interact with systems. For more sensitive operations, a higher level of authorization is required.

**7. Overreliance **
Overreliance is another concern having to do with granting autonomy to users or systems using LLMs. Without oversight, there is the chance of misinformation, miscommunication or even legal/security issues due to the content generated by the models.

Solution: Again, access control should be enforced through authorization and authentication, with [restrictions being placed on the more sensitive operations](https://thenewstack.io/how-to-control-access-in-llm-data-plus-distributed-authorization/). Similar to excessive agency monitoring, observability of the traffic flowing through the system should be implemented allowing the organization the ability to understand the interactions taking place. Prompt control should also be used to restrict how interactions with the LLM occur.

Ultimately, LLMs are accessed via API calls and should be managed in the same way that traditional API traffic is. Defense-in-depth as well as observability in the ecosystem are key to seeing how traffic is flowing through the system. All of this can be accomplished with an AI gateway that has specialist integrations to manage the nuances of AI API traffic.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)