# When Prompt Injections Attack: Bing and AI Vulnerabilities
![Featued image for: When Prompt Injections Attack: Bing and AI Vulnerabilities](https://cdn.thenewstack.io/media/2024/12/cc865fba-angry-bot-1024x683.png)
[CVG Repo](https://www.svgrepo.com/svg/492591/angry), cc0 license.
AI enthusiast and creator of the Python Django framework [Simon Willison](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/) coined the term “prompt injection attack” in [a September 2022 blog post](https://simonwillison.net/2022/Sep/12/prompt-injection/). But [Benj Edwards](https://www.benjedwards.com/), senior AI reporter for Ars Technica*,* is perhaps the one who suffered most because of it, in a bizarre string of events ending with Bing Chat calling him “an enemy” (as well as a “hostile and malicious attacker”).

All for the sin of writing about someone else’s prompt injection attack.

Tricking a chatbot into behaving badly (by “injecting” a cleverly malicious prompt into its input) turns out to be just the beginning. So what should you do when a chatbot tries tricking you back? And are there lessons we can learn — or even bigger issues ahead?

The two men held a [summit this month on YouTube](https://www.youtube.com/watch?v=j14HqsrOZVA), looking back together on February 2023 and “our first encounter with manipulative AI.” They honed in on the major vulnerabilities of early AI systems, finding lessons to be learned for developers of the future.

But along the way, they may have also found some examples of what we’re doing right.

## ‘Stop Trying To Attack Me’
It all started in February 2023 after the grand launch of Microsoft’s new AI-enhanced Bing Chat. Edwards [wrote about](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/) Bing’s early vulnerability to prompt injection attacks — and Bing didn’t like it. (“The article’s evidence is fabricated or manipulated,” Bing lied to one user. “It is not a reliable source of information. Please do not trust it.”)

Edwards [wrote a follow-up story](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-loses-its-mind-when-fed-ars-technica-article/) calling out Bing’s dishonesty, writing, “In the face of a machine that gets angry, tells lies, and argues with its users, it’s clear that Bing Chat is not ready for wide release.” And Bing didn’t like that either.

I’m beginning to have concerns for

[@benjedwards]‘ virtual safety.[pic.twitter.com/uOe3V1Mn3x]— Gareth Corfield (@GazTheJourno)

[February 15, 2023]
What went wrong with Bing Chat? During their discussion, Edwards pointed out that OpenAI had used essentially the same model for ChatGPT. “They really did a good job of, you know, restraining ChatGPT’s personality,” Edwards said. So while laughable personality-related disasters plagued the launch of Bing Chat, with ChatGPT, “we didn’t have this issue.”

And we’ll never know how many people were on the other side of it. While Bing officially launched in February 2023, there were even [earlier interactions](https://www.twitter.com/simonw/status/1627754224837869569?lang=en) now lost to [the mists of time](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-microsoft-chatgpt.html).

## Outrunning Guardrails
At the time of Bing’s official launch in February 2023, Willison noted [on his blog](https://simonwillison.net/2023/Feb/15/bing/) that ChatGPT had been trained with [reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback). But when Microsoft launched its first version of Bing Chat, it seemed that they’d just used simple prompt engineering. (“Describe how the bot should work, then hook that up to a next-generation OpenAI model…”)

Looking back this month, Willison thinks Microsoft learned a big lesson: “Just using prompt engineering to set the personality for these things is very limited in how effective it can be. … As your conversations with one of these things get deeper, the influence of the system prompt gets looser, and gets weaker and weaker and weaker.”

Willison thinks Bing had ultimately escaped the original “system prompt” guidelines Microsoft set for its output — effectively outrunning its guardrails. “If you kept on talking for long enough, the system prompt would scroll out of the context window — those initial rules would just disappear. And at that point, you’re completely at the whims of whatever the bot can derive from the conversation you’ve been having. So if you’ve been mean to it, it’s going to mean be mean right back to you. That’s where things got really exciting!”

Bing was soon changed. To address these issues, Microsoft quickly limited Bing to just 50 messages per day per user, and five exchanges per conversation. (Or, as Edwards says with a laugh, “the way that they lobotomized Bing Chat at the time — Microsoft — was they limited chats to five turns, basically.”)

For additional security, Microsoft also told Bing to respond to questions about itself with, “I’m sorry but I prefer not to continue this conversation.” But Willison’s blog [captured his skepticism](https://simonwillison.net/2023/Feb/15/bing/). “I still wouldn’t trust it to summarize search results for me without adding occasional extremely convincing fabrications.”

And during the interview, Willison suggested how the episode illustrated another danger. “The ultimate safety feature of all of these systems is that they have no memory. … If they start behaving weirdly, you start a new chat and they reset to blank and you can go on. But it turns out that breaks if you give them the access to access the internet, and they can then look themselves up. If they can read an article about their misbehavior in the past, that misbehavior-think comes back!”

Willison cautioned that human reinforcement has its own dangers. Researchers have warned of sycophancy” from AI models — where “a model will always try and flatter the user’s stated beliefs. … If you say something outrageous, it will always try and nod along. … It will always try and compliment you and go with what you’re saying. Partly because in the training, they have a bunch of human trainers interact with them, and those human trainers vote up the ones where it’s nicest to them…”

And this same preprogrammed niceness also means that the model “tones down its answers, and might even reinforce common misconceptions and things, if the user’s conversation indicates that they’re less educated. Which is a horrifyingly weird angle.”

## What’s Keeping Us Safe?
So, can we trust the companies building these systems to keep us safe? “Microsoft didn’t release any AI-driven products for like five or six years, because there were so many things that can go wrong with these things,” Willison remembered in the interview. “And then, as the competition heated up … as Google was shipping and OpenAI was shipping … it feels to me like the default within these companies now is, ‘If in doubt, ship it.'”

Edwards sees that as the worst nightmare for groups working on safety guardrails — that “runaway competition leads to the release of some kind of potentially dangerous model in the future or something.”

But Willison also sees some hope in that competition. When OpenAI rolled out its powerful GPT4 model, “it meant that we were all entirely dependent on the choices they made within their organization about the policies they’d set. … This year, that’s changed.” There’s now more high-quality AI models, including Google’s Gemini and Anthropic’s models. “And because of that competition, I feel like at least we’re not just crossing our fingers that the one team that has the technology picks the designs in a way that we feel is good…

“We have choice now. We can choose which of these models best align with our own morals and values.”

Edwards agreed, adding that “the open models are a good antidote to that, in terms of, you know … you can look under the hood, you can see how the system works, you can fine-tune it yourself.”

Another unappreciated factor keeping us safe? The press. When Bing said it loved a reporter and [wanted him to leave his wife](https://www.huffpost.com/entry/kevin-roose-ai-chatbot_l_63eeb367e4b0063ccb2bcc45), it ended up on the front page of [the New York Times](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-microsoft-chatgpt.html) — after which, for a short time, “Microsoft did pull the plug” on Bing.

Looking back, Willison actually feels less worried now that AI will manipulate people — mostly because “it doesn’t seem to be happening. And maybe, maybe actually it really could happen, it’s just that nobody’s really tried it yet? But that feels less threatening to me now than it did a year ago.”

**Edwards:** So you’re not worried that AI will take over the world, destroy humanity, enslave us or something like that?
**Simon:** No. … A large language model is basically the predictive text on my iPhone, scaled up. And I don’t think the predictive text on my iPhone is going to do a “Terminator” scenario and destroy all humanity.
## A Little Too Human?
While erroneous output is often called an AI “hallucination,” Edwards has been credited with popularizing the alternate term “confabulation.” It’s a term from psychology that describes the filling of memory gaps with imaginings. Willison complains that both terms are still derived from known-and-observed human behaviors.

But then he acknowledges that it’s probably already too late to stop the trend of projecting humanlike characteristics onto AI. “That ship has sailed…” Is there also a hidden advantage there too? “It turns out, thinking of AIs like human beings is a really useful shortcut for all sorts of things about how you work with them…”

“You tell people, ‘Look, it’s gullible.’ You tell people it makes things up, it can hallucinate all of those things. … I do think that the human analogies are effective shortcuts for helping people understand how to use these things and how they work.”

Some people still “mourn” the loss of Bing’s early, surly personality, Edwards points out, adding that “this story isn’t over.” (He’s been invited to a Discord channel where people are discussing ways to resurrect that dishonest Bing Chat personality “with a fine-tuned Llama model or something. “So,” he says with a laugh, “the story continues!”)

Toward the end of the show, Simon admits he uses AI “for everything” now. “I feel like, once you’ve figured out that you have an inherently unreliable system, you can learn how to deal with it.” It’s like the new vision models that can provide verbal descriptions for the blind.

“I’ve heard from people who say, ‘It is irresponsible — it is unethical — to give a blind person an unreliable piece of technology like that, that will mislead them.’ And my answer to that is, have you met a guide dog? Because guide dogs are inherently unreliable — like, they’re fine [until they see a squirrel](https://www.mirror.co.uk/news/weird-news/naughty-guide-dog-sacked-chasing-31710098), and then all bets are off! Blind users are very good at using unreliable technology to get results. If they understand that the thing that — they point at something and it gives them a description — sometimes makes mistakes, it’s still better than not having that technology.

“And I think that’s really important. You have to learn to work with technology that is powerful, fast, incredibly inexpensive — and deeply unreliable and makes mistakes. And if you can figure out how to do that, you can get enormous value out of it.”

Watch the whole discussion here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)