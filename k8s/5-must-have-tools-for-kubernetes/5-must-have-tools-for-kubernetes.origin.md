# From Zero to K8s Hero: 5 Must-Have Tools for Kubernetes
### Episode #35: Stay ahead of the competition by mastering these 3 tools for beginners and these 2 for more advanced users.
In this article, I'll introduce 5 must-have tools to start your journey with Kubernetes.

The first three tools in this list are absolutely indispensable for beginners. The last two make you stand out as a beginner and look like an advanced user.

I'll provide my point of view on what tools can give you an edge over your colleagues and which ones are not worth learning.

What qualifies me to give you such suggestions?

I have spent countless hours in the last few years trying all the Kubernetes tools I could get my hands on, either during my working hours or during my free time for my side projects.

I have to admit it. I am a tools nerd. I love to play with all the shiny tools, and the Kubernetes ecosystem has plenty of them.

Given that new tools pop up every day, like mushrooms, I have always thought I needed advice on which ones are worth learning and which are not worth my time.

So, I tried as many as possible, and after years of experience, I am now ready to mentor others.

In this article, I want to give the guidance I missed when I first picked up Kubernetes years ago.

So please don't waste any more time, and let's dive deep into this article.

**1. Browse your Kubernetes cluster: K9s**
My favourite Kubernetes tool is [K9s](https://k9scli.io/), a terminal-based UI that lets you interact with your Kubernetes cluster.

If you, like me, have been raised with "Bread and... Linux" " you will appreciate the beauty of using CLI tools that are both open source and highly customisable with Skins, plugins, command aliases and custom key bindings.

What are the benefits of using K9s as your primary tool for browsing your cluster:

**Support for all standard Kubernetes objects**: view and interact with pods, containers, services, RBAC, volumes, events, etc.**CRD Support**: Support interacting with Custom Resource Definitions (CRD).**Runs everywhere**: Runs on any OS and can be installed with most package managers.[Skins](https://github.com/derailed/k9s#skins): Change the look and feel but also the behaviour of the UI based on the cluster and context you are working on. Between the advanced features, you can also make a read-only context, preventing any involuntary modification in your production clusters.[Plugins](https://github.com/derailed/k9s#plugins): I personally played with this feature a while ago when I wanted to parse some JSON logs from a Kubernetes pod and display them in tabular form. I created a Kubectl plugin in Python that I called[rich-json-logs](https://github.com/gsantoro/rich-json-logs#k9s-plugin)and then plugged it into K9s. Almost straightforward.[Command aliases](https://github.com/derailed/k9s#plugins): Command aliases are less powerful than plugins but can save some keystrokes.[Custom key bindings](https://github.com/derailed/k9s#hotkey-support): With one or two keystrokes, you can either view a specific type of Kubernetes resource, call a plugin, a command alias or many other features.
What are the alternatives:

[Lens](https://k8slens.dev/): a paid alternative with a generous free personal plan. This desktop application doesn't offer more than K9s unless you have a quite expensive Pro or an Enterprise license.[OpenLens](https://github.com/MuhammedKalkan/OpenLens): an open-source version of Lens. Since Mirantis, the company behind Lens, has moved away from open-source, this project won't get any more updates.
**2. Automate everything: Kubectl**
If you have ever worked with Kubernetes, you will have already encountered [Kubectl](https://kubernetes.io/docs/reference/kubectl/), the Kubernetes command line tool.

Why did I only put it second on my list?

This tool can do anything you need with Kubernetes, but it doesn't provide such a nice user experience as K9s.

When working with Kubernetes, especially if you are a DevOps and in the middle of an incident, you must move fast!

Given that I can't remember the syntax of the Kubectl commands and that each command involves a lot of typing, K9s is a much superior tool for my needs.

Why do I still suggest Kubectl?

Whenever I need to write some automation that interacts with Kubernetes, Kubectl is my tool of choice.

The best part is that you don't have to choose between these two.

You can use K9s for the speed and UX and Kubectl for its extensibility and make them work together.

Look at the command below. Without using any other tool, I'll get the version label of all pods with the label `app=cassandra`
.

```
kubectl get pods --selector=app=cassandra -o jsonpath='{.items[*].metadata.labels.version}'
```
I took this last command from [Kubernetes quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/), a great resource if you ever want to [Prepare for your Certified Kubernetes Administrator exam](https://cloudnativeengineer.substack.com/p/prepare-for-your-cka-exam-e1c33883eaf2) since you can use it at the exam.

What are the alternatives:

K9s: we have already discussed this in the previous section.

[Kubernetes client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/): If you need to automate interacting with your Kubernetes cluster in code and you want to avoid using Kubectl in bash, you can use the Kubernetes SDK in your language of choice.
**3. Package manager: Krew**
The third tool on my list is [Krew](https://krew.sigs.k8s.io/plugins/), the official package manager of Kubectl.

I recently learned about this tool, but it is an excellent addition to my arsenal.

Like any package manager, there is not much to say about it other than it does its job well and is supported by all operating systems.

The tool's best part is the documentation with the list of [official plugins](https://krew.sigs.k8s.io/plugins/) that Krew supports.

If you go through that list, you might discover plugins you did not know existed.

**4. Aggregate logs from multiple Kubernetes resources: Stern**
Stern is the first in this list of tools geared towards more advanced users.

If you have looked at pod logs in Kubernetes, you may have encountered a use case when you wanted to combine logs from various pods or containers within a pod in the same output.

[Stern]allows you to`tail`
multiple pods on Kubernetes and multiple containers within the pod. Each result is color-coded for quicker debugging.
**5. Look under the hood: node-shell**
Node-shell allows you to start a shell to access the underlying OS of a Kubernetes node.

This tool has been invaluable when developing observability tools for Kubernetes.

As I explain in my in-depth article [Kubernetes: node-shell](https://cloudnativeengineer.substack.com/p/ep-2-kubernetes-node-shell), more than a few times, I had to look at a Kubernetes node in order to tail pods/container logs that are written directly to the node host to feed into Elasticsearch.

I couldn't have done it without node-shell.

Node-shell, like many other tools in this list, can be installed via Krew and integrated into K9s.

**Conclusion**
The list of tools in this article is definitively incomplete.

I could have mentioned:

Helm

Customise

K3d

Kind

And many more.

Most of them are a bit more advanced and deserve an article on their own.

I might cover some of them in the future.

**🎯 In case you missed**
**🗣️ Shoutout**
[FinOps Weekly](https://newsletter.finopsweekly.com/)by my friend Victor Garcia.
In his own words

Optimize your Cloud Costs! Become a Master of understanding Billing and Optimizing Workloads. Join the FinOps Weekly and get the latest FinOps news every Sunday.

Are you ready to take your skills to new heights? 🚀

🚢 Let's embark on this journey together!

👣 Follow me on [LinkedIn](https://www.linkedin.com/in/santorogiuseppe/) and [Twitter](https://twitter.com/gsantoro15) to receive valuable content on AI, Kubernetes, System Design, Elasticsearch, and much more.

🎓 If you want personalised guidance, I am here to support you. Book a mentoring session with me at [https://mentors.to/gsantoro](https://mentors.to/gsantoro) on MentorCruise, and let's work together to unlock your full potential.

♻️ Remember, sharing is caring! If this content has helped you, please re-share it with others so they can benefit from it.

🤩 Let's inspire and empower each other to reach new heights!