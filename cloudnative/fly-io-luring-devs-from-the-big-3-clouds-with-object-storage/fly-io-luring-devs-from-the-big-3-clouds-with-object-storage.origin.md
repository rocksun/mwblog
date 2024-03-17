# Fly.io Luring Devs from the Big 3 Clouds with Object Storage
![Featued image for: Fly.io Luring Devs from the Big 3 Clouds with Object Storage](https://cdn.thenewstack.io/media/2024/03/162b4c83-white-tailed-eagle-2015098_1280-1-1024x609.jpg)
[Fly.io](https://fly.io/) is behind what may be one of the hottest underground developer movements happening today, as the company has quietly attracted more than a quarter-million developers organically and is now establishing key partnerships to reach even more devs.
Fly.io is a platform for developers to easily launch and manage applications globally.
[Kurt Mackey](https://www.linkedin.com/in/mrkurt), CEO and founder of Fly.io, said. Fly.io competes with Platform as a Service (PaaS) providers like [Heroku](https://thenewstack.io/service-design-couldve-prevented-herokus-free-tier-closure/) and [Render](https://thenewstack.io/render-cloud-deployment-with-less-engineering/) for initial developer adoption, but ultimately, Mackey aims to compete with major cloud providers like [AWS](https://aws.amazon.com/?utm_content=inline-mention), Azure, and [GCP](https://cloud.withgoogle.com?utm_content=inline-mention).
## Rebel Alliance
Indeed, Mackey told The New Stack he envisions the future of cloud computing as consisting of a “Rebel Alliance” of around 50 specialized companies, each focusing on a specific developer need. For instance, Fly.io, along with partners
[Supabase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/) ( for managed [Postgres](https://thenewstack.io/from-a-fan-on-the-ascendance-of-postgresql/)) and [Tigris Data](https://www.tigrisdata.com/) (for [object storage](https://thenewstack.io/the-new-metrics-of-object-storage/)), form a “minimum viable cloud” that developers can use to build almost any type of application.
Traditional cloud providers like AWS, GCP, and Azure are becoming dated, as they are built around operational practices that were more relevant a decade ago, Mackey noted.
And newer hosting platforms like Fly.io, Railway,
[Netlify](https://thenewstack.io/netlifys-approach-to-the-frontend-according-to-its-new-cto/), and [Vercel](https://thenewstack.io/vercel-and-svelte-a-perfect-match-for-web-developers/) are emerging, offering better alignment with modern development practices, improved functionality, and a superior developer experience, wrote [Martin Casado](https://www.linkedin.com/in/martincasado), a General Partner at [Andreessen Horowitz](https://a16z.com/), where he focuses on enterprise investing, in a [blog post](https://a16z.com/announcement/investing-in-tigris/). Andreessen Horowitz has invested in both Fly.io and Tigris Data.
“The benefits of these new platforms can be functional — Fly.io, for example, has far simpler multiregion support than AWS — but they also get adopted because they have better native support for modern applications frameworks and practices and a far better developer experience,” Casado wrote in the post.
## Meet Developers Where They Are
In addition, Fly.io enables developers to build apps with their favorite frameworks. The Fly.io CLI generates containers for most popular frameworks, including
[Rails](https://thenewstack.io/why-were-sticking-with-ruby-on-rails-at-gitlab/), Phoenix, [Django](https://thenewstack.io/dev-news-django-updates-storybook-7-6-and-node-js-20-beta/), Node, [Laravel](https://laravel.com/), and [.NET](https://thenewstack.io/net-7-simplifies-route-from-code-to-cloud-for-developers/), and Fly supports the [Go](https://thenewstack.io/go-1-18-the-programming-languages-biggest-release-yet/) and [Rust](https://thenewstack.io/rust-vs-go-why-theyre-better-together/) programming languages.
Fly.io transforms containers into micro-VMs that run on the company’s hardware in more than 30 regions on six continents. Fly.io offers what it calls Fly Machines, which are full Linux micro-VMs running on the company’s metal, built from customers’ own containers with a single command or API call, the company says on its website.
According to the website, “Fly Machines are the engine of the Fly.io platform: fast-launching VMs that can be started and stopped at subsecond speeds. Control them with their fast REST API or the flyctl CLI. Or use
[Fly Launch](https://fly.io/docs/reference/fly-launch/) for opinionated app-wide configuration and deployment.”
## Fly.io Lucked out
Fly.io’s initial focus was on enabling developers to easily build and manage their own
[CDN](https://thenewstack.io/cdn-outages-exploring-ways-to-increase-resilience/)s. It has since evolved to provide a highly controllable and “region-less” infrastructure platform.
“At the outset, we said if we do a good job a lone developer is able to build a CDN, which means you can run one bit of code in a whole bunch of places, manage it all with one lifecycle, and not have like really complicated, multi-region problems to solve,” Mackey said.
And because the company was so focused on CDNs Fly.io “lucked into” building “this cloud that doesn’t care. It’s region-less in some ways. It doesn’t care about which data center you need to run in — you can run on all of them, or you can run one of them. It’s totally up to you. The goal is getting close to people. And I think what we stumbled on was like kind of the right abstraction for what developers want to manage on the infrastructure.”
## Storage Is a Key, Enter Tigris
That’s good for developers because storage has been a key issue preventing applications from fully migrating to these new clouds, as robust cloud storage solutions are complex to build and operate, said
[Ovais Tariq](https://www.linkedin.com/in/ovaistariq/), co-founder and CEO of Tigris Data.
Last month, on Valentine’s Day,
[Tigris launched the public beta](https://www.tigrisdata.com/blog/object-storage-public-beta/) of its object storage service running on top of Fly.io. Tigris is a globally distributed object storage service that provides low latency anywhere in the world, enabling developers to store and access any amount of data using the [Amazon S3](https://thenewstack.io/amazon-s3-express-one-zone-introduces-near-real-time-object-storage/) libraries they are already using in production.
## Uber in the House
Tariq and his Tigris co-founders led the storage platform teams at Uber. “Over six years, we built and operated Uber’s global storage infrastructure, supporting millions of users per day across the Uber Rides and Uber Eats apps,” he said in a
[blog post](https://www.tigrisdata.com/blog/object-storage-public-beta/).
“Almost half of the team is from Uber,” Tariq told The New Stack.
The Tigris team is obviously capable of building and running a global object storage service, leveraging their experience with
[FoundationDB](https://thenewstack.io/foundationdb-a-reliable-key-value-store-with-acid-compliance/).
## Amazon S3 Led the Way, but Developers Want More?
In a post on March 14 – the
[eighteenth anniversary the launch of S3](https://www.tigrisdata.com/blog/a16z-round-press-release/) (and [Pi Day](https://www.piday.org/) as well) Tariq praised S3 for leading the way in changing how developers work with data storage by delivering Simple Storage Service (S3). Indeed, “S3 rewrote the rules of storage and propelled us into a new era of cloud computing,” Tariq said.
However, “As time has passed, developers
[want to work with newer, more streamlined cloud platforms over the big three ‘traditional’ cloud platforms](https://survey.stackoverflow.co/2023/#section-admired-and-desired-cloud-platforms) (AWS, Azure, and Google Cloud),” Tariq said in the post. “By 2006 standards, AWS S3 is a technical marvel. However, it isn’t 2006 anymore, it’s 2024.”
Tigris enables applications to write and read in any region, and even handles conflicting updates in multiple regions, providing a consistent global view of the data as a true global multi-master storage platform, Tariq said.
Tigris does this by running redundant FoundationDB clusters in Fly.io’s regions, using
[NVMe](https://thenewstack.io/why-nvme-is-a-better-choice-for-your-data-center/) volumes for caching, and a queuing system to distribute object data to multiple replicas and regions where the data is in demand, Mackey said.
“We use Kubernetes to run our workloads we have built Kubernetes on top of Fly,” Tariq said in an interview. “And we’re using it for the simplification. The simplicity that Fly provides from a network perspective made it easy for us to build this multiregional global application. If it had been using AWS, they would cost me a lot of infrastructure complexity.”
Furthermore, Tigris provides an S3-compatible API, making it easy for developers to integrate with their existing frameworks and libraries.
## Gains from Tigris Partnership
So, Fly.io has partnered with Tigris to offer object storage as part of the Fly.io platform, allowing developers to create a Tigris project using the “fly storage create” command, with all necessary configurations injected into the application.
For customers, Fly.io consolidates billing for all services, including Tigris, under a single monthly bill, simplifying accounting for developers.
Fly.io has around 90 employees, has raised $110 million in funding, and operates its own hardware in 37 regions worldwide to provide low-latency access to applications.
Mackey said the company primarily attracts small, impatient, and intellectually curious developer teams who want to ship and iterate quickly without seeking permission.
Also, Fly.io sees significant potential in supporting developers working on emerging and transformative use cases, particularly in areas like AI, Mackey said.
Moreover, Tigris’s Tariq told The New Stack he also sees a lot of potential in the AI space, where infrastructure challenges around scaling compute and storage efficiently can be addressed through innovations in both compute and storage.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)