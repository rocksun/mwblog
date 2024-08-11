# How To Protect Your Java Against Licensing Liability Risks
![Featued image for: How To Protect Your Java Against Licensing Liability Risks](https://cdn.thenewstack.io/media/2024/08/ec5ebd45-java-1024x576.jpg)
So, you have removed all the Oracle JDKs from your environment that require an expensive Oracle Java SE Universal license, which is related to the Oracle Master Agreement (OMA). But now you need to prevent Oracle Java from sneaking back in and triggering a new licensing obligation to [Oracle](https://developer.oracle.com/?utm_content=inline+mention). Here’s a look at disabling the JavaUpdater and other current and common approaches, their effectiveness and shortcomings, as well as providing several additional mechanisms for your consideration.

## Background
In January 2023, Oracle changed the license requirements for [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) to an “all-employee metric.” The specifics should be reviewed in their actual agreement, but for the purposes of this discussion let’s paraphrase that agreement to mean: If you have installed one or more instances of Oracle Java SE, regardless of installation location, that falls under the Oracle Technology Network (OTN) license, your organization could be subject to the “all employee” license requirement, regardless of how many employees use Java or even have or use a computer. The potentially significant financial risk to your organization warrants ongoing vigilance.

## How Does Oracle Java Get Back In?
There are several ways in which Oracle Java can be installed or updated. Some of these methods apply only to desktops; some apply to servers. Both environments should be considered as both are subject to the same Oracle licensing requirements. There are several ways in which Oracle Java can be installed or updated.

- Users download directly from download.java.com or oracle.com/downloads.
- Users download from externally maintained mirror sites.
- The JavaUpdater background process — (on Windows Desktops) installed alongside
[Oracle Java Development Kit](https://thenewstack.io/survey-86-of-oracle-java-users-migrating-to-alternatives/)(JDK) or Java Runtime Environment (JRE). - The Java Control Panel Applet — allows one-click updates to an existing JVM (Java Virtual Machine)/JDK.
- Golden or other base Virtual Desktop Infrastructure (VDIs)/images created before migration.
- Backups/recovery images taken before you migrated your Java.
- OS convenience notifications — if Java is not installed on a system and the user types “Java” at a command prompt, they will get a message pointing them to java.com.
- Many legacy applications that require Java may prompt the user to download Oracle Java; newer applications generally request OpenJDK, but it is not universal.
- JavaScript — There are several functions that make it convenient for developers to present direct downloads or clickable buttons that redirect to Oracle Java websites.
Following are some do’s and don’ts to consider for the highlighted points above:

## Blocking java.com and `oracle.com/java/download`
Is Not Enough
Java has been available for nearly 30 years. In that time, it went through many iterations, including from free to paid, depending on the provider. Due to Java’s popularity and the fact that Oracle Java was available for free for many use cases, Oracle Java was made available through many web channels, distribution partners and academic institutions, many of whom have not bothered to maintain or remove fully functional copies of publicly available JDKs and JREs. These older binaries are not generally troublesome from a licensing perspective (security is another matter), but the accompanying Java updater and Java control panel applet make it quite easy for a user to inadvertently update their installation to a version that would require an Oracle license.

We will discuss strategies applicable to the most common versions that remain deployed (Java 6-21), but you should be aware that there are specific versions of Oracle Java that are subject to license requirements. These are 8u211+,11,12,13,14,15,16. In addition, Oracle considers the use of “commercial features” as another trigger for their license requirement such as the use of their MSI ([Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Windows Installer ) or use of JFR (Java Flight Recorder).

*Note: In September 2024 Oracle Java 17 will also require a paid OTN license for commercial use. *
Do:

- Block the download sections (and specific versions if you can).
Don’t:

- Block the whole domain. Java.com has a wealth of information, documentation and discussion that is helpful for anyone that participates in the Java community.
## Disabling Java Update
Oracle Java includes a background (TSR or terminate-and-stay-resident) process that is enabled by default to check for new versions of Java.

These can be disabled without affecting the current working state of the installed Java. Azul recommends removing, or at the very least disabling, these at the registry level and disabling the user’s ability to use or re-enable them. Some older distributions of the Oracle JVM/JRE/JDK allowed the uninstallation of the updater; newer builds and versions do not separate this component. Note, it is a violation of the Oracle terms to modify or remove any portion of the JDK, however, it is not a violation to restrict access to any files.

## Disabling Java Control Panel Applet
The control panel applet (`javacpl.exe`
on Windows) included with Oracle Java JREs provides a graphical interface to control many aspects of the Oracle JVM. I am going to call out WebStart here, even though it is not separated from the Oracle JVM because the control panel applet has close ties to WebStart and the equivalent functionality is implemented separately by the open community (in the IcedTea-Web open source project). The control panel applet includes a tab that allows the user to update their Java in several ways:

By either setting up the automation or clicking the “update now” button, the user can initiate a download of the most up-to-date version of their JRE/JDK.

Do:

- Disable this functionality entirely, no self-service user-level functionality remains in this interface (remove access to
`javacpl.exe`
). - Understand the underlying properties files that are manipulated by this interface and modify/update them at the administrator level.
- On Windows, you can disable two registry keys “EnableJavaUpdate” and “EnableJavaUpdateCheck” (DWORD) under
`HLM:\SOFTWARE\JavaSoft\Java Update\Policy`
. - Power users should be educated on the IcedTeaWeb-settings interface, which replaces most of this functionality.
Don’t:

- Delete
`javacpl.exe`
— this would violate Oracle terms.
## Updating Golden or Other Base VDIs/Images
Many enterprises use gold images to instantiate virtual machines for various use cases, from quick spot testing and agile development to standardization of production-grade machines. These images often include general-purpose or corporate-mandated software and may have included a JRE for servers or a JDK for development images. Because these images remain offline with their disks in an archived state until instantiated, they can lie dormant and not be picked up by normal scanning/observation mechanisms. If they remain present in your environment, they do represent a risk if they are instantiated and used in production scenarios.

Do:

- Visit your VDI/image repository to determine if Java is included with standard builds or images. If found, rebuild your images using an appropriate binary.
- If you have pre-image-startup triage capabilities, ensure that an updated JVM is used.
Don’t:

- Place the burden of replacement on the image user.
- Allow temporary use of Oracle JVMs.
- Assume short-lived images are short-lived.
## Refreshing Backups, Recovery Images and Snapshots
Over time, backups, etc. will become less of an issue; they will age out naturally. But during the period immediately following migration, particular care should be made to track systems that invoke any of these restoration mechanisms. Care should be taken with the backups themselves; it has been noted that Oracle in certain scenarios has indicated that backed-up files remain readily available and easily enabled and thus represent license risk violation. Systems restored from backups will be subject to your existing software execution policies, so ensure they will be captured and remediated as soon as possible. Once remediated, a new backup/snapshot should be taken, and if possible, previous backups should then be moved offline and made “not readily available.”

Do:

- Make/update snapshots that do not include Oracle Java.
- Ensure execution policies address the execution of unwanted Oracle Java binaries.
Don’t:

- Ignore the backup archive, if it can be used, it will be.
- Assume that the end user will discover the situation and remediate.
- Allow even older (non-OTN) Java to run unchecked, review the Java updater and Java control panel settings at a minimum.
## Disabling OS and Convenience Updates
If a user types “java” at a command prompt or an application requests Java on an uninitiated (free of any Java) MacOS system, you will get a response from the OS telling you to visit java.com:

Do:

- Educate your user base on the Java they should use (based on corporate standards or guidance).
- Make Java readily available via self-service options. As there are many options and application-specific requirements, it is unreasonable to expect apps and users to adhere to specific versions. While it is safe to allow flexibility in major Java versions, it is recommended that the user select the most up-to-date patch version (of a major version) when possible.
- Consider a supported OpenJDK that includes timely security and patch updates.
- Install a Java runtime via
`dmg/rpm/msi`
from[https://www.azul.com/downloads](https://www.azul.com/downloads). - Install/build Java via homebrew
- Brew
`install OpenJDK@<java version number>`
- Brew
Don’t:

- Visit java.com and install any versions referenced therein.
## Addressing Java Packaged With Applications
This scenario requires some care and possible communication with the software vendor. There are applications that legitimately include a Java JRE or JDK as part of their installation, such as low-power/IoT devices using Java Compact Profile, Virtual Machine Images used in network-restricted environments, etc. In these cases, it is important to properly understand the application’s support requirements and license liability.

In most instances, vendors today will support their applications running on a TCK (Technology Compatibility Kit)-certified [build of OpenJDK](https://thenewstack.io/this-week-in-programming-microsoft-jumps-back-into-java-with-openjdk-build-preview/). If a vendor does certify their software as OpenJDK compatible, it is sufficient to pick any OpenJDK distribution that you want. Vendors may certify with a particular distribution, but that is probably due to convenience or a lack of understanding on their part. The vendor should consider their testing as being against the OpenJDK specification, which means any certified OpenJDK would be sufficient. If a vendor uses classes specific to a distribution, they should document the requirement specifically.

In some rare cases, a vendor takes the position that using any JRE other than the prescribed Oracle JRE will invalidate their support contract. In cases such as these, you should request written documentation of the above requirement along with a statement that the use of Oracle Java for this purpose in your environment does not subject your organization to the Oracle All-Employee License Model.

Do:

- Investigate each application that meets this situation. Visiting the vendor’s website or contacting their support department is a good start.
- Request instructions for migrating applications to an OpenJDK. Don’t expect too much trouble with the migration process, particularly for more recent versions of Java.
Don’t:

- Ignore this situation. Without an explicit statement absolving you of any license liability to Oracle, using Oracle JDK with a third-party application exposes you to licensing risk.
## Mitigating JavaScript or Enablement from External Sites
All it takes is a simple line of script to create an HTML button that enables a user to download Oracle JDK with one click — and create a new license liability. While these scenarios are usually outside your scope of control, there are a few proactive steps you can take.

Do:

- Educate your users on the approved Java options available to them.
- Make the appropriate downloads easily available.
Don’t

- Allow users to continue to use Java downloaded from java.com or oracle.com.
## General Recommendations
Preventing ongoing Oracle Java licensing risk is doable, but it should be clear by now that a perimeter strategy alone is not the best approach. It needs to be combined with a mitigation strategy and reasonable vigilance.

- Monitor Oracle Java and remediate any new Oracle Java instances as soon as possible. Replacing the Oracle JDK with an OpenJDK distribution is not that difficult and introduces little compatibility, stability or security risk. Your new Java (not application) vendor should also be able to provide guidance for this type of effort.
- If you have a real-time desktop management solution available (like BeyondTrust, CyberArc, etc.), use it to disable key Java installers, executables and launchers (
`java.exe`
,`javaw.exe`
,`javaws.exe`
,`jp2launcher.exe`
, etc.). - Use Group Policies on Windows where possible. It is a more reliable way to control whether Java can run or be installed and can be enforced centrally through companywide policies.
- Use file system scanners or inventory tools to look beyond installation registries. Tools like Flexera or Microsoft Endpoint Configuration Manager, formerly known as System Center Configuration Manager (SCCM) can be configured to run periodic full file system scans.
- Azul offers customers access to our Azul Migration Advisory Tools, a set of discovery and migration (shell) script examples that our team uses when we assist with migration efforts.
## Conclusion
Due to the pervasive nature of Java and recent changes to Oracle’s Java license model(s), it is important to understand your risk and exposure if you continue to allow Oracle Java to be run in your environment.

Avoiding costly license liability requires ongoing vigilance and triage. The above guidance is provided as a “best effort” approach, and I am sure there are other mechanisms that could introduce Oracle Java back into your environment.

Please feel free to comment and add any findings that you think could affect others, and we will do our best to provide our suggestions for how to triage. If you would like further details or have concerns that are better not shared on a public forum, please contact migration@azul.com and we will get back to you directly.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)