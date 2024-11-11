# How Time Plays a Crucial Role in Aggregating Mobile Data
![Featued image for: How Time Plays a Crucial Role in Aggregating Mobile Data](https://cdn.thenewstack.io/media/2024/11/3a3c095b-image2-1024x576.png)
Mobile apps, like the backends they interact with, are a system of computed events. However, this system can be one of outright chaos. Apps run on devices with runtimes that developers don’t have access to, with batteries that last only a few hours, with cracked screens preventing full use of the UI and network connections that can vary in strength merely by the location of the user.

And all of that is before getting into the actual computational limitations of the devices that apps run on, and the fact that the “system” is made up of thousands or millions of users simultaneously doing different things with the app.

These factors might all be occurring at once but with differing levels of visibility for app developers. And because these apps are the basis of many businesses, there must be ways to find meaningful information in the activity from apps. Mobile observability solutions have to solve for a real quantity called “time” at every step in the process, and cobble that data together to reflect a user experience.

A key challenge for mobile observability solutions is recreating high-fidelity user experiences from activity that is distributed across millions of devices, each occurring on its own timeline with its own set of user intentions and hardware limitations.

The limits of [mobile apps](https://thenewstack.io/hard-truths-to-consider-when-designing-slos-for-mobile-apps/) mean making sense of mobile data should start with suspicion:

- Is the data arriving at the backend in the correct order?
- Is the instrumentation all occurring at a native level, or is it abstracted or part of a hybrid framework?
- Have all events been completed within the timeframe we’re looking at, or do I need to wait to make sense of it?
Additionally, there is a higher-order set of questions to consider outside one’s code when aggregating this mobile telemetry. Is “time” relative? Have users completed actions when their sessions end, or do you need to build in flexibility for actions that have many states before they resolve?

Luckily, these questions are functional, not philosophical. In the end, the answers to these questions are solutions that mobile observability vendors use to “bend time” to make sense of mobile-specific data. By learning about some key challenges in collecting mobile telemetry, you can start thinking about how to use that telemetry meaningfully when observing your apps.

## When Will the Mobile Data Get to the Backend?
Mobile observability SDKs typically report mobile events to the backend at the end of a user session. The overarching goal is to keep the SDK’s activity as lightweight as possible; otherwise, receiving a constant stream of events over a network would monopolize the resources of the app that the SDK is observing.

Further, this means that while individual app activity isn’t reported precisely in real time, the thousands or even millions of app sessions are able to be received, processed and aggregated into meaningful metrics as soon as is practical.

Coming into the backend services are highly asynchronous events that must be organized as sessions full of actions. And even the reliability of those events is in question. The connection to send the events might have failed and retried later, or the events might be received from older or jail-broken devices whose timestamps could be skewed a day or two from a canonical clock. These factors need to be reconciled by the backend in real time before displaying the information to mobile engineers.

Further, certain events hit the backend out of order. The user session is usually reported with a single request delivering a single payload, containing important features like [networking results](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/) or [performance traces](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/).

However, alerting logs can arrive in real time as a means of breaking glass for emergencies. Additionally, crashes are only reported when an app is relaunched, as those exceptions follow strict rules set by mobile operating systems, not the developer. To turn these disparate events into a cohesive timeline requires a strategy for encapsulating all this mobile activity.

## Mobile Observability Must Account for Delayed Data
![Mobile data is frequently delayed from when it’s collected on a device to when it’s sent to a server.](https://cdn.thenewstack.io/media/2024/11/9c3206d9-image1-1024x576.png)
Mobile data is frequently delayed from when it’s collected on a device to when it’s sent to a server.

To make this information navigable and useful in a dashboard, mobile observability vendors build systems that look backward and forward. While a user can be understood to use an app in sessions, displaying sessions to developers means synchronizing multiple flavors of activity. Sessions in a dashboard can consist of the network requests and interactions that are reported at the end of sessions. They can also include the real-time logs that came over a separate network connection.

Additionally, user sessions can include traces occurring both [within and between sessions](https://www.cncf.io/blog/2024/06/14/why-embrace-created-span-snapshots-for-mobile-observability-with-opentelemetry/), and crashes that end sessions. Finally, digging into a user’s full experience requires stitching together the sessions for individual users or devices, or layering network requests in a given session over simultaneous traces, even if the information is received out of order. Mobile observability solutions can’t take for granted at any point that a session is simply “done,” as there might be more user activity to add.

## When Should Mobile Engineers Use Key Mobile Telemetry?
User sessions are ultimately a tool developers use to diagnose app issues. However, not all issues are the same, and not all information about sessions needs to be responded to at the same time.

A pervasive networking issue on an older app version might not be significant right now but might be something to diagnose when there’s downtime between releases and you want to ensure there has since been a fix. On the other hand, a crash from a superuser might be something to know immediately so you can prevent it from happening to your most valuable users.

All mobile telemetry is a tool for diagnosis, and understanding that you receive telemetry over time is the first step to making meaningful decisions about how to use it. The key is determining the balance between knowing some information quickly versus having a more robust set of information after a longer time interval.

Real-time alerting should be a canary in a code mine, so to speak, to anticipate and ward off larger potential issues. The data might not show the total number of affected users, but if you wait to count up all those users, you’ll be scrambling with a broken app and unhappy users. What was the point of an early warning in that situation?

However, not all information needs to be responded to in real time. Seeing how a new feature affects session duration means waiting for days, weeks or even months for user activity to be collected. And even with this time window, you wouldn’t want to know performance down to the granularity of real-time information. An aggregate will be sufficient to make measurements and form conclusions against.

Mobile observability vendors must make trade-offs in how they ingest and aggregate different mobile signals. For example, examining app performance for certain key user flows requires a long tail of information that’s bound to change over time. However, telling [mobile teams their new app version crashed](https://thenewstack.io/hard-truths-to-consider-when-designing-slos-for-mobile-apps/) because an unrecognized selector is disturbing their UI rendering is something to advise them about as soon as possible.

Accounting for the time effects of information requires working with multiple granularities. If you need to know about issues right when they start, knowing you’ll have to contend with noisiness and incompleteness, getting that information in five-minute granularities will point you to the problem. If you want to get a fuller picture of app performance, using a one-day granularity will greatly expand the amount of user activity you can incorporate.

Some long events, like sessions or traces that extend across multiple sessions, might get lost in a shortened time interval like five minutes, but would be incredibly meaningful for large-scale reports over periods of days. Conversely, forwarding telemetry every five minutes might create noise given the asynchronous ingestion of data laid out above but could be very helpful for noticing critical failures, like a high crash rate, as soon as that information starts to become available.

Many mobile observability vendors also offer hourly granularity, which can be a sweet spot for observing some aspects of mobile systems, as the hourly bucket can both alert with higher fidelity than the five-minute granularity and aggregate activity within a shorter, more rapid time window than the daily granularity.

## Wrapping Up
Traditionally, crash rates have stood as the mobile developer’s analog to a backend warning or error log. These events are calculable and create numerical measures that can be displayed in a line graph over time. These are certainly helpful for developers. But they don’t provide the whole picture.

The [effect of time on when mobile telemetry can be collected, sent, processed and analyzed](https://thenewstack.io/five-tips-for-designing-highly-effective-mobile-slos/) by mobile teams is a significant challenge when building and observing mobile apps. Engineers should understand the pros and cons of monitoring telemetry through different time granularities because there are trade-offs between data accuracy versus immediate actionability.

Likewise, mobile observability vendors must build their systems to accommodate the strains of delayed and out-of-order data collection in mobile. For example, [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=aggregated-data) solves this problem by modeling the use of real mobile apps — the simultaneous interactions with many different device types, often with many processes occurring on those devices, in many physical and technological conditions.

A user experiences all these while using an app, and so the ability to reproduce their experience is vital to learning whether your app functions correctly, and more importantly, performs well.

If you’re mostly familiar with observing backend systems, you’ll be surprised by how challenging it is to effectively observe the mobile environment. You can learn more about these key differences, and what you need to deliver better user experiences, in [our mobile observability guide](http://get.embrace.io/mobile-observability-guide/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=aggregated-data).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)