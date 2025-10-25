[![](https://substackcdn.com/image/fetch/$s_!JfEm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf29953d-3248-4296-9bcb-050b60a061dc_6609x4406.jpeg)](https://substackcdn.com/image/fetch/$s_!JfEm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf29953d-3248-4296-9bcb-050b60a061dc_6609x4406.jpeg)

Photo by cottonbro studio: https://www.pexels.com/photo/man-in-gray-long-sleeve-suit-holding-a-pen-8369520/

It was hard to ignore the AWS outage that happened this past Monday. Even if you didn’t see any impact first hand, you probably heard stories of smart doorbells not ringing, smart beds overheating and smart fridges developing a potty-mouth.

There was a lot of early speculation about the cause, ranging from rogue AI to conspiracy theories about “internet kill switches”. But now Amazon have release an [official summary](https://aws.amazon.com/message/101925/) detailing the root cause.

Unfortunately, it’s not an easy read. Lots of long, information-dense paragraphs. But fortunately, I was really struggling with my blog topic for the week! So here’s my summary.

**DynamoDB errors impacted a wide range of AWS services**. The summary details impacts to EC2 and NLB, but other services listed include Lambda functions, SQS/Kinesis, EKS, and Redshift to name a few. This resulted in a broad, but not total outage of service in us-east-1 and some impact to other regions.

Cracking the nut a little, the summary detailed how problems cascaded from DynamoDB to EC2 and finally NLB. DynamoDB is key to the system that manages EC2 lifecycles, so those errors prevented new instances being created. This caused a delay in propagating network state information, causing erroneous health check failures. These failures brought down NLB nodes, causing connection errors.

There’s an old proverb in SRE circles: “It’s always DNS”.

A race condition in management of DNS entries for DynamoDB resulted in the removal of the entries for all IPs in the us-east-1 region. This stopped anyone talking to DynamoDB in that region, kicking off the cascade of effects described above.

The specifics of this failure are detailed in a mammoth 776 word paragraph including a fair bit of architectural detail. What it boils down to is that multiple “DNS Enactors” are responsible for updating DNS entries for DynamoDB, and there are checks in place to make sure they always write the most up-to-date information. But this time, an Enactor was delayed more than expected, and applied old information on top of new. This old information was seen as stale and cleaned up by the “DNS Planner”, deleting all the DNS entries.

This is one of those rare outages where you can’t point to a code or configuration change as the root cause. In this case, it was just the wrong combination of events happening at the wrong time, exposing a flaw.

This raises the question as to why the problem happened in us-east-1 and not another region. Were I to speculate (and I will), it could be down to the sheer popularity of that region, with extra load from users and Amazon services alike resulting in the delays that kicked off the whole situation.

The long root-cause paragraph ends with the sentence *“This situation ultimately required manual operator intervention to correct”*. This held true across the downstream failures in EC2 and NLB. I won’t go into all the specific actions listed, but they included manual repair of data and tooling as well as applying throttles to reduce excess load.

Late in the summary are a list of the actions Amazon is taking to prevent this kind of issue happening again. Explicit mitigations are detailed for DynamoDB, EC2 and NLB. Most importantly, the race condition that caused the whole problem is to be fixed, and EC2 and NLB will receive updates to “velocity control” and throttling (which to me sound like the same thing).

Interestingly, they’ve disabled the DNS Planner and DNS Enactor automations while the race condition fix is implemented. This could imply that DNS is being managed manually, which I would assume could have impact on scaling of DynamoDB for a period.

For me, the main lesson from this incident is that *complex systems behave in complex ways*. AWS and other hyperscalers are probably the most complex systems most of us will get our hands on.

Experiencing the wrong set of events in DynamoDB brought it down completely, and DynamoDB is sufficiently critical to other systems that they also got into bad states requiring manual intervention.

When looking at the resolution, it was interesting seeing the timings of different events. The underlying DynamoDB problems were resolved at 2.40AM PST, but knock-on effects on EC2 and NLB lingered for almost 12 hours longer, being resolved at 2.09PM and 2.15PM respectively. This shows that secondary effects can be just as severe as primary ones, and sometimes establishing a root cause first can help you tackle problems in the most effective order.

Will this make people re-think building on AWS? Maybe some. Will it result in a renaissance of simple VPS-based hosting? Probably not.

But when architecting our own systems, this shows that it’s important to understand what the most critical components are, and what might happen if they suddenly stopped working.