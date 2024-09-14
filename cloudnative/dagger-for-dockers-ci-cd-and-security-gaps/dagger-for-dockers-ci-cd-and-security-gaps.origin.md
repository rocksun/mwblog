# Dagger for Docker’s CI/CD and Security Gaps
![Featued image for: Dagger for Docker’s CI/CD and Security Gaps](https://cdn.thenewstack.io/media/2024/09/b31bafd4-olivie-strauss-fsdvg0_9haa-unsplash-1-1024x683.jpg)
The idea I had was to share my [Neo4j knowledge graph](https://thenewstack.io/build-a-movie-database-with-neo4js-knowledge-graph-sandbox/) project on a [Docker](https://thenewstack.io/why-capistrano-got-usurped-by-docker-and-then-kubernetes/) [container](https://thenewstack.io/containers/) for possible work and revisions by folks who could help with the project. This, again, is not a commercial project but a sandbox project involving oceanographic data analysis.

However, I spoke with at least two developers who were adamantly opposed to that, and they said I would need [GitHub](https://thenewstack.io/this-year-in-programming-go-rust-github-lead-2021-stories/) or [git](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/) for any kind of work for several reasons — which I know of and are well known — such as its systematic approach, its effectiveness for pull requests and its ability to trace and audit past changes, etc.

But again, I wanted something simple, and I think it would involve just a maximum of two or three people to review the code in the application, and that’s about it because I’ll be doing everything else. When using code from other runtimes for my project, I could also just use a hardened [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) container from [DockerHub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/) for security, as opposed to having to bother with signatures and [SBOMs](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) and such. Because Chainguard consistently updates its container images, you can leave the security updates to it to manage.

While looking into the right option to share my knowledge graph application, I remembered a talk given by Chainguard developer relations advocate [Adrian Mouat](https://www.linkedin.com/in/adrianmouat/), at KubeCon + CloudNativeCon EU in Paris earlier this year. The talk was called “Building Container Images the Modern Way” (I was there for the talk, and it was packed).

Use

[@dagger_io]to build pipelines input:[@chainguard_dev]’s Building Container Images the Modern Way –[@chainguard_dev]’s Adrian Mouat demo. It « real strength » is its modules, he said.[@KubeCon_][@linuxfoundation][@thenewstack][pic.twitter.com/bTCpBcuV1C]— BC Gain (@bcamerongain)

[March 22, 2024]
The key element I took away from it, not necessarily for my project, but in general, was that indeed, for deployments and in many other ways, GitHub is and has been the way to go. However, it could be supplemented by improvements, especially in terms of the CI/CD organization of pipelines.
Docker, for CI/CD specifically, falls short. Although going back to my original project, yes, Docker is perfect, I think, for what I want to do. But it’s emerged that, again, for CI/CD, Docker does have its shortcomings, as well as for certain security aspects.

One of the key points that came out of Mouat’s talk was how [Dagger](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/) seems well-suited for CI/CD, and additionally, it can be integrated with GitHub for CI/CD projects, as Mouat explained.

## I Want My CI/CD
Dagger offers programmable CI/CD through containerization. But as mentioned above, this is not an either-or situation, as is the case with my project. Again, my project is just about shipping a simple application in a container to a couple of people. It’s definitely not a full-blown CI/CD type of collaboration.

As Mouat defined during his talk, Dagger is a tool that leverages [BuildKit](https://docs.docker.com/build/buildkit/)‘s power to define CI/CD pipelines in code. It excels in creating complex build pipelines that can be reused across projects, providing strong caching and parallelism capabilities, he said.

These reusable build pipelines in a container are key.

“Defining reusable build pipelines as code is a critical precondition for reducing [DevOps](https://thenewstack.io/devops/) complexity and enhancing security and compliance. Allowing developers to run these pipelines locally using Docker BuildKit, a tool they are familiar with, automatically ensures consistency between development and production environments,” [Torsten Volk](https://www.linkedin.com/in/torstenvolk/), an analyst at TechTarget’s Enterprise Strategy Group, said. “This is critical for implementing policy-driven security to enable developer productivity while ensuring security at the same time.”

And again, Dagger is integrated with GitHub, [GitLab](https://about.gitlab.com/?utm_content=inline+mention) or plain git, or can be. Therefore, you’re getting the best of both worlds in many ways, with the security aspects and simplification.

The programmability of the CI/CD pipeline and the different options that Dagger offers make it particularly apt for CI/CD. This is where a simple Docker container, while great for my project, would arguably fall short — at least according to one of Dagger’s creators, [Sam Alba](https://www.linkedin.com/in/samalba/), co-founder and vice president of engineering at Dagger, and former vice president of engineering at Docker.

Before the Dagger project was created in 2018 and while at Docker, [Alba wrote in a blog post](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/) for The New Stack: “While we made great progress, more remains to be done here, in particular going beyond containers as the sole unit and orchestrating pipelines of containers.”

While at Docker, “the overall automation of the software supply chain” was not solved, Alba wrote: “We unlocked so much value toward the end of that supply chain but didn’t adequately address the needs of developers as they coded and collaborated, and today CI/CD remains a mess.”

For image sharing locally, Docker can be great. During his talk, Mouat showed the feasibility of using an upstream [Golang](https://thenewstack.io/golang-what-are-constants-in-go-and-how-do-you-use-them/) image, compiling it in a [Go](https://thenewstack.io/go-the-programming-language-of-the-cloud/) application, and setting an entry point.

“And that works, as you’re probably aware. The problem is, we’ve still got our build tool in that image,” Mouat said. “So, our final image doesn’t just have our application. It’s got all the build tools, and it’s got all the stuff in the underlying Debian operating system that we don’t really need to run our application. Ideally, I would like to get rid of that because it’s just a source of potential CVEs [Common Vulnerabilities and Exposures] and problems.”

As Mouat said during his talk, Dagger is not designed just for building container images. It’s really designed to solve the whole CI/CD problem, “where you’re trying to debug CI/CD but it works differently,” Mouat said. “You can’t run it locally, or at least it doesn’t run the same locally as it does remotely, and you end up with 20 commits that are all like, ‘works this time, sort of,’” Mouat said. “It always continues to fail, and you’re pulling your hair out. That’s what Dagger is aimed at.”

## The Right Container
Docker remains king in a number of ways, including its lightweight nature and reproducibility. While arguably limited in some respects, it’s perfectly adequate for other use cases. This is evident in my project, where I just want to share my Neo4j knowledge graph with a couple of people.

However, for full-blown CI/CD, and especially for the security challenges associated with it, Dagger merits close consideration. This also aligns with the well-established need to [shift left](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/) in security, which continues to be a challenge.

“Shifting left software supply chain security and compliance is the only way to limit an organization’s operational risk, and it has even become a precondition for working with most governments. Building policy-driven security management into the software supply chain creates the foundation for an enhanced security posture,” Volk said. “This protects the entire software supply chain in a proactive automated manner without ending up as seaweed on the anchor of app developers. This makes CIOs very happy.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)