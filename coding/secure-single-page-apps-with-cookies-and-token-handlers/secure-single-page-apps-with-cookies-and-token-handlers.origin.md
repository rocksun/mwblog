# Secure Single-Page Apps With Cookies and Token Handlers
![Featued image for: Secure Single-Page Apps With Cookies and Token Handlers](https://cdn.thenewstack.io/media/2024/08/48e00c7a-pokerchips-1024x576.jpg)
Single-page applications (SPAs) are rapidly gaining a stronger foothold as an easy-to-develop interface for digital data delivery and customer engagement. Websites with single backends serving HTML and data were once the dominant online interface, but now SPAs with multiple microservices on the backend are becoming more prevalent.

However, SPAs are inherently difficult to secure. Instead of being connected to a single backend server, they are connected to [microservices](https://thenewstack.io/microservices/) via APIs. While this gives SPAs their lightweight advantage, it also creates significant security risks. User authentication must often occur in the browser instead of taking place in a protected server behind a network firewall.

In addition, SPAs typically have a large number of dependencies on third-party data [connected with APIs](https://thenewstack.io/api-management/) to the application. High volumes of third-party connections can create a twofold problem.

First, developers have no control over the security built into APIs created by other practitioners and organizations. Second, programming in this complex and diverse environment can be tedious because of the large amount detailed, customized code and input settings involved. It can be easy to miss an important step and unknowingly create a security gap. Additionally, hidden security risks can be introduced as the environment grows and adapts to shifting business demands over time.

## Website Security Doesn’t Work for Single Page Applications
In securing websites, developers are able to use cookie-based sessions to grant users access to the web application. The frontend website client stores cookies on the browser that are sent to a single backend data server with every user access request. The authorization decisions can be based on the session data kept in storage so user access remains secured behind the network firewall.

This setup isn’t possible for SPAs because a single-page application doesn’t have a dedicated backend. A content delivery network (CDN) often serves the code to the SPA through static files. These files are returned through API calls to the application. In an SPA configuration, the user’s session can’t be kept in a cookie because there is no backend data storage. Instead, [access tokens can be used to call APIs](https://thenewstack.io/jwts-on-a-journey-sending-jwt-access-tokens-across-apis/) on behalf of the authenticated user.

## SPA Security Vulnerabilities
SPA security challenges hinge on the fact that browser-based authentication is vulnerable to a wide range of cyberattack types. One threat type is cross-site scripting (XSS) credential theft. In this attack method, malicious actors inject code capable of stealing [access tokens and user credentials into the browser](https://thenewstack.io/best-practices-for-storing-access-tokens-in-the-browser/) to gain unauthorized access to valuable data and systems.

While XSS is a common vulnerability, it is not the only one that developers must defend against. To make matters even more difficult, fixing one vulnerability often opens up new ones, which makes securing SPAs a never-ending game of shifting objectives. For instance, using OAuth flows to authenticate user or API access with OAuth [tokens instead of session cookies](https://thenewstack.io/how-to-handle-sessions-with-cookies-and-tokens/) seems like a good way to mitigate XSS attacks.

However, if these tokens are stored in local storage, threat actors can easily gain access to local and session storage to exfiltrate tokens. If tokens can be refreshed, the problem is exacerbated because attackers can gain access even after a user session ends.

Another example of unintended issues that can come with a security fix is building strong security policies into content security policy (CSP) headers. While this can add another layer of security control, some sources may be able to open content security policies and disable them.

The bottom line is the browser is a hostile environment when it comes to defending against unauthorized and malicious access to data and systems. Any security measures require careful testing and constant vigilance to ensure closing one attack vector doesn’t open the way for another one.

## Using Both Cookies and Tokens
One way of securing SPAs that has recently been developed for protecting user authentication against malicious actors is a token handler pattern that merges website cookie security and access tokens. By implementing a token handler architecture that removes authentication from the browser and leverages a backend-for-frontend (BFF) configuration using same-site cookies and tokens, organizations are able to benefit from the lightweight aspects of SPAs without sacrificing security.

In this setup, an OAuth agent hosted as a backend component sits between the SPA and the authorization server. The OAuth agent handles the OAuth flow for the SPA and instead of the SPA being issued a token, a secure HTTP-only cookie is issued that the SPA can use to gain access to its backend APIs and microservices.

An OAuth proxy hosted in a high-performance API gateway sits between the SPA and the API and translates the cookie into an access token. In this way, tokens never reach the SPA where they could be exfiltrated by threat actors.

A key advantage of the token handler pattern is it separates API access from website concerns so that organizations can experience the full benefits of SPAs. Using OAuth and OpenID Connect protocols, developers can deploy token components to the API side of the architecture, effectively separating it from the web development end of the environment. In this way, website and application frontend developers and managers can maximize user experiences without backend authorization limitations.

## BFF Architecture Solution
The token handler pattern resolves multiple SPA vulnerabilities by providing a way to lean into the best of website and application security by combining the convenience of sessions and cookies with the strength of access tokens. However, it can be a complex architecture to implement. There are [resources, including design documents](https://curity.io/resources/learn/token-handler-overview/), available that provide in-depth guidance to help developers take advantage of this breakthrough in SPA security.

The token handler pattern makes it possible for organizations to confidently use SPAs without introducing new security vulnerabilities. This architecture is a welcome evolution in protecting SPAs against unauthorized or malicious access. It opens up new possibilities for teams that have been concerned about the security of their SPAs and for companies that have been reluctant to use SPAs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)