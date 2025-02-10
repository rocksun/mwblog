# 12 Critical Open Source Projects Losing Security Support in 2025
![Featued image for: 12 Critical Open Source Projects Losing Security Support in 2025](https://cdn.thenewstack.io/media/2025/01/769aa84f-vanna-phon-hrxikdxoapo-unsplash-1024x576.jpg)
Nothing lasts forever, and this especially true in [open source software](https://thenewstack.io/open-source/). Even the most popular versions of open source technologies will one day reach their end-of-life (EOL).

The EOL event for a major version of an open source software package is more challenging than just missing out on new features that will only be incorporated into future versions. It creates security risks for applications that depend on that [open source software](https://thenewstack.io/the-future-of-open-source-needs-more-give-and-less-take/).

For example, the Apache Struts framework recently identified a critical vulnerability ([CVE-2024-53677](https://www.herodevs.com/vulnerability-directory/cve-2024-53677)). While the issue was identified in actively supported Struts 6 versions, it applies to deprecated, end-of-life versions of Struts 2 that thousands of applications still use.

Companies still reliant on Struts 2 are exposed unless they can immediately migrate to Struts 6, which is unrealistic for most applications. Another option is to use a drop-in replacement for your open source library from a trustworthy, long-term support provider. These solutions include vulnerability patches, which provide a viable, secure, and near-instant solution to potentially looming disasters — especially for businesses in regulated industries — giving you more time to plan your migration thoroughly. Our team at HeroDevs offers a solution like this for Struts 2. In the week after CVE-2024-53677 was identified, interest in our Struts solution grew by 20x, highlighting just how big of an issue a critical CVE can be for users of unsupported OSS.

By getting ahead of your open source software’s end of life, you can better plan your migrations so you don’t put your and your customer’s data at risk. This list of 12 represents what I think are some of the most critical projects that will have EOL events in 2025. It’s important to note that this list is not exhaustive. My team has identified nearly 150 primary open source EOL events in 2025, and there are likely more that can’t be predicted yet.

It’s important to note that there is more than just one type of end-of-life event, such as a complete discontinuation of a package vs the discontinuation of support for just specific versions. AngularJS was completely deprecated in January of 2022 because the team at [Google felt it no longer met the needs](https://thenewstack.io/herodevs-throws-net-6-users-a-post-deprecation-lifeline/) of the modern web landscape. Meanwhile, the .NET Foundation and Microsoft discontinued support for .NET 6 in November 2024 to focus on the newer .NET 8 and future versions. Most projects that will reach their end-of-life in 2025 are version EOLs similar to .NET 6.

### 1. Laravel v10 (Feb. 4, 2025)
[Laravel](https://thenewstack.io/introduction-to-laravel-for-ruby-on-rails-or-django-fans/) is a full-stack web application framework based on PHP. It is very developer-friendly, widely used, and has a strong community. It is designed to simplify and accelerate web development. Laravel v10 will reach its end of life on Feb. 4, 2025.
### 2. OpenSSL v3.1 (March 14, 2025)
OpenSSL is widely used for encrypted, secure communications across the web and communications platforms. It is likely the most commonly used package on this list; anything with an API likely uses it. OpenSSL v3.1 will reach its end-of-life on March 14, 2025.

### 3. Ruby v3.1 (March 31, 2025)
[Ruby](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/) is a programming language extensively used with the Ruby on Rails web framework. Ruby on Rails is widely known for enabling the rapid development of web-based applications. Ruby v3.1 will reach its end-of-life on March 31, 2025.
### 4. js v18 (April 30, 2025)
[Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) is a cross-platform JavaScript runtime environment that doesn’t need much introduction. Many companies — including some of the largest — use it to build applications fast and scalable applications. Node.js v20 introduces a permission model and performance updates in the V8 engine. Node.js v18 will reach its end of life on April 30, 2025.
### 5. Django v5.0 and v5.1 (April 30, 2025)
[Django](https://thenewstack.io/what-is-pythons-django/) is a Python-based web application framework that enables the development of quick, easy, and clean programs. It handles complex databases well, making it suitable for data-intensive applications, data science tools, and social media applications. Django v5.0 and v5.1 will expire on April 30, 2025.
### 6. Kafka v3.4 (May 3, 2025) and v3.5 (Aug. 25, 2025)
[Kafka](https://thenewstack.io/gitops-for-kafka-at-scale/) is one of the most scalable and widely adopted distributed pub/sub frameworks for real-time data pipelining and analytics use cases. Kafka’s ability to handle large volumes of data in a scalable, fault-tolerant way has made it the bedrock of many large-scale data architectures. v3.4 will reach its end-of-life on May 3, 2025. v3.5 will reach its end-of-life on Aug. 25, 2025.
### 7. Drupal v10 (June 16, 2025)
[Drupal](https://thenewstack.io/drupal-creator-websites-needed-more-than-ever-in-the-ai-era/) is a CMS and framework known for its flexibility, scalability, and extensibility. It is widely used in content-centric platforms like websites, community and social platforms, and media companies. Drupal v10.3, the last supported version of Drupal 10, will end its support on June 16, 2025.
### 8. Kubernetes < v1.32 (July 2025)
[Kubernetes](https://thenewstack.io/kubernetes/) is the most widely used platform for container orchestration. Most containerized applications will use some version of Kubernetes, especially those with complicated systems that can benefit from microservice architectures. Like many open source software release schedules, Kubernetes releases follow a structured timeline where each minor version is supported full-term for one year following the release, with a 2-month maintenance period before its end-of-life. Kubernetes v1.34 was released on May 15, 2024, and is expected to reach the end of its full support in May 2025 and its end-of-life in July 2025.
### 9. MongoDB 6 (July 31, 2025)
[MongoDB](https://thenewstack.io/5-reasons-to-run-mongodb-on-kubernetes/) is a versatile, scalable NoSQL database widely used across different industries and loved for its flexible support of various kinds of data (fully structured, semi-structured, and unstructured). MongoDB 7 brought exciting improvements like Queryable Encryption, but it does mean that the six will reach its end-of-life on July 31, 2025.
### 10. NumPy v1 (Sept. 17, 2025)
[NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) originated as a fork of Numerical Python (Numeric) and incorporated improvements from Numarray. The Python scientific computing community wildly adopts it, which is excellent for intensive numerical data processing and computation applications. On Sept. 17, 2025, all versions of v1 will reach their end-of-life.
### 11. Postgres v13 (Nov. 13, 2025)
[PostgreSQL](https://thenewstack.io/modern-postgresql-deployment-3-cloud-native-approaches-you-should-know/) is a highly extensible relational database management system that supports SQL for querying and data management. It is widely used in data analytics, business databases, and web applications. V13 will reach its end of life on November 13, 2025.
### 12. Angular v17 (May 15, 2025) and v18 (Nov. 19, 2025)
[Angular](https://thenewstack.io/angular-shares-potential-ideas-for-2025-improvements/) is a comprehensive framework launched by Google engineers in 2010 and later rewritten to replace AngularJS in 2016. It is widely used to build scalable web applications.
Angular v17 will end on May 15, 2025, and v18 on Nov. 19, 2025.

Migrations take significant amounts of time (and money). The complexity of migration varies depending on several factors, including the open-source software packages/framework, your codebase’s cleanliness, your team’s size, and your application’s scale. At HeroDevs, we spend much time talking with organizations about migration and remediation options. From the front-end AngularJS migrations (where 100k lines of code migration might require [2.7 years of effort](https://xlts.dev/blog/2021-01-15-the-math-of-migrating-from-angularjs)) to Spring 5->6 migrations (where a large project with many dependencies could take [more than 6 years of effort](https://www.herodevs.com/blog-posts/spring-framework-6-the-full-cost-of-migrating-from-v5-to-v6)), these EOL moments should be planned and budgeted for.

Suppose an OSS package you rely on expects an EOL event in the coming year. In that case, you should have already started your planning and migration — especially if you are in an industry that is highly regulated, like healthcare (HIPAA), payments (SOC 2 and PCI DSS), education (FERPA), and government (FedRAMP).

If you need more time, there are options. Direct or third-party commercial support may offer extended long-term support, allowing you to plan your migrations according to your timeline and keep your data secure.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)