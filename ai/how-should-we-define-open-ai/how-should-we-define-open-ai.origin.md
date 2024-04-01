# How Should We Define ‘Open’ AI?
![Featued image for: How Should We Define ‘Open’ AI?](https://cdn.thenewstack.io/media/2024/03/a3f984f6-screenshot-from-thomas-padilla-keynote-at-niso-plus-2024-taking-questions-1024x574.png)
“Our vision is a world where all benefit from the unfettered exchange of information,” explains
[the official website](https://www.niso.org/what-we-do) for the National Information Standards Organization.
Accredited by the American National Standards Institute (ANSI), it’s the nonprofit standards group for library/publishing/bibliographic applications for both “traditional” and new technologies.
But there’s one very important standard that’s still developing in the world: What exactly constitutes an open artificial intelligence, or “open AI”? It’s a question
[Archive.org’s deputy director Thomas Padilla](https://niso.cadmoremedia.com/Title/77531239-61fa-48aa-807f-4885a13cc672) tackled this year in his keynote for that year’s NISO Plus conference.
“It’s a talk about the AI,” Padilla promised his audience.
“But like most talks about technology, it ends up being to talk about us and about what we want to achieve.”
## Is Llama 2 Open Source?
While the Open Source Initiative is still
[working on their official definition](https://opensource.org/deepdive/drafts/the-open-source-ai-definition-draft-v-0-0-3) of “open source AI” — through a consultative community process — some important distinctions are already clear.
Identifying five characteristics that open AI should have, Padilla said he believes “open” AI should be reusable, with users weighing trade-offs between performance and “broader reusability and the potential for others in our community to build upon the bottom model.”
But how does that play out in the real world?
Meta’s
[Llama 2](https://llama.meta.com/llama2/) declares it’s open source, and free for research and commercial use — but Padilla reviewed [the license terms at its GitHub repository](https://github.com/meta-llama/llama/blob/main/LICENSE), “putting my librarian hat on.”
Under “Additional Commercial Terms,” it warns that if a licensee has more than 700 million active monthly users, “You must request a license from Meta, which Meta may grant to you in its sole discretion.”
And otherwise, “You are not authorized to exercise any of the rights under this Agreement unless or until Meta otherwise expressly grants you such rights.”
Padilla called that “some shade against the other big tech companies, for the most part” — although Red Monk co-founder Steve O’Grady is fairly clear that that’s not pure
[open source:](https://thenewstack.io/gitlab-co-founder-and-ceo-on-iteration-and-open-source/)
useful clarification, which makes the targets clear. you can use it unless you work at, say, google. imagine if linux was open source, unless you worked at facebook.
and that’s just one of multiple field of use restrictions, any one of which means it’s not open source.
[https://t.co/x2CYrKLifF]
— steve o’grady (@sogrady)
[July 19, 2023]
But Padilla thinks there’s another clause even more deserving of a “Llama side-eye.”
Padilla feels that very much is “… not in the spirit of
[open source](https://thenewstack.io/an-open-source-journey-to-greener-cloud-native-environments/). It feels to me like it sort of — it explodes the whole thing. How is that open source? It’s not!”
But Padilla adds that “other models have come onto the market that do show a degree of promise, I think, for having a stronger alignment with the spirit of open source …” — citing specifically the open language model
[OLMo](https://allenai.org/olmo).
OLMo describes itself as a “truly open LLM and framework,” and emphasizes that “all code, weights, and intermediate checkpoints are released under the Apache 2.0 License.”
## Mysterious Answers
Meta’s Llama isn’t the only game in town.
ChatGPT’s developers even named their technology
[OpenAI](https://thenewstack.io/openai-algorithm-allows-ai-to-learn-from-its-mistakes/) — and here, Padilla tells his audience, “I also believe OpenAI is open.”
But there’s still room for criticism. Transparency is part of Padilla’s definition of openness — it plays a role in the “integrity of knowledge”— defined as making sure authors and “knowledge producers” are credited.
Instead, today content producers are being “ghosted,” as Padilla sees it — with crediting either not existing “… or it’s vaguely referenced to. I think that’s bad.”
With much of today’s generative AI, it’s more like mysterious answers summoned from a magical seance. “You get responses like, ‘I don’t have access to how I provided you this answer.'”
Responses like that would never fly for a peer-reviewed paper, Padilla points out:
I asked Chatgpt how much of its data comes from Wikipedia: I don’t have access to my training data, but I was trained on a diverse range of data from the internet, including sources such as books, websites, and other texts to develop a wide understanding of language.
— James (Jim) McTague (@Mctaguej)
[December 8, 2023]
There’s another issue. In February, Fast Company
[spoke to the head of the OLMo project](https://www.fastcompany.com/91021305/ai2-new-open-source-llm), AI2 senior director of research Hanna Hajishirzi, about Meta’s models. Their conclusion? The models were very valuable, but the data behind them still wasn’t available. “We don’t understand the connections starting from the data all the way to capabilities,” the magazine noted.
And even beyond that, “The details of the training code is not available. A lot of things are still hidden.”
So another aspect of transparency is good documentation — and here, Padilla sees promise in
[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)‘s [model cards](https://huggingface.co/docs/hub/en/model-cards).
When users upload a model to Hugging Face’s tools, they’re prompted to specify the model’s parameters and which datasets were used (according to Hugging Face’s
[definition of model cards](https://huggingface.co/docs/hub/en/model-cards)) — as well as the model’s intended use, and its “potential limitations, including biases and ethical considerations.”
Padilla says he’d “love to see more uptake of this” — and “possibly even a requirement” to upload them to Hugging Face. “Perhaps that’s around the corner.”
“Without transparency, you have no assurance of knowledge integrity,” Padilla tells the audience. “And if you have no knowledge integrity — then why bother be involved in something like this at all? I really think it weakens the value proposition of the entire thing.”
## How Should AI Be Held to Account?
In addition, open AI should also very much be accountable, Padilla believes — meaning that it’s developed (and used) according to specific community needs.
For “accountability,” Padilla applauded policy and regulation and executive orders “attempting to enshrine certain protections and safeties to guide the development and implementation of AI,” including the White House’s October “
[Executive Order on Safe, Secure, and Trustworthy Artificial Intelligence](https://www.whitehouse.gov/briefing-room/statements-releases/2023/10/30/fact-sheet-president-biden-issues-executive-order-on-safe-secure-and-trustworthy-artificial-intelligence/).”
But Padilla also cited the real-world accountability principles espoused by Distributed AI Research Institute (founded by AI researcher
[Timnit Gebru](https://thenewstack.io/google-grapples-with-ethical-ai/)), on the organization’s [Research Philosophy](https://www.dair-institute.org/research-philosophy/) page.
One of their aims is to reduce “the distance between researchers and community collaborators.” Another aim of theirs is to focus on trust and time, to forge “meaningful relationships with communities.” And they in particular are talking about minoritized or marginalized communities that are not often at the center of AI research, but are often on the receiving end of negative impacts of AI research that does not take into account the lived experience.
“I think DAIR provides us a nice roadmap,” Padilla said.
## Sustainability
Padilla said
[open AI should be adopted in a “sustainable”](https://thenewstack.io/sos-sustainable-open-source/) way, with an awareness of “interdependence, threats and opportunities.”
To that end, Padilla proposes three ways of looking at it. To demonstrate what he calls the “exploded” view of interdependence, Padilla showed a
[2018 data visualization](https://www.moma.org/collection/works/401279) exhibited at New York’s Museum of Modern Art which (according to its gallery label) “analyzes the vast networks that underpin the ‘birth, life, and death’ of a single Amazon Echo smart speaker.” (It moves from the periodic table of elements, Padilla told the audience, “up to the strip mining that needs to happen to gain the raw materials to produce a Dot, up to smelters and refiners and then favorable labor conditions, up to the component manufacturing and so forth.
“I think it’s one way to kind of get a sense of the interdependency that’s at play when we adopt, not just AI, but any technology.”
There’s also a “systems” view — Padilla cites the world-systems theory, which explores how different parts of the world get relegated to their roles in the production of what Padilla calls “highly polished commodity products.” And Padilla also provided an example for the kinds of questions explored in the “replacement” view. In October, a U.S. House subcommittee on technology oversight
[heard testimony from Emily M. Bender](https://democrats-science.house.gov/imo/media/doc/Dr.%20Bender%20-%20Testimony.pdf), a linguistics professor at the University of Washington.
“I find that the phrase ‘artificial intelligence’ is best understood as a marketing term,” Bender had said, “and one which only muddies the waters. It is clearer to talk about automation.” This leads to different questions, including:
- What is being automated?
- Who is automating it and why?
- Who benefits from that automation?
- Who is being harmed and what recourse do they need?
- Who has accountability for the functioning of the automated system?
- What existing regulations already apply to the activities where the automation is being used?
The arrival of AI shouldn’t just be about worrying about which jobs will be replaced. Ideally, we also want open AI to have an “affirmative” impact, Padilla believes —
[ supporting the evolution of roles in organizations](https://thenewstack.io/how-we-learn-will-drive-modern-it-organizations-and-business/).
## Marketing Terms vs. Technical Descriptors
Padilla had opened his talk with a damning observation from
[a paper written last August](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4543807). While earning his PhD at Carnegie Mellon, David Gray Widder had teamed up with Sarah West, managing director of the AI Now research institute, and Meredith Whittaker, president of the Signal Foundation (a nonprofit focused on open source privacy technology and developers of the Signal messaging app).
“We find that the terms ‘open’ and ‘open source’ are used in confusing and diverse ways,” the researchers wrote, “often constituting more aspiration or marketing than technical descriptor, and frequently blending concepts from both open source software and
[open science](https://thenewstack.io/nasas-thirst-for-open-source-software-and-for-open-science/).”
“This complicates an already complex landscape, in which there is currently no agreed on definition of ‘open’ in the context of AI, and as such the term is being applied to widely divergent offerings with little reference to a stable descriptor.”
So we’re currently living in a world where licensing terms are hard to assess, Padilla said, not to mention the jolt of discovering a tech stack that is highly proprietary — and expensive. “We think we know what open means and then we start experiencing kind of like this M.C. Escher-like experience….”
“I think it behooves us to have, you know, a more concrete sense of what we want from AI and the knowledge work that we do collectively together.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)