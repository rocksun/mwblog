# How AI Agents Are Starting To Automate the Enterprise
![Featued image for: How AI Agents Are Starting To Automate the Enterprise](https://cdn.thenewstack.io/media/2025/02/99637b45-alexander-mils-zzl4cvkd9mq-unsplashb-1024x576.jpg)
So far, 2025 has been the year of [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) — where generative AI technology is used to automate actions. We’ve seen OpenAI’s Operator debut, demonstrating a prototype [agent](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/) that can browse the web and do tasks for you. Now a new company called [Orby](https://www.orby.ai/) is bringing that same approach to the enterprise, with a type of AI model it calls a Large Action Model (LAM).

I spoke with Orby’s co-founder and CTO, [Will Lu](https://www.linkedin.com/in/will-dongxu-lu-9b9b972b/), about agents in the enterprise. Prior to Orby, Lu had been an engineering leader at Google Cloud AI.

So what is a LAM and how exactly is it different from an LLM? Lu explained that — unlike LLMs, which process text or images as input and generate text or images as output — LAMs are designed specifically for automation tasks in enterprise environments. He mentioned Salesforce and SAP as examples of IT software products its LAM has explored, in order to identify tasks that can be automated.

LAMs take *actions* as input, he continued — giving as examples application screenshots, webpage HTML content, user interactions (such as mouse clicks and keyboard inputs). He says that Orby’s LAM can use that context to automate complex workflows.

## Traces of Enterprise Software
Lu used the word “traces” to describe the workflow data that its foundation LAM, called [ActIO](https://www.orby.ai/actio), has been collecting. He said it has collected “over a million traces, and usually a trace can be 10 to 50 steps long.”

In a clarification email after, Lu expanded on the definition of ‘trace’:

“…a trace is a sequence of actions for completing a specific task. An action is captured as a combination of contexts, screenshot & html for web applications & accessibility trees for desktop applications, and events, such as mouse click, key type, etc.”

He went on to explain that their software actively explores enterprise software environments (e.g., Salesforce, ERP systems) to identify tasks that can be automated. The agent autonomously attempts these tasks, and the best-performing attempts (successful traces) are used to fine-tune the model.

Like most other large language models, Orby has trained ActIO on open web data. However, Lu added that they can also fine-tune using a customer’s proprietary data.

## Comparisons to OpenAI’s Operator
Orby’s solution has similarities to OpenAI’s Operator, which [launched](https://openai.com/index/introducing-operator/) near the end of January. Operator, currently only available to Pro users ($200 per month), was described by OpenAI as a “research preview of an agent that can use its own browser to perform tasks for you.” In a review, Kevin Roose of the New York Times [called it](https://www.nytimes.com/2025/02/01/technology/openai-operator-agent.html) “more an intriguing demo than a product I’d recommend using — and definitely not something most people need to spend $200 a month on.”

I asked Lu how Orby compares to OpenAI Operator?

One of the differences, he said, is that Orby has a concept it calls “grounding.”

“Basically, grounding is [for] a specific action you want to do — say, for example, submit a report. So that’s the action, and then you want to find the elements that can get that thing done, and then trigger it. That’s called the grounding step.”

This concept comes from a project Orby did alongside Ohio State University, called [UGround](https://osu-nlp-group.github.io/UGround/) — described as “a universal visual grounding model for locating the element of an action by pixel coordinates on GUIs.” UGround was trained on 10M elements from 1.3M screenshots.

“When it comes to really complex, real enterprise use cases, what we expect is technical people to make sure that it runs at scale.”

– Will Lu, Orby CTO
Lu also noted that Orby has an AI agent software stack that it offers to enterprises.

“So basically […] we designed it so that users can demonstrate how a task is done. Based on that demonstration, we generate both the description and the code under the description to be run. Then […] developers can come in, look at the description and generated code, and make modifications to their needs — and then run the agent based on the code that the app defined.”

Lu added that for simple tasks, non-technical employees can run those. But for more complex “actions,” developers are typically involved.

“When it comes to really complex, real enterprise use cases, what we expect is technical people to make sure that it runs at scale. When, for example, a task is currently being done by 100 people, you want to make sure that the virtual machine is set up correctly, the agent is running in the same environment there, and can they get access to all the systems and all the credentials.”

## Advice for CIOs
AI agents, or [agentic AI](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) to use the trendy term, has rapidly become a priority for enterprise IT departments to consider. So I asked Lu what advice he’d give to CIOs and other enterprise IT leaders, when considering if and when to use AI agents.

“I think the most critical thing is to find real business pain that users are looking for,” he replied. “And then, when it comes to business pain, we want to identify the steps that are very time-consuming for users.”

Those steps might be time-consuming for human employees, but “really, really easy for a computer to do,” he added.

One use case from Orby’s customers is expense report auditing.

“Almost every enterprise has this process, and the process is kind of tedious,” Lu said. “You have to open a report, look at all the receipts, look at all the information being filled out, and then check whether the information matches […] or not. And also check those reports against the policies that are defined by the company — like, for example, there’s no alcohol [allowed].”

“…as long as our agents get access to the system […] we can log into the system and then conduct the work.”

– Lu
My instinctual follow-up question as a tech journalist was to ask what APIs Orby’s software connects to — SAP, for example. But Lu confirmed that it’s all done via an AI agent; no APIs are needed.

“That’s the beauty of our solutions. We [Orby’s software] mainly operate those applications as if we were humans operating those systems. So there’s no actual integration needed. So as long as our agents get access to the system, as long as we have the credentials, we can log into the system and then conduct the work.”

So, how about security concerns? Lu confirmed that security is “always a top ask from almost all the enterprises” and that they work with each customer on that.

Lastly, it’s worth noting that even though Orby’s goal is to help enterprises automate workflows, for now there is always a human in the loop.

“There’s a whole agentic workflow design [that] is a core of our whole offering, because the models today still don’t work 100%, and it will still be that way for a very long time,” said Lu. “So we have this human loop process built in by design.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)