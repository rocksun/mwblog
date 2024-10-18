# How the Argo Project Is Avoiding WordPress-Type Problems
![Featued image for: How the Argo Project Is Avoiding WordPress-Type Problems](https://cdn.thenewstack.io/media/2024/10/e62150b5-argo-1024x576.png)
This has been a challenging year for open source software with [Terraform](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/) and [Redis](https://thenewstack.io/redis-users-want-a-change/), which are both updating their licenses away from open source and toward a style of “[fair source](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/)” that’s meant to protect the business models of their respective creators.

Now, the [war between Automattic and WP Engine](https://thenewstack.io/the-wordpress-saga-does-matt-mullenwegg-wants-a-fork-or-not/) is heating up in a way that’s leaving thousands of users without updates and creating ambiguity for users. I won’t weigh in on who is right between these two parties. This is ultimately a trademark dispute that has spilled out into the open.

But that’s all it is.

There are a lot of arguments flying around about what fair contribution looks like from people profiting off [open source](https://thenewstack.io/open-source/). These are moral arguments and I’m sympathetic to them, but they are not legal arguments. When you make software open source, you set the rules for its use, and I’m not aware of any major licenses that require specific contributions in return from people who profit from open source.

## Why the Argo Project Is Open Source
When Intuit created Argo ([it’s on the Argo project website](https://argoproj.github.io/)), it made a big bet that Argo was the best way to service business-critical functions. Its creators knew the best chance of making Argo a successful project was to make sure there were businesses heavily incentivized to maintain and expand the project.

The result? Intuit invited [Codefresh](https://codefresh.io/) (now part of [Octopus Deploy](https://octopus.com/)) to become the first project maintainer to build a business model on the Argo Project. A few months later, Red Hat joined to become the second commercial vendor, and 18 months later Akuity joined to become the third.

All three of these commercial maintainers, [Codefresh](https://codefresh.io/?utm_content=inline+mention), [Red Hat ](https://www.openshift.com/try?utm_content=inline+mention)and [Akuity](https://akuity.io/?utm_content=inline+mention), decided to invest in some way in the Argo project, all have full-time maintainers and [contribute at various levels](https://insights.lfx.linuxfoundation.org/foundation/cncf/overview?project=argo&repository=https:%2F%2Fgithub.com%2Fargoproj%2Fargo-cd&dateFilters=Last%2012%20Months&dateRange=2023-09-28%20to%202024-09-27&compare=PP&granularity=month&hideBots=true). I can’t speak for Red Hat or Akuity, but we at Octopus do this because Argo is core to our business and to the value we deliver to our users. We invest heavily in security contributions because our users expect to be secure. We invest heavily in bug fixes and feature contributions because our [enterprise users](https://codefresh.io/enterprise-argo-support/) rely on it.

But let’s be clear, there is nothing in the Argo license that requires us or any other company to contribute to the Argo Project or send payment. This is open source software. It’s [free, as in speech, and free as in beer](https://www.howtogeek.com/31717/what-do-the-phrases-free-speech-vs.-free-beer-really-mean/).

In an era of companies moving to more restrictive licenses and extracting value through trademarks, we haven’t changed our stance. Can it be frustrating when other companies contribute less and claim more? Sure. Worse, I’ve seen other companies attempt to monetize Argo that haven’t contributed anything to the project at all. But does this violate the Apache license that we use to distribute Argo? No.

When Ed Lee, one of the creators of Argo still at Intuit, [added the Apache license](https://github.com/argoproj/argo-cd/commits/master/LICENSE) and we supported the continuation of that license, it was because we believed that open source is powerful enough to withstand bad actors and opportunists. That if we invested in the community, they would be willing to invest in us.

I’m proud of the partnership we’ve built with the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), Intuit and, yes, other commercial Argo vendors.

This collaboration is key because the Argo Project is maintained by a mix of end-user companies like Intuit and Black Rock as well as vendors Codefresh, RedHat, Akuity and, more recently, Pipekit, with the trademark held in trust by the CNCF. Because of this balance of power, it would be impossible for any one company to grab the wheel and change licenses. In fact, our governance prevents anyone from having more than [40% of the vote](https://github.com/argoproj/argoproj/blob/main/community/GOVERNANCE.md) on major issues or conflicts.

At Codefresh, we invest heavily in the security, user experience, reliability and scalability of Argo. We do it not just because it’s the right thing to do, but because we believe it’s the best way to service our customers who selected our [GitOps Platform](https://codefresh.io/product/gitops/) as their technology stack or who use our experts to support their Argo deployments.

Successful open source projects and businesses work when the moral and financial incentives are aligned. I hope the WordPress community can recover from this and that users don’t suffer too long while the fight remains.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)