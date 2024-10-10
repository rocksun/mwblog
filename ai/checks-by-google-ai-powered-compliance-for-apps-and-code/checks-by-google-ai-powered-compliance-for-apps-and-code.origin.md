# Checks by Google: AI-Powered Compliance for Apps and Code
![Featued image for: Checks by Google: AI-Powered Compliance for Apps and Code](https://cdn.thenewstack.io/media/2024/10/a672fe71-checksbygoogle-1024x577.jpg)
Google is making its AI-powered compliance platform generally available as [Checks by Google](https://checks.google.com/). It encompasses three new product offerings that will check apps, code and soon [AI models](https://thenewstack.io/beyond-prompt-engineering-governing-prompts-and-ai-models/) for compliance issues, including personally identifiable information, government regulatory requirements, and whether a developer model will “talk out of turn” by providing controversial or inappropriate responses.

Checks by Google emerged from [Google’s incubator](https://area120.google.com/) and was used internally to test Google’s own large language models, said [Fergus Hurley](https://www.linkedin.com/in/fergushurley/), the co-founder and general manager of Checks by Google.

“We’re providing insights and tools to these companies because most of them do not have insights and tools that they need,” he said. “Some of our customers include the top five social media apps, the top five games, the top five finance apps, and these companies are very well-resourced, but they just don’t have the level of insight that they need to get through their job. We bridge that gap [between] the development team and the compliance team.”

Checks by Google is integrated with [Vertex](https://cloud.google.com/vertex-ai), the Google Cloud offering for generative AI, but works with other major model providers as well. Vertex has more than 150 generative AI models available, including [Anthropic’s Claude](https://thenewstack.io/a-nue-ux-web-framework-plus-anthropic-openai-boost-ai-apis/) and [Mistral](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/).

## App Compliance
Checks by Google has three offerings: [App Compliance](https://checks.google.com/app-compliance/), which is available now, and [Code Compliance](https://checks.google.com/code-compliance/) and [AI Safety](https://checks.google.com/ai-safety/), which are in a closed beta with a waitlist.

App Compliance checks an app or website or service to see if it’s complying with rules for collecting user data. For example, it can check for compliance against the [GDPR](https://www.gdpradvisor.co.uk/gdpr-countries) in Europe, the [CCPA](https://oag.ca.gov/privacy/ccpa) in California and the [LGPD](https://www.dlapiperdataprotection.com/index.html?t=law&c=BR) in Brazil.

“We look at what the app is required to do based on the different regulations around the world,” Hurley said. “We cover these rules and if you have users in those regions, we turn on those checks.”

App Compliance can also run an analysis on a publicly used app to check against any organizational privacy policies. It relies on an LLM that’s fine-tuned for understanding privacy policies, comparing them to what the app or product is actually doing and performs both dynamic and static analysis, he said. For example, Checks runs the apps on actual physical devices and monitors the network traffic coming off the apps as well as the user experience.

“We’ve got a smart AI crawler looking at what the app is actually doing. It’s able to play games, it’s able to log into the app if the login credentials are provided to us, but it’s a smart AI crawler.”

— Fergus Hurley, co-founder and general manager, Checks by Google
“We have built our own fine-tuned model for understanding privacy policies, and that’s used across many teams at Google now as well,” he said. “We are able to identify issues that the product might have from a compliance perspective. We’ve got a smart AI crawler looking at what the app is actually doing. It’s able to play games, it’s able to log into the app if the login credentials are provided to us, but it’s a smart AI crawler.”

Hurley noted that co-founder [Nia Cross Castelly](https://www.linkedin.com/in/niacastelly/) is a lawyer, although Hurley cautioned that the AI is not providing legal advice.

“She was responsible for [Google Play](https://play.google.com/store/games?hl=en_US) policies, which developers follow very closely to get access to billions of users,” he said. “So we do have a lawyer overseeing this stuff, but we are not providing legal guidance. That’s important.”

Instead, the AI is simply providing [insights and tools that bridge the gap between the development](https://thenewstack.io/6-development-insights-to-empower-it-teams/) team and the compliance team, he added.

## Code Compliance
Code Compliance, which is in closed beta, allows developers to get ahead of regulatory issues before an app is published. It can be integrated into an IDE, Hurley said, so that developers receive alerts directly in the IDE about issues that are integrated into their build systems.

Code Compliance provides information about critical issues, which can include security issues, but it also might detect, for example, an outdated SDK.

“We also help people create, manage and maintain their safety labels on Google Play,” he said. “That’s the Holy Grail, being able to be that one place that people need to go to be able to get all their compliance insights.”

## AI Safety
The third offering, which is being tested in a closed beta, is AI Safety.

Developers have three main problems they need to solve with AI and [AI-driven apps](https://thenewstack.io/5-best-practices-for-building-reliable-genai-apps/), Hurley said. First, they need to be able to set up their policies, which he called the ‘align phase.’ During this phase, they determine what policies are relevant to them and their website or app.

Second, they need to evaluate to make sure that the policies are adhering to their actual initial model release and vice versa. Third, after launching the actual GenAI product, developers need to ensure it’s behaving correctly in the wild.

“We have built a product to help with each of those parts as part of this AI safety product, so really, it’s trying to build out the governance command center here,” he said. “In the first phase, the alignment, people want to be able to configure their policies, and right now, we support the core policies that really every generic product needs around violence, hate speech, and sensitive data — such as PII (personally identifiable information).”

The evaluation phase helps developers determine whether the policies adhere to their initial model release and vice versa, he said. This phase is where the product performs red teaming and adverbial testing using prompts developed in-house by Google, he said.

![Shows the three questions in the Checks by Google framework: What is an app required to do; what an app says it's doing; and what an app is actually doing.](https://cdn.thenewstack.io/media/2024/10/c1fd99cc-checksbygoogleframework.jpg)
Screenshot of the Checks by Google framework

Red teaming is a [security testing technique](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/) that involves simulating malicious attacks on a system or organization to identify vulnerabilities and assess resilience. The name comes from a controlled war game where a red [team attempts to breach the security](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/) of a target, which a blue team defends. Adversarial testing is a type of software testing that involves intentionally trying to break an application or system by introducing unexpected or malicious inputs. It helps find weaknesses that could be exploited by malicious actors.

“One thing developers struggle with once they’ve built their model is coming up with these adversarial prompts, and that’s where us having this huge corpus of adversarial prompts is so valuable, and that’s where we’re leaning into a lot of the work being done by [Gemini](https://thenewstack.io/how-to-build-a-qa-llm-application-with-langchain-and-gemini/) and [Gemma](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) and other Google teams as well,” he said, adding that it also incorporates the best practices developed by those teams. “We run those prompts against the developer model, and we make sure the responses that form that model are the ones that the developer would want.”

This step shouldn’t be underestimated. Not only can AI models produce statements that could be publicly embarrassing, but they can also provide incorrect information that costs companies money.

“People sometimes try and get the models to do things that they shouldn’t do,” he said. “One of the most public cases of this is where Air Canada had a case where their agent responded and said that the person could get a refund. What ended up happening is that Air Canada said, ‘No, you can’t get a refund based on these conditions.’”

That led to a court case and in the end, [Air Canada did have to issue the refund](https://www.cbsnews.com/news/aircanada-chatbot-discount-customer/), he said.

“It’s now sort of set the rules that companies are responsible for what their GenAI agents say and do, and they do have that responsibility,” he said. “Making sure that the agent is following the company’s policies is so critical, but that’s one of the most public examples of one of the things that will be prevented by the model being fine-tuned, based on the company’s policies, to only talk about what the company actually offers.”

“One things developers struggle with once they’ve built their model is coming up with these adversarial prompts, and that’s where us having this huge corpus of adversarial prompts is so valuable, and that’s where we’re leaning into a lot of the work being done by Gemini and Gemma and other Google teams as well.”

— Fergus Hurley
Third, once the GenAI product is released, [developers need to be able to monitor](https://thenewstack.io/monitoring-developer-metrics-team-approach-is-best/) whether it behaves correctly in the wild. For instance, there was a case of a general-purpose AI agent that a company launched to provide for a specific use case, but people learned they could “hack” it and gain free access to a model that’s actually very expensive to use.

“The most important part is just making sure that things don’t go off the rails and having those safeguards in place,” he said. “We have a guardrails product where it monitors the input prompt and the output prompt and detects issues, like an input prompt that should not reach the model would be when someone is trying to potentially jailbreak the model, and then on the output side of things, no PII should ever be exposed by a model, and there should be many safeguards in place to prevent that from happening.”

He pointed out that if developers do not want to perform the fine-tuning themselves, they can use guardrails to automatically create monitoring and safeguards.

“They are able to go in and select for the input guardrails, [e.g.] I want to turn on jailbreak prevention,” he said. “Let’s say they’ve configured these different ones with different sensitivity thresholds, then they can configure the output thresholds, and then they deploy that to production as part of their model.”

Guardrails act as a filter on the model rather than actually fine-tuning it directly. The filter does not significantly impact performance, he added.

## Customizable by Industry, Focus
Checks by Google’s offerings can be customized by industry as well, he added. For instance, if an app is dealing with children’s data, there are very specific rules that app must follow.

“We work with some of the biggest game companies out there for kids,” he said. “You could imagine healthcare and finance or other major heavily regulated industries have their own very specific needs, and that’s where the goal, over time, is to build out this ecosystem of checks, where people are able to turn on the Checks that are most relevant to their business.”

Hurley said Checks by Google’s products cut across all types of developers; they see [frontend developers](https://roadmap.sh/frontend), as well as [backend](https://roadmap.sh/backend) and [full stack developers](https://roadmap.sh/full-stack), using the tools.

Right now, it’s free to get started, although some businesses are more complex and do need paid services to help them with compliance, he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)