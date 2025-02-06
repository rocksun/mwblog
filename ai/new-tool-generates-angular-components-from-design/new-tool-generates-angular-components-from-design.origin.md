# New Tool Generates Angular Components From Design
![Featued image for: New Tool Generates Angular Components From Design](https://cdn.thenewstack.io/media/2025/02/95b6b934-autocode-simplifies-coding-designs-1024x683.jpg)
Coding to [Figma](https://thenewstack.io/figma-caters-to-developers-with-dev-mode-and-ai-integrations/) UI design specifications can be time-consuming for frontend developers. A new artificial intelligence tool called Auto Code from [WaveMaker](https://www.wavemaker.com/) is designed to simplify the process by generating web and mobile components. The code can then be exported to [Angular](https://thenewstack.io/angular-shares-potential-ideas-for-2025-improvements/) for the web and [React Native](https://thenewstack.io/react-native-fork-supports-development-on-apple-vision-pro/) for mobile.

“This handoff process between the design team and the frontend engineering teams takes up time because of the number of iterations it goes through to get the fit and finish perfectly implemented,” said [Prashant Reddy](https://www.linkedin.com/in/prashantr/?originalSubdomain=in), WaveMaker’s senior director of product. “With Auto Code, what we are trying to do is to make that handoff between a designer and the frontend engineering team as pixel perfect, as precise as we can, so that we can reduce the number of iterations that the teams go through in order for them to deliver the end product.”

## Low-Code But for Programmers
[WaveMaker is a low-code platform](https://thenewstack.io/new-figma-plug-in-converts-design-to-angular-react-native/), but it’s primarily used by professional frontend developers at financial institutions, large product companies and independent software vendors, according to WaveMaker co-founder and CTO [Deepak Anupalli](https://www.linkedin.com/in/deepakanupalli/?originalSubdomain=in). Often these companies are building and delivering hundreds of screens as part of their product modernization journey.
“Even before LLMs ([large language models](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)), we were generating code in Angular and React Native, and we were actually giving the code to the developer so that they can build their application on top,” he said. “That is how we were able to convince our developers to adopt the product. They are actually seeing real code, they own it and they customize it.”

## What Auto Code Does
Auto Code translates Material 3-based Figma designs to production-ready code for UI elements, app navigation and interactions.

[Material 3 is Google’s open source design system](https://m3.material.io/). Figma uses a Material 3 Design Kit, which includes pre-designed components, styles, and guidelines. This makes it possible for designers to easily create prototypes and mockups that adhere to Material 3 principles.
While WaveMaker AutoCode works out of the box for Figma designs using the Material 3 design system, it can be enabled to work with client-proprietary design systems. AutoCode identifies design elements such as forms, lists and cards and maps them to corresponding widgets within WaveMaker studio. It supports Figma variables, modes and design tokens to maintain the integrity of the original design through the development process.

Generated code can also be customized to add business logic within WaveMaker’s studio environment.

## Creating Components
WaveMaker currently has more than 90 components, including buttons, text fields, forms, multi-step forms, tables and charts. It also offers mobile app components that are commonly used, including bottom navigation.

“There are patterns that emerge, that that we see as common across web and mobile app, and then we componentize that and add that into the product,” Reddy said.

Auto Code can recognize individual components such as a text box or a button, but it also can group them and recognize that together, they create a long form or a registration form.

“That abstraction is very important because then the programming model shifts to ‘Where do you want the data that is coming out of this form to go to?’” Reddy said. “Our AI model recognizes all the components that are in the design, and then groups the components in the design into logical, higher order abstractions — like forms, table grids, list of cards — whether they are vertical or horizontal.”

It recognizes higher order abstractions, also.

“From a program point of view, when you see a list of cards, you think of them as an array in your data,” he said. “It’s very important for the programmer to not see the five cards that are in the Figma design as individual cards but as a list. So our AI model does all of that.”

## AI But Not LLM
Auto Code is a [machine learning](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/)-based (ML) tool, but not [generative AI](https://thenewstack.io/navigating-the-complexity-of-legacy-code-with-generative-ai/). Rather than training an LLM, it relies on metadata from the Figma design. This solves the issue of hallucination, Reddy and Anupalli said.

“Our implementation is based on ML techniques that don’t use LLM, and so that’s one part of the solution architecture that makes it predictable and consistent every time you run,” he said. “We generate the design tokens, then the components that use them and then the page. These are all architectural guardrails that make sure that the translation quality is accurate, and you can verify that at each layer.”

WaveMaker also offers a WaveMaker CoPilot, an AI-powered assistant within WaveMaker’s developer studio that can provide prompt-based UI customization for WaveMaker AutoCode generated UIs.

*Editor’s Note: Updated Feb. 5, 10:28 a.m. to correct the spelling of Deepak Anupalli.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)