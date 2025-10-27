During this week’s [PyTorch Conference 2025](https://events.linuxfoundation.org/pytorch-conference/?__hstc=132719121.c7e7a3a3b1b149ab85ef60029fb25108.1761329988449.1761329988449.1761329988449.1&__hssc=132719121.3.1761329988449&__hsfp=3360764624&ajs_aid=913fde38-5396-42fb-9661-2bbde650c913) in San Francisco, I sat down with [Luca Antiga](https://www.linkedin.com/in/lantiga/), the head of the Technical Advisory Council for the [PyTorch Foundation](https://pytorch.org/) and the CTO of end-to-end AI platform Lightning AI. Antiga was part of the team that wrote the original [PyTorch paper](https://papers.nips.cc/paper_files/paper/2019/hash/bdbca288fee7f92f2bfa9f7012727740-Abstract.html) and co-authored the [“Deep Learning with PyTorch”](https://www.manning.com/books/deep-learning-with-pytorch) book. Who better to talk to about the state of PyTorch itself and get an update on the PyTorch Foundation?

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Antiga, whose academic background is actually in biomedical engineering, noted that one of the reasons why PyTorch [became so popular](https://thenewstack.io/why-pytorch-gets-all-the-love/) is that it is very friendly to researchers. Those researchers eventually graduated or went to work in the tech industry and brought PyTorch with them.

“It’s very ‘pythonic,'” Antiga explained. “Whereas back in the day, there were many frameworks that were in Python, but you needed to code in a kind of meta language that gets between the problem in yourself, and it makes debugging a lot harder, and so on. Pytorch was kind of revolutionary in that sense in that it brought the ease and iteration speed of Python, and, you know, the bias toward action that Python has into the world of like neural networks and back propagation and GPU computing.”

When PyTorch was created, the industry still focused on neural networks — often for image or sentiment analysis. Then ChatGPT brought generative AI (GenAI) to a wider audience, but Antiga argues that PyTorch always remained relevant.

“Throughout all these revolutions that came, you always see PyTorch there,” he said. “And there are, of course, others like JAX and so on — they’re very strong. But comparatively, PyTorch is a whole industry and empowers the whole industry. And together with that came a great ecosystem.”

And while PyTorch is most often associated with training models, it has also become central to running models in production now.

“If you go and see the inference frameworks that are most popular — vLLM, SGLang — and they run PyTorch, right? And they run PyTorch in production,” Antiga noted. “If you interact with any chatbot today, chances are that you’re running PyTorch at that time.”

Another reason PyTorch has been gaining in popularity recently is that reinforcement learning — which rewards models for the right action and provides negative feedback when they take the wrong turn — is now routinely being used to [fine-tune pre-trained large language models](https://huggingface.co/learn/llm-course/en/chapter12/2) (LLMs). As it turns out, PyTorch is well-suited for this kind of use case, too.

“Reinforcement learning will encourage a model to do more of the things that work when confronted with an environment where you can go in with an action, the environment state changes, and you get a reward for your actions,” Antiga explained.

## The State of the PyTorch Foundation

As for the PyTorch Foundation itself, it’s worth noting that it was only a few months ago that the foundation [started bringing in additional projects](https://pytorch.org/blog/pt-foundation-expands/), starting with vLLM and DeepSpeed. With Ray, the popular open source distributed computing framework for scaling AI and Python applications, the foundation has now [added its fourth project](https://thenewstack.io/ray-comes-to-the-pytorch-foundation/).

But the plan isn’t to become a large umbrella foundation, Antiga stressed.

“What I’m mostly concerned about in the ecosystem is the users. What journey do the users experience when they approach an ecosystem that is kind of sanctioned by the PyTorch Foundation,” he explained. “My goal is to have them succeed.”

For more of our conversation, subscribe to our podcast or watch the full interview on YouTube.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)