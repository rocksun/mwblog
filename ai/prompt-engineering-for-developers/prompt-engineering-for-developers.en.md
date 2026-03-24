When I first started writing prompts, I had the unrealistic expectation that since [LLMs](https://thenewstack.io/introduction-to-llms/) “know everything,” they would always execute perfect outputs. With that expectation, the prompts I built early on gave the model a wide range of potential outputs. And I was left wondering whether I was working with the same AI as everyone else who thought it was amazing.

I have a lot of opinions about AI, but in the case of my frustrations with its output, I was the problem. If you, too, are the architect of your own struggles when it comes to LLM output, fear not. Help is here.

## What is a prompt?

Anything you ask of an LLM model. In more technical terms, it’s any input you send to a model. This could be a single word or a detailed system message, and anything in between.

In the context of prompt engineering, a prompt is a designed input structured to elicit a reliable output.

## What does prompt engineering really mean?

When I used to think about prompt engineering, I thought about telling the model my thoughts, expecting it to take an unclear input and output a finished version of my project. That isn’t prompt engineering.

For example, the same prompt “draw a cat” will give you a different result every time you use it. But if you’re actually looking for an image of a black cat, smiling, with a red bowtie, ask for that specifically. You still won’t get the same result each time, but the result you do get will be closer to aligning with your expectations and likely be something you and the model can iterate on rather than starting over and over again.

Yes, this is a silly example and an obvious user prompt, but it so clearly illustrates a poorly designed prompt. If you want a drawing of a black cat with a red bowtie, you’ll just ask for that. But when the topic is a little more challenging, like “design a system that handles user authentication”, the ask may appear less clear. How many users does the site have? Is it a [microservices](https://thenewstack.io/introduction-to-microservices/) architecture? Do you want OAuth, JWT, or session-based auth?

That was a very long way of saying that engineering a good prompt will reduce variance and increase reliability.

## How LLMs process prompts

LLMs aren’t magic mind readers. What we may consider thinking or reasoning when done by a human is something else when it comes to an LLM. LLMs follow statistical patterns learned during training, and they’re very good at pattern-matching an output to your input prompt. Even better when you help them find the pattern you want.

LLMs follow a hierarchy when following instructions:

* System instructions carry the most weight
* Developer instructions come next
* User input comes last

## How to build better prompts

If you need something specific, say you want to build an internal tool that lets your team query a database using plain English, take time to research before you start prompting. Understand what the tool actually needs to do. Ask yourself the hard questions first: does it need to handle multiple table joins, should it validate queries before running them, who has access, how do you handle a query that returns nothing? The clearer you are on what you want before you start, the less time you spend telling the model to do it over.

You don’t have to be an expert. LLMs can help you do your research. But do your research and know what you want the LLM to build before building the website.

### Strong prompts include the following in their instructions:

**Clear instruction**: Know what you’re looking for and ask for it clearly. “Build a to-do list app” gives the model too much latitude. “Build a to-do list app with tasks that clear from the screen when I check them off and a calendar so I can assign tasks per day” refines the output.

**Context**: Give the model what it needs to perform the task well. Unnecessary context increases noise, but too little leads to generic outputs. If you’re building a backend tool for engineers, tell the model: “The user is a senior backend engineer working with distributed systems.” That one line shifts tone, vocabulary, and assumed knowledge.

**Constraints**: Without constraints, the model will fill in the gaps. This expands the realm of possible outputs. Strong constraints align output possibilities with your expectations.

**Output format**: If you’re writing code, this is important. If you don’t specify a format, you can’t reliably parse the output. Even if the model returns something sensible-looking 90% of the time, that remaining 10% will break your pipeline at the worst moment. Specify the structure you expect:

## Prompt patterns every developer should know

We don’t need to reinvent the wheel each time we need something from an LLM.

**Few-shot prompting** provides the model with a mini-dataset. The dataset consists of exactly what you’re looking for in terms of output, structure, tone and style. If you find yourself writing lengthy details about your output expectations, you might want to swap that out with a few-shot prompt.

**Chain-of-thought** prompts are great to use when you’re unsure of what you need. These prompts ask the model to reason step by step before answering. Yes, this improves the quality of tasks that require judgment. Another benefit is that it allows you to work as a thought partner alongside the LLM.

**Role prompting** improves the model’s output when you’re building something for a certain audience. You’d build something different for a beginner than you would an expert. Set the domain context by including “You’re a [data analyst](https://thenewstack.io/can-you-trust-ai-to-be-your-data-analyst/) working primarily with Snowflake data focused on product analytics.” This will influence the vocabulary, assumed knowledge, and possible tradeoffs.

**Tool-augmented prompting** turns the model into a source of real information by giving it access to your tools. Tool-augmented prompting will help you get an answer to a specific question like “What did the deployment pipeline return for the last build?” as long as you also provide a function that queries your system, like `get_ci_build_status(pipeline_id: str) -> BuildResult` to call.

## Pro tips

Because learning how to do something makes that something look easier than it does in practice.

* Evaluation matters too. You won’t know if a prompt works until you measure it.
* Validate. Validate inputs. Validate outputs. Have a plan for what to do when the model returns something unexpected.

## Conclusion

The best way to summarize this article is to take a look at the differences between a good prompt and a vague prompt.

Vague prompt:

Good prompt:

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)