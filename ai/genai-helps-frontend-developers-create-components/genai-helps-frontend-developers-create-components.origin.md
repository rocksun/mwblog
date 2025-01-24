# GenAI Helps Frontend Developers Create Components
![Featued image for: GenAI Helps Frontend Developers Create Components](https://cdn.thenewstack.io/media/2025/01/674ff385-frontendwebdevelopment-1024x683.jpg)
When developer and attorney [Julia Machado](https://www.linkedin.com/in/juliamachado/?locale=en_US) developed websites for WordPress, she found an ecosystem of plug-ins for the open source PHP-based content management system, but when she tried to find the same in the JavaScript world, there just wasn’t anything similar.

She wanted to apply the microfrontend approach — which architects web applications by breaking them down into smaller, independent components — to JavaScript web development.

So Machado started [WebCrumbs](https://github.com/webcrumbs-community/webcrumbs), an open source solution for creating components for the JavaScript community. It allows you to create components and plugins that are compatible with frameworks such as React and Angular, as well as plugins that are in CSS/Tailwind and HTML. The results are open source.

Webcrumb’s goal is to create “an industry-standard solution for modern web development, creating the first open ecosystem of plugins for the JavaScript community and related frameworks (like React, Nextjs, Vue, Svelte, and others).”

That’s an interesting project in its own right, but what’s getting more attention these days is [Frontend AI](https://tools.webcrumbs.org/frontend-ai), an off-shoot of the original Webcrumbs.

## Frontend AI
Frontend AI is a generative AI model that creates the plugin or template for developers, exporting the code as CSS/[Tailwind](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/), HTML, [React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/), [Angular](https://thenewstack.io/angular-shares-potential-ideas-for-2025-improvements/), [Svelte](https://thenewstack.io/youll-write-less-code-with-svelte-5-0-promises-rich-harris/) or [Next.js](https://thenewstack.io/next-js-canary-supports-partial-pre-rendering-for-faster-sites/). It also incorporates a code editor and visual studio, making it easy for developers to customize the components it creates.

Machado’s team launched version 3 of Frontend AI last week. It was first released in a silent launch back in May, beginning as a team tool for learning how to build components.

Frontend AI is not trying to compete with offerings such as [Vercel’s v0 Gen AI chat](https://v0.dev/), which Machado categorized as more focused on creating full sites.

[One reviewer described it this way](https://hackernoon.com/should-you-try-v0-webcrumbs-or-both): v0 generates React code that is compatible with Shadcn UI and Tailwind CSS, “making it perfect for developers who want to build modern, beautiful UIs.”
“At its core, Webcrumbs uses artificial intelligence to generate code components directly from images or text descriptions,” the writer, [Mr. Ånand](https://hackernoon.com/u/astrodevil), wrote. “You can describe any UI element, or even upload a visual reference, and Webcrumbs instantly transforms that into React, Vue, Svelte, or even HTML.”

Unlike Vercel v0, Frontend AI is focused on creating plugins and the code for microfrontends, Machado explained to The New Stack. Developers can create a component with a natural language description or an image, she explained.

“The first thing you notice is we are much faster — […] you click submit, it generates the request,” Machado said. “The other thing is that once you [are] finished, you do not have to ask AI [about] every little single change you’re making.”

![A screenshot of a Frontend AI component -- in this case a blog -- that creates the code, which the picture displays in the pop-up code editor.](https://cdn.thenewstack.io/media/2025/01/897c59ed-frontendai.png)
A screenshot from Frontend AI.

The goal is eventually to create a full-stack solution. She also intends to merge Webcrumbs and Frontend AI at some point down the road, she told The New Stack. But for now, Frontend AI is focused on… well, the frontend end.

Technically, you can ask Frontend AI to create a whole website [— making it a bit of a low-code option](https://thenewstack.io/terraform-cloud-now-offers-less-code-and-no-code-options/) — but that’s not the point of it, Machado stressed.

And anyway, where’s the fun in that?

## Working With Templates
Once a component is created, developers have the option to submit it for [open source licensing](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/). There is already a dropdown list of more than 100 templates to help jump-start the process with open source code. At some point, the company may allow developers to sell the templates in a marketplace, Machado said.

The code results are shown in a visual interface that allows developers to tweak the themes, font, color and spacing on any elements Frontend AI generates. That interface is growing as the team adds more customer abilities to modify the tools with drag and drop, Machado said.

“We are not [generating the code](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/) after the design,” Machado said. “We are generating them all together so you never have that problem you have in Figma, for instance, that you generate something and then the code shows you something else.”

Eventually, the components built with Frontend AI will be embeddable with one line of code, she added. Currently, developers can copy the code from the code editor, download the code, or get the PNG.

## Applying Rules to Components
Frontend AI also allows you to create rules that you can write — so for instance, Machado demonstrated applying a rule that applies orange to her components.

There’s also the option to test the component on mobile, tablet and desktop. Sometimes, the components don’t play well with a particular screen size.

![A screenshot showing how Frontend AI auto-detects problems a component might encounter on a particular type of device, and then offers to fix that problem.](https://cdn.thenewstack.io/media/2025/01/c6882626-runthefixfrontendai.png)
Frontend AI can detect problems a component might encounter on a specific device and offers to fix those problems. Screenshot from Frontend AI.

“Another thing we have that [is] new as well is this responsiveness button over here [where] you can see how the component plays — like here you can see it’s not good for mobile,” she said. “It will prompt you, ‘Do you want to fix?’ And then you run the fix and you see the code being regenerated for you, for that type of screen.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)