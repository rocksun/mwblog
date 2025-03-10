# Lambda HyperScaler Focuses on the AI Developer
![Featued image for: Lambda HyperScaler Focuses on the AI Developer](https://cdn.thenewstack.io/media/2025/03/36e838c5-aicloudfordevelopers-1024x543.jpg)
There’s a little secret that [Lambda](https://lambdalabs.com/), an artificial intelligence (AI) hyperscaler, knows: Not all AI developers are software developers, suggested [Robert Brooks IV](https://www.linkedin.com/in/boborado/), a Lambda founding team member and the vice president of revenue.

“These folks are not necessarily software engineers. They’re experts in math; that is what their skill set is,” Brooks told The New Stack. “If you allow those people to not have to focus on the DevOps side of running a cloud and just focus on the math, a.k.a. building the machine learning model, that’s why we’ve gotten to build a big brand in the space.”

## Lambda Focuses on AI Developers
Lambda, named after Alonzo Church’s Lambda Calculus, historically focused on [machine learning engineers](https://thenewstack.io/5-new-kubeflow-1-3-features-that-machine-learning-engineers-will-love/) — and predominantly on the training and fine tuning side of the AI market. That meant developers were either building something from scratch or taking an open source model and fine-tuning it to their own needs.

Now, it’s marketing itself as a hyperscaler for all AI developers, from the hardcore deep learning researcher to the web developer plugging a machine learning API into an application’s [frontend](https://thenewstack.io/introduction-to-frontend-development).

“Really, within the last two years, we’ve seen inference explode on our platform because the greatest thing about an NVIDIA chip is it has that dual purpose of being good for training and inference,” Brooks said. “We’ve seen an explosion in terms of our user growth related to the software engineer [who’s] using AI within their code.”

In AI, inference is the process where a [trained machine learning model](https://thenewstack.io/machine-learning-for-real-time-data-analysis-training-models-in-production/) uses its knowledge to make predictions or decisions on new, unseen data. It’s what essentially creates the output of AI.

## Why a Cloud for AI Developers?
There’s a remarkably simple reason why Lambda decided to focus on a hyper cloud for AI developers: They were [machine learning engineers who wanted to build](https://thenewstack.io/the-machine-learning-building-blocks-developers-require-to-do-mlops/) an infrastructure to support their own apps.

The platform sits on 25,000 [GPUs](https://thenewstack.io/revolutionizing-storage-the-role-of-gpus-in-modern-infrastructure/), making it “one of the few companies in the world that have the ability to use our infrastructure to actually serve these applications correctly,” Brooks said.

“Few companies have as many [NVIDIA](https://thenewstack.io/a-developers-guide-to-nim-nvidias-ai-application-platform/) GPUs as we do. That’s why we’re on this particular path,” he added. “The reason we deploy infrastructure is [that] we ultimately want to be able to use it, because we’re actually machine learning engineers.”

“Because we have all that infrastructure, we allow folks to grow with us and not be limited artificially — no pun intended on that word.”

— Robert Brooks IV, Lambda founding team member and the vice president of revenue
Their founder, [Stephen Balaban](https://www.linkedin.com/in/sbalaban/), is a machine learning engineer who was at a computer vision contest when AI started to be able to identify a dog from a cat. He built a computer vision app that ran locally on the iPhone called DreamScope, which used a crude, bespoke [neural network](https://thenewstack.io/who-needs-neural-networks-the-generative-prowess-of-state-transition-models/) to do what generative AI does today, Brooks said.

“Ultimately, by building these applications, we’ve been relying on more and more NVIDIA GPUs to build and then productionize AI,” he said. “So we had this problem in 2015, 2016, and around 2017 we fully pivoted into building this infrastructure for other AI teams, as we were very familiar with that problem.”

To the best of their knowledge, Lambda posts one of the lowest cost inference APIs in the world, Brooks claimed. The company made that decision on purpose.

“We’re vertically integrated so there’s a lot of people that we compete with that are just built on top of other people’s GPU clouds, but because we actually own the infrastructure, we can control the cost better,” he said. “We own the data centers. We own the GPUs. We own everything. We write all the software. We actually market ourselves as the cheapest inference API out there. It is not rate limited.”

Companies often allow developers to use up to X amount of million of tokens per hour, day or month, but then the developer has to talk to a salesperson, he said.

“Because we have all that infrastructure, we allow folks to grow with us and not be limited artificially — no pun intended on that word,” Brooks added.

Many worry about the shelf life of GPUs because Nvidia is starting to launch new ones every two years, while historically that cadence has been every three to four years, Brooks said. Lambda doesn’t worry about that because it deploys GPUs for customers today, and once the contract ends, Lambda uses the GPUs for their own AI training and services.

“There’s this really nice feedback loop, because we’re machine learning engineers running a cloud where it’s allowing us to grow faster and produce more AI research and more machine learning software as time goes on,” he said.

## Tools for AI Developers
One way the startup helps machine learning engineers and AI developers is that it has a plug-and-play approach to on-boarding.

“When a machine learning engineer or AI developer goes on to our cloud and spins up a GPU, all of their tools, frameworks, libraries that they need to rely on — essentially, their app store — is already pre-built and in there for them, so they can actually focus on their work,” Brooks said.

Lambda launched its [Inference API](https://docs.lambdalabs.com/public-cloud/lambda-inference-api/), which became generally available in December. It allows developers to use AI language models in their applications without the overhead of managing the complex infrastructure.

“We now have dedicated services towards helping customers actually serve models within their apps. It’s been a nice, gradual uptick towards much more production-focused AI, or what we call inference,” Brooks said.

It also introduced [Lambda Chat](https://lambda.chat/), which provides access to various [large language models](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/), many of which are open source. Lambda Chat is their first foray into [serving consumers with open source models](https://thenewstack.io/google-serves-up-cloud-gpus-with-a-side-of-open-source-llms/), Brooks said. It’s free for consumers, although Lambda does charge developers for the API calls.

Last month, the [company raised $480M in series D funding](https://lambdalabs.com/blog/lambda-raises-480m-to-expand-ai-cloud-platform?) to expand its AI cloud platform. The plan is to use that money to build more software tools for AI developers and deploy more GPUs to meet customer demand.

The company also said it will continue to develop Lambda Chat, which hosts [DeepSeek-R1](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) and other open source models.

## DeepSeek Enters the Chat
TNS asked Brooks how DeepSeek R1 has changed things in AI for hyperscalers. DeepSeek R1 is a large 671 billion parameter Mixture of Experts (MoE) model, meaning its designed to handle complex tasks by strategically activating different “expert” sub-networks within the larger model. It made headlines for being able to do AI with fewer GPUs.

The introduction of DeepSeek to the market led to a boost in demand, Brooks added.

“We’ve experienced sort of extreme demand from that, related to not only machine learning and engineers spinning up instances on our cloud, but also folks using our inference API to plug into their application,” he said. “So it was a democratizing effect in terms of starting to spread more of that functionality across more apps.”

But ultimately, Deep Seek itself doesn’t have enough GPUs to run the production, he said. That’s why there’s a limit to how many questions you can ask.

He said Lambda serves many larger enterprises with these private cloud buildouts of 4,000 to 8,000 GPU clusters. Enterprises are interested in running DeepSeek but with more GPUs.

## Competitors
Other companies that are offering GPUs as a service include:

[Nebius](https://nebius.com/), which offers a machine learning managed service;[Beam](https://www.beam.cloud/), which boasts an AI infrastructure for developers;[Cerebrium](https://www.cerebrium.ai/), which sells serverless for machine learning engineers;[SaturnCloud](https://saturncloud.io/), which targets[data scientists](https://roadmap.sh/ai-data-scientist); and[Modal](https://thenewstack.io/serverless-for-ai-devs-modals-python-and-rust-based-platform/).
*Editor’s Note: Updated March 7, 2025 at 1:17 p.m. EST to reflect the name of the company is now Lambda.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)