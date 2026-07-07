“Sign in with Google” and “Continue with Apple” have carried federated login for more than a decade. They strip away onboarding friction, kill password fatigue, and turn anonymous traffic into accounts, which is why they sit on nearly every consumer signup page. The machinery underneath them is the problem.

Those buttons run on third-party cookies. The legacy social login flow relies on the exact cross-domain mechanism that privacy regulators have spent years trying to shut down.

> “The legacy social login flow relies on the exact cross-domain mechanism that privacy regulators have spent years trying to shut down.”

Safari has blocked third-party cookies by default since 2020 (Intelligent Tracking Prevention) and Firefox since 2019 (Enhanced Tracking Protection), which already puts roughly half the web in a cookieless state.

Chrome is the messier story: Google walked back [its forced deprecation](https://thenewstack.io/google-and-the-future-of-online-privacy-moving-beyond-third-party-cookies/) in 2024 and moved to a user-choice model instead of flipping a switch, so the “cookie-pocalypse” deadline everyone built roadmaps around never actually arrived. Do not read that as a reprieve. Two major engines are blocked by default; Chrome’s Incognito is blocked by default; ad blockers and consent fatigue keep climbing; and the cookie is eroding by attrition, whether or not anyone announces a death date. Any login flow built on it is on borrowed time.

FedCM (Federated Credential Management) is the standard built to keep federated login working once that mechanism is gone. The W3C and the major browser engines developed it as a browser-native API that runs federated identity flows without cross-site tracking.

## How it actually works

The shift is architectural. In a legacy flow, clicking a social button fires hidden iframes, redirects, or pop-ups so the identity provider can read its own cookies and confirm who you are. That same channel lets the IdP track you across the web. FedCM puts the browser in the middle as a trusted mediator.

The site asks for an identity token through one explicit API call, `navigator.credentials.get()`, and the browser runs the rest:

1. The site requests an identity token from the browser.
2. The browser fetches account details from a config file hosted by the IdP, kept siloed from the site making the request.
3. The browser shows a native sign-in prompt instead of a pop-up.
4. On explicit user consent, the browser passes a token back to the site’s backend to create a session.

Authentication and passive tracking get decoupled. (More on the API: the FedCM spec and MDN docs.)

It also fixes the NASCAR problem. Years of bolting on every available social login produced signup pages plastered with competing brand buttons, the registration equivalent of a stock car covered in sponsor decals. That is [cognitive load](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/), and cognitive load costs conversions.

> “FedCM skips the wall of buttons and surfaces the right account in a single native prompt.”

Because the browser already knows which provider you used last, FedCM skips the wall of buttons and surfaces the right account in a single native prompt.

## Legacy flow vs. FedCM

|  | **Legacy federated flow** | **FedCM** |
| --- | --- | --- |
| Mechanism | Hidden iframes, redirects, pop-ups | One browser-mediated API call |
| Privacy model | Depends on third-party cookies | No third-party cookies; explicit per-sign-in consent |
| User experience | Redirect chains, blocked pop-ups, the NASCAR button wall | One-tap native browser prompt |
| Security | Phishable redirect surfaces | Browser-isolated prompt the page can’t spoof |

The practical payoff is conversion. Every extra click and every interrupted redirect sheds a percentage of the people trying to sign up, and mobile browsers frequently block the secondary windows legacy flows depend on. A single native prompt removes that drop-off.

> “Every extra click and every interrupted redirect sheds a percentage of the people trying to sign up, and mobile browsers frequently block the secondary windows legacy flows depend on.”

There is a maintenance angle, too: a standardized browser UI means your team stops building and babysitting bespoke login components, and the flow upgrades through browser releases rather than refactors.

## What this looks like in production

Axel Springer runs FedCM on Ory across hundreds of millions of users. Thomas Bergemann, its General Director of Product & Revenue, put the result plainly: **“**We see an over 15x increase in registrations.” ([Read the case study](https://www.ory.com/case-studies/axel-springer).)

Google’s own testing on browser-mediated sign-in shows the same shape of result: dropping the jarring secondary-window step, the one mobile devices routinely block, cuts user drop-off.

Shopify moved onto browser-mediated identity ahead of the cookie changes and held checkout conversion stable on strict, privacy-centric mobile browsers, the exact environments where legacy flows quietly fail.

## Getting started with Ory

**Step 1: Put the backend behind a CIAM platform.** Don’t hand-roll this. [Ory Kratos](https://www.ory.com/kratos) processes the backend side of FedCM natively, turning browser-side identity assertions into secure user sessions. (See the [Ory FedCM deployment docs](https://www.ory.com/docs/kratos/social-signin/fedcm).)

**Step 2: Configure your social sign-in providers.** In the Ory Console, open the Social Sign-In panel, select your IdP, and enter its FedCM Config URL. Back-channel trust verification is handled for you.

**Step 3: Embed the JavaScript trigger.** Drop a lightweight snippet on your login page to detect support and fall back cleanly when it isn’t there:

```

if ('IdentityCredential' in window) {
  navigator.credentials.get({
    identity: {
      providers: [{
        configURL: 'https://auth.your-business.com/self-service/methods/oidc/fedcm/google',
        clientId: 'YOUR_CLIENT_ID',
      }]
    }
  }).then((credential) => {
    return fetch('/self-service/methods/oidc/fedcm/login', {
      method: 'POST',
      body: JSON.stringify({ token: credential.token })
    });
  }).catch((err) => {
    console.error('FedCM flow interrupted, fallback to traditional OIDC:', err);
  });
}

```

If the browser doesn’t support FedCM, the flow falls back to a standard OpenID Connect redirect, so nobody gets locked out mid-migration. Want to test before you wire up a real IdP? There’s a [free MockFedCM site](https://mockfedcm.com/) for that.

## Where this leaves you

Federated login is moving into the browser, and the privacy model is moving with it. Safari and Firefox already block by default; Chrome is leaking the cookie out the side rather than killing it outright. Neither path leaves your social logins where they were.

The teams auditing their [auth stack](https://thenewstack.io/you-can-build-authentication-in-house-but-should-you/) now are the ones who won’t be debugging broken login loops on someone else’s timeline later. Better to make this move on your own schedule than on the browser’s.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/1aff35a5-cropped-25826b9b-jeff_hickman_headshot-600x600.jpg)

Jeff Hickman is a customer engineering leader with more than 15 years in enterprise identity and cybersecurity. With software engineering roots and Fortune 500 implementation experience, he delivers executive insights on transforming security challenges into competitive advantages. https://www.ory.com/authors/jeff-hickman

Read more from Jeff Hickman](https://thenewstack.io/author/jeff-hickman/)