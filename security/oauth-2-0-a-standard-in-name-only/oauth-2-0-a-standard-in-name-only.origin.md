# OAuth 2.0: A Standard in Name Only?
![Featued image for: OAuth 2.0: A Standard in Name Only?](https://cdn.thenewstack.io/media/2024/12/04250612-1587430004271.jpeg)
[Belinda Fewings](https://unsplash.com/@bel2000a?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/brown-and-grey-padlock--RdoPEdnfnw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
As the CTO of an integration platform company, I’ve spent countless hours analyzing [OAuth 2.0](https://thenewstack.io/master-difficult-user-authentication-requirements-with-oauth/) implementations across hundreds of SaaS applications. While OAuth 2.0 is often touted as a standard, the reality is far more complex and fragmented.

OAuth 2.0 emerged in 2012 as the successor to OAuth 1.0, aiming to [simplify the authorization](https://thenewstack.io/the-cedar-programming-language-authorization-simplified/) process for web and mobile applications. Its goals were noble:

- Mandate the use of SSL for enhanced security
- Simplify the complex signature process required in OAuth 1.0
- Better support for mobile devices, which were rapidly gaining prominence
In theory, OAuth 2.0 would provide a unified way for applications to request limited access to user accounts on other systems without sharing passwords. This would make integrations safer and more [manageable for both users and developers](https://thenewstack.io/zeroops-helps-developers-manage-operational-complexity/).

**A Fragmented Landscape**
However, the reality of OAuth 2.0 implementations is far from standardized. Eran Hammer, the author of the OAuth 1.0 spec, who [famously quit](https://www.wired.com/2012/07/developer-quits-oauth-2-0-spec-calls-it-a-bad-protocol/) during the release of OAuth 2.0, is quoted as saying — “With very little effort, pretty much anything can be called OAuth 2.0 compliant.”

Here are some key issues:

**Excessive Flexibility:**The OAuth 2.0 specification includes numerous optional components and flows. While well-intentioned, this flexibility has led to wildly divergent implementations.**Complexity:**The core OAuth 2.0 specification is 81 pages long, but understanding it fully requires reading thousands of pages across 20+ additional RFCs. This complexity makes it[challenging for developers](https://thenewstack.io/how-ddev-can-help-solve-local-web-development-challenges/)to implement correctly and consistently.**Inconsistent Implementations:**Major platforms often deviate from the core specification or implement specific RFCs uniquely. For example:
-
- Microsoft Azure requires a redirect URI for a token refresh, which is not part of the standard specification.
- Wix has its own “OAuth 2 solution” with non-standard “basic” and “advanced” flows. To refresh the advanced option, you must send the client_id and secret, access token,n, and refresh token, which is very unusual.
**Security Concerns:**Some OAuth 2.0 flows, like the resource owner password credentials grant, are inherently insecure but still permitted by the specification.
**Case Study: The Return of Signatures**
Ironically, one of the primary reasons for moving from OAuth 1.0 to 2.0 was to eliminate the need for complex signatures. However, security concerns have led to the introduction of Proof Key for Code Exchange (PKCE), specified in RFC 7636. PKCE reintroduces a signature-like mechanism to prevent specific attacks, particularly in mobile environments. This development highlights how the OAuth 2.0 ecosystem has had to evolve to address security gaps, sometimes by reintroducing concepts it initially sought to eliminate.

A great example of this type of implementation is Pleo, an expense management company based in Europe. RFC 7636 came out in 2015, and Pleo is the first company I’ve seen use it. Their API for this use case was created in 2022. The rest of their compliance with OAuth 2.0 is excellent. They make all the “recommendations” since they have already implemented PKCE. They are probably OAuth 2.1 compliant, but more on that later.

**What Makes a Good Standard? **
A good standard strikes a delicate balance between specificity, flexibility, and simplicity. Specificity is crucial, providing precise requirements through words like “must” and “required.” However, flexibility is equally important to ensure widespread adoption across various implementations. The key lies in finding the proper equilibrium and avoiding excessive optionality, which can lead to inconsistent implementations.

Simplicity is another critical factor — a good standard should be concise and easy to understand. For instance, OAuth 1.0’s 81-page specification contrasts sharply with OAuth 2.0’s thousands of pages spread across multiple RFCs, highlighting how complexity can be a significant drawback. Ultimately, an effective standard provides precise mandatory requirements while allowing for necessary flexibility, all within a comprehensible framework that doesn’t overwhelm implementers with excessive documentation.

**The Path Forward: OAuth 2.1 and Beyond**
Recognizing these challenges, the OAuth community is working on OAuth 2.1. This revision aims to:

- Consolidate best practices and multiple RFCs into a single, comprehensive document
- Require PKCE for all clients, enhancing security across the board
- Remove problematic grant
[types like the resource](https://thenewstack.io/understanding-kubernetes-resource-types/)owner password credentials flow - Unify the treatment of public and private clients
- Enforce limiting of refresh tokens and secure redirects
While OAuth 2.1 promises to address many of the current pain points, it also raises questions about backward compatibility and adoption timelines.

**Implications for Developers and Businesses**
For developers and [businesses building integrations](https://thenewstack.io/building-an-integrated-infrastructure-for-real-time-business/), the current OAuth 2.0 ‘standard’ presents several challenges:

**Increased Development Time:**Each OAuth implementation may require custom code, increasing development and maintenance costs.**Security Risks:**Inconsistent implementations can lead to security vulnerabilities if not carefully managed.**User Experience Impact:**Variations in OAuth flows can confuse end-users and potentially impact the adoption of integrated services.**Compliance Concerns:**For businesses in regulated industries, ensuring that each OAuth implementation meets security and privacy standards can be complex.
**Conclusion: Is OAuth 2.0 Too Flexible To Be a Standard**
While OAuth 2.0 provides a framework for authorization, its current state is far from a proper standard. Excessive flexibility and fragmentation have led to an ecosystem where “OAuth 2.0 compliant” can mean wildly different things in practice.

As we look towards OAuth 2.1 and potential alternatives like the Grant Negotiation and Authorization Protocol (GNAP), it’s clear that the quest for a truly standardized, secure, and developer-friendly authorization protocol continues. In the meantime, developers and businesses must remain vigilant, carefully evaluating each OAuth implementation they encounter and building robust systems to handle the variations.

The lesson extends beyond OAuth: When designing standards, it is crucial to balance flexibility and specificity. Too much flexibility can lead to fragmentation, while too much rigidity can hinder adoption. As we continue to build and connect digital systems, finding this balance will be key to creating truly effective standards.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)