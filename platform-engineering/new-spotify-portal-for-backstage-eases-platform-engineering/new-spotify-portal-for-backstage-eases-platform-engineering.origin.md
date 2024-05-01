# New Spotify Portal for Backstage Eases Platform Engineering
![Featued image for: New Spotify Portal for Backstage Eases Platform Engineering](https://cdn.thenewstack.io/media/2024/04/1f03f273-pia-nilsson-spotify-backstage-1024x576.jpeg)
LONDON — When
[Pia Nilsson](https://www.linkedin.com/in/pia-nilsson-02b47b1/) arrived at the audio streaming company [Spotify](https://thenewstack.io/how-spotify-achieved-a-voluntary-99-internal-platform-adoption-rate/) in 2016, she marveled at what she saw — and not in a good way.
“What I found was a very nice, collaborative, transparent, passionate company. But it was such a mess. The infrastructure was such a mess. I’ve never felt almost useless in my job,” Nilsson, now senior director of engineering at
[Spotify](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/) and general manager for [Backstage](https://backstage.io/), told The New Stack.
“There was no way to find out things. I had to go back to being an engineer, to work my way back through the ecosystem to understand it,” she said, because Spotify was still working as a startup, even though it was a decade old.
Each squad had its own context, with no centralized documentation and standards. “The learning curve was too deep,” she said. “You learn over and over again, because it’s so differently implemented.”
She wasn’t alone. Back then,
[ developer onboarding took an average of 110 days](https://thenewstack.io/how-spotlify-adopted-platform-engineering-culture/). If Spotify had this problem, how can smaller companies manage?
The company solved its problem, and its solution, Backstage, an open source platform for building developer portals, is helping other organizations also solve similar problems.
Today,
[Spotify launched today a new internal developer portal](https://info.backstage.spotify.com/roadmap), Spotify Portal for Backstage, into private beta, as a full-featured, low-to-no-code portal built on Backstage.
## The Problem: Too Many Interruptions
Nilsson has spent decades as an engineer exploring engineering culture and how it builds large-scale infrastructure. Trying to answer: How do we actually ship high-quality code fast?
It’s what motivated her to join Spotify’s “wonderful autonomous culture.” But, as the audio streaming platform scaled, development had slowed way down. And its quarterly developer surveys revealed that it wasn’t the tech slowing them down.
People couldn’t find things. And they were interrupted all the time, because the collaborative culture embraced shoulder-tapping, developer autonomy, radical transparency and inner sourcing.
“How are we going to help all of these people out here at Spotify without telling them what to do? Because we hate that,” Nilsson said. “And we need to keep the collaborative spirit and they need to talk to their colleagues.”
The
[Backstage software catalog and developer platform](https://thenewstack.io/spotifys-backstage-a-strategic-guide/) became the answer for Nilsson and her colleagues. Read on for this exclusive look at how the most popular open source framework for building developer portals solved not only Spotify’s sociotechnical troubles, but then was outsourced to solve for thousands of other teams.
## Maintain Autonomy, but Reduce Context Switching
Spotify’s engineering culture is famous for its focus on
[ developer joy](https://thenewstack.io/measure-developer-joy-not-developer-productivity-atlassian-says/) and autonomy. Back in 2016, the [platform team](https://thenewstack.io/platform-engineering/) began to look for patterns about what makes some teams happier than others.
The platform team discovered that backend developers were measurably a little bit happier because someone had created a shared catalog across all backend components. All while machine learning engineers, web developers and functional teams like those in charge of the playlists, users and royalties, each had their own platforms or webpage portals.
Each engineering group had its own services to worry about, some with
[documentation](https://thenewstack.io/an-engineers-best-tips-for-writing-documentation-devs-love/) and some not. It led to a great engineering culture, but a lot of context switching, across about 400 Spotify squads.
“We wanted to consolidate all of that. It’s not just a technical problem — although it is — it’s very much psychological,” Nilsson said. “And you need to help people maintain full ownership of what they actually work on.”
So the platform team began in 2017 to create what became Backstage.
## Backstage’s ‘First Constituents’
Nilsson’s team chose the data team as its “first constituents,” getting them enrolled in Backstage. It involved “unlocking the problem of people not wanting to lose their mandate,” she said. “That’s their job. They’re actually data experts,” she said.
To this day, the Spotify data team maintains its own Backstage homepage, alongside its huge data ecosystem.
The secret to Backstage — which she joked is not a secret, as it’s open sourced — is its extensibility.
“We allowed the data folks in this example to write a little Backstage plugin and maintain full ownership of it through a
[GitLab](https://about.gitlab.com/?utm_content=inline+mention) feature, called [Code Owners](https://docs.gitlab.com/ee/user/project/codeowners/).” Backstage is essentially a homepage, she said, made up of a [mono repository](https://thenewstack.io/monorepos-hal-9000-approved-code-management-and-collaboration/), that each team “can maintain full ownership of what they’re accountable for.”
This was also a strategic decision because, at the start, the Backstage team was just seven people.
“The beauty of this is decentralizing decisions. Decisions should be made by the people who understand the problem,” Nilsson said. “And this little team I had, we understood the problem of discoverability and how we could help people find what they needed, while the people contributing plugins to Backstage maintain full ownership of those.”
## The Secrets to Backstage’s Mass Adoption
Within two years, Backstage had reached mass adoption across Spotify — 100% voluntary.
“I speak to so many adopters all the time and they believe that they need to hire this huge Backstage team because they think of it as a monolith,” Nilsson said. “But then they miss out on the psychological aspect,” because no team wants to give up their mandate.
“I always recommend to everyone to stay small,” she added, “because then you do all these other things that you shouldn’t do. Instead, you need to help them craft the Backstage plugin that they are going to own and be proud of .”
As with all things Spotify culture, it’s show and share, not tell. Nilsson’s team organized a bunch of community sessions, inviting folks from various functions and domains to come and demo their Backstage plugins, showing off their domain knowledge and the features they are able to deliver faster.
Now Backstage at Spotify has more than 200 internal Backstage plugins, to enable more extensibility.
A common engineering pattern, Nilsson noted, is to solve a business problem. Once it’s solved, only then do you build an abstraction layer or user interface. For Spotify, that started with each squad solving its own concerns. Then Backstage enabled teams to build user interfaces (UIs) on top and list them in a shared UI component library, which in turn enables reusability.
## Better Retention, Faster Software Development
With Backstage, Spotify’s developer activity, software development life cycle and developer retention have all markedly improved. Developer onboarding went from 110 days to 20 days. And the Backstage frequent users — the half of the staff that uses the portal more often than the other half — are 5% more likely to stay at Spotify longer.
![Frequent Backstage users are 2.3 times more active in GitHub, create twice as much code changes in 17% less cycle time, deploy software twice as often and their software is deployed for three times as long, and they are 5% more likely to be at Spotify a year later.](https://cdn.thenewstack.io/media/2024/04/d845cccc-backstage-roi-1024x321.jpeg)
Spotify’s data on developers who frequently use Backstage indicates the portals help make them more productive and more likely to stay with the organization.
“I believe, at least for myself, if I am enabled like this, I am going to be happier,” Nilsson said. She referenced the Spotify slogan: Happy developers, happy code. “If it’s a joy to work, you wouldn’t leave.”
Spotify sees a measurable link between Backstage and
[ developer joy](https://thenewstack.io/how-intercom-ships-industry-leading-developer-experience/).
“If we are keeping this very collaborative, transparent, trusting environment, trusting people’s own judgment and expertise,” she continued, “if we have that culture, Backstage is certainly a core piece of that.”
But how can you
[ measure developer experience](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/) and culture?
As one of the biggest
[Google Cloud Platform](https://cloud.withgoogle.com?utm_content=inline+mention) customers, Spotify has a longstanding collaboration with Google, built on top of similar engineering cultures, including that of regular [developer surveys](https://thenewstack.io/github-developer-productivity-at-30-billion-messages-per-day/).
## ‘We Always Look at Ourselves as the First Customer’
For more than a decade now, Nilsson’s team has run quarterly engineering satisfaction surveys, with the engineering workforce split into thirds for more continuous, monthly feedback. This qualitative data is combined with quantitative data across all the Spotify platform products, including the
[Backstage Insights plugin](https://backstage.spotify.com/marketplace/spotify/plugin/insights/).
“We have always been looking at ourselves as the first customer,” Nilsson said, adding more developer experience data to the feedback mix.
“Dogfooding is how you create tools that people want to use,” she said, which is another core tenant of the platform organization.
Spotify was certainly one of the first platform engineering teams, back in 2016, to start recruiting product people, Nilsson said, as “one way to maintain a human-problem-oriented approach to technical problem-solving.”
Having a product manager, designer, and product owner collaborating with engineers, she argues, can help define a platform strategy in a sociotechnical way.
There is also the
[ Spotify annual Hack Week](https://newsroom.spotify.com/2023-03-16/tips-for-creating-a-successful-hack-week/), where every employee, from human resources to agile coaches, is expected to hack their work, whether it’s about people, processes or tech, or a mix of those factors. The Backstage product has benefited from engineers hacking their own developer experience.
Spotify also has the habit of colleagues embedding on other teams to develop empathy and a growth mindset. Since for the platform team, their colleagues are their customers, having
[ platform engineers embed on app teams](https://thenewstack.io/how-platform-teams-can-align-stakeholders/) offers a first-hand perspective to dev struggles — evading the bad habit of just building what they think is best.
“Recently, we had an engineer going to work on the desktop app. He was deeply inside of the
[CI](https://thenewstack.io/ci-cd/) team in the platform organization, so very far from the actual Spotify app,” Nilsson said. “When he came back, he had so many insights that he brought back to the platform organization.”
## Creating an Industry Standard
One of the reasons for the rise of platform engineering over the last 18 months has been the tech layoffs, leaving most teams doing more with less. “Backstage was never for reductions,” Nilsson said. “It was the opposite. It was in order to enable folks who were onboarding as well as to enable the teams we already had that we wanted to speed up.”
But while it was originally built as an internal product, Spotify has an ethos that in order to create an industry-standard — like around internal developer portals and catalogs —
[ you should open source it](https://github.com/spotify).
Backstage is both a commercial product, and an open source tool, the open source framework has more than 3,000 company adopters and more than 2,200 contributors. Everyone is welcome as a contributor in this open ecosystem, with 150 external Backstage plugins, including by
[PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) and Travis CI.
“And then we sell some of our enterprise products where we think we have some great value to offer. And we have scaled and battle-proven from within over the years,” she said, including the Backstage experimentation platform, which was released publicly after a decade of use in-house by the Spotify app team.
## Launching ‘Backstage in a Box’
Whether freemium or premium, Backstage is likely to continue to dominate the platform engineering world, with Forrester predicting that half of all companies looking for a
[ platform-led software development approach will adopt Backstage](https://www.forrester.com/what-it-means/ep352-tech-trends-2024/) by the year’s end.
Today’s launch of Spotify Portal for Backstage is the latest step in its plan to continue that market domination.
“What we have been hearing since 2020 [is] ‘We love Backstage, everyone wants to use it,’ but not everyone has
[TypeScript](https://thenewstack.io/typescript/) developers, and the complexity of going from not having an [internal developer portal] and not having done all of the work that we had done — as in understanding the complexity and then realizing what our solution is — not having done that prep work for years makes Backstage pretty hard,” Nilsson said.
“There are always going to be customers who are asking: Can you simplify this for me?”
The Spotify Portal for Backstage is opinionated by design, with a setup wizard and a catalog wizard that promises to help teams get started in under five minutes. It also comes with a software catalog and software templates, to help companies lay down golden paths for backend services, websites and more, which enable developers to spin up new projects in seconds.
This new portal also includes the popular Backstage plugins of
[ Soundcheck](https://backstage.spotify.com/marketplace/spotify/plugin/soundcheck/), [ TechDocs Documentation](https://backstage.io/docs/features/techdocs/), [ Search](https://backstage.io/docs/features/search/getting-started/) and a new Config Manager.
In addition, today Spotify announced two enterprise consulting and support services.
The Spotify Portal for Backstage, Nilsson said, “bring in customers who are eager to partner with us to build the best possible Backstage experience ever.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)