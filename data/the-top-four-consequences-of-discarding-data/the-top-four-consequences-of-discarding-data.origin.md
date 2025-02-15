# The Top Four Consequences of Discarding Data
![Featued image for: The Top Four Consequences of Discarding Data](https://cdn.thenewstack.io/media/2025/02/0f4b428e-missingpiece-1024x576.jpg)
Data costs a fortune. The [average cost](https://hydrolix.io/the-cost-of-discarding-data/) of storing 1 terabyte is about $3,351 per year, and in 2025, the volume of unstructured data is expected to hit 175 billion terabytes. This explains why more than 400 engineering professionals say their companies discard [data](https://thenewstack.io/data/) to cut costs.

Other companies [sample data](https://hydrolix.io/blog/4-observability-anti-practices/), ingesting, [storing](https://thenewstack.io/storage/) and analyzing only half of what’s coming in from their application and infrastructure. Either way, not keeping all their data has repercussions, and may cause an even greater impact on a company’s bottom line.

Discarding or sampling data is like throwing out 500 pieces of a 1,000-piece puzzle. Yes, you can get an idea of the image in the puzzle; however, you can’t see the full picture. You need that full picture to truly take advantage of [observability data](https://thenewstack.io/observability/) to predict potential incidents before they happen, and ensure your applications and infrastructure are operating as they should. Otherwise, you risk dangerous consequences:

**1. Unresolved cyberthreats**: In order to detect and shut down low and slow attacks, like advanced persistent threats (APT), investigators must look back many months or even years to understand what happened, what the root cause was, who was affected, where it started and so on.
But when data is discarded, it increases the chances of not having all those details. It’s like throwing out the needle with the haystack. Important information may go down the drain, leaving gaps in the attack chain that can’t be filled. That means investigators may not find and shut down the root cause, increasing the risk of the attack persisting — or it may take more time to connect the dots, leaving an open window for more attacks.

**2. Compliance issues**: Compliance regulations include mandates to store log data for security, auditing and legal purposes. For example, the Sarbanes-Oxley Act (SOX) requires companies to maintain detailed logs for auditing and financial reporting.
The Gramm-Leach-Bliley Act (GLBA) requires financial institutions to secure customer data, which involves log storage to monitor access and changes. The Payment Card Industry Data Security Standard (PCI DSS) requires storing logs for at least one year. The Health Insurance Portability and Accountability Act (HIPAA) requires health-care organizations to log and monitor access to electronic protected health information. If companies do not meet the data retention requirements, they could face steep fines, among other penalties.

**3. Faulty AI models**: To predict when end users will experience poor performance, especially when it comes to streaming video and web applications, companies may use AI for anomaly detection. However, to train those models, they need data.
The models need historical data to identify patterns, to determine what’s normal and abnormal, and to fine-tune those models so they can detect performance issues based on past behavioral indicators. For example, companies need to be able to predict when a performance issue will occur so they can reroute traffic — for example, to a different content delivery network (CDN). Without data that shows the warning signs, the models can’t make those predictions.

**4. Resource inefficiencies**: What if you are using 1,000 servers but you only need 750? How would you know? By analyzing log data from cloud services, you can see where you need to scale up resources and how well those servers are performing. Without visibility into how your services are performing, you may be running services on containers that are overprovisioned.
Or, you may miss an issue with a service, such as a bug that is causing timeouts and repeated retries, resulting in excessive compute charges. You need access to log data to understand why failures are occurring and know where you may need more or fewer resources. In other words, you can’t spot the problem child without watching all the children.

If you keep all of your data, you can avoid these consequences. But you need to keep it all without breaking your budget.

Ingesting, retaining and analyzing all of your data is key for maintaining a healthy, functional and secure infrastructure. Managed observability service Hydrolix for AWS — which recently launched on the[ AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-jmgtt23uz7fkm?applicationId=AWS-Marketplace-Console&ref_=beagle&sr=0-1) and is part of AWS CloudFront Service Ready program — makes that doable.

You can [learn more about Hydrolix](https://hydrolix.io/partner-program/cascade/) here.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)