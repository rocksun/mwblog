# Building for Integrations Is a Future-Minded Growth Strategy
![Featued image for: Building for Integrations Is a Future-Minded Growth Strategy](https://cdn.thenewstack.io/media/2024/09/4a4af189-andy-brown-4coahsfibkq-unsplash-1024x799.jpg)
[Andy Brown](https://unsplash.com/@basallt?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash.](https://unsplash.com/photos/a-bunch-of-pens-and-notebooks-on-a-table-4cOaHsfIBKQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
In a world where teams [use SaaS solutions](https://thenewstack.io/saas-is-dead-long-live-saas/) for everything from hiring decisions to social media posts, an abundance of tools can quickly go from a blessing to a burden.

According to a Harvard Business Review study, the average employee switches between apps 1,200 times daily, leading to four hours lost each week to context-switching. Imagine a world where seamlessly integrated workflows can help create more time for deep thinking, prevent conflicting sources of truth, and reduce redundant IT spending.

This is why it’s valuable to build pluggable products. If they’re built correctly, integration capabilities can become essential growth drivers for your platform. This means not just shipping information from [one API endpoint to another](https://thenewstack.io/api-management/) but designing a seamless experience that creates new possibilities for developers and users alike.

We’ve aspired to this from the beginning at Canva, but as technology has evolved and our platform has become more complex, we’ve had to reevaluate how we approach integrations continuously. I hope that by sharing what we’ve learned, other startups can benefit from our experience.

## The Meandering Path to Building a Pluggable Platform
Early on, we recognized that apps and [APIs](https://thenewstack.io/apis-are-driving-new-business-models-and-unlocking-revenue-streams/) could help us expand Canva’s capabilities and meet user needs faster than if we were to build everything in-house. However, the number one rule in startups is prioritization, and integrating with other platforms is often deprioritized against more foundational features. In Canva’s case, our primary focus was to grow our core product before [expanding externally through APIs](https://thenewstack.io/long-live-the-api-stack-full-life-cycle-api-management-is-dead/).

Our first APIs were released in 2019. They enabled very simple integrations within Canva, like bringing images from a DAM or CMS like Bynder to Canva or publishing a Canva design directly to a platform like Instagram. These lightweight, single-function extensions validated use cases and tested the potential of extending our platform.

As we grew, we also saw an opportunity to reach new users by equipping developers and platform partners with a simplified, unauthenticated version of the Canva editor that could be embedded in third-party solutions via a pop-up.

While both of those integration points were popular, the feedback and feature requests that we received because of them made us realize that these initial offerings would not be able to support the long-term needs of developers and users. It became increasingly obvious that we needed to make it easy (and rewarding) for other platforms to meaningfully integrate with us and give customers and partners more choices while maintaining the integrity of the core Canva experience for end users.

To do that, we needed to invest time and resources to build the proper infrastructure, with the underlying philosophy that [it’s better to slow down and ship the right solutions](https://thenewstack.io/say-no-to-ship-it-culture-slow-and-steady-wins-the-race/) than to [ship fast and compromise your product value.](https://thenewstack.io/how-sprinting-slows-you-down-a-better-way-to-build-software/)

## The Importance of Balancing User and Developer Experience
These extensibility frameworks were popular with our early developer community but weren’t the right technical solutions for long-term growth. Our initial APIs were disjointed and limited in functionality, and the unauthenticated “pop-up version” of Canva delivered a user experience that suffered from slower, less responsive performance.

We needed to meet developers’ needs without compromising the user experience that draws people to Canva. With that in mind, we worked closely with beta developers on our platform to learn which app functions were most desirable for app builders. We uncovered numerous exciting possibilities but knew it would take a lot of effort to build each one robustly. We focused on shipping those that could provide the safest, most straightforward, and most powerful experience for users, like programmatic image uploads and the ability to add elements to designs.

We also needed to ensure every third-party app met the same quality bar we set for our overall Canva product experience. Our earliest adopters helped us learn that not every team has the resources to meet this bar. So, we evolved our early APIs into a full SDK, including a UI Kit full of standard components and thorough design guidelines. These ensure anyone can build beautiful apps no matter the size of their team while simplifying development, resulting in hundreds of apps being launched in under a year.

Delivering a simple but more robust solution to the pop-up integration required a different balancing act. When building a new library of public REST APIs, we had to follow industry standards for API specs, naming, security, and endpoint testing to provide a familiar experience for developers. While table stakes, it’s a step often skipped in the interest of speed. To be thorough in that regard, we had to prioritize the essential parts of the Canva Editor while still giving integration partners enough flexibility to pick and choose which parts of the Canva Editor would best suit their users.

Knowing our partners understand their user needs best, we were keen to give developers a familiar, flexible framework while ensuring they could build something that feels true to Canva, no matter the platform.

## Validating Your APIs With Early User Feedback
We knew REST APIs could help teams using Canva streamline their workflows with other apps, but we were still determining how our partners would implement them in practice.

Over time, we’ve set up multiple ways to hear directly from partners — such as our Developer Community — which has become vital when deciding what to build next because we get direct feedback on the diverse ways integrations might help us and our partners grow.

For example, we heard from Vela, a leading e-commerce optimization platform whose users asked for a more robust native design editor. Using the Connect APIs, Vela built an integration where users can access and view Canva designs directly in the Vela UI. They can also easily modify and update their creative assets right from Vela’s UI through an “Edit in Canva” functionality.

When those designs have been updated, users are immediately returned to where they started in Vela, making the whole process feel seamless. According to Vela, this has saved their users several hours a month, enabling them to focus on what they love doing most — growing their respective businesses. Vela’s feedback helped us validate our original vision for the Connect APIs and how they could help our customers and partners’ users be more productive.

Getting early user feedback is instrumental in the API design process. It helps you understand how useful your new endpoints will be and what is needed for future iterations.

## The Future of Work Is Integrated
Expanding our developer platform through well-thought-out APIs and supportive tools has played a significant role in our evolution from a personal design tool to an all-in-one work platform.

We’ve been able to keep pace with the needs of sales or marketing professionals with well-used integrations like Slack and Asana while simultaneously enabling organizations like Vela to build the solutions they need in-house. Our Apps SDK also helped us scale our AI offering from a native AI feature to nearly 100 AI-powered apps in under a year.

As we’ve built this developer platform to evolve with our users’ changing needs, we’ve learned that it’s important to balance the developer’s needs while standing strong in your core product values. Our path to the right solution was not a linear journey but a winding road that forced us to ask ourselves whether we were shipping the “right thing” or the “easy thing”.

When building pluggable products, the goal is to create an experience that delights everyone involved — products that users love, developers want to build on, and product owners are proud of. Focusing on all of their needs will help you achieve this balance.

## Related Articles
[Long Live the API Stack: Full-Life-Cycle API Management Is Dead]
[How Sprinting Slows You Down: A Better Way to Build Software]
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)