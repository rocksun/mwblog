# GitOps: How We Integrate a New Service in Under 1 Hour for 25 Clusters!
## Bootstrapping Otterize at Scale with GitOps through Argo CD
Fun Fact:we only needed under an hour to integrate the new service, but it took usonlyover four months to purchase the license. So, your setup can be as fast as you want, but if your other procedures are the bottleneck, it doesn’t really matter when bringing a new tool into the game!This isn’t about placing blame; there are various reasons for this, including purchasing processes and data protection considerations.

Here you can see the big-picture we tried to achieve and succeeded (we believe at least)!

Why can’t it be easy, and why did it take a whole hour? Trust me, I ask myself that every single time too…!

When adding a new service to your tech stack, the biggest challenge is figuring out how to integrate it seamlessly and at scale without sacrificing performance or scalability. Why is this so tough? Well, every tool comes with its own quirks — especially when you’re dealing with a mix of SaaS, self-hosted solutions, and the need to securely manage credentials and tokens to establish a secure connection.

We faced this exact challenge with [Otterize](https://otterize.com/). And we’re not just talking about deploying the [Helm chart](https://github.com/otterize/helm-charts). We had to think through the entire setup — connecting to the SaaS, deploying controllers, and more.

**What We Had to Work With:**
Since we’re all about efficiency, we wanted to keep things as simple as possible. Why? Because manually clicking through setup processes (a.k.a. [ClickOps](https://blog.equinix.com/blog/2022/12/01/what-is-clickops-and-how-can-you-prevent-it/)) is a recipe for mistakes and inconsistencies. Plus, let’s be honest — we’re a bit lazy. So, the goal was to automate everything we could.

So enough of the introduction, let’s move on to the next step and get an overview of what we actually want to set up.

# The Setup
Here’s what we aimed to achieve:.

**Create an Organization**: Set up the organization in Otterize.**Invite Users (2.2)**: Get the right people into the organization.**Set Up the Environment (2.1)**: Create the necessary environment for integration.**Create Integration with Kubernetes**: Connect to the cloud solution using`clientId`
and`clientSecret`
.**Secure Credentials**: Push the`clientId`
and`clientSecret`
to Azure Key Vault.**Deploy Everything (establish Connection)**: Use[Argo CD](https://argo-cd.readthedocs.io/en/stable/)to deploy the Otterize stack, the External Secrets Operator, and any related secrets and
A Quick Note on the Client ID: As of August 16, 2024, the

`clientId`
cannot be directly referenced from a secret. So, for now, we manually add the`clientId`
to the cluster's values.
# How We Did It: Step-by-Step on the CLI
## 1. Create the Organization
We started by creating an organization using the Otterize CLI:

`otterize organization create --format json `
Output looks like:

[
{
"id": "org_h....",
"name": "Cryptocurrency Crusader Otters"
}
]
Afterward, we renamed it to match our cluster and stage:

`otterize org update "org_..." --name "cluster-name-stage"`
ID NAME IMAGE URL
Organization updated
Organization renamed to: cluster-name-stage
## 2.1 Create the Environment
Next, we created the environment:

`otterize environment create --org-id "org_fcb967hrqz" --name test3 --labels test=true,env=test,env2=test2 --format json `
Output looks like:

`[`
{
"appliedIntentsCount": 0,
"id": "env_ubpiqq7odl",
"labels": [
{
"key": "env",
"value": "test"
},
{
"key": "env2",
"value": "test2"
},
{
"key": "test",
"value": "true"
}
],
"name": "test2",
"namespaces": [],
"serviceCount": 0
}
]
## 2.2. Invite Users to the Organization
We sent out invitations to our team members:

`otterize invites --org-id "org_..." create --email "artem.lajko@...."`
Output looks like:

`ID EMAIL ORGANIZATION ID INVITER USER ID STATUS CREATED AT ACCEPTED AT`
inv_fn3evo2p7p artem.lajko@ org_ usr_u PENDING 2024-08-15
Invite sent to artem.lajko@
## 4. Integrate with Kubernetes
Then, we created the Kubernetes integration:

`otterize integrations create --org-id "org_...." kubernetes --env-id env_6u... --name test-k8s --format json`
Output looks like:

Caution: this CLI was built with a different version/revision of the Otterize Cloud API.
Please run otterize version for more info.
[
{
"cluster": {
"id": "cluster_q..."
},
"components": {
"credentialsOperator": {
"status": {
"type": "NOT_INTEGRATED"
},
"type": "CREDENTIALS_OPERATOR"
},
"intentsOperator": {
"configuration": {
"awsIAMPolicyEnforcementEnabled": false,
"databaseEnforcementEnabled": false,
"egressNetworkPolicyEnforcementEnabled": false,
"globalEnforcementEnabled": false,
"istioPolicyEnforcementEnabled": false,
"kafkaACLEnforcementEnabled": false,
"networkPolicyEnforcementEnabled": false,
"protectedServices": [],
"protectedServicesEnabled": false
},
"status": {
"type": "NOT_INTEGRATED"
},
"type": "INTENTS_OPERATOR"
},
"networkMapper": {
"status": {
"type": "NOT_INTEGRATED"
},
"type": "NETWORK_MAPPER"
}
},
"credentials": {
"clientId": "cli_...",
"clientSecret": "df5..."
},
"defaultEnvironment": {
"id": "env_6u..."
},
"id": "int_...",
"name": "clsuter-name-stage",
"organizationId": "org_...",
"type": "KUBERNETES"
}
]
## 5. Push Credentials to Azure Key Vault
We securely stored the credentials in Azure Key Vault:

`az keyvault secret set --vault-name kv... --name "otterize-cloud-client-secret" --value ".." >/dev/null`
az keyvault secret set --vault-name kv... --name "otterize-cloud-client-id" --value ".." >/dev/null
## 6. Update Helm Chart Values
Finally, we updated the Helm chart with the necessary credentials:

` otterizeCloud:`
certificateProvider: otterize-cloud
credentials:
# fill clientId and clientSecret in order to connect to Otterize Cloud
clientId: "cli_..."
clientSecretKeyRef:
secretName: otterize-cloud-credentials-secret-key
secretKey: otterize-cloud-client-secret
We used a Python templater to automatically insert the `clientId`
into our values.

See if everything has worked as expected:

Of course, we didn’t do this manually — we have a templater that automates the entire process. After running the script, everything was deployed smoothly, without a hitch.

And here you can see the script (without templating), but what comes out at the end and is executed.

#!/bin/bash
# Set environment variables
NAME="<cluster-name-stage>"
STAGE="<stage>"
SUBSCRIPTION="<...>"
KEY_VAULT_NAME="<...>"
LABELS="cluster=<>, env=<>,..."
OTTERIZE_CLOUD_INVITE_USERS="braveone@e-mail.com,lazy@e-mail.com,..."
GROUP_ID="..." #Azure AD Group (Platform Team)
# Function to set the subscription
set_subscription() {
az account set --subscription $SUBSCRIPTION
if [ $? -ne 0 ]; then
echo "Failed to set Azure subscription."
exit 1
fi
}
# Step 1: Create the organization and save the ID in ORGA_ID
ORGA_ID=$(otterize organization create --format json | jq -r '.[0].id')
if [ -z "$ORGA_ID" ]; then
echo "Failed to create organization."
exit 1
fi
echo "Organization ID: $ORGA_ID"
# Step 2: Rename the organization with the provided NAME
otterize org update "$ORGA_ID" --name "$NAME"
if [ $? -ne 0 ]; then
echo "Failed to rename organization."
exit 1
fi
echo "Organization renamed to: $NAME"
# Step 3: Iterate over OTTERIZE_CLOUD_INVITE_USERS, retrieve user names, format the email in lowercase, and send invitations
IFS=',' read -ra ADDR <<<"$OTTERIZE_CLOUD_INVITE_USERS"
for email in "${ADDR[@]}"; do
email=$(echo "$email" | xargs) # Trim any leading/trailing whitespace
# Get the user's first and last name from Azure AD
user_info=$(az ad user show --id "$email" --query '{firstName:givenName,lastName:surname}' --output tsv)
# Extract the first name and last name
first_name=$(echo "$user_info" | awk '{print $1}')
last_name=$(echo "$user_info" | awk '{print $2}')
# Construct the new email format and convert it to lowercase
formatted_email=$(echo "${@hpa.hamburg.de">first_name}.${last_name}@hpa.hamburg.de" | tr '[:upper:]' '[:lower:]')
# Send invitation using the formatted email
otterize invites --org-id "$ORGA_ID" create --email "$formatted_email"
if [ $? -ne 0 ]; then
echo "Failed to send invite to $formatted_email."
else
echo "Invite sent to $formatted_email."
fi
done
# Step 3b: Invite users from an Azure AD group by ID
group_emails=$(az ad group member list --group "$GROUP_ID" --query "[].mail" -o tsv | tr '[:upper:]' '[:lower:]')
for email in $group_emails; do
if [ -n "$email" ]; then
# Send invitation using the email directly from the group
otterize invites --org-id "$ORGA_ID" create --email "$email"
if [ $? -ne 0 ]; then
echo "Failed to send invite to $email."
else
echo "Invite sent to $email."
fi
fi
done
# Step 4: Create the environment and save the ID in ENV_ID
ENV_ID=$(otterize environment create --org-id "$ORGA_ID" --name $STAGE --labels "$LABELS" --format json | jq -r '.[0].id')
if [ -z "$ENV_ID" ]; then
echo "Failed to create environment."
exit 1
fi
echo "Environment ID: $ENV_ID"
# Step 5: Create the integration and save the CLIENT_ID and CLIENT_SECRET
CREDENTIALS=$(otterize integrations create --org-id "$ORGA_ID" kubernetes --env-id "$ENV_ID" --name "$NAME" --format json | jq -r '.[0].credentials | "clientID=\(.clientId)\nclientSecret=\(.clientSecret)"')
CLIENT_ID=$(echo "$CREDENTIALS" | grep "clientID=" | cut -d'=' -f2)
CLIENT_SECRET=$(echo "$CREDENTIALS" | grep "clientSecret=" | cut -d'=' -f2)
if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ]; then
echo "Failed to create integration or retrieve credentials."
exit 1
fi
# Step 6: Push the client ID and client secret to the Azure Key Vault
az keyvault secret set --vault-name "$KEY_VAULT_NAME" --name "otterize-cloud-client-id" --value "$CLIENT_ID" >/dev/null
if [ $? -ne 0 ]; then
echo "Failed to store Client ID in Azure Key Vault."
exit 1
fi
az keyvault secret set --vault-name "$KEY_VAULT_NAME" --name "otterize-cloud-client-secret" --value "$CLIENT_SECRET" >/dev/null
if [ $? -ne 0 ]; then
echo "Failed to store Client Secret in Azure Key Vault."
exit 1
fi
echo "Client ID and Client Secret successfully stored in Azure Key Vault."
# Output the Client ID for the integration
echo "The Client ID for the integration is: $CLIENT_ID"
and this is what the end result looks like:

**Is this ideal?** No, we’d prefer the clientId to be referenced directly from the Secret.
**Is that truly ideal?** No, the best solution would be a [Terraform provider](https://registry.terraform.io/browse/providers) to streamline the workflow like this:
# Conclusion
Thanks to GitOps with Argo CD and tools like External Secrets, we were able to streamline our setup and keep things lazy (in the good, smart way). You’ve now seen how we integrated Otterize at scale into our workflow.

But wait…

[meme](https://hicentrik.com/meme-marketing-guide-memevertising-2021/)]
what is Otterize and Otterize Cloud? If you’re curious, I explained that in detail in a previous blog post:

⭐️ [Kubernetes — Automate workload IAM on Azure with Otterize](https://medium.com/itnext/kubernetes-automate-workload-iam-on-azure-with-otterize-860faa221eac) ⭐️

You also have a great collection of Blogs here:

# Contact Information
Got questions, want to chat, or just keen to stay connected? Skip the Medium comments and let’s connect on [LinkedIn](http://www.linkedin.com/in/lajko) 🤙. Don’t forget to subscribe to the [Medium Newsletter](/@artem_lajko/subscribe) so you never miss an update!