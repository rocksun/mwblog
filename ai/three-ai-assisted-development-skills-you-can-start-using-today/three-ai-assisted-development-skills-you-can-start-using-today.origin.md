# Three AI-Assisted Development Skills You Can Start Using Today
![Featued image for: Three AI-Assisted Development Skills You Can Start Using Today](https://cdn.thenewstack.io/media/2025/04/be67445e-aws-ai-developer-skills-use-1024x578.jpg)
Things are changing fast in [AI](https://thenewstack.io/ai/), as if developers didn’t have enough to keep up with. The New Stack recently spoke with [Antje Barth](https://www.linkedin.com/in/antje-barth/), the principal developer advocate for generative AI (GenAI) at [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), about how developers can prepare for an increasingly[ AI-driven enterprise](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/).

Barth shared how AI is changing development and how software engineers can adjust to the new realities of AI development.

## 1. Shift To AI for Code Creation
When [large language models](https://thenewstack.io/llm/) (LLMs) entered the spotlight after [the release of OpenAI’s ChatGPT-3](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/) in late 2022, code correction became an immediately evident use case. A [slew of coding copilots became available](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/).

While those are still popular, the cutting edge now is in “[vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/),” which uses the natural language capabilities of AI to create code. The [term was coined](https://x.com/karpathy/status/1886192184808149383?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1886192184808149383%7Ctwgr%5Eb693bc66e22eeb798ec744f69374aeea4cab7926%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fthenewstack.io%2Fvibe-coding-where-everyone-can-speak-computer-programming%2F) by [data scientist](https://roadmap.sh/ai-data-scientist) [Andrej Karpathy](https://github.com/karpathy) in 2023, and it’s steadily gained attention since.

“There’s a new kind of coding I call ‘vibe coding,’ where you fully give in to the vibes, embrace exponentials, and forget that the code even exists,” Karpathy wrote in a post on X. “It’s possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also, I just talk to Composer with SuperWhisper so I barely even touch the keyboard.”

Vibe programming moves beyond code correction to using the AI to create the whole code via natural language prompts, which are also used to refine the code if needed. It’s made programming more intuitive, Barth said.

She pointed to tools like [Amazon Q ](https://thenewstack.io/amazon-q-developer-now-handles-your-entire-code-pipeline/)[Developer](https://thenewstack.io/amazon-q-developer-now-handles-your-entire-code-pipeline/) and other copilots on the market that allow users to communicate in natural language. They don’t just generate code, she noted, but can be used across the software development lifecycle to create unit tests, [documentation](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/) and other development tasks.

“Vibe coding captures everyone’s attention at the moment,” Barth said. “I see it really kind of an evolution, rather than a completely new concept, which is exciting.”

That has led to questions about whether organizations will even need developers to know code.

“There’s different opinions as well in the industry, but I strongly feel, coding is a critical skill, a super critical skill, and it’s not just to write code, but also to read code and to be able to understand what is good quality code, and is it exactly that code that I need for my application,” she said.

But, she added, “I also see that AI assistance and the tooling around it can augment you as a developer to be faster.”

She envisioned the process as using AI to quickly generate the code for a prototype and determine if an idea is feasible. The software engineer’s technical knowledge comes into play when the prototype is put into production in larger systems.

“There is definitely great opportunity around vibe coding to start off and then, obviously using the tools across the cycle,” she said. “But the knowledge is really critical.”

## 2. Let AI Write Its Own Prompts
[Prompt engineering](https://thenewstack.io/developer-tips-in-ai-prompt-engineering/) was [all the rage in the wake of ChatGPT-3](https://thenewstack.io/how-will-generative-ai-change-the-tech-job-market/). But there’s no reason to stress about prompt creation unless you’re just curious about it, according to Barth.
“These days, my advice is to actually use the AI to create a good prompt.”

— Antje Barth, principal developer advocate for generative AI, AWS
“A year ago, I think I would have totally told you prompt engineering is a critical skill to have,” Barth said. “These days, my advice is to actually use the AI to create a good prompt. Before you give it detailed instructions, I would ask the AI, ‘Hey, this is what I want to accomplish; help me create a really, really solid and good prompt to achieve this.’”

Having the AI write its own prompt is also advisable because different AI systems have different and unique ways to prompt, she added.

“I should have a basic understanding of why this is important and how to structure, but the actual prompt writing, I can totally use the AI for this these days, too.”

## 3. Use Embedded and Agentic AI
Thanks in part to [AI agents](https://thenewstack.io/ai-agents/), AI is shifting away from its original chatbot interface to becoming an embedded tool that’s highly specialized to work processes or tasks. This is a particularly key trend for frontend and web application developers, who will need to figure out how to embed AI functions in the user interface.

For instance, [Amazon Q Developer started as a chatbot](https://aws.amazon.com/blogs/devops/aws-chatbot-is-now-named-amazon-q-developer/). While you can still use it that way, Amazon launched on March 6 the new [Amazon Q Developer CLI](https://aws.amazon.com/blogs/devops/introducing-the-enhanced-command-line-interface-in-amazon-q-developer/). It’s basically an enhanced agent that mirrors the experience developers have with their internal development environment (IDE) with Amazon Q, Barth said, but from within the CLI.

“CLI support was out for Q for over a year, but now it has the agentic capabilities matching the experience from the IDE,” she told The New Stack. “What that means is, with agentic AI, the system ultimately uses a high-quality language model to help it reason and plan. In this case, Q Developer CLI is built on top of [Bedrock](https://thenewstack.io/amazons-bedrock-can-now-check-ai-for-hallucinations/) and it uses Claude Sonnet 3.7, so it has really kind of high-quality reasoning capabilities, and you can [have] a natural language chat in your CLI, and it makes life so much easier.”

Barth said she uses the tool almost daily. One task it has made easier is handling [git commands](https://git-scm.com/docs).

“I don’t have to remember how to reverse a [git](https://thenewstack.io/tutorial-git-for-absolutely-everyone/) commit, for example, in the syntax anymore,” she said. “I can just tell it a natural language, ‘Hey, please revert this last git commit for me,’ and it comes up with the correct CLI BASH command for me.”

In a similar vein, she can ask it, “What are my S3 buckets in this region?” and it translates it to the correct AWS CLI syntax.

“This is where we see agentic AI improving developer experience,” Barth said. “Every application, probably every customer experience, UX, will be disrupted with agentic AI.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)