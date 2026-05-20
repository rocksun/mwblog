Picture making a lasagna with noodles, peanut butter, and pears. You’ve got the base right, but the ingredients don’t quite add up to a palatable meal.

It’s how [Mike Paciello](https://www.linkedin.com/in/mike-paciello-1231741/) explains the accessibility gaps that surface when developers use LLM-based methods to code web pages and apps. “With AI-based tools, the gap that exists today is structural, not incidental. The root of the challenge is that LLMs have been trained on an inaccessible Web,” Paciello, Chief Accessibility Officer at [AudioEye](https://www.audioeye.com/), tells *The New Stack*.

To extend the lasagna metaphor, the problems are baked in.

> “With AI-based tools, the gap that exists today is structural, not incidental. The root of the challenge is that LLMs have been trained on an inaccessible Web.”

## **The AI and web accessibility gap**

An LLM builds a navigation menu that looks clean in review but adds conflicting ARIA labels, structures headings by visual size rather than semantic hierarchy, and traps keyboard users inside the component. None of these problems surface in a browser, they only do when a real user with a screen reader or assistive technology that relies on keyboard input, tries to navigate the page.

Case in point: When page headers are semantically incorrect, navigation suffers and readers with disabilities pick up sections out of order. Focus management, a key accessibility construct, becomes a challenge. If a click opens another window, and when ARIA labels are not properly integrated into code, a low-vision or blind user can’t reliably navigate back and forth. They get stuck in a keyboard trap and usually the only way out is by shutting down the computer.

Unfortunately, such incidents are far from isolated. A whopping 95.9% of the top million homepages have detectable [Web Content Accessibility Guidelines (WCAG)](https://www.audioeye.com/compliance/wcag/) failures, reversing six consecutive years of improvement, according to the [2026 WebAIM Million report](https://webaim.org/projects/million/). The average web page has 297 accessibility issues, even among companies actively investing in accessibility, as per [AudioEye’s Digital Accessibility Index](https://www.audioeye.com/digital-accessibility-index/2025/).

Accessibility oversights cost money and damage reputation. Target paid $6 million in damages and $3.7 million in attorney fees and costs [in a 2006 lawsuit](https://wsc.us.org/case-target) after a group of blind or low-vision California plaintiffs argued the retail giant’s website was inaccessible due to its incompatibility with screen-reader technology. Over the years, lawsuits have increased. Since 2020 alone, total [accessibility lawsuit filings have more than doubled](https://www.audioeye.com/guides/2026-web-accessibility-litigation-report/), with 78% targeting e-commerce businesses. The barriers driving a record number of accessibility lawsuits — keyboard navigation failures, missing labels, broken screen reader support — are exactly what AI-generated code most commonly gets wrong.

## **The lag in LLM accessibility**

A lack of education compounded by a lack of prioritization worsens the situation. Most native HTML elements used to construct a web page have some attribute that makes it usable and accessible, but too often, neither the LLM nor the coder is familiar with these constructs. LLMs and developers need to know that the navigational schema that renders information for blind or low-vision users is not the same as that for visual learners.

A [June 2025 report](https://www.nycbar.org/reports/the-impact-of-the-use-of-ai-on-people-with-disabilities/), “The Impact of the Use of AI on People with Disabilities,” from the NYC Bar Association states: “AI relies on large-scale statistical learning, which tends to optimize for the ‘average’ user. People with disabilities, who form a highly diverse and frequently underrepresented group, are often excluded or mischaracterized.”

“The whole enterprise builds on a shaky house of cards,” Paciello says. Fortunately, fixes are straightforward.

## **Tips: WCAG compliance for developers**

Developers can tackle worrisome accessibility issues by following these tips.

### 1. Prioritize accessibility testing

Treat accessibility like you would privacy and security. “You don’t deploy code without running a security check; don’t deploy code without running an accessibility check,” Paciello advises. The earlier you catch issues, the cheaper they are to fix.

> “You don’t deploy code without running a security check; don’t deploy code without running an accessibility check.”

### 2. Integrate accessibility testing into your SDLC

Use an [SDK like AudioEye](https://www.audioeye.com/solution/developer-tools/)’s to detect and resolve accessibility issues throughout the software development lifecycle. Ensure the object and code libraries you use have semantic HTML built in. (More about workflow integration, later.)

Recognizing the magnitude of the accessibility problem, a number of companies deliver “overlay widgets,” pop-ups that enable users to make changes on the fly to the visual presentation layer. Unfortunately, these “fixes” are just theater, changes like increasing or decreasing the font size that do nothing to address fundamental accessibility problems. “It’s rooted in a fundamental misunderstanding of how people with disabilities use technology to interact with the web,” Paciello says.

### 4. Keep accessibility current after launch.

Websites change constantly. A site that passes an audit today can fail tomorrow after a content update, a new plugin, or a framework change. Using a solution that combines 24/7 automated monitoring with expert-written custom fixes means you’re catching new issues as they’re introduced, not months later when a complaint arrives.

### 5. Invest in education

To address misunderstandings with respect to accessibility, take free coding courses, like [those from AudioEye](https://www.audioeye.com/courses/accessible-coding/), that teach the fundamentals of accessibility testing at the component level, from focus management and landmarks to form validation and color contrast. Developers need to understand where the cursor lies or how the user interacts with the screen reader and use semantic HTML along with the appropriate CSS for a running start.

## **Workflow: Where accessibility testing should live in your development process**

Make sure the tools you use complement your process. To prioritize accessibility, ensure it’s woven into the entire software development cycle, right from the development of design and requirements, to coding and QA testing.

Testing tools like AudioEye’s SDK are designed to integrate across the development pipeline. Doing so ensures that each page and every construct on the page is coded according to WCAG guidelines, so they’re accessible and usable, while also integrating with component-level testing with Jest, which catches issues before they compound. Similarly, full-page CLI testing catches contextual issues like heading hierarchy that component testing can miss.

CI/CD integration makes accessibility checks automatic on every deployment, catching issues before they reach users. But code isn’t the only thing that changes. Content updates, new features, and third-party scripts can all introduce new barriers after a site is live. That’s where an accessibility partner comes in, one that combines AI-powered automation with expert-written custom fixes to catch and resolve issues continuously, not just at launch. As the site evolves, that ongoing support is what keeps accessibility from slipping between updates.

## **The recipe to get accessibility right**

Incorporating accessibility into web applications and pages is a must-do as AI-assisted coding picks up momentum. “LLMs are like students; we need to fix what they get wrong,” Paciello says. “But here’s the beauty of it: Once you do teach them, you get speed, you get scale right out of the box, and that repeats itself going forward.”

With accessibility issues addressed, developers will have all the ingredients to make a killer “lasagna” — and potentially skirt ADA compliance lawsuits too.

*Test your website using [AudioEye’s accessibility scanner](https://www.audioeye.com/solution/accessibility-scanner/) to detect any accessibility issues.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/9056536e-cropped-a44aa3a7-1597405674814-600x600.jpeg)

Poornima Apte is a trained engineer turned award-winning freelance technology writer. She’s a frequent contributor to Forbes, Fortune, Salesforce, MIT, Princeton, Mechanical Engineering, the American Society of Civil Engineers, and Tech Briefs, among other publications. A professional member of the...

Read more from Poornima Apte](https://thenewstack.io/author/poornima-apte/)