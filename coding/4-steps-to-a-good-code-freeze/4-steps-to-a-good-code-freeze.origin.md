# 4 Steps to a Good Code Freeze
![Featued image for: 4 Steps to a Good Code Freeze](https://cdn.thenewstack.io/media/2024/08/ae29e662-freeze-1024x638.jpg)
I remember it as if it happened yesterday: My engineering manager had just crushed my dreams. “We won’t be able to deploy for a week. We’re in a code freeze for quarterly earnings,” she told me again. The A/B test I had planned to beat our OKR (objectives and key results) wouldn’t happen in time.

The concept of code freezes during critical times such as quarterly earnings or peak traffic seasons is a common practice in the engineering ecosystem. Code freezes are implemented to prevent incidents and ensure product stability when uptime is especially crucial. But the jury is still out on whether code freezes are an effective solution at peak times, and whether development teams still find them useful.

**What Is a Code Freeze?**
A code freeze is a period of time when [software development teams](https://thenewstack.io/managing-software-development-team-dynamics-from-within/) halt the deployment of new code changes to production environments. This practice helps to ensure system stability during critical periods for the business, such as peak traffic (such as retail’s Black Friday) or significant events (ticketing sites releasing Taylor Swift tickets). The goal is to [minimize the risk of introducing new bugs](https://thenewstack.io/progressive-delivery-accelerate-app-releases-while-minimizing-bugs/) or issues that could disrupt service.

During a code freeze, development efforts will be limited to deploying to staging environments or will be restricted to local feature branches. This allows development teams to maintain momentum while still being able to merge, just not to production. Additionally, code freezes are good times to focus on planning, documentation and non-deployable tasks. Effective communication and preparation are essential to manage the workflow before, during and after a code freeze, ensuring a smooth transition and maintaining system reliability.

Here are four steps for helping to ensure a successful code freeze:

**1. Communication Is Key**
The first step to take around any code deployment — and any code freeze — is to communicate effectively. Don’t let your product team be taken by surprise like I was when I learned our A/B test wouldn’t ship. It’s not just about the code being deployed or deployments being frozen, but managing expectations across the entire organization. Changes should be communicated internally, highlighting the potential customer-facing impacts and coordinating any response with relevant teams.

For instance:

**Bug fixes**: A bug fix might resolve an issue for some users, but could also disrupt workarounds used by other teams or services. Communicating these changes helps teams to prepare effectively.**Frontend updates**: Small deployments, such as reordering menu options, can create confusion if they’re not communicated properly. This can lead to an influx of support requests and tickets being raised, burdening the support team unnecessarily.**Internal tool adjustments**: Changes to request rates for internal tools can trigger alerts, causing confusion and extra work for on-call staff. Clear communication ensures everyone understands the context of these changes and can respond appropriately.
Communicating changes in an internally visible shared dashboard ensures that everyone, from engineers to support staff, is aware of what is being deployed, its purpose and its potential impact. This holistic approach helps manage expectations and reduce friction during critical periods.

**2. Implement a Strategy for Managing Deployments Before and After Freezes**
The period before a deploy freeze often sees a rush to make changes, while the period after can resemble a traffic jam. This happens regardless of whether a formal freeze is in place. To manage these periods effectively:

**Pre-freeze rush**: There’s a tendency to push as many changes as possible before a freeze. This can lead to hasty decisions and insufficient testing, increasing the risk of incidents. It’s important to prioritize critical updates and ensure these are thoroughly tested before any code freeze to avoid unnecessary incidents.**Post-freeze traffic jam**: After a freeze, the backlog of changes can overwhelm the system, as well as development teams. This period requires careful coordination to stagger deployments and monitor their impacts closely.
Staggered vacation schedules can create similar issues. By recognizing and planning for these patterns, organizations can better manage workflows and maintain stability.

**3. Use Freeze Periods for Non-Deployment Work**
While deploy freezes are used to prevent engineers from becoming overburdened, that doesn’t mean developer teams should do nothing. This time can be used for tasks that don’t require immediate deployment, such as:

**Planning and coordination**: Develop detailed plans and coordinate upcoming projects. This preparatory work can streamline future deployments and improve overall efficiency.**Tool development**: Focus on building and enhancing internal tools, such as internal developer platforms, that support processes and improve productivity.**Documentation and training**: Update documentation and provide training sessions to upskill team members. This ensures everyone is prepared for future challenges and changes.
This approach helps maintain productivity without risking system stability and ensures that the team continues to contribute value even when deployments are paused.

**4. Run a Post-Freeze Review**
After the freeze period, it’s crucial to review the approach taken. This involves:

**Gathering feedback**: Talk to on-call engineers, support staff, process organizers and even customers about their experiences. Understanding their perspectives helps identify pain points and areas for improvement.**Assessing effectiveness**: Evaluate what worked well and what didn’t. Were there any incidents during the freeze? How were they handled? What could have been done differently?**Implementing changes**: Based on the feedback and assessment, introduce changes to make the process smoother and more effective for the next critical period.
This continuous improvement cycle ensures that the organization learns from each experience and enhances its approach over time.

**Prepare for Incidents**
Regardless of whether a deploy freeze is in place, incidents will occur. Preparation is key to managing them effectively:

**Build out an incident cheat sheet**: Prepare a comprehensive guide that includes on-call schedules, incident processes and backup plans. This ensures everyone knows what to do and whom to contact in case of an incident.**Implement training and drills**: Conduct regular training and incident response drills. This helps teams stay sharp and prepared for real incidents.**Institute a support system**: Ensure that there’s a robust support system in place. This includes having enough resources and tools to manage incidents effectively and reduce downtime.
Remember, [incidents provide valuable learning opportunities](https://thenewstack.io/3-strategies-to-turn-incidents-into-learning-opportunities/). They foster teamwork, improve problem-solving skills and lead to better systems and processes. By preparing thoroughly, organizations can turn incidents into opportunities for growth and improvement.

By taking each of these steps, organizations can navigate critical periods smoothly and balance the [needs of the business](https://thenewstack.io/5-signs-your-business-needs-an-operations-intervention/) with the well-being of their employees.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)