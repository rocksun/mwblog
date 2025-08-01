Vibe coding is all the rage these days, and with so many AI-powered tools making it so easy to do, it’s tempting to run with it and let tools like GitHub Copilot take over. But sometimes, like when building out production integrations, it’s not enough to write code based solely on vibes.

Especially when it comes to planning out the architecture of your integration, or deciding which features of a third-party platform to use, [large language models (LLMs)](https://thenewstack.io/introduction-to-llms) may not always be trained on the latest information. This makes the human in the loop especially important in that decision-making process. However, when building an integration with a platform you don’t have experience with, it can be painful to dig through countless pages of documentation, trying to get up to speed.

Developers building integrations have faced this challenge for years, and software vendors have tried countless ways to shorten the learning curve to productivity. A new entry, [Docusign Developer AI Assistant for VS Code](https://developers.docusign.com/tools/ai-assistant-vs-code/), currently in beta, offers a potential solution to this long-standing problem. In this article, I’ll walk you through how the Developer AI Assistant can help you vibe code Docusign integrations responsibly.

## Install the Developer AI Assistant

The Docusign Developer AI Assistant is available as an extension in the Visual Studio Code (VS Code) marketplace. The assistant works on top of GitHub Copilot, so you’ll also need a [GitHub Copilot](https://github.com/features/copilot) license or free trial, and you’ll need to install the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) in VS Code. Once you’ve installed the extension, you can open the Copilot chat window in VS Code and add the Developer AI Assistant to the conversation with `@Docusign`. You’ll be prompted to sign in to your Docusign developer account.

## Vibing Through the Discovery Phase

One of the major pitfalls that developers can come across when vibe coding is that the LLM doesn’t always have the full context needed to ideate the best options for building an integration. LLMs only know what they were trained on, and as documentation is frequently updated, they can sometimes return information that’s out of date. It can be helpful to supplement more generic LLMs with AI tools trained specifically on information from third-party providers, so you can trust that their inputs are up to date and accurate.

Instead of immediately generating code, you can involve the AI assistant in the planning phase of your project, and consult on which APIs or other Docusign products are the best fit for your use case.

Let’s say you want to write data to Salesforce from your Docusign workflows but you don’t know how. Just ask the AI Assistant:

[![Prompt to write data to Salesforce from your Docusign workflows](https://cdn.thenewstack.io/media/2025/07/0cc2bc67-write-data-to-salesforce-prompt.png)](https://cdn.thenewstack.io/media/2025/07/0cc2bc67-write-data-to-salesforce-prompt.png)

Source: Docusign

The assistant outlines two options for the integration, one using the Docusign [Apex Toolkit](https://developers.docusign.com/docs/salesforce/salesforce101/apex-toolkit/) and another using an [extension app](https://thenewstack.io/auto-read-data-into-agreement-workflows-with-docusign-extension-apps) and a [Maestro workflow](https://developers.docusign.com/extension-apps/workflows/). Both of these solutions are outlined at a high level, without getting too far into the weeds.

Here’s how it works: If I’m not familiar with any of the concepts mentioned by the Developer AI Assistant, I can simply ask where to learn more, and the assistant provides me with a list of links to the documentation with a brief description of what each piece of documentation covers. While it may not eliminate the need to read documentation entirely, the Developer AI Assistant gives developers a direct entry point into the relevant docs, eliminating unnecessary friction in the discovery phase of building an implementation.

[![Prompt to learn more](https://cdn.thenewstack.io/media/2025/07/6e31342e-learn-more-prompt.png)](https://cdn.thenewstack.io/media/2025/07/6e31342e-learn-more-prompt.png)

Source: Docusign

Now that I have more information, I can choose which option I want to use from the assistant’s initial reply, and get step-by-step instructions on how to implement it.

[![Prompt to get implementation steps](https://cdn.thenewstack.io/media/2025/07/b057cdf6-extension-steps.png)](https://cdn.thenewstack.io/media/2025/07/b057cdf6-extension-steps.png)

Source: Docusign

With no prior knowledge of Docusign products, you can chat with the Developer AI Assistant to understand the best solution for your use case. Instead of spending time reading documentation, you can describe your problems to the assistant to learn about potential solutions in real time.

If you were to jump into vibe coding immediately, your prompts to the AI Assistant might be more vague and might not lead you to the right solution. In this example, you may not know to ask for information about [extension apps](https://developers.docusign.com/extension-apps/), but because you spent some time describing your problem, the Developer AI Assistant is able to identify extension apps as a potential solution.

## Vibe Check: Generate Some Code

If you want to embrace vibe coding and let the assistant take over, you can ask it to generate some code for you in the language of your choice.

Following my earlier example, once I’ve built a workflow that writes data back to Salesforce, I can ask the assistant to help me write some code in Node.js that triggers that workflow. The first code the assistant returned simply triggered a workflow through the [Maestro API](https://developers.docusign.com/docs/maestro-api/maestro101/), but required me to hard-code my workflow ID. After some more instruction, the assistant was able to return some code that [gets a workflow](https://thenewstack.io/build-api-driven-custom-agreement-workflows-with-docusign-maestro) ID through an API call, then triggers that workflow.

[![Prompt to generate code](https://cdn.thenewstack.io/media/2025/07/fba7e87c-workflow-code.png)](https://cdn.thenewstack.io/media/2025/07/fba7e87c-workflow-code.png)

Source: Docusign

## Keep the Momentum Going With Authentication

In many ways, vibe coding is best suited for prototyping, when you’re just getting started with a project and there’s more room for error. To run the code the Developer AI Assistant gave me, I need an access token.

I could ask the assistant to generate some code that does authentication for me, or to help me understand [the different authentication types](https://www.docusign.com/blog/developers/demystifying-docusign-authentication) available to me. But as I’m just building a prototype, and I want to see how this works before building out a full implementation, I don’t want to be bogged down by authentication right now. Instead, I can start running code immediately by asking the assistant to generate an access token for me with the command `@docusign /getAccessToken`.

[![Prompt to get an access token for authentication](https://cdn.thenewstack.io/media/2025/07/21ee70b6-get-access-token.png)](https://cdn.thenewstack.io/media/2025/07/21ee70b6-get-access-token.png)

Source: Docusign

## AI Assistance Beyond Just Vibes

Of course, when you’re ready to fully build out a production version of your integration, you’ll need to implement authentication, and you may not be able to rely on vibe coding as much in the production development stage. At that point in the development life cycle, it can be most helpful to use AI tools as learning aids, rather than relying on them to generate code for you.

It’s important to be smart when vibe coding — you don’t want to let any bad vibes into a production environment. But, with trusted tools, you can balance vibe coding with other AI-assisted insights to make sure you’re building integrations from an informed place. With careful consideration of the tools you’re using and how you’re using them, it’s possible to avoid the pitfalls of vibe coding while still using AI to make your development experience easier.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/32ea98c7-paige-rossi.jpg)

Paige has been working for Docusign since 2020. As Lead Developer Advocate on the Developer Advocacy team, she writes content and code to help developers learn how to use Docusign technology, represents Docusign at community events, and supports Docusign developers...

Read more from Paige Rossi](https://thenewstack.io/author/paige-rossi/)