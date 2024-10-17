# Get Started With Meta’s Llama Stack Using Conda and Ollama
![Featued image for: Get Started With Meta’s Llama Stack Using Conda and Ollama](https://cdn.thenewstack.io/media/2024/10/f221e080-zdenek-machacek-w4oc9l5jmvc-unsplashb-1024x740.jpg)
I like to show tech working in my posts, and on my modest pre-silicon MacBook. So when Meta’s [Llama 3.2 and Llama Stack](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/) for developers were released, I was keen to try it out. However, I discovered that the process is still a little complex and not quite flexible enough.

First of all, what is the stack? Meta has tried to define components of a platform, which can help people build their own Large Language Model (LLM) consuming systems. The main component is *inference,* where the training data is used to predict token responses — which is why we are all here. The slightly awkwardly named *agentic system* refers to the assumption that AI will work with other entities — probably other AIs — as opposed to just responding to chat. But the exact definition of [AI agency](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) is hotly debated. There are plenty of [other components](https://github.com/meta-llama/llama-stack), although I imagine some of these may be redefined in the future. They are accessed by an API of REST endpoints.

The other key term is the definition of a *distribution.* This is where [“APIs and Providers are assembled together to provide a consistent whole.”](https://github.com/meta-llama/llama-stack/blob/main/docs/getting_started.md) At the moment, these are a bit ad-hoc, and a more time will be needed for these to bed established — the success or failure of the platform will be decided on how good these are.

The idea of the stack is solid, though: offer turnkey solutions to the components you aren’t interested in, and select the parts you are.

## Getting Started
You can use a Python-controlled environment to set things up, or Docker. Right now, there aren’t too many references to using Docker.

At the moment, the system doesn’t work on Windows — I found that some of the Python libraries referring to the interactive console were Unix-specific. But this seems minor. The main example template in the stack doesn’t play well without a dedicated GPU, but I could get around that by using an [Ollama](https://ollama.com/) distribution. (If you have a reasonably solid Unix box, you should encounter much less resistance to getting started.)

If you use a [local distribution](https://github.com/meta-llama/llama-stack-apps), it is recommended that you create an isolated Python environment with [Conda](https://docs.conda.io/projects/conda/en/stable/).

## Enter the Python
Conda is an open source tool that comes with both Anaconda and [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/), and it functions as both a package manager and an environment manager. We’ll use the small snake.

I used homebrew to install Miniconda for my trusty MacBook:

1 |
brew install miniconda |
And the version checks out:
Conda changes your prompt to show “base” or “stack” — hence you need to remember to use `conda deactivate`
to turn it off.

These are the first steps to setting up:

12345678910111213 |
#Clone the repo. Note the other directories below meta-llamagit clone https://github.com/meta-llama/llama-stack-apps.git#Create your named conda python environmentconda create -n llama-stack python=3.10#Activate the conda environmentconda activate llama-stackcd llama-stack-apps#install modules from requirements filepip install -r requirements.txt |
[Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) is easy to install, and we’ll use it to work with a slightly earlier and smaller LLM model, 3.1. The idea is that we’ll talk to the server that Ollama sets up at localhost:
Note that my prompt reflects the name we gave conda, “llama-stack”.

Now run the model to check that it works. That prompt is like an inline ChatGPT with the model:

Yes, it took 27 minutes to respond to hello — so as I mentioned earlier, my pre-silicon MacBook is really too underpowered to attempt this.

Note that Ollama can unload from memory, so take a glimpse at this API response to confirm that the model is loaded:

The recommended call to install the Ollama distribution no longer seems to work:

So, use the new build command, which is interactive. Note that the options are nicely provided using the TAB key:

We know we are using Conda, not Docker for this distribution. Confusingly, the available option refers to “remote” Ollama, though it is very much local.

The end of this process completed, with the next clue on the trail:

As you see, it recommends that I configure my new stack, which I named TheNewStackStack. So far, we’ve created, built, installed, and loaded, and now we need to configure. This is what Meta should be looking to simplify in newer versions.

However, I ran the line given, and we got an interactive form where we needed to pair the inference provider to the “remote” Ollama server. The other entries used are the Meta-provided defaults:

I did wonder if I didn’t quite get this right, but again, this appeared to work. In the end, it gave the line to actually run the stack:

Unfortunately, I could not get our TheNewStackStack to run — it didn’t seem to be aware of the Ollama server. So close!

It’s great that Meta has made an early version of their intentions available to access, and if you have a good Unix system and more luck than me it should be accessible. I will have another try on a later release when some of the oddities are ironed out. But this post should give you a feeling for the work you need to do, and the experience you need to push through before you can try out some of the example scripts and actually use the stack!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)