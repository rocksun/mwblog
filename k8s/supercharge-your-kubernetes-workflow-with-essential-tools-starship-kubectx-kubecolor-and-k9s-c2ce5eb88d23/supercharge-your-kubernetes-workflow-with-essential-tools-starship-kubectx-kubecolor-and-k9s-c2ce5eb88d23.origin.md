# Supercharge Your Kubernetes Workflow with Essential Tools: Starship, Kubectx, Kubecolor, and K9s
If you’re working with Kubernetes, you will fast learn how important it is to stay organized to avoid mistakes.
I’ve found that combining
**Starship**, **Kubectx/Kubens**, **Kubecolor**, and **K9s** gives you a clean, responsive prompt that helps you to stay focused while still having a minimal set of plugins that are easily maintained. Let’s go trough them one by one.
# 1. Starship: Speed and Simplicity
[Starship](https://starship.rs/) is a fast, minimal and agnostic shell prompt that you can customize to show key info, like which Kubernetes cluster and namespace you’re in.
No more waiting around for your prompt to load — just speed and efficiency.
- Always know your context like clusters and namespaces
- Color differentiate between Production and Testing to reduce mistakes
- Integrates well with Git
Put this in your
starship.toml config
[kubernetes]
disabled = false
symbol = "⎈"
format = '[$symbol](bright-black) [$context( \($namespace\))]($style)'
[[kubernetes.contexts]]
context_pattern = "^production$"
context_alias = "production"
style = "green"
# 2. Kubectx/Kubens: Switch Clusters & Namespaces Instantly
[Kubectx](https://github.com/ahmetb/kubectx) and [Kubens](https://github.com/ahmetb/kubens) let you switch between clusters and namespaces with one simple command.
# Use this
kubectx <cluster>
kubens <namespace>
# Instead of this
kubectl config use-context <cluster>
kubectl config set-context --current --namespace=<namespace>
And you’ll never have to guess what context you’re in because Starship will display it right in the prompt!
- Save yourself a lot of time
- Less use of
namespacecommands.
# 3. Kubecolor: Color-Coded Kubectl Output
[Kubecolor](https://github.com/kubecolor/kubecolor) makes
kubectl output easy to read by adding color highlights.
Turn messy text into clear, readable info when you’re troubleshooting or managing clusters, is a game-changer.
- Faster overview of errors and deployments
- Less strain on your eyes
- Color coded
kubectl logs
## 4. K9s: Visualize and Manage Kubernetes Resources
[K9s](https://github.com/derailed/k9s) gives you an interactive, terminal-based UI for managing your Kubernetes clusters.
It’s great for quickly viewing logs, monitoring pods, and understanding what is happening across your environments especially during new deployments.
# 5. Bonus: Kubectl edit with VS Code
Add
export KUBE_EDITOR='code --wait' to your
.bashrc to add VS Code as default kubectl editor. Makes it easier to debug your YAML files with the number of extensions available.
- Integrates with
kubectl edit
- Integrates with edit in K9s
# The Road to Perfect Workflow
Together, these tools will create smooth and informative experience. Starship shows you where you are, Kubectx/Kubens help you jump between clusters, Kubecolor makes sense of your outputs, and K9s gives you a full visual overview whil editing in Visual Studo Code helpt you avoid indenting errors. Try them, and you’ll never want to go back!
# Am I missing something?
Leave a comment and let me know if there are other tools that you use!