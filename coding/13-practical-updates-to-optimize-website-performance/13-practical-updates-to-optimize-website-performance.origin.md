# 13 Practical Updates to Optimize Website Performance
![Featued image for: 13 Practical Updates to Optimize Website Performance](https://cdn.thenewstack.io/media/2024/06/89362a80-13-practical-web-performance-1024x576.jpg)
We recently underwent a major website performance improvement process to give our customers a positive experience from the first click. Our site had relatively low conversion rates, and our team struggled with the division of website management responsibilities. We anticipated that adopting a structured website product management approach would facilitate long-term planning and establish clear management and ownership, all essential to the practical results we were seeking.

In the [first article in this series](https://thenewstack.io/7-technical-updates-to-boost-website-performance/), I explained our cultural shift to treat our website as a product and the initial steps we took to improve Gcore.com’s performance. We then extended our initiative to strengthen our website against security vulnerabilities, maintain consistent uptime, boost search engine optimization (SEO) and improve accessibility.

The methods I’ll share here are broadly applicable and can help your business achieve similar results.

## Stability and Security Improvements
Beyond performance, we also decided to strengthen our website against security vulnerabilities and take steps to maintain consistent uptime.

### 1. SSO Authentication
Single sign-on (SSO) simplifies user authentication by allowing users to access multiple applications with one set of login credentials. We implemented SSO on our website to streamline access management and minimize security risks. This improves [user experience](https://thenewstack.io/bad-by-design-the-world-of-intentionally-awful-user-interfaces/) by minimizing the number of passwords they need to remember and manage. By consolidating authentication, we’re now able to monitor and secure access points more efficiently.

As a result of this and other new security measures detailed below, the number of vulnerabilities on our website has significantly decreased. We now have no [critical P1 issues](https://thenewstack.io/classifying-severity-levels-for-your-organization/), which require immediate attention. We also have no P2 issues, which are high-priority but not critical. Only three moderate, five low and two informational problems remain. This 2.5x reduction in vulnerabilities and elimination of all critical issues highlights the effectiveness of our security improvements.

![A bar chart shows the number of web vulnerabilities on Gcore.com from March 2023 to May 2024, grouped monthly, highlighting 10 issues in total.](https://cdn.thenewstack.io/media/2024/06/67507f4d-monthly-web-vulnerabilities2.png)
This monthly web vulnerabilities chart shows 10 issues over the last 15 months, reflecting improved security.

### 2. Web Application Firewall (WAF) and Bot Protection
After implementing WAF and bot protection in April 2024, the frequency of incident command meetings (ICMs) related to security breaches was cut by more than half.

### 3. Gcore DDoS Protection
This strategy protects our website against distributed denial of service (DDoS) attacks and guarantees high availability. After implementing [Gcore DDoS Protection](https://gcore.com/ddos-protection) on Gcore.com and Gcore.com/blog, we achieved 99.99% availability over the past 30 days, as monitored by Site24x7. Additionally, to further enhance performance monitoring, we set up an alternative tool at Sentry to monitor Core Web Vitals (CWVs).

In the past couple of months, we’ve had zero Incident Command Meetings (ICMs), giving us confidence about the effectiveness of our shielding measures. After implementing Gcore DDoS Protection, we reduced ICMs by more than half on a half-on-half (HoH) basis (comparing the most recent six months to the six months prior), increasing uptime from 80% to 99.99% over the past year.

### 4. Automatic Pod Scaling
This method adjusts the number of running pods in a containerized environment. At Gcore, we implemented automatic pod scaling on our blog in December 2023 and on the main site in February 2024. Afterward, the number of ICMs related to our blog was reduced by more than half on a half-on-half (HoH) basis. In addition, our uptime increased from 80% to 99.99% year-over-year (YoY).

## SEO Strategies
In digital marketing, search engine optimization (SEO) is essential for increasing visibility and driving organic traffic, so we made significant improvements to our website’s SEO strategy. While [Google](https://cloud.google.com/?utm_content=inline+mention) continually innovates to identify safe, user-friendly and functional websites, we focused on several key areas that are consistently known to enhance rankings.

### 1. Structured Data Markup
Structured data markup involves adding specific types of code to your website to help search engines understand the content better, which can enhance search visibility, improve click-through rates (CTRs) and provide a better user search experience. Implementing structured data markup can lead to higher search rankings, competitive advantages and benefits for e-commerce sites, such as data portability and future-proofing content.

To improve the health of our website, we enhanced the structured data markup on our product pages. We added structured data directly to the source code or the head section of the HTML so that our product pages had the appropriate markup. For example, we updated pages that only had “Price” information to include “lowPrice” and “highPrice” values, which provides more detailed pricing information to search engines.

This effort improved website health scores from 60/100 in December 2022 to 97/100 in June 2023, and to a perfect 100 in June 2024. Our structured data markup is accurate and comprehensive, significantly enhancing our site’s SEO and overall manageability.

![Three circular gauges showing improved website health scores over time: 60 in Dec. 2022, 97 in June 2023 and 100 in June 2024](https://cdn.thenewstack.io/media/2024/06/dc63d536-website-health-score.png)
Website health score improved from 60 in December 2022 to 100 in June 2024, reflecting enhanced SEO and performance.

### 2. Special Tags for Lists
To address performance issues identified in Google’s CWV assessment, we implemented unique HTML tags for list content on our website starting in August 2023. We intended for this change to enhance readability and page structure, particularly for mobile where scores were notably low (our CDN/e-commerce page rating was 46 for mobile versus 65 for desktop). Mobile pages required significant enhancement to meet Google’s mobile-first indexing standards.

By improving the structure with unique tags, we aimed to boost our largest contentful point (LCP) and first contentful point (FCP) metrics, enhancing user experience and our overall web performance scores across devices. Between November 2023 and May 2024, the mobile performance score increased by 16%, LCP improved by 32% and FCP by 46%. These improvements can be largely attributed to our implementation of unique HTML tags for list content, which enhanced readability, improved page structure and allowed faster rendering of critical elements.

![Performance score improvements from November 2023 to May 2024, including LCP and FCP metrics](https://cdn.thenewstack.io/media/2024/06/e308c53c-performance-score-improvements.png)
Performance score chart from November 2023 to May 2024, showing a 16% increase in mobile scores, with LCP up by 32% and FCP by 46%.

### 3. Google Tag Manager (GTM) Optimization
This involves refining the GTM configuration to improve a website’s efficiency and performance. We started by thoroughly analyzing the GTM setup to identify and remove unnecessary tags.

We discovered that over 75% of existing GTM tags were irrelevant. By simplifying the GTM configuration and removing 300 redundant tags, we optimized resource utilization, reduced the load on our servers and sped up page load times.

### 4. SEO Standards for Images
We optimized images on the website by using appropriate formats, compressing files and providing clear, high-quality pictures. We now deliver all visuals in WEBP format to reduce file sizes without compromising quality, improve page load times and boost SEO performance.

Additional advanced image optimization techniques, such as Gzip and [Image Stack](https://gcore.com/image-stack) via Gcore CDN compress images by 30% to 70%, significantly improving key performance metrics like LCP and FCP, which matter for SEO. As a result, our images are optimized for user experience and search engine visibility, leading to higher search rankings.

### 5. Google Search Impact and Organic Traffic
These are crucial indicators of how well a website attracts and retains visitors through organic searches. Our efforts in optimizing our website’s SEO and performance have led to a significant increase in Google Search impact.

This substantial growth in organic traffic positively impacted several related marketing metrics over the past year:

- Organic traffic increased by 5x.
- Engaged sessions increased by 5x.
- Engagement rate improved by 21%.
- Conversions increased by 11x.
## Accessibility Improvements
As part of our overall website improvements, we also took five steps to improve its accessibility.

### 1. Color Scheme Adjustments
This process involves modifying the website’s color palette to enhance accessibility for users with visual impairments such as color blindness by selecting color combinations that provide sufficient contrast between text and background.

On our website, we adjusted the color schemes to accommodate all users by using tools and guidelines from accessibility standards like the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/). These adjustments help make our website accessible to a broader audience and allow all users to navigate and interact with our content efficiently and effectively.

### 2. Font-Size Adjustments
Modifying text sizes on a website improves readability for all users, particularly those with visual impairments. We implemented scalable font sizes that adapt to user preferences and browser settings, providing better readability across devices and screens.

### 3. Improved Alt Texts
By providing detailed descriptions (alt attributes) for images on a website, content becomes accessible to users who rely on screen readers and SEO is boosted. Our content marketing department reviewed and updated all image alt texts to provide clearer and more descriptive information.

### 4. Eliminated 404 Issues
Eliminating 404 (page not found) issues requires identifying and resolving broken links so that users can reach the correct pages. We automated 404 error detection and streamlined redirect chains from three to one, which means that instead of going through three redirects to reach the final destination, users now only go through one, enhancing the speed and efficiency of navigation. This improvement was applied across the production environment for Gcore.com, with all tests passing successfully for improved navigation and a better overall website experience.

## Our Results
We evaluated our numbers for an objective look at how this project performed.

**Load times:**Our focus on optimizing images and implementing lazy loading significantly improved load times. For example, the LCP improved by 32% over seven months.**SEO ranking:**By enhancing our SEO practices, such as optimizing structured data and implementing advanced image optimization techniques, our Google Search impact increased fivefold year-over-year (YoY). Organic traffic grew by 500% YoY, with engaged sessions and engagement rates seeing substantial increases.**User engagement:**Accessibility improvements, including color scheme adjustments and font-size modifications, led to a better user experience. This resulted in a 21% increase in engagement rate and a 5x increase in engaged sessions YoY. Conversions increased elevenfold YoY, all while maintaining a steady conversion rate.
While we’re delighted with these results, our innovation continues as we push for even more website improvements.

## Conclusion
Starting with a culture shift in how we approach our website, we were able to significantly improve its performance, SEO ranking, accessibility and user engagement. A product management approach that emphasizes data-driven decision-making and collaboration proved a solid foundation to undertake specific improvements. The proof is in the data: We’ve seen a boost in metrics across the board.

I encourage other organizations to adopt similar strategies to improve their business outcomes through superior online customer experiences. I hope that by sharing our process at Gcore, you’ve gotten some ideas about where to get started. Good luck!

*Elena acknowledges her team, who realized this project and provided data for the article: Nikolay Baranov, Karen Bzhshkyan, Ochuko Eyube, Daria Gromova, Galina Iakusheva, Ilia Kotiashkin, Mikhail Loviagin, Grachia Martirosian, Rustam Mustafaev, Eugene Shygabutdinov and Maria Yurlava.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)