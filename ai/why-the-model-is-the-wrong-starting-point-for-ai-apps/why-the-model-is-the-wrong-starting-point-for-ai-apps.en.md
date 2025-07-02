When it comes to choosing models, developers often start with a frontier model, which is another name for a cutting-edge, large language model such as OpenAI’s GPT-4, Google’s Gemini Ultra, and Anthropic’s Claude 3 series.

But frontier models can quickly become cost-prohibitive. That’s when developers tend to find smaller models that may trade some accuracy for costs, according to Forrester principle analyst [Rowan Curran](https://www.forrester.com/analyst-bio/rowan-curran/BIO4966), whose research focuses on AI, machine learning and data science.

After seeing what can be accomplished with a big frontier model, developers understand the problem more and their own level of appetite for risk, he explained. That’s when they will switch to one or more smaller, open-weight models. [Open-weight models](https://www.ntia.gov/programs-and-initiatives/artificial-intelligence/open-model-weights-report/background) are where the trained parameters (aka, weights) are made publicly accessible, usually for download.

It’s not necessarily a one-to-one mapping, though. As an example, Curran said these models might have 85% of the accuracy, but they can be run at 20% of the cost.

“We started to see that shift as well, where people are starting to break the problem down: from how do we just use one model [to] kind of solve all this, to how do we really optimize around relatively cheaper models,” he said. “You can’t really do that until you reach v2 of your application, and understand what the v1 outcomes really looks like.”

That’s one reason you’ll often see AI apps with a thumbs up/thumbs down option to provide feedback for results, he added: It helps companies understand what works, to better fine-tune their offerings.

## Evals and Other Considerations For AI Apps

When you’re trying to decide which model to use for your application, your first step probably shouldn’t be a model at all. Instead, you should focus more on building a [base eval](https://thenewstack.io/where-ai-benchmarks-fall-short-and-how-to-evaluate-models-instead/) than picking a model, advised Thesys CEO [Rabi Shanker Guha](https://www.linkedin.com/in/rabisg/).

[Thesys is a generative user interface (GenUI)](https://thenewstack.io/generative-ui-for-devs-more-than-ai-assisted-design/) company that specializes in AI-driven interfaces. When Guha and his co-founder (designer Parikshit Deshmukh) began, they started with an evaluation — or eval as it’s often shortened to in AI.

> “…people are starting to break the problem down from how do we just use one model kind of solve all this, to how do we really optimize around relatively cheaper model.”  
> **— Rowan Curran, Forrester principle analyst**

“The first thing we did was we came up with a base eval for how to evaluate these models,” said Guha.

For their eval, they tracked a web dev arena LLM benchmark and a benchmark called the [τ-benc (tau-bench](https://arxiv.org/abs/2406.12045)).

“We ideally need a model that scores high enough on both of these things, and based on that, then we had these evals,” Guha explained. “So we did not actually test out hundreds of models, but we tested out the five top models based on [the] existing two benchmarks, plus our benchmark.”

Using these, as well as a human eye to measure the actual output of the UI, they were able to narrow their choice down to two or three models, and then they started experimenting.

Developers should think about more than just the model, warned [Abhishek Sengupta](https://www.linkedin.com/in/abhisheksengupta88/?originalSubdomain=in), practice director for the IT consultancy the Everest Group.

“The data set used to train the model, the cost of inference, performance against relevant test cases, and security features are some criteria to keep in mind,” Sengupta advised.

## Don’t Marry Yourself to an AI Model

With a new model coming out seemingly every week, and prices continuing to go down, developers are wise not to attach themselves to one model or company too quickly, said [Lee Robinson](https://www.linkedin.com/in/leeerob/), who heads developer experience at frontend hosting company Vercel.

“Don’t get too attached to one specific model. Make it easy so that you can move between models and then [verify and test](https://thenewstack.io/test-driven-development-with-llms-never-trust-always-verify/) as you try out different models,” advised Robinson. “You want to have an abstraction layer between that so you can easily move, because it’s almost guaranteed there will be a newer, better model in a very short amount of time.”

That means ensuring you build your code in the right way so you can trade out models as needed, he continued.

Increasingly, companies that cater to AI development work are offering developers the chance to easily switch models and experiment with what works. For instance, Robinson pointed out that [Vercel offers an AI SDK](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/), which allows you to change AI models with one line of code. And just last week, Vercel rolled out [AI Gateway](https://thenewstack.io/frontend-ai-vercel-abstracts-model-chaos-in-one-interface/), which abstracts away the hassle of switching models, giving developers access to approximately 100 models without worrying about API keys, provider accounts, or rate limits.

Similarly, [SAP made it easier](https://thenewstack.io/sap-unveils-new-ai-tools-for-developers/) this year for its enterprise developers to use different models by adding an abstraction layer to ensure that security, ethics, data privacy and protection are all ensured with AI models.

“With OpenAI, Mistral, Anthropic, you name it, we have the flexibility to make use of these large language models based on the needs of the application, because they all differentiate in costs, in accuracy, in performance, and of course, which use cases are best,” [Michael Ameling](https://www.linkedin.com/in/michael-ameling/?originalSubdomain=de), president of the SAP Business Technology Platform, told the New Stack. “We can make use of different models depending on the use case in our application.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)