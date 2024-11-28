# Why Developers Should Try Predictive AI
![Featued image for: Why Developers Should Try Predictive AI](https://cdn.thenewstack.io/media/2024/11/3444767d-ai_motherboard-1024x630.jpg)
Everyone’s experimenting with [generative artificial intelligence (Gen AI)](https://thenewstack.io/gen-ais-iphone-moment-what-it-means-for-developers/), but developers should consider incorporating other forms of machine learning into their applications, according to [Rita Kozlov](https://www.linkedin.com/in/ritakozlov/), vice president of product for Cloudflare’s developer platform and AI.

“Everyone is experimenting, and I think that gives a sense that there’s more happening in production, in really meaty use cases, than there actually are,” Kozlov said. “What we are seeing is there are a lot of chatbots that are being thrown into the forefront of the user experience.”

## Alternatives to AI Chatbots
That’s not necessarily the right approach, she added. Pushing [chatbots](https://thenewstack.io/ai-beyond-chatbots-and-assistants-adaptive-applications/) just to use Generative AI can make it seem like the company is “just checking the AI checkbox” without concern about whether it’s actually helpful to users, she said.

Predictive AI is another option developers should explore, she suggested. Predictive AI uses [machine learning algorithms](https://thenewstack.io/machine-learning-algorithm-sidesteps-the-scientific-method/) to identify patterns in past events and make predictions about future events. It’s used for tasks such as fraud detection, credit risk assessment, demand forecasting, and even disease diagnosis.

For instance, a calendar [app could use machine learning](https://thenewstack.io/create-machine-learning-apps-in-your-notebook-with-tecton/) to help someone find available appointment times.

“You don’t necessarily need to lean into generative AI for that,” Kozlov said, adding, “Obviously, there are a lot of use cases where generative AI is extremely useful to people today.”

Predictive AI relies on [inference AI](https://thenewstack.io/when-cloud-meets-intelligence-inference-ai-as-a-service/), which is the specific act of using a trained model to generate predictions on new data. It actually requires fewer resources to run inference AI than it does to run training workloads, she said.

Cloudflare’s [Workers AI](https://developers.cloudflare.com/workers-ai/) manages the backend and gives developers access to serverless AI inference via APIs. The platform also provides [access to a variety of open source models](https://developers.cloudflare.com/workers-ai/models/), she added.

## Wider Adoption of Smaller Models
Another trend Kozlov has noticed is that organizations should deploy smaller models trained on fewer parameters rather than leverage the largest model possible.

“People realized, great, there are models that have 400 billion parameters, but you can’t run them practically. They are way too expensive,” she said. “We’re also seeing a shift back towards smaller models.”

What developers are finding is that it’s easy enough to use a popular GenAI provider that offers only a few models by using the [AI’s API](https://thenewstack.io/the-future-of-apis-lessons-in-security-composability-ai/).

“People realized, great, there are models that are 400 billion parameters that exist, but you can’t run them practically. They are way too expensive.”

– Rita Kozlov, Cloudflare vp of product, developer platform and AI
Where it gets tricky is when developers want to deploy certain open source large language models or models that are internally trained, Kozlov said. Then, they need to provision virtual machines for infrastructure.

“If you’re looking to leverage some of the really incredible open source models, or a model that you’ve trained yourself,… you’re back to having to provision VMs and really thinking about what’s the peak capacity that I’m going to get, or what’s the peak load that I’m going to get, and provisioning capacity around that.”

Most workloads are not running at 100% all the time — that’s incredibly rare, she said. That means developers are doing a lot of guessing work with provisioning and overpaying for resources that don’t need to be paid for.

“You’re slowing yourself down because you have to think about all that stuff and manage it, and set up load balancing, routing, all that, instead of doing the thing that motivated you to use AI in the first place, which is you want to get to market as quickly as possible, and give yourself that competitive advantage of having AI integrated into your application,” she said.

## Cloudflare’s Use of Predictive AI
Cloudflare has been using predictive AI to, for example, identify real attacks versus legitimate spikes in web traffic, Kozlov said.

“We realized we could take the same network that we’ve built out to help protect and accelerate applications, and use that network to offer developers services to build their applications directly on top of it, instead,” she said.

Besides APIs to connect to inference AI, the cloud-based web platform offers developers:

[Vectorize](https://developers.cloudflare.com/vectorize/), its vector database, which allows developers to bring their own memory/domain-specific information to the model;[Support for Retrieval Augmented Generation](https://developers.cloudflare.com/workers-ai/tutorials/build-a-retrieval-augmented-generation-ai/), which can be used to fine-tune models on domain knowledge and- An
[AI gateway](https://developers.cloudflare.com/ai-gateway/), which helps monitor the costs of running various AI models.
“The AI gateway helps you monitor all these things and experiment, but in a way that allows you to then get and compare the results, and really narrow in on what’s important to you for a particular workload, whether it is cost or whether it’s performance or whether it’s accuracy, and seeing the responses that your users are getting,” she said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)