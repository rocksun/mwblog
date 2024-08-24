# Best Practices for Responding to a Major Outage
![Featued image for: Best Practices for Responding to a Major Outage](https://cdn.thenewstack.io/media/2024/08/adae8bd2-outage-1024x571.png)
In the weeks since the Crowdstrike outage brought millions of systems to a halt, countless articles have been written about the cause of the outage, its impact and the costs companies incur during service disruptions.

Virtually every large company had some set of hosts offline due to the faulty update in CrowdStrike’s Falcon software. Our customers at BigPanda were no exception. On July 19, between 04:00 and 07:00 UTC (8-11 a.m. EDT), our systems logged an increase in shared incidents that peaked at 290% of normal, indicating something big was happening throughout our customer base. The outage affected 8.5 million Microsoft Windows-based hosts worldwide.

When faced with the massive scale of the [CrowdStrike outage](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/), IT teams had to get creative to speed up their response and recovery times. Our customers shared their approaches with us, including alert correlation, incident enrichment, high-volume ticket management and the importance of post-event analysis.

**1**: Control the Flood of Alerts With Alert Filtering and Correlation
Thousands of hosts fell offline during the faulty update. Alerts were sent not just from affected systems but also from interrelated systems, and online systems took additional load as a result. This left response teams facing a flood of alert noise and the challenge of sifting through that noise for relevant and actionable information about what was occurring.

IT teams with previously deployed robust alert correlation were best positioned to correlate the flood of “Host not Reporting” and related service alerts into fewer, clearly articulated incidents. Alert filtering and correlation were instrumental in managing the volume of requests, providing critical data and helping teams prioritize and resolve issues efficiently.

## 2: Rapidly Identify Incidents Tied to Affected Hosts
Response [teams then faced the challenge of identifying which incidents](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/) were related to the CrowdStrike update and which were not. Due to the [volume of incidents](https://thenewstack.io/incident-response-is-shifting-left-closer-to-the-customer/) associated with the outage, there was the risk of other issues being ignored in the chaos.

Teams need incidents enriched with important information, such as auto-generated titles, summaries of incidents and, importantly, suspected root causes. This allows responders to immediately identify which incidents are related and address them appropriately. Importantly, non-CrowdStrike-related incidents were still visible and actionable even when other incidents threatened to overwhelm operations teams.

## 3: Create a List of All the Affected Hosts
Once [steps were identified](https://support.microsoft.com/en-us/topic/kb5042421-crowdstrike-issue-impacting-windows-endpoints-causing-an-0x50-or-0x7e-error-message-on-a-blue-screen-b1c700e0-7317-4e95-aeee-5d67dd35b92f) to recover affected systems, you need a consolidated list of hosts showing outages. This is accomplished with a combination of searching for incidents based on enrichment tags and analytics such as an overview of monitoring impacts, drilling down into specific tools and identifying actionable incident trends.

During the outage, this was essential for responders to work through restoring and rebooting servers, and it saved time determining the ultimate scope of the impact.

## 4: Control the Volume of Created Tickets
Here, too, robust correlation made the difference, significantly reducing the number of tickets created and eliminating significant wasted effort. Those using integrated workflow automation to automatically create tickets from correlated incidents had the best experience, with tickets promptly routed to the right teams (and creating tickets that contained the right context to speed remediation).

The incident also served as a pressure test for current IT infrastructures, proving that systems across the entire ops process were able to handle a massive spike in ticket volume. Where systems were overtaxed, teams are working post-outage to increase scalability and resilience. When facing an outage, use the findings from the event to reevaluate your correlation patterns and improve them in ways that will make the next outage easier to handle.

## 5: Post-Event Analysis Through Data Extraction and Analytics
A common response to the outage was to conduct additional insights and reporting following the outage such as reports on mean time to X (MTTx) and tool efficiency. Teams need to consolidate data from diverse workflows into a single, industry-specific dashboard, simplifying the process of identifying gaps, rationalizing tools and optimizing workflows.

Savvy customers continue to use these tools to gather and customize the required data and reports to assess the outage’s final impact.

The response from our customers and ITOps team around the world highlights the importance of preparedness and adaptability in managing large-scale disruptions of this magnitude. This outage has been a catalyst for many to reassess and enhance their operational systems, ensuring greater scalability against future disruptions. We need to prioritize incident response strategies and implement robust monitoring systems to mitigate the impacts of future major [outages like Crowdstrike](https://thenewstack.io/crowdstrike-outage-what-can-cloud-native-teach-us/). The collective knowledge gained from this experience will contribute to stronger and more adaptive IT infrastructures across industries.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)