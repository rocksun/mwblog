The cloud is incredibly useful — but what if you’re a Python-loving data scientist?

The prevailing advice has been that if you want to run industrial-grade [Python,](https://thenewstack.io/what-is-python/) then run it on Kubernetes.

“We just think that’s dead wrong,” said [Matthew Rocklin](https://matthewrocklin.com/).

In 2020, Rocklin co-founded [Coiled.io](https://coiled.io/) to offer an even easier way to unlock the cloud’s potential. “The answer is just ‘Go use raw VMs [virtual machines]’,” Rocklin said [on the “Talk Python” podcast](https://talkpython.fm/episodes/show/519/data-science-cloud-lessons-at-scale#transcript-section). “They’re actually pretty good, if you do a few things around them.” (Like configuring the right software environments and appropriate logs.)

In 2015, Rocklin created [Dask](https://en.wikipedia.org/wiki/Dask_(software)), a Python library to spin up lots of VMs for analyzing and manipulating data. And after years contributing to Python projects for data science (like Tools, Multiple Dispatch, and SimPy), Rocklin co-founded Coiled.io to make it even easier to deploy that VM-creating software.

[![](https://cdn.thenewstack.io/media/2025/10/88920bde-talkpython-300x225.png)](https://cdn.thenewstack.io/media/2025/10/88920bde-talkpython-300x225.png)

He explained their mission last month [in a podcast episode](https://www.youtube.com/live/omBibVGLzyo?si=Nmx6q00_j4A_i5ZH) explaining “The messy truth of cloud-scale Python.” Podcast host [Michael Kennedy](https://www.linkedin.com/in/mkennedy/) agreed that much of today’s cloud infrastructure seems focused on web and API developers. Even the tutorials for data scientists aren’t emphasizing [Docker](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/) and [Linux skills](https://thenewstack.io/introduction-to-linux-operating-system/), Kennedy believes — although Rocklin sees another possible response. “Maybe we shouldn’t solve this by educating people.

“Maybe we should solve it by building better tooling.”

It’s a fresh perspective straight from the heart of the Python community. And throughout the podcast, Rocklin made the case that data scientists have their own unique set of concerns.

And that a VM-oriented solution like Coiled could be the right tool for the job.

## Why Docker and Kubernetes Aren’t Ideal for Data Scientists

Ask ChatGPT for some commands you can cut-and-paste to launch 100 virtual machines, he said, “and it’ll type at you for a couple of minutes! And it’s not the kind of typing that most data scientist people who have just used Python for a couple of years can do.

“I was actually quite shocked at how hard this relatively commonplace thing was to do.”

Rocklin acknowledges Docker is a great tool, but not necessarily for data scientists, since it’s “very much specialized to provide a really stable system that can run for decades.” Data scientists, though, want “a system that can change every five minutes. The choices that tools like Docker, Kubernetes or Terraform make are actually quite different than the choices you would make if you were building sort of middleware for this audience.

“It’s designed for cloud infrastructure engineers.” (And while middleware exists, “it’s not designed for our use cases.”)

So, “We rolled our own.”

And during the podcast, he quickly spun up a 1,000-core EC2 cluster from a notebook computer — twice.

## A Simple Demo: Spinning up a Cluster With Python Decorators

During that demo, podcast host Kennedy marvelled at how much capability was packed into simple Python statements.

vm\_type="g5.xlarge",  
keepalive="20 minutes"  
region="us-west-2",

And while they spoke, Rocklin switched off the ARM hardware just by typing one character (changing the decorator statement with the ARM flag into a comment).

# arm=True,

And then he began bringing up a new cluster.

Python’s decorators have always allowed you to extend a function’s behavior — so these statements extend the VM-defining Coiled function (that’s available after importing the Coiled library). “What we joke about internally is that our core competency is turning VMs on and off,” Rocklin said. “Once you have that technology, writing APIs around it is pretty cheap.”

Rocklin also believes that if you put a Docker push cycle into the data science work cycle, “It gums everything up. People end up not doing it.” So instead of using Docker, Coiled’s VMs copy a user’s environment.

The end result of this demo? A thousand machines that look just like the user’s original machine, “just more numerous or bigger or with GPUs, or whatever you like.”

The first 1,000-vm cluster cost $1.39, Rocklin said (adding that the second one “is costing me 45 cents so far … “). “The cloud is both way cheaper and way more expensive than I realized going in, based on whether or not you’re doing it correctly, or doing it incorrectly. There’s like several orders of magnitude difference.”

Later, Rocklin even puts a number to it. “Serverless, Lambda and similar technologies typically have like a 4X to 5X premium on cost. They also have limitations like you can’t get big machines, you can’t get GPUs, your software environments have to be of a certain size.”

## How To Avoid Unexpected Cloud Billing

Also joining them on the podcast was Coiled staff software engineer [Nat Tabris](https://www.linkedin.com/in/nat-tabris/), who sees that as another difficulty of the cloud: its lack of guardrails, especially for people who don’t know where the risks are.

Rocklin smiled, remembered being a grad student using [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)‘ free tier, who created some VMs, turned them off, “and then three months later I get a bill for $400. And it wasn’t the VMs, it was the attached storage to the VMs or some networking resource that had stuck around — that I had no concept of.”

Kennedy adds that there are “all sorts of little other services” that can surprise you with fees (including databases and database storage). “And so part of what we try to do,” Tabris said, “is put in defaults, put in controls so that you can’t accidentally spend that much money.”

Ironically, that essential compute time “tends to be a fairly predictable part of the cost.” The surprisingly large bills come from “all of these other things that you don’t even think about — like, ‘If I flip this setting, now I’m hitting this S3 API a lot, and it turns out you pay per API call.'”

Tabris remembers a customer using a 1,000-node cluster who’d set up debug-level logging, which created “very chatty logs … I think it was like a $15,000 bill.” (Although that story “had a happy ending, because we talked to AWS and they ended up eating that cost for the customer.”) Rocklin points out that’s another good lesson for handling these sudden surprise bills: If you talk to AWS, they can give you money back.

And Coiled now has a warning if it sees chatty logs.

So when Kennedy asks what the workflow is to make sure his 2,000 machines didn’t run all day or unnecessarily, Rocklin points out Coil watches for that automatically — and shuts down machines if they aren’t being used.

## The Freedom To Experiment

But something happens when VMs are easy to create, said Rocklin: It gives users “a lot of ability for the user to start experimenting with hardware.” (One user ran through every region in their cloud trying to find A100 GPU instances.) “We often see people playing with ARM versus Intel versus AMD, playing with every GPU type.”

And you can also experiment with regions. For example, if your data set is stored in one region, Tabris said, “it makes an orders-of-magnitude difference how quickly you can download it if you are close to it, than if you are far from it.”

Tabris came from the web development world, but realized that for data scientists, “it actually makes sense to try out different instance types to explore. ‘What’s this GPU do for me?'” Different CPUs can also make a difference — even small changes like going from the ARMv8 to ARMv7. “Some of that actually really does make a difference for data science workloads, because it has to do with those wide instructions.”

Some CPUS have better memory — DDR5 instead of DDR4. “Does that make a difference for my workload? Is it going to save money?” It may be hard to know in advance, but “It’s really easy to just try.”

Rocklin later calls it “the joy of this … It’s that variety that’s actually really a core part of the cloud,” calling it something Coiled cares a great deal about.

## The Philosophy of Making Cloud Computing Playful

Podcast host Kennedy appreciated the extra ease, since variety and experimentation are ultimately a key part of the data science ethos. “We’re going to experiment, we’re going to explore, we’re going to play.”

And Rocklin agreed. “I think a lot of why Python became popular is that it feels like play, often. We’re given these libraries that are both easy to use and powerful. And that feels like play.”

In contrast, working with the Boto library in AWS or writing YAML in Kubernetes “does not feel like play … But here today we got to play with making 2,000 VMs — half ARM, half Intel. Half on the U.S. east coast, half on the U.S. west coast … And now suddenly the cloud is like play.

“And you just do different things when things become playful. You behave differently. Folks have fun. And the cloud is a really fun tool to use. Once you get past all the pain.”

When asked for final thoughts, Rocklin said the cloud’s great promise, for a delightful and powerful data tool — isn’t always delivered well. He urges data scientists not to settle.

Kennedy acknowledged, “It’s gotten really complex — but it doesn’t have to be.” And Tabris added that “This message of ‘Things are supposed to be delightful’ is important to us.”

Rocklin agrees that the cloud “can be a delightful experience … We should all be playing. If you don’t want to use Coiled, that’s fine. But there’s other ways to do things. Go play.”

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)