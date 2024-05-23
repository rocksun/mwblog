# What is DevOps?
## A System Engineer’s journey and perspective
[Florian Olivo](https://unsplash.com/@florianolv?utm_source=medium&utm_medium=referral)on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral) **Introduction**
What is DevOps? It’s a question that I remember asking myself before getting into the specific IT field and truly understanding what the answer was.
I’m reminded of a time when I was at a VMware user conference in Melbourne, Australia. I was in a room with many other VMware enthusiasts, eager to find out more about some of the exciting products that VMware and its sponsors had been working on. The gentleman giving the presentation had a really catchy name that made me chuckle; KevOps.
As a Systems Engineer at the time, I looked up to DevOps as the next frontier. At a high level, I knew that it was something about code which I was poor at. But the very nature of it eluded, and frankly, intimidated me. My first understanding was that you needed to be a strong developer, with a great level of coding experience. This is something that I wasn’t good at and never thought it possible to bridge this gap. But the more I dug, the more I discovered. And eventually, as I will explain, found myself doing that very job which seemed to be an unclimbable mountain.
**A brief history of DevOps**
Before we get into what DevOps is, let’s first look back in time to a problem statement.
For non-IT readers:
Operations: Builds the servers that applications run on, such as websites. Developers: Build the applications that run on these servers.
The year is approximately 2007, and there is dysfunction in the way that the development and operations teams are working together across the industry. They are often siloed from one another and have misaligned goals for what their next milestones are. Developers are unable to get their deployments out in a timely manner as operations have many competing priorities to look after the server fleet. No-one is “winning” with this model.
This is where the DevOps term is coined, and we start to pick up momentum on the movement which has (in my humble opinion) revolutionised parts of the IT industry which required some much needed resolution to a rather large problem.
**So, what ** *is *DevOps? *is*DevOps?
Firstly, DevOps cannot be described in a single sentence or statement. In fact, it is something that has several elements or facets. Depending on which lens you are looking through depends on the definition you may be after.
DevOps could be described as:
- A culture
- A framework
- A technical approach
- A type of engineer
Each of these points has a definition depending on your perspective and expertise. This is similar to other concepts like Agile or ITIL wherein your understanding of these topics really boils down to your role and responsibility and how those frameworks fit into it.
Like a house, DevOps builds upon strong foundations before proceeding into implementation of structure and finishing touches. The below diagram helps to illustrate how DevOps starts at a cultural level and builds into living and breathing technologies:
**DevOps as a culture**
With GenAI being a hot topic at the moment, most of us would be familiar with Large Language Models (LLM) such as ChatGPT or Gemini. If you ask ChatGPT what Devops is, this is roughly the response you will get:
“DevOps” is a collaborative approach to software development and IT operations aimed at enhancing the speed, efficiency, and quality of delivering software products and services. It emphasises breaking down silos between development and operations teams, fostering a culture of collaboration, automation, and continuous improvement.
This definition is a perfect way to sum up the cultural aspect of DevOps. It aims at breaking down the barriers between development and operations teams, and thrusting them together in order to achieve a mutually beneficial relationship.
Some of the mantras that DevOps as a culture strives for are:
- We do away with manual and cumbersome tasks.
- We promote automation which in turn helps drive efficiency and agility.
- We use repeatable patterns for consistency.
- We promote collaboration to enhance capabilities and proficiency.
- We learn and adapt to new challenges with an outlook of simplicity rather than complexity.
Lets look at some examples for cultures that do and do
**not **follow the DevOps model.
## Does
**not **follow the DevOps model *Operations team:*
- Tasks are performed manually, such as installing software updates.
- Repeat work does not get automated.
- Requests for new infrastructure are actioned manually.
- Developer code for proprietary applications is deployed manually.
- There are competing priorities to getting activities done within monthly cycles.
- Tasks do not follow a linear process, and are subject to human error.
*Development teams:*
- Significant delays on deployment of proprietary applications as there is a heavy reliance on the operations team.
- Unable to test some deployments in a timely manner.
- No understanding of infrastructure, or if there is, no access to infrastructure.
- Cumbersome and clunky feedback loops from operations team to highlight issues with deployment.
In order to really understand what DevOps solves, we need to understand what a poor environment looks like. Don’t get me wrong, this still happens today and implementing DevOps doesn’t solve everything. However, in the above example, it would help leaps and bounds with timelines and speed of delivery.
**Does** follow the DevOps model *DevOps team:*
- Has a combination of skills across infrastructure, code, automation and build techniques.
- Reviews problems and figures out the best way to solve them once with automation, then relies on said automation to self-heal and correct in the future.
- Follows a strict process for changes being introduced into the environment using a pattern-based approach.
- Uses the smallest possible number of manual tasks.
- Changes are small and incremental.
- Feedback loops are strong and help to build rapport with team members.
When we put these two examples side by side, the improvements are obvious. It is only when you are exposed to this way of thinking that you truly appreciate what DevOps can offer and what you stand to gain from using it.
For our non-DevOps example, the main keyword should be clear; manual. The very essence of DevOps is to automate as much as you possibly can. But, something that is paramount to keep in mind is that you
*can’t* automate everything. DevOps is a journey. This means that you must have clear demarcation between environments that are and are **not **ready for the DevOps method.
For the transition to DevOps, the first element we
*must* get right is culture. We need to accept it and embrace it wholeheartedly. Without culture, we have no unity and no common ground to operate on. DevOps is about collaboration and the understanding that it is not individuals that succeed, it is a team who succeeds. You’ve heard the saying before “a chain is as strong as its weakest link”. This saying speaks volumes to what DevOps means and what its methodologies show us.
After the culture has been agreed upon, the rest falls into place easily as the ground rules have been established.
# DevOps as a framework
When we look at DevOps as a framework, we think more about the ways of working. This consists of:
- What does DevOps mean for our teams?
- What are the sub-concepts of DevOps that need to be understood?
- How do we ensure everyone in our team is set up for success?
These are a sampling of many other questions we ask ourselves. The framework allows us to define our ways of achieving success and deliver meaningful results with tangible benefits.
Let’s do a quick high level list of what each side of DevOps has expertise in:
For non-IT readers: I’m sorry to say that this is just some of the technical jargon and concepts that we use within IT. I recommend doing research into the topics that you don’t understand and are interested in knowing more about.
This is another sampling of some key concepts which are common within the DevOps framework. There are others, however the aim here is to simply illustrate the main ones. Like in our DevOps as a culture section, you may start to identify some mutually beneficial areas of expertise.
At its core, DevOps as a framework aims to bring together these different areas of expertise for the purpose of deploying, managing and maintaining your infrastructure solutions and applications. It does this by:
- Combining SCM and CI/CD processes to build and deploy infrastructure-based solutions. This is commonly referred to as a GitOps model.
- Automating manual tasks that are regularly repeated.
- Leveraging the concept of stateless architecture that is fault tolerant and can scale based on demands.
- Creating event-driven architectures that react to changes in an application.
- Reusing well known patterns to enhance agility and speed of delivery.
# DevOps as a technical approach
Before we proceed into more of the technical detail and technical elements of DevOps, I’d like to take a trip back in time to a real world scenario that I experienced first hand.
For non-IT readers:
Windows — I’m sure most are familiar with Windows on your laptops/PCs. There are also server versions available to build applications upon.
VMware — This is a virtualisation platform that allows you to run several virtual servers on a single physical server located in a data centre.
SCCM — A specific product for Windows servers to install applications and operating system updates (patches)
In a specific environment back in 2017, I recall doing manual tasks which were similar to what was referenced in the DevOps as a culture section that did
**not **follow the DevOps model. The environment was Windows heavy, and used VMware as its virtual environment. Servers were patched manually using SCCM. This process consisted of:
- Each member of the operations team taking a handful of servers from a list
- Logging into those servers using management access
- Launching the SCCM client
- Installing updates
- Performing reboots
It was a cumbersome process, especially given that there were several servers that had to be patched in this manner. The cherry on top of all this? It was a monthly occurrence.
This example helps to illustrate what life was like before DevOps on the operations side. It is also one of the many tasks which are required to be performed regularly to maintain the environment and to “keep the lights on” as the saying goes. When you realise what DevOps can offer, performing manual tasks regularly feels like a lot of wasted effort with very little return on investment in the form of time.
In regards to DevOps as a technical approach, we now start to get deeper into the actual tools which are used to perform various actions and tasks.
Below is a list of concepts and some respective applications which you may be familiar with:
For non-IT readers: more technical jargon and concepts! Feel free to do your own research.
This is another sampling only, for the purposes of illustration.
By using a combination of these tools to run our environment, we can build out solutions that are either platform related (supporting a platform in a large/scaled environment) or application specific. This diagram shows how we can apply these concepts and applications into a real-world scenario:
**Point 1 — Code is stored in GitHub**
This ensures that we can:
- Properly maintain a consistent source of truth which the entire team will use.
- Create versions of the codebase to have staggered and controlled deployments into various environments such as dev > test > prod.
- Vet changes that are proposed to be introduced into the codebase by undergoing review and approval processes from peers.
- Integrate with Buildkite for automatic deployments.
**Point 2 — Using Terraform for IaC**
Terraform is used to Create/Replace/Update/Delete (CRUD) resources on AWS. By using Terraform in conjunction with Github and Buildkite, we are using what is referred to as a GitOps model that can perform deployments on our behalf. It also ensures:
- Resources are deployed using a consistent and streamlined approach.
- There are no deviations from this process, as only Buildkite is given access to perform deployments using Terraform.
- Code can be reused over and over to promote the Don’t Repeat Yourself (DRY) model, where you only need enhancement rather than doing things from scratch every time.
**Point 3 — Using Buildkite for CI/CD**
Buildkite is used as the CI/CD platform to perform validation, planning and deployments. Buildkite will use GitHub as its source to ensure we maintain consistency.
**Point 4 — Validation of code before deployment (the CI of CI/CD)**
Validation and planning pipelines are run before any deployments so we know what to expect.
You may also choose to enhance this step and perform a mock deployment in a development environment. This can further highlight unforeseen issues, and cause you to re-think your approach and make adjustments.
**Point 5 — Pull request peer review**
Once enough evidence has been gathered, we can request colleagues to review our pull request and, if all is in order, proceed to merging.
Collaboration is king, and as mentioned in the culture aspect of DevOps there is always something more you can learn and adjust based on thoughts of your colleagues.
**Point 6 — Pull request merging and deployment (the CD part of CI/CD)**
Once a pull request is approved and merged, automation will take over and resources are deployed.
By utilising this GitOps model, each step along the way is controlled and should have relatively foreseen actions. It can be used over and over again to continuously introduce changes into your environment.
DevOps is all about finding ways of making life easier through the tools you have.
# DevOps as a type of engineer
With the previous layers comfortably in place, we find ourselves at the apex of the DevOps house; engineering. For DevOps engineers, the lower layers give us the strong foundations we need to put pen to paper and come full circle to complete the entire model.
But in a rather counterintuitive way, being labelled as a DevOps engineer is not something that aligns neatly across the industry. For example, there is no issue with applying the DevOps model to say an on-premises environment. Most of the conceptual tools outlined have on-premises equivalents. And even if they don’t, you can still use Software as a Service (SaaS) based offerings to perform deployments in an on-prem setting.
As a field, it has been collectively assumed that DevOps means public cloud only and it’s not the case. Whilst the DevOps models apply comfortably to public cloud, there are still edge case scenarios where you can apply it to on-prem environments. This brings me to the crux of this section which makes it hard to define someone as a DevOps engineer.
In the technical approach section, we covered concepts such as IaC and CI/CD. The tools that build upon these concepts will appear in different forms throughout the industry. This is because the number of tools (in some senses) which use these concepts as their basis are vast. As an example, within
*company A* as a DevOps engineer, you might use the tools GitHub (SCM), GitHub Actions (CI/CD) and Terraform (IaC). But as a DevOps engineer in *company B*, you might use BitBucket (SCM), Bamboo (CI/CD) and CloudFormation (IaC for AWS).
The point being illustrated is that DevOps at the engineering level does not have consistency across the entire industry. Personally, I’ve worked across several environments now that utilise the DevOps model and there is not a single environment that uses the exact same tools. Whilst there are many similarities, they are not like for like.
Another good example is when you are applying the DevOps model to the public cloud space. Although they all have similar concepts, they are still different in terms of the terminology they use and how they apply those concepts in action.
This makes it challenging to define someone as a DevOps engineer. Realistically, when you do see a role for a DevOps Engineer, it will be for that specific company and that specific environment. One could argue that a Platform Engineer may come into the equation when you start to talk about multi-cloud and multiple different technology stacks. Despite this, the term DevOps Engineer will stick around and the assumption is that there is an expected level of ambiguity that comes with it.
# Conclusion
I hope now that after reading this, you get some insights into the very complex question that is
*What is DevOps?* The beauty of DevOps is that it has many different rabbit holes to explore and will continue to change in the future. Many organisations are still striving to achieve their final version of DevOps, leading to plenty of opportunities for eager engineers to get their hands dirty and implement some sophisticated solutions.
DevOps is an advanced model that is not simple to understand. I tell people who I give advice to or mentor that as a DevOps engineer you don’t need to understand absolutely everything. Instead, you need to be able to find an answer relatively quickly and start to apply your DevOps logic to the situation. It takes years of dedication and constant upskilling to hone one’s abilities and potential purely given the nature of DevOps and the meeting of two major IT fields.
If you are looking to explore DevOps or are just curious, the best way to learn is by doing. The technical approach section covers some great applications that you can use. Some of these even come free to use in a personal setting, allowing you to experiment and practice your own labs and setups.
Thank you for reading! If you find this content appealing, please let me know so I can continue to create such content.