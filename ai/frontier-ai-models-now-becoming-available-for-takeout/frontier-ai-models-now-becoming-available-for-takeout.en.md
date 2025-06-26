AI with top frontier models is like restaurant food — you have to visit OpenAI, Google or Microsoft to consume it. But that is slowly changing.

Top AI companies are making takeout versions of their proprietary frontier large language models, which users can run in their own data centers.

Companies can also use custom inference models, with or without internet connections.

Google is customizing versions of its Gemini LLM that companies can install on servers with GPUs in their data centers. That’s a big change from the past when Gemini was available only on Google Cloud.

Google’s Gemini was born on TPUs, but is now ported to GPUs in the public cloud, which allows them to be installed on private servers, [Sachin Gupta](https://www.linkedin.com/in/bayareagupta), vice president and general manager of infrastructure and solutions at Google Cloud, told The New Stack.

> “We are offering this in air-gapped and in connected scenarios.”  
> **– Sachin Gupta, Google Cloud**

“We take those models and they’re optimized for GPUs, and then we’re able to bring them on-premise using [Nvidia] Blackwell systems,” Gupta said. “We are offering this in air-gapped and in connected scenarios.”

AI startup Cohere is also customizing versions of its frontier large language model that companies can deploy on their own hardware. The company, earlier this month, raised $500 million in funding on a valuation of $5.5 billion.

Burning compute on bigger and bigger models is not actually what enables business value, [Autumn Moulder](https://www.linkedin.com/in/autumn-moulder/), vice president of engineering at Cohere, told The New Stack.

Cohere is providing hardware flexibility for their on-premise models.

“That’s one of the things that we focused a lot on when we built this entire self-contained system,” Moulder said.

Many companies are looking to ditch the cloud and repatriate workloads in-house for cost and security reasons. These custom models are fine-tuned to specific applications of organizations and to run in constrained environments.

## The Hardware

The concept of proprietary AI models running on in-house hardware is a fairly young phenomenon.

OpenAI and Anthropic don’t have those capabilities yet, and did not respond to requests for comment.

Historically, popular frontier models were beholden to proprietary hardware. Google Gemini used the company’s TPUs, OpenAI used Nvidia GPUs, and Anthropic used custom chips in the cloud.

Companies that wanted on-site AI instead turned to open models like DeepSeek, Mistral and Llama, which can be downloaded and supported on various systems. These models are easily customizable and free.

Google’s port of Gemini from TPUs to GPUs will expand the LLM’s footprint, giving it an edge over OpenAI, whose models are restricted to cloud servers.

Cohere’s AI initiatives started off with Google’s TPUs, but it is now porting its model to other AI hardware.

> “We allow for silicon optionality, and work with multiple providers for inference.”  
> **– Autumn Moulder, Cohere**

“We allow for silicon optionality and work with multiple providers for inference. We have a partnership with Nvidia and AMD,” Moulder said.

To be sure, this isn’t for casual users. It may still take millions of dollars to customize and deploy these black-box AI models.

Google and Cohere are betting on ease of deployment as a way to attract customers. Their models are pre-packaged applications that don’t require customers to develop everything from scratch.

## Why Is Takeout Catching On?

The age of doubting AI is over, and companies are confidently moving AI to production inside their own data centers, said [Jack Gold](https://www.linkedin.com/in/jckgld/), principal analyst at J. Gold Associates.

Some companies want their IT in-house and prefer AI models in their own systems for security and compliance reasons, Gold said.

Google’s Gupta gave the example of ServiceNow, which has developed an AI agent for Gemini.

“That agent acts on customer data … that must remain on-premise. And there’s some compliance requirements around that,” Gupta said.

Data sovereignty requirements also require companies to keep customer data on private servers in specific geographic locations, said [Charlie Dai](https://www.forrester.com/analyst-bio/charlie-dai/BIO5344), vice president and principal analyst at Forrester Research.

To go to production in AI, especially in critical infrastructure industries, companies need a level of control over where the data is going, Cohere’s Moulder said.

“You need to be able to know where your data is going. You can’t necessarily rely on third-party data that’s sitting on servers controlled by someone else,” Moulder said. “That opens you up to too many regulatory concerns.”

## The Models

The in-house models are typically constrained versions of the large language models that are targeted at inferencing. Both use Kubernetes as a computing layer.

Developers need to understand efficiency in private computing environments, especially with AI-enabled systems going into production, the executives said.

Stress testing the AI system is also important.

Customers tried Gemini in Google Cloud and they want features such as the 1-million context window and multi-modal capabilities in their own data centers, Gupta said.

“We are able to use our fully managed on-prem cloud service Google Distributed Cloud … to simply enable Gemini Pro, Gemini Flash API for customers. They don’t have to worry about anything in that stack, they just get an API that’s exposed to them,” Gupta said.

Cohere packages and delivers models by recognizing the target architecture the customer is on, Moulder said.

“We just make sure that’s what’s available to them. But the entire system, it’s pretty much the same, just compiled for each different architecture,” Moulder said.

Cohere makes sure there are zero dependencies on a particular managed provider.

“And then we allow for a lot of configuration that goes into that environment. And that lets us target virtual private cloud, on-premise. It’s all the same to us,” Moulder said.

## Customizable Models

Customers can customize the on-prem model with their own data.

Exposed APIs allow customers to start integrating agents or machine learning workflows.

“We’ve also found some of them do have very specific needs, where we can customize a model that’s just vertically integrated and works really well for that particular subject area with certain partners,” Moulder said.

Google partnered with Nvidia to provide a confidential computing stack, which secures the data.

“The partnership allows us to protect the IP of the model running in confidential VMs so that when the model’s in use, it’s fully protected in an encrypted VM,” [Justin Boitano](https://www.linkedin.com/in/justinboitano/), vice president for enterprise AI software at Nvidia, told The New Stack.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/06/501d027b-agam-shah_avatar_1497985030.-600x600.jpg)

Agam Shah has covered enterprise IT for more than a decade. Outside of machine learning, hardware and chips, he's also interested in martial arts and Russia.](https://thenewstack.io/author/agam-shah/)