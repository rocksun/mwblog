# JetBrains Improves AI Code Completion, OpenAI Boosts JSON
![Featued image for: JetBrains Improves AI Code Completion, OpenAI Boosts JSON](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
[JetBrains](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/) announced its annual IDE updates this week, along with news that its [AI assistant](https://thenewstack.io/jetbrains-launches-new-ai-assistant-powered-by-multiple-llms/) now leverages updated [large language models](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) (LLMs), which means the assistant can provide faster code completion for [Java](https://thenewstack.io/how-to-protect-your-java-against-licensing-liability-risks/), [Kotlin](https://thenewstack.io/angular-18-kotlins-new-compiler-astro-adds-react-19-support/) and [Python](https://thenewstack.io/whos-keeping-the-python-ecosystem-safe/).
“The AI chat is now smarter with GPT-4o support and includes chat references for better context,” a company press release stated. “New capabilities include AI-assisted VCS conflict resolution, in-terminal command generation, and customizable prompts for documentation and unit tests.”

Also with this update, the new [JetBrains UI](https://blog.jetbrains.com/blog/2024/07/08/the-new-ui-becomes-the-default-in-2024-2/) — designed to reduce visual complexity and provide easier access to essential features — is now the default for all users. However, for those who dislike change, the classic UI is available as a plugin.

![Screenshot of the new JetBrains UI.](https://cdn.thenewstack.io/media/2024/08/90c82ae7-jetbrainsui.jpg)
Screenshot of the new JetBrains UI, [via JetBrains](https://blog.jetbrains.com/blog/2024/07/08/the-new-ui-becomes-the-default-in-2024-2/).

Finally, the Search Everywhere dialog now allows developers to preview the codebase elements they’re searching for. JetBrains IDEs will automatically detect and use system proxy settings configured on the developer’s machine by default.

In addition to this news, a few of the IDE-specific updates include:

- Revamped
[Jupyter notebooks](https://thenewstack.io/jupyter-notebooks-the-web-based-dev-tool-youve-been-seeking/)and new AI cells to help iterate faster on data analysis workloads in PyCharm 2024.2; - New IDE functionality, such as the “Add Method to Interface and All Its Implementations” refactoring, and support for the latest
[Go](https://thenewstack.io/golang-how-to-use-the-go-install-command/)features in GoLand 2024.2. The update also includes performance improvements, fixes for remote development and dev containers, and enhanced support for Go frameworks; and - WebStorm 2024.2 support for special path resolving for frameworks with file-system-based routing such as
[Next.js](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/), initial debugging support for Bun, the ability to run and debug TypeScript files directly, version control enhancements and features to improve the user experience.
## New OpenAI Feature Ensures Outputs Match JSON Schemas
[OpenAI introduced this week Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/), a feature that ensures model-generated outputs will exactly match [JSON](https://thenewstack.io/no-cache/key-concepts-json/) Schemas provided by developers.
This is part of an effort that began last year with DevDay when OpenAI introduced JSON mode. JSON mode improved model reliability for generating valid JSON outputs, but didn’t guarantee the model’s response would conform to a particular schema. Structured Outputs in the API ensures model-generated outputs will exactly match JSON Schemas provided by developers, the company said on its blog.

Generating structured data from unstructured inputs is one of the core use cases for AI in applications, OpenAI explained.

“Developers use the OpenAI API to build powerful assistants that have the ability to fetch data and answer questions via function calling (opens in a new window), extract structured data for data entry, and build multistep agentic workflows that allow LLMs to take actions,” it noted.

But developers had to work within the limitations of LLMs by using open source tooling, prompting, and retrying requests to ensure that model outputs match the formats needed to interoperate with their systems, the team noted.

![Chart showing reliability across OpenAI's gpts based on how the JSON model is generated](https://cdn.thenewstack.io/media/2024/08/d19938e3-openaichart.jpg)
Chart showing reliability across OpenAI’s gpts based on how the JSON model is generated. Screenshot via [OpenAI’s blog post](https://openai.com/index/introducing-structured-outputs-in-the-api/).

“Structured Outputs solves this problem by constraining OpenAI models to match developer-supplied schemas and by training our models to better understand complicated schemas,” it added.

Structured Outputs incorporates two forms in the API:

- “Function calling: Structured Outputs via tools is available by setting strict: true within your function definition,” the blog noted. When Structured Outputs are enabled, model outputs will match the supplied tool definition.
- “A new option for the response_format parameter: Developers can now supply a JSON Schema via json_schema, a new option for the response_format parameter,” the post stated. “This is useful when the model is not calling a tool, but rather, responding to the user in a structured way.
There are some limitations and restrictions outlined in the post, such as [Structured Outputs allowing only a subset of JSON Schema](https://platform.openai.com/docs/guides/structured-outputs), which helps OpenAI ensure the best possible performance.

## New Open Source Tool Turns Figma Design into Code
Figma has launched a [new open source project called Handoff](https://www.figma.com/community/file/886892605736203125/handoff-components) that offers a new way for creators and engineers to automate turning Figma design into code.

Handoff is lightweight, cloud-agnostic, and built for the [open source community](https://thenewstack.io/how-to-give-and-receive-technical-help-in-open-source-communities/) under the MIT license. It can extract, transform and distribute Figma decisions as code, bridging the gap between design and development, the company stated. Its code can be tested, improved or deployed from GitHub.

Handoff is built on Figma’s Rest API and is available via the [Figma Marketplace](https://www.figma.com/community/plugin/1376124565609689822/handoff).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)