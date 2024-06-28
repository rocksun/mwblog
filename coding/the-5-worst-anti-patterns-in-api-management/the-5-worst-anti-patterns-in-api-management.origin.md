# The 5 Worst Anti-Patterns in API Management
![Featued image for: The 5 Worst Anti-Patterns in API Management](https://cdn.thenewstack.io/media/2024/06/733ca170-donuts-2031755_1280-1024x683.jpg)
Imagine this: you are working in a company named *DonutGPT* as Head of [Platform Engineering](https://thenewstack.io/platform-engineering/), and you sell millions of donuts online every year with AI-generated recipes. You need to make your critical services available to hundreds of resellers through secured APIs. Since nobody on earth wants to see his donut order fail, your management is putting on the pressure to ensure a highly available service.

Your current production environment consists [mostly of VMs](https://thenewstack.io/the-new-age-of-virtualization/), but you are in the process of progressively migrating to a [cloud native platform](https://thenewstack.io/cloud-native/). Most of the production services you handle expose APIs, but your team has very little control and visibility over them. Each service is owned by a different developer team, and there is no consistency in languages, deployed artifacts, monitoring, observability, access control, encryption, etc.

Some services are Java-based, “secured” with old TLS 1.1 certificates, and behind a JWT access control policy. Other services are Python-based, use TLS 1.3 certificates, and are behind a custom-made access control policy. This diversity can be extended to the rest of the services in your production environment.

You (reasonably) think that this situation is far from ideal, and you plan to rationalize APIs at *DonutGPT* with the help of an API Management solution. Your requirements include:

- Your APIs should be strongly governed with centralized and consistent security policies
- You need advanced traffic management like rate limiting or canary releases
- You need real-time observability and usage metrics on all public endpoints
Simply put, you want predictable operations, peace of mind, and better sleep.

It looks like your plan is right, and you are on track for better days (or nights). However, an [API journey](https://thenewstack.io/three-horizons-of-your-api-journey/) is long, and the road ahead is full of obstacles. Here are the top five worst anti-patterns you should avoid when you start your API odyssey.

## Anti-Pattern 1: Monolith-Microservices
You are about to invest time, money, and effort in setting up an API management solution. In this process, you will centralize many aspects of your exposed services like traffic management, connectivity security, and observability. It’s easy to think, “The more centralized everything is, the more control I have, and the better I will sleep.” Why not use this API management solution to intercept every API call and transform the HTTP body to sanitize it from sensitive data (like private information)?

This would ensure that every API call is clean across the whole system. That’s true, but only in the short term.

Let’s fast forward three years. Your API management platform is now mature and manages hundreds of APIs across dozens of different teams. The initial quick win to sanitize the HTTP body within the API management workflow gradually became a white elephant:

- The first quick patch inevitably evolved into more complex requirements, needing to be adapted to every API. Your ten stylish lines of code quickly grow to an unmaintainable 5000-line script.
- No one wants to take ownership of this custom script now that it operates many teams’ APIs
- Every new version of an API may require updating and testing this piece of code, which is located in the API platform and separated from the services’ code repositories.
- It takes a lot of work to test this custom script. If you have any issues, you will first learn of them from live traffic, and you will have a hard time debugging it.
- Your API solution is highly resource-intensive. You should avoid delegating the whole HTTP body to your reverse proxy. This consumes most of the CPU allocated to your platform, giving you very little margin for security while making it a super expensive approach.
In short, it’s best to avoid short-term decision-making. What seems like a good idea at the time may not hold up several years down the road. API management is designed to discover, secure, organize, and monitor your APIs. It should not be used as a shortcut to execute application code.

→ Separation of concern is critical when designing your next production platform.

## Anti-Pattern 2: Cart Before the Horse
Another interesting anti-pattern is a laser focus on the long-term, possibly idealized, outcome without recognizing or understanding the steps to get there. Your API transformation project is so expensive you want to ensure everything runs smoothly. So, you choose the most feature-rich API management solution to cover all possible future needs despite being unable to take most of its capabilities today.

Sure, it’s more expensive, but it’s a safe bet if it prevents you from a potential migration in three years. This may seem risk-free, but you only see the tip of the API project iceberg.

Fast forward three years with this top-notch & expensive solution:

- The transition from the legacy platform took way longer than expected.
- This new solution required paid training sessions from the vendor for your team and many developers throughout the company
- You STILL have yet to use many features of the solution.
- Many developer teams avoided adopting this new platform due to its complexity.
- Your initial goal of controlling all API calls within the company has yet to be reached.
- You still have inadequate sleep.
At this point, you acknowledge that the most complete (and complex) solution might not be the best option, so you bite the bullet and decide to migrate to a simpler solution that fits your existing needs. In your attempt to avoid an API management migration three years after starting your project, you ended up causing it anyway, only sooner than initially anticipated.

The point here is that while you should aim for your long-term vision (and choose a solution that aligns with it), address your needs today and strategically build towards that vision. This includes planning for progressive training and adoption by the teams. If the product cannot provide you with a progressive learning curve and deployment journey, then you won’t be able to stick to your plan.

Here is an example of a progressive journey with the same product:

- Start small with basic ingress resources on Kubernetes.
- Then, an API Gateway will be introduced that brings API traffic management and security.
- Then, after you have a much better understanding of the features that are important for your business, transition to an API management platform.
In a nutshell, don’t pick a product because of all the bells and whistles. No amount of cool features will solve your challenges if they never get used. Evaluate them based on what it’s like to use to meet your needs today and whether or not they provide a progressive transition to more advanced use cases in the future.

→ Don’t get ahead when transitioning to your API management platform.

## Anti-Pattern 3: Good Enough as Code
As a modern Head of Platform Engineering, you strongly believe in[ Infrastructure as Code](https://youtu.be/RFvC_lGc2X8?si=dMVYaYzKUKauFCw1) (IaC). Managing and provisioning your resources in declarative configuration files is a modern and great design pattern for reducing costs and risks. Naturally, you will make this a strong foundation while designing your infrastructure.

During your API journey, you will be tempted to take some shortcuts because it can be quicker in the short term to configure a component directly in the API management UI than setting up a clean IaC process. Or it might be more accessible, at first, to change the production runtime configuration manually instead of deploying an updated configuration from a Git commit workflow. Of course, you can always fix it later, but deep inside, those kludges stay there forever.

Or worse, your API management product needs to provide a consistent IaC user experience. Some components need to be configured in the UI. Some parts use YAML, others use XML, and you even have proprietary configuration formats. These diverse approaches make it impossible to have a consistent process.

You say, “Infrastructure as a Code is great, but exceptions are ok. *Almost* Infrastructure as a Code is good enough.”

Fast forward three years:

- 60% of the infrastructure is fully declared in configuration files and sits in a git repository
- Those configuration files are written in five formats: YAML, INI, XML, JSON, and a custom format.
- The remaining 40% requires manual operations in some dashboards or files.
- There is such diversity in configuration formats or processes that your team is unable to get the platform under control and constantly needs to be rescued by other teams that have knowledge of each format or process.
- Human error is so high that your release process is prolonged and unreliable. Any change to the infrastructure requires several days to deploy in production, and this is the best-case scenario.
- In the worst-case scenario, a change is deployed in production, creating a major outage. As your team is not able to troubleshoot the issue quickly, the time to recovery is measured in hours. Your boss anxiously looks at the screen over your shoulder, waiting for the miraculous fix to be deployed. Thousands of donut orders are missed in the process.
- You don’t even try to sleep tonight.
The conclusion is obvious — setting up API Management partially as code defeats the purpose of reducing costs and risks. It’s only when[ your API Management solution is 100% as code](https://traefik.io/solutions/api-management/) that you can benefit from a reliable platform, a blazing fast time to market, and fast recovery.

Exceptions to the process will always bring down your platform’s global efficiency and reliability.

→ Never settle for half-baked processes.

## Anti-Pattern 4: Chaotic Versioning System
When you start your API journey, planning for and anticipating every use case is difficult. Change is inevitable, but how you manage it is not. As we’ll see in this section, the effects of poor change management can snowball over the years.

Let’s go back to the very beginning: You are launching your brand new API platform and have already migrated hundreds of APIs into production. You are pretty happy with the results; you feel under control and are getting better sleep.

After one year, your state-of-the-art monitoring alerts flood your notifications, pointing to a bunch of API calls from one of your biggest customers with 404 errors. 404 errors are widespread, so you pay little attention to them and quickly forward the issue to the developer team in charge of the API.

During the following months, you see the number of 404 errors and 500 errors rising significantly, affecting dozens of different APIs. You start to feel concerned about this issue and gather your team to troubleshoot and find the root cause.

Your analysis uncovers a more significant problem: your APIs need a consistent versioning system. You designed your platform as if your API contracts would never change, as if your APIs would last *forever*.

As a result, to handle change management and release new versions of their APIs, each team followed the processes:

- Some teams did not bother dealing with compatibility checks and kept pushing breaking changes.
- Some teams tried to keep their APIs backward compatible at all costs. Not only did this make the codebase a nightmare to maintain, but it slowly became obvious that it discouraged teams from innovating, as they wanted to avoid breaking changes and maintaining compatibility with all versions.
- Some teams followed a more robust process with the use of URL versioning, like https://donutgpt.com/v1/donuts and https://donutgpt.com/v2/donuts. They were able to maintain multiple versions at the same time, with different codebases for each version. The problem was that other teams were using different strategies, like query parameter versioning (https://donutgpt.com/donuts?version=v1) or even header versioning.
- Some teams consistently followed a specific versioning strategy like URL versioning but did not provide versioned documentation.
This study makes you realize how creative the human brain is — the developers chose so many different options!

The result is that customers were:

- Using outdated documentation
- Calling outdated or dead APIs
- Calling different APIs with different versioning strategies
- Calling unreliable APIs
- Receiving donuts with your new “experimental recipe” when they ordered your classic “Legend GPT Donut”
The key takeaways are apparent: No code lasts forever, and change is a natural part of API development. Given this truth, you must have a strong, reliable, and repeatable foundation for your release process and API lifecycle management.

Your choice of API management solution can help, too. Choose a solution that provides a flexible versioning strategy that fits your needs and can be enforced on every API of *DonutGPT*.

Additionally, ensure teams maintain several versions of their APIs that can be easily accessible as part of a broader change management best practice. This is the only way to maintain a consistent and reliable user experience for your customers.

→ Enforce a uniform versioning strategy for all your APIs.

## Anti-Pattern 5: YOLO Dependencies Management
Now that you’ve learned why managing your API versioning strategy is critical, let’s discuss dependency management for APIs — a topic that is often highly underestimated for a good reason. It’s pretty advanced.

After the miserable no-versioning-strategy episode, you were reassured to see versioning policies enforced on every piece of code at *DonutGPT*. You were even starting to sleep better, but if you’ve read this far, you know this can’t last.

After two more months, your state-of-the-art monitoring again alerts you to several API calls from one of your biggest customers, resulting in 404 errors! You’ve got to be kidding me! You know the rest of the story: task force, troubleshooting, TooManyDonutsErrors, root cause analysis, and (drum roll) …

All your APIs indeed followed the enforced versioning strategy: https://donutgpt.com/v1/donuts. So, what happened?

This was only enforced on the published routes on the API management platform. The services behind the APIs were following a different versioning strategy. Even for those few, there was no dependency management between your API routes and backend services.

In other words, https://donutgpt.com/v1/donuts and https://donutgpt.com/v2/donuts were able to call the same version of a service, which led to a situation similar to the no-versioning-strategy episode, with a terrible customer experience. It gets even more complex if some services call other services.

You start to see my point: you need dependency policies enforced on all your APIs and services. Every API needs to be versioned and call a specific service version (or range), and this same approach should be applied to every service. To achieve this, your API management solution must provide a flexible way to express dependencies in API definitions. Furthermore, it should check for dependencies at the deployment phase through intelligent linters to avoid publishing a broken API dependency chain.

These capabilities are uncommon in API management products, so you must choose wisely.

→ Enforce dependency checks at deployment.

## Wrap Up
You dedicated most of your career to building *DonutGPT’s *infrastructure, solving countless challenges during this adventure. The outcome has been quite rewarding: *DonutGPT* disrupted the donut market thanks to its state-of-the-art AI technology, producing breathtaking donut recipes.

You are proud to be part of this success story; however, while accelerating, the company now faces more complex problems. The biggest problem, by far, is the industrialization of *DonutGPT’s *APIs consumed by customers and resellers. During this journey, you tried multiple solutions, started over, and made some great decisions… and some debatable ones. *DonutGPT* messed up a few donut orders while exploring the API world.

Now that you can stand back and see the whole project, you realize that you have hit what you consider today to be anti-patterns. Of course, you learned a lot during this process, and you started thinking it would be a great idea to give that knowledge back to the community through a detailed blog post, for example.

Of course, this story, the character, and the company are fictitious, even though AI-generated donut recipes might be the next big thing. However, these anti-patterns are very real and have been observed repeatedly during our multiple conversations at Traefik Labs with our customers, prospects, and community members.

While planning your API journey, you should consider these five principles to maximize your return and minimize your effort:

- Design your API platform with a strong separation of concerns. Avoid delegating business logic to the platform.
- Do not set the bar too high or too fast. Proceed step by step. Start with more straightforward concepts like ingresses and progressively move to more advanced API use cases once you understand them better.
- While industrializing your processes, tolerating exceptions will defeat the purpose, and you won’t gain all the expected benefits of a fully automated platform.
- Versioning becomes a critical challenge in the long run. Starting your API journey with a strong and consistent versioning strategy across all your APIs will make your platform more scalable, reliable, and predictable.
- Within complex infrastructures with many moving parts, controlling and certifying runtime dependencies for all components is crucial to achieving a high level of trust and stability for your platform.
Of course, this list is not exhaustive, but it covers the most common practices. All that said, these recommendations should not prevent you from drifting away and trying different processes. Innovation is built on top of others’ feedback, but still requires creativity.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)