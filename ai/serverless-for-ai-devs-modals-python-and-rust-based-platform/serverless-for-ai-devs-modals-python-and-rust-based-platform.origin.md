# Serverless for AI Devs: Modal’s Python and Rust Based Platform
![Featued image for: Serverless for AI Devs: Modal’s Python and Rust Based Platform](https://cdn.thenewstack.io/media/2025/01/66ff29cd-osarugue-igbinoba-ekkn8um6mmc-unsplash2-1024x576.jpg)
[Serverless](https://thenewstack.io/serverless/) has been a trend in internet development for the past decade or more, but has taken on new meaning in the generative AI era. [Modal](https://modal.com/) specializes in providing serverless infrastructure tailored for compute-heavy and long-running AI, ML, and data workflows, which are typically challenging for conventional serverless solutions. It’s aimed squarely at developers who don’t want to deal with the massive computing demands of LLMs and other AI infrastructure.
Before we look at what Modal offers, here is a quick reminder about what “serverless” is. The term was [coined around 2012](https://web.archive.org/web/20121017030524/http://www.readwriteweb.com/cloud/2012/10/why-the-future-of-software-and-apps-is-serverless.php) in a ReadWriteWeb article but really only gained traction after the release of AWS Lambda [at the end of 2014](https://thenewstack.io/serverless-on-public-cloud-the-ultimate-showdown/). Like many IT terms, the definition has become muddled over time, but basically, it refers to when server technology is [abstracted away for a developer](https://thenewstack.io/serverless-has-unlocked-a-new-world-of-cloud-mashups/), typically using cloud platforms. Servers still exist, of course, but the developer needn’t worry about configuring them — that’s what a serverless provider does.

Modal takes that concept and brings it to the compute-intensive workloads of AI. According to the company, its customers use Modal “for a wide range of use cases, including Generative AI inference, LLM fine-tuning, computational biotech, and media processing.”

## ‘Lambda on Hard Mode’
In a recent blog post, founding Modal engineer Eric Zhang [called its service](https://modal.com/blog/serverless-http) “Lambda on hard mode.” In the post, he pointed out the “constraints” of a traditional serverless function platform like [AWS Lambda](https://thenewstack.io/theres-a-service-for-that-amazon-web-services-and-serverless-computing/):

“Functions on AWS Lambda are limited to 15-minute runs and 50 MB images. As of 2024, they can only use 3 CPUs (6 threads) and 10 GB of memory. Response bandwidth is 16 Mbps.”

This, Zhang claimed, doesn’t cut it in our current AI-driven world. He stated that Modal containers “can each use up to 64 CPUs, 336 GB of memory, and 8 Nvidia H100 GPUs.” Its containers, he wrote, “are potentially long-running and compute-heavy, with big inputs and outputs,” which, he added “is the opposite of what ‘serverless’ is usually good at.”

“Modal containers are potentially long-running and compute-heavy, with big inputs and outputs. This is the opposite of what ‘serverless’ is usually good at.”

– Eric Zhang, Modal founding engineer
Zhang offered this explanation in the context of detailing Modal’s HTTP and WebSocket stack, which enables serverless functions to take web requests. Interestingly, he notes that the “Rust ecosystem was invaluable to making this custom network service, which needed to be high-performance and correct.”

When it comes to compute for AI workloads, much of it is done these days on GPUs. Modal leases GPUs from cloud providers, but it adds value by abstracting GPU management complexities — such as provisioning, scaling, and orchestration. Zhang also admits that Modal isn’t running an edge network yet:

“While our serverless functions are already running in many different clouds and data centers based on compute availability, since GPUs are scarce, our actual servers only run in Ashburn, Virginia for now.”

## Developer Fit
While Rust was used to build Modal’s HTTP and websockets infrastructure, Python is used for much of the rest of the service. CEO Erik Bernhardsson recently [noted on X](https://x.com/bernhardsson/status/1867969138628411683) that “a very large %” of Modal’s backend code base “is still in Python because it lets us iterate faster.” But, he added, “Once things settle and we need the performance, we will rewrite it in Rust.”

As for end users, Modal is [Python-only](https://modal.com/docs/guide), but the company says it “may support other languages in the future.”

In an interview [last September](https://www.youtube.com/watch?v=K_r-nX_y9aM), Bernhardsson indicated that the original target user for Modal was a “traditional machine learning engineer” who tends to use Python to write applications. However, the company wants to expand to other developers — particularly JavaScript devs.

“The very latest […] group of people coming to AI, they’re actually not necessarily Python developers,” he said. “They’re […] doing JavaScript, and they realize, like, oh, I can call OpenAI, and I can do all this […] prompt engineering. That’s not necessarily the group we’ve done super well with.”

## What Types of Applications Are Suitable?
In terms of the types of applications suitable for Modal, Bernhardsson said that it’s found a strong market fit with AI inference applications. AI inference, as defined [by Oracle](https://www.oracle.com/uk/artificial-intelligence/ai-inference/#:~:text=AI%20inference%20is%20when%20an,way%20that%20mimics%20human%20abilities.), occurs “when an AI model that has been trained to see patterns in curated data sets begins to recognize those patterns in data it has never seen before.”

Initially, Bernhardsson found the inference use case surprising but later recognized that Modal’s architecture — designed for quickly starting and shutting down containers — was well-suited for this purpose. He explained, “If you can start containers very quickly and shut them down very quickly, you can build this autoscaling inference framework.”

“The big challenge is […] scale and stability and performance.”

– Erik Bernhardsson, Modal CEO
The sweet spot seems to be that Modal does “inference at scale” really well. Bernhardsson mentioned that many of their customers do their own ML training but then rely on Modal to do the inference work.

Certainly, Modal’s capacity to deal with data intensive workloads at scale is a big part of the appeal for customers.

“The big challenge is just, like, scale and stability and performance,” explained Bernhardsson. “When you’re running thousands and thousands of GPUs at scale and handling […] 10,000 requests a second, obviously you’re building a very different product […] so that is something that we’ve had to spend a lot of time over the last few years, just scaling the core systems.”

## Another Tool for the AI Engineer Belt
It’s worth noting that Modal can be used alongside other AI development tools, such as [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/), a framework that simplifies building applications powered by LLMs. According to [LangChain’s documentation](https://python.langchain.com/docs/integrations/providers/modal/), you can deploy a web endpoint on Modal — ideal for handling heavy workloads — to serve an LLM model. LangChain then interacts with this endpoint, sending prompts and receiving LLM-generated responses for further processing.

In summary, Modal has nicely adapted the serverless model to meet the demands of modern AI development. Combining serverless abstractions with the scale needed for compute-heavy tasks helps developers do tasks like building inference pipelines, processing large datasets, and deploying LLM-based applications. AI workloads will only continue to grow in complexity, so minimizing the overhead of managing infrastructure is going to be at the forefront of AI engineers’ minds.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)