# Is Crypto the Solution To Paying Open Source Developers?
![Featued image for: Is Crypto the Solution To Paying Open Source Developers?](https://cdn.thenewstack.io/media/2024/12/3238eb29-tea-protocol-logo-1024x576.png)
RALEIGH, N.C. — The whole world runs on open source software, but far too much of that software is not only free but [maintained by unpaid hobbyists](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/).

It’s a problem [Max Howell](https://www.linkedin.com/in/mxcl/) knows all too well.

Howell created [Homebrew](https://brew.sh/), the widely used open source package manager for Linux and MacOS. Introduced to the world in 2009, Howell built the project in stolen moments.

“I worked on Homebrew on and off because I needed to pay the rent,” he told The New Stack at [All Things Open](https://2025.allthingsopen.org/) in October. “So I’d save up money and then quit, in order to work on it for an extended period of time.”

![XKCD comic "Dependency"](https://cdn.thenewstack.io/media/2021/12/179b8373-xkcd-dependency.png)
The “Nebraska problem,” illustrated. (Source: xkcd)

Since 2021, he’s been working on solving what’s known as the “Nebraska problem,” as illustrated in this famous xkcd cartoon: vital [open source projects](https://thenewstack.io/open-source/) that “some random person in Nebraska has been thanklessly maintaining since 2003.”

He’d been looking for a way to help [developers spend more or even all of their time maintaining open source software](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/).

“Three years ago, I became frustrated,” Howell said. “So I should try and come up with something myself.”

With [Timothy Lewis](https://www.linkedin.com/in/timothythomaslewis/), he co-founded [tea](https://tea.xyz/), a protocol for a decentralized (i.e. [Web3](https://thenewstack.io/its-a-web3-world-now-how-the-hype-compares-to-web-2-0/)) technology framework. ([Lewis recently took the role of CEO](https://www.businesswire.com/news/home/20241108214004/en/tea-Welcomes-New-Leadership-to-Drive-Open-Source-Vision-and-Unveils-CHAI-The-First-Universal-Impact-Ranking-Solution-for-Open-Source); Howell is the chief open source officer.) At All Things Open, tea officially unveiled [Chai](https://teaxyz.acemlnb.com/lt.php?x=3TxtmrUFUqPUT55qA1c5Zwar_n7Xz~gVkypZgIMKUnLN6qi26gc7hu14PaWeiNDxnuY3YIHMMnGb6H_), an open source tool designed to not only map the open source ecosystem but also help maintainers earn tokens that Howell and his supporters believe will have intrinsic (i.e., monetary) value.

Tea is also building tools to help make o[pen source more secure](https://thenewstack.io/are-we-thinking-about-supply-chain-security-all-wrong/) as well as equitable: On Monday, tea released [teaBASE](https://github.com/teaxyz/teaBASE), an open source toolkit that includes features that enable developers to create secure, signed commits and make user-contributed dev tools more easily accessible, according to the company.

TeaBASE includes: cryptographic signing capabilities, package management integration, securityratings, an extension store and dotfile syncing.

But back to Chai. How does it determine which maintainers are working on projects that matter most to the community — and thus deserve rewards for their work?

“Chai uses package manager data,” Howell said. “I realized when founding the company that the data that these package managers had is very useful for developing a graph of impact from the different open source projects based on the dependency information.

“When you make a new open source project, you pick your dependencies. You very rarely have zero dependencies. And picking those dependencies is a careful process. You don’t pick them willy-nilly. You don’t pick things that don’t work or are fake. So it’s very good reputation data, and we realize it’s a similar kind of algorithm to Google’s page rank.”

## The Role of Crypto
Since February, Chai has been running a “testnet” (more on that later) with more than 16,000 open source projects registered, a sliver of the 10.5 million open source projects currently running globally, Howell acknowledged, but a good start. About 1.7 million people are represented in the testnet, he said.

Among the biggest projects represented in the testnet: [Dontenv](https://github.com/motdotla/dotenv), [Husky](https://github.com/typicode/husky) and [Inquirer](https://github.com/SBoudrias/Inquirer.js).

“They’re not getting anything from this,” he said. “They’re just trying it out and helping us to understand if what we’ve built works. The wider developer communities are more skeptical, because crypto is a bad word, right?”

![Max Howell, creator of Homebrew, at All Things Open in October 2024. Howell's new company, tea, aims to make open source more secure and equitable.](https://cdn.thenewstack.io/media/2024/12/0f305cf0-max-howell-1024x981.jpg)
Max Howell, creator of Homebrew, is now focused on rewarding open source maintainers who build valuable software. (Photo of Howell at All Things Open by Heather Jolsyn.)

It’s certainly accumulated more critics in the past couple of years, especially after the[ high-profile fraud and conspiracy convictions](https://www.justice.gov/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes) of [Sam Bankman-Fried](https://www.linkedin.com/in/sam-bankman-fried-8367a346), founder of FTX and Alameda Research, now serving a 25-year prison term.

And yet, cryptocurrency’s value appears to be on the upswing. [The price of a single Bitcoin hit $100,000 for the first time](https://www.nytimes.com/2024/12/04/technology/bitcoin-price-record.html?unlocked_article_code=1.fE4.awxD.YY_GxPtsRLS8&smid=url-share) this past Wednesday.

Howell told TNS he didn’t know much about cryptocurrency before starting tea. “But I’ve learned that, yeah, there are a lot of scams, there are a lot of bad people in the sector. But people have high hopes that projects like ours are the ones that are going to show that it’s just a technology, that it can be used for good as well as for bad.”

To combat that reputation, tea has embraced transparency. “We’re very transparent about how everything works, where the token is going to go when it’s live, and things like that,” he said. “I think the wider developer community will be on board when they see the success stories that we anticipate happening after the main launch. Some of these developers are going to get an awful lot of tokens because they have a lot of very successful projects, and we’ve onboarded them.”

## How Chai Works
So, how does Chai work? It connects package managers across platforms like Homebrew, NPM, PyPl, and more to create a universal graph of open source packages, showing dependencies, relationships and contributions.

It features:

- A database with tables and migrations and an entity relationship diagram (ERD) data exploration.
- Pipelines for crates and Homebrew, showcasing strategies for pulling and transforming data.
- An API to query the graph.
Projects that are signed up with the tea protocol receive rankings based on their package manager activity. “We called the resulting rankings ‘tea rank,’ and you get a ranking for every project in the graph,” Howell said. The open source packages are ranked from zero to 100. “The higher your ranking, the more tea token rewards we give you every 24 hours.”

The system includes guidelines to ensure that developers building valuable software are rewarded. “There’s a lower limit where you get nothing, to ensure that people don’t try and game the system by creating trees of fake packages,” Howell said. “Chai is the on-chain database that we run that calculates those rankings by pulling in all the package manager data and keeping it up to date.”

In the testnet, he said, “We have a test token that has no value.” But the “mainnet,” which will coincide with the generation of tokens meant to have value on the cryptocurrency exchanges, is slated to begin in 2025, at a specific date yet to be announced.

“We don’t know what the value is going to be, but we have targets in mind that we’re trying to hit when we do launch it,” Howell said. “We’re launching with several major exchanges. so we know what we’re trying to get, and our marketing engine is working accordingly to try and get the value attribution that the community thinks it’s worth up to that point. If it reaches that point, then the open source projects that sign up should get a very healthy amount of that token, and then the mission can be achieved.”

## Funding and What’s Ahead
Over the past three years, he said, tea has raised $18 million from investors. The company has previously announced support from Acuitas Group Holdings. Along with Betaworks Ventures, Binance Labs, Percival VC, Round 13 Digital Assets Fund, StrongBlock and Wax Blockchain — all investors with deep roots in the cryptocurrency/digital assets industries.

“We were considering doing another round [of investment] recently, but we’re going to try and launch the token instead,” Howell said.

“Once the tokens live, then the business has mechanisms to use in order to keep it buoyant, at least initially,” he said. “But we’re actually launching it via a separate company to keep the VCs away from the final protocol.”

To launch and govern the tokens, tea has established a nonprofit organization, The Tea Association, in Switzerland, “which is run by people completely separated from our VC pool,” Howell said. A big reason why he’s keeping the nonprofit separate from the venture capitalists who have invested in his company, he said, is to reassure the open source community.

“I want the open source community to trust that the protocol is not being influenced by any of those kinds of people, and that the protocol itself will be run by the open source community in the longer term,” Howell said.

He added, “We want to be open source and transparent in everything we’re doing. We’re an open source company. We are building tools to help the open source community, and we want them to have control and governance over that, to see how it works and contribute.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)