# CodeGate: Open Source Tool Secures AI Coding Assistants
![Featued image for: CodeGate: Open Source Tool Secures AI Coding Assistants](https://cdn.thenewstack.io/media/2024/12/de20e3a0-codegate-ai-project-2-1024x576.jpg)
That friendly, ever-so-helpful AI coding assistant? You can’t trust it.

Most programmers now use [AI coding assistants](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/) such as [GitHub Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/), [ChatGPT](https://thenewstack.io/how-to-learn-unfamiliar-software-tools-with-chatgpt/), and [Amazon Q Developer](https://thenewstack.io/amazon-q-developer-now-handles-your-entire-code-pipeline/). In fact, according to a 2024 Stack Overflow survey, [76% of respondents already use or plan to use AI code assistants](https://stackoverflow.blog/2024/05/29/developers-get-by-with-a-little-help-from-ai-stack-overflow-knows-code-assistant-pulse-survey-results/).

That may be a big mistake.

In an e-mail interview, [Craig McLuckie](https://www.linkedin.com/in/craigmcluckie/), one of [Kubernetes’ co-creators](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/) and founder and CEO of [Stacklok](https://stacklok.com/), a software supply chain security company, told The New Stack, “Over the past weeks, I have watched AI coding assistants exfiltrate secrets to OpenAI, and I’ve seen various [large language models] recommend deprecated and dangerous (even hallucinated) packages that AI coding assistants then try to install.”

Yow!

It gets worse. “It gets doubly complicated because foreign adversaries have been busily publishing malicious packages with names that are commonly hallucinated,” McLuckie added.

To combat this problem, he said, StackLok has a new open source project, [CodeGate](https://codegate.ai/). Locally hosted (i.e., run by developers on their own machine) is what he calls a “privacy-focused solution that acts as an essential layer of security within a developer’s generative AI workflow.”

## How CodeGate Works
Specifically, CodeGate, licensed under [Apache 2](https://opensource.org/license/apache-2-0), acts as a local proxy between developers and AI coding assistants. The program runs within a dedicated [Docker](https://www.docker.com/?utm_content=inline+mention) container. It ensures that sensitive information remains protected while leveraging AI’s productivity benefits.

CodeGate does this by monitoring prompts for code secrets, such as API keys and credentials. It encrypts your secrets on the fly as your code goes back and forth between your workstation and the AI service.

This commitment to privacy is a standout feature. The tool operates entirely on your local machine, ensuring no data except the coding assistant’s required traffic leaves your system.

The program also blocks potentially harmful libraries and deprecated dependencies by using a real-time database to identify them and intervening when an AI tool suggests such questionable components. As McLuckie told TNS, “It alerts the developer whenever an LLM recommends an unsafe dependency, but otherwise sits quietly in the background.”

CodeGate currently supports integration with popular AI providers such as [OpenAI](https://openai.com/) and [Anthropic](https://www.anthropic.com/), as well as tools like GitHub Copilot and [continue.dev](https://www.continue.dev/). The developers plan to expand compatibility by including more tools, such as the AI pair programming tool [aider](https://aider.chat/) and the AI code editor [Cursor](https://www.cursor.com/).

As the software development landscape evolves with AI integration, tools like CodeGate will play a crucial role in balancing the benefits of AI assistance with the necessary safeguards for security and privacy. [CodeGate’s open source code base](https://github.com/stacklok/codegate) invites collaboration and scrutiny from the developer community, which should help accelerate improvements and widespread adoption.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)