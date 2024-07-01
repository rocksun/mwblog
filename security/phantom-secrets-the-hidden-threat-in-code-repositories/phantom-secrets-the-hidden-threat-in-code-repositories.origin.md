# Phantom Secrets: The Hidden Threat in Code Repositories
![Featued image for: Phantom Secrets: The Hidden Threat in Code Repositories](https://cdn.thenewstack.io/media/2024/06/0fa327ff-getty-images-bwvuu8mlx9w-unsplash-1024x683.jpg)
The increasingly complex nature of the modern software development environment has given rise in recent years to the growing problem of programmers leaving [secrets exposed in code repositories](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/), making them easy pickings for cybercriminals.

[GitGuardian](https://www.gitguardian.com/) has been tracking the issue for several years, putting in stark detail the climbing number of exposed [secrets](https://thenewstack.io/managing-secrets-in-your-devops-pipeline/) found in [GitHub](https://thenewstack.io/githubs-2fa-push-boosts-adoption-among-developers/) every year in its annual State of Secret Sprawl reports. The latest report, released this year, showed that the company [detected almost 12.8 million new secrets](https://www.gitguardian.com/state-of-secrets-sprawl-report-2024) in GitHub commits in 2023, almost 3 million more than the year before.
In 2020, in the first year of the reports, the number was 3 million. In 2023, 8 million of the 1.1 billion commits GitGuardian scanned exposed at least one secret.

Researchers from [Aqua Security](https://thenewstack.io/aqua-security-uncovers-major-kubernetes-attacks/) last week added to the growing concern, saying they found some secrets — [API tokens](https://thenewstack.io/why-your-api-keys-are-leaving-you-vulnerable-to-attack/), [credentials](https://thenewstack.io/unused-credentials-key-culprits-in-cloud-attacks-study-says/) and [passkeys](https://thenewstack.io/stytch-takes-the-hassle-out-of-passkey-authentication/) – that have been exposed for years. They also discovered that hard coding one secret into code only once may permanently expose it, even after it is supposedly removed.

Even more worrying: most scanning methods miss these “phantom secrets,” with the researchers finding that almost 18% of secrets in [Git repositories](https://thenewstack.io/create-a-local-git-repository-on-linux-with-the-help-of-ssh/) might be overlooked.

“We uncovered major secrets, including credentials to cloud environments, internal infrastructures and telemetry platforms, exposed on the internet,” [Yakir Kadkoda](https://www.linkedin.com/in/yakir-kadkoda/) and [Ilay Goldman](https://www.linkedin.com/in/ilaygoldman/), researchers with Aqua’s security unit, Aqua Nautilus, [wrote in a report](https://www.aquasec.com/blog/undetected-hard-code-secrets-expose-corporations/). “Through a variety of Git-based processes whose impact is not well understood by developers and AppSec professionals, and [source code management (SCM)](https://thenewstack.io/5-version-control-tools-game-developers-should-know-about/) platforms’ behavior, secrets remain exposed even after considered removed.”

## Developers and Their Secrets
Developers for years have been hard coding secrets into software for faster configuration and other legitimate purposes. The rise of cloud computing and the increasingly complex and decentralized nature of programming today, with open source and third-party code and [code reuse](https://thenewstack.io/coding-from-scratch-creates-new-risks/) becoming the norm, have made programming faster but also opened it up to increasing cyberthreats and [supply chain risks](https://thenewstack.io/fortifying-the-software-supply-chain/).

Myriad security vendors have sounded the alarm about exposing secrets, with Kadkoda and Goldman writing that they for years have “been educating developers not to hard-code secrets into their code.” In addition, the global market for secrets management software is expected to rise rapidly, with one predication calling for it to jump from $67 billion last year to [$104.6 billion by 2031](https://www.linkedin.com/pulse/secret-management-software-market-size-2031-overview-iqjaf/).

The problem with phantom secrets is due in large part to the way SCM systems, such as GitHub, Bitbucket, and [GitLab](https://about.gitlab.com/?utm_content=inline+mention), save deleted or updated code commits in their Git-based infrastructures, according to the Aqua Nautilus team. That can mean even a single secret used in code or a secret that is thought to have been deleted can remain exposed.

For the report, the Aqua researchers scanned the top 100 organizations on GitHub, which included more than 52,000 publicly available repositories.

“During our research, we uncovered some significant secrets, including gaining access to the complete cloud environments of some of the biggest organizations in the world, infiltrating the internal fuzzing infrastructure of sensitive projects, accessing telemetry platforms, and even obtaining access to network devices, Simple Network Management Protocol (SNMP) secrets, and camera footage of Fortune 500 companies,” Kadkoda and Goldman wrote. “These discoveries could lead to significant attacks on the impacted organizations.”

## Mozilla and Cisco as Cautionary Tales
In one case, the researchers uncovered an API token for Mozilla’s FuzzManager, an internal tool used to collect and analyze [fuzzing](https://thenewstack.io/api-fuzzing-what-is-it-and-why-should-you-use-it/) data to find security vulnerabilities. The token gave them access to Mozilla’s internal fuzzing data, which is usually kept secret so that bad actors can’t exploit unpatched bugs. In another, they found privileged API tokens for Cisco’s Meraki Dashboard, which lets organizations manage their networks. Attackers that find such tokens can take control of network resources and access sensitive information, including SNMP secrets and camera footage.

In another case, they found an Azure service principal token of a large healthcare company in a Git commit. The token gave the holder high access to the company’s [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure resources, including its internal [Azure Kubernetes Service](https://thenewstack.io/install-cloud-foundry-on-azure-kubernetes-clusters/) and Azure Container Registry. A malicious actor with the token could take control of the company’s [Kubernetes](https://thenewstack.io/kubernetes/) clusters.

All the organizations with exposed secrets were notified and the secrets revoked.

Still, the problem of phantom secrets remains. Aqua scanned the repositories using two tools — [git clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) and [git clone –mirror](https://git-scm.com/docs/git-clone) — in mirrored versions of the repositories and found they missed almost 18% of secrets. The problem is commits remain accessible through “cache views” on the SCM, so any secret removed from cloned and mirrored versions of a repository can still be available to anyone who knows the commit hash.

## Getting to the Cached Views
The researchers outlined four strategies for retrieving cached view commits, from brute forcing commit hashes and using REST API endpoints to looking at the GUI of pull requests and using a GitHub historical dataset.

Organizations will have to address the phantom secrets problem if they want to stem the cyber-risks to developers, according to cybersecurity experts.

“This issue is essential as it points to a fundamental flaw in how secrets are managed in Git-based systems, which can impact numerous organizations,” [Eric Schwake](https://www.linkedin.com/in/ericschwake/), director of cybersecurity strategy at [Salt Security](https://salt.security/), told The New Stack. “Exposure to secrets like API tokens and credentials can lead to serious consequences such as unauthorized access, data breaches and financial losses. The persistent nature of ‘phantom secrets’ even after deletion or updates worsens the problem, posing a long-term risk. Because APIs are the foundation of modern applications, they are becoming more of a target for attackers.”

[Sarah Jones](https://www.linkedin.com/in/sarah-jones-209b9690/), cyberthreat intelligence research analyst at [Critical Start](https://www.criticalstart.com/), said a multilayered approach to mitigating such risks will be important for organizations.
“Developers require comprehensive training on secure coding practices, proper secret management using dedicated tools and the criticality of preventing accidental leaks,” Jones told The New Stack. “Automated scanning tools can identify secrets before they are pushed to public repositories, with code review processes adding an additional layer of security. Furthermore, organizations should implement dedicated secret management solutions to ensure secure storage and granular access control.”

## Malicious Actors Love Developers
Both Schwake and Jones said developers will continue to be an attractive target for threat actors because of their access to sensitive information and systems and the expanded attack surface due to the growing use of open source code and [cloud native development](https://thenewstack.io/cloud-native/). Also, as the practice of [DevSecOps](https://thenewstack.io/5-tips-for-developer-friendly-devsecops/) is integrated into the development lifecycle, attackers will continue to shift their focus to exploiting vulnerabilities in the development process itself, according to Schwake.

“However, the situation is gradually improving,” he said. “As security breaches become more frequent and their impact more severe, developers are starting to recognize the importance of security. Organizations should invest in security training programs and integrate security tools into development workflows. Adopting DevSecOps practices also fosters a culture of shared responsibility for security, encouraging developers to take ownership of security in their work.”

He added that “we are also seeing increased importance in posture governance across the entire API development lifecycle to try and prevent security issues as soon as possible.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)