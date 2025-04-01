# Red Hat Arms Developers With AI-Powered Migration Tools
![Featued image for: Red Hat Arms Developers With AI-Powered Migration Tools](https://cdn.thenewstack.io/media/2025/04/8b189415-getty-images-rofhvbj8qrc-unsplash-1-1024x678.jpg)
LONDON — At [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) here, [Red Hat ](https://www.openshift.com/try?utm_content=inline+mention)showed off its developer chips by announcing updates to two of its programming and [platform engineering](https://thenewstack.io/platform-engineering/) tools. The company has released [Konveyor AI (Kai) 0.1](https://www.redhat.com/es/blog/new-updates-konveyor-ai-use-ai-driven-application-modernization-without-fine-tuning-model), an AI-enabled, open source [application modernization](https://thenewstack.io/application-delivery-controllers-a-key-to-app-modernization/) tool, and [Red Hat Developer Hub (RHDH) 1.5](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/pdf/about_red_hat_developer_hub/Red_Hat_Developer_Hub-1.5-About_Red_Hat_Developer_Hub-en-US.pdf), an enhanced developer portal designed to streamline software development processes.

## Konveyor AI 0.1: AI-Driven Application Modernization
[Konveyor AI 0.1](https://www.cncf.io/blog/2024/11/22/konveyor-ai-supporting-application-modernization/) integrates generative artificial intelligence (GenAI) into the legacy migration workflow. The name of its game is to simplify app modernization for cloud native environments. There’s no word about it being used to drag Social Security’s [COBOL](https://thenewstack.io/going-from-cobol-to-cloud-native/) code kicking and screaming into the 21st century.
Kai uses the [retrieval-augmented generation (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) approach. It does this by combining a company’s legacy static code analysis and past migration examples. With RAG, Kai can offer highly relevant code suggestions based on how similar migration challenges have been tackled before, thus avoiding extensive AI retraining.

This release combines model-agnostic [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) with static code analysis, allowing developers to automate source code changes and gain insights from past transformations without requiring model fine-tuning.

Finally, Konveyor is also introducing updates to [help replatform applications to Kubernetes](https://konveyor.io/components/konveyor-cli/). For example, a new asset-generation feature allows for application deployment and runtime configuration retrieval, creating [Kubernetes](https://thenewstack.io/kubernetes/) deployment artifacts.

Other key new features include:

**Improved static code analysis:**Identifies potential issues when adopting new technologies.**Issue tracking:**Maintains a history of resolved modernization challenges.**Enhanced migration intelligence:**Offers 2,400 predefined rules for different migration paths, with the option to define custom rules.**VS Code extension:**Provides suggested code changes within the IDE.
## RHDH 1.5: Enhanced Developer Portal
RHDH 1.5 is a customizable developer portal designed to improve developer productivity and streamline application development. According to a statement by [Balaji Sivasubramanian](https://www.linkedin.com/in/balajisiva/), Red Hat’s senior director of developer tools, “The latest features in Red Hat Developer Hub are designed to not only help organizations increase adoption and efficiency but also allow for a more tailored portal, providing developers direct access to the tools, templates, and components they need to drive innovation.”

So, what are these? First, this release is all about customization. With the [RHDH Extensions Catalog](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/installing_and_viewing_plugins_in_red_hat_developer_hub/rhdh-extensions-plugins_assembly-install-third-party-plugins-rhdh), available as a developer preview, programmers can access a catalog view of community and verified Red Hat plugins.

The extensions catalog offers a doorway to over [60 dynamic plugins](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/dynamic_plugins_reference/con-preinstalled-dynamic-plugins#con-preinstalled-dynamic-plugins%7Chttps://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/dynamic_plugins_reference/con-preinstalled-dynamic-plugins#con-preinstalled-dynamic-plugins). You can then customize the Developer Hub to meet your specific needs. Additionally, with the dynamic plugin framework, your teams can manage any plugin — including custom ones — at runtime without needing to rebuild and redeploy the portal. This makes it significantly faster and easier to onboard new tools and capabilities.

The Developer Hub also now comes with, as a developer preview, a locally runnable version of [RHDH Local](https://github.com/redhat-developer/rhdh-local). This lets platform engineers run a lightweight, self-contained version of RHDH on their local machines, enabling programmers to make changes to their portal more quickly and easily with faster cycle time.

With RHDH Local, users can work on templates, try out plugins, validate software catalogs, and more without installing RHDH on a Kubernetes cluster. Additionally, because it runs in a containerized environment, users can spin up RHDH Local in seconds and tear it down just as quickly. Speaking as someone who likes to keep as much local control as possible, I really love the RHDH Local idea.

Last but not least, an analytical dashboard provides detailed metrics on portal usage, helping teams identify areas of success and improvement.

These updates are part of Red Hat’s ongoing effort to support organizations in developing intelligent applications and maximizing developer productivity. Red Hat plans to keep enhancing its migration toolkit with AI-driven capabilities, aiming to make large-scale modernization more efficient.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)