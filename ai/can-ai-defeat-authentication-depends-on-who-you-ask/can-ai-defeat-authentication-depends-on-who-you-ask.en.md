Speaking at the U.S. Federal Reserve last month,  [OpenAI CEO Sam Altman](https://thenewstack.io/openais-sam-altman-ai-is-now-ready-for-the-enterprise/) warned of a “fraud crisis,” in that AI will soon be able to fool authentication methods built into most applications.

“A thing that terrifies me is apparently there are still some financial institutions that will accept a voice print as authentication for you to move a lot of money or do something else — you say a challenge phrase, and they just do it,” Altman said, as [reported by CNN](https://edition.cnn.com/2025/07/22/tech/openai-sam-altman-fraud-crisis). “That is a crazy thing to still be doing… AI has fully defeated most of the ways that people authenticate currently, other than passwords.”

But if AI has “defeated” authentication, as Altman claimed, the CEO/co-founder of authentication platform [Stytch](https://stytch.com/) disagrees.

In a new interview, Stytch’s [Reed McGinley-Stempel](https://www.linkedin.com/in/reed-mcginley-stempel-17362245/) told us what’s working (and what’s not) right now in the authentication sector. And yes, if historical trends repeat, AI may give bad actors some new tools — but that’s only the first phase.

So while Altman predicts a “significant impending fraud crisis”, there’s another side to this story. AI has also helped Stytch harden their authentication solutions “under the hood,” their CEO says — and could one day even give defenders the upper hand.

## The Worst and the Best

OpenAI’s CEO had first warned that some financial institutions still use voiceprints for authentication, despite researchers discovering [ways to bypass it](https://uwaterloo.ca/news/media/how-secure-are-voice-authentication-systems-really). And Stytch’s CEO said  “I wholeheartedly agree. It’s one of the worst authentication methods available.” (AI can already generate realistic deepfakes — so how hard would it be to finetune an audio samples of someone’s voice enough to bypass a voice security system?)

But he disagrees with Altman’s claim that “AI has fully defeated most of the ways that people authenticate currently, other than passwords…” Just for example, one common way of authentication is with “something you have” — like how financial sites offer to remember your device. Even if AI can mimic your voice or replicate your face — it’d be far trickier to fabricate the unique signature of your device’s IP address and stored cookies. And that’s especially useful, since most fraud happens remotely online.

“AI will not be able to beat this…” McGinley-Stempel says. No matter how good AI tools become, “one thing you can still control with just current technology… is you can decide, ‘Is this authentication coming from the same device that it previously was enrolled in?'” And then couple that with biometric passkeys — whether bound to your device, or just synced to your iCloud account. Even in our resource-constrained world, “Honestly, it’s a pretty easy lift to do for companies.”

## Will Passwords Protect You?

McGinley-Stempel takes issue with Altman’s remarks in another way. “I disagree with him that passwords are a last great hope — they’re not.” It’s not that AI also has superpowers for deducing your password. But “the problem I see is the phishing efforts are getting so much more sophisticated.”

The cybersecurity company Darktrace found one unexpected side effect of the arrival of ChatGPT: [phishing emails suddenly started getting better](https://www.darktrace.com/blog/email-attack-trends-how-phishing-attacks-are-becoming-more-sophisticated-and-harder-to-identify). They’re longer, more linguistically complex, and just plain more convincing. Telltale signals like bad grammar and common English mistakes will be less frequent, notes McGinley-Stempel.

But AI helps attackers in other ways. “The other thing we’re seeing is more phishing websites are having to be taken down than ever — because anyone can go vibe code a fake ‘Bank of America’ landing page!” And it’s not just websites phishing for passwords or the passcodes that come with phones — but also AI-generated emails and text messages. There’s even been [news](https://www.azfamily.com/2023/04/10/ive-got-your-daughter-scottsdale-mom-warns-close-encounter-with-ai-voice-cloning-scam/) [reports](https://www.cbsnews.com/news/elder-scams-family-safe-word/) of faked voice calls using AI-powered voice-cloning tools.

Stytch primarily works on authentication solutions, so McGinley-Stempel admits he just doesn’t have a good sense of how other players are securing our government-standard identifications. Although “If folks start creating fake birth certificates, passports, licenses — I’m sure the government will catch up at some point. But I’m wondering how long that will take.”

## When Fraud Gets Democratized…

Speaking more generally, McGinley-Stempel says there’s a big change coming with AI-power fraud. “It democratizes coding, and so therefore it democratizes abuse.” (While it’s difficult to say whether fraudulent actors will increase 10X or 100X, there’s a clear return on investment, especially in countries where there’s “low-enforcement” of prosecutions against fraudsters targeting people in other countries.)

“I do think that crescendo is going to land,” he says, though “I don’t know if that will be next month, next year…” But he is worried that [the release of ChatGPT-5](https://www.cnbc.com/2025/08/07/openai-launches-gpt-5-model-for-all-chatgpt-users.html) could bring “a huge change.”

Security is an issue people tend to kick down the road until there’s a major incident that’s “all over the news cycle… Change typically then actually happens.” Whether it’s government agencies or companies needing security, “it feels to me like we’re in the part of the fraud crisis curve where actually a lot of people see it coming — but a lot of people are also really busy with other things they’re doing.” They may be doing things that are “helping to a degree,” McGinley-Stempel says, but “they’re probably just not solving the ultimate risk.”

It’s a general principle of many new technologies. “Typically, what we find is fraudsters adopt new technologies faster than legitimate users… And defenders ultimately, generally, get it to a good enough stasis where things are all right… there’s kind of an equilibrium after that.”

The part he worries about is that first phase. What happens when fraudsters adopt today’s cutting-edge tools, and “AI is giving them superpowers — it’s expanding who can be a fraud actor.”

And even then — will the historical parallel repeat with AI? “I don’t know what will happen one way or another,” McGinley-Stempel acknowledges, but AI “feels like a different beast.”

Just to illustrate the point, imagine the scenario where we’ve finally developed artificial general intelligence — and where fraudsters are faster at using it than defenders. There’s the possibility that “even if defenders catch up — you know, a year later, six months later — that’s still a lot of room for damage in terms of something going very, very wrong.”

## AI Fighting AI?

But it’s not all bad. “AI is going to create a fraud crisis, but it’s also going to remove a lot of tedium from people’s lives,” McGinley-Stempel says. “One of the tools that we have allows end users to authenticate AI agents, to operate on their behalf… like good, sanctioned AI agents!”

And what’s interesting is Stytch is actually *using* machine learning to help fend off unwanted AI agents (as well as the scraping bots that feed [LLMs](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/)).

Stytch’s authentication platform has always made it easy to build “really, really secure but also low-friction signup and login experiences.” (This includes supporting common standards like Google passwords and Apple’s [Face ID](https://en.wikipedia.org/wiki/Face_ID) and [Touch ID](https://en.wikipedia.org/wiki/Touch_ID).) But on top of that there’s also their additional bot-mitigation technology which McGinley-Stempel says “helps us fingerprint every piece of traffic that comes to our customer’s site — tell you if this is the same device that you’ve seen previously. If it’s a new device, is this a human? Is this an AI agent? Is it a good agent or is it a bad agent or is it just a general bot, like a script bot…? We’re collecting hundreds of signals on a device when it gets fingerprinted invisibly.”

But they’re now training their model on every version of the major web browsers — going back decades — “on the widest set of possible emulated devices that a real user would run these browsers on.” Effectively, this creates “the verified set for each version of each browser — what does the exact fingerprint profile look like?” This allows Stych to automatically spot any suspicious “drift” from their “verified proofs”.

In short, McGinley-Stempel says, “AI and ML help us build a better ‘lie detector’ test for traffic on the Internet.”

While some other companies may be using machine learning for things like verifying CAPTCHA responses, “I’ve not heard of anyone doing what we’re doing on the browser side. We’re bringing ML and AI… to determine real versus fake browsers!”

McGinley-Stempel calls it using AI “under the hood…

## Security vs. Cost

It’s not a question of whether we’ll have technology for authentication, McGinley-Stempel believes. “The thing I am worried about is whether it will always be *cheap enough* for every application and website to remain secure.” Companies have to calculate their security budget — after all, some sites won’t be attacked “as ardently as others…” McGinley-Stempel acknowledges. “It’s almost like you’re being an underwriter for your own risk. If you get that calculation wrong, that’s where you’re still going to see breaches in the news and things like that… ”

Meanwhile, attackers are also calculating their estimated return on investments. So in the middle of these two calculations, “Because it is expensive, If they want us to use AI to continually defend against AI — it’s going to become like a game theory problem.”

But the Stytch CEO still sees some hope for the future.

There’s a joke that ends “I don’t need to be faster than the bear. I just need to be faster than the *other guy* running from the bear.” And that’s how many companies think about security, McGinley-Stempel says — hoping someone else ends up becoming the easier target. “That has always been the case, actually.”

But are we on the cusp of something better? Once we’ve made our adjustments to AI-powered attackers, “AI on the defensive side theoretically gives us *unlimited* human hours, if we’re willing to invest in it — to research problems. To research, like, dark web forums where people usually talk about how they’re defrauding different sites and different people.”

And so “I think it is possible,” the Stytch CEO says, looking toward the future. “Though I don’t know if we’ll absolutely do it, it is possible we end up building a much more secure layer on the internet in the next few years.

“Even if we have a fraud crisis that balloons in the first 6 to 12 months…. ”

In short, AI could offer all the resources we need to — cheaply and at scale — finally build a world that’s authenticated and secure for everyone.

A world where *both* people can finally outrun the bear.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)