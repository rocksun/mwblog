# 2 Ways AI Assistants Are Changing Kubernetes Troubleshooting
![Featued image for: 2 Ways AI Assistants Are Changing Kubernetes Troubleshooting](https://cdn.thenewstack.io/media/2024/04/d428b6a6-ai-changing-kubernetes-troubleshooting-1024x576.jpg)
Of all the hoopla around AI, the most misguided part is the insistence on fine-tuned large language models (LLMs). Too many believe specializing a model based on a massive collection of domain-specific data is the only way to build useful AI assistants.
This demand for fine-tuning is even more common in highly specialized or technical fields, such as software development and cloud services. A prime example is the ongoing maintenance and troubleshooting of Kubernetes clusters designed to deliver apps. This situation underscores the critical challenge faced by DevOps and app development leaders: There needs to be a better solution for managing the complexity of
[cloud native infrastructure](https://thenewstack.io/the-cloud-native-community-needs-to-talk-about-testing/). These environments often present intractable challenges that defy experience, wisdom or [intuition around troubleshooting](https://thenewstack.io/why-intuitive-troubleshooting-has-stopped-working-for-you/).
In response, startups and open source projects claim to have fine-tuned existing models to include specialized knowledge about Kubernetes that generic models, even GPT-4 Turbo, wouldn’t normally ingest or have access to.
However, the challenge is not a problem with the fine-tuning itself, but its inability to mimic the human approach to troubleshooting. No matter how intelligent the model, you’ll get no real value unless it can replicate how you perform troubleshooting: gathering disparate resources, jugging all the critical details you’ve found in logs and
kubectl output in your head, leaning on your experience, and distilling it all into a logical next step.
There are only two key areas that make an AI assistant useful in the
[Kubernetes world](https://thenewstack.io/the-quest-for-high-quality-kubernetes-deployments/). Assistants must be:
- Embedded within Kubernetes clusters with access to artifacts that describe its state, like the output of
kubectl get/logs/describe.
- Able to understand your questions in natural language and translate complex operational data into simple, actionable next steps.
Fine-tuning just prioritizes hype over what matters to you most: acting on what’s actually happening with your pods, nodes and apps.
## Getting Kubernetes AI Assistance Halfway Right
The AI and cloud native spaces are growing simultaneously, so new tools are overlapping in these two domains.
New open source command-line interface (CLI) tools like
[K8sgpt](https://github.com/k8sgpt-ai/k8sgpt) and [KoPylot](https://github.com/avsthiago/kopylot) wrap their operations around
kubectl to gain access to your cluster’s state. By running that command on your behalf using the context available in your
.kube/config file, these tools can read and process the output directly, rather than forcing you to switch context. They then proxy data to OpenAI’s API to deliver AI-generated responses in your terminal.
It’s a clever workaround, but these CLI tools still require a high level of Kubernetes knowledge, or another CLI tool. You need to know the right commands, not just a question about your cluster’s status, to initiate interaction.
Another open source tool,
[mico](https://github.com/tahtaciburak/mico), advances this concept by converting your natural language queries into
kubectl commands. You can ask mico to, for example, print the number of times each pod in
xyz namespace has restarted, and it will use the
jsonpath argument in
kubectl to filter output down to just the relevant line.
We love to see how the open source community is leveraging AI, but these tools are limited: They either understand the cluster’s state but can’t handle natural language queries, or they help you write queries but only return
kubectl output without the next troubleshooting steps. You could replace the default OpenAI models powering these tools with a specialized alternative, but that won’t help you reduce your troubleshooting time or help your less-experienced peers monitor their apps.
## What Makes AI Assistance Valuable for Kubernetes Troubleshooting?
The answer is an AI assistant that excels in understanding cluster state and interpreting natural language — fine-tuning be damned.
### Access to Your Cluster’s State
Without access to the cluster state, the only way to get help from your AI assistant is to play a game of telephone on your path to resolving issues. Even with a fine-tuned AI, you can expect the conversation to go a little like this:
- You know enough about Kubernetes to run
kubectl get podswhen your
[deployment](https://thenewstack.io/the-quest-for-high-quality-kubernetes-deployments/)doesn’t come up immediately.
- You ask your AI assistant why a pod would crash due to a
CrashLoopBackOfferror.
- The AI responds by telling you that the most common possible causes of a
CrashLoopBackOfferror include insufficient memory, missing dependencies and container failure due to port conflict. Perhaps it’s smart enough to ask you to run
kubectl describe pod POD_NAMEfor clues about its resource usage and limits … perhaps.
- You tell your AI assistant about that output, including the
Terminatedstate and last emitted event:
Back-off restarting failed container.
- The AI suggests you run
kubectl get events --field-selector involvedObject.name=POD_NAMEto search for other possible causes.
- You find events around failed readiness and liveliness probes, along with the backoff process, but nothing new, and you let your AI assistant know.
- The AI assistant suggests you run
kubectl logs POD_NAME --all-containersto search for specific errors with your containerized app or its dependencies from your manifest, like a database or messaging queue.
- Amidst the lengthy logs, you find a warning from
docker-entrypoint.shsaying it couldn’t execute because of a
not foundargument.
- You ask your AI assistant about that warning, and it (finally) tells you to check your Kubernetes manifest for a typo or misconfiguration in the arguments you’ve attached to that container, which is the root cause of your issue.
You certainly received assistance from your AI tool, but the assistance was not particularly efficient. It might have saved you from Googling each error or running
kubectl ... help commands to find the right syntax. But because you were responsible for accurately sharing information about your cluster’s state and understanding each step from your AI assistant, you still carried almost all the cognitive load and did not save very much time.
Access to a cluster’s state is essential. A valuable AI assistant must automatically respond to your original question about
CrashLoopBackOff by running
kubectl commands itself, parsing the output for clues, bringing in context from the
[collective Kubernetes troubleshooting knowledge](https://thenewstack.io/can-chatgpt-save-collective-kubernetes-troubleshooting/) available online and delivering a precise path to remediation — no runbooks or deep dives into documentation required.
### Understanding Your Natural Language Questions
A Kubernetes AI assistant that can read outputs or logs and deliver an executive summary of what to think about next is great, but it assumes you have enough Kubernetes knowledge to know what question or specific
kubectl command to run. The real added value, especially for application developers with limited knowledge of Kubernetes operations, comes from the ability to ask questions in your natural language:
- Some folks might need to ask beginner-level prompts: “What is a pod?”
- Others can ask specific questions about the cluster based on a basic understanding of Kubernetes: “Are there any failing pods in my
xyznamespace?”
- The most advanced DevOps engineers might take it one step further: “What should I do about this notification, which says one of my nodes is suddenly
NotReady?”
When the AI can translate a question into the relevant command to gather state context (
kubectl get pods -n xyz), it can effectively reduce the cognitive load on your team. DevOps engineers can reduce their mean time to resolution (MTTR) by using the AI assistant as a resource to reflect their specialized knowledge, and developers can troubleshoot their apps in a self-service fashion.
When the AI assistant runs on platforms where your team operates, like Slack or
[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Teams, this knowledge is more accessible and collaborative. When the next significant incident strikes your app, DevOps engineers and developers can engage your AI assistant in the same channel for more targeted root cause analysis and a remediation plan that goes beyond a temporary fix.
## A New Type of Kubernetes AI Assistant
To address these issues, Botkube recently launched
[AI Assistant](https://botkube.io/blog/real-time-platform-engineer-advice-ai-assistant), which is designed to operate in both areas of Kubernetes troubleshooting and directly in collaboration platforms.
The assistant works by listening to your natural language questions about your Kubernetes cluster and its apps, converting your queries into the appropriate
kubectl get/logs/describe commands and interfacing with an LLM to explore root causes and opportunities. From this, the assistant can deliver insights and recommend next steps on your troubleshooting journey.
![](https://cdn.thenewstack.io/media/2024/04/9b8d0ee9-updateyaml.gif)
This assistant enhances Botkube’s notification, investigation and troubleshooting tools by operating on the most valuable bounds of both areas. Using AI Assistant helps you research why an issue is happening, learn
kubectl to perform basic operations, or tap into Kubernetes expertise to seek out root causes and find a workable solution.
## Cluster State && Natural Language >>> Fine-Tuned LLM
Under the hood, Botkube’s AI Assistant uses ChatGPT-4.
We’re not ashamed to admit that we’re using the same model as every open source tool and most new paid platforms. We can’t fine-tune what ChatGPT knows, but we can add nuance to queries and tweak the nature of its responses to provide a better troubleshooting experience.
For example, we layer additional instructions on top of common natural language queries and data about a cluster’s state to “force” ChatGPT to provide more comprehensive answers. We also enrich ChatGPT’s default output with better formatting and organizational structure to help you focus on troubleshooting, not deciphering instructions.
Adding value just before and after interfacing with an LLM can do much more than fine-tuning. We designed AI Assistant to be context-aware and compatible with the questions you genuinely want to ask of your cluster — not the complex
kubectl commands you may be used to.
## Ways to Use an AI Assistant
The opportunities are generally bounded only by how much detail
kubectl emits and the Kubernetes knowledge built into OpenAI’s latest models … which is quite a lot. You can ask:
- Basic questions about the Kubernetes ecosystem, such as details on the differences among containers, pods and nodes.
- Specific questions related to a cluster’s state, like confirming that all pods in the
xyznamespace are healthy.
- For specific troubleshooting help around a new error notification, without having to reference a runbook or read documentation.
Botkube’s
[executor](https://docs.botkube.io/usage/executor/) features then let you turn the AI Assistant’s insights into immediate remediation by helping you craft the right
kubectl through a drop-down interface (rather than a dozen runs of
kubectl ... help).
DevOps engineers can speed up workflows by spending less time in the terminal and more time where collaboration happens. And app developers can fix Kubernetes issues on their own instead of filling out a ticket and waiting for someone to help.
No matter your title or role, you can start using Botkube’s embedded AI assistant today with a new or existing Botkube account.
[Sign up now for free](https://app.botkube.io/) to enable our Kubernetes AI assistant with a single click, with no configuration required.
Toss it a few questions and you’ll quickly see why cluster awareness and natural language — not fine-tuned LLMs — are the best path forward to manage the complexity of your cloud native infrastructure.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)