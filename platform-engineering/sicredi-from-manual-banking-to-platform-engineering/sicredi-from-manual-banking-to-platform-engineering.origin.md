# Sicredi: From Manual Banking to Platform Engineering
![Featued image for: Sicredi: From Manual Banking to Platform Engineering](https://cdn.thenewstack.io/media/2024/10/3f7ec36b-getty-images-38hnyyzyvok-unsplash-1-1024x683.jpg)
As more banking customers began clamoring for an expanding range of modern [fintech services](https://thenewstack.io/overcoming-the-challenges-of-working-with-a-mobile-fintech-api/) such as digital wallets and crypto in 2017, developers inside the 102-year-old Brazilian credit union, [Sicredi](https://ri.sicredi.com.br/en/), saw the intriguing possibilities before them.

But as they began experimenting and working to imagine, build and deliver these new banking innovations for customers, they were slowed by the demands of other everyday business operations, slow internal [software development cycles](https://thenewstack.io/why-we-shift-testing-left-a-software-dev-cycle-that-doesnt-scale/) and other institutional challenges. Sicredi’s long history of banking in the past had grown its development systems into large, hard-to-manage legacy systems and infrastructures that were unwieldy and inefficient.

“The delivery of new products and features was taking too long to reach our customers,” [Eduardo Abe](https://www.linkedin.com/in/eduardolopesabe/), Sicredi’s platform engineering manager, told The New Stack. “The software development cycle was very slow because a lot of time was lost on operational demands, increasing wait times throughout the development cycle and the time-to-market of business products.”

The time for change arrived as customers began eyeballing the innovative financial services that were appearing in the marketplace by 2017, said Abe. Sicredi officials did not realize it at the time, but the road to creating a [platform engineering](https://thenewstack.io/platform-engineering/) strategy inside the company had just begun. Its old development infrastructure could no longer keep up with the growing demands of customers and technology. The race was now on.

“With the [aim of accelerating the use of these new technologies](https://www.youtube.com/watch?v=eDbQ18Fx0qU) in our business products, we decided to adopt an organizational format using [agile methodology](https://thenewstack.io/agile-reinvented-a-look-into-the-future/) principles, start using public cloud, and a new microservices architecture model to guide the development of cloud-native applications,” he said. “From this context, there was an exponential growth in development teams, creating a huge challenge for technology teams.”

## Moving From DevOps to Platform Engineering at Sicredi
Abe, who joined Sicredi as the SRE (site reliability engineer) and DevOps manager in January 2022 and later became the platform engineering manager in March 2024, said that [DevOps](https://thenewstack.io/devops/) practices were adopted at Sicredi in 2016 as the credit union worked to streamline and better manage its development systems.

In 2017, Sicredi implemented an [Infrastructure as Code](https://aws.amazon.com/what-is/iac/) strategy, giving the credit union new tools to provision and support its computing infrastructure using code instead of manual processes and settings. Meant to increase efficiency and save time managing its systems, this move helped to put the organization on the track to its eventual move to platform engineering. With the concept of an eventual platform now established, Sicredi’s homebuilt [independent developer platform (IDP)](https://thenewstack.io/the-hidden-costs-of-free-internal-developer-portals/) was underway on the road to its platform engineering future.

To refine its corporate DevOps strategies even further, the DevOps team was split in 2019 into a software engineering team and an agile infrastructure team, with the aim of getting more control over a still unwieldy infrastructure, said Abe. At the end of 2019, Sicredi’s IDP was put into production.

But the work was still not finished. By 2021, Sicredi began building its team to fully incorporate a platform engineering approach for its operations.

And by the beginning of 2024, Sicredi migrated the technology of its IDP from [Java](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/) to Go to accelerate technology plug-ins.

Building its own IDP for platform engineering was not a task for the meek, said Abe.

“Our platform abstracts various technologies for developers to use, accelerating the provisioning of infrastructure resources, including repositories, databases, messaging services and Amazon S3 buckets in the software development cycle,” he said. “It also abstracts all our [CI/CD](https://thenewstack.io/ci-cd/) tools, including [Jenkins](https://thenewstack.io/cloudbees-scales-jenkins-redefines-devsecops/) and [GitLab](https://about.gitlab.com/?utm_content=inline+mention), and acts as an orchestrator, deploying to our container solution.”

The Sicredi IDP, which it named DevConsole, has delivered massive improvements in work processes, workflows and more for the company, said Abe.

“The infrastructure platform engineering model and the IDP solution have made Sicredi’s complex hybrid infrastructure operation simple and scalable,” he said. “Numbers show that between the years 2021 and 2023, for example, the development teams grew by 45% without the need to expand the infrastructure team,” while business results grew due to the accelerated development of new products and features for users, he added.

## More Details on Sicredi’s IDP
DevConsole is used today by some 240 development teams and more than 1,000 developers at Sicredi, according to Abe. It has been used in the creation of more than 4,000 applications for use with different business partners, such as Pix (Brazil’s instant payment service).

The credit union’s developers use the platform to build applications for a wide range of digital channels as well as for core banking, customer engagement and payment requirements of 45,000 credit union employees and their eight million customers across some 2,700 branch offices in Brazil.

To keep the IDP up to date, it is reviewed quarterly by a team of 23 platform engineers who monitor and maintain it for the company’s developers, said Abe. The team includes engineers covering the IDP, containers, streaming and CI/CD tasks.

Sicredi has more than 6,900 applications running on 47 different Kubernetes clusters across a private cloud using Canonical OpenStack.

## Looking Back on Sicredi’s Platform Engineering Strategy
“The concept of platform engineering is fundamental in critical operations and complex systems,” said Abe. “The platform enables scalability, autonomy, self-service and resilience.”

Several important lessons have been learned, he said.

“I think understanding that the IDP is a technology product helps us structure objectives aimed at accelerating the software development cycle,” said Abe. “Working with platform metrics is also fundamental. Nowadays, we probably would not develop an IDP from scratch. But when we started our journey in 2017, the concept of platforms and IDPs did not even exist.”

The improvements in application development and business operations for the credit union continue to be huge for the business, said Abe. “In the past, processes were done manually and reactively, and now with the platform, we work proactively and are self-service oriented.”

Sicredi began these processes through experiments with small automation projects back in 2015 using Jenkins and [Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/), said Abe.

## Other Markers for Success
So, what has been the biggest operational gain for the credit union as a result of using platform engineering?

“The most important thing for the adoption of our IDP at Sicredi is having autonomy with responsibilities,” said Abe. “Throughout the platform, we have implemented guardrails to prevent our developers from using the IDP incorrectly. A developer can allocate CPU and memory resources for their application, but only up to a certain limit. Beyond that, they need to justify the reason. Another super important factor was our DevOps team, who help evangelize the use of the platform within the development teams.”

Abe said he continues to be amazed by Sicredi’s platform engineering journey that led to the creation of its IDP. “There were many ups and downs until we arrived at an ideal solution,” he said. “I could not participate from the beginning, but for the past three years, I have been working directly on our platform and we are satisfied with the results.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)