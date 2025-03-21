# Simplifying Secret Management in Kubernetes with AWS and External Secrets Operator
![Secrets Management in Kubernetes with AWS and External Secrets Operator](/content/images/size/w2000/2024/11/kb-ima--3-.png)
Managing sensitive information, like passwords and API keys, in Kubernetes can be challenging. You want to keep your secrets secure while still making them available to your applications.

In this guide, we'll walk you through how to connect AWS Secrets Manager with your Kubernetes cluster using the External Secrets Operator. By the end, you’ll have a straightforward setup to handle secrets efficiently and securely.

For this tutorial, **OpenID Connect (OIDC)** is a key requirement. It helps Kubernetes service accounts communicate securely with AWS IAM roles.

This connection allows the External Secrets Operator to fetch secrets from AWS Secrets Manager. If your cluster doesn’t already have OIDC set up, don’t worry—we’ll show you how to get started.

## Before going into the implementation part, let's understand how the External Secrets Operator functions.
### How It Works
The External Secrets Operator is a Kubernetes controller that integrates external secret management systems like AWS Secrets Manager with Kubernetes. Here's the basic flow:

**External Secrets Definition**: You define an`ExternalSecret`
resource in Kubernetes, specifying which secrets you want to fetch from AWS Secrets Manager.**Operator Syncs Secrets**: The operator watches for`ExternalSecret`
resources. When it finds one, it fetches the specified secrets from AWS Secrets Manager.**Creates Kubernetes Secrets**: The operator then creates or updates a Kubernetes`Secret`
resource with the fetched data.**Applications Access Secrets**: Your applications can then access these secrets as they would any other Kubernetes secret, using environment variables or volume mounts.
![](https://www.kubeblogs.com/content/images/2024/11/image-8.png)
### Why This Approach?
**Security**: Secrets remain in AWS Secrets Manager, which is designed for secure secret storage.**Consistency**: Centralizes secret management across multiple clusters and environments.**Automation**: Automatically syncs secrets when they change, reducing manual updates.
### Components Involved
**AWS Secrets Manager**: Stores your secrets securely in AWS.**External Secrets Operator**: Runs in your Kubernetes cluster, syncing secrets from AWS.**Service Account with IAM Role**: Allows the operator to authenticate with AWS using IAM roles, leveraging Kubernetes service accounts.
### Authentication Flow
**Service Account Authentication**: The operator uses a Kubernetes service account annotated with the IAM role ARN.**IAM Role Assumption**: Through the OIDC provider, AWS trusts the service account to assume the IAM role.**Access Secrets Manager**: With the IAM role's permissions, the operator fetches secrets from AWS Secrets Manager.
By understanding this flow, you can see how all the parts work together to make secret management secure and efficient.

Now, let’s move forward with a step-by-step tutorial to set this up in your cluster.

## Step 1: Set Up the OIDC Identity Provider
First, we'll set up the OpenID Connect (OIDC) identity provider for our EKS cluster. This will allow Kubernetes service accounts to securely assume AWS IAM roles.

### Create an EKS Cluster
If you haven't already, create an EKS cluster. AWS automatically sets up an OIDC identity provider for your cluster during this process.

![](https://www.kubeblogs.com/content/images/2024/11/image-9.png)
**Note**: If you already have an EKS cluster with OIDC configured, you can skip this part.
### Add an Identity Provider (If Not Already Created)
**Navigate to the AWS IAM Console**: Go to the IAM service in the AWS Management Console.**Select "Identity Providers"**: From the left-hand menu.**Add Provider**: Click on "Add provider".**Provider Type**: Choose**OpenID Connect (OIDC)**.**Provider URL**: Paste the OIDC URL from your EKS cluster.**Audience**: Typically, this is`sts.amazonaws.com`
. This links your EKS cluster with AWS IAM.**Complete the Setup**: Review your settings and click**Add provider**.
![](https://www.kubeblogs.com/content/images/2024/11/image-10.png)
*Tip: Ensure the Provider URL matches your cluster's OIDC URL. This step is crucial for the integration to work smoothly.*
## Step 2: Create an IAM Role Using Web Identity
Now, we'll create an IAM role that our Kubernetes service account can assume to access AWS Secrets Manager.

### Navigate to IAM Roles
**Go to the IAM Service**: In the AWS Management Console.**Select "Roles"**: From the left-hand menu.**Click "Create role"**.
### Select Trusted Entity Type
**Choose "Web identity"**under "Select trusted entity".**Select Identity Provider**: Choose the OIDC provider you set up earlier.**Audience**: Enter`sts.amazonaws.com`
or the specific audience value you used.
![](https://www.kubeblogs.com/content/images/2024/11/image-11.png)
### Attach Permissions Policies
**Search for "SecretsManager"**in the policies.**Select "SecretsManagerReadWrite"**: This allows read and write access to secrets.
![](https://www.kubeblogs.com/content/images/2024/11/image-12.png)
### Modify the Trust Relationship
After creating the role:

**Navigate to the Role**: Click on the role you just created.**Go to the "Trust relationships" tab**.**Click "Edit trust policy"(**Before):Open 074e0aad-2909-4d47-a586-2e7d69baaf33-20241118-102250.jpeg
![](https://www.kubeblogs.com/content/images/2024/11/image-13.png)
*Note: Replace *`region-code`
* and the OIDC ID with your own values.*
**Naming Convention**: The`sub`
value follows the format`system:serviceaccount:<namespace>:<service-account-name>`
. Make sure the namespace and service account name match exactly.
After:
![](https://www.kubeblogs.com/content/images/2024/11/image-14.png)
## Step 3: Install the External Secrets Operator
Before we configure the YAML files, we'll install the External Secrets Operator using Helm.

### Install Using Helm
**Add the Helm Repository**:
`helm repo add external-secrets https://charts.external-secrets.io`
**Install the Operator**:
`helm install external-secrets \ external-secrets/external-secrets \ -n external-secrets \ --create-namespace`
*Alternatively, you can refer to the **External Secrets Operator documentation** for other installation methods.*
## Step 5: Configure Kubernetes Manifests
Now, we'll create the necessary Kubernetes YAML files to set up the service account, secret store, and external secret.

### Create `service-account.yaml`
This service account will be used by the External Secrets Operator to access AWS Secrets Manager.

![](https://www.kubeblogs.com/content/images/2024/11/image-15.png)
```
apiVersion: v1
kind: ServiceAccount
metadata:
name: service-account-external-secrets-operator
namespace: external-secrets
annotations:
eks.amazonaws.com/role-arn: "arn:aws:iam::12858755912:role/SecretsManager" # Replace with your Role ARN
```
### Create `secret-store.yaml`
Now that you've created a generic secret in your cluster, the next step is to reference this secret in your Secret Store configuration.

The Secret Store will allow your cluster to connect to AWS Secrets Manager using the IAM user credentials you've stored.

```
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
name: aws-secretsmanager # Name of the SecretStore
spec:
provider:
aws:
service: SecretsManager # Specify the AWS service as SecretsManager
region: us-east-1 # Specify the AWS region where your Secrets Manager is located
auth:
secretRef:
accessKeyIDSecretRef:
name: aws-secret-user-secret # Reference the Kubernetes secret containing the Access Key ID
key: access-key # Specify the key within the Kubernetes secret for Access Key ID
secretAccessKeySecretRef:
name: aws-secret-user-secret # Reference the Kubernetes secret containing the Secret Access Key
key: secret-access-key # Specify the key within the Kubernetes secret for Secret Access Key
```
*Ensure the region matches where your secrets are stored in AWS Secrets Manager.*
Now that you've configured the Secret Store, the next step is to create an `ExternalSecret`
. This resource will periodically fetch secrets from AWS Secrets Manager and store them in a Kubernetes secret.

![](https://www.kubeblogs.com/content/images/2024/11/image-16.png)
### Create `external-secret.yaml`
This specifies which secrets to sync from AWS Secrets Manager to Kubernetes.

```
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
name: my-external-secrets # Name of the ExternalSecret resource
spec:
refreshInterval: 10m # Defines the interval to refresh the secret data from AWS Secrets Manager
secretStoreRef:
name: aws-secretsmanager # References the SecretStore configured earlier
kind: SecretStore # Specifies the kind of the reference, which is SecretStore
target:
name: my-kubeops-db-secret # Name of the Kubernetes secret that will be created/updated with the fetched data
creationPolicy: Owner # Defines the ownership policy for the secret; Owner means the secret will be deleted if the ExternalSecret is deleted
dataFrom:
- extract:
key: DB-CREDENTIALS # The key in AWS Secrets Manager that holds the credentials
```
The `ExternalSecret`
will automatically create a new Kubernetes secret named `my-kubeops-db-secret`
. This secret will securely store all the values from the `DB-CREDENTIALS`
key in AWS Secrets Manager.

The values from AWS Secrets Manager are periodically fetched and kept up-to-date in the Kubernetes secret, ensuring your application always has the latest database credentials.Create `nginx-deployment.yaml`

Finally, we'll deploy an NGINX application that uses the secret we just created.

```
apiVersion: apps/v1
kind: Deployment
metadata:
name: nginx-deployment
namespace: external-secrets
spec:
replicas: 1
selector:
matchLabels:
app: nginx
template:
metadata:
labels:
app: nginx
spec:
containers:
- name: nginx
image: nginx
env:
- name: DB_PASSWORD
valueFrom:
secretKeyRef:
name: my-kubeops-db-secret
key: db-pass
```
In this deployment, we are securely injecting the database password (`DB_PASSWORD`
) into the NGINX container using Kubernetes secrets. Here's how it works:

- The
`valueFrom.secretKeyRef`
section references the Kubernetes secret named`my-kubeops-db-secret`
. - The
`key`
field,`db-pass`
, identifies the specific key in the secret, which contains the password value. - For example, if
`my-kubeops-db-secret`
contains a key-value pair like`db-pass: kubeops-consulting`
, the environment variable`DB_PASSWORD`
in the container will have the value`kubeops-consulting`
.
## Conclusion
And there you have it! You've successfully integrated AWS Secrets Manager with your Kubernetes cluster using the External Secrets Operator. Your applications can now securely access secrets without hardcoding them or managing them manually.

If you’re looking for an end-to-end observability solution and want to focus on your product while we handle the monitoring and logging infrastructure, feel free to reach out to **kubenine**. We deliver top-level observability solutions so you can focus on what matters most—your product.

By following these steps, you can simplify your CI/CD process while keeping your secrets secure. With this setup, managing sensitive information becomes hassle-free, and your Kubernetes environment stays safe and organized.