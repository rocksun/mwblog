If we wonder how Large Language Model (LLM) providers will try to improve their services in the next few years, we can start by trying to foresee how current limitations will be addressed. While LLMs have been fairly successful in the chat box format, they are both expensive in terms of energy usage and have interminable problems with hallucinations. Software developers battle with increasing token usage to achieve more focused results.

There is still a bit of guess work involved in working out how size vs. training truly effects output, but the problems with energy and hallucinations have put a limit on expansion. So this post looks at the possible directions that LLM providers might choose to move towards.

But first we have to check the validity of Yann LeCun’s prediction that [LLMs are a dead end](https://www.businessinsider.com/meta-ai-yann-lecun-llm-world-model-intelligence-criticism-2025-11). While this might ultimately be true with respect to “artificial general intelligence,” the sheer money and momentum invested with the AI companies ensures that we will still be using LLMs for some time yet. LeCun himself has [launched a startup](https://www.linkedin.com/posts/yann-lecun_as-many-of-you-have-heard-through-rumors-activity-7397020300451749888-2lhA/) to “continue the Advanced Machine Intelligence research program (AMI) I have been pursuing over the last several years”; but this won’t bear fruit for a while.

## Ontologies

Many of the old approaches to AI have been brushed aside by the successes of LLMs, but I still remember when it was assumed that artificial intelligence would be composed of large [ontologies](https://www.shepbryan.com/blog/ontologies-101) — think of these as concept maps, very much like hashtags, to connect ideas within some type of formal structure. Because LLMs train on vast amounts of information, they internalise concepts in a somewhat random manner, yet appear to understand how things relate. But we know that LLMs can help create knowledge graphs; and [Retrieval-Augmented Generation](https://thenewstack.io/a-blueprint-for-implementing-rag-at-scale/) (RAG) is one vital method used to keep an LLM response honest, by feeding it with formatted expert knowledge.

One possible approach to fight hallucination would be to focus on maintaining lots of large knowledge graphs in certain subject matters, and sharing these amongst other provider services.

The pressure to do this may be regulatory. For example, we’ve seen recently how Australia has [put an age restriction on social networks](https://www.theguardian.com/australia-news/2025/dec/13/will-other-countries-follow-australia-social-media-ban-under-16s) because of the various negative effects of screen addiction on children. So it might be necessary to create the equivalent of the “Children’s Britannica” — a large set of information that doesn’t divulge facts from problematic areas. Maintained by third parties, more regulated information may persuade national governments that LLMs won’t spread biased facts.

## Hub and Spoke

Formally sharing large amounts of information might work against the business models of competing providers, but working together could still lead to efficiency savings.

We already have hope some here: the early and slightly surprising universal acceptance of Anthropic’s [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) as the “USB of the LLM” may tell us that where an idea is good enough, competing providers (such as OpenAI in this case) will take it up.

OpenAI has already underlined a possible distribution model with its [Apps SDK](https://thenewstack.io/openais-apps-sdk-a-developers-guide-to-getting-started/) and how that might work with its Atlas browser. The idea here is to literally treat local knowledge as a kind of MCP server that the LLM can call on. In this way, OpenAI is taking a shot at replacing the web — by answering general queries with its ChatGPT model, but calling user application servers to get local expert information. In exactly the same way as OpenAI uses MCP tools to access your hard drive, for example.

## Local LLMs

Many people already run LLMs locally, and we have shown readers [ways to do this](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) over the past few years. While the big bleeding edge models will remain in the cloud, there are plenty of smaller pre-weighted open source models that users can run on their laptops. Running locally is still a bit technical, but apps like Ollama make it much simpler. Of course, the ultimate local machine might well be your phone.

We’ve already seen how Agentic CLI systems can choose a quick cheap model for some queries, leaving the more expensive models for “deep thought” or “planning.” This leads to the idea of maybe using a local model for smaller queries, while sending harder queries to the bigger models crunching in the cloud.

## The Life Stream

The other reason to look locally is to pick up the user’s personal context. This begins to make a lot of sense when we see how good Google has historically been in answering user queries, because it knows enough about them to exclude irrelevant results.

It is reasonable to assume that Amazon trains LLMs with information from millions of Alexa speakers, as well as isolating the identity of individual speakers in a family. But a local LLM could just listen and read all your speech and content in order to fully understand not just your geographical location, but also what interests you in detail.

While the possibly Orwellian consequences of the “life stream apps” did alarm us in 2010s, we still filled them with our continuous status reports. Agentic CLIs use setup markdown files to give the LLM hints about a project, so analysing a user over time could certainly be more efficient. Socrates is supposed to have said “the unexamined life is not worth living,” and while I doubt he would’ve approved of AI, a moderate amount of recording could certainly give a rich (if personal) graph for an LLM to start working with.

## Conclusion

It might need a small “correction” (i.e. crash) in the market before the large providers set to work on improving efficiency, or for investors to move away from chasing “artificial general intelligence.” Perhaps large companies will move together into another hype area to continue the AI momentum and keep their share prices high. But the chances are good that engineering will shift into improving existing investments.

If you use LLMs for software development, you will have a front row ringside seat for any upcoming changes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)