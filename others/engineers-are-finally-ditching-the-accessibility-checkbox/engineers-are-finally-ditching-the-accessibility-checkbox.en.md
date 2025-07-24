A couple of years ago, I dropped the accessibility bomb in an engineering meeting, and I watched the joy of life leave the room. Someone muttered something about homework, a couple of people rolled their eyes, and I’m convinced the rest just silently hoped I’d forget about it.

It’s not that [engineers didn’t want to build accessible products](https://thenewstack.io/entrepreneurship-for-engineers-how-to-build-products-customers-love/). Accessibility had a tendency to show up when prospects would demand something called a VPAT. We can all picture that “accessibility advisor” quoting WCAG standards, and it instantly reminds us of that security advisor presenting OWASP guidelines as security “requirements.” Ugh.

But it’s 2025, and accessibility is table stakes.

Accessibility isn’t just a checkbox or a legal buzzword. It’s not a side quest for compliance crusaders either. Instead, it’s increasingly central to building resilient, user-friendly, and future-proof software. And if your product happens to involve documents — PDFs, forms, reports — the stakes are significantly higher.

At Nutrient, we build tools that help users interact with documents, not just UIs. That means accessibility isn’t just a frontend concern — it’s baked into the content we render, preview, and manipulate. We’ve learned the hard way that you can’t fix accessibility by slapping aria-label on a few buttons if your PDFs are a labyrinth of untagged content that neither developers nor end users can manage.

This article is for [engineers and production teams](https://thenewstack.io/why-successful-platform-engineering-teams-need-a-product-manager/) around them, who are ready to stop rolling their eyes at the topic and start problem-solving. We’ll keep it simple, skip the fluff, and focus on what matters: why accessibility should be on your radar now, and how to make meaningful progress without burning out.

## The Two-Layer Problem: UI vs. User-Centered Accessibility

For most product teams, accessibility starts and ends with the UI: Does the user see the right thing? Can they click, keyboard tab, or swipe through it? Are the labels clear, the colors readable, the focus indicators visible?

These are all good questions. But they miss the bigger point.

Accessibility is not about the UI — it’s about the user. And users don’t present themselves in predictable, idealized states, regardless of what the user persona card suggests. Sometimes they’re using a screen reader. Sometimes they’re navigating entirely by keyboard. Sometimes they’re just temporarily impaired — a broken wrist, a migraine, or just holding a baby in one arm while using your app with the other one.

That’s why accessibility matters. It’s not about conformance levels, standards, and satisfying a legal department. It’s about ensuring that people — real, varied, and unpredictable — can interact with what we’ve built.

And here’s where the game is changing: Interfaces are no longer fixed. AI can generate UI on the fly, personalized for the end user. Apps are increasingly stitching together components from APIs, Markdown, documents, and user input.

It’s no longer enough to design a nice UI and ensure it can be used in an accessible way. We must ensure that the building blocks — the components, content, documents, and especially AI-generated modules — are accessible by default. If you’re previewing a PDF in-app or rendering structured content dynamically, accessibility isn’t something that can be bolted on afterward.

At Nutrient, we see this play out in documents. However, the lesson applies broadly: In a world where UIs are increasingly fluid, accessibility must start at the foundation. Not just in its appearance, but also in how it behaves, sounds, and adapts.

That’s not an edge case. That’s where software is going.

## How 2025 Regulations Are Making Accessibility Table Stakes

If accessibility has always felt like a “someday” task — something to clean up post-launch or delegate to QA — 2025 is here to change that.

The European Accessibility Act (EAA) went into effect on June 28, 2025. It mandates that any digital product or service offered to consumers in the EU — from banking apps to e-commerce platforms — must be accessible to all users. That includes websites, mobile apps, and yes, documents.

Across the Atlantic, the U.S. is catching up. Under the updated Americans with Disabilities Act (ADA) rules, state and local governments have deadlines in 2026 and 2027 to make their digital experiences comply with WCAG 2.1 Level AA. Private companies are next in line.

And the lawsuits? They’ve already started. Accessibility litigation is on the rise, and procurement teams are beginning to view accessibility in the same way they approach security — as a deal-breaker, not a feature request.

But — again — this isn’t just about legal pressure.

Accessibility is becoming an essential component of modern software infrastructure. As AI, personalization, and responsive [design create more dynamic interfaces](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/), the only way to ensure inclusivity is by making accessibility an integral part of how things are built, not an afterthought added later.

It’s no longer a question of “if” accessibility will appear in your backlog. It’s when. Or it’s likely already there. It’s also about whether you’ll be ready to deal with it before the deadline, or after the fire drill.

## Practical Engineering Steps That Don’t Require Accessibility Experts

Let’s be honest: Accessibility can feel overwhelming. The standards are dense, the tooling is inconsistent, and the guidance sometimes reads as if it were written exclusively for compliance officers, rather than someone shipping code.

But here’s the good news: You don’t have to boil the ocean. You just have to stop ignoring the fire.

Start with the basics — the things that genuinely help real users and show up in almost every standard and audit:

* Use semantic HTML. <button> beats <div onclick> every time. Like anyone had to tell you this.
* Label your controls. Every input needs a label. Every image requires alt text, unless it is purely decorative. Don’t overdo it; the users don’t want the screen reader to explain vignettes.
* Support keyboard navigation. Tab order should make sense. Focus shouldn’t disappear. Skip links aren’t old-fashioned — they’re necessary.
* Check your contrast. It’s not just aesthetics. Bad contrast makes your app unreadable for some users.

These are not exotic practices. They’re just reasonable defaults.

Then, bring in the tooling:

* Use automated checkers like Axe, Lighthouse, or WAVE to catch low-hanging issues.
* Test with real assistive technology occasionally — a screen reader, reduced motion settings, or high contrast mode.
* Bake accessibility checks into your CI pipeline. Treat it like performance budgets or test coverage: visible, automated, and non-negotiable.

If your product involves [dynamic content or documents](https://thenewstack.io/how-to-use-llms-for-dynamic-documentation/), consider the accessibility of that output too. Ask: Can a screen reader make sense of this? Can someone fill it out without a mouse? You don’t need to be a PDF/UA expert, but you do need to care about it.

You’re not alone in this. Many open source libraries, design systems, and frameworks now prioritize accessibility out of the box. Use them. Extend them. File issues when they fall short.

Progress doesn’t mean perfection. It means deciding not to ship avoidable barriers.

## From Checkbox Mentality to Core Engineering Practice

Accessibility isn’t a feature you check off once. It’s an ongoing practice, just like testing, security, or performance. It doesn’t always win sprint points. It doesn’t always show up in user feedback. But when it’s missing, some humans out there simply can’t use what you built.

And when that happens, it’s not just a technical failure. It’s an experience that shuts people out.

You don’t need to become an expert overnight. But you can start. You can fix what you know is broken. But even better, you can [build habits that scale across your team](https://thenewstack.io/high-performing-devops-teams-build-self-service-platforms/), your product, and the future interfaces you haven’t even thought of yet.

Because when the UI disappears — when AI completely takes over the generation of the layout, or when your app adapts to voice, screen readers, or unknown input — the only thing that will ensure usability is how well your components, your content, and your code respect the user’s reality.

That’s accessibility. Not a checkbox — but a good software foundation.

And if you’re an engineer, that foundation is yours to build. Own it. Make humans proud.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/10/e3426e55-cropped-bcc380cc-milos-dekic-nutrient-600x600.jpg)

Miloš is a Product Management leader at Nutrient, shaping the future of digital documents through innovative software. With a diverse career spanning software engineering, consulting, and leadership roles, he has founded companies, led teams, and mentored many along the way....

Read more from Milos Dekic](https://thenewstack.io/author/milos-dekic/)