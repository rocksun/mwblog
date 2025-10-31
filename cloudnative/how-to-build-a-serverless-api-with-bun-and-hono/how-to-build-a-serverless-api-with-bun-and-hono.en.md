There was a time when Node.js was the go-to runtime for JavaScript. For better and sometimes for worse, if you wanted to build a JavaScript application, you were using Node.js for the backend. Because of habit and the huge number of tools, libraries and frameworks that support Node.js, it remains a widely used choice. But in recent years, new runtimes have appeared to address some of the challenges developers face with Node.js.

One of these new backend runtimes is Bun, introduced in 2021. Bun’s elevator pitch is that it is “like Node.js but designed for speed, modern workflows and with fewer tools to install,” which addresses many of the frustrations developers have had with [Node.js](http://node.js). This is important because the web in 2025 looks a lot different than it did when [Node.js](http://node.js) was first created in 2009.

[Hono was created in December 2021](https://thenewstack.io/hono-shows-the-way-for-microframeworks-in-a-post-react-world/) by Japanese developer Yusuke Wada. According to its GitHub repository, Hono is “a small, simple and ultrafast web framework built on Web Standards.” It was originally built for Cloudflare Workers, but now works “on any JavaScript runtime,” including Node.js, Deno, Bun and Vercel (although Node support requires an adapter and Node ≥ 18).

## Why Build an API with Bun and Hono?

Before we dive into building a serverless API, let’s look at some similar tools now that the marketplace is more competitive.

### The Classic: [Node.js](http://node.js) and Express

This is a heavier — more boilerplate, slower startup times and larger memory footprint — architecture than Bun and Hono.

### The Competitor: Deno and Oak

Of all the options out there, Deno and Oak are the closest to Bun and Hono. Deno is a modern runtime — secure defaults, built-in tooling, performance optimizations — with first-class TypeScript support, designed with security and developer-friendly defaults in mind.

So why would you want to build an app with Bun and Hono?

Even in a more competitive marketplace, there are clear benefits to this combination. First, there’s speed. Bun was built specifically for performance, making API responses extremely fast. Then there’s simplicity. The setup is minimal, letting you focus on logic instead of configuration. This architecture is also TypeScript-ready, making type-safe development easier. On top of that, it’s serverless-friendly, with templates for Cloudflare, AWS Lambda and other platforms.

Let’s take it for a test drive.

We’re going to build a simple serverless API that:

* Receives two numbers from the browser;
* Calculates the sum;
* Stores results in memory and in the application.

## Prerequisites for This Tutorial

Before starting, you should have the following installed on your machine:

## Setting Up Your Bun and Hono Project

We have some installs and basic setup to handle before we start our build. In a new terminal window in a new project in your IDE, let’s install Bun and initialize a new Hono project.

First, we need to install Bun.

```
bun install
```

After a successful install, we’re ready to initialize the Hono project.

```
bun create hono hono-api
cd hono-api
```

This is where you can see all the templates Hono offers. We’re going to select the “bun” template followed by a “Y” for project dependencies, and the Bun package manager.

For this project, we’re only going to need two files:

* `src/index.ts` — This is part of the package we just installed. This page will be our API backend.
* `test.html` — You’ll have to add this page in the `hono-api` file. This is our browser interface.

## Building `index.ts`

All the following code blocks can be added to the same file in this same order. I broke it down to do a deep dive into the functionality of our serverless API.

### Imports and Initialization

CORS is the middleware we’ll use. This allows the API to be accessed from a browser, preventing cross-origin issues.

```
import { Hono } from 'hono'
import { cors } from 'hono/cors'


const app = new Hono()
```

Next, let’s enable CORS. The code below will apply CORS to all routes.

```
app.use('*', cors())
```

The next thing we’re going to do is create the in-memory storage. When we submit numbers from the browser, this code will allow a results array to also appear in the terminal. Even though we’re saving them in the terminal, they’re still temporary and will clear when you restart the server.

```
const results: { a: number; b: number; sum: number }[] = []
```

### Building the Routes

The first route we’re going to add is our root route. This is a basic GET for the `/` endpoint.

```
app.get('/', (c) => c.text('Hello, world!'))
```

The next route will be another GET route, this time with a URL parameter. You can use this to test functionality by adding a word to the end of the URL in your browser. The word will appear in the browser’s page.

```
app.get('/api/greet/:name', (c) => {
  const name = c.req.param('name')
  return c.json({ message: `Hello, ${name}!` })
})
```

We’re now ready to add our POST route `/api/sum`.

This code will receive two numbers from the browser, validate their type, calculate the sum, then store it in the `results` array. It will log the memory contents in the terminal. This code returns the sum in JSON.

```
app.post('/api/sum', async (c) => {
  try {
    const { a, b } = await c.req.json()
    if (typeof a !== 'number' || typeof b !== 'number') {
      return c.json({ error: 'Both a and b must be numbers.' }, 400)
    }


    const sum = a + b
    results.push({ a, b, sum }) // store in memory
    console.log('Stored sums:', results) // debug log to terminal
    return c.json({ sum })
  } catch (err) {
    return c.json({ error: 'Invalid JSON body.' }, 400)
  }
})
```

The last route we’re going to build is a GET route, `/api/sum`.

This will send the code to the browser as JSON.

```
app.get('/api/sum', (c) => {
  return c.json(results)
})
```

The last step is to export the app.

```
export default app
```

Here is the code in one copy/paste option:

```
import { Hono } from 'hono'
import { cors } from 'hono/cors'


const app = new Hono()


app.use('*', cors())


// STORAGE
const results: { a: number; b: number; sum: number }[] = []


// ROOT
app.get('/', (c) => c.text('Hello, world!'))


// GET
app.get('/api/greet/:name', (c) => {
  const name = c.req.param('name')
  return c.json({ message: `Hello, ${name}!` })
})


// POST
app.post('/api/sum', async (c) => {
  try {
    const { a, b } = await c.req.json()
    if (typeof a !== 'number' || typeof b !== 'number') {
      return c.json({ error: 'Both a and b must be numbers.' }, 400)
    }


    const sum = a + b
    results.push({ a, b, sum }) // store in memory
    console.log('Stored sums:', results) // debug log to terminal
    return c.json({ sum })
  } catch (err) {
    return c.json({ error: 'Invalid JSON body.' }, 400)
  }
})


// GET
app.get('/api/sum', (c) => {
  return c.json(results)
})






// Export
export default app
```

## Building `test.html`

`test.html` is a simple web interface that connects the frontend to the backend. Since it’s basic HTML, we are not going to go over it in depth. This is where you can enter two numbers and add them together, and the sum will be displayed on the page. It also logs the stored results in your terminal.

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Test Sum API</title>
</head>
<body>
  <h1>Sum API Test</h1>
  <input id="num1" type="number" placeholder="Enter first number" />
  <input id="num2" type="number" placeholder="Enter second number" />
  <button onclick="callSum()">Calculate Sum</button>
  <p id="result"></p>


  <script>
    async function callSum() {
      const a = Number(document.getElementById('num1').value)
      const b = Number(document.getElementById('num2').value)


      const response = await fetch('http://localhost:3000/api/sum', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a, b })
      })


      const data = await response.json()
      document.getElementById('result').innerText = JSON.stringify(data)
    }
  </script>
</body>
</html>
```

## How to Run Your Serverless Application

Once your build is complete, you can run the app with the command `bun run src/index.ts`.

You can open the `test.html` file manually in your browser by double-clicking it in your project folder (on a Mac, I found it using Finder).

The browser will look like this:

[![](https://cdn.thenewstack.io/media/2025/10/8d376771-sum3-1024x280.png)](https://cdn.thenewstack.io/media/2025/10/8d376771-sum3-1024x280.png)

And each time you hit “Calculate Sum,” your terminal will update with something that looks like this:

[![](https://cdn.thenewstack.io/media/2025/10/75da9cc6-terminal-resize.png)](https://cdn.thenewstack.io/media/2025/10/75da9cc6-terminal-resize.png)

And that’s it! You now have a working serverless sum API with a simple web interface.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)