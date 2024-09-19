# 3 API Vulnerabilities Developers Accidentally Create
![Featued image for: 3 API Vulnerabilities Developers Accidentally Create](https://cdn.thenewstack.io/media/2024/09/df2bc274-usingapissecurely-1024x683.jpg)
By her own admission, [Katie Paxton-Fear](https://www.linkedin.com/in/katiepf/?originalSubdomain=uk) isn’t the sort of [cybersecurity](https://roadmap.sh/cyber-security) hacker that will lead the keynote at Black Hat or Def Con. But the ethical hacker is exactly the sort of hacker who could exploit your application’s API. And it isn’t even that hard, she acknowledged at last week’s [Kong API Summit 2024](https://thenewstack.io/kong-new-ai-infused-features-for-api-management-dev-tools/).

“Because I used to [make APIs](https://thenewstack.io/sxsw-2017-make-apis-easy-use-web/), I understand how I can break them,” Paxton-Fear told live and virtual audiences. “[API hacking](https://thenewstack.io/lessons-learned-from-hacking-the-tesla-api/) is broadly far more about the logic of how an API works than a specific payload, and developers still make little mistakes, actually lots of little mistakes.”

Mistakes that she can leverage, she shared in her talk, “[Top 4 API Bug Bounty Finds: Avoid Common Mistakes and Vulnerabilities](https://konghq.com/resources/videos/top-4-api-bug-bounty-finds-avoid-common-mistakes-vulnerabilities).”

## The Silliest, Potentially Lethal Bug
![Katie Paxton-Fear gives a talk on why APIs are vulnerable.](https://cdn.thenewstack.io/media/2024/09/0916b73a-apiwhyvulnerable.jpg)
Hacker Katie Paxton-Fear discusses why APIs are vulnerable.

Paxton-Fear demonstrated just how simple and in some cases “silly” these bugs could be. For instance, she’s awarded the “silliest bug” to an API bug on an app for airport systems. The application supports requesting planes to fly overhead, which is typically used for community air shows.

“When I was looking at it, I realized that you would be able to give some information about your local [airport](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/) — again, makes sense,” she said. “Planes need runways. You need information about runways. You need information about airports. How else are you going to actually have planes fly overhead?”

However, the app didn’t require a password. It just used a last name and an email, neither of which are private.

“They’re very public, especially if you work in an industry where you know a lot of networking takes place, you might even have that information on your LinkedIn profile,” she said. “When we were having a look at this and we found a last name and an email address, we realized we could change somebody’s booking for this.”

That may seem like a minor vulnerability on the surface, but it’s not. With no password required, she could have changed things such as the runway length or facilities.

“Now, this is a huge deal because planes need specific runway sizes for a reason, and that’s because they have a stopping distance,” she said. “If the runway is too short, the plane will just keep going.”

She could have changed the landing strip length to state it could accommodate a 747 when it’s actually only designed for small commuter plans, which could have led to damages, crashes and even deaths.

“Even though this is a relatively simple vulnerability, it has a huge impact, and that’s what I mean when I start to say API hacking is far more about the logic of an application,” she said. “This was intentionally designed without a password because they didn’t want to deal with having a password, but that isn’t necessarily the right choice for security.”

## A Quizzical Vulnerability
The second vulnerability she discussed she called quizzical, and it was actually the quickest bug she’d ever found. Paxton-Fear was looking at a mobile app and using an Android emulator on her computer. She was able to insert the traffic that the emulator was sending.

“If you don’t know about [Android development](https://thenewstack.io/scoring-comparison-android-ios-development/), one of the big problems or the big challenges that a lot of developers have to overcome is actually optimizing their access,” she said. “You can’t just make tons of requests on a phone, because every single time you transmit on the phone’s antenna, you are draining the phone of battery.”

“My bugs are about understanding what an application does, how it’s supposed to work, and therefore how to break it. And this is most API hacking.”

— Katie Paxton-Fear, ethical API hacker
Instead, apps use batching to send one request with five sub-requests in it, which saves the phone battery. The server or the API will then unwrap that batched request and turn that into the five requests you ask for, take all of the output and wrap it around again.

“This means we can still use the same API,” she said. “We’re not having to create a mobile-only API. We just need to create this wrapping and unwrapping that we didn’t have before. And this really does help when it comes to [developing mobile apps](https://thenewstack.io/the-role-of-the-database-in-mobile-app-development/), because you can’t just transmit constantly.”

In this case, she tested a simple quiz app that would allow users to take correct answers and turn them into in-game currency, that could be exchanged in real time.

“A lot of you are probably thinking I could do an [API request](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/), get all the questions, get all the answers to all the questions, and generate some free currency, and that’s absolutely what you could do,” she said. “But it wasn’t just for this one quiz question. This is how every single question was set up. So you could go in there, and this is question ID one, but you could change that one to a 2,3,4, it’s your standard RESTful API, you know. And it was really, really easy to turn this into in-game currency.”

Again, she said, it’s about the logic of the application, not about API functionality.

“My bugs are about understanding what an application does, how it’s supposed to work, and therefore how to break it. And this is most API hacking,” she said. “APIs are not typically vulnerable to a lot of attacks, and most [API attacks](https://thenewstack.io/the-economics-of-api-attacks-and-how-developers-can-stop-them/), more broadly, don’t target an API’s fundamental infrastructure. They target the functionality itself.”

## The Undocumented API
API gateways can help to enforce authorization standards, but are not widely used across the industry, she said. However, a lot of APIs are simply undocumented, as if that somehow will protect them, she added.

“A lot of APIs focus more on being undocumented. If you can’t access it, it doesn’t exist,” she said. “Just because something is undocumented doesn’t mean you’re going to get someone like me who goes and pries anyway.”

She’s even seen developers take their JSON and obfuscate it in some ways; obscuring key names, for instance.

“That is still just covering up a problem,” she said. “You really need to sit there and ask, should this really be public.”

[APIs are difficult to test](https://thenewstack.io/reining-in-the-api-wild-west-5-api-testing-best-practices/) automatically, she added, because they are reliant on you being able to understand the logic.
“I’ve seen a lot of people talk about the future of AI for things like hacking, but we’re still missing out on just doing basic automation on APIs because they are so logic-focused and business logic-focused,” she said. “Literally, all of my vulnerabilities are in these two categories: the authentication is missing and there’s some kind of business logic issue with how it’s written that has a security impact.”

She also showed a Laravel routing controller, which allows you to define endpoints, demonstrating the difference between vulnerable code:

![Vulnerable code sample. It has three extra lines that can be exploited.](https://cdn.thenewstack.io/media/2024/09/197d6e83-vulnerable-code-api-.jpg)
Vulnerable code sample from Katie Paxton-Fear’s presentation.

And the not-vulnerable code:

![Invulnerable code from Katie Paxton-Fear's presentation.](https://cdn.thenewstack.io/media/2024/09/ed8629a3-notvulnerable-code-api.jpg)
Invulnerable code from Katie Paxton-Fear’s presentation.

The only difference between the two is three lines of code and that if statement, she noted.

“This is not even a line of code, and this, you can bypass the authentication. As soon as you add [middleware](https://thenewstack.io/middleware-in-the-frontend-tool-helps-manage-webhooks-on-vercel/) into that, you add that authentication,” she advised. “Very often we’re looking at missing if statements. This is a [function called delete](https://thenewstack.io/learn-react-delete-functionality-and-the-set-state-hook/), and it deletes everything in the database, but it’s missing an if statement.”

## The API Problem in a Nutshell
The problem with APIs isn’t so much that they’re hard to secure, but that they are prolific and developers prioritize other tasks to testing and securing APIs, she added. There are literally hundreds and thousands of API endpoints, so it’s not surprising things get missed.

“While you can get a solution that can really help you manage it, if you don’t have the the teamwork and the culture around security, it’s going to fail, just like anything else will.”

— Paxton-Fear
But it’s also an [IT cultural problem](https://thenewstack.io/say-no-to-ship-it-culture-slow-and-steady-wins-the-race/) that creates security problems.

“At the end of the day, any developer is going to value breaking down their product backlog and their sprint backlog more than fixing vulnerabilities, because in the sprint, even in the waterfall model of software engineering, the functionality is on completing features to get a complete product,” Paxton-Fear said. “Fixing bugs isn’t given the same priority. And this is how things get forgotten.”

Instead, there needs to be basic internal reviews where finding vulnerabilities is prioritized. And security can’t be the Department of No, because that ends up in conflict with developers instead of solving security problems. And IT organizations have to stop prioritizing speed over security.

“While you can get a solution that can really help you manage it, if you don’t have the the teamwork and the culture around security, it’s going to fail, just like anything else will,” she said.

Instead, focus on changing the culture and getting developers vested in security. And a simple way to do that effectively is to teach developers how to hack and test their own code, she advised.

“Most developers really like it. They find it fun,” Paxton-Fear said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)