[Logs](https://thenewstack.io/observability-2-0-or-just-logs-all-over-again/) are essentially a language, and if you throw the right information into a [large language model (LLM)](https://thenewstack.io/introduction-to-llms/), it can help explain what happened. There is a hook in [Gonzo](https://www.linkedin.com/pulse/introducing-gonzo-better-way-analyze-logs-your-jonathan-m-reeve-phd-r0i2c/) where users can throw a log into their favorite LLM via backend APIs. This helps bubble up patterns such as repeated critical metrics and assists in pattern analysis and heat charts to separate the signal from the noise. As more code is created by AI, the complexity of logs is not getting simpler, necessitating a step back to look at the fundamentals of how data is analyzed.

“Logs are language, so if you throw the right information into an LLM, it can actually help explain what happened with the log … it looks across all your logs and bubbles that up and looks at a lot of pattern analysis,” [Bob Quillin](https://www.linkedin.com/in/bob-quillin-46802511/), co-founder and CEO of [observability](https://thenewstack.io/introduction-to-observability/) startup [ControlTheory](https://www.controltheory.com/), told me.

Let’s see how you can install Gonzo on a laptop to see how easy (or not) it is to get started on generating logs that are useful from apps running on your laptop or across a wide-scale multicloud environment. After working with Gonzo, I found it’s necessary not to mistake its simplicity for its design to scale for large operations. Similar to how Stripe got started supporting smaller customers, Gonzo is designed to allow organizations to scale at will their [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "monitoring and observability") reach.

I recommend Brew to get started for a quicker install instead of pulling everything from GitHub directly in the console.

If you have [Homebrew](https://thenewstack.io/install-homebrew-on-macos-for-more-dev-tool-options/) already installed, updates will be installed automatically as Gonzo is installed. This command downloads and installs Homebrew:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Download the latest release for your platform from the releases page.

Using [Nix](https://thenewstack.io/flox-gears-up-nix-for-the-enterprise/) package manager (beta support):

```
nix run github:control-theory/gonzo
```

Build Gonzo from the source:

```
git clone https://github.com/control-theory/gonzo.git cd gonzo make build
```

Create a mock app that generates logs. I recommend this one, activated by cutting and pasting these commands into your terminal:

`while true; do  
echo "$(date) INFO Starting request" >> application.log  
echo "$(date) ERROR Something failed" >> error.log  
echo "$(date) DEBUG Debug details here" >> debug.log  
sleep 2  
done`

Check that your fake app is generating logs with this command in a second terminal window:

`tail -n 5 application.log`

You should see something like this (which means your app is generating logs):

[![](https://cdn.thenewstack.io/media/2026/02/a6c6ca01-screenshot-2026-01-14-at-4.22.29-pm.png)](https://cdn.thenewstack.io/media/2026/02/a6c6ca01-screenshot-2026-01-14-at-4.22.29-pm.png)

Let’s now let Gonzo do its magic as it lists and analyzes your logs by opening a third terminal window and running:

`gonzo -f application.log -f error.log -f debug.log`

You should see something like this:

[![](https://cdn.thenewstack.io/media/2026/02/8f86cace-screenshot-2026-01-14-at-4.24.32-pm-1024x643.png)](https://cdn.thenewstack.io/media/2026/02/8f86cace-screenshot-2026-01-14-at-4.24.32-pm-1024x643.png)

Let’s now scale Gonzo to the next big thing it can do. While not full-blown Kubernetes, we start with Minikube, which is a local node Kubernetes cluster you can run on your laptop inside a virtual machine (VM) or container that you can download [here](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download):

`minikube start`

Once up and running (potential problems in my build notwithstanding), you should get something like this:

[![](https://cdn.thenewstack.io/media/2026/02/75eeb1eb-screenshot-2026-01-14-at-9.08.54-pm-1024x349.png)](https://cdn.thenewstack.io/media/2026/02/75eeb1eb-screenshot-2026-01-14-at-9.08.54-pm-1024x349.png)

Run a simple nginx app:

`kubectl create deployment nginx --image=nginx`

Stream those logs to Gonzo:

`kubectl logs -f deployment/nginx | gonzo`

The Gonzo interface pops up, and the logs start coming in:

[![](https://cdn.thenewstack.io/media/2026/02/645873c4-screenshot-2026-01-14-at-9.01.57-pm-scaled.png)](https://cdn.thenewstack.io/media/2026/02/645873c4-screenshot-2026-01-14-at-9.01.57-pm-scaled.png)

Let’s click on an error log and see what it reveals:

[![](https://cdn.thenewstack.io/media/2026/02/a5cf48a3-screenshot-2026-01-14-at-9.23.23-pm-1024x386.png)](https://cdn.thenewstack.io/media/2026/02/a5cf48a3-screenshot-2026-01-14-at-9.23.23-pm-1024x386.png)

It looks like the API for the AI link has not been configured yet. We’ll have to look at this in a coming post and see what AI observability-specific capabilities are in store with Gonzo and how they work.

## Closing Thoughts

Gonzo is a new project, and in many ways it reminds me of [Jaeger](https://www.jaegertracing.io/). Not the early days of Jaeger, but Jaeger as it is now. A lot of engineering work has already gone into Gonzo’s development, and like Jaeger for traces, it is clean, fast and simple. And as you see above, you can almost immediately begin to observe a Kubernetes cluster with a few bugs (although in this case, it was a Minikube and not a full-blown working Kubernetes deployment).

Both Jaeger and Gonzo are geared for cloud native deployments, and as such, I would expect Gonzo to replicate Jaeger’s success. It just works. Again, this is just a simple look in this tutorial, a rudimentary look at what Gonzo can do, and I believe the creators when they say that it can scale across multiclouds, multideployments and different applications. And it’s not choosy about the different streams, as it doesn’t matter whether the data and log texts are coming from files or applications from different sources into its terminal.

Of course, AI will play a big component in its development, both for observability of AI applications, and it’ll be interesting also to see how it’s integrated in support of using it for drawing observability analysis.

Interesting days ahead for observability and open source.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)