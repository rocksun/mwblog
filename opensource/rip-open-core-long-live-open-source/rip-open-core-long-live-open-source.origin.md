# RIP Open Core — Long Live Open Source
![Featued image for: RIP Open Core — Long Live Open Source](https://cdn.thenewstack.io/media/2024/11/8ff0d5c9-markus-spiske-8oykwqgbskq-unsplash-1024x683.jpg)
[Markus Spiske](https://unsplash.com/@markusspiske?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/tilt-shift-photography-of-html-codes-8OyKWQgBsKQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
The significance of open source has never been more apparent. It’s critical for how we build software today and will only become increasingly prominent as time passes. The problem is the way we’re used to introducing open source into the market is no longer relevant.

In 2022, I wrote [“The Future of Open Source, or Why Open Core Is Dead](https://thenewstack.io/the-future-of-open-source-or-why-open-core-is-dead/).” Since then, multiple companies have pulled the plug on open-core models, resulting in several significant fiascos. I’ve seen how the turmoil and questions around open source continue to grow while also witnessing first-hand how impactful open source can be. Open source initiatives (like the one I’m working on — OPAL) continue to grow and thrive, reinforcing the powerful reach and collaborative spirit of true open-source projects.

**Getting With the Times**
To quickly recap the 2022 article, In *The Future of Open Source, or Why Open Core Is Dead*, I described the limitations of the open-core model and why it often backfires.

Open-core was originally popular because it allowed companies to build a community around a free product version while charging for a more full, enterprise-grade version. This setup thrived in the 2010s, helping companies like [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) and Redis gain traction.

But times have changed, and today, instead of enhancing a company’s standing, open-core models often create more problems than they solve.

The speed at which software is adopted and built has increased exponentially. Rather than fostering growth, companies relying on open-core found themselves trapped. As soon as their projects gained traction, they became easy prey for competitors who could use the free, open-core version to develop competing services.

This results in companies having to race against their own [open source communities](https://thenewstack.io/how-to-give-and-receive-technical-help-in-open-source-communities/), imposing limitations on them or withdrawing from the open source offering altogether.

[Elastic is a prime example of where this happened](https://opensourceconnections.com/blog/2021/01/15/is-elasticsearch-no-longer-open-source-software/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform). After building a successful OSS project, Elastic watched as multiple companies — AWS among them — built services directly on top of it, undercutting Elastic’s own offerings. This resulted in Elastic having to shift the licensing for Elasticsearch in a desperate attempt to limit the exploitation of their code by competitors, resulting in a storm of criticism and confusion in the community.
Docker saw something similar when its open source product gained momentum, only to have the commercial version struggle. Attempts to restrict the OSS version led to a backlash and distrust from the open-source community.

**The Growing Winds of Change**
As I predicted in 2022, the shift away from open-core continues to accelerate as more notable companies abandon it.

In August 2023, HashiCorp’s Terraform, a widely adopted tool in infrastructure-as-code,[ changed its licensing model to restrict commercial competitors](https://www.theregister.com/2024/05/24/opinion_column_terraform/). This shift resulted in a community backlash and the creation of [OpenTofu](https://opentofu.org/)—a fork that allowed the open-source community to keep Terraform’s core functionalities free from restrictive licensing without strings attached.

A year later, Cockroach Labs[ announced that it would abandon its open-core model for CockroachDB](https://thenewstack.io/cockroach-rescinds-open-core-for-a-free-enterprise-version/) instead of offering only an enterprise-licensed version for self-hosted users. As in previous cases, the change aimed to prevent competition from arising when rivals use Cockroach’s product against it, offering it as a commercial service without contributing back to Cockroach Labs.

Sentry, too,[ recognized the pitfalls of an open-core approach and responded by introducing a Functional Source License (FSL)](https://blog.sentry.io/introducing-the-functional-source-license-freedom-without-free-riding/). This license allows users broad freedom to run and modify Sentry but with a critical caveat: they can’t use it to compete directly with Sentry. This change was made to supposedly protect the project’s sustainability while ensuring that Sentry’s efforts aren’t easily replicated or exploited for commercial gain by others.

The trend reflected in these examples is clear: companies are moving away from open-core because the model is increasingly incompatible with maintaining both community trust and commercial security.

**A New Hope – Back to True Open Source**
While open-core and source-available models had their moment, companies are beginning to realize the importance of true open source values and are finding their way back. This return to open source is a sign of growth, with businesses realigning with the collaborative spirit at the core (wink) of the OSS community.

More companies are adopting models that genuinely prioritize community engagement and transparency rather than using them as marketing or growth tactics.

After a three-year detour into source-available licensing to mitigate competition from unlicensed commercial providers, Elastic[ recently reintroduced Elasticsearch and Kibana under the AGPL](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/), an OSI-approved license. This choice reestablishes Elastic’s commitment to the open source community and allows developers to trust that their contributions will support a fully open and transparent project.

Elastic de facto embraced an open-foundation model (more on that in a second), especially in analytics and security, which allows it to differentiate its commercial offerings without withholding core functionalities from the community. By nurturing foundational projects that complement its enterprise products, Elastic can maintain a clear boundary between free community use and paid enterprise features — one of the key lessons many companies are learning as they move beyond open-core.

This healing process signals a broader movement as companies recognize that building true open source projects fosters lasting community support and avoids the pitfalls of models that attempt to restrict usage or lock in customers.

**The Path Forward – Open Foundation**
As the open-core model fades, we’re seeing a more sustainable approach take shape: the Open-Foundation model. This [model allows the open-source offering](https://thenewstack.io/data-unions-offer-a-new-model-for-user-data/) to be the backbone of a commercial offering without compromising the integrity of the OSS project. Rather, it reinforces it as a valuable, standalone product that supports the commercial offering instead of competing against it.

For open-foundation to work, the OSS project must be viable on its own, offering real value without requiring a paid upgrade to fulfill its core purpose. This allows for a clear distinction between the open source and commercial versions, each with its unique value proposition.

One practical test for this model is simple: when a company considers adding a feature, it should be immediately apparent whether it belongs in the OSS project or the commercial offering. Ideally, contributions to the OSS version should support and enhance the commercial product without creating dependency loops. This alignment preserves the integrity of the open source project while allowing the commercial version to thrive.

Several companies effectively exemplify the open-foundation model. Vercel uses this approach with projects like[ Next.js and Svelte](https://vercel.com/oss), creating powerful tools for developers while monetizing with complementary services. At[ Permit.io](http://permit.io/), our OSS projects like[ OPAL](https://github.com/permitio/opal),[ Cedar-Agent](https://github.com/permitio/cedar-agent), and[ Permit-CLI](https://github.com/permitio/permit-cli) also leverage open foundation, offering core tools as open source while building a business around extended capabilities. Supabase has taken a similar route, contributing to various[ PostgreSQL-based projects](https://supabase.com/open-source) that serve as the bedrock of its commercial offerings.

Elastic’s recent decision to return Elasticsearch to open-source with AGPL is another example of an open-foundation in action. Core functionality is open, while advanced enterprise features support their paid offerings in analytics and security. Other companies, like[ Resend with React-email](https://github.com/resend/react-email) and[ Spotify with Backstage](https://backstage.io/), use open foundation to foster community collaboration, leveraging OSS to build engagement while aligning with sustainable commercial goals.

These examples show that an open foundation offers a promising path forward, reinforcing the idea that open source can serve community and business interests.

**Modernized Roman Concrete**
If we ask ourselves where we are headed — we should look to something as enduring as concrete. We often idealize Roman concrete, imagining it as superior to the modern version — a technology lost to the ages, and feel a sense of loss. But the truth is, it wasn’t ever “better,” and it was never truly lost. Like concrete, open source is a fundamental cornerstone of human civilization; it is monumental in building things and is here to stay. Changing from the Roman recipe (i.e., open-core) to a more modern one (e.g., open-foundation) doesn’t mean anything is lost — the collaboration, resilience, and community value of open source will endure, adapting to new models and meeting the needs of a changing landscape without losing its essence.

Open source may shift and transform, but it’s as strong as ever — and likely to remain so for generations. It is all about finding the right way to leverage it efficiently.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)