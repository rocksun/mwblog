# 4 API Security Best Practices
![Featued image for: 4 API Security Best Practices](https://cdn.thenewstack.io/media/2024/07/dcb99323-token-1024x576.jpg)
APIs are the backbone of modern digital solutions. Consequently, API security should be a top business concern. Yet, as with developing businesses, there is always something that you can improve with regard to API security. Therefore, do not consider this article a comprehensive guide but an inspiration on where to start. If you consider the following two bullet points, you will have a good foundation for your API security to build upon:

- Use an API gateway.
- Use access tokens for authorization.
Let me elaborate on their benefits and show examples of how you can evolve your API security.

## 1. Use an API Gateway
When going live and exposing an API, place an API gateway in front of it. The API gateway then serves as a single entry point to your API (or APIs). As a result, you can use it to enforce common policies. For example, you can ensure that all publicly available endpoints support HTTPS.

HTTPS uses an encrypted communication channel (TLS). However, TLS is not limited to HTTPS. I recommend using TLS for any protocol that runs on TCP. This way, you can encrypt data in transit, protect it from eavesdropping and thus avoid (some) unauthorized access to the data you expose via your API.

HTTPS is scarcely the bare minimum of securing an API. You should also consider implementing [authentication and authorization](https://curity.io/resources/learn/authentication-vs-authorization/). Use a protocol like [OAuth](https://curity.io/resources/learn/oauth-overview/) or [OpenID Connect](https://curity.io/resources/learn/openid-connect-overview/) for that purpose. Both protocols allow you to delegate access to your API with the help of an [access token](https://thenewstack.io/jwts-on-a-journey-sending-jwt-access-tokens-across-apis/) while keeping trust management central.

## 2. Use Access Tokens for Authorization
In practical terms, the access token commonly implies a JSON Web Token (JWT) format. At its core, a JWT is [a signed JSON object](https://curity.io/resources/learn/self-contained-jwts/) that conveys information about an access grant in a verifiable manner. In OAuth, [the authorization server](https://curity.io/product/) is central for processing and communicating that grant. It is the authorization server’s responsibility to add accurate [data to the access token](https://thenewstack.io/the-data-your-access-token-reveals-and-how-to-secure-it/) and sign it.

### Carefully Design JWTs
JWTs are a handy tool for API authorization. They can carry all necessary information for your API and its microservices to apply access rules and grant or deny a request. One thing you should spend time on is sketching out what information your API needs for its rules. This exercise is called [the token design](https://curity.io/resources/learn/scopes-claims-tokens-and-all-the-things-in-between/). As part of designing the token, make sure you use an asymmetric signature algorithm.

Asymmetric signatures provide nonrepudiation, which implies that only one authority, the authorization server, can issue the access token because it is the only authority with access to the required keys. Using asymmetric signatures, you can be sure that the authorization server issued the access token and not any other party. This is how you can build trust in technical terms.

### Validate JWTs
Once you know what to expect from an access token, you are ready to integrate. Use the API gateway for coarse-grained access control. It should reject any request that is obviously malformed, like when it is missing the access token or when it includes an invalid token. An invalid token can also be a token that does not have the [appropriate scope](https://curity.io/resources/learn/scopes-and-how-they-relate-to-claims/) for the request. [JWT security best practices](https://curity.io/resources/learn/jwt-best-practices/) include the following:

- Always validate the access token.
- Specify and check expected values for the following:
- signature algorithm
- issuer (identifier of the authorization server)
- audience (identifier for your API)
- Validate time-based claims, such as:
- expired
- issued at
- not-before
- Do not trust values in JWT header parameters.
Be cautious if you depend on JWT header parameters to load the key material. For example, only load referenced keys of the kid parameter from a trusted source such as a configured URL (JSON Web Key Set URI, jwks_uri) or, alternatively, use discovery mechanisms like OpenID Connect Discovery. As mentioned, the key is essential for building trust, so you must be careful. Once you have validated the syntax of the JWT, you can validate the signature and, if successful, use the claims to process the access rules.

## 3. Avoid Common Risks
With an API gateway and access tokens for authorization, you can avoid common API security risks. For example, among [OWASP top 10](https://curity.io/resources/learn/owasp-top-ten/) you can find the following items:

- Broken object-level authorization (BOLA)
- Broken user authentication (BUA)
- Broken object property-level authorization (BOPLA)
- Unrestricted resource consumption
- Unrestricted access to sensitive business flows
You can configure rate limiting in the API gateway and thus avoid unrestricted resource consumption. In addition, the API gateway can require an access token on all requests by default. In combination with having the API validate the access token on every request and base its access control on the claims within the token, you can avoid both broken object-level authorization and broken object property-level authorization.

With OAuth, the authorization server takes over important and difficult security work. Among other things, it authenticates users, which minimizes broken user authentication due to flaws in proprietary implementations. You can enable [multifactor authentication](https://curity.io/resources/learn/introduction-to-mfa/) at the authorization server to mitigate the risk of unrestricted access to sensitive business flows.

## 4. Evolve API Security
By adding an API gateway and using [OAuth or OpenID Connect to base authorization on access tokens](https://thenewstack.io/supply-chain-attacks-how-to-mitigate-oauth-token-theft/), you can mitigate a bunch of top API security risks. Furthermore, you can evolve your architecture in a scalable manner. For example, implement and combine best practice patterns like the privacy-preserving [phantom token pattern](https://curity.io/resources/learn/phantom-token-pattern/) or [the token handler pattern](https://curity.io/resources/learn/the-token-handler-pattern/) for browser-based applications. All you need to kick off is an API gateway and access tokens for authorization.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)