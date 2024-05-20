# PyCon US: Simon Willison on Hacking LLMs for Fun and Profit
![Featued image for: PyCon US: Simon Willison on Hacking LLMs for Fun and Profit](https://cdn.thenewstack.io/media/2024/05/921d055f-vibes-1024x819.jpg)
![Simon Willison shared his thoughts about working with large language models at PyCon US.](https://cdn.thenewstack.io/media/2024/05/5207aa71-simon-01-300x199.jpg)
Simon Willison shared his thoughts about large language models at PyCon US.
PITTSBURGH —
[Simon Willison](https://simonwillison.net/), co-creator of the widely-used [Python Django framework](https://thenewstack.io/what-is-pythons-django/), has focused his creative energies on [large language models](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) (LLMs) [of late](https://x.com/simonw).
He stopped by
[PyConUS 2024](https://us.pycon.org/2024/) here on Saturday to give a keynote address and encourage the Pythonistas to investigate the possibilities of LLMs.
Sure, LLMs have limitations. They
[make stuff up](https://thenewstack.io/3-ways-llms-can-let-you-down/), and their answers [can reflect hidden biases](https://thenewstack.io/threads-and-threats-when-computers-think-and-biases-emerge/), and are [difficult to move into production](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/). But this does not mean LLMs don’t hold great potential.
“Just because a tool is flawed doesn’t mean it’s not useful,“ Willison told the audience. “And if you understand their flaws and know how to work around them, there is so much interesting stuff you can do with them,”
## Do LLMS Pass the Vibe Check?
Willison has been tinkering with LLMs for about two years now.
“It’s crucial to remember that these things, no matter how convincing they are when you interact with them, they’re not intelligent entities,” Willison said.
LLMs are basically giant autocomplete machines. But, as it turns out, autocomplete gets some really interesting properties as it is scaled up.
“Spooky, what it can do,” Willison said.
LLMs are built from mountains of scraped data (illicitly obtained or otherwise), scraped from the Web, Wikipedia, GitHub, electronic books and repositories of scientific literature.
![](https://cdn.thenewstack.io/media/2024/05/b1043833-llm-size-1024x819.jpg)
Where Llama gets all its information from.
Despite these voluminous sources of data, the total of all the collected data usually amounts to a few terabytes. It is a large collection, but not so unwieldy that it couldn’t fit on a modern laptop.
Collect a few TBs of source material, spend a million dollars in compute and you too can have a LLM.
“They’re not actually that hard to build, if you have the resources,” Willison said.
“If you understand their flaws and know how to work around them, there is so much interesting stuff you can do” with LLMs
—Simon Willison
As a result, there are many many LLMs out now. How do you pick which one to use?
One site Willison uses to evaluate LLMs is the
[LMSYS Chatbot Arena](https://chat.lmsys.org/), a research site. At this site, you provide a question, which is then given to two LLMs. You evaluate the answer from each one.
The Arena tracks 44 LLMs, at last count. A
[leaderboard](https://chat.lmsys.org/?leaderboard) shows which LLMs are ahead of the pack, just in terms of popular votes.
“This is genuinely the most useful tool we have for evaluating these things, because it captures the vibes of the models,” Willison said. The vibe represents how informative and normal a response may be, at least to human judges.
As of Sunday, the top three LLMs were all GPT-4 variants; the top 10 was dominated by proprietary models created by big tech companies or startups. But models with open licensing are creeping up the chart, with Meta’s Llama 3 ranking at No. 7.
This is a good news, according to Willison.
“This is no longer a technology which is locked up behind firewalls,” he said. We can start running these things on our own hardware now, and we can start getting good results out of them.
He found that the open model
[Mistral](https://mistral.ai/), for instance, can be run directly on an iPhone, even without an Internet connection.
## Prompt Engineering: ‘a Big Bag of Dumb Tricks’
But to the beginner, working with LLMs may seem daunting.
By and large, LLMs just provide a single command line for the user to interact with.
“It’s like taking a brand new computer user and dropping them into Linux with [only] a terminal and telling [them], ‘Hey, you figure it out,'” Willison said.
Plus, given their sometimes unpredictable behavior, he said, “working with these things is really quite incredibly tricky to get them to do what you really want them to do.”
But work with LLMs for awhile, and you’ll find that
[prompt engineering](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/), as it is called, is a “big bag of dumb tricks.”
Here are a few tricks Willison suggested.
For one, it helps if you present the problem you are trying to solve as a little screenplay.
You script out a dialogue where the user asks for something — say, a list of possible pelican names — and the computer responds with a list of pelican names, which is left to the LLM to generate, which the LLM will then make up.
“If you give it a little screenplay, it will fill out the gaps,” he said.
It also helps if you supply some supplemental material for the LLM. If you want a summary about a particular subject, include everything else you have found on the Web about that subject in that query.
“One of the things these models are fantastic at doing is answering questions based on a chunk of text just given,” he said.
Another trick: Give them the tools they need to do a job. Oddly enough, two things that LLMs can’t do well are the two things computers have historically been best at: mathematics and looking things up.
![](https://cdn.thenewstack.io/media/2024/05/98a4da02-prompt-injection-300x240.jpg)
A sample prompt injection attack.
So, if you have the question, what is the population of France times 352, you prep the LLM with a link to Wikipedia and to a calculator app. Then, instruct it to find the population on Wikipedia (68 million) and have the tools to multiple that times 352.
Adding in third-party apps is the way to break LLMs out of their boxes, and can be incredibly easy to do, Willison promised: “When people get all excited by agents and fancy terms like that, this is all they’re talking about.”
## How Prompt Injection Works
The downside of adding third-party apps, however, are security concerns around prompt injection, where a third party can preface their own malicious code in front of your own.
Take, for instance, a personal chat assistant, a common AI-based app being built these days, something that, upon voice command, can book a flight or cancel a lunch meeting (Google recently
[ launched one](https://assistant.google.com/)). It could easily be overtaken by a third party that instructs it to change the password and erase the action from its logs.
“Turns out we don’t know how to prevent this from happening,” he said, noting he coined the term “prompt injection” (like SQL injection) to describe this kind of security attack.,
Prompt injections are not an attack on LLMs themselves, but rather on all the tools we put on top of LLMs. Nobody has figured out a way to fully prevent prompt injection attacks, though many solutions do offer some protection. But if there are holes, attackers will find a way to exploit them.
“Never makes untrusted text — text from emails and from the web — with access to tools and access to private information,” Willison said. “You’ve got to keep those things completely separate.”
## Build Stuff You Couldn’t Build Previously
Willison himself evaluates any new technology in terms of what he could build with it that he couldn’t have done otherwise.
And LLMs, he said, “do this better than anything else I’ve ever seen.”
OpenAI is making advances in its user interface. An alpha release,
[Code Interpreter](https://365datascience.com/trending/chatgpt-code-interpreter-what-it-is-and-how-it-works/) provides the capability for ChatGPT to write Python code and place it in a [Jupyter Notebook.](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)
Willison used it to plot the outline of Adirondack Park, which was mapped in a
[GeoJSON file](https://geojson.org/) as a series of line segments. He had to go back twice and reiterate his request before being able to get a full outline of the park against the state map.
With LLMs, you very rarely will get the answer you are looking for on the first try. Sometimes you can add explicit instructions, and sometime you can just tell ChatGPT to “do better.”
Despite the multiple iterations, Willison was able to complete the project within about three minutes.
Just the fact that Willison can spin up these projects within a few minutes opens the door … to many other side projects, he said.
He also wrote a counter that monitored his Pycon talk in real time, tallying the number of times he said “AI” or ” artificial intelligence,” and updating the number in real time during the presentation (on the top right-hand corner of the presentation screen.)
To build the counter, he merely asked the latest release of ChatGPT,
[ChatGPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/), what his options were for build such an app, given that he was a Python programmer with a Mac.
He asked for multiple options. This point was important, he noted, in that ChatGPT will usually only give one answer, which may or may not actually work. Asking for multiple options will give you more choices.
“It will much more likely give you a result you can use,” he said.
Using a Python audio translation tool he never heard of before, ChatGPT returned a Python script that almost worked —and did, after a few minor tweaks. He then asked ChatGPT to generate the code to place the counter on the computer screen.
“Those three prompts gave me exactly what I needed,” he said. Total time invested? About six minutes.
If he were to spend half a day coding this feature, he wouldn’t have bothered. But that it could be done in less than 10 minutes?
Such ease of use, he said, “enables all these projects that I never would have considered before.”
## Not Generative but Transformative
[Generative AI](https://thenewstack.io/ai/) may not be the best name for these technologies, Willison surmised. It suggests a machine that can produce mostly junk. A better name, he said, would be “transformative AI.”
“The most interesting applications are the stuff that when you feed large amounts of text into it, and then use it to evaluate and do things based on that, so you’ve got structured data extraction,” he said. “Things like that are much less likely to hallucinate.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)