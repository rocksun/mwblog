Jan Lehnardt said it best in a [Mastodon post](https://sunny.garden/@janl@narrativ.es/115230600679633623): “What the f\*\*\* is going on with Ruby?”

What’s going on is the RubyGems community is upset after maintainers were kicked off the GitHub repository late last week. RubyGems are packages of reusable Ruby code and other components, used to add functionality to a Ruby project. They are the standard package manager for the Ruby language.

Earlier this month, Ruby Central replaced all maintainers with its Director of Open Source [Marty Haught](https://github.com/mghaught). Ruby Central is a non-profit organization committed to “driving innovation and building community within the Ruby programming ecosystem since 2001.” It also runs both RubyConf, the world’s largest Ruby conference, and RailsConf.

## Community Safeguarding or Hostile Takeover?

If the goal is to build community, Ruby Central may have made a serious misstep. On Sept. 9, without explanation, an anonymous RubyGems maintainer renamed the RubyGems GitHub enterprise to Ruby Central, added Ruby Central’s Director of Open Source Marty Haught as a maintainer, and removed every other maintainer of the RubyGems project, according to maintainer [Ellen Dash](https://github.com/duckinator), aka [Puppy or duckinator](https://bsky.app/profile/duckinator.bsky.social).

On Sept. 15, the anonymous maintainer said he/she restored the previous permissions after talking with Haught, who Dash reported had said the deletion was a mistake that “should never have happened.”

“The ‘restoration’ kept a notable change: Marty was now an owner of the GitHub enterprise,” Dash wrote. “The RubyGems team responded by immediately began putting in place an overdue official governance policy, inspired [by Homebrew’s](https://github.com/rubygems/rfcs/pull/61).”

But on Sept. 18, with no explanation, she wrote that Haught revoked GitHub organization membership for all admins on the RubyGems, Bundler and RubyGems.org maintainer teams.

“By doing this, he took control for himself and other full-time employees of Ruby Central,” [Dash wrote in a goodbye to RubyGems post](https://pup-e.com/goodbye-rubygems.pdf) shared on social media. “Later that day, after refusing to restore GitHub permissions, Ruby Central further revoked access to the bundler and rubygems-update gems on RubyGems.org.

“I will not mince words here: This was a hostile takeover.”

## Ruby Non-Profit Cites Fiduciary Duty

On Sept. 19, [Ruby Central posted an explanation](https://rubycentral.org/news/strengthening-the-stewardship-of-rubygems-and-bundler/) for its actions, citing security concerns and related fiduciary duty as the driver for this decision.

“As the nonprofit steward of this infrastructure, Ruby Central has a fiduciary duty to safeguard the supply chain and protect the long-term stability of the ecosystem,” stated the Ruby Central post, which is not credited to any individual.

“In consultation with legal counsel and following a recent security audit, we are strengthening our governance processes, formalizing operator agreements, and tightening access to production systems,” it continued. “Moving forward, only engineers employed or contracted by Ruby Central will hold administrative permissions to the RubyGems.org service.”

Ruby Central also cited [software supply chain attacks](https://thenewstack.io/lessons-learned-from-2021-software-supply-chain-attacks/) as requiring “proactive steps to safeguard the Ruby gem ecosystem end to end.”

[Freedom Dumlao](http://linkedin.com/in/freedomdumlao), a Ruby Central board member and CTO for Vestmark, also explained [why security issues required the action](https://apiguy.substack.com/p/a-board-members-perspective-of-the?r=43k3q&utm_medium=ios&triedRedirect=true).

“Ruby Central has been responsible for RubyGems and Bundler for a long time. This isn’t a new development, and I’m honestly very confused about the confusion,” he wrote. “What isn’t confusing is that [supply chains are under attack](https://thenewstack.io/how-supply-chain-attackers-maximize-their-blast-radius/). We can see this in recent attacks on RubyGems and also in major attacks on other ecosystems that have made global news. Companies that depend on Ruby count on Ruby Central to ensure they are not at risk. Some of those companies are sponsors of Ruby Central and some are not, but all have a legitimate need to know that they can tell their users that the software they are using is safe.”

But the news hasn’t been well-received as Ruby developers took to social media and blogs to express their frustration and sometimes outrage with Ruby Central’s move.

## Community Response to Ruby Central’s Actions

“’Fiduciary responsibility’ is a hell of a euphemism for ‘we were offered millions of dollars from a hostile donor in exchange for control of the RubyGems infrastructure,’” [Sam Stephenson](https://indieweb.social/@sstephenson), a Chicago-based developer, [posted to Mastodon](https://indieweb.social/@sstephenson/115231391147943333). He did not say who that hostile donor might be.

[![A screenshot of Sam Stephenson's Mastodon comment on 'Fiduciary responsibility' is a hell of a euphemism for 'we were offered millions of dollars from a hostile donor in exchange for control of the RubyGems infrastructure.'"](https://cdn.thenewstack.io/media/2025/09/5dd99225-samstephensonrubygemscomment.jpg)](https://cdn.thenewstack.io/media/2025/09/5dd99225-samstephensonrubygemscomment.jpg)

Screenshot from [Mastodon](https://indieweb.social/@sstephenson/115231391147943333).

He wasn’t alone in his condemnation. [Mike Perham](https://github.com/mperham) is a self-described Rubyist and the creator of [@sidekiq](https://github.com/sidekiq/sidekiq) , a popular, open source Ruby framework for running background jobs, and [Faktory](https://github.com/contribsys/faktory), a language-agnostic persistent background job server. He was among those who saw [the move as overreach](https://www.reddit.com/r/ruby/comments/1nmzqq2/comment/nfoaj3w/) on Ruby Central’s part.

“Ruby Central does not own the copyright of the RubyGems source and that repo existed before Ruby Central. Ruby Central’s role is to manage the rubygems.org infrastructure and pay for the ongoing maintenance of RubyGems,” he said. “RC does not control who is a maintainer and who is allowed on the maintenance staff. Like any OSS project, that has always been a team decision.”

Ruby Central needs to provide the community with more information, he added.

“We can only speculate about actual reasons until you tell us the sponsor and their demand. This change demands sunlight,” he stated. “rubygems/rubygems was not under control of Ruby Central until hsbt removed the entire existing team and added Marty [Haught] as an admin, unilaterally, without discussion. That was an illegal power grab. That action should have been a public process, not a back room deal.”

[![Mike McQuaid's thoughts on the brouhaha between Ruby Central and RubyGems maintainers.](https://cdn.thenewstack.io/media/2025/09/f73eee71-mike_mcquaid.jpg)](https://cdn.thenewstack.io/media/2025/09/f73eee71-mike_mcquaid.jpg)

Screenshot from [Mastodon](https://sunny.garden/@mikemcquaid@mastodon.social/115246937754924431).

“I didn’t see a way to keep it from getting worse, so I stepped down and documented what I saw,” Dash said in a [Bluesky response](https://bsky.app/profile/duckinator.bsky.social/post/3lz7mwj3lmk2y) to engineer [Mike McQuaid](https://github.com/mikemcquaid), who tried — and failed — to [broker a discussion](https://sunny.garden/@mikemcquaid@mastodon.social/115246934696920846) between RubyCentral and maintainers over the issue. “I gave that project a third of my f\*\*\*-ing life and I had to explain that I failed it. It hurts in a way I can’t describe.”

## A Video and a Promise for More Communication

On Monday, Ruby Central scheduled a Q&A session for the community but announced late in the afternoon that the session would be rescheduled due to Rosh Hashanah. In the meantime, Executive Director Shan Cureton, who joined the organization in May, released a [video message on YouTube](https://www.youtube.com/watch?v=VyCiE3GjQps).

She apologized for the poor communications and the confusion it created. She explained why it was necessary from Ruby Central’s point of view.

“When Bundler and RubyGems came under our responsibility through the merger with Ruby together, it came with operational risk, legal responsibility, and practical obligations,” she said. “Unfortunately, the merger left governance liability and operational gaps that we are now closing.”

Cureton noted that in recent weeks, roles and responsibilities had changed and there were [sponsor questions about supply chain](https://thenewstack.io/the-challenges-of-securing-the-open-source-supply-chain/) risk that made one thing clear: Ruby Central needed to close governance and access gaps quickly.

“With the departure of a lead maintainer and a transition of security engineer, questions around administrative access to RubyGems bundler and rubygems … became urgent,” she said. “We had already started these discussions with the current maintainers about how to strengthen the governance and access controls. We value their contributions deeply, but it became clear that we couldn’t reach agreement on the steps needed to address security and liability concerns in the timeline that we were facing.”

Ruby Central also cited [software supply chain](https://thenewstack.io/get-a-handle-on-software-supply-chain-security-with-lfx/) attacks as requiring “proactive steps to safeguard the rubygem ecosystem end to end. As a result of these concerns, Ruby Central’s board voted to temporarily remove “certain administrative and commit privileges until agreements could be put in place,” she said.

“This decision was never meant to be permanent,” Cureton said. “It was about shoring up protections, buying us the time we needed to set agreements, and doing right by the community and the companies that depend on us.”

Meanwhile, she added, normal publishing and installation continue.

> “This decision was never meant to be permanent. It was about shoring up protections, buying us the time we needed to set agreements, and doing right by the community and the companies that depend on us.”  
> **– Ruby Central Executive Director Shan Cureton**

“As Ruby Central’s executive director, I’ve been tasked with getting the organization into truly sustainable shape. This means not only stabilizing how we operate as an organization, but also strengthening how we govern and maintain open source infrastructure,” she said. “When we began reviewing our practices, it became clear that we needed stronger security pro protocols and clearer governance in RubyGems and Bundler.”

She added that Ruby Central has recently began hiring staff, and that triggered new responsibilities and protocols around offboarding and stronger security controls for an organization historically ran by volunteers and independent contractors.

These steps were about more than risk mitigation, she added.

“They’re about making sure that Ruby Central remains sustainable and able to serve the Ruby community,” she said.

She made clear two things: First, permissions are restricted only temporarily while Ruby Central finalizes operator and contributor agreements; and, second, this is the first time Ruby Central has put these legally binding agreements in place for maintainers.

## The RubyGems Problem for Ruby Central

“In most [open source projects](https://thenewstack.io/what-to-do-when-critical-open-source-projects-go-end-of-life/) where the code is a library or framework, you usually don’t see formal operator agreements,” Cureton said. “People contribute under contributor license agreements, codes of conduct, or decisions made by a steering community. But rubygems.org is different. It’s not just code. It’s a production service. It runs critical infrastructure for the Ruby ecosystem, processes billions of downloads, stores sensitive metadata, and is relied on by companies that have compliance requirements.”

Because it’s a service, Ruby Central carries legal liability, financial exposure and operational risk, according to Curetan.

“This is why operator agreements are necessary. They ensure access is tied to responsibility and accountability,” she said. “While you may not see them in projects like Rails or React, they’re the norm in services like npm, pi, or Docker Hub. RubyGems.”

“I want to acknowledge that the way that the process played out felt very abrupt and we regret that,” she said. “Our mission has always been about protecting the community, protecting the ecosystem, and building a stronger foundation for the future. ”

Comments were turned off on the YouTube video.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)