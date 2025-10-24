NEW YORK — [Laurie Lay](https://www.linkedin.com/in/laurie-lay/), senior software engineer at Ippon Technologies, has some good news for JavaScript developers: You don’t have to master [Python](https://thenewstack.io/what-is-python/) for [machine learning](https://thenewstack.io/javascript-library-runs-machine-learning-models-in-browser/) (ML). While Python obviously dominates in that field, using JavaScript with ML will offer [frontend developers](https://roadmap.sh/frontend) new ways to enhance an application’s functions with AI on devices, she said.

Lay explained what [JavaScript](https://thenewstack.io/introduction-to-javascript/) and [Node.js](https://thenewstack.io/a-backend-for-frontend-watt-for-node-js-simplifies-operations/) bring to the new frontier of AI at the [devmio International JavaScript Conference](https://javascript-conference.com/new-york/) held Sept. 30-Oct. 1 in Brooklyn.

## Why Python is King of ML

Python has thus far been the language for performing machine learning tasks, but there’s nothing innate about the syntax of Python that led it to become the top language for machine learning, according to Lay.

“For the past decade, any serious discussion about machine learning has always been linked to the Python programming language, and this dominance wasn’t by accident, nor was it because Python is exceptionally fast language,” she said. “The true reason is because Python became a high-level glue language for a large majority of other libraries.”

The heavy lifting in machine learning is not performed by the Python code itself, but is handled by foundational libraries like [NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) for numerical computing and [Pandas](https://thenewstack.io/pandas-a-vital-python-tool-for-data-scientists/) for data manipulation, she said. These libraries are actually sophisticated Python wrappers around highly optimized, low-level code written in C and Fortran, she continued.

[![Fullstack developer Laurie Lay talks about using JavaScript for machine learning.](https://cdn.thenewstack.io/media/2025/10/ed5b3406-laurie_lay_presentation.jpg)](https://cdn.thenewstack.io/media/2025/10/ed5b3406-laurie_lay_presentation.jpg)

Laurie Lay presents on JavaScript and machine learning. Photo by Loraine Lawson.

“It’s this architecture that allowed scientists and researchers to work with a simple, readable syntax in Python, while also harnessing that raw computational speed of C for those intensive mathematical operations,” she said. “This combination of ease and high performance boosted the machine learning development.”

It didn’t hurt that Python had early, substantial investment from companies such as Google, which backed the development of [TensorFlow](https://thenewstack.io/python-tutorial-use-tensorflow-to-generate-predictive-text/) and [hired Python’s creator Guido van Rossum](https://www.forbes.com/sites/tomiogeron/2012/12/07/dropbox-snags-google-exec-and-python-god-guido-van-rossum/), she said.

“Money, ease of use and a strong community helped solidify Python’s position to produce this rich ecosystem, tools, frameworks and high-quality documentation,” she said.

## If Not Python, Then JavaScript?

So the barrier to entry really isn’t about Python syntax, but about “replicating this massive, battle-tested, low-level scientific computing ecosystem,” she said. Python dominates in offline model training, but the landscape is shifting significantly now.

“The idea of performing serious machine learning in JavaScript is now actually a practical reality because it’s driven by a number of technological advancements,” she said.

First, there’s the speed of JavaScript engines, such as [Google V8](https://v8.dev/), which have increased dramatically with techniques like just-in-time compilation, which executes JavaScript at speeds once unimaginable for an interpreted language, she explained. Second, Node.js provides a robust, scalable server-side environment, which frees JavaScript from the confines of the browser.

There’s also the npm ecosystem, which has created the world’s largest software registry. The ecosystem encourages a culture of open collaboration and makes it easier to share and build upon complex tools, Lay said.

The npm ecosystem now includes a number of dedicated machine learning libraries that give developers the necessary tools to build and train models in JavaScript. But there’s an even more significant shift that’s taken place since Python became the ML champion, she said.

“Probably the most influential shift has been in the continuous improvement of hardware on the modern client devices, from laptops to the phones in your pockets, which now possess that computational power to actually run these sophisticated machine learning models locally,” Lay said. “And this has been the game changer for everything.”

## JavaScript for Machine Learning

The goal isn’t to replace Python, Lay cautioned. It’s about enabling machine learning on the client with JavaScript.

“It’s about bringing machine learning into the environments where JavaScript is the native language, namely in the web browser,” she said. “This opens up a new class of applications that are really difficult or impossible to achieve with a traditional, server-centric architecture. “

> “It’s about bringing machine learning into the environments where JavaScript is the native language, namely in the web browser …”  
> **– Laurie Lay, senior software engineer at Ippon Technologies**

Running machine learning models on the client side unlocks a number of features that were not possible before, Lay continued.

A traditional cloud-based AI model requires users to send their private information and data — including photos, private messages or medical information — to a third-party server for processing, she said. This creates inherent privacy and security risks. But on a device, machine learning with JavaScript can reduce those risks.

“When learning models run directly in the user’s device, the data never has to leave it, and it stays private and secure,” she said. “This is really important for applications handling sensitive information, like healthcare, finance, our enterprise applications. We can also see that by eliminating the dependency on network connectivity, our applications are faster and more reliable, and also predictions can be more instantaneous, because the application can even function offline.”

Models can also be fine-tuned and customized for each individual user on their own device, she added.

“Product recommendation models, for example, could adapt to a user’s unique style or clothing by looking at their images and never having to have them send their private images to a separate server,” Lay said.

## The Node Advantage

Node.js also offers advantages for the machine learning architecture, according to Lay.

The backend logic powered by Node lives in one world, while the complex number-crunching machine learning models that are almost exclusively written in Python live in another world, she pointed out.

To make them talk, developers had to build a separate Python microservice, wrap it in a [Flask](https://thenewstack.io/how-to-use-flask-a-lightweight-python-framework/) API — Flask is a lightweight, minimal Python web framework also used to build APIs — and then make network calls from the Node app. It’s slow and complex to deploy, and also introduces another point of failure, she added.

“The power of Node is that it is built on this event driven, non-blocking I/O model powered by Chrome’s V8. This makes Node really good at handling tons of simultaneous web requests, and by adding machine learning functionality directly into the JavaScript code and your Node server, then you can have an ideal platform for serving predictions from an already trained machine learning model,” Lay said.

Node is ideal for building those, real-time applications for things like intelligent chatbots, enabling it to handle thousands of simultaneous conversations or to process real-time data from connected devices, she added. This enables the creation of functions such as a home assistant that can adjust the thermostat based on people or pets in a room or a live recommendation engine to serve personalized recommendations to a large user base with minimal latency.

## Why Machine Learning Needs JavaScript and Python

“One of the main things that I want to make sure comes out of this talk, though, is that it’s not a choice between Python or JavaScript,” Lay said. “It’s not always one over the other. It’s about leveraging the strengths of each of those ecosystems for your machine learning applications.”

Python still excels when developers need computationally intense model training, she said. JavaScript works best for serving real-time, scalable APIs with Node and the client side. It also supports additional security and device-specific operations for applications.

> “It’s an evolution of the web platform that’s happening right now, and as developers, we have the ability to build the new generation of these intelligent applications.”  
> **– Laurie Lay**

It’s possible to even take a hybrid approach, where a developer trains a model in Python to optimize a complex machine learning model. The model could be saved as JSON; and in Node, the coder could use a library like TensorFlow that would load the pre-trained model into memory. Then the developer could expose an API endpoint, and the client applications could call and get predictions from that pre-trained model, she explained.

“This approach combines the power and maturity of the Python training environment with that super-fast, multiple-request performance of Node and the robust, scalable architecture for deploying machine learning models here,” she said.

Don’t think that machine learning in the JavaScript ecosystem is a “a fleeting trend,” she added.

“It’s an evolution of the web platform that’s happening right now, and as developers, we have the ability to build the new generation of these intelligent applications,” Lay said. “Many of our apps that are already built with JavaScript have the ability to keep application data localized, private and real time. This makes JavaScript a really perfect language for deploying machine learning models on our small, resource-constrained local devices.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)