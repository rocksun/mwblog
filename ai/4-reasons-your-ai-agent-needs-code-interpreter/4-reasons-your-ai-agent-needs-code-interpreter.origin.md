# 4 Reasons Your AI Agent Needs Code Interpreter
![Featued image for: 4 Reasons Your AI Agent Needs Code Interpreter](https://cdn.thenewstack.io/media/2024/04/dfa23f6e-robot-1797548_1280-1024x576.png)
Building AI agents is hard. You’ll struggle with
[hallucinations](https://thenewstack.io/the-security-risks-of-generative-ai-package-hallucinations/), keeping the agents on track and [navigating them](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/) to use the right tools.
One way to overcome these problems is to give agents code-execution capabilities.
Here are some reasons why your AI agent should have a code interpreter.
**1. Extra Skills**
Agents with code interpreters gain powers like performing a statistical analysis of CSV files or plotting charts.
When you ask different agents for the same thing, it becomes evident how much those with an underlying code interpreter differ. The following tasks are almost impossible to finish without running code:
- Analyze NVIDIA stock and predict its development.
- Play a Poker game with me.
- Book me a flight.
See how Perplexity (an agent without a code interpreter) deals with a data analysis task. Even when provided a data file, the agent cannot finish the task — the best it can do is provide advice on what code I should run.
Here is how ChatGPT with an underlying code interpreter would deal with the same task…
… including the installation of new packages and generating a chart.
Note that the end users don’t
[need to be aware that the app carries out coding](https://thenewstack.io/why-your-code-needs-abstraction-layers/) tasks behind the scenes since the primary objective (like “book me a flight”) often doesn’t revolve around coding.
**2. Complex Reasoning** [Large language models](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) (LLMs) are great at generating text [but struggle](https://thenewstack.io/3-ways-llms-can-let-you-down/) with reasoning and complex thinking.
Google’s team
[made an interesting parallel](https://blog.google/technology/ai/bard-improved-reasoning-google-sheets-export/) from the famous book “Thinking, Fast and Slow” by Daniel Kahneman. The ability to execute code equips agents with slow thinking (effortful, logical and calculating) versus fast thinking (intuitive and automatic), and is represented by how agents act without a code interpreter.
In their analogy, agents relying purely on LLMs can be thought to operate without slow thinking, quickly producing text without a deeper thought. Below is an example of how even simple tasks might require some system and cannot be answered just intuitively.
**3. Reducing LLM Hallucinations**
A recent
[ paper](https://arxiv.org/abs/2305.13534) confirmed that LLMs are hallucinating on multistep tasks even when given reasoning prompts. As a follow-up to the findings from the paper, a software engineer [demonstrated](https://aditya-advani.medium.com/mitigate-gpt-4-hallucinations-using-code-interpreter-29fea4887eec) how using a code-interpreter-style LLM engine successfully reduces hallucinations by an order of magnitude. He found that code interpreters can reduce the GPT-4 hallucination rate from <10% to <1%.
Code interpreters can handle uploads and downloads, write code to look up data from source files and arrive at conclusions instead of reasoning freestyle like simpler agents usually do.
Other
[ways to battle LLM hallucinations](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/) include RAG, fine-tuning and increasing the size of LLM context windows.
**4. Testing**
Another big challenge is the LLM code generation. When an agent can not only
[generate but also run code](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/), it’s able to test the functioning of its own output and iterate on it.
## Building with Code Interpreters
I think we will see code interpreters powering even more AI agents and apps as a part of the new ecosystem being built around LLMs, where a code interpreter represents a crucial part of an agent’s brain. For inspiration to build, see popular open source products like
[ Open Interpreter](https://github.com/OpenInterpreter) or [ AutoGen](https://github.com/microsoft/autogen).
There are still challenges to overcome, such as finding a secure and optimal way to run the LLM-generated code, which can be solved by executing the processes in an
[ isolated cloud environment](https://e2b.dev/docs). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)