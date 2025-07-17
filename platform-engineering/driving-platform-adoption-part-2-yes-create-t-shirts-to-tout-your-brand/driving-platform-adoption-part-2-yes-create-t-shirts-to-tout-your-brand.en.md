*This is the second in a series. Read also:*

“Do you have a T-shirt yet?” our colleague [DaShaun Carter](https://www.linkedin.com/in/dashaun/) asks platform teams. That seemingly frivolous question actually cuts to the heart of [platform marketing](https://thenewstack.io/the-art-of-platform-marketing-youve-gotta-sell-it/): brand identity. While engineers often dismiss branding as marketing fluff, the reality is that technical teams form deep attachments to their tools just like sneakerheads obsessing over the latest Air Jordans.

Consider how developers self-identify: Ask them what type of developer they are, and they’ll immediately name their primary language. “I’m a Java developer” or “I’m a Python dev.” Operations folks do the same — they’re “VMware admins” or “Linux admins.” This tribal identification with technology tools drives both adoption and persistence through the inevitable technical challenges.

This brand affinity matters even more for internal platforms since you can’t piggyback on existing [open source or vendor communities](https://thenewstack.io/power-community-open-source/). When developers weave your platform into their professional identity, they’ll not only stick with it but also evangelize it to colleagues. That word-of-mouth marketing is pure gold.

Little wonder, then, that many of the successful platform teams we’ve talked with over the years put a lot of effort into branding their platforms. Organizations like the [U.S. Air Force](https://en.wikipedia.org/wiki/Kessel_Run), JPMorgan Chase and Mercedes-Benz each create brands for their internal development platforms.

## Symbols: Names, Logos and Color Schemes

[![Brand building blocks](https://cdn.thenewstack.io/media/2025/07/721f01e3-buildingblocks-1024x535.png)](https://cdn.thenewstack.io/media/2025/07/721f01e3-buildingblocks-1024x535.png)

Brand building blocks.

The basic building blocks of a brand — logos, slogans, color schemes and names — deserve serious attention from Day 1. While your platform’s visual identity should align with your organization’s brand, you have room to be more playful and personable. Avoid dry, bureaucratic names like “Enterprise Developer Services” or “Internal Cloud Platform Architecture Cluster.” Instead, give your platform a name you’d use affectionately. If you find people referring to your platform by its initials (EDS or ICPAC, with the above), you probably need a better brand name.

Look at successful examples: The [U.S. Air Force’s “Kessel Run”](https://en.wikipedia.org/wiki/Kessel_Run) captures the platform’s maverick spirit, while [JPMorgan Chase’s “Gaia”](https://www.youtube.com/watch?v=QOvBWlf7Cgg) suggests global enterprise scale. Your platform’s name should signal its essence to developers.

Here are some ways to start brainstorming brand names:

1. **What superpower does your platform give developers?** “Turbo” for speed, “Nimbus” for seamless cloud integration, “Vault” for security and compliance.
2. **How would a developer casually mention your platform in conversation?** “I’m pushing the app to Shipyard” or “Let’s test it in Vault.” Names that feel awkward in these contexts will struggle to gain organic adoption.
3. **What metaphors or symbols from your industry, company culture or technology space could represent your platform’s purpose?** Consider using terminology that aligns with your industry. The U.S. Air Force’s Kessel Run is a great example; it evokes flight and coolness.

Once you settle on a brand, you should put the logo, name and colors on all of your platform’s UIs, documentations, maybe even command line tools. You’re also going to need to create physical manifestations of your brand: stickers, T-shirts and banners. This last part is a serious recommendation, done by most organizations I’ve talked with. It’s why Carter always asks about the platform’s T-shirt first thing.

The platform’s brand signals what your platform does for developers and what your platform is. Speaking of, let’s look at defining your platform’s ethos as part of its brand.

## Case: Platform Branding in 12 Parsecs

As part of an ongoing effort to modernize how the U.S. Air Force built and ran software, [project Kessel Run was set up](https://en.wikipedia.org/wiki/Kessel_Run) to introduce agile software development and platforms into the service branch. This was an imposing task and required a little irrelevant maverickness, done, of course, with permission and intentionally.

[![Kessel Run logo](https://cdn.thenewstack.io/media/2025/07/0ff55ea1-kessel-run-logo.jpg)](https://cdn.thenewstack.io/media/2025/07/0ff55ea1-kessel-run-logo.jpg)

Kessel Run logo.

What better way of embodying that ethos than to evoke Han Solo, the maverick pilot from “Star Wars.” In the movie, Han Solo boasts that he “made the Kessel Run in less than 12 parsecs,” something that even his trusted co-pilot balks at. Thus, when the service branch was looking for a name that would bring that spirit of doing the impossible — and maybe a little bit of bravado — it named the project Kessel Run, [complete with a logo that evoked that same ethos](https://en.wikipedia.org/wiki/Kessel_Run), using a silhouette of Han Solo’s ship.

[![The "AgileAF" T-shirt](https://cdn.thenewstack.io/media/2025/07/ab35b9c8-agileaf.jpg)](https://cdn.thenewstack.io/media/2025/07/ab35b9c8-agileaf.jpg)

The “agileAF” T-shirt.

This attention to branding, slogans and other marketing continued with slogans like “Code. Deploy. Win.” And, of course, T-shirts such as the cleverly done “#agileAF” which could stand for “agile Air Force” or the popular slang expansion, “AF.”

Kessel Run has been a great success. Obviously, clever T-shirts and logos are a small part of that. But they’re an example of what we see consistently at organizations that put in place and maintain platforms: Marketing is a necessary component.

## Ethos: How Your Platform’s Beliefs Drive What You Get

More than just a name, the brand often comes with a set of principles and values — an ethos. Organizations often make little booklets of their platform ethos. At the very least, they write them up and include them in the documentation.

Here are some examples of technology brands and ethos:

* **Java:** Stability, portability and backward compatibility. “Write Once, Run Anywhere” embodies the philosophy that code should be able to run across platforms without modification, prioritizing reliability and enterprise-grade robustness over cutting-edge innovation. This clear brand and ethos signal that Java is a perfect pick for programming enterprise applications.
* **Apple:** User experience, aesthetics and tightly controlled integration. Apple optimizes for a seamless, intuitive experience, often at the expense of user-level customizability. It signals that Apple is perfect for consumers, maybe not so much for “enterprise-grade” needs.
* **Cloud Foundry:** Developer productivity, simplicity and enterprise requirements for security and reliability. Cloud Foundry assumes that developers should be able to push code with minimal configuration, while the platform handles everything else: networking, scaling, load balancing and service bindings. Developers and platform engineers using Cloud Foundry should not have to spend much time assembling or maintaining the platform; instead, they can focus on delivering applications efficiently.
* **Kubernetes:** Infinite customizability with a toolbox mentality for building platforms. Kubernetes is built on the philosophy that developers and operators should have the ability to customize every detail of the platform and control over their applications and infrastructure, even if that means greater complexity and more low-level platform building.

For your platform, let’s look at some example principles that can form your platform ethos. These are five principles that map to most platform teams:

1. **Developer experience first:** A fast, easy way to get apps to production. Remove friction through self-service and automation, and integration with developer tools and workflows.
2. **Ship now, customize when needed:** Production-ready from Day 1. Begin with enterprise-grade defaults, then configure and extend as your needs evolve.
3. **Security and compliance as a feature:** Make the right path the easy path. Embed compliance and security into platform primitives. Replace approval meetings with automated policy enforcement.
4. **Observable by default:** Built-in logging, monitoring and debugging from Day 1. When things break, provide clear paths to resolution.
5. **Reliable by default:** Enterprise-grade from the start. Built-in stability at every layer and ready to scale.

Brand and ethos are two faces of the same thing: They define what your platform “stands for” and give the people who use it (developers and operators) some shared identity. For example, developers who use the platform are known for getting ideas to production quickly while keeping their apps compliant and secure. Operations people who work on the platform are known for reliability in production while still catering to developer needs.

You should also think about how brand and ethos are part of the platform itself, a tool that helps guide and reinforce how it’s used. For example, most platform branding we’ve encountered drives the idea that the platform is used for fast-evolving applications, shipping apps frequently. The self-service (no tickets needed!) aspects of a platform embody this ethos. Providing default project templates and automating security and compliance checks also embody this ethos. You want the ethos to match up to the things your platform does for developers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/01/a4afb134-cropped-2f47e82b-michael-cote-e1674132550806.png)

Michael Coté studies how large organizations get better at building software to run better and grow their business. His books "Changing Mindsets," "Monolithic Transformation" and "The Business Bottleneck" cover these topics. He’s been an industry analyst at RedMonk and 451...

Read more from Michael Coté](https://thenewstack.io/author/cote/)

[![](https://cdn.thenewstack.io/media/2023/01/1815de83-cropped-60bb08d8-rita-manachi-e1672939182784.jpg)

Rita Manachi is a marketing and communications pro with decades of experience in high tech. She is a marketing manager at VMware Tanzu.

Read more from Rita Manachi](https://thenewstack.io/author/rita-manachi/)