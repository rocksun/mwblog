I have never been too focused on open source project details and licensing, despite working around colleagues who are very concerned with these issues. So while I was intrigued by the sudden spat within the Ruby community, this post will not be a history of Ruby gems, a study of the motivations of Ruby Central, or the personal politics of David Heinemeier Hansson (DHH). You can read all the “he said, she said” in [our analysis post](https://thenewstack.io/open-source-turmoil-rubygems-maintainers-kicked-off-github/), or from a recent article in [404 Media](https://www.404media.co/how-ruby-went-off-the-rails/). This post is about **how a developer should approach any risk in software, and what it looks like.**

I will note that the infrastructure service of Ruby Central may have become too important for Shopify, the primary sponsor and funder, to keep trusting the creative open source community.

I will also add that I, personally, use both Ruby and Rails. I’ve depended on them in paid gigs and I’ve used Bundler to sort out my gems and the team’s gems. Actually, I have been on some open source conversations concerning Ruby — on the future of [Ruby Shoes](http://shoesrb.com/), whose maintainer famously [disappeared](https://www.slate.com/articles/technology/technology/2012/03/ruby_ruby_on_rails_and__why_the_disappearance_of_one_of_the_world_s_most_beloved_computer_programmers_.html). I’ve also been on the other side of the room, when Oracle took over Sun Microsystems and developers discovered, to their horror, that Larry Ellison owned Java.

## The Paradox of Successful Open Source Software

The open source development community made the software industry possible, but ironically, some of these languages, systems and tools became so financially valuable that they have become subject to more scrutiny and pressure — and needed resources to withstand the threats.

The open source model works because once a problem is understood and solved, that solution can be shared in a library or package, as an ongoing understanding. But that’s just the beginning of things. The package has to be stored, updated and maintained. As they get updated, someone also has to understand which versions of packages still work with each other.

We tend to think of open source software that we use as having been handed down from a Higher Place and maintained by fiat. Of course, they are usually maintained by volunteers who are all too happy to accept some well-needed funding. Meanwhile, working developers naively assume that personalities, ego and money play no part in their favourite languages and tools.

## Understanding Fiduciary Duty and Trust in Software

One of the symptoms of a complex society is that the formal and the informal can appear to exist together. If I buy fruit in a street market and it makes me sick, that would appear to be something I can’t do anything about. But actually, you might have recourse to a local environmental health office, and the market probably has a manager too. What I’m getting at is that even though you haven’t agreed on a contract, there are still legal expectations. Behind all this is the flows and eddies of trust, which underly absolutely all forms of commerce. Markets need the trust of consumers and vendors. Towns need the trust of markets.

> Open source software is like a patchwork quilt — everything is embedded in a community, and that is the foundation of our trust. But the edges abut unevenly.

When a company owns software, corporate law and responsibility make the rights of the consumer quite straightforward. While corporations like Microsoft are largely faceless, they are held rigidly in place by the law, and we can trust that to a certain extent. Open source software is more like a patchwork quilt. Everything is embedded in a community, and that is the foundation of our trust. But the edges abut unevenly.

## Assessing Modern Software Supply Chain Risks

Ruby Central blamed supply chain attacks for their need to take sudden control. Today, supply chain risks are very real. Before thinking of these, just consider the [CrowdStrike](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages) issue. One bad update helped crashed over 8 million systems and resulted in a huge financial loss for airports. This was not the result of a cyberattack or any form of organized malfeasance. Yet Delta Air Lines filed a $500 million lawsuit against CrowdStrike, alleging gross negligence and deceptive business practices. Delta claimed that CrowdStrike deployed untested software updates.

Today the car supplier [Jaguar Land Rover](https://www.autocar.co.uk/car-news/new-cars/jlr-prepares-build-first-cars-august-coming-days) is fighting a cyberattack. This actually threatens the health of third-party suppliers, which don’t have alternative buyers for their parts. On a more familiar level, I talked about the [VSX attack](https://thenewstack.io/agentic-coding-and-the-weakness-of-extensions-for-ides/) a couple of months ago.

One simply doesn’t need to throw in the final factor, enemy State interference, to see the issues.

## How Developers Can Mitigate Technology Risks

So what’s a dev supposed to do? The first thing is not to dedicate yourself to being a “Rails dev.” Be a developer who has a solid understanding of the MVC model, backed by practical experience of Rails and maybe community activity. Don’t hold your enthusiasm above what your client or employer needs. If you like the opinionated nature of Rails, encourage it elsewhere. You like Ruby? Who doesn’t! But be prepared to use Python with Django instead of Rails. While the actions of DHH might be relevant to how you feel, you will discover that projects like Rails have many leaders.

> You like Ruby? Who doesn’t! But be prepared to use Python with Django instead of Rails.

Appreciate all the risks in your [entire workflow chain](https://buttondown.com/dorian/archive/supply-chain-risks-in-late-2025/). This initially sounds like an academic job or something for management. If you are approaching senior level, this is largely *your* job. Your manager will defer to you if you have proved that you grok both the company’s goals and how development can be improved. If you simply think “Rust is cool,” that won’t cut it. Your chain means literally everything that goes into making the product. And “risk” means any change (from pricing to controlling companies) that would impact the product.

## Build a Career on Concepts, Not Specific Tools

The simplest professional way to practically deal with risk is to know how to replace everything on your chain, and what off-the-shelf or community-driven projects are making the running and why. If you work with corporate products where the company is a peer competitor, that is a risk; if you work with community products that aren’t transparent, that is also a risk. Develop a curiosity for what makes companies make poor decisions. And be honest with your own record; have you trusted people in the industry who later let you down?

Every action with a goal has at least one risk assessment attached to it. We’ve all headed out to a shop that may be shut and worked out what the alternatives are. But we all use trust to make the final decision on likely outcomes.

> Don’t get into one programming language — get into its aims. Speed, parallelism, range, etc.

So don’t get into one programming language — get into its aims — speed, parallelism, range, etc. Then appreciate how the language hits those goals. I like C#. I like the way it improves on Java. I appreciate that because Microsoft has backed it, it is stable. But what if they get into Rust? By looking into Rust, maybe I can mitigate the risk by removing doubt in my mind — or understanding what some [Microsoft developers might be seeing](https://thenewstack.io/microsoft-goes-all-in-on-rust-for-core-infrastructure-and-much-more/).

## Be a Community Member, Not Just a Consumer

As we know, software can be backed by large companies or open source communities. For this reason, developers must understand whether they are acting as consumers or community members.

If your relationship with software is as a consumer, you have rights and expectations. There is a solid edifice you can throw eggs at. You can complain on social media. Ultimately, shareholders fear you.

If your relationship is that you are using open source, you are part of the community. Start elbowing your way in. This is how you will be seen by your peers, and ultimately rated as a developer. The reason why software still has open source communities is that a developer is part craftsperson, part enthusiast, part gardener.

But ultimately it’s about developing trust relationships that go underneath superficial marketing or personalities. Take the time to understand the environment. If you build things with software, you aren’t a passive ghost.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)