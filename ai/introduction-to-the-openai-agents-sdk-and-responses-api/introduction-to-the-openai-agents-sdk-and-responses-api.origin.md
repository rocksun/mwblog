# Introduction to the OpenAI Agents SDK and Responses API
![Featued image for: Introduction to the OpenAI Agents SDK and Responses API](https://cdn.thenewstack.io/media/2025/03/9c5be4c1-yasa-design-studio-yoh9dcqndii-unsplashb-1024x576.jpg)
As OpenAI introduced what everyone else is calling the [Agents SDK](https://openai.com/index/new-tools-for-building-agents/), it admitted that using the existing capabilities in a joined up fashion “can be challenging, often requiring extensive prompt iteration and custom orchestration logic without sufficient visibility or built-in support.” In short, using [agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) needed quite a bit of programming, and that is not the story any AI provider wants to sell.

To return the narrative back to the idea that spending money on AI will eventually eradicate the need for expensive human software development, or indeed humans, OpenAI is implementing a structure to allow for simple orchestration.

Let’s first summarize what the problems are. Agentic tasks imply at least two processes working individually, with one task starting another and with the results reporting back to a final reporting process in the end — hopefully at similar times. The “results” also have to be in a known format (e.g., a sentence, a file, an image, a database), but this is not easy to generalize. Even the happy path is a fine balance — dealing with and explaining errors is another problem. These are all familiar orchestration problems. But as an industry, no one believes orchestration is a “solved” problem. Heavy LLM use also adds the need to control token usage; [tokens](https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/) being the new black gold.

To start the orchestration journey, OpenAI has added some new APIs to its core platform. Notably, it has introduced a basic **Responses API** that cleans up some of the assumptions made by the chat agents.

In the simplest sense, this can capture the output:

123456789 |
from openai import OpenAI client = OpenAI() response = client.responses.create( model="gpt-4o", input="Write a one-sentence bedtime story about a unicorn." ) print(response.output_text) |
You can analyse images at this level; and add one of the tools below. Beware: new models are likely to stop supporting the existing Chat Completions API — many new features only support the new Responses API.
Let’s look at these new tools. **Web search** allows an agent to crawl the web for simple tasks. The short Python script below shows how a model is given the option of using this tool:

12345678910 |
from openai import OpenAIclient = OpenAI()response = client.responses.create( model="gpt-4o", tools=[{"type": "web_search_preview"}], input="What Kubernetes news story appeared today?")print(response.output_text) |
The `reesponse`
will also contain references to any cited articles. These queries can be defined by time or location. You can also weigh the cost, quality and latency.
**File Search** is effectively a hosted vector store. You indicate that file search is an available tool, and identify your vector store:
123456789101112 |
from openai import OpenAIclient = OpenAI()response = client.responses.create( model="gpt-4o-mini", input="What is deep research by OpenAI?", tools=[{ "type": "file_search", "vector_store_ids": ["<vector_store_id>"] }])print(response) |
If needed, an Agent will use it. The response will cite the documents used in the response. You can limit the responses to control token usage and latency. There are [limits to total file size](https://platform.openai.com/docs/guides/tools-file-search#limitations), files searched, and the size of the vector store. The types of documents searchable (by file type) [seem extensive](https://platform.openai.com/docs/guides/tools-file-search#supported-files).
The **Computer Use** tool is interesting:

“The computer use tool operates in a continuous loop. It sends computer actions, such as `click(x,y)`
or `type(text)`
, which your code executes on a computer or browser environment and then returns screenshots of the outcomes back to the model.”

This sounds like it is pretending to be [Selenium](https://www.selenium.dev/), the tool we used to use to test web interfaces via scripts. Obviously this acknowledges that we are not yet in the AIs only talking to other AIs world yet. But it is at least a nod to the idea that not everything is a web site.

## Trying Out Agents
I’ll use the Python examples (it is definitely a Python-first product, but the docs also show the JavaScript equivalent script). We’ve run Python a few times in my posts, but on my new MacBook, I’ll just check that I have Python installed:

The result was that python@3.13 3.13.2 is already installed and up-to-date.

My pip is also there (as pip3).

So now I can install the OpenAI packages:

Ah, I remember this. We need a virtual:

I then activate the virtual:

And we are ready to proceed.

Now of course, you will need to use and set an OPENAI_API_KEY. I created myself a new key on my [account page](https://platform.openai.com/settings/organization/api-keys), and set the OPANAI_API_KEY (don’t worry, it is much longer than this):

And you gotta make sure you have some black gold — [I mean tokens](https://platform.openai.com/settings/organization/billing/overview). I’ve presented some of the ways to avoid paying OpenAI by using [local models](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/), but for this post I’ll assume you are paying for tokens.

As is traditional, lets just start with a check that the above basics are in place via a simple request with the following **haiku.py:**

123456 |
from agents import Agent, Runneragent = Agent(name="Assistant", instructions="You are a helpful assistant")result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")print(result.final_output) |
And we get a fine response:
(A good traditional haiku should make a mention of the passing seasons, but that’s not why we are here.) Usually, I’d check my balance as well — but it has not been disturbed.

## Nest of Agents
As you see, we have already used an [agent](https://github.com/openai/openai-agents-python). Not that it intervened in any way, but we’ll come to that.

OpenAI has simplified the orchestration process with some simple terms. A **handoff** is an introduction to the asynchronous world, where something has to wait for something else. Let’s break down their example, which I’ll run as **hola.py**:

12345678910111213141516171819202122232425 |
from agents import Agent, Runnerimport asynciospanish_agent = Agent( name="Spanish agent", instructions="You only speak Spanish.",)english_agent = Agent( name="English agent", instructions="You only speak English",)triage_agent = Agent( name="Triage agent", instructions="Handoff to the appropriate agent based on the language of the request.", handoffs=[spanish_agent, english_agent],)async def main(): result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?") print(result.final_output)if __name__ == "__main__": asyncio.run(main()) |
This displays two basic things. First of all the role setting for agents in plain English that we are used to, but also setting up the interplay between agents. The handoff agent keeps a list of available agents to answer responses.
Now, this implies that my German request will not get the right response. So if we change the query within **hola.py**:

1234567 |
...async def main(): result = await Runner.run(triage_agent, input="Wie geht es ihnen?")... |
And run our nest of agents:
So, while OpenAI had no problem translating German, the triage agent had no relevant language agent to hand to, so it did the job and responded in English. Our German customers are unlikely to be too upset, but we can improve.

So if we finally add the German agent and put it in the handoffs list to **hola.py**:

123456789101112 |
...german_agent = Agent( name="German agent", instructions="You only speak German",)triage_agent = Agent( name="Triage agent", instructions="Handoff to the appropriate agent based on the language of the request.", handoffs=[spanish_agent, english_agent, german_agent],)... |
We can try that German request again:
This time the correct agent is called, and responds. Our German customers are now happier — ausgezeichnet! Don’t forget that [my Warp terminal](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) is giving you the times for these responses too.

## Conclusion
We first looked at the response loop, which may include further tool calls. If the response has a handoff, we set the agent to the new agent and go back to the start.

There are logging options below this, but as usual OpenAI is giving quite a high level API at this stage — which should encourage experimentation without the need to get too involved with orchestration.

While I’ve introduced agents here, in later posts, I’ll look at further parts of the SDK.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)