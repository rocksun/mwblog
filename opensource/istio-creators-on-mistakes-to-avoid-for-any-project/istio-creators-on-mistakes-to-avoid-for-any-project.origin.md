# Istio Creators on Mistakes To Avoid for Any Project
![Featued image for: Istio Creators on Mistakes To Avoid for Any Project](https://cdn.thenewstack.io/media/2024/12/ec8a85ca-bruce-green-1-1-1024x683.png)
Istio has emerged as an open source project that checks off most — if not all — boxes about what an open source project should be.

In addition to its number of contributors hailing from different and often competing organizations, downloads, and of secondary importance, GitHub stars, Istio’s adoption as a [service mesh](https://thenewstack.io/service-mesh/) has amassed many superlatives and arguments for why it’s a very good choice. Like [Linkerd,](https://thenewstack.io/some-linkerd-users-must-pay-fear-and-anger-explained/) Istio is one of the most popular open source service meshes.

But that does not mean that there were not a number of stumbles along the way from when [Istio](https://thenewstack.io/ambient-mesh-can-sidecar-less-istio-make-applications-faster/) was created to today. Istio has set a new standard for service mesh in cloud native environments, offering security, [observability](https://thenewstack.io/observability/) and traffic management for all applications. However, Istio’s creators struggled from the outset with what the community of users really needed. Upon the launch of 1.0, marketing was involved and the hype did not necessarily live up the promise — or at least it didn’t initially.

Considering that Istio is now a leading service mesh used for observability, the travails and struggles of its creators serve as a great lesson about what not to do in many cases — including the mistakes that can be avoided early on for any open source project, especially for those whose creators have great ambitions. The project creators’ learnings were described in detail during a packed session (I had never seen such a long line for a talk before before the session began) at [KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) in Salt Lake City during their talk, “[What Istio Got Wrong: Learnings from the Last Seven Years of Service Mesh](https://kccncna2024.sched.com/event/1i7nP?iframe=no).” Istio co-creators from Solo.io — [Louis Ryan](https://www.linkedin.com/in/louiscryan/), CTO at Solo.io, and [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) co-creator and [Christian Posta,](https://www.linkedin.com/in/ceposta) the global field CTO at Solo.io — described Istio’s success story, warts and all.

## Vision and Hiccups
![](https://cdn.thenewstack.io/media/2024/12/5934b5e1-capture-decran-2024-12-06-185942.png)
One of the slides from the KubeCon+CloudNativeCon presentation. Source: Solo.io

A misstep at the beginning of the project’s creation involved focus and vision, and how both are needed and not exclusive to one another — because an unfocused approach to fulfilling a vision can lead to disaster. As Ryan explained during his talk, Istio was initially created to “connect, secure, control and observe.”

“One of the bigger problems in Istio was those are the goals; those are the vision, but vision and focus are not the same thing. And if we had focused on maybe one or one and a half of those things, I think the project would have avoided some of the missteps that happened early on,” Ryan said. “I’m as guilty of that as anybody: We had ambitious goals. We wanted to do a lot of things where there were a lot of real problems to be solved, but focus was perhaps something that was an issue early on in the project.”

In the early stages of Istio’s development, there were initially 50 CRs. “That’s a lot of API surface and a lot of features — features that users would, in any case, take multiple years to fully digest and consume. Never mind us knowing exactly how they were going to use them from the get-go and shipping them all at once,” Ryan said. “So, that’s been a long and very painful lesson. Some of the refactors we’ve gone through have obviously reduced or been more focused on how we try to deliver on that vision. “

It quickly became apparent that what worked at [Google](https://cloud.google.com/?utm_content=inline+mention) — Istio was initially created under the Google umbrella — did not necessarily work for other organizations. As Ryan described, he had worked on projects that “connected, secured, observed and controlled” while at Google. “I understood the problems they were designed to solve and how they were being built at Google. But building those things at Google is not the same as building them for a radically different audience,” Ryan said. “A huge learning experience for me was internalizing that the things I had learned to be important inside of Google were not the same things that would be important to you.”

Version 1.0 of Istio was released in July 2018, there was a lot of marketing, interest and high expectations for the release that did not meet expectations.

“If you build something with quality and deploy it, people are going to be happy. You’ll get a net positive result — they’ll promote it, talk to their friends, and make public statements about how amazing it is and how it solved a pain point or provided value,” Posta said. “Unfortunately, Istio 1.0 did not do that from the get-go.”

Upon downloading the binaries and attempting installation for Istio 1.0, the process often failed, Posta said. Proxies occasionally launched, but control plane pods frequently recycled themselves, creating instability. The documentation was insufficient, particularly for large clusters, which did not operate as intended. The advertised multi-cluster support at the time also failed to deliver. These shortcomings prevented the achievement of a positive network promoter score, resulting in frustration and confusion among users, Posta said.

The lack of focus in Istio 1.0 contributed heavily to the struggles. The features included in the initial release — such as connecting, securing, controlling and observing — were extensive, Posta said. “There were a lot of features in Istio 1.0. When we first announced it, there was a lot of stuff and it sounded exciting and [it was] stuff that you need,” Posta said. “Although the list of capabilities appeared exciting and necessary, the experience of using the product did not align with expectations.” Users were left unsure of where to begin, even with basic functionality like traffic shifting, which “was not very clear in Istio 1.0.”

Organizational silos within enterprises compounded the difficulties. Different teams managed networking, security, infrastructure and application development. This division made it unclear which team should take responsibility for Istio. With its hybrid capabilities spanning networking and security, Istio lacked a natural owner. At the time, cross-functional teams were rare, and platform engineering or platform teams had not yet emerged as a common structure. This organizational ambiguity left Istio without a clear home within enterprises, Posta explained.

A takeaway after reviewing my

[@KubeCon_]NA notes on[@soloio_inc]‘s[@christianposta]and Louis Ryan talk “What Istio Got Wrong: Learnings from the Last Seven Years of Service Mesh” is open source projects can suffer when multi-functional teams are targeted.[https://t.co/ed5mTa8igr][pic.twitter.com/cvbRQYO85b]— BC Gain (@bcamerongain)

[December 11, 2024]
“Enterprises were structured in silos. They had different teams responsible for different areas: Networking was a team, security was a team, infrastructure was a team and application developers were a team,” Posta said. “When people initially installed or downloaded it, they were like, ‘Who is going to run this? Who is going to use this?’”
The shift to Istio 1.1 brought a renewed emphasis on predictable and regular releases. A quarterly release schedule was adopted, helping to rebuild confidence and establish a rhythm. Since then, this schedule has been largely maintained, with only minor deviations, reflecting a commitment to consistency and improvement, Ryan and Posta explained.

Efforts were made to involve various vendors in Istio’s development. One notable success was the establishment of a governance model — specifically an open governance framework, Posta said. Although Istio was not initially part of an open foundation, governance structures were implemented to encourage vendor participation and foster collaboration. A steering committee and a technical oversight committee were created, with seats on these committees allocated based on levels of contribution to the project. This contributorship-based model incentivized active involvement in the project, Posta said.

## Set for the Future
Despite missteps and challenges, the Istio community demonstrated resilience. The pursuit of ambitious goals in the technology industry requires time, often spanning years, Posta explained. While hype cycles may peak quickly, meaningful progress demands sustained effort. “Contributors to Istio, many of whom have dedicated nearly a decade to the project, illustrate this commitment,” Posta added.

Users previously struggled with how they could use Istio. They still are sometimes uncertain about the features they want, Posta said. “Now, we try to be more focused and advise users to pick one thing they want to succeed with in their implementation and then move on to the next — whether it’s a security feature, an observability goal or traffic management,” Posta said.

“Almost every engagement Solo generally starts with a focus of delivering “incremental success,” Ryan said. “The same approach applies to software delivery and open source projects. Without focus, if you try to do too many things at once, you’re going to have quality problems,” Ryan said. “And boy, did Istio have quality problems.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)