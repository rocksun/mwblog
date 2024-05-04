# Platform Engineering for a Mainframe: Design Thinking Drives Change
![Featued image for: Platform Engineering for a Mainframe: Design Thinking Drives Change](https://cdn.thenewstack.io/media/2024/05/8cdcfe3d-project-impala-2-1024x576.jpg)
We talk a lot about
[developer experience in the face of cloud native complexity](https://thenewstack.io/how-the-developer-experience-is-changing-with-cloud-native/). Yet [ 71% of Fortune 500 companies](https://planetmainframe.com/2022/12/relevance-of-mainframe/) are still on the mainframe. How can we modernize the experience of mainframe engineers?
Companies on the mainframe face changing regulatory requirements at a time of rapid growth. Add to this, the
[ average age of a mainframe developer](https://www.zippia.com/mainframe-systems-programmer-jobs/demographics/) is 47, meaning those with experience are approaching retirement — and the next generation needs onboarding.
Legal & General (L&G) is one of the world’s biggest asset managers, with $1.7 trillion in assets and 10,000 employees. At the virtual
[Enterprise Technology Leadership Summit](https://itrevolution.com/etls-eur24/) in late April, L&G’s tech leaders shared their [ platform engineering](https://thenewstack.io/platform-engineering/) journey, which enabled them to foster an excellent developer experience without the need for engineers who can use mainframe tools.
This transformation of their mainframe development approach is a sociotechnical mix of tooling and empathy for all stakeholders involved. And it bridges the distance of time and technology.
## Design Thinking to Modernize the Mainframe
All three presenters in the virtual event —
[Tariq Surty](https://www.linkedin.com/in/tariq-surty-8911101/), IT director for retail, [ Jennifer Pickard](https://www.linkedin.com/in/jenniferpickard/), head of engineering, and [ Bharghava Vamsi Krishna Bhogireddy](https://www.linkedin.com/in/bharghava-vamsi-krishna-bhogireddy-246543b/), senior operations architect — work in the pensions division of L&G. In 2012, the British government mandated that all employers have to offer a pension scheme, which employees must opt out of, not into.
As a result of that requirement, L&G’s pension division alone scaled from 250,000 in 2012 to more than 5 million customers today. More recent changes to regulation around the U.K. pension scheme have L&G expecting continued growth over the next few years.
![Case of Change: Unrelenting volume of change A timeline o the pension sector in UK which has been undergoing significant regulatory change. 1998: Individual pensions. 2002: SERPS were replaced with the State Second Pension Scheme or S2P 2004: The Pensions Act introduced the Pensions Regulator & Pension Protection Fund 2006: Pension simplification brought in 2010: State pension age started to change 2011: Triple Lock introduced 2012: Auto-enrollment — possibly the biggest initiative in UK pensions 2014: Massive pension reforms 2015: Start of the pension freedoms 2016: New flat rate, single tier state pension introduced 2018: State pension age for women increased to 65 2019: Auto-enrollment contributions increased 2020: State pension age increased 2021: suspension of triple lock system 2022: State pension increase](https://cdn.thenewstack.io/media/2024/05/5712d79a-legal-general-rate-of-change.jpeg)
This timeline illustrates the rate of change and complexity within the U.K. pension system over the last 26 years.
In 2021, in response to that scale of growth and expected strain on its core pension administration system, L&G asked: Instead of moving to a modern platform, why not modernize the mainframe? The aim was to enable a secure systems development life cycle and the three 3Qs: quickness, quality and quantity of change.
“Why not join the IT revolution and bring all the great things that
[DevSecOps](https://thenewstack.io/ebooks/devsecops/best-of-devsecops-trends-in-cloud-native-security-practices/) and modern software development practices and tools have to offer?” asked Surty during the presentation. “Such that we can drive not only the quantity of change, but also the quality and quickness of change too.”
He added, “Most of you I’m guessing will probably be too young to remember the mainframe technology in the same way as you are probably too young to remember the Chevrolet Impala. But given we were working with heritage technology and wanted to drive for more agility, nimbleness and speed,” they named their platform engineering initiative Project Impala.
Many enterprises look to tame the mainframe with
[big-bang cloud migrations](https://thenewstack.io/going-from-cobol-to-cloud-native/). Legal & General instead took an empathy-driven [design thinking](https://blog.container-solutions.com/wtf-is-design-thinking) approach to try to understand the different groups working with the mainframe and their pain points.
“We just thought it was really important that we took the time to hear people who engage with the mainframe and make sure that we listen to those issues and that we would have to iterate through some of those solutions and options,” Pickard said.
The platform team ran sessions in which they listened to different groups of developers, quality engineers, and anyone who engaged with the mainframe. After about two months, and many thoughts of Post-It notes generated, she said, Project Impala’s leaders had a deep understanding of the different teams, their workflows and handoffs.
L&G’s empathy-based design thinking approach followed this flow:
**Empathize.**To understand people’s needs better. **Define.**Identify the big problems to solve. **Ideate.**Discuss solutions that might be useful. **Implement or prototype.**Create mock-ups to be tested. **Test.**Share and gain feedback.
“The teams found that quite cathartic in different points that they could articulate their issues and their concerns, but equally they started to come together in terms of their own view as to how they could improve things and things that they’d observed,” Pickard noted. “Likewise, when it came to the tooling and what options were out there, people were just less aware.”
## Teaching Mainframe Devs About DevOps
It became clear that the mainframe developers needed to learn about contemporary
[DevOps](https://thenewstack.io/devops/) practices.
The L&G platform team consolidated the key learnings into:
- Tooling.
- Time it took to create quality data.
- Number of manual steps and handoffs.
- Environment contention.
Environment contention, Pickard said, indicates what occurs in the production mainframe “during those peak end-of-month processing times. The capacity is allocated to that production system, and you end up with less capacity being given to the lower environment. Which, in some cases, would lead to those systems really slowing down and more or less being unusable for the development teams.”
None of these issues, the team realized, would be solved by a “big bang” cloud migration.
“We’d need to make sure that we went slowly and incrementally to introduce those changes, and learn how that settled with the teams,” Pickard said. “But we also want to address the next generation and give them tooling capability that meant they could be the next generation that continues to support and maintain and grow that mainframe capability.”
The questions that arose included:
- How do we get
[CI/CD](https://thenewstack.io/ci-cd/)on the mainframe?
- How do we get the mainframe on the cloud?
- In a virtualized environment, how can we lose that workflow contention, when there is only enough capacity to run certain workloads?
- How do we encourage platform adoption?
- How can we encourage the next generation of mainframe engineers?
“How do we ensure that it’s adopted, it’s used, people remain curious, and we engage the next generation,” Pickard asked, echoing the developer focus of all platform engineering initiatives.
The platform team continued encouraging open communication with mainframe stakeholders with show-and-tell sessions. Then they recruited an entry-level engineer who bought a “fresh lens as to what options were there and what was workable, but it also meant that they could validate some of the initial tooling.”
Legal & General also introduced a small
[bug bounty](https://thenewstack.io/gitlabs-top-5-tips-for-running-a-bug-bounty-program/) for teammates who spotted vulnerabilities as a way to foster a culture of continuous feedback without blame.
## ‘Leslie’: The Modern Mainframe Developer Persona
In order to stay focused on their ideal developer persona, L&G’s engineering division brainstormed with
[GitHub’s Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/), asking the generative AI coding assistant what a modern mainframe developer looks like.
It came up with “Leslie,” who can code in both
[COBOL](https://thenewstack.io/how-cobol-code-can-benefit-from-machine-learning-insight/) and [Python](https://thenewstack.io/python/), and can switch between green screens and GUIs. She can handle terabytes of data with ease and is “someone who is not afraid of legacy systems but embraces them as a challenge and an opportunity.”
This mainframe engineer persona is a balance of contradictions — old and new, reliable and innovative, secure and agile. And she can use modern cloud computing,
[AI](https://thenewstack.io/ai/) and DevOps.
So how did the platform team reach that persona? By adopting and adapting DevOps processes for the mainframe.
“It was very evident from the outset, we had to adopt CI/CD processes for our mainframe development life cycle,” Bhogireddy said, in order to provide a uniform developer experience across this old and new.
But that wasn’t enough. The team had to work with a test dataset that was representative of 14 engineering teams serving 5 million customers.
“Along with providing immutable mainframe environments, just imagine spinning up and down a physical mainframe that you get immutably, like every other organization or heritage application or product that has stood the test of time,” Bhogireddy added.
The engineering teams could no longer rely on their peers’ institutional knowledge of the 25-year-old pension system. If they continued to do so, they would run into problems as those with first-hand experience with the mainframe retired.
As the original mainframe developers aged out, so must the “personnel dependencies about the knowledge of how to configure these environments, how to make those changes,” Bhogireddy added.
In other words: The pension system engineers’ “hero culture” had to be designed out.
The platform team examined anything that developers spent more than 30 to 40 minutes on a day, looking to eliminate toil by automating everything as code.
This involved adopting a large set of enterprise tooling, Bhogireddy said. Then, these tools were embedded into the L&G mainframe development life cycle, “so that our Leslies can develop and deliver the chain into production, which continues to stay on the physical mainframe for less than two weeks. That was the dream. That was the aim we were going toward.”
All testing was to continue before pre-production on the virtual, immutable mainframe, provided by the
[PopUp on-demand mainframe](https://www.popup-mainframe.com/), on top of a [Microsoft Azure](https://news.microsoft.com/?utm_content=inline+mention) cloud environment and leveraging [Delphix](https://www.delphix.com/) continuous data capabilities.
## Pursuing a Uniform Developer Experience
The platform team had solved the environment and data problems but still had to work out how to provide a uniform developer experience, from the young Java developer all the way to the most senior mainframe developer who is unfamiliar with contemporary,
[cloud native development](https://thenewstack.io/cloud-native/).
The platform team created a clone of all code, including 80,000 modules in GitHub, which allowed them to use an off-host integrated development environment to perform application development. The mirror is created and maintained using Broadcom’s
[Endevor Bridge for Git](https://techdocs.broadcom.com/us/en/ca-mainframe-software/devops/ca-mainframe-application-tuner/12-0/using/performance-testing-with-ca-mat-in-devops-ci-cd-pipelines/build-performance-testing-ci-cd-pipeline/install-the-pipeline-tools/install-and-configure-ca-endevor-bridge-for-git.html).
“And then the magic happened: when the most senior developers saw what young Leslies could achieve,” Bhogireddy said. “They could see pushing the code to pre-prod in a click of a button, not the 25 to 30 commands you need to type on a black and green screen.”
It was another sign that the platform team’s empathy-driven approach to orchestrating a platform experience for Leslie was working. Still, the team had to get everyone to come on board to this new mainframe developer experience.
“It was not going to be a big bang story. That was the end state where we wanted the developers to go to, but there are transitional periods,” Bhogireddy said.
“All over, Leslies are now in different transition states. And each of these transition states has developed value.”
The work, he said, wasn’t over: the platform still had to exhibit that value to its ideal developer persona. “We can have the best intention. We can have the best technological solution,” but without the teams, along with senior management and seven ecosystem partners, brought on board, adoption wouldn’t have been successful.
But it was. Now the pension system developers can deliver changes to pre-production in less than four hours. They can create environments in minutes. They can use the automated unit tests, which highlight COBOL code to show which code has been tested or not. Vulnerabilities are scanned earlier in the pipeline.
Bhogireddy attributes much of Project Impala’s success to continuously seeking feedback during the whole transformation.
![Young Leslie quoted as saying: "I didn't know what the fuss was about Mainframe Development?" I am a trained Cloud DevOps Engineer and am not finding any difference with Mainframe DevOps Pipelines." The Senior Mainframe engineer is saying "I didn't think mainframe development in the Cloud would be possible but as I saw what was being done, I started to believe."](https://cdn.thenewstack.io/media/2024/05/5b3cbde5-mainframe-vs-cloud.jpeg)
Two Legal & General employee testimonials that show the success of a unified developer experience.
Legal & General has been chosen as
[ Britain’s most admired company](https://www.britainsmostadmired.com/winners/most-admired-companies/) for the last two years. Project Impala recently received an [impact innovation award](https://www.cmg.org/2024/02/cmg-honors-legal-general-with-the-impact-innovation-award/) from CMG, an IT professionals nonprofit.
“The heartwarming thing for us with our young Leslies telling us, what is this about mainframe development? I’m a cloud-based developer,” Bhogireddy said. “But you won’t find any difference between the DevOps pipelines we created, or our senior most mainstream engineer who was reluctant to come on this journey, [who] has now converted.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)