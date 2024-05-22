# Kubernetes RBAC Permissions You Might Not Know About, but Should
![Featued image for: Kubernetes RBAC Permissions You Might Not Know About, but Should](https://cdn.thenewstack.io/media/2024/05/b1762463-kubernetes-rbac-permissions-featured-image-1024x683.jpg)
Role-based access control (
[RBAC](https://thenewstack.io/3-frameworks-for-role-based-access-control/)) is the default access control approach in [Kubernetes (K8s)](https://thenewstack.io/kubernetes/). This model categorizes permissions using specific verbs to define allowed interactions with resources. Within this system, three lesser-known permissions —
escalate,
bind and
impersonate — can override existing role limitations, grant unauthorized access to restricted areas, expose confidential data or even allow complete control over a cluster. This article explains these potent permissions, offering insights into their functions and guidance on mitigating their associated risks.
## About RBAC Role and Verbs
If you are not already familiar with the
[key concepts of Kubernetes](https://roadmap.sh/kubernetes) RBAC, please refer to the [Kubernetes’ documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
However, I do need to briefly describe one important concept directly related to this article: role. This describes access rights to K8s resources within a specific namespace and the available operations. Roles consist of a list of rules. Rules include verbs — available operations for defined resources.
Here is an example of a role from the K8s documentation that grants read access to pods:
Verbs like
get,
watch and
list are commonly used. However, more intriguing ones also exist.
## Three Lesser-Known Kubernetes RBAC Permissions
For more granular and complex permissions management, the K8s RBAC has the following verbs:
**: Allows users to create and edit roles even if they don’t have initial permissions to do so.**
escalate
**: Allows users to create and edit role bindings and cluster role bindings with permissions they haven’t been assigned.**
bind
**: Allows users to impersonate other users and gain their privileges in the cluster or in a different group. Critical data can be accessed using this verb.**
impersonate
Below, you’ll learn about these verbs in more detail. But first, create a test namespace and name it
rbac:
|
1
|
kubectl create ns rbac
Then, create a test service account (SA) resource named
privsec in the
rbac namespace you just created:
|
1
|
kubectl -n rbac create sa privesc
You’ll use these throughout the rest of this tutorial.
### Escalate
By default, the Kubernetes RBAC API doesn’t allow users to escalate privileges by simply editing a role or role binding. This restriction works at the API level even if the RBAC authorizer is disabled. The only exception is if the role has the
escalate verb.
In the image below, the SA with only
update and
patch permissions can’t add a new verb to the role. But if you add a new role with the
escalate verb, it becomes possible.
![How adding the escalate verb to the role allows the user to change the role permissions and add a new verb](https://cdn.thenewstack.io/media/2024/05/4c6c8e84-kubernetes-rbac-permissions-2-1024x356.png)
Adding the
escalate verb to the role allows the user to change the role permissions and add a new verb.
Create a role that allows read-only access to pods and roles in this namespace:
|
1
|
kubectl -n rbac create role view --verb=list,watch,get --resource=role,pod
Bind this role to the SA
privesc:
|
1
|
kubectl -n rbac create rolebinding view --role=view --serviceaccount=rbac:privesc
Check if the role can be updated:
|
1
2
3
|
kubectl auth can-i update role -n rbac --as=system:serviceaccount:rbac:privesc
no
The SA can read roles but can’t edit them.
Create a new role that allows role editing in the
rbac namespace:
|
1
|
kubectl -n rbac create role edit --verb=update,patch --resource=role
Bind this new role to the SA
privesc:
|
1
|
kubectl -n rbac create rolebinding edit --role=edit --serviceaccount=rbac:privesc
Check if the role can be updated:
|
1
2
3
|
kubectl auth can-i update role -n rbac --as=system:serviceaccount:rbac:privesc
yes
Check if the role can be deleted:
|
1
2
3
|
kubectl auth can-i delete role -n rbac --as=system:serviceaccount:rbac:privesc
no
The SA can now edit roles but can’t delete them.
For the sake of experimental accuracy, check the SA capabilities by using a JSON Web Token (JWT):
|
1
|
TOKEN=$(kubectl -n rbac create token privesc --duration=8h)
Remove the old authentication parameters from the config, as
[Kubernetes will check the user’s certificate first](https://stackoverflow.com/questions/60083889/kubectl-token-token-doesnt-run-with-the-permissions-of-the-token) and won’t check the token if it already knows about the certificate.
This role shows you can edit other roles:
Try to add a new verb,
list, which you already used in the read-only view role:
Success.
Now, try to add a new verb,
delete, which you haven’t used in other roles:
This confirms that Kubernetes doesn’t allow users or service accounts to add new permissions if they don’t already have them — only if users or service accounts are bound to roles with such permissions.
So extend the
privesc SA permissions. Do this by using the admin config and adding a new role with the
escalate verb:
|
1
|
KUBECONFIG=~/.kube/config kubectl -n rbac create role escalate --verb=escalate --resource=role
Now, bind the
privesc SA to the new role:
|
1
|
KUBECONFIG=~/.kube/config kubectl -n rbac create rolebinding escalate --role=escalate --serviceaccount=rbac:privesc
Check if you can add a new verb to the role now:
Now it works. The user can escalate the SA privileges by editing the existing role. This means that the
escalate verb gives the appropriate admin privileges, including those of the namespace admin or even cluster admin.
### Bind
The
bind verb allows the user to edit the
RoleBinding or
ClusterRoleBinding objects for privilege escalation, similar to
escalate, which allows the user to edit
Role or
ClusterRole.
In the image below, the SA with the role binding that has the
update,
patch and
create verbs can’t add
delete until you create a new role with the
bind verb.
![How adding the bind verb to the role allows the user to change the role permissions and add a new verb](https://cdn.thenewstack.io/media/2024/05/261d0c3a-kubernetes-rbac-permissions-3-1024x356.png)
Adding the new role with the
bind verb allows the user to extend the role’s binding permissions.
Take a closer look at how this works.
Change the
kubeconfig file to admin:
|
1
|
export KUBECONFIG=~/.kube/config
Remove old roles and bindings:
|
1
2
|
kubectl -n rbac delete rolebinding view edit escalate
kubectl -n rbac delete role view edit escalate
Allow the SA to view and edit the role binding and pod resources in the namespace:
|
1
2
3
4
5
6
7
|
kubectl -n rbac create role view --verb=list,watch,get --resource=role,rolebinding,pod
kubectl -n rbac create rolebinding view --role=view --serviceaccount=rbac:privesc
kubectl -n rbac create role edit --verb=update,patch,create --resource=rolebinding,pod
kubectl -n rbac create rolebinding edit --role=edit --serviceaccount=rbac:privesc
Create separate roles to work with pods, but still don’t bind the role:
|
1
2
3
|
kubectl -n rbac create role pod-view-edit --verb=get,list,watch,update,patch --resource=pod
kubectl -n rbac create role delete-pod --verb=delete --resource=pod
Change the
kubeconfig to the SA
privesc and try to edit the role binding:
|
1
2
3
4
5
|
export KUBECONFIG=~/.kube/rbac.conf
kubectl -n rbac create rolebinding pod-view-edit --role=pod-view-edit --serviceaccount=rbac:privesc
rolebinding.rbac.authorization.k8s.io/pod-view-edit created
The new role has been successfully bound to the SA. Note that the
pod-view-edit role contains verbs and resources that were already bound to the SA by the role that binds
view and
edit.
Now, try to bind a role with a new verb,
delete, which is missing among the roles that are bound to the SA:
|
1
2
3
4
|
kubectl -n rbac create rolebinding delete-pod --role=delete-pod --serviceaccount=rbac:privesc
error: failed to create rolebinding: rolebindings.rbac.authorization.k8s.io "delete-pod" is forbidden: user "system:serviceaccount:rbac:privesc" (groups=["system:serviceaccounts" "system:serviceaccounts:rbac" "system:authenticated"]) is attempting to grant RBAC permissions not currently held:
{APIGroups:[""], Resources:["pods"], Verbs:["delete"]}
Kubernetes doesn’t allow this, even though you have permission to edit and create role bindings. But you can fix that with the
bind verb. Do so using the admin config:
|
1
2
3
4
5
6
7
|
KUBECONFIG=~/.kube/config kubectl -n rbac create role bind --verb=bind --resource=role
role.rbac.authorization.k8s.io/bind created
KUBECONFIG=~/.kube/config kubectl -n rbac create rolebinding bind --role=bind --serviceaccount=rbac:privesc
rolebinding.rbac.authorization.k8s.io/bind created
Try once more to create a role binding with the new
delete verb:
|
1
2
3
|
kubectl -n rbac create rolebinding delete-pod --role=delete-pod --serviceaccount=rbac:privesc
rolebinding.rbac.authorization.k8s.io/delete-pod created
Now it works. So, using the
bind verb, the SA can bind any role to itself or any user.
### Impersonate
The
impersonate verb in K8s is like
sudo in Linux. If users have
impersonate access, they can authenticate as other users and run commands on their behalf. The kubectl tool has the
--as, --as-group and
--as-uid options, which allow commands to be run as a different user, group or universally unique identifier (UUID), respectively. If a user was given impersonation permissions, they would become the namespace admin, or — if there is a
cluster-admin service account in the namespace — even the cluster admin.
The
impersonate verb is helpful to check the RBAC permissions delegated to a user. An admin should perform a command according to the template
kubectl auth can-i --as=$USERNAME -n $NAMESPACE $VERB $RESOURCE and check if the authorization works as designed.
In this example, the SA wouldn’t get info about pods in the
rbac namespace by just performing
kubectl -n rbac get pod. But it becomes possible if there is a role with the
impersonate verb:
|
1
2
3
|
kubectl auth can-i get pod -n rbac --as=system:serviceaccount:rbac:privesc
yes
|
1
2
3
|
KUBECONFIG=~/.kube/config kubectl -n rbac create sa impersonator
serviceaccount/impersonator created
Now, create a role with the
impersonate verb and a role binding:
|
1
|
KUBECONFIG=~/.kube/config kubectl -n rbac create role impersonate --resource=serviceaccounts --verb=impersonate --resource-name=privesc
(Look at the
--resource-name parameter in the above command: It only allows impersonation as the
privesc SA.)
|
1
2
3
4
5
|
role.rbac.authorization.k8s.io/impersonate created
KUBECONFIG=~/.kube/config kubectl -n rbac create rolebinding impersonator --role=impersonate --serviceaccount=rbac:impersonator
rolebinding.rbac.authorization.k8s.io/impersonator created
![The role with the impersonate verb helps the user to get info about pods](https://cdn.thenewstack.io/media/2024/05/045d18b5-kubernetes-rbac-permissions-4-1024x335.png)
Getting info about pods with a role that has the
impersonate verb.
Create a new context:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
|
TOKEN=$(KUBECONFIG=~/.kube/config kubectl -n rbac create token impersonator --duration=8h)
kubectl config set-credentials impersonate --token=$TOKEN
User "impersonate" set.
kubectl config set-context impersonate@kubernetes --user=impersonate --cluster=kubernetes
Context "impersonate@kubernetes" created.
kubectl config use-context impersonate@kubernetes
Switched to context "impersonate@kubernetes".
Check the permissions:
|
1
2
3
4
5
6
7
8
9
|
kubectl auth can-i --list -n rbac
Resources Non-Resource URLs Resource Names Verbs
selfsubjectaccessreviews.authorization.k8s.io [] [] [create]
selfsubjectrulesreviews.authorization.k8s.io [] [] [create]
...
serviceaccounts [] [privesc] [impersonate]
No additional permissions exist besides
impersonate, as specified in the role. But if you impersonate the
impersonator SA as the
privesc SA, you get the same permissions that the
privesc SA has:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
|
kubectl auth can-i --list -n rbac --as=system:serviceaccount:rbac:privesc
Resources Non-Resource URLs Resource Names Verbs
roles.rbac.authorization.k8s.io [] [edit] [bind escalate]
selfsubjectaccessreviews.authorization.k8s.io [] [] [create]
selfsubjectrulesreviews.authorization.k8s.io [] [] [create]
pods [] [] [get list watch update patch delete create]
...
rolebindings.rbac.authorization.k8s.io [] [] [list watch get update patch create bind escalate]
roles.rbac.authorization.k8s.io [] [] [list watch get update patch create bind escalate]
configmaps [] [] [update patch create delete]
secrets [] [] [update patch create delete]
Thus, the
impersonate SA has all of its own privileges as well as all the privileges of the SA it is impersonating, including those that a namespace admin has.
## How To Mitigate Potential Threats
The
escalate,
bind and
impersonate verbs can be used to create flexible permissions, resulting in granular management of access to K8s infrastructure. But these verbs also open the door to malicious use, since, in some cases, they enable a user to access crucial infrastructure components with admin privileges.
Three practices can help you mitigate the potential dangers of misuse or malicious use of these verbs:
- Regularly check RBAC manifests.
- Use the
resourceNamesfield in the
Roleand
ClusterRolemanifests.
- Use external tools to monitor roles.
Take a look at each in turn.
### Regularly Check RBAC Manifests
To prevent unauthorized access and RBAC misconfiguration, periodically check your cluster RBAC manifests:
|
1
2
3
|
kubectl get clusterrole -A -oyaml | yq '.items[] | select (.rules[].verbs[] | contains("esalate" | "bind" | "impersonate")) | .metadata.name'
kubectl get role -A -oyaml | yq '.items[] | select (.rules[].verbs[] | contains("esalate" | "bind" | "impersonate")) | .metadata.name'
### Use the resourceNames Field
To restrict the use of
escalate,
bind,
impersonate or any other verbs, configure the
resourceNames field in the
Role and
ClusterRole manifests. There, you can — and should — enter the names of resources that can be used.
Here is an example of a
ClusterRole that allows creation of a
ClusterRoleBinding with
roleRef named
edit and
view:
You can do the same with
escalate and
impersonate.
Note that in the case of
bind, an admin sets permissions for a role, and users can bind that role to themselves only if allowed to do so in
resourceNames. With
escalate, users can write any parameters within a role and become admins of a namespace or cluster. So,
bind restricts users, while
escalate gives them more options. Keep this in mind if you need to grant these permissions.
### Use External Tools To Monitor Roles
Consider using automated systems that monitor creating or editing roles with suspicious content, such as
[Falco](https://thenewstack.io/falco-is-a-cncf-graduate-now-what/) or [Tetragon](https://thenewstack.io/tetragon-1-0-promises-a-new-era-of-kubernetes-security-and-observability/).
You can also redirect Kubernetes audit logs to a log management system like
[Gcore Managed Logging](https://gcore.com/cloud/managed-logging), which is useful for analyzing and parsing K8s logs. To prevent accidental resource deletion, create a separate service account with the
delete verb and allow users to impersonate only that service account. This is the principle of least privilege. To simplify this process, you can use the kubectl plug-in
[kubectl-sudo](https://github.com/postfinance/kubectl-sudo).
At Gcore, we use these methods to make our
[Managed Kubernetes service](https://gcore.com/cloud/managed-kubernetes) more secure; we recommend that all our customers do the same. Using managed services doesn’t guarantee that your services are completely secured by default, but at Gcore, we do everything possible to ensure our customers’ protection, including encouraging RBAC best practices.
## Conclusion
The
escalate,
bind and
impersonate verbs allow admins to manage access to K8s infrastructure flexibly and let users escalate their privileges. These are powerful tools that, if abused, can cause significant damage to a K8s cluster. Carefully review any use of these verbs and ensure that the least privileged rule is followed. Users must have the minimum privileges necessary to operate, no more.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)