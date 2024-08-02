# Google and the Future of Online Privacy: Moving Beyond Third-Party Cookies
![Featued image for: Google and the Future of Online Privacy: Moving Beyond Third-Party Cookies](https://cdn.thenewstack.io/media/2024/07/fab213e0-chocolate-2599637_1280-1024x682.jpg)
**Update**: I liked how this article turned out and was pleased that I was able to cover the impending demise of third-party cookies from different angles. Fate had other things in store, though – a few days after writing this, Google [reversed its decision](https://apnews.com/article/google-privacy-chrome-cookies-browser-bffdd0ca0af9ba7a94e95c2c7a11e4d2) to end third-party cookies (for now).
*As I was cursing my luck and thinking of alternate timelines, the Marvel series “What If…?” came to mind. This series covers what would happen if Peggy Carter became Captain America, or if Doctor Strange turned evil, or if the Avengers were attacked by zombies, and so on.*
*I now humbly segue and present you with: “What If…Developers Had to Navigate a World Without Cookies?”*
In the early days of the web, if you changed a setting on a website or placed something in your shopping cart, refreshing the page would mean starting all over again. Websites treated every visitor like a stranger. To create [more personalized online experiences](https://thenewstack.io/dynamic-data-capture-sets-the-stage-for-extreme-personalization/) based on past sessions, Netscape[ created browser cookies](https://montulli.blogspot.com/2013/05/the-reasoning-behind-web-cookies.html), which saved the user’s preferences and browsing history on their device. Other browsers quickly adopted this helpful functionality.

While Netscape’s introduction of first-party cookies aimed to improve the user experience by remembering preferences and settings, advertisers soon began to implement third-party cookies to track users’ internet activity and target them with ads based on previous websites they had visited. Over the years, first-party cookies have been used for authentication and logging in to websites, while third-party cookies have been used and abused for targeted advertising, tracking users across websites, data collection, and other types of surveillance.

For these privacy reasons, [Google](https://cloud.google.com/?utm_content=inline+mention) planned to follow in the footsteps of Mozilla and Apple, which already block third-party cookies in[ Firefox](https://venturebeat.com/business/firefox-enhanced-tracking-protection-blocks-third-party-cookies-by-default/) and[ Safari](https://www.zdnet.com/article/apple-blocks-third-party-cookies-in-safari/), respectively, and[ deprecate third-party cookies by default in Chrome and Chromium-based browsers ](https://developers.google.com/privacy-sandbox/3pcd)in 2025. Google has already restricted third-party cookies by default for[ 1% of Chrome users](https://developers.google.com/privacy-sandbox/3pcd/prepare/prepare-for-phaseout). The company has since [pulled back on these plans](https://www.axios.com/2024/07/22/google-chrome-keeps-cookie-policy).

While the end of third-party cookies has its benefits, the proof will be in the pudding — as with any significant change, the end of third-party cookies raises many questions. Regardless of how you feel about the end of third-party cookies, you must think through what the change means for your apps and projects. Some use cases will not be possible when third-party cookies disappear, and you’ll need solutions.

**Balancing Privacy and Personalization**
Google says privacy is the main driver behind its plan to stop supporting third-party cookies in Chrome. Without third-party cookies, personalized remarketing simply can’t be done.

If the end of third-party cookies works as advertised, I look forward to not seeing intrusive popups, not being tracked as an individual online, and not being served ads that I don’t want to see. However, given that Google and many others rely on third-party cookies to make billions of dollars, third-party cookies won’t disappear without being replaced.

While phasing out third-party cookies, Google is simultaneously investing in[ Privacy Sandbox](https://privacysandbox.com/), which aims to offer privacy-preserving alternatives to anyone who needs to serve content and ads for their businesses. The Privacy Sandbox APIs will let Chrome and any other browser that adopts them act locally on their device’s behalf to protect the user’s identifying information as they browse. For example, the[ Topics API](https://developers.google.com/privacy-sandbox/relevance/topics) enables interest-based advertising without tracking the sites an individual user visits.

As Privacy Sandbox continues to gain traction, developers will have a new set of web standards to adhere to when creating apps and websites. These standards will ensure privacy while also maintaining a level of personalization.

**Setting a New Standard for User Security**
For decades, cookies have allowed developers to adopt subpar security practices for user authentication and tracking. Third-party cookies were available, and they could store user authentication information and details. However, since these were third-party cookies, nobody had any control over who could use or access the data within.

The potential end of third-party cookies will result in security improvements, requiring developers to rethink their previous methods and adopt new ways to handle user authentication and identifying information securely. Think of third-party cookie elimination as a forcing function for storing that information more securely, such as with HTTPOnly and Secure Cookies.

If you rely on third-party cookies, you’ll need to find privacy-preserving ways of authentication and identification. One potential solution is the[ FedCM API](https://developer.mozilla.org/en-US/docs/Web/API/FedCM_API), designed to let identity providers make identity federation services available on the web without needing third-party cookies and redirects. The FedCM API enables federated authentication for activities such as signing up or signing in.

**Redefining the Developer Experience**
The end of third-party cookies is an opportunity to fix the mistakes or bad practices you may have followed while building your apps and websites years ago. This should help make your apps and websites more private and secure, but it’s also a chance to reflect on how much control you really need over every aspect of your app or site.

As we move into a cookie-less world, how much time do you want to dedicate to keeping up with these changes? You may want to[ outsource some of this work](https://www.informationweek.com/software-services/applying-the-socratic-method-to-build-versus-buy) so that you don’t have to be an expert on all things cookies and can instead have a dedicated tool that keeps track of every change and update.

Perform a thorough audit to see where your applications and websites use third-party cookies and develop solutions for those scenarios. For each process that uses third-party cookies that you built yourself, devise a game plan for whether you will continue building or employ a third-party provider.

One solution is to reduce third-party cookie use and employ other mechanisms like session IDs in areas such as authentication, where reduction is impossible. I suspect many developers will shift from third-party cookies to first-party cookies, which might drive other implementation changes, like using custom domains or profile databases. If you already use a provider to handle third-party cookies, check if they support moving to first-party cookies.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)