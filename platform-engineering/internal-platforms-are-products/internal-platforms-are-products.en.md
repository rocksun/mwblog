There is a failure mode so common in platform engineering that it barely gets mentioned anymore. A team ships a self-service workflow — environment provisioning, policy enforcement, automated approvals — and the thing works. Technically, it does exactly what it was scoped to do.

Then, six weeks later, half the engineering org is still on old scripts, Slack is full of exception requests, and the platform team is in an uncomfortable position: either mandate adoption or watch their work quietly routed around.

The engineering wasn’t the problem; the engineering was fine. What failed was the assumption that building the capability was the same as solving the problem.

> Internal platforms are products. Not metaphorically so… but structurally.

Internal platforms are products. Not metaphorically so… but structurally. They have users with competing needs, alternatives that exist whether or not they are sanctioned, friction points that shape behavior, and adoption curves that do not resolve on their own. The difference between a platform that becomes the default and one that gets bypassed is usually not technical quality. It is whether the team building it was thinking like a product team or an infrastructure team.

## The abstraction of “developer” is too coarse to design for

Most platform teams build against broad roles: developer, site reliability engineer, data engineer, security engineer. Those labels are operationally convenient and analytically useless. A team maintaining a decade-old backend service has fundamentally different constraints than a team running [machine learning training](https://thenewstack.io/machine-learning-for-real-time-data-analysis-training-models-in-production/) pipelines or a team responsible for regulated production deployments. Optimizing for the abstract developer means making compromises that serve no specific team particularly well, which is exactly how you end up with a platform everyone tolerates and nobody advocates for.

Product teams use personas not as a UX formality but as a forcing function. Who is this built for first? Whose workflow gets optimized, and who absorbs the trade-off? Platform teams that skip this step tend to ship capabilities that are technically complete and practically ignored.

## Rollout is not adoption

This distinction matters more than most platform teams acknowledge. Shipping a feature and publishing documentation are rollouts. Adoption is a measurable behavior change over time, and it follows a curve that bears little resemblance to a launch checklist.

> Shipping a feature and publishing documentation are rollouts. Adoption is a measurable behavior change over time, and it follows a curve that bears little resemblance to a launch checklist.

Early adopters will work through rough edges because they are motivated, curious, or both. The mainstream will not move until the platform is clearly easier than whatever they are already using. Laggards will hold out until the old path is actively painful. Treating these groups identically (same rollout, same messaging, same level of polish) results in the uneven adoption pattern that [platform teams](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/) consistently misread as a communication failure. It’s not — it’s just a product sequencing failure.

A platform that works extremely well for a narrow segment is more durable than one that tries to cover every case on day one and ends up covering none of them well.

## Friction is a design choice

Platform teams default to treating friction as something to minimize. Faster provisioning, fewer manual steps, automated approvals. That instinct isn’t wrong, but it is incomplete. Some friction is load-bearing — slowing down high-risk changes, forcing explicit acknowledgment at a policy boundary, surfacing cost or security implications at the right moment — these are valid, intentional design choices.

The real problem is friction that has outlived its purpose: Approval gates are added after an audit that no longer applies, and policy checks that treat a low-risk config change the same as a production infrastructure modification. Developers feel it; the platform no longer knows why it exists. Product teams ask regularly what a given constraint is protecting against and whether it is still doing that job. Platform teams almost never do.

Platform teams default to treating friction as something to minimize. Faster provisioning, fewer manual steps, automated approvals. That instinct isn’t wrong, but it is incomplete. Some friction is load-bearing — slowing down high-risk changes, forcing explicit acknowledgment at a policy boundary, surfacing cost or security implications at the right moment — these are valid, intentional design choices.

The real problem is friction that has outlived its purpose: Approval gates are added after an audit that no longer applies, and policy checks that treat a low-risk config change the same as a production infrastructure modification. Developers feel it; the platform no longer knows why it exists. Product teams ask regularly what a given constraint is protecting against and whether it is still doing that job. Platform teams almost never do.

## Behavioral signals are feedback

The complaint that platform teams cannot get user feedback is almost always wrong. The feedback is there, it is just arriving in forms that do not look like feature requests.

Watch what teams do, not what they say. Repeated questions about the same [edge case](https://thenewstack.io/handling-edge-cases-and-exceptions-in-python/) indicate the platform does not handle it, regardless of what the documentation claims. Custom scripts that duplicate functionality already in the platform create friction in the official path that is not worth tolerating. Requests that cluster around the same policy indicate the policy is miscalibrated. These are not user failures. They are diagnostic signals, and ignoring them because they did not arrive in a structured format is how platform teams ship v2 of something nobody used.

## Roadmaps should be written in outcomes

The typical platform roadmap is a list of things to build: a new abstraction layer, a refactored auth flow, and observability tooling. Those are outputs. The question product teams ask—and platform teams should ask—is what changes as a result. What decision gets easier? What risk becomes harder to take accidentally? What costs become visible that were previously invisible?

Framing work this way does not mean building whatever users ask for. Sometimes the right call is a constraint rather than a feature. Sometimes removing flexibility improves adoption by eliminating decision surfaces that teams should not be managing in the first place. But the decision should be made based on impact, not implementation convenience.

This is the approach we take at [env zero](https://env0.com), an infrastructure-as-code governance platform built for platform engineers to establish golden paths across their organizations. Rather than treating the roadmap as a backlog of capabilities, we use product telemetry to surface friction points and behavioral signals: where teams deviate from the golden path, where workflows stall, where exception patterns cluster. That data drives the outcomes we prioritize in each iteration. Not what is technically interesting to build next, but what is actually getting in the way of the teams we serve.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/75945e03-cropped-35e959f0-screenshot-2026-02-23-at-15.14.59.png)

Oleg Danilyuk is the Director of Product at env zero, where he leads product vision, roadmap, and cross-functional collaboration to solve real-world cloud management challenges. He brings over a decade of product experience spanning cloud infrastructure, AI-powered advertising, and medtech....

Read more from Oleg Danilyuk](https://thenewstack.io/author/oleg-danilyuk/)