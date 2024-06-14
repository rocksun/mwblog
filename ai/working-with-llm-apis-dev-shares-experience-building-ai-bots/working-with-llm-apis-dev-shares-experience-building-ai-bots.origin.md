# Working with LLM APIs: Dev Shares Experience Building AI Bots
![Featued image for: Working with LLM APIs: Dev Shares Experience Building AI Bots](https://cdn.thenewstack.io/media/2024/06/172f6adc-ania-kubow-trains-developers-about-ai-bots-1024x638.jpg)
[Software developer and trainer Ania Kubów](https://www.codewithania.com/)’s course on developing with the [large language model PaLM 2](https://www.freecodecamp.org/news/how-to-use-the-palm-2-api/) is already out of date. Just five months after its release, Google deprecated the PaLM 2 language model in favor of [Gemini](https://thenewstack.io/langchain-and-google-gemini-api-for-ai-apps-a-quickstart-guide/). It’s frustrating, but it’s the nature of tech, she told The New Stack.
Demystifying artificial intelligence APIs is one of
[Kubów’s goals as a trainer](https://www.youtube.com/@aniakubow). We asked Kubów what [developers can expect](https://thenewstack.io/2024-forecast-what-can-developers-expect-in-the-new-year/) when it comes to dealing with LLMs and their APIs. She said she’s noticed a [trend toward AI APIs](https://thenewstack.io/6-api-trends-and-practices-to-know-for-2024/) becoming easier to use.
“There is a kind of pattern emerging, especially with the APIs that I have used, that I’m starting to see more,” she said. “At the beginning, even just organizing the documentation, you would read some documentation, and it could seem quite chaotic.”
The accelerated pace of AI is mostly due to the crazy adoption curve of the technology.
## Beware of AI Data Cutoff Dates
In the beginning, there was a lot of confusion about what AI actually was — and arguably, that confusion still surrounds the tech. Kubów sees AI as less of a threat to programmers and more of a robust tool.
“I always just like to think of it […] as a really good Google search, because that’s essentially what it is,” she said. “You’re getting some data that’s been trained. You’re feeding it [data] into a large language model, and that’s what you get back.”
Since AI relies on models trained with a cutoff date — for instance,
[OpenAI’s GPT-3.5 model is trained up until January 2023](https://www.reddit.com/r/OpenAI/comments/1c2cg7t/what_is_your_gpts_training_data_cutoff_date/) — she often advises developers to add their own data or scrape web pages and store it to a database in order to add information to the model.
“I like to remind developers that, it’s really good Google search, [but] be aware of the cutoff date,” she said. “It’s quoting you from 2023, because that’s the latest knowledge it has. So that’s something to be aware of.”
That cutoff data can be significant depending on how
[developers are deploying the LLM](https://thenewstack.io/a-new-tool-for-the-open-source-llm-developer-stack-aviary/). For instance, if you’re building a Formula One chatbot, and someone asks it who won the “latest race,” it might say Lewis Hamilton because its most recent data is from 2023, she said.
## Getting Started with AI APIs
Kubów recommended developers start with a text-to-text model from OpenAI’s GPT-4 or
[Google’s Gemini](https://thenewstack.io/how-to-get-started-with-googles-gemini-large-language-model/).
“It’s one API, and then you can do various things with it,” she explained.
She doesn’t have a preference for any one LLM over another — both OpenAI and Google’s Gemini have their pros and cons, she added.
“Writing the correct prompt is also a consideration that you might want to look at before using up your credits or your money making all these calls.”
— Ania Kubów, software developer and trainer
Although the frontend has to deliver the streaming data ability to deliver chats, Kubów said that what’s significant with the LLM API is happening on the backend. Developers have to understand what they want the chatbot to do, understand the model they want to use, and the kind of output they desire, which will be shaped by the prompt developers create, she added.
“That’s the most important, doing it in a financially efficient way, because each call you make will cost something,” she said. “Writing the correct prompt is also a consideration that you might want to look at before using up your credits or your money making all these calls.”
Primarily, she’s seen developers working on chatbots. She has built a variety of bots, including a
[sales AI bot](https://www.youtube.com/watch?v=x2k_wwH6TqY) and a [multiturn conversation chatbot](https://www.youtube.com/watch?v=l3TLQuwr4G0). She’s also worked with image AI LLMs, [building an image](https://thenewstack.io/3-best-practices-for-image-building-and-scanning/) analyzer that allows users to send an image and have the AI put text to the image. Another generates images based on text using [DALL-E with JavaScript](https://www.youtube.com/watch?v=xv9UbWp_Frs).
“I built out a frontend for it to upload the image on the frontend, send it over to the backend, and then the backend would send it over to the AI,” she said.
## Challenges Developers Commonly Face
In general, Kubów has found the APIs easy to use and self-explanatory. There are some models that can be more difficult to work with, however.
“Obviously, the more difficult ones, the ones sending images over or creating vector embeddings, when you might not understand what a vector embedding is and what is used for, can be bit trickier,” she said. “Of course, we haven’t seen vector embeddings out there before in the API world as much, or at all.”
The common problems she sees developers encounter are when they don’t get the expected results from a chatbot. Often, that relates to writing the prompt. Other issues can result from AI’s accelerated adoption curve — a programmer might have installed a package that’s already newer than the one in the documentation, for instance.
“It all comes from just the rapid change that we’re experiencing,” she said. “The results [can] be quite unpredictable if you’re just starting out.”
The key to success when starting out is to pay close attention to the documentation, she advised.
“As you know, a lot of my tutorials that I made just a month ago or two months ago are now outdated,” she said. “So checking the documentation as much as possible, to check for the latest updates, is definitely something that I would recommend.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)