# Bring Shadow APIs Into the Light With Service Catalogs
![Featued image for: Bring Shadow APIs Into the Light With Service Catalogs](https://cdn.thenewstack.io/media/2024/10/1c413708-shadowapis-servicecatalogs-1024x576.jpg)
As organizations continue to migrate toward [microservice-based architectures](https://thenewstack.io/microservices/), implement real-time data strategies and shift toward API-first approaches, managing and governing APIs often becomes increasingly complex.

## API Sprawl and Shadow APIs Add Complexity and Risk
The more APIs you have, the more APIs you need to secure, manage and govern. It doesn’t take long to reach the land of “[API sprawl](https://thenewstack.io/heres-how-to-tame-your-api-sprawl-and-why-you-should/),” where there are hundreds, or even thousands, of new APIs that aren’t properly accounted for.

While this all seems simple and predictable, it’s something that many organizations still struggle with. These struggles typically take the form of “[shadow APIs](https://thenewstack.io/shadow-zombie-and-misconfigured-apis-are-a-security-issue/)” — undiscovered and unmanaged legacy APIs that are often still running in production. These APIs present serious risks for any business.

### Increasing Vulnerability to API Security Breaches
The lack of visibility into a rapidly growing API landscape creates a breeding ground for security vulnerabilities. Shadow APIs, often unmonitored or poorly maintained, become prime targets for attackers who exploit improper authentication logic or weak encryption standards. Kong research highlights this risk, with the number of annual attacks forecast to [grow 548%](https://konghq.com/resources/reports/ai-and-api-adoption-challenges) by 2030, for a total of 42,000 API attacks in the U.S. alone.

### Data Leaks and Sensitive Information Exposure
Because these APIs are often not tracked or monitored, they can inadvertently expose sensitive data, such as customer personally identifiable information (PII), financial records or proprietary business information. For example, a legacy API developed for a now-defunct service may still have access to sensitive databases, unintentionally exposing data to anyone who knows how to call it. What’s most concerning is that these data leaks often occur silently, without anyone in the organization noticing until it’s too late.

### Regulatory Standard Noncompliance
The inability to fully account for all APIs means that organizations struggle to comply with industry regulations. APIs that process sensitive data may fall outside of mandated compliance checks, such as [GDPR](https://gdpr-info.eu/) or [HIPAA](https://www.hhs.gov/hipaa/index.html) audits, simply because they aren’t cataloged as part of the organization’s official API inventory. This lack of oversight can result in costly regulatory fines, not to mention the potential damage to customer trust.

## Improving API Governance With Service Catalogs
Just like a library catalog helps patrons find materials, a [service catalog](https://thenewstack.io/microservices/what-is-a-microservice-catalog-and-why-do-you-need-one/) acts as a centralized system of record for an organization’s services and APIs. The service catalog is the discovery and visibility mechanism for all of your APIs and services. In other words, it’s the bane of API sprawl and shadow APIs. Let’s break it down further.

One of the most powerful features of a service catalog is its discovery engine, which dynamically updates the catalog as new services are deployed and inactive ones are decommissioned. The discovery engine allows the service catalog to retain both its accuracy and reliability as a source of truth with zero manual intervention.

It is important to note, however, that not all service catalogs are created equal.

Certain catalogs whose discovery engines do not deeply integrate with critical infrastructure (like API gateways and service meshes) typically need to be populated and maintained by hand. These manual processes are highly prone to error and result in outdated catalogs almost immediately.

In other words, if your service catalog can’t auto-populate, it undermines the entire purpose of adopting such a solution. You may as well try to manage, measure and govern every API and service manually in an Excel sheet. This is untenable for an organization with a massive service footprint.

An automated service catalog that is built to deeply integrate with various infrastructural applications offers complete visibility into an organization’s north-south and east-west API traffic. This allows the catalog to display analytics about the service (such as request count, error rate and latency) that reflect its dynamic real-world usage, rather than static and outdated data.

## Take Control of Your API Landscape
Organizations can no longer afford to leave critical customer data, PII and authorization credentials just “floating” out there, unseen, in production. Hope cannot be your API security strategy.

Recognizing the need for a well-integrated, automated service catalog, we built the [Konnect Service Catalog](https://konghq.com/products/kong-konnect/features/api-service-catalog), now available in [public beta](https://konghq.com/blog/product-releases/service-catalog). Try it out now by logging into [Kong Konnect](https://cloud.konghq.com/login?utm_medium=syndication&utm_source=newstack&utm_campaign=konnect-demo), registering for a [30-day free trial](https://konghq.com/products/kong-konnect/register?utm_medium=syndication&utm_source=newstack&utm_campaign=konnect-demo) or checking out [this live demo](https://www.youtube.com/watch?v=MctyzrVMCfQ) that showcases its UI/UX.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)