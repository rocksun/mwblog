The open source hardware community is debating Arduino’s [new Terms and Conditions](https://www.arduino.cc/en/terms-conditions/) following the company’s acquisition by Qualcomm.

[![Arduino_Uno_-_R3 - Creative Commons via Wikipedia - by SparkFun Electronics from Boulder, USA](https://cdn.thenewstack.io/media/2025/12/20d64af2-arduino_uno_-_r3-creative-commons-via-wikipedia-by-sparkfun-electronics-from-boulder-usa-150x150.jpg)](https://cdn.thenewstack.io/media/2025/12/20d64af2-arduino_uno_-_r3-creative-commons-via-wikipedia-by-sparkfun-electronics-from-boulder-usa-150x150.jpg)

Arduino microcontroller board

Chief microcontroller rival Adafruit has argued that the new terms threaten open principles by restricting reverse engineering of cloud tools, asserting perpetual licenses over user uploads and implementing broad monitoring for AI-related features.

Arduino has defended the changes, claiming restrictions only apply to its [SaaS cloud applications](https://thenewstack.io/cloud-services/), that data handling is standard for modern platforms, and its commitment to open source hardware remains unchanged.

## The Debate Over Arduino’s New Terms and Conditions

Last week, I spoke to Arduino, Adafruit and the EFF about Qualcomm’s [October acquisition](https://thenewstack.io/can-arduino-teach-a-tech-giant-how-to-win-over-developers/) of the beloved company known for its [single-board microcontroller kits](https://youtu.be/QxPBCBX8ac8).

Many criticisms came from rival Adafruit, whose products include Arduino-compatible hardware kits. In late November, Adafruit’s Managing Editor [Phillip Torrone](https://github.com/ptorrone) had [warned its 36,000+ followers on LinkedIn](https://www.linkedin.com/posts/adafruit_opensource-privacy-techpolicy-activity-7396903362237054976-r14H/) that (among other things) Arduino’s users were now “explicitly forbidden from reverse engineering or even attempting to understand how the platform works unless Arduino gives permission.”

But Arduino [responded in a blog post](https://blog.arduino.cc/2025/11/21/the-arduino-terms-of-service-and-privacy-policy-update-setting-the-record-straight/) that “Restrictions on reverse engineering apply specifically to our Software-as-a-Service cloud applications. Anything that was open, stays open.”

An Arduino spokesperson said their blog post reassured many readers, who’d said they felt “understanding and relief that our commitment to the [open source spirit](https://thenewstack.io/open-source/) is unwavering and Arduino’s core mission remains unchanged.” Yet Adafruit’s critical LinkedIn post had drawn over 1,575 upvotes. I asked both sides to clarify their positions. Does this really represent a turning point since Arduino’s founding in 2004?

Here’s what they had to say.

## Reverse Engineering: Cloud Apps vs. Hardware Boards

I asked [Mitch Stoltz](https://www.linkedin.com/in/mitch-stoltz-90283ab/), EFF director for competition and IP litigation, who agreed that Arduino “isn’t imposing any new bans on tinkering with or reverse engineering Arduino boards.”

Like Adafruit, Arduino’s primary user base is at-home enthusiasts. Arduino provides an open source electronics platform — which includes single-board microcontrollers such as the [Arduino UNO](https://www.arduino.cc/product-uno-q) — and various kits/shields/accessories, as well as development software.

[![Limor_Fried_TC2013 (Creative Commons via Wikipedia) - by TechCrunch from TechCrunch Disrupt NY 2013 Day Three](https://cdn.thenewstack.io/media/2025/12/085e125a-limor_fried_tc2013-creative-commons-via-wikipedia-by-techcrunch-from-techcrunch-disrupt-ny-2013-day-three-207x300.jpg)](https://cdn.thenewstack.io/media/2025/12/085e125a-limor_fried_tc2013-creative-commons-via-wikipedia-by-techcrunch-from-techcrunch-disrupt-ny-2013-day-three-207x300.jpg)

Limor Fried (Wikipedia)

Nonetheless, Adafruit founder [Limor “Ladyada” Fried](https://www.linkedin.com/in/ladyada/) says Arduino’s response “downplays how central the cloud and web tools have become to the Arduino experience.”

“If you go to the Arduino software page and the cloud page, you’re strongly encouraged to use the cloud editor/web IDE and cloud plans, especially on platforms like ChromeOS where the [cloud editor](https://cloud.arduino.cc/) is the recommended or only realistic path,” Fried said. “So when Arduino says ‘These restrictions only apply to SaaS,’ that still means the restrictions apply to the tools many new users are being steered into as their primary Arduino environment.

“On top of that, using those cloud tools generally requires an Arduino account, and the signup flow prominently presents marketing and profiling consents, including consent to processing personal data for commercial offers and to profiling for customized offers.

[![Adafruit's LadaAda shares screenshot of Arduino signup - ag1Ca7zTnZDHZ4dS](https://cdn.thenewstack.io/media/2025/12/c2f26d6f-adafruits-ladaada-shares-screenshot-of-arduino-signup-ag1ca7ztnzdhz4ds.png)](https://cdn.thenewstack.io/media/2025/12/c2f26d6f-adafruits-ladaada-shares-screenshot-of-arduino-signup-ag1ca7ztnzdhz4ds.png)

“That is a very different model than ‘download a local IDE and just start hacking on hardware,'” Fried said.

“Even if the underlying firmware and libraries remain open source, the practical entry point for many users is moving”, she pointed out, in that accounts are tied to personal data, marketing and profiling prompts have been introduced, and are being linked to centralized, subscription-oriented cloud services.

## Understanding the License on User-Uploaded Content

[![](https://cdn.thenewstack.io/media/2025/12/2d396bc0-1685947-300x300.jpg)](https://cdn.thenewstack.io/media/2025/12/2d396bc0-1685947-300x300.jpg)

Phillip Tororne

Adafruit’s Torrone had also said Arduino’s new documents “introduce an irrevocable, perpetual license over anything users upload.”

But Arduino argues they’re instead clarifying that “content you choose to publish on the Arduino platform remains yours, and can be used to enable features you’ve requested, such as cloud services and collaboration tools.”

In a follow-up interview, an Arduino spokesperson provided clarifying examples:

* “If a user uploads their code sketches on their Arduino Cloud subscription, the content remains their own, private to them, and the licensing rights granted to Arduino are strictly functional to perform the requested features (e.g. compiling the sketch in the cloud).”
* “If the user uploads code or content to Project Hub or to the Forum, where the content is visible to all other users, then Arduino requires the user, who retains the ownership of the content, to grant a license to handle the publication.”

“[W]ithout this license, we could not run user projects on the cloud or display their posts in the forum, which is why this type of license is typically required to run any modern cloud service or social platform.”

Arduino’s old terms of use had also required a license for using material posted, notes EFF’s Stoltz, which he says is “normal for any online platform.”

But then Stoltz adds that “Still, some of the changes to the terms are troubling.”

Arduino’s old terms “were unusual in giving users the ability to revoke that license at any time. The new terms remove that ability, making the license irrevocable. It’s disappointing to see a platform that was once especially user-protective revert to the norm.”

## User Data and the Right To Delete Accounts

Arduino also pointed out an additional privacy protection. “All users retain the right to request deletion of their account and/or content at any time. Upon such deletion, the relevant content will no longer be visible to other users.”

Torrone had complained of “years-long retention of usernames even after account deletion,” but Arduino calls that “a misunderstanding of our policy … When a user requests account deletion, we immediately delete the account and remove the user’s username from all associated Forum posts.

“The five-year public retention of usernames applies only to users who simply have not logged into their Arduino user account for 24 months *and* have not submitted any data or account deletion requests.” (In those cases, Arduino seeks a status where “contributions remain attributed to inactive usernames, honoring their contribution to the community.”)

So, for those inactive-for-two-years users, accounts are automatically deactivated, Arduino’s blog post clarified, but with usernames preserved in the Arduino Forum “to address an explicit request from the Forum community to maintain attribution for user-generated content.” (And where a user does request account deletion, “the username would be promptly removed and related posts would become anonymous.”)

Even then, with those inactive accounts, “After five years the username is deleted,” Arduino’s spokesperson explained, “and relevant user posts or comments are de-identified.

“This policy is not meant for data retention for commercial use, but instead solely to help preserve content attribution, something the community has emphasized as valuable.”

But Adafruit’s Fried still says there’s a troubling pattern in how usernames are retained and not deleted. “Policy choices that treat the community’s identity and data as a managed asset, rather than something users can fully control.”

## AI Features and User Monitoring Policies on Arduino

The culture difference is most clear where the new Terms and Conditions list several “prohibited uses of AI,” which include criminal use and violation of the law, intentions to harm (including dissemination of false information and manipulative or deceptive acts), generating facial recognition databases and [military use](https://news.ycombinator.com/item?id=46013385).

Arduino’s blog post notes its new AI features are optional — including AI-powered [computer vision and audio models](https://www.arduino.cc/en/uno-q/) and an [IDE with pre-trained AI models](https://docs.arduino.cc/software/app-lab/). But in the new Terms and Conditions, Arduino “reserves the right to monitor User accounts and use of the AI Product … [for] verifying compliance with laws and this policy.”

Arduino says the monitoring is “to comply with existing laws and regulations, including applicable privacy laws, export controls, and other global regulatory requirements” and “verify compliance with legal and policy standards.” And they add their ultimate goal is “protecting the users and Arduino” and to enable “robust and reliable operation of the AI products.”

But their conditions also include the right to monitor for other reasons, including “administering and managing Arduino’s business.”

Adafruit’s Fried says Arduino “should, of course, comply with applicable laws and respond appropriately to clear evidence of criminal activity.” But “they should design their AI and cloud offerings so that monitoring is narrowly targeted, proportionate, and clearly explained, instead of defaulting to broad surveillance across all users.”

> “You cannot say ‘this code is open source, but it may not be used for military purposes’ and still call the license open source.”
>
> **— Adafruit Founder Limor Fried**

Fried instead sees “an ongoing surveillance posture, not just responding to specific, well-founded reports of abuse.”

So yes, an open source application can watch for the creation of facial-recognition databases or military use “as long as they are transparent about what they log, how long they keep it, and under what circumstances they review it.” But there are concerns about “broad continuous monitoring erodes user trust, especially in an educational/maker context where many people are minors or hobbyists who expect a relatively private environment.”

And there’s an even larger issue of principle. “Genuine open source licenses [do not allow field-of-use restrictions](https://www.gnu.org/licenses/gpl-faq.en.html?utm_source=chatgpt.com#NoMilitary),” Fried said. “You cannot say ‘this code is open source, but it may not be used for military purposes’ and still call the license open source.

Once you present something as open source, you no longer get to pick and choose ‘good’ versus ‘bad’ users.” Fried calls such restrictions “fundamentally incompatible with [open source licensing](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/ "open source licensing"),” and would like to see Arduino remove them. “If a project wants that kind of control, it should be honest and call itself ‘source-available’ or something similar, not open source.”

Torrone noted that Arduino’s Terms and Conditions also state users will undertake not to use Arduino’s platform or services “to identify or provide evidence to support any potential patent infringement claim against Arduino … or any of Arduino’s or Arduino’s Affiliates’ suppliers and/or direct or indirect customers.” But the specifics almost seem beside the point. Fried says Arduino’s usage restrictions “effectively override the freedoms the license is supposed to guarantee.”

## What’s Next for Arduino and the Open Source Community?

“Transparency and open dialogue are fundamental to the Arduino ethos,” its spokesperson said Friday, “and understanding the community’s concerns, we are eager to set the record straight and reaffirm our commitment to the open source community.”

The representative also added that “We are committed to continuing to listen to community feedback.”

So what will Adafruit do next? Fried said Friday that Adafruit isn’t changing, and would “keep designing and shipping open source hardware, with hardware, firmware, and software available so people can learn from it, modify it, and build on it.” And the company supports “multiple” ecosystems, also continuing work on Wi-Fi/Bluetooth low-energy (BLE) chips, matter-based Internet of Things (IoT), and the Linux Foundation’s real-time OS [Zephyr](https://www.zephyrproject.org/).

“We are always open to working with other makers and companies, including Arduino, as long as the collaboration allows us to ship great products with strong documentation and truly open source licensing.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)