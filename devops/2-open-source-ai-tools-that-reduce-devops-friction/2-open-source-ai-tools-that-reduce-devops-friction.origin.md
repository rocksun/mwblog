# 2 Open Source AI Tools That Reduce DevOps Friction
![Featued image for: 2 Open Source AI Tools That Reduce DevOps Friction](https://cdn.thenewstack.io/media/2024/09/d3665d01-open-source-ai-tools-devops.png)
AI is playing a transformative role across industries. While some fear that AI might lead to a [dystopian takeover, like Skynet](https://www.firefly.ai/blog/chatgpt-can-code-iac-for-devops), I believe there’s still plenty of room for innovation and efficiency gains before we reach that point. That is why we are investing heavily in building AI-driven cloud solutions to help teams gain better control over the cloud (and AI itself).

I’ll share some real, practical examples of how you can channel AI for greater [DevOps](https://thenewstack.io/devops/) efficiencies through two open source tools: AI as Code ([AIaC](https://aiac.dev/)) and the [Kubernetes](https://thenewstack.io/kubernetes/)-focused [K8sGPT](https://k8sgpt.ai/).

## The AI Landscape in DevOps
With AI, the first things that come to mind might be image generation or content creation using tools like Stable Diffusion, DALL-E 2 and Midjourney, which have made it possible to turn text prompts into stunning visuals. But AI’s potential extends far beyond these creative applications into the technical realm, particularly in DevOps.

Imagine if the tools you use every day in DevOps — like Kubernetes (K8s), Open Policy Agent (OPA) or Argo CD — could be transformed into human-like assistants. We are exploring this kind of innovation, using AI to create human-like representations of these tools.

Beyond the novelty of generating images or videos, AI’s true power lies in its ability to parse large amounts of text-based data. It can translate that understanding to generate code (which is essentially text), then apply that knowledge to diagnosing issues and even automating infrastructure management.

We decided to test these new frontiers and see how generative AI (GenAI) stacks up in these domains, which have required many human hours of toil. We wanted to see how close to human results GenAI could get for typical, common DevOps use cases.

## Automating Code Generation with AIaC
Code generation is one of the most significant ways AI is making an impact in DevOps. A great example is GitHub Copilot, which went from novel to widely adopted even faster than GitHub could have predicted. This is also why competitors like [AWS](https://aws.amazon.com/?utm_content=inline+mention) are investing significant R&D hours producing and leveling up competing tools like [Amazon Q](https://aws.amazon.com/q/).

DevOps has been built upon taking everything infrastructure and transitioning it to code, aka [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code/). This includes deployment pipelines, monitoring, repositories — anything that is built upon configurations can be represented in code. This is where AI tools like ChatGPT and AIaC come into play.

AIaC, an open source command-line interface (CLI) tool, enables developers to generate IaC templates, shell scripts and more, directly from the terminal using natural language prompts. This eliminates the need to manually write and review code, making the process faster and less error-prone.

For example, when [creating a Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) for a Node.js application with security best practices in mind, simply describing the requirements in natural language allows AIaC to generate a secure Dockerfile:

1 |
```aiac dockerfile for nodejs with comments``` |
This approach extends to generating Kubernetes manifests, Helm charts and even policy configurations in Rego for OPA. With the growing number of config languages and domain-expertise DevOps teams are required to know, this can significantly reduce the learning curve and barrier to entry. The ability to reprompt and refine your output helps you get the precise configuration needed, tailored to a specific environment.
Because it isn’t always efficient to work directly with a GPT model via a browser, especially in a production environment, we developed AIaC as a CLI. We believe this makes it straightforward to integrate AI-driven code generation into existing workflows.

## Diagnosing and Resolving Kubernetes Issues with K8sGPT
While generating code is a powerful AI use, diagnosing and resolving issues in complex systems like Kubernetes can be even more valuable. This is where K8sGPT, a fairly recent [entry](https://github.com/cncf/sandbox/issues/38#issuecomment-1862551641) in the Cloud Native Computing Foundation ([CNCF](https://cncf.io/?utm_content=inline+mention)) sandbox, comes in. Developed by [Alex Jones](https://github.com/AlexsJones), a longstanding contributor and advocate in the CNCF community, K8sGPT is an open source tool that uses AI to analyze and diagnose issues within Kubernetes clusters.

Running K8sGPT is as simple as issuing a command from the terminal. The tool connects to the Kubernetes cluster, identifies problems and uses AI to provide human-readable explanations and potential fixes. For example, if a pod is stuck in a pending state, K8sGPT can analyze the situation and suggest corrective actions, such as modifying an affinity selector or adjusting resource limits.

This AI-driven approach significantly reduces the time and expertise required to troubleshoot Kubernetes issues, building upon known and common issues. It empowers even those without deep Kubernetes knowledge to manage and maintain clusters effectively. It also learns from the AI’s explanations and suggestions, given that K8s has been around for a decade and many challenges have been written about and resolved.

## The Future of AI in DevOps
The use of AI in DevOps is still in its early stages, but it’s quickly gaining momentum with the introduction of new open source and commercial services. The rapid pace of innovation suggests that AI will soon be embedded in most DevOps tools. From automated code generation with AIaC to advanced diagnostics with K8sGPT, the possibilities seem endless.

Firefly is not just observing this revolution — it’s actively contributing to it. By integrating AI into DevOps workflows, teams can work smarter, not harder. Whether through open source projects like AIaC or adopting AI-driven diagnostics in Kubernetes, we’re helping to pave a future where AI is an indispensable part of the DevOps toolkit.

As these tools continue to evolve, we can’t forget security and privacy concerns. GenAI tools are third-party tools, and ensuring that sensitive (internal or customer) data isn’t leaked during interactions with AI models is crucial, particularly when using free or experimental versions of AI tools. You may wish to opt for paid versions or API-based integrations that offer more control over data privacy.

## Bringing It All Together
AI is no longer just a buzzword; it’s a practical, powerful tool that can drive significant efficiencies in DevOps. By embracing AI-powered tools like AIaC and K8sGPT, friction in workflows can be reduced, team productivity can be boosted and organizations can stay ahead of the curve in an increasingly competitive landscape.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)