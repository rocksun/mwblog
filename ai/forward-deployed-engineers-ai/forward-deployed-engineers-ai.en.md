Companies adding AI to their products often think that a powerful model is the key to successful integration. This assumption holds for early-stage use cases, where using an API can quickly demonstrate value. However, it stops working once AI becomes part of larger systems that different teams depend on.

At that point, the biggest challenge is making the model work reliably within existing infrastructure alongside internal data, legacy software, compliance rules and workflows that were never designed for AI. [MIT’s NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) Initiative studied 300 public AI projects and found that 95 percent of enterprise AI pilots produced little or no measurable impact on profit and loss. The problem was not the models, but how they were put into use.

When AI companies like OpenAI and Anthropic began rolling out their models to large enterprises, they encountered the same implementation challenges. To solve this, [they began placing engineers directly with clients](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/). These engineers work with the company’s teams to integrate the system, launch it in production and improve it as issues appear. This close collaboration shortened feedback loops, accelerated deployment and increased the chances that systems actually worked in production. This approach is now known as [forward deployed engineering (FDE)](https://thenewstack.io/why-the-forward-deployed-engineer-is-techs-hottest-job/).

This shift is getting harder to overlook. OpenAI set up its forward deployed engineering team in 2024 and quickly grew it. Anthropic also announced plans to grow its Applied AI group to meet rising demand. Across the industry, job postings for forward deployed engineers jumped by more than 800 percent between January and September 2025. AI labs seem to agree that the future of AI adoption relies on deployment, not just improving model quality.

## The origin of forward-deployed engineering

The concept of forward deployed engineering started well before AI companies became popular. It actually began around twenty years ago at Palantir.

Palantir develops data intelligence software for government agencies and large financial firms. These organizations operate in environments with complicated infrastructure, strict compliance requirements and operational complexity that off-the-shelf software cannot easily solve. The usual approach of shipping the product, providing documentation and letting the customer handle the rest did not work in these cases.

So Palantir introduced a new role called “Deltas.” Deltas are software engineers who work directly with customers and build solutions within the client’s environment, focusing on what is needed to make the system work in real-world situations. While traditional software engineers design features for many customers at once, Deltas take a different approach. They concentrate on one organization at a time, learning its infrastructure, data and workflows, then adapting the system to fit how that organization actually works.

This approach was so effective that until 2016, Palantir had more Deltas than software engineers. For a software company, this was unusual. More than half of the engineers worked directly with clients instead of building the core product.

This same idea is still at the heart of forward deployed engineering today. To see why this model is effective, it helps to look at what forward deployed engineers actually do.

## What FDEs actually do

Forward deployed engineers work directly within a client’s environment with a clear goal: get the system running in production and keep it running smoothly.

In practice, this means becoming part of the client’s technical team. A forward deployed engineer joins the company’s communication channels, works closely with product and engineering teams and builds directly with the client’s data and systems. They help decide what to build and they also take responsibility for building, integrating and ensuring it works well after launch. This role combines software engineering, product insight and operational know-how, and success is measured by how well the system is used and performs, not by time spent.

A typical engagement starts by learning how the organization really works. This involves mapping data flows, identifying where AI can help or automate tasks and determining how teams will use the results. Afterward, the forward deployed engineer builds and integrates systems to meet these needs. Once the system is live, the engineer stays involved, making adjustments, improving reliability and responding to feedback as people use the system.

As one FDE put it, “The model is usually the cleanest part. The hard part is finding the workflow nobody documented, the data source people actually trust, and the person who knows why the process works that way.”

![](https://paper-attachments.dropboxusercontent.com/s_A338BDD7AE57218BBDDFE8EAC2901991A9BE9315A0F4F64ADDE7007CB485DFEB_1779880519343_VpuMemcA.png)

What FDEs do

That is what separates the role from traditional consulting. Consultants usually work for a set time and are judged by what they deliver. Forward deployed engineers, on the other hand, are measured by whether the system continues to run well and continues to add value after it goes live. Their job does not end at handoff, because they stay involved until the system becomes part of daily operations and the client’s own team can manage it.

Knowing what this work looks like day-to-day helps explain why companies building advanced AI systems have invested so much in this approach. But it still leaves the question: Why does AI need this model when traditional software didn’t?

## Why AI needs FDE more than traditional SWE

In traditional software, most of the risk comes at the beginning. You design, integrate and test, and once everything works, it usually keeps working. If something breaks, it’s easy to find and fix the problem.

AI systems introduce a different kind of risk because they are probabilistic. A model may perform well in testing yet degrade once exposed to production data and real users. Instead of failing outright, the system can become unreliable, returning inconsistent or irrelevant results that slowly erode user trust.

![](https://paper-attachments.dropboxusercontent.com/s_A338BDD7AE57218BBDDFE8EAC2901991A9BE9315A0F4F64ADDE7007CB485DFEB_1779880474691_NE1eNfms.png)

Why AI Deployments need FDE

The typical software delivery model isn’t built to handle this type of failure because internal teams are set up to deliver features, not to remain involved long enough to stabilize a system that evolves over time. Consultants, on the other hand, usually work within fixed scopes and deadlines and once their job is done, they move on. In both cases, ownership fades at the moment an AI system needs the most hands-on attention.

Forward deployed engineers help solve this problem. By working within the customer’s environment, they spot issues as they arise, make quick adjustments and improve the system in real time. That proximity is what turns a promising model into something reliable enough to depend on.

## How the FDE model is becoming more accessible

The FDE model used by leading AI companies is typically inaccessible to smaller organizations due to the cost of sustaining it. Companies with large budgets can assign multiple engineers, sometimes entire teams, to a single client deployment. Smaller organizations face the same implementation challenges but don’t have the engineering capacity to dedicate teams to open-ended integration work.

To close that gap, a few different approaches are now emerging. AI labs are expanding deployment support around their models, with OpenAI launching a [dedicated deployment company](https://openai.com/index/openai-launches-the-deployment-company) and Anthropic, OpenAI, and Cohere all increasing investment in forward-deployed or applied AI roles. Large consulting firms are also filling the gap through partnerships designed to help enterprises take AI beyond pilots. At the same time, platform companies, such as [Bit Cloud](https://bit.cloud), are pairing forward-deployed engineers with tooling so a single engineer can bring a production-ready starting point into a customer’s environment rather than building each integration from zero.

These approaches all share the idea that the main bottleneck has changed. Now, the challenge is not the model itself, but finding engineers who can work within a customer’s systems, understand real workflows, and deliver solutions that work in production.

## Wrapping up

Forward deployed engineering began in response to a real-world problem. Organizations had access to more powerful software but often struggled to make these systems work in their day-to-day operations. The main issue was not the technology, but the gap between what the software offered and what organizations actually needed for their own infrastructure, data and workflows.

AI labs ran into the same problem Palantir faced twenty years ago. The most reliable way to make complex systems work was to put engineers close to the people using them, the data they depended on and the problems they were meant to solve.

As AI becomes part of core business systems, the advantage will go to teams that can move beyond prototypes and make deployment repeatable. Whether that support comes from an internal team, an AI lab or a platform, the companies that get this right will be the ones whose AI investments actually work in production.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/fd90908c-1739284331173-600x600.jpeg)

Oluwadamilola is a software engineer and technical passionate about sharing knowledge his with the community

Read more from Oluwadamilola Oshungboye](https://thenewstack.io/author/oluwadamilola-oshungboye/)