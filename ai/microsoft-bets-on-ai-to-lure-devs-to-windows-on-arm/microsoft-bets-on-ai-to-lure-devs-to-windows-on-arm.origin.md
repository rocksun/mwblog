# Microsoft Bets on AI to Lure Devs to Windows on Arm
![Featued image for: Microsoft Bets on AI to Lure Devs to Windows on Arm](https://cdn.thenewstack.io/media/2024/06/b17172cf-joel-overbeck-amkdlzfdmia-unsplash-1-1024x683.jpg)
Could [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)’s AI-infused [Copilot+ PC](https://thenewstack.io/copilot-pcs-understanding-microsofts-evolving-ai-pc-stack/) platform, which supports Windows-based [Arm devices](https://thenewstack.io/arm-pushes-ai-into-the-smallest-iot-devices-with-cortex-m52-chip/), be the “[killer app](https://thenewstack.io/tomorrows-5g-killer-apps-will-need-a-strong-foundation-in-ci-cd/)” that lures developers to Windows on Arm?

Perhaps. Though some say it may be just a party trick or shiny object to make more developers look in Microsoft’s direction. Indeed, Microsoft and its PC partners have been trying to attract developers – and customers in general – to [Windows on Arm for more than a decade](https://www.directionsonmicrosoft.com/blog/will-windows-on-arm-pcs-finally-be-worth-buying/).

Maybe a better way to look at the situation is a variation of the “[Field of Dreams](https://en.wikipedia.org/wiki/Field_of_Dreams)” theme. If Microsoft builds it, will they come? Well, Microsoft built it. Now, will developers come?

“It’s a tricky trap to be in … you can’t get all the apps converted to Arm if there aren’t lots of customers demanding it, and you can’t get customers if the machine won’t run the apps they need,” [Richard Campbell](https://www.linkedin.com/in/richjcampbell/?originalSubdomain=ca), a longtime Microsoft MVP, told The New Stack. added.

“I think the Copilot play is a workaround,” Campbell added. “Microsoft has tried to sell Windows on Arm before, and it hasn’t gone particularly well. So perhaps Copilot is the secret to making a successful Arm product?”

In fairness, there are more and more native Windows on Arm apps now available. But are there enough to convince developers this is a good platform? That is not yet clear.

## Copilot+ and SoCs
Microsoft introduced Copilot+ at its [Build developer conference](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/) last month, and the PCs became available this month from Microsoft and partners including Acer, ASUS, [Dell](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention), HP, Lenovo and Samsung, starting at $1,000 a pop.

The Windows on Arm devices run on Qualcomm’s latest Snapdragon X series of processors. The Snapdragon X is a family of systems-on-chip (SoC) that delivers strong CPU performance, on-device AI inferencing and more. The Snapdragon X Elite is an ARM64 SoC. Moreover Copilot+ PCs feature [neural processing units (NPUs)](https://thenewstack.io/qualcomm-amd-add-fuel-to-the-ai-pc-engine/) capable of delivering more than 40 trillion operations per second (TOPS) of compute. The new class of PCs is up to 20 times more powerful and up to 100 times as efficient for running AI workloads compared to traditional PCs, the company said.

Admittedly, the new Snapdragon SoC is impressive, partly because its NPU has such high performance. So the various Copilots should run brilliantly on that hardware. Plus. the promise of long battery life is also a draw, Campbell said.

[Rockford Lhotka](https://www.linkedin.com/in/rockfordlhotka/), vice president of strategy at [Xebia](https://xebia.com/) and another longtime Microsoft MVP, says he is cautiously optimistic about the new hardware and OS capabilities but wants to give it a try. “I am very excited to see if the battery life claims are true in the real world. I love my Surface devices, but battery life has always been a serious challenge,” he said.
## Big Potential
However, some Microsoft developers see potential for Copilot+ and the AI use case.

“AI can be a killer Windows on Arm app, driving both adoption and developer interest,” said [Vasil Buraliev](https://www.linkedin.com/in/vasbu/?originalSubdomain=mk), a project manager and software development consultant at VBU Consulting. “The combination of performance benefits, native optimization and strategic ecosystem development could position Windows on Arm as a leading platform for AI innovation.”

Moreover, he noted that Microsoft has “consistently demonstrated its ability to reach the pinnacle of any strategic initiative it undertakes, whether it takes one, five or 10 years,” he said.

## Copilot Runtime
Microsoft brought its Copilot stack to Windows with the [Windows Copilot Runtime](https://learn.microsoft.com/en-us/windows/ai/overview) to infuse AI into every layer of Windows. The Windows Copilot Runtime includes the Windows Copilot Library, a set of APIs powered by more than 40 on-device AI models that ship with Windows. It also includes [AI frameworks](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/) and toolchains to help developers bring their own on-device models to Windows, Microsoft said.

## Recall Recalled?
In addition, the company introduced the Windows Semantic Index, a new OS capability that supercharges search on Windows and powers new experiences such as the new [Recall](https://learn.microsoft.com/en-us/windows/ai/apis/recall) feature. “With Recall, in preview starting June 18, you can access virtually what you have seen or done on your PC in a way that feels like having photographic memory,” said [Yusuf Mehdi](https://www.linkedin.com/in/yusufmehdi/), Microsoft’s executive vice president and consumer chief marketing officer, in a [blog post](https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/).

However, Recall has run into a snag and has been delayed. The Recall preview release will occur “in the coming weeks,” [Pavan Davuluri](https://www.linkedin.com/in/pavand/), corporate vice president of Windows + devices at Microsoft said in a [blog post](https://blogs.windows.com/windowsexperience/2024/06/07/update-on-the-recall-preview-feature-for-copilot-pcs/).

“Today, we are sharing an update on the Recall (preview) feature for Copilot+ PCs, including more information on the set-up experience, privacy controls and additional details on our approach to security,” his post said.

## Attractive Black Eye?
The Recall episode is a black eye for Microsoft, because the company highlighted it at the launch. They wanted Recall to be the showcase app for these Copilot+/Windows on Arm PCs, but now it’s scaring some people off, analysts indicated.

However, the promise of the Recall feature remains attractive to developers.

“In terms of the AI and NPU, if Windows can reliably search, find and summarize my content across the local device and OneDrive, that would be a game changer,” Lhotka said.

## Rocky Start
Indeed, while the on-chip AI acceleration trend is in play across the market right now with major players pushing to provide on-device AI services within increasingly smaller footprints, “Microsoft’s current implementation with examples like the Copilot+ PC, however, has gotten off to a comparatively rocky start compared to earlier work from Google in equipping its phones with basic pieces of AI functionality such as the magic eraser within their photos app,” [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at Omdia told The New Stack.

Moreover, “Microsoft’s more aggressive, systemwide approach with features such as Recall has only called into question the company’s ability to provide AI services in a secure manner,” Shimmin argued. “I’m sure the company and its hardware partners will in time find a better balance between capability and privacy, for example, but for now, the company has done little to truly ‘wow’ its sizable ecosystem of software developers, especially those sensitive to privacy concerns.”

## Long Game?
Meanwhile, rather than being a killer app for Microsoft, the AI play could be part of a larger strategy.

“Windows on Arm is a long game,” [Jason Bloomberg](https://www.linkedin.com/in/jasonbloomberg/?originalSubdomain=nl), an analyst at Intellyx, told The New Stack. “Today, developers writing for platforms like Microsoft Surface are leveraging the technology, but more generally, Windows on Arm lacks the broad ecosystem that will make it competitive with more popular Arm operating systems. However, this weakness is more a temporary symptom of Microsoft’s long game rather than a flaw in its strategy.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)