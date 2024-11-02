# Platform Engineering’s Most Critical First Decision
![Featued image for: Platform Engineering’s Most Critical First Decision](https://cdn.thenewstack.io/media/2024/10/75c83f97-getty-images-nfv7cca-vwy-unsplash-1024x683.jpg)
Building a [platform engineering](https://thenewstack.io/platform-engineering/) platform for your company is a big task, with lots of critical decisions that must be made. But perhaps the most important decision that must be tackled first is deciding where to start building the platform — from the frontend or from its backend.

Why is this so critical?

Because for a platform engineering platform to work well and be successful, it needs to be built around a well-designed backend utilizing solid business logic that allows it to best serve the developers who will use it, [Luca Galante](https://www.linkedin.com/in/luca-galante/), a core contributor to the global developer’s community [PlatformEngineering.org](https://platformengineering.org/), told The New Stack. By starting with the backend and that critical business logic, the platform can then be used with any kind of graphical user interface (GUI), a code-based interface, or with a [command line interface (CLI)](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/), he said.

“What you want is a very solid core as a backend and then you can plug and play different interfaces for different users and for different levels of abstractions that you want to provide to them,” he said. “You cannot really build business logic into a frontend. The frontend is just designed to visualize stuff, to give you a nice developer experience. It is not designed to let you define how to how developers interact with the underlying infrastructure, or how they configure things in detail. It does not let you layer on top a [role-based access control](https://thenewstack.io/3-frameworks-for-role-based-access-control/).”

And that [business logic](https://thenewstack.io/web-developers-not-moving-more-business-logic-to-the-client/) is important because it creates that powerful foundation and code for everything that will follow as the platform — which is also called an [internal developer platform](https://thenewstack.io/internal-developer-platform-vs-internal-developer-portal-whats-up/) or IDP — is engineered and built, he said.

“If you start with the portal first, you do not have any of that flexibility, because the developer experience is constrained,” said Galante, who is also the vice president of product and growth for platform engineering vendor, [Humanitec](https://humanitec.com/). “It needs to be the same across different teams, across different workflows, which does not scale in the enterprise and puts you back to square one to rethink this from the ground up.”

These are not new concepts, he added. “Building a platform is like building any other application,” said Galante. “Nobody builds applications frontend first. That is just not practice.”

## Origins of the ‘Frontend vs. Backend First’ Argument
So, with all these sensible arguments for starting with the backend due to its robust built-in business logic, why do some nascent platform engineering teams continue to try designing their company’s IDPs beginning with the frontend in the first place?

In those cases, said Galante, it is often due to motivations from the platform’s administrative team to build something that will instantly show some kind of early success to company executives who have mandated the creation of a platform engineering infrastructure and provided the funding.

“I think that the majority of them [perform a [Google](https://cloud.google.com/?utm_content=inline+mention) search on] platform engineering and find that there are backend tools and frontend tools, like [Backstage](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/) and other portals,” he said. “Then they conclude that they can implement a portal and show that pretty user interface in just a few weeks, and then their dashboard is done. So, they get an early win, and it does work to an extent.”

But problems surface later, however, as the executives release more budget dollars and order the admin team to go and build the rest of the platform, said Galante.

“Then they see that they need to now build the needed business logic into the platform,” he said. “They think that they are going to try and shoehorn it in somehow into this frontend layer that they already built, but that is where things hit the fan. That is where things start breaking.”

## Learning From These Failures
But don’t listen to him, says Galante. Instead, he says, IDP planners should learn from the lessons and mistakes suffered by the platform admins who have tried unsuccessfully to follow this frontend-first approach in the past.

“The issue is in the configuration and the orchestration of the infrastructure,” said Galante. “So, ultimately, what you need is to have a North Star to orient you as a platform team, and where you solve that is in the backend of the platform.”

One of the best places to learn about this is from more experienced platform engineers who are now building their second, third, or later platforms, he said. “Those people who did those early tried and then they usually became head of platforms or vice president of platforms at a new enterprise a few years later. And now they are like, ‘no way I am doing the same mistakes again.’”

Many of those early IDP administrators and designers may also now be looking to start with a pre-built platform from a platform engineering vendor the next time so they do not have to go through the massive and difficult task of building one themselves again from scratch, said Galante.

## Why Platform Engineering – From the Backend – Is Worth the Effort for Enterprises
Despite all the pains of going through this process, more companies today are finding that IDPs are worth their planning, creation, implementation, and upkeep, said Galante. Platform engineering empowers software developers and accelerates operational efficiencies inside enterprises by [allowing IT systems administrators to choose and assemble proven, curated and regularly maintained development applications](https://thenewstack.io/platform-engineering-it-is-all-about-the-tooling/), which can then be delivered to a company’s developers via an all-in-one self-service portal.

These platforms allow developers to do their core work activities rather than spending valuable time searching for applications they need to create and test their code. These IDPs provide developers with the code-building tools they require in an accessible, easy-to-use environment built to provide automation, standardization and flexibility.

The time spent bringing it all together is worth the immense effort that it will take, added Galante.

“With platform engineering — and this is really important — it is probably not a once-and-done three-month project,” said Galante. “That is how you will fail as a platform engineer.”

Instead, platform engineering is about building something that is “usually really starting to pay off in six to 12 to 18 months down the line, with huge economies of scale after that,” said Galante. “And so, it is very important that, as a team, you attach your long-term objectives to this long-term vision of your platform. And this is why we are going to do it the right way and why we are going to start from the back end and really fix the problems that matter.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)