# Building the Future Together With Community-Driven Open Source
![Featued image for: Building the Future Together With Community-Driven Open Source](https://cdn.thenewstack.io/media/2024/10/a4906060-hands2-1024x574.png)
It’s safe to say that [open source software](https://thenewstack.io/open-source-software-use-driven-by-cost-cutting-survey-says/) has had a profound impact on the world. From Linux to GNU to the Apache ecosystem, much of today’s technology landscape is powered in some way by tools that have been collaboratively developed out in public.

We are in the process of building an open source community for [Apache Polaris (Incubating)](https://polaris.apache.org/) with the [Apache Software Foundation](https://www.apache.org/) (ASF), and we wanted to share some thoughts on the power of open source, why it matters and how to go about starting an open source project. But first, we need to define what open source actually is.

## The Real Meaning of Open Source
On one hand, [open source](https://thenewstack.io/open-source/) simply means any software for which the source itself is “open” or publicly available. That is the narrowest definition. But as you might expect, the reality is far more nuanced. At the risk of oversimplifying, we will posit that there are two primary nuances that matter: [open source licenses](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) and open source governance.

The [open source license](https://opensource.org/licenses) dictates what a person is allowed to do with the code. These licenses range from the more permissive end of the spectrum, such as MIT and Apache (“Do what you want, but you can’t sue us, and please include the copyright and some other information”), to the more restrictive end, such as General Public License or GPL (“You must always include the source code and also anything closed source that you link with this code and ship to customers is now legally required to be open source, haha!”).

Somewhere in the middle is Business Source License or BSL (“You are free to use this as long as you’re not making money selling it, because only we are allowed to do that”). Individuals are well advised to spend time familiarizing themselves with the license options that exist and picking one that works best for their needs.

Open source governance then dictates the rules for how a given open source codebase or project evolves over time by setting up a framework for how the community developing the project interacts and collaborates. Typically, one of the most critical aspects of open source governance is who decides what happens with the project. Is there a benevolent dictator, such as Linux in the old days? Is there a single company driving everything like dbt Labs or Redpanda Data? Is there a group of trusted owners who collectively make decisions in some way like they do with Apache? If there is a group of trusted owners, who gets to be an owner?

There are a lot of questions to be answered when considering a governance approach, and no one approach is necessarily better than another. It all depends on what your goals are for the project over time.

## Choosing What Works for Your Needs
Once you have a sense for what open source is, the next question to ask yourself is why even open source your codebase in the first place? Though there are many potential motivations, a few of the key ones are:

**More contributors.**With open source software, the number of developers working on a project is driven more by how much community interest it generates, rather than the amount of funding available to hire engineers.**More perspectives.**As with many things in life, exposure to a more diverse set of perspectives and ideas often leads to better results.**More adoption.**When software development is driven by community and collaboration, it’s far more likely to result in stable standards that see broad adoption than multiple competing closed source efforts.**More good.**By making your software open, you contribute to the greater good, by building something of value and offering it for free.
Conversely, there are reasons why you might not want to work in open source:

**Less control.**Though this depends greatly on the governance model, the goal with many open source governance models is to prevent any one principal from exerting too much control over a project’s direction. The community comes first.**Less private advantage.**When you give the source away for free, it can be more challenging to monetize, though there are business-oriented licenses like BSL that try to strike a balance between open and closed.**Less velocity.**This is by no means a given with open source software, but when opening up development to a larger community, and in particular when emphasizing the[needs of the community](https://thenewstack.io/open-source-communities-need-more-safe-spaces-and-codes-of-conducts-now/)over the need to move quickly, it can potentially result in open source development moving faster than commensurate closed source development might. However, this may also be offset by the sheer number of active contributors if the project grows large enough.
Once you’ve made the decision to open source, the next steps depend heavily on the approach you want to take. We will focus on the approach we’re most familiar with: open sourcing through the ASF.

## Why the Apache Software Foundation?
The ASF exists to provide [software for the public good](https://thenewstack.io/apache-software-foundation-struggles-weight-much-success/). Its core ethos is the concept of the power of community over code, known as the “Apache way.” This philosophy emphasizes the importance of a healthy, collaborative and engaged community in the success and sustainability of an open source project, rather than solely focusing on the code itself. Thousands of people around the world contribute to ASF open source projects every day, making the ASF one of the largest open source foundations.

The ASF is a non-profit, public charity, 501(c)(3) membership corporation, providing legal, branding, press, fundraising, infrastructure support and proven community mentoring to the many Apache projects. Since the initial release of Apache Hadoop, the ASF hosts a lot of open source projects tied to the [big data ecosystem](https://thenewstack.io/apache-streaming-projects-exploratory-guide/).

Apache Iceberg is one of the many open source projects in this ecosystem that exemplifies the power of community through the accelerated growth of contributions from diverse perspectives and backgrounds.

In the context of the big data ecosystem, [Apache Iceberg](https://thenewstack.io/apache-iceberg-a-different-table-design-for-big-data/) is an important piece because it defines a specification for abstracting files as tables in a way that provides reliability guarantees, performance optimizations and can integrate with with many other tools in the landscape.

Apache Iceberg also includes a standardized specification for managing and organizing metadata about Iceberg tables. However, Iceberg doesn’t provide a reference catalog implementation because it exceeds the scope of the project. To complete the Iceberg solution, it made sense to have an open source catalog implementation “close” to Iceberg at Apache. That’s why [Polaris](https://incubator.apache.org/projects/polaris.html) landed as a podling in the ASF incubator.

## The Apache Incubator Process
The [Apache Incubator](https://incubator.apache.org/) is a gateway for open source projects seeking to become part of the ASF. It helps those incoming projects (called “podlings”) adopt the Apache style of governance and operation while guiding them through the ASF services available to these projects so they can become top-level ASF projects. There are clear and detailed instructions for the whole process in the [Incubator Cookbook](https://incubator.apache.org/cookbook/), but we’ll give an overview of the main highlights here.

The best way to begin is to find a champion, although not required, to help guide the project. This is someone from the [Incubator PMC](https://home.apache.org/phonebook.html?pmc=incubator) (IPMC) who is interested in seeing your project come to the ASF, and is willing to help guide you through the process and advocate for your cause.

In our case, JB Onofré is the champion for Polaris. If you’ve done any work in the Apache world (or even if you haven’t), there’s a decent chance you might know someone on the IPMC already — there are 284 PMC members as of this writing, and they are typically folks who have been deeply engaged in Apache open source projects for a number of years, so their community networks are often quite large.

If you find someone you know on that list, it’s worth reaching out to see if they have any suggestions for you on how best to proceed. Even if they’re not in a position to act as a champion themselves, they may know someone who is. If you find that you don’t know anyone, the best thing to do is just email the IPMC mailing list directly, introduce yourself and your project, and let them know you’re looking for someone who might be willing to be a champion.

Once you have a champion lined up, the next step is to begin drafting an Incubator proposal following the [podling proposal template](https://cwiki.apache.org/confluence/display/INCUBATOR/New+Podling+Proposal). Proposals include sections describing the project, explaining how the goals of the project align with those of the ASF, addressing common concerns with proposed podlings and listing the people who are currently active developers. The proposal will be used to provide an overview of the project and help justify why you believe it can be a good fit in the Apache ecosystem.

Another key part of the proposal is the mentor list. Mentors are IPMC members who, similar to the champion, volunteer to help guide and coach the podling through the incubation process. Your champion can help you find some suitable mentors if you don’t have connections yourself.

Once your proposal is drafted, the next step is to take the proposal to the IPMC for discussion. A strong emphasis is made on the podling’s alignment with the community over code philosophy, demonstrated diversity of contribution from multiple sponsoring companies or organizations, and a collaborative openness in all aspects of the work.

As part of the discussion, the committee may request changes to the proposal. In our case, we ended up making some minor changes to the proposed list of committers to more closely align with common convention. If there are significant concerns with the proposal, more drastic changes may be required, or the [project itself might need](https://thenewstack.io/does-your-open-source-project-need-foundation-oversight/) to spend some more time preparing and come back another time.

Assuming the IPMC discussion proceeds agreeably, then at some point it will be appropriate to initiate a vote. Your champion can help you know when a good time to start the vote is, and will likely be the person to do so (though technically anyone involved in the podling proposal can). The vote lasts at least 72 hours and will be a majority vote tallied among the binding votes cast by IPMC members.

Typical Apache convention is to only initiate a vote once there seems to be general consensus among the discussing parties. When this process is followed, there is often a reasonable chance that the official vote will pass. But if not, the dissenting parties will be on the hook to provide constructive feedback, and the project can come back with a new proposal at a later time after the shortcomings have been addressed.

In the case where the vote succeeds, your champion and mentors will then help guide you through the logistics of getting the project set up within Apache infrastructure: GitHub repository, mailing lists, documentation and legal support.

At this point, the focus shifts to increasing the project’s community and adopting the Apache way. This includes supporting new contributors and growing them into committers and eventually PMC members, publishing regular podling releases, maintaining documentation and consistently refining both the code and release process to best fit the needs of end users.

Once the project reaches sufficient maturity, your champion or mentors can recommend to the IPMC that the project is ready for graduation. If the IPMC votes in the affirmative, then the project graduates from the Incubator and becomes a new Apache Top Level Project (TLP).

## The Power of Open
By collectively donating Polaris to the ASF and having individuals from numerous companies contributing, there’s a broader community to support its continued innovation. We see open source as the future of software development, [empowering developers to innovate](https://thenewstack.io/empowering-developers-is-critical-to-drive-ai-innovation/) faster with powerful services that the whole industry benefits from. By prioritizing transparency, fostering collaboration and encouraging rapid iteration, open source has quickly become a de facto way for users to drive technological progress through a collective effort of shared knowledge.

*To learn more about Kubernetes and the cloud native ecosystem, join us at KubeCon + CloudNativeCon North America in Salt Lake City, Utah, on Nov. 12–15.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)