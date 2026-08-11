⁠**Security researchers this week disclosed** an npm supply-chain attack affecting more than 400 packages, including projects connected to Keyv and Cacheable. The attackers used stolen developer credentials to publish malicious versions.

This incident appears to point to a trend in software security: Attackers are going after the developers and workflows already trusted to publish.

> Attackers are going after the developers and workflows already trusted to publish.

## Worm spreads through credentials

According to [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/), the malicious releases contained a variant of the Mini Shai-Hulud credential-stealing worm as they bypassed source repositories as they spread, and began with stolen maintainer credentials. Once inside, the worm searched developer machines and CI environments for any other credentials it could use.

When it found an active npm publishing token, it downloaded the latest version of every package the account could access, injected a malicious preinstall lifecycle hook, bumped the patch number and published the infected versions. Because npm runs preinstall hooks automatically before installation finishes, the malware could start running on developer workstations and [CI runners](https://thenewstack.io/anthropic-mendral-cicd-acquihire/) before application tests or security checks began.

> Because npm runs preinstall hooks automatically before installation finishes, the malware could start running on developer workstations and CI runners before application tests or security checks began.

## Preinstall hooks enable silent execution

In CI environments, it stayed connected to the active job, where it could reach workflow secrets, runner credentials, and publishing permissions. On workstations, it could continue running in the background and inject startup files into Visual Studio Code and [Claude](https://thenewstack.io/anthropic-claude-containment-failure/), including .vscode/tasks.json and .claude/settings.json.

The attack exposed a weakness in trusted publishing, highlighting that malware running inside an authorized workflow can request its own short-lived token instead of stealing a long-lived publishing credential. The resulting malicious package can even carry valid [provenance attestations](https://docs.npmjs.com/generating-provenance-statements/).

## Provenance doesn’t guarantee integrity

This campaign shows how quickly an attack can move from a developer’s machine into the rest of the release process. Shared CI systems add another opening because GitHub Actions can reuse dependencies across workflow runs. GitHub’s [documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) warns that those cached files are not signed or verified.  
  
The lesson for engineering teams is to keep publishing access away from the parts of the pipeline that install dependencies. The principle of restricting what automated processes can do echoes [a bigger trend in how the industry is rethinking blanket permissions for AI-assisted coding](https://thenewstack.io/microsoft-copilot-token-budgets/).

> This campaign shows how quickly an attack can move from a developer’s machine into the rest of the release process.

## Isolate publishing from dependency installation

Microsoft recommends upgrading to [npm CLI 12](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/), pinning known-good versions and using [min-release-age](https://docs.npmjs.com/cli/v11/using-npm/config) to give teams time to review new releases before they are installed.

Rotating the stolen token [may not be enough](https://thenewstack.io/apple-ai-bug-report-caps/) once a compromised package has run its lifecycle scripts. Teams may also need to rebuild affected machines and base images, clear shared caches and recreate software artifacts from trusted dependencies.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)