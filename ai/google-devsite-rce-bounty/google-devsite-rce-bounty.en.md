**Google took two months to patch an unauthenticated RCE vulnerability** in its developer documentation infrastructure. The problem was a reused OAuth client secret, which DevSite stored in a Flask session cookie and also used to sign sessions. Anyone who recovered the secret could forge a valid cookie and execute Python code on the server.

[Simon Köck](https://www.linkedin.com/in/simonkoeck/), a software engineer at Otark GmbH, [discovered the flaw](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce) in Google’s [DevSite](https://developers.google.com/) infrastructure, the shared platform behind developers.google.com and several sibling documentation sites. Köck tells *The New Stack* that forged sessions were accepted on all seven affected domains, which relied on two different signing keys, and that he ran his code-execution proof on three of them, developers.google.com, docs.partner.android.com and web.dev.

> Köck tells *The New Stack* that forged sessions were accepted on all seven affected domains, which relied on two different signing keys, and that he ran his code-execution proof on three of them

Google rated the vulnerability S0, the top of its severity scale, and [awarded Köck a $90,000 bounty](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce). That figure reflects a $75,000 base payout for an S0 RCE in what Google classifies as a normal application tier, multiplied by 1.2 for exceptional report quality.

Köck confirmed unauthenticated RCE with a Python sleep payload, measuring response delays that matched his payload, and deliberately stopped short of running commands or touching files, credentials, or internal services. “I’d call it an exceptionally serious RCE because anyone could reach it without an account or victim interaction,” he tells *The New Stack*, adding that he doesn’t know whether the three hosts he tested shared the same backend machines.

> “I’d call it an exceptionally serious RCE because anyone could reach it without an account or victim interaction,”

The more consequential unknown sits behind the server itself. Köck tells *The New Stack*, [Arvin Shivram](https://brutecat.com/about), a Singapore-based researcher who goes by @brutecat and has reported more than 130 Google vulnerabilities by his own count, has since pointed out that internal App Engine apps often have access to Stubby, Google’s internal service-to-service communication system. Köck acknowledges that access “could be a major part of the impact,” though he says he didn’t verify what this particular DevSite process could reach.

One concern is whether an attacker could have modified Google’s developer documentation, replacing installation commands or download links with malicious ones. That could have enabled a [supply-chain attack](https://thenewstack.io/attackers-up-their-game-with-latest-npm-package-compromise/), but Köck didn’t test for write access to the content systems, and Google hasn’t disclosed DevSite’s process permissions or backend access.

The exposed key also let Köck forge DevSite sessions, though he stopped short of checking whether those sessions could impersonate users or reach anyone’s data. By his own accounting, the demonstrated impact amounts to code execution on three hosts and accepted forged sessions on seven, while the full blast radius, including any path into Google’s internal services, remains unproven.

## One OAuth secret, two jobs

DevSite stored a serialized OAuth2WebServerFlow object from Google’s oauth2client library, which Google has [deprecated in favor of google-auth](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html), inside a Flask session cookie, [exposing the OAuth client secret](https://thenewstack.io/best-practices-for-storing-access-tokens-in-the-browser/) in the process. Google had also reused that same [OAuth client secret](https://thenewstack.io/the-different-token-types-and-formats-explained/) as DevSite’s [Flask session-signing key](https://flask.palletsprojects.com/en/stable/quickstart/#sessions), which Köck confirmed by reproducing the cookie’s signature offline, giving him the ability to forge sessions the server would accept.

## Pickle turns forgery into RCE

The OAuth callback used [Python’s pickle](https://docs.python.org/3/library/pickle.html) to deserialize session data, so Köck swapped the flow object for a malicious pickle payload, signed the forged cookie and let the callback execute it. The chain depended on three mistakes lining up, a secret exposed in the cookie, that same secret doing double duty as a signing key, and unsafe deserialization of session data, and fixing any one of them would have broken it.

> The chain depended on three mistakes lining up, a secret exposed in the cookie, that same secret doing double duty as a signing key, and unsafe deserialization of session data, and fixing any one of them would have broken it.

## Patch pace raises questions

Köck reported the vulnerability on August 6, and Google accepted it the following day. The company approved the bounty on August 27 but [didn’t deploy a fix until October 7](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce).

Google hasn’t explained the two-month remediation window or whether it implemented interim mitigations, and questions also remain about the fix itself. Köck’s account of two separate signing keys explains why his recommendations mention two exposed OAuth client secrets, but Google hasn’t confirmed whether both were rotated or whether existing sessions were invalidated.

Köck tells *The New Stack*, he was never given a forensic conclusion and doesn’t know whether Google found evidence of exploitation before the patch, and the company hasn’t said either. Google had not responded to a request for comment as of this update.

*An earlier version of this story said a single signing secret worked across all seven affected domains. Köck says the domains used two different signing keys. This story has also been updated with comment from Köck.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)