[Julian Wilkison-Duran](https://www.linkedin.com/in/julianduran/) has created what he calls the Poor Man’s Machine Learning model for the browser.

“What I really want to do is bring that machine learning into the frontend and I don’t believe that models need a billion parameters to be able to do really cool stuff, especially on the frontend,” he said. “What I set out to do is create a new model that didn’t require these huge amounts of parameters and massive amounts of memory to run but [is] still able to do very practical things inside the web browser.”

The result is [AsterMind-ELM](https://github.com/infiniteCrank/AsterMind-ELM), an open source machine learning library written in [JavaScript](https://thenewstack.io/introduction-to-javascript/) and not, he added, a [Python](https://thenewstack.io/new-python-cli-tool-catches-mcp-server-issues-before-agents-do/) library with a JavaScript wrapper. He introduced the open source project at the [devmio International JavaScript Conference](https://devm.io/experiences/the-javascript-community/) held in Brooklyn last week.

Wilkison-Duran, a full-stack software engineer at Ippon Technologies, built AsterMind-ELM to be a modular, Extreme Learning Machine (ELM) library for JavaScript and [TypeScript](https://thenewstack.io/what-is-typescript/). He rewrote the [Extreme Learning Machine (ELM)](https://www.geeksforgeeks.org/machine-learning/extreme-learning-machine/) network in JavaScript for frontend developers to use.

## Understanding ELM

[ELM](https://www.linkedin.com/school/ntusg/) is type of neural network algorithm developed in 2006 by [Guang Bin Huang](https://www.linkedin.com/in/guang-bin-huang-5949a9b3/?originalSubdomain=sg), whose research at the Nanyang Technological University in Singapore focuses on neural networks. ELM is used in machine learning and AI. It’s fast and efficient at training tasks such as classification, regression and clustering.

But in 2006, researchers were trying to solve a problem of balancing the best learning rate for your data set.

“A lot of people have been asking this question everywhere because they don’t want to spend billions of dollars on data centers,” he said.

Huang’s solution was to ask what if we don’t train all of that by creating a hidden layer that’s just completely random and never touched. Would it still work?

“To many engineers, especially in his day, this sounded like shipping production code without running unit tests. It just sounds crazy,” Wilkison-Duran said. “What he did was a simple math trick that we all learned in high school. He said, ‘What if we use the hidden layer as a map?’”

All the magic happens inside the hidden layer, he added. It’s like overlooking a city and trying to give directions — you can’t see the individual streets because the buildings are too tall. But what if you placed a grid on top of the city, Wilkison-Duran said.

“All of sudden, [it’s] kind of like Battleship: So you can say, ‘Oh the bank is in square three, five or the park is in four, three,” he explained.

> “What I figured out is neural networks, that’s all they are is matrix math.”  
> **– Julian Wilkison-Duran, creator of AstroMind ELM**

It gives developers a reference that’s not exact and never will be, but it’s a good enough map of the data to be able to tell where things are, he said.

Now that you have a map how do you figure out how to get from point A to point B. The answer is the [Moore-Penrose inverse](https://www.cantorsparadise.com/demystifying-the-moore-penrose-generalized-inverse-a1b989a1dd49), which is also known as the pseudoinverse.

“This is a simple matrix manipulation that most of us learned in high school and we didn’t really understand why we were learning it; and I didn’t really understand why I was learning matrix math in high school either, until like a year ago,“ Wilkison-Duran said. “What I figured out is neural networks, that’s all they are is [matrix math](https://math.libretexts.org/Bookshelves/Applied_Mathematics/Applied_Finite_Mathematics_(Sekhon_and_Bloom)/02%3A_Matrices/2.01%3A_Introduction_to_Matrices).”

Think of the hidden layer like this: When the data is put into the hidden layer, it acts like a mashed-up piece of paper, Wilkison-Duran explained. Astro-Mind ELM uses the output layer as a GPS for the hidden layer map.

“Say I take a piece of paper and I literally mash it up. It’s really hard for me to tell the sentences on that piece of paper now or even what it says, but if I unfold that piece of paper, all of a sudden it starts to make sense again,” he said.

ELM is used in situations where real-time training speed and computational efficiency are more critical than achieving the absolute highest accuracy. Uses include industrial applications where training speed is critical — such as financial forecasting, social media sentiment analysis, real-time control systems, and complex pattern recognition.

## AstroMind ELM Brings ML to the Browser

Unlike a normal neural network, Astro-Mind ELM doesn’t solve for all of the hidden layers. It only solves for the last layer, so memory consumption, all the settings, decreases significantly, he said.

“Instead of having to train billions of parameters, you’re training just the last layer,” he said.

AstroMind-ELM brings the capabilities of ELM to the browser and makes it available to JavaScript developers.

“I put it into the browser and said what can you do with it now that it’s in the browser?” Wilkison-Duran said. “I’ve taken that technology and that math and all this stuff that makes ELM and rewritten it into JavaScript … in such a way that you can train models instantly and it runs inside the browser without massive amounts of memory.”

He stressed again that AsterMind-ELM was not written in Python and then wrapped in JavaScript, but has been rewritten entirely in JavaScript.

AstroMind-ELM is not designed to handle huge [large language models](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) that generate massive amounts of text, he added. Instead, it’s very specific models that you can create and train on the fly, then chain together like blocks of Legos, he said.

“AsterMind brings instant, tiny, on-device ML to the web,” Wilkison-Duran explained in the GitHub repo. “It lets you ship models that train in milliseconds, predict with microsecond latency, and run entirely in the browser — no GPU, no server, no tracking.”

In addition to ELM, the library now includes kernel ELM.

“In this case, kernel ELMs, they don’t use the grid,” he said. “Instead they use kind of landmarks. If you think about a neighborhood and you’re walking through it, there’s a tree over there and it’s big and I can recognize it. There’s a mailbox over there. What kernel ELMs do is use those landmarks to try to figure out where your data is.”

## Demonstrating AsterMind ELM

He demonstrated training the model live with just 20 sentences. The model then classified the data into world, sports, business and science & technology. It predicted one sentence would belong in science and technology, which was correct. But interestingly, it was correct when it gave the sentence a 48% chance of being science and technology, while the other options were only ranked at 18% and 17%.

“What it did is it classified all that data into world sports, business, and science and tech, and then on the column side, these are all your vectors,” he said. “Vectors don’t mean anything until you give it a name but in this case, the vectors represent sentences and the other thing that I want to point out in this slide is that it’s not big, so the model itself is actually just a [JSON file](https://thenewstack.io/working-with-json-data-in-python/).”

> “AsterMind brings instant, tiny, on-device ML to the web.”  
> **– AstroMind GitHub repository**

He also demonstrated training the model to recognize his voice and distinguish between left and right, then played a game using voice commands to control the action.

“This is going to be a game changer, because everybody is saying, ‘Oh the frontend is DEA (dead on arrival) now. You can just generate that with an LLM [and] it can generate a rich and dynamic UI that you can actually do amazing things with,” he said.“What we actually like to do as JavaScript developers, [is] create amazing widgets, create very awesome visuals.”

He demonstrated training the ELM with a four-on-the-floor drum beat, which is the typical rock drum beat. It quickly generated the beat without waiting for anything to spin up or any backend intervention.

The AstroMind ELM library also allows developers to chain models together and have more than one model running inside the browser at a time. He demoed a few different models from the library.

“The main point is you can build fantastic things with this model,” he said.”You can [train it with very little data](https://thenewstack.io/machine-learning-for-real-time-data-analysis-training-models-in-production/). You can even use synthetic data to train it initially.”

ELM also doesn’t require you to keep the data. Once it is trained, the data can be thrown away to free up memory.

As for the context window — which can be an issue with LLMs — the limit is within the hidden layer and the memory limits of JavaScript itself, he said.

“I have done extensive experiments on this, and I could get up to 1,000 parameters using a web worker and online learning,” he said. “What that means is, like, I could have 1,000 parameters, but it’s in a web worker, and I stream the training data so that it doesn’t take up all the memory at one time.”

## What Can You Build With It?

The repo explains that with the AstroMind ELM library components, such as Kernel ELMS, Online ELM, DeepELM and Web Worker offloading, developers can create:

* Private, on-device classifiers for language, intent, toxicity or spam, for example, that retrain on user feedback;
* Real-time retrieval and reranking with compact embeddings for search and RAG;
* Interactive creative tools such as drum generators and autocompletes that respond instantly;
* Edge analytics: Regressors/classifiers from data that never leaves the page; and
* Deep ELM chains for powerful pipeline that are still tiny and transparent.

Wilkinson-Duran hopes to build a community around the open source project. He said those who want to participate at this point can do a pull request, which he’ll review. One outcome he wants is to build an ecosystem of weights that developers could share.

“What I really want is for people to be able to improve these models, so I made it open source so that everybody can dig in, help me figure out how to make these even more powerful than what they already are,” he said. “What I’m getting at is, it doesn’t take much. You can feed it whatever data you want, train it instantly, and who cares if it doesn’t work right away, because you didn’t spend billions of dollars on it like LLMs. You use what you have and you train with what you got.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)