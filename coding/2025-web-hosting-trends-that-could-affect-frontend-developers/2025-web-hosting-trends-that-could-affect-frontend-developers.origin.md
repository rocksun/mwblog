# 2025 Web Hosting Trends That Could Affect Frontend Developers
![Featued image for: 2025 Web Hosting Trends That Could Affect Frontend Developers](https://cdn.thenewstack.io/media/2024/12/c2e50afd-webhostingwires-1024x581.jpg)
The battle between open source web hosting platforms and proprietary platforms will bleed into 2025. That means frontend developers may have to make the case for open source website platforms.

Proprietary platform such as Squarespace and Wix appeal to organizations due to their convenience, but these hosting platforms also lock in users and make migration difficult if business needs change, said [Jon Penland](https://www.linkedin.com/in/jonpenland/), chief operating officer at the WordPress-managed hosting platform [Kinsta](https://kinsta.com/). Open source solutions, on the other hand, provide flexibility and control to both organizations and frontend developers, he said.

Open source projects do come with multiple points of risk, he pointed out — something that recently became awkwardly apparent with the [WordPress/WP Engine drama](https://www.reddit.com/r/webdev/comments/1g4y68w/the_wordpress_vs_wp_engine_drama_and_why_you/).

Even so, developers can make a solid case for [open source solutions](https://thenewstack.io/open-source-winning-over-the-financial-services-industry/), he contended.

“The case, from a developer perspective, is flexibility,” Penland said. “Open source systems in general have been designed to have these bolt-on ways of making modifications to the way that the software operates, adding features, that sort of thing. And from a developer perspective, that’s really the core argument.”

Proprietary platforms limit what organizations can do with their websites — if a feature isn’t supported, organizations are just out of luck, he added. Also, if a proprietary platform deprecates a feature the website relied on, there’s no recourse, whereas with open source, there’s often a third-party tool that can be used.

“In the case of a robust ecosystem like [WordPress](https://thenewstack.io/wordpress-alternatives-stick-with-php-or-pivot-to-javascript/), you can almost always find the tool out there that you can use to implement and develop whatever feature that you want,” he said. “You can build it yourself if you have your own in-house development team. And you’re not at the whims of a third party who may decide this feature is not working for us as well as we had wanted to and it’s not worth the maintenance cost, so we’re going to do away with it.”

The New Stack spoke with Penland about the web trends Kinsta foresees for 2025. While these predictions may not directly [affect your code](https://thenewstack.io/veracode-how-third-party-code-impacts-software-security/), they can affect performance of websites, hinder site migration and raise other issues of concern for frontend developers.

## Containerization Becomes Standard
Developers can, of course, manage their own [containerization](https://thenewstack.io/virtualization-and-containers-better-together/) on platforms such as [AWS and ](https://aws.amazon.com/?utm_content=inline+mention)[Vercel](https://vercel.com/docs/integrations/external-platforms/kubernetes). But increasingly, legacy web platforms will manage containerization for developers, Penland predicted.

Traditionally, the gateway process for web hosting is shared hosting, which takes a single server or single virtual private server (VPS) and divvies up those resources between multiple customers. That approach has drawbacks, according to Penland.

“If you signed up for shared hosting accounts, say you had 50 sites, all of them existed in a single shared environment, so if one site ever had a problem [and] was compromised in some way, you had risk to all of your site,” he said. “Also all of those sites shared software. They shared the same MySQL server; they shared the same PHP software; and if you had any sort of coding issue causing, like, object cache not to be emptied properly, you could actually leak stuff between the different sites that were sharing that code.”

“If you signed up for shared hosting accounts, say you had 50 sites, all of them existed in a single shared environment, so if one site ever had a problem [and] was compromised in some way, you had risk to all of your site.”

—Jon Penland, Kinsta chief operating officer
That raises security concerns, but it also can create performance issues, he added.

“From a hosting management perspective, if that server ran into resource issues, it was very difficult to move sites from one server to a different server because the software wasn’t designed to operate,” he said. “You had to actually migrate the websites individually.”

Kinsta has deployed a containerized infrastructure for approximately five years now and has found that containerization addresses these concerns by basically providing a wrapper around each website that’s hosted. This solves three problems, Penland explained.

First, all the software, such as [MySQL](https://thenewstack.io/deploy-mysql-and-phpmyadmin-with-docker/), is unique to the website, so there are no concerns about problems leaking between websites. Second, if an attacker manages to get into a container, they can’t reach other sites because they’re locked out of those containers. Third, containers by design can be easily moved from one server to another.

“If a host sees a server that’s running into resource issues, it’s much easier to redistribute that load among a variety of servers and not to continue to have this one server struggling for resources,” he said. “Containerization has made hosting more secure and more performant, and as folks experience the difference, it becomes very difficult to go back to that traditional share hosting model.”

## Websites Become a Priority Over Social Media
One prediction that might be of particular interest to small shop or entrepreneur frontend developers is that small- and medium-sized businesses (SMBs) will turn to websites again after experiencing problems with social media platforms.

[Social media platforms like Facebook](https://thenewstack.io/before-facebook-the-late-ward-christensen-booted-up-the-first-social-network/) and Instagram once seemed sufficient to these organizations, but it’s becoming harder to gain visibility on them.
“SMBs are waking up to the fact that social media platforms are advertising platforms,” he said. “What’s happened is that, in the last couple of years, if you’re not paying money to have your content land in front of end users, you get zero visibility on social media, and so it doesn’t work as a place to build a community anymore, unless you’re willing to really pay every time you try and post something on that platform.”

SMBs need a place they can own, which means they need a website, Penland said.

“SMBs are waking up to the fact that social media platforms are advertising platforms.”

— Penland
“They should have a website, and then they should have that connected to all of the different advertising platforms, and that’s going to be social media, that might be other things like Google ads or whatever,” he said. “If any of those stop working for them, they can move away from that platform, and they still have continuity for their customers.”

At the same time, however, Penland noted that Google’s algorithm updates in the past two years have deprioritized pure content websites in favor of product sites or community discussion sites like [Reddit](https://thenewstack.io/how-reddit-solved-devops-three-stooges-in-a-door-problem/). Monetizing through ads or affiliate alone is fading, he added.

## AI Comes to Web Hosting
Finally, a web hosting trend that will affect [developers is the introduction of artificial intelligence](https://thenewstack.io/ai-for-developers-how-can-programmers-use-artificial-intelligence/) into website hosting customer support. Penland said he sees a divergence in the web hosting industry between providers, with some leveraging AI automation at the expense of customer experience, he said.

“Some providers in our space have put generative [AI-based agents](https://thenewstack.io/gitlab-uses-ai-agents-to-automate-non-coding-dev-work/) as frontline support, and so when you try to reach out to that host, if you have a support need, you get a chatbot that’s based on some implementation of ChatGPT or some other generative AI tool on top of their documentation, and that’s the first line that you have to interact with,” he said. “In some cases, it’s difficult, or possibly impossible, to actually get a real person into that chat.”

We asked Penland whether developers may also see web hosting platforms start to offer AI capabilities as an add-on service. He said it’s a possibility.

“It’s something that we’ve thought about, and we’ve looked at what tools are out there that might make sense for us to offer in that way,” he said. “I don’t have anything to announce, but I do think that’s possible.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)