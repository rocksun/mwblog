**When Elon Musk’s X sent cease-and-desist letters** demanding that Nitter — an open-source alternative front end for the social media platform — permanently shut down its instances and remove the project’s source code repository, it went after the code itself.

While Nitter.net was the project’s main public instance, other developers can run their own versions because the code is open source. So taking Nitter.net offline doesn’t really eliminate Nitter, because its code can be forked and used to run independent instances, including services such as [XCancel](https://github.com/zedeus/nitter/wiki/Instances). X’s demand for the repository goes further.

## Open source meets platform control

Open source gives developers control over Nitter’s code, but not the platform it relies on. X still controls access to its service, and its latest move shows how that control can extend beyond just changing an API.

> Open source gives developers control over Nitter’s code, but not the platform it relies on.

Nitter used to let people read public X posts without an account, but that stopped working in 2024 after X shut off the guest access the project relied on, taking Nitter.net offline. Nitter later found a way back by using real X accounts to access posts, according to the [project’s GitHub repository](https://github.com/zedeus/nitter).

That got Nitter back online, but it also meant relying on X accounts to keep it running. X controlled those accounts and could change the rules around them at any time. That doesn’t necessarily put someone who simply downloads or forks Nitter’s code in the same position, since doing so alone doesn’t mean they’ve agreed to X’s terms.

## X’s cease-and-desist claims

Those changes are now at the center of X’s legal case. According to the cease-and-desist letter — first [reported](https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/) on by *TechCrunch* — X says Nitter violated its rules by scraping data and accessing accounts and session tokens, and accuses the project of “unlawful use and circumvention” of its API.

X’s lawyers also cited the Lanham Act and [Section 33.02 of the Texas Penal Code](https://tcss.legis.texas.gov/resources/PE/htm/PE.33.htm), which deals with accessing computer systems without the owner’s “effective consent.” But breaking a platform’s rules doesn’t mean the law was broken, too.

> Breaking a platform’s rules doesn’t mean the law was broken, too.

## GitHub’s code removal standard

Under [Section 1201 of the Digital Millennium Copyright Act](https://www.copyright.gov/policy/1201/), software can be targeted if it’s used to bypass technology that protects access to copyrighted material, even when the software doesn’t contain that material itself.  
  
A claim that software bypasses a technical restriction isn’t enough on its own to get a repository removed from GitHub. For a Section 1201 complaint, the company must identify the copyrighted material being protected and explain how the code circumvents the technology controlling access to it, according to [GitHub’s guidelines for submitting circumvention claims](https://docs.github.com/en/site-policy/content-removal-policies/submitting-content-removal-requests).

X reportedly says Nitter got around its API restrictions to access accounts and session tokens. The question is whether those restrictions were protecting copyrighted material in the way Section 1201 requires.

## The YouTube-dl precedent

A similar issue arose in 2020, when GitHub removed the open-source [YouTube-dl project](https://github.blog/news-insights/policy-news-and-insights/standing-up-for-developers-youtube-dl-is-back/) following a Section 1201 complaint from the Recording Industry Association of America. GitHub later restored the repository and changed how it handles these complaints, adding technical and legal review before removing code when a circumvention claim isn’t clear.

For now, the repository remains on GitHub, archived and read-only. The code can still be viewed and forked, even though Nitter’s developer is no longer working on it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)