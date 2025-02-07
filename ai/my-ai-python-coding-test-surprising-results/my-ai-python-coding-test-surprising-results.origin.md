# My AI Python Coding Test: Surprising Results
![Featued image for: My AI Python Coding Test: Surprising Results](https://cdn.thenewstack.io/media/2025/02/0aee6a55-jeshoots-com-2vd8lihdnw-unsplash-1-1024x683.jpg)
You know it’s coming.

You’ve heard the grumblings.

You’ve read the memos and listened to the talks.

AI is writing code.

Trust me, I get the concern. I’m also a novelist and I’ve read accounts of other writers using AI to bang out books at a rate for which the human being cannot keep up. The silver lining there is that creative efforts undertaken with AI tend to be pretty bad.

But what about the coding side of things?

I decided to put [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) to the test and have it write some [Python](https://thenewstack.io/python/) programs to see how it fared.

I was not impressed.

First, let me tell you how I did this.

## What I Used
To begin with, I decided to use a locally installed instance of Ollama, with the [Msty](https://msty.app/) frontend. I decided to add the frontend into the mix because I wanted it to be as efficient as possible. Although the terminal usage of Ollama is fairly simple, Msty makes some of the features more accessible (such as adding new models and Knowledge Stacks and using a prompts library).

Initially, I decided to use the llama-3.2 model for the first round of testing. I fed Ollama the following prompt:

1 |
Write a Python application that asks the user how many dice to roll, how many sides are on each dice, and then roll the dice the user has entered |
Here’s the code llama-3.2 spit out:
Guess what? It didn’t work. It looked as though it was going to function perfectly, but then it wound up stuck in a loop asking *How many dice would you like to roll?*
There were a few obvious errors in the code. Take a look at line 49, which is this:

1 |
first_half = ', '.join([str(result)[:half_points] for result in results.split(',')[0:-1]]) |
That should be:
1 |
first_half = ', '.join([str(result)[:half_points] for result in result.split(',')[0:-1]]) |
Ollama’s output had *results.split*, when it should be *result.split*. That’s a pretty goofy error, but it’s easily fixed.
There’s another similar error in the line below that, which is:

1 |
second_half= [result[half_points:]for result in results.split(',')] |
That should be:
1 |
second_half= [results[half_points:]for result in results.split(',')] |
After making those changes, the program finally runs.
Even then, if you enter a larger number when asked how many dice to roll, the error pops back up, only this time telling you that *results.split *should be *result.split*. Guess what… that won’t run either!

I then tried the same prompt with the gemma2:2b model. As you probably expected, the code generated wouldn’t work. Again, it wound up caught in a loop, asking how many dice to roll.

If I pare the program down to simply create an app to roll random dice numbers, gemma2:2b gets it right.

I went back to each model and ran different queries to have it create various [Python apps](https://thenewstack.io/how-to-use-pyscript-to-create-python-web-apps/) (of varying degrees of difficulty) and found it to be hit-and-miss. For instance, I wrote this query for gemma2:2b:

1 |
write a python program that accepts input for a users clothing choices and then reports what they should wear |
The output of that query worked fine. I then ran the same query with the Llama 3.2 model, and the code it produced was vastly different, but it ran as well.
Here’s where things get annoying.

I added the [DeepSeek R1](https://thenewstack.io/how-to-run-deepseek-r1-on-aws-using-infrastructure-as-code/) model to Msty, and every time I queried, the response seemed more like a long, drawn-out discussion on how to write code. What llama and gemma took roughly 30 seconds to spit out, [DeepSeek](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/) ran for 10 minutes and gave me nothing I could use other than a long-winded back and forth that felt as random as it was guided.

## What I Discovered
In the end, here’s what I discovered about using AI to write code:

- Start with a simple query, such as Write a program to roll a die.
- Test the output.
- Then ask the AI to update the original with a query such as
*taking that same program and allowing it to ask users how many dice to roll.* - Test the output.
- Further, refine the application with another query.
- Test the output.
- Keep refining until you’re done.
Whenever I used Ollama and Msty to write Python programs with the above tactic, the results were much better than diving into something more complex. The other takeaway is that different models are better suited for this purpose. For example, skip right past DeepSeek and use one of the Qwen models (such as Qwen2.5 Coder). When I attempted the same experiment using the Qwen2.5 Coder LLM, things were a bit more predictable. Almost every time I used this model, the results worked. Even better, the code it produced was far less complicated, so it was easier to read and debug (when needed).

Another thing is not to expect perfect results. You *will* have to tweak things and even try out different models. I even ran across issues with Msty tanking on me, which helped me draw this simple conclusion:

The companies creating AI want you to believe their tools are as capable as you are at writing code and that is not exactly true. When you use AI to write code, it’s imperative that you comb through every line in the output and test it because, more than likely, you’re going to have to spend a good amount of time debugging.

I was actually excited about writing this piece because I’d tested Ollama and Msty with some fairly basic applications, and it performed admirably. When things got more complex, however, AI let me down.

In the end, remember these key things:

- Choose the right model.
- Start off simple.
- Vet the code.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)