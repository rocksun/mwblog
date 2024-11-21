# Kubernetes Runtime Defense Evolves Beyond eBPF
![Featued image for: Kubernetes Runtime Defense Evolves Beyond eBPF](https://cdn.thenewstack.io/media/2024/11/b3ef9197-engin-akyurt-xcwek_bx7ys-unsplash-1-1024x683.jpg)
The cloud brought with it its fair share of [security challenges](https://thenewstack.io/upskilling-developers-to-meet-todays-security-challenges/), expanding the attack surface well beyond the static perimeter protections of the [web application firewall](https://thenewstack.io/how-attackers-bypass-commonly-used-web-application-firewalls/), network IP-based rule, and infrastructure layer configurations.

The rapid [emergence of AI](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) has only exacerbated those challenges and “forced security into the runtime — the elusive attack surface that everyone knows they need to secure but that security technology has not been able to keep up with,” said [Vrajesh Bhavsar](https://www.linkedin.com/in/vrajeshio/), co-founder and CEO of [Operant AI](https://www.operant.ai/), the four-year-old startup whose runtime application platform aims to defend not only cloud applications but [also AI models and APIs](https://thenewstack.io/bypassing-ebpf-to-protect-runtimes-in-kubernetes-apps/).

The San Francisco-based company’s platform includes such capabilities runtime risk scanning and analysis, enforcement of runtime security measures across APIs, data stores, legacy endpoints, and [Kubernetes](https://thenewstack.io/kubernetes/) clusters, vulnerability scanning of APIs to smoke out vulnerabilities and generate real-time insights, and [policy as code](https://thenewstack.io/is-policy-as-code-the-cure-for-multicloud-config-chaos/) for scaling security policies across multiple clouds.

At the recent [KubeCon + CloudNative NA](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) show in Salt Lake City, Utah, Operant AI took another step, introducing the 3D Runtime Defense Suite, which pulls capabilities around real-time discovery, detection and defense into a single package to ensure protection at every layer of cloud applications, including AI models and APIs.

## A Suite of Defenses
The enhanced discovery capabilities include instant live blueprints of AI workloads, models and AI APIs, identification of ghost APIs and shadow AI data flows, and tracking data-use patterns from third-party APIs to data stores.

Runtime detection targets Open Web Application Security Project’s ([OWASP](https://thenewstack.io/mitigate-owasp-security-top-threats-with-an-api-gateway/)) top 10 [large language model (LLMs) threats](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/), including prompt injections, sensitive data exfiltration, model theft and data poisoning. Operant’s current platform already covers more than 80% of OWASP’s threats across APIs, Kubernetes and [LLMs](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/). Another feature is detecting the leakage of sensitive data like personally identifiable information (PII), secrets and API keys.

The defense section includes automated in-line block and redaction of sensitive data flows, quarantine for suspicious third-party containers and AI models, and enforcing rate limiting and token use for sensitive APIs, including endpoints.

## Auto-Redacting of Sensitive Data
The automatic redaction of sensitive data flows is a key feature that addresses the issue of data privacy, both from the point of defense as well as data governance and compliance with the growing number of government regulations. AI development now is a mixed bag, with some companies stopping AI development over data privacy concerns while others build AI products and features that may be sharing private data with third parties, either by accident or design, Bhavsar told The New Stack.

“In today’s GenAI [generative AI] application world, companies are building all sorts of business-critical capabilities with their models,” he said. “But in order for AI to work, it needs really, really good data. So, how do we protect the data and get the capabilities we need without shutting down the entire AI application flow?”

Operant’s in-line auto-redaction detects common forms of private data — think Social Security numbers, phone numbers and API keys — as they move through the live application, flags them and prioritizes their risk profiles based on how critical they are.

“The system allows engineers the option to either shut down the whole data flow by default or to let it run with in-line auto-redaction protecting the private elements of the data,” Bhavsar said. “In-line auto-redaction redacts the private data before it leaves the internal application environment, which is a huge win both for data privacy and data governance because it means that the core sensitive elements are not able to be sent anywhere, while the application itself can continue to function.”

## Moving Beyond Logging and eBPF
Operant isn’t the only vendor looking to protect the runtime environment. Other companies rely on tools like [eBPF](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/) — which enables programs to run in a privileged context like the operating system kernel — and logging, which creates large numbers of alerts that software engineers have to deal with. While they warn developers of attacks, Operant’s technology takes steps to shut them down.

“These approaches cause a reactive overload for strapped teams while lacking the multidimensional context required to actually make sense of attack paths that in reality connect from external third parties, through APIs, through services, all the way to data stores,” Bhavsar said. “This was true before teams were building sophisticated GenAI products and features but is made even more exaggerated by the data flows and application architecture required to make GenAI work, whether a team is using an AI API or a third-party model deployed on Kubernetes, as most of them are.”

In addition, attacks at runtime — including prompt injections, zero-day vulnerabilities data exfiltration, data poisoning and distributed denial of services (DDoS) — need to be blocked at runtime, something these other runtime mechanisms can’t do.

AI application security tools also aren’t enough. AI applications don’t live in a vacuum, and organizations can secure just AI elements of a cloud application.

“You have to secure the entire cloud stack in which it is embedded, including all of the ephemeral and complex interactions happening within Kubernetes, which has become the de facto platform for AI application development,” he said. “To do that, you need to be securing the data an application or model is using before it leaves the perimeter.”

## Security by Default Is Key
Operant ensures all API and Kubernetes interactions inside an application’s perimeter are secure before data is sent out, enabling AI software and models to provide business value without security concerns blocking their ability to function. The security-by-default mode lets teams develop AI faster and more responsibly with noninvasive runtime defense controls in place before attackers enter the environment.

Operant is looking to cast a wide net with its 3D Runtime Defense Suite, not only in terms of capabilities but also in its coverage of generative AI platforms like [OpenAI’s GPT models](https://thenewstack.io/openais-chatgpt-now-formats-output-to-developer-queries/), [Google’s Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/), [Cohere](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/) and [Anthropic’s Claude](https://thenewstack.io/a-nue-ux-web-framework-plus-anthropic-openai-boost-ai-apis/). Given the rapid evolution of the AI industry and the wide range of choices development teams are making, an effective AI defense product needs to be vendor- and platform-agnostic to cover changes and ensure resilience, Bhavsar said.

“We wanted to build the right plug and play architecture from the beginning so that adding another provider in the future or customizing the ones we support within customer stacks would remain simple like the rest of the implementation of our product,” he said. “This was a key strategic decision we made … so that it will allow security engineers and developer teams to incorporate security practices that will stand the test of time and scale without extra cost or heavy manual work as they continue to evolve their development processes and tooling.”

## Building on Experience
Both Bhavsar and [Priyanka Tembey](https://www.linkedin.com/in/priyanka-tembey-a1947611/), a co-founder of Operant and its CTO, each bring more than a decade of experience building machine learning and AI for cybersecurity use cases, which gave them a sense of which approaches were short-term measures and what can be transformational at scale.

“There is a ton of noise in the industry, but we are building to last with technology that is, by default, designed to scale and be flexible in a way that matches real engineering teams where they are, and also sets them up with effortless cyber-resilience for the future even as AI continuously evolves,” Bhavsar said.

They’re getting support for their ideas. The company, which launched publicly in April 2023, raised $10 million in capital venture funding in September from SineWave Ventures, Felicis, Alumni Ventures, Massive, Calm Ventures and Gaingels, giving it a total of $13.5 million raised in just over a year.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)