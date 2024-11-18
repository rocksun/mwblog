# Using AI for DevOps: What Developers and Ops Need To Know
![Featued image for: Using AI for DevOps: What Developers and Ops Need To Know](https://cdn.thenewstack.io/media/2024/11/0558f5ae-alexander-mils-qthbyjnmwhu-unsplashb-1024x576.jpg)
As the adoption of [AI tools](https://thenewstack.io/favorite-ai-tools-of-developers-and-tips-for-using-them/) and [agents](https://thenewstack.io/make-the-most-of-ai-agents-tips-and-tricks-for-developers/) is increasing among developers, leveraging AI for larger-scale [DevOps](https://thenewstack.io/devops/) approaches is one of the next frontiers for AI-powered software development. While it may be tempting to lead with technology approaches first, embracing DevOps with a more holistic strategy may be the better option. To get some additional insight on what developers may want to consider when using AI with DevOps, I collected perspectives from a number of DevOps experts and developers.

“Success in DevOps is about people and processes in addition to tools,” [writes David Brooks](https://thenewstack.io/devops-in-2024-automate-first-ai-second/), senior vp of evangelism at [Copado](https://www.copado.com/). “Most users are typically so far behind that they don’t have the time to focus on improving their processes and educating their people to use these new tools properly.”

**Employing AI in a DevOps Environment**
Taking that “measure twice and cut once” approach, which focuses on people and processes, was echoed by several other DevOps experts I spoke with. They all stressed that using AI has to be incorporated as part of a larger plan that supports the goals of the organization.

“In DevOps, AI tools play a pivotal role in managing critical workflows like authentication, permissions, testing, and deployment management,” said [Amit Eyal Govrin](https://www.linkedin.com/in/amitgovrin/), founder and CEO of [Kubiya.ai](http://kubiya.ai). “Unlike code generation tools, where deviations from one outcome to another can be acceptable, AI in DevOps demands precision and consistency… developers need to prioritize solutions that not only align with organizational standards but also deliver predictable and repeatable results. Ensuring the AI models are grounded in code and capable of providing transparent, explainable results is essential for regulatory compliance and reliable performance in enterprise environments.”

Having a clear understanding of your organization’s development workflows is a must, and something that [Nick Durkin](https://www.linkedin.com/in/nickdurkin/), field CTO at [Harness](https://www.linkedin.com/company/harnessinc/), encourages developers to understand completely before using AI.

“In DevOps, AI tools play a pivotal role in managing critical workflows like authentication, permissions, testing, and deployment management.”

– Amit Eyal Govrin, founder and CEO of Kubiya.ai
“AI can be incredibly powerful in DevOps when it’s implemented with a clear framework that makes it easy for developers to do the right thing and hard for them to do the wrong thing,” says Durkin. “Making it easy to do the right thing starts with standardizing templates and policies to streamline workflows. Create templates and enforce policies that support easy, repeatable integration of AI tools. By establishing policies that automate security and compliance checks, AI tools can operate within these boundaries, providing valuable support without compromising standards. This approach simplifies adoption and makes it harder to skip essential steps, reinforcing best practices across teams.”

Durkin underscores the need to establish clearly defined policies that enforce “…security, quality, and governance standards at every step” to help developers and minimize errors. “Embedding policy-driven checks into AI tools means that every action taken in the pipeline follows rigorous rules, eliminating the possibility of shortcuts or missed steps,” said Durkin. “For example, if your policy requires AI-driven security scans, then every deployment will automatically include these scans, ensuring compliance without adding manual work.”

That approach can be especially important in highly regulated industries. Durkin explained that one of their financial services customers requires every developer using OpenAI to go through a strict, well-defined pipeline that includes extra steps for added resilience and security.

“This balance — using templates to simplify workflows while enforcing policies to maintain quality and security — creates a framework where AI empowers developers rather than constrains them,” said Durkin. “It enables smoother adoption and integration and helps teams focus on high-impact work, knowing that compliance and governance are covered automatically.”

**Tips for Making AI and DevOps Play Nice**
While having a well-considered strategy in place before embracing AI and DevOps is a must, Durkin and Govrin both offered up some additional tips and advice for getting AI tools and technologies to integrate with DevOps ambitions more easily.

“In enterprise environments, deploying AI applications locally can significantly improve adoption and integration,” said Govrin. “Unlike consumer apps, enterprise AI benefits greatly from self-hosted setups, where solutions like local inference, support for self-hosted models and edge inferencing play a key role. These methods keep data secure and mitigate risks associated with data transfer across public clouds.”

“Think of it like a chef in a kitchen: AI should be used to automate the prep and cleanup, but leave the actual cooking to the chef [developer].”

– Nick Durkin, field CTO at Harness
Durkin suggests using AI-powered DevOps to minimize distractions and make things easier for developers. “Automate the toil that developers don’t enjoy doing. One of the best ways to introduce AI is by using it to handle essential but repetitive or time-consuming tasks, such as compliance checks, testing, or infrastructure management. These are the tasks that developers must complete but don’t look forward to. When AI takes on these items, it frees developers to focus on the more creative and fulfilling aspects of their work, making the integration of AI a positive experience from the start.”

In addition to automation, Durkin argues for “removing the worst parts of the job, not the best” when considering AI DevOps adoption. “AI should make daily work easier and more enjoyable, not replace the work developers value most. Think of it like a chef in a kitchen: AI should be used to automate the prep and cleanup but leave the actual cooking to the chef. Developers want to write code and solve problems; they don’t want to spend time on repetitive, [low-value] work.”

Using AI to eliminate — or minimize or streamline — the least enjoyable tasks helps teams see the value of AI-powered DevOps firsthand and translates into teams that are “much more likely to embrace the change enthusiastically. This approach also fosters a culture of support for innovation, where AI is viewed as a tool for empowerment rather than a replacement,” says Durkin.

**Thoughts on DevOps Tools and Platforms**
While we’ve mainly discussed AI-powered DevOps approaches and tips up to this point, a number of AI tools and platforms are proving to be useful in minimizing any potential friction with DevOps approaches.

[Eran Bibi](https://www.linkedin.com/in/eran-bibi/), the co-founder and chief product officer at [Firefly](https://www.firefly.ai?utm_content=inline+mention), has [shared practical examples](https://thenewstack.io/2-open-source-ai-tools-that-reduce-devops-friction/) of using AI for streamlining DevOps via the open source tools *AI as Code* ([AIaC](https://aiac.dev/)) and the [Kubernetes](https://thenewstack.io/kubernetes/)-focused [K8sGPT](https://k8sgpt.ai/).
“The rapid pace of innovation suggests that AI will soon be embedded in most DevOps tools.”

– Eran Bibi, co-founder of Firefly
“The use of AI in DevOps is still in its early stages, but it’s quickly gaining momentum with the introduction of new open source and commercial services,” writes Bibi. “The rapid pace of innovation suggests that AI will soon be embedded in most DevOps tools. From automated code generation with AIaC to advanced diagnostics with K8sGPT, the possibilities seem endless.”

[Raj Rajkumar](https://www.linkedin.com/in/rajkumar72/), a Technology Consultant at [Tata Consultancy Services](https://www.tcs.com/), has [outlined some benefits](https://www.linkedin.com/pulse/how-ai-evolving-software-development-devops-tools-raj-rajkumar-bew5e/?trackingId=1a2ht8L7QfmS1Q1NwvJxJg%3D%3D) that he believes using AI-powered tools will bring to DevOps in the near future.
“Tasks that currently require human intervention — like requirement gathering, advanced code review, and predictive maintenance — could soon be entirely managed by AI, allowing developers to focus more on innovation,” writes Rajkumar. “The combination of AI and DevOps tools will not just enhance software development but will redefine the way teams work, creating faster, more intelligent, and more reliable systems.”

**Better Together: The Future of AI and DevOps**
While the use of AI in DevOps circles is still relatively new, it’s inevitable that adoption will increase over time. The path to adoption can also be made less arduous by focusing on some clever adoption strategies, like using AI to foster collaboration and thinking beyond using AI just for code generation, Durkin argues.

“AI should reduce friction across teams, whether in development, security, or operations. If an AI tool creates more friction than harmony, it may not be the right fit,” says Durkin. “AI-powered DevOps tools can transform the entire software delivery lifecycle, far beyond just generating code. The most valuable AI implementations will impact testing, compliance, monitoring, and other often-overlooked areas, removing ‘toil’ and empowering developers to focus on strategic, high-impact work.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)