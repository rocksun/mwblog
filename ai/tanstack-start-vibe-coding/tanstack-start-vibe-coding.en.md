It’s no secret that it’s gotten significantly easier to build applications in the last few years. And [vibe coding](https://thenewstack.io/vibe-coding-agentic-engineering/) is only making it easier and easier. But how exactly would someone build a full-stack application with file-based routing systems, server functions, streaming SSR, and type-safe handling if they don’t even know full-stack applications need those elements?

Welcome to [TanStack Start](https://tanstack.com/start/latest). TanStack isn’t the only full stack framework of its kind, but it’s definitely one of the easiest for beginners. Unlike [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/) or [Remix](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/), which also offer server-side rendering and full-stack capabilities, TanStack Start emphasizes type-safe routing, server functions, and minimal boilerplate. That makes it easier to get a working app quickly without configuring multiple tools.

TanStack Start is designed for developers who want the power of a full-stack framework without the overhead of heavy configuration or sacrificing type safety. Or, now in the case of this tutorial, build for those newer developers who don’t fully understand what a full-stack application needs but still want to make something cool.

*TanStack Start uses Typescript.*

What makes TanStack Start good to vibe code with?

* **Type-Safe by Default**: Unlike some other frameworks, TanStack Start ensures your routes, server functions, and data fetching are fully typed, reducing runtime errors. This is great for vibe coding because you can move fast without worrying about breaking your app while experimenting.
* **File-Based Routing**: Adding new pages is as simple as creating a new file. There’s no need to configure complex routing manually. For vibe coding, this means you can spin up new ideas instantly and see them in the browser without setup headaches.
* **Server Functions**: You can run secure server-side logic directly in your app without creating separate APIs. This lets you vibe code full-stack features quickly, without stopping to build an external backend.
* **Streaming SSR**: Your pages render faster because TanStack Start can stream content from the server to the client efficiently. For vibe coding, this ensures your prototypes feel smooth and responsive even as you add more features.
* **Flexible & Lightweight**: While similar in spirit to Next.js, TanStack Start is smaller, easier to customize, and tightly integrated with the TanStack ecosystem. This allows you to vibe code without fighting the framework, giving you creative freedom to build what you want.

All you need is [Node.js](http://node.js) and npm installed. We’ll install TanStack Start in the project itself.

Let’s review the TanStack Start basics together so you’re comfortable building applications on top of this framework.

## TanStack Start foundation

These are the basic principles TanStack Start was built on.

* **The root**: Think of this as the “parent” of every page. In TanStack`root.tsx`is the global wrapper. It stays on the screen no matter which page you navigate to. This is where you put your navigation bars, footers, and global styles so you don’t have to rewrite them for every page.
* **The index**: Commonly known as`index.tsx`is the default entry point. Think of this as the homepage. It loads automatically whenever someone visits your site.
* **The pages**: These are your about, product, contact, etc pages. They’re made from individual route files that TanStack Start turns into clickable links and browser addresses. With TanStack Start, rather than writing complex routing tables, you can add a file and TanStack Start provides all the boilerplate code needed for the page to get automatically added to your site.

## Create a new TanStack Start App

In your project terminal, you can create a new app with the following code:

```

npm create @tanstack/start@latest
```

Then a few prompts will appear. Here’s how you can answer:

* **Project name**: name your project
* **Toolchain**: ESLint
* **Would you like demo pages?** No
* **Add-ons?** None

Then we’re ready to install dependences

```

cd your project name
npm install
```

## Start the Development Server

The next step is to run the dev server. This may seem like we’re doing this pretty early in the process, and it is. But this is the benefit of working with TanStack Start. Your application already has all the nuts and bolts installed. We’re ready to run right after installation.

```

npm run dev
```

Navigate your browser to`http://localhost:3000`and you’ll see the TanStack Start default page.

Once you confirm your setup worked correctly by seeing the boilerplate app in your browser, let’s go back to the IDE’s file tree so we can see exactly what we’re working with.

Your project structure should look like this:

```

src/
├── routes/
│   ├── __root.tsx
│   └── index.tsx
├── components/
├── routeTree.gen.ts
├── router.tsx
├── vite.config.ts
└── package.json
```

`__root.tsx`

You can find this file in`src/routes/__root.tsx`.

Understanding the root layout helps you see how individual pages fit into the overall app structure. This is the foundation of your app. It sets up the HTML structure, loads necessary scripts, and provides a consistent wrapper for every page. Without it, your pages wouldn’t display properly, your JavaScript wouldn’t run, and shared elements like headers or footers would be hard to manage.

This file wraps all your pages. The key pieces are:

* `<Outlet />` – renders the current page (e.g., `index.tsx`)
* `<HeadContent />` – manages `<title>` and `<meta>`
* `<Scripts />` – injects JS so the page is interactive

Here’s the TanStack Start boilerplate code:

```

import { HeadContent, Scripts, Outlet, createRootRoute } from '@tanstack/react-router'

export const Route = createRootRoute({
  component: RootComponent,
})

function RootComponent() {
  return (
      
      
        
        
        
      
    
  )
}
```

## `index.tsx`

This is your application’s home page. It’s the first impression your users get. This is a great place to start vibe coding because you can see code additions and changes almost immediately. There’s no limit to what you can build with TanStack Start. All the boilerplate is just a starting point.

Some important parts to take note of:

* `createFileRoute('/')`maps this file to the URL /, so this component displays when users visit your home page.
* `HomePage`is the React component shown for this route.

Here’s the boilerplate:

```

import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  component: HomePage,
})

function HomePage() {
  return
```

# Welcome to TanStack Start!

}

## `src/routes/about.tsx`

Here’s where you can customize as well. The`src/routes`folder already has an additional page. `about.tsx` included. If you navigate your browser to`http://localhost:3000/about`you’ll see the boiler plate about page.

Here’s my favorite part about TanStack Start. If you want to add a new page, all you have to do is copy/paste the same boilerplate code into a new file in the routes folder. This is also where vibe coding makes this even easier.

The boilerplate provided for the `about` page looks like this:

```

import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/about')({
  component: AboutPage,
})

function AboutPage() {
  return
```

# About This App

}

It’s very easy to add a new page. We’ll make a contact page in this next example. First, add a`contact.tsx`file into the routes folder. I used AI to help me. I pasted the `about.tsx` file into an AI tool and asked it to turn this into a contact page. It returned the following code to get my contact page started:

```

import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/contact')({
  component: ContactPage,
})

function ContactPage() {
  return (
```

# Contact Us

) }

There’s a lot more to explore with TanStack Start but these are the main foundational building blocks. The most important takeaway from this tutorial is how easy it is to get a working prototype on the web. TanStack Start helps you vibe code live applications without having to think about architecture, routing, or any of the other elements that could trip you up and keep you from focusing on the more exciting business logic.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)