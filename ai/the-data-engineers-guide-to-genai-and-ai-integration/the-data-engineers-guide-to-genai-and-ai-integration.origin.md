# The Data Engineer’s Guide to GenAI and AI Integration
![Featued image for: The Data Engineer’s Guide to GenAI and AI Integration](https://cdn.thenewstack.io/media/2025/01/9939e8da-stephen-harlan-a0nub-d0jmo-unsplash-1024x683.jpg)
[Stephen Harlan](https://unsplash.com/@gogostevie?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-red-dont-panic-sticker-on-a-wall-a0nUb-D0Jmo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
When we started Nexla in 2016, our mission was to make data readily available to any data consumers, which also involved making it easier to integrate apps. We believed that ML and AI would completely change data engineering.

However, we did not expect generative AI (GenAI) to change everything this fast. Its adoption by enterprises is happening faster than Cloud Computing or Big Data, and these past technologies were labeled as do-or-die extinction events. GenAI seems much more urgent, like an incoming tsunami, and you have to ride or die now.

GenAI is difficult to use. High-tech powerhouses and startups are already demonstrating its power. However, as with most innovations, the tools they create and use require skillsets that most companies lack. Tooling needs to be simplified before the rest of the world can adopt GenAI.

Don’t panic.

First, you will continue to have a job. GenAI is not (yet) replacing people, and it’s not replacing data engineers for a long time. If you’re a [data engineer](https://thenewstack.io/5-python-libraries-every-data-engineer-should-know/) willing to try out some new tools and know where to use GenAI first, you’ll be fine.

While the early GenAI applications required a lot of coding, more straightforward tools are emerging. At Nexla, we used GenAI to help automate the repetitive tasks that take up a lot of [time in integration](https://thenewstack.io/two-times-integration-testing-in-production-has-gone-wrong/). Less technical engineers can integrate [data by building](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/) reusable data products and workflows without coding. The connectors, schema, and how the data products and workflows are implemented all get generated. This includes building GenAI retrieval augmented generation (RAG) pipelines (more on RAG below.)

Finding your first uses of GenAI has also become more straightforward. Just figure out which employees or customers could use assistants, also called copilots, to let them do a task independently. One of the more common examples is a chatbot assistant that provides recommendations utilizing a knowledge base such as a support database.

You can think of this dual use of GenAI as AI integration — integration for AI by AI.

**GenAI In the Real World: TripAdvisor and Bloomreach**
Many examples now exist of companies using GenAI to create more personalized experiences or improve operations. We work with several companies on it. You’re probably already benefitting from GenAI and may not realize it.

The travel platform TripAdvisor uses GenAI to improve the experience of more than 400 million monthly active users and 1 billion reviews. They created an AI-powered trip planning application that creates detailed day-by-day itineraries with personalized recommendations based on user profiles and preferences to help users plan their trip, such as an overview of restaurants in the Back Bay area of Boston. TripAdvisor has also started to use GenAI internally to support customer service, sales, marketing, finance, accounting, HR, and analytics departments. This information is now more accessible to users, search engines, and external (partner) apps.

TripAdvisor integrated GenAI with its recommendation engine, using GenAI to help the [engineering team write code](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/). This is one of many examples of AI integration.

Another great example is Bloomreach, a cloud-based e-commerce experience platform that personalizes 25% of eCommerce experiences in the US and UK. They use AI to improve search and product matching. They also provide Bloomreach Clarity, a conversational shopping product that uses natural language, such as English, and images to help find the right products.

AI-powered integration has helped Bloomreach cut its integration times in half. This is important when onboarding eCommerce customers. But more importantly, it also improves data accuracy. There is no good AI without good data. Better AI outcomes lead to improved end-user satisfaction with each eCommerce experience.

**The Cliff Notes — The Data Engineer’s Guide to GenAI and AI Integration**
After seeing these and other GenAI projects, here’s my advice.

-
**Invest in Core Data Engineering Skills**
AI can’t replace data engineers. These projects still required data engineers who understood the fundamentals of data engineering — including data modeling, DataOps best practices, and, yes, SQL optimization. Make sure you continue to build up these core skills. Even if GenAI makes recommendations, you still need to be the expert that makes the final decision.

-
**Learn GenAI RAG Now**
Gen AI RAG is the most common pattern for implementing GenAI. Instead of re-training or fine-tuning a large language model (LLM), which can be very expensive and complicated, you load the relevant data, your knowledge base, into a vector database. Whenever a question (prompt) is asked, you first search in the vector database for the most relevant context. You then send the question and context to a generic LLM, like ChatGPT or Llama.

GenAI RAG is the way to go. You need to know how to use it; [this tutorial can help](https://nexla.com/ai-infrastructure/retrieval-augmented-generation/).

-
**Try Using GenAI-Powered Tools**
The tutorial uses Nexla to build your GenAI RAG pipeline, and several parts of the pipeline development are actually “developed” for you using GenAI. Don’t be afraid to try new AI-powered integration tools. Be scared if you don’t because others will.

AI-powered integration has improved integration productivity by 2x or more in most of the projects we’ve seen. It automates the little details that slow integration down, like extracting data schema and identifying the best standard model, mapping transforms, or automating schema evolution in a data pipeline.

Also, GenAI isn’t perfect. As an expert, you must be able to spot issues (see Point 1).

-
**Get Ready for Agentic AI**
Agentic AI just means an agent is driving the “chatbot” interaction with an LLM to make decisions independently. Over time, more companies will begin to fine-tune models using techniques like Retrieval-Augmented fine-tuning (RAFT) or training and re-training their oodels.

This may sound hard; again, don’t panic. Some are saying 2025 will be the year of agentic AI. That means you have some time to learn.

**It’s Deja Vu All Over Again**
While some say AI is changing the world, it’s not changing the need for data engineers. Those core skills are still needed. But as with every new trend, you must keep up with the times. That means you need to learn and use [RAG now and start learning more about fine-tuning and model](https://thenewstack.io/rag-vs-fine-tuning-models-whats-the-right-approach/) training next.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)