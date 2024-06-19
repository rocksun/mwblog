# Python Mulls a Change in Version Numbering
![Featued image for: Python Mulls a Change in Version Numbering](https://cdn.thenewstack.io/media/2024/06/c2a2c9f1-nick-hillier-yd5rv8_wzxa-unsplash-1024x683.jpg)
A Python core maintainer is lobbying to change the way the
[Python programming language](https://thenewstack.io/what-is-python/) numbers its releases. [Hugo van Kemenade](https://github.com/hugovk), who will be the release manager for the upcoming Python 3.14 and 3.15 releases, has authored the proposal PEP 2026, “ [Calendar Versioning for Python](https://peps.python.org/pep-2026/),” for how all future releases be numbered.
In short, this proposal suggests that Python versions will be numbered 3.YY.micro where:
*3 is the major version number – it is always 3.*
*YY is the minor version number – it is the short year number: {year} – 2000.*
*micro is the micro version number – it is incremented for each bugfix or security release.*
He noted that there would never be a Python 4. “Python 3” will be the brand going forward.
Thus, Python 3.15 would actually be 3.26, with the “26” representing the year of the release (“2026”).
## Python End of Life
“This aims to make the support lifecycle clear by making it easy to see when a version was first released, and easier to work out when it will reach end of life (EOL),” van Kemenade wrote. Each Python release is supported for five years.
Since 2019, major
[ Python updates](https://thenewstack.io/how-python-is-evolving/) have occurred on an annual basis, as per the release schedule set by [Pep 603](https://peps.python.org/pep-0693/). This numbering would better reflect the cadence, he wrote.
Many people assume Python follows the industry standard of
[semantic versioning](https://semver.org/). The SemVer standard [dictates](https://www.joabj.com/Writing/Tech/Dev/1509-Software-Versioning.html) a version number would be in the format of MAJOR.MINOR.PATCH, where MAJOR would be a major update (that could break API backward compatibility), MINOR would be a version with no breaking changes and PATCH would just be for patches.
This assumption that Python does semantic versioning has led to some frustrations as many yearly Python 3 releases actually break backward compatibility, though users assume otherwise as all new releases are in the 3.XX tree. But major versions are incremented after the first dot, i.e. the
[current release is 3.12](https://devguide.python.org/versions/) and the next major release, later this year, will be 3.13.
Any of these versions may come with breaking changes, flaunting SemVer convention (Python actually predates the Semantic Version standard by about 15 years).
Van Kemenade wrote and
[presented his proposal](https://pyfound.blogspot.com/2024/06/python-language-summit-2024-should-python-adopt-calver.html) the [Pycon 2024 conference,](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/) held last month in Pittsburgh.
Instead of adopting SemVer, van Kemenade suggested Python should go with an increasingly common
[Calendar Versioning](https://calver.org/) (CalVer), which includes some elements of the Gregorian calendar year in the numbering. ![Examples of CalVer numbering with JavaScript and other languages.](https://cdn.thenewstack.io/media/2024/06/552d4a83-calver-examples.jpg)
From the presentation of Hugo van Kemenade (Python Foundation)
Canonical, for instance, uses a calendar-friendly YY.0M.micro, where the year is represented by YY, the month by oM and patched releases by the micro designation. Thus the current Ubuntu version is
[24.02](https://ubuntu.com/download/server).
Going forward, Python releases would go this way:
3.15.0 will be released in 2026 (3.26)
3.16.0 will be released in 2027 (3.27)
3.17.0 will be released in 2028 (3.28)
3.18.0 will be released in 2029 (3.29)
3.19.0 will be released in 2030 (3.30)
And so on…
Skeptical observers on Slashdot noted that this two-number approach would be problematic around the turn of the century, where a two-digit year designation would present ambiguity, making it difficult for build systems to auto-update to the latest version of the programming language, among other issues.
In the year 2100, Python v3.00 would follow Python v3.99?
“Did
[Y2K](https://thenewstack.io/how-the-y2k-bug-returned-on-jan-1-2020/) teach us nothing?” one reader [quipped](https://developers.slashdot.org/story/24/06/15/0642232/python-language-summit-2024-security-workflows-calendar-versioning-transforms-and-lightning-talks). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)