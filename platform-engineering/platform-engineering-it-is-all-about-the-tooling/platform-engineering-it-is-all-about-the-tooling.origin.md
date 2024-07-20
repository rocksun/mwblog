# Platform Engineering: It Is All About the Tooling
![Featued image for: Platform Engineering: It Is All About the Tooling](https://cdn.thenewstack.io/media/2024/07/328685ee-thisisengineering-f7v66rfronu-unsplash-1024x683.jpg)
[Platform engineering](https://thenewstack.io/platform-engineering/) continues to grow in use and popularity as more companies find that it empowers their software developers and accelerates their operational efficiencies.
By adopting platform engineering, IT systems administrators choose and assemble proven, curated and regularly maintained development applications and deliver them to a company’s developers via an all-in-one self-service portal. That portal frees developers to do their work, rather than spending valuable time searching for applications they need to create and test their code. Also called [internal developer platforms (IDPs)](https://thenewstack.io/the-hidden-benefits-of-internal-developer-platforms/), these platforms are designed to provide developers with the best code-building tools in an easy-to-use environment built to provide automation, standardization, and flexibility for busy application developers.

However, to do this well, IT admins must start by selecting and providing the best combinations of tools for the developer teams in their operations.

## Choosing the Right Platform Engineering Tools
IT admins have lots of choices for the tools they will provide to their developers. They can start from nothing and review and select the individual tools they want to incorporate based on the software needs of their companies, or they can choose from a myriad of collated and recommended reference architectures that are available and get a head start on the process.

“There are different flavors of portals, there is open source, there are different vendors and so on,” [Luca Galante](https://www.linkedin.com/in/luca-galante/), the vice president of product and growth for platform engineering vendor, [Humanitec](https://humanitec.com/?utm_content=inline+mention), and the host of the annual [PlatformCon platform engineering conference](https://platformcon.com/), told The New Stack.

One such collated and recommended [collection of tools for platform engineering](https://platformengineering.org/platform-tooling) is from [PlatformEngineering.org](https://platformengineering.org/), a global platform engineering developer’s community. Created by Humanitec in January 2022 to establish standards and help educate the industry about the new software delivery method, this “platform engineering landscape” tool collection is broken into five development planes. Each of the planes — Developer Control Plane, Integration and Delivery Plane, Monitoring and Logging Plane, Security Plane, and Resource Plane — includes multiple options for applications that can be used to fill those development tool needs.

Other collections of tools from which to start are also available, including [a cloud native landscape](https://landscape.cncf.io/?view-mode=grid) from the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), offering a huge selection of choices from a broad range of community projects and vendors.

“But the big sort of debate lately is ‘where do you start?’” said Galante.

That challenge is what led PlatformEngineering.org to create its own collection of recommended and proven [platform engineering tools](https://thenewstack.io/7-great-tools-for-your-platform-engineering-toolchain/), which is designed to give enterprises an easy-to-use starting place for bringing these practices into their operations, said Galante.

“We distilled a sub-selection of [the [CNCF](https://thenewstack.io/botkube-building-bridges-across-the-cncf-landscape/) tool landscape] based on the community and looking at over 500 platform engineering setups over the last five years, and seeing, OK, what are best practices that are out there and what do people use,” said Galante. “So that is how this basically became the reference architecture for everybody that is either advancing their platform engineering journey or starting their platform engineering journey.”

The reference architecture idea is gaining traction with businesses, he said. Some 20% of the presenters at the PlatformCon 2024 event talked about reference architectures, “so people are really using that now to talk about how they organize their platforms,” said Galante. “Obviously each one of them will have different pools of applications in the different respective [planes], but the architecture is very, very similar [between them].”

The most important part of building a platform engineering platform is to start from the back end foundation because the rest of it will be basically plug and play, said Galante. “Building a platform is like building a house, you want to start from the foundation and then add everything later. That gives you a lot of flexibility and a lot of resilience as a platform team. It is the back end that orchestrates everything, and the front end allows developers to have self-service and get the tools that they need. Those are the core parts of platform engineering.”

## Behind the Scenes in Platform Engineering Platforms
The five planes that make up the PlatformEngineering.org platform tooling landscape include categories for the multiple components that companies can choose for their platforms, said Galante. These application categories include developer portals, version control, application and platform source code, CI pipelines, image registries, platform orchestrators, CD pipelines, and infrastructure control planes. Other categories include [observability](https://thenewstack.io/observability/) and analytics applications, [secrets management](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/), security, cluster management, and data, networking, and services applications.

These applications in the PlatformEngineering.org landscape include [Backstage.io](https://platformengineering.org/tools/backstage-io-spotify), a developer portal; [Atlassian Compass](https://platformengineering.org/tools/compass), another developer portal; [Harbor](https://platformengineering.org/tools/harbor), an open source registry; [Jaeger](https://platformengineering.org/tools/jaeger), an observability application; [Helm](https://platformengineering.org/tools/helm), an open source package maintenance tool for Kubernetes; [MongoDB](https://platformengineering.org/tools/mongodb), a developer database, [Cocalico](https://platformengineering.org/tools/project-calico-open-source), an open source networking and security application for containers; and more.

“The important things are in your two your two first planes — your developer control plane and your integration delivery plane,” said Galante. “The integration delivery plane, it is the back end of your platform. There you have stuff like the platform orchestrator. That is the essential bit — it is the brain of the platform, and it is what allows you to make it really enterprise-ready.”

The second most important part of the platform construction is the orchestrator, “which basically lets developers access these capabilities of the platform,” said Galante. Next is the portal and the rest of the components, which help deliver and present the right tools to the dev teams.

## Bringing Developers Into the Platform Building Equation
At its essence, platform engineering is all about enabling developers with self-service availability of the applications they need to do their work, driving process automation to make developers more efficient by reducing the manual steps they need to take and incorporating process standardization by design.

But to make that happen, shouldn’t developers have some input into the platform engineering process that will be affecting them?

“100% they should be included, but they are not always included,” said Galante. “When they are not included, platform engineering issues can fail. They should have a voice when it is put together.”

To Galante, however, developer inclusion does not extend to having input on which specific tools will be included and offered in a company’s IDP, he added.

At that point, a company’s IT admins need to have the authority to choose and offer the development tools that will be needed across a company’s development environment and be able to ensure that they serve all dev teams and personnel, said Galante.

“The thing that they should not have a voice on, in my opinion, is what tools [should be chosen],” he said. “The tools are irrelevant from the developer perspective — the thought from engineering is ‘let me worry about what the tools are, let me abstract the underlying complexity,’” he added. For platform teams and developers, the IT admins should ask for opinions, but leave the decisions to the administrators, he said.

“As a developer, tell me what you want,” said Galante. “Tell me what you need to do your job well, tell me where the pains are, and I will build a platform that solves that, that drives automation and lets me standardize the stuff in the back end, and you do not have to worry about all that stuff,” he said. “That is why it is essential that they are involved early in the process, and that there is a very, very tight feedback loop between the platform team and developers, because you want to build golden paths for them, not golden cages, right?”

A main goal in building these platforms is to abstract away the complexity without removing too much context or making developers themselves feel abstracted and uninvolved in the process, said Galante.

“The thing is, it is not black or white,” Galante explained. “In an enterprise, you are going to have [multiple] development teams, and [each] is already used to their specific tools — they have their own [CI/CD](https://thenewstack.io/ci-cd/) applications and more. The problem is that it is hard for the platform team to standardize [on individually requested tools] because every development team has their own flavor and does things differently.”

That means that the platform team needs to just do what it thinks is the best for the whole company and give that same standard platform to every team and every developer for their use.

“So, that makes it the minimum common denominator that covers across everybody,” said Galante. “Obviously, is not going to make everyone happy, but it should improve the overall experience of everyone.”

Platform engineering and moving to an IDP is a decision made to benefit an entire organization, and it requires some top-down alignment from engineering.

“You need to build those feedback loops … but from a business alignment perspective, there needs to be clear executive decisions to drive this so that it makes sense,” said Galante.

For large enterprises, platform engineering has gained favor because it provides broad freedom and creativity for developers who no longer need to wait weeks for IT admins to respond to ticket requests so they can do their work with the needed tools. That is why large companies like [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), Facebook, Netflix, and others were the first ones to start developing their own IDPs starting around 2010, said Galante.

“But we are now at a stage where every insurance company, bank, or whatever has thousands of developers, right?” said Galante. “So, pretty much if you are an enterprise, they are all in the same situation where you need to provide this platform layer in between developers and operations. That is where we are right now.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)