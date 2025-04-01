# How To Centralize Kubernetes Secrets Management With Vault
![Featued image for: How To Centralize Kubernetes Secrets Management With Vault](https://cdn.thenewstack.io/media/2025/03/6fac0638-centralize-kubernetes-secrets-management-vault2-1024x640.jpg)
Managing secrets in [Kubernetes](https://thenewstack.io/kubernetes/) (K8s) environments is a critical yet often overlooked challenge. Many teams start by using K8s’ built-in secrets, only to realize later that they come with security and management limitations. Secrets such as database credentials, API tokens and private keys are fundamental to secure application operations, yet handling them incorrectly can expose entire systems to risks.

This post explores the challenges of managing secrets in K8s and why relying solely on built-in K8s secrets can introduce security risks and operational inefficiencies. It delves into the benefits of using a [centralized secrets management](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/) solution like HashiCorp Vault, highlights the advantages of integrating K8s clusters with Vault, and explains how the [Secrets Store Container Storage Interface (CSI) Driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver) simplifies secret retrieval without direct API calls. I’ll also share a practical architecture overview and best practices for scaling Vault across multiple clusters.

## The Challenge with K8s Secrets
By default, [K8s secrets](https://thenewstack.io/kubernetes-secrets-management-3-approaches-9-best-practices/) are stored unencrypted in etcd. The distributed key-value store that serves as K8s’ primary data storage system, etcd holds all cluster states and configurations, including deployments, services and secrets. This means that anyone with access to etcd or the K8s API server, which acts as the control plane for managing resources and handling requests from users and applications, can retrieve these secrets.

Additionally, secrets are frequently hardcoded into environment variables or configuration files, creating a maintenance nightmare when they need to be updated across multiple applications and clusters and increasing the risk of exposure and mismanagement.

A common pattern is storing secrets in ConfigMaps or embedding them in YAML files, but this approach introduces several problems:

**Lack of encryption:**K8s secrets are only Base64-encoded, not truly encrypted.**Limited access control:**Role-based access control (RBAC) policies in K8s don’t provide fine-grained control over who can access secrets.**No built-in audit trail:**It’s difficult to track who accessed or modified a secret.**Secret sprawl:**Secrets often get duplicated across multiple namespaces and applications.**Rotation challenges:**Without an automated system, rotating secrets requires manually updating multiple deployments.
Given these limitations, it’s clear that K8s secrets alone are not sufficient for secure secrets management at scale.

## Vault-Based Secrets Management
Instead of relying on K8s secrets, a more scalable and secure approach is to integrate K8s clusters with an external secrets store like HashiCorp Vault. This provides a single, centralized place for managing secrets across multiple clusters, ensuring that secrets are never stored in plain text within K8s.

A secrets store enables:

- Applications to retrieve secrets dynamically from Vault via API calls.
- No secrets are stored in K8s to eliminate exposure risks.
- Enforcement of access control policies, so only authorized services can access specific secrets.
- A single place (Vault) to make all updates, which automatically propagates to all clusters consuming the secret.
- Automatic secret rotation, reducing security risks and compliance burdens.
By centralizing secrets, teams reduce the risk of secrets leaking through misconfigurations or unauthorized access.

### Connecting K8s Clusters to Vault
To integrate [Vault with K8s](https://thenewstack.io/hashicorp-vault-operator-manages-kubernetes-secrets/), a common approach is to use the K8s authentication method in Vault. This allows workloads running inside K8s to authenticate with Vault without requiring static credentials.

The process includes:

- Deploying Vault in a highly available setup.
- Enabling K8s authentication in Vault, mapping K8s service accounts to specific secrets access policies.
- Configuring workloads to retrieve secrets dynamically using Vault’s API instead of storing them in environment variables or ConfigMaps.
- Using Vault Agent or the Secrets Store CSI Driver to automatically inject secrets into running pods at runtime.
### Synchronizing Secrets Across Clusters
In environments with multiple K8s clusters, managing secrets centrally in Vault offers a significant advantage. Instead of manually updating secrets across different clusters, teams can store secrets once in Vault and allow all clusters to retrieve them dynamically.

For example, consider an organization running five K8s clusters, each hosting different applications but sharing common environment variables. By using Vault, any update to a secret — such as a database password — can be made in Vault, and all clusters will automatically retrieve the updated version without requiring manual redeployment of applications.

### Avoiding Direct Vault API Calls
A key consideration when using Vault is avoiding direct API calls from applications. While applications can retrieve secrets directly from Vault using its software development kit (SDK), this approach introduces several challenges:

**Code modifications:**Applications must include Vault logic, leading to dependencies and vendor lock-in.**Performance overhead:**Every API request to Vault adds latency and can introduce rate-limiting issues.**Handling Vault credentials:**Applications need credentials to authenticate with Vault, creating another secrets management challenge.
A better approach is using the Secrets Store CSI Driver, which allows K8s to mount secrets from Vault into pods as files. This method decouples applications from Vault and ensures secrets are injected securely into the container’s filesystem without modifying application code.

## Demonstrating Vault + Secrets Store in Action
A practical implementation of Vault with K8s uses the Secrets Store CSI Driver along with Vault’s integration. The architecture consists of:

**Vault server:**Stores and manages secrets centrally.**Vault CSI daemonset:**Retrieves secrets from Vault and syncs them with K8s.**Secrets Store CSI Driver DaemonSet:**Acts as an abstraction layer, enabling secrets from various providers (e.g., Vault, AWS Secrets Manager, Azure Key Vault) to be injected into pods.**SecretProviderClass CustomResourceDefinition (CRD):**Defines which secrets to fetch from Vault and how they should be exposed to workloads.
## Live Secret Updates with Vault + K8s
One key advantage of this setup is updating secrets dynamically. If a secret changes in Vault, it can be automatically propagated to running workloads. However, some additional configurations may be required for seamless updates:

**Rolling updates:**Since pods don’t automatically reload secrets, a rolling restart of workloads ensures updated secrets are picked up.**Sidecar approach:**Some teams use a Vault sidecar to refresh secrets dynamically without requiring pod restarts.
When deploying Vault in large-scale K8s environments, teams must carefully balance security, performance and operational efficiency. High availability (HA) is essential, requiring Vault to be deployed in HA mode with robust backup and failover mechanisms to prevent service disruptions. Performance optimization is equally critical, particularly for the Secrets Store CSI DaemonSet, which must be configured with appropriate resource limits to handle high loads efficiently.

Following the principle of least privilege ensures that applications and users can access only the secrets they require, minimizing exposure risks. Additionally, enabling audit logging in Vault provides visibility into secrets access and modifications, helping organizations maintain compliance and quickly detect unauthorized activity. By addressing these considerations, teams can implement a scalable, resilient and secure secrets management strategy for their K8s workloads.

## K8s Secrets Management: More Than Just a Best Practice
Securing secrets in K8s is more than just a best practice — it’s a necessity for protecting sensitive data and maintaining operational resilience. While K8s’ built-in secrets management offers convenience, it lacks the encryption, fine-grained access control and lifecycle automation needed for enterprise-grade security. By centralizing secrets in Vault, organizations gain a robust, scalable solution that simplifies secrets distribution, enforces security policies and enables automated rotation.

When paired with the Secrets Store CSI Driver, teams can seamlessly integrate secure secrets retrieval into their K8s workloads without introducing complexity or direct dependencies on Vault. As organizations scale across multiple clusters, a well-architected approach to secrets management minimizes human error and enables a more resilient infrastructure by reducing security risks and improving operational efficiency.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)