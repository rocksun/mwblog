# Part-3 End-to-End Java DevOps Automation Project
**Prerequisite**: [Part-2 End-to-End Java DevOps Automation Project](https://medium.com/p/0b94eedad757/edit)
# Setting Up CI/CD Using Jenkins
**Install Plugins in Jenkins**
**1. Eclipse Temurin Installer**
— Automatically installs and configures the Eclipse Temurin JDK.
— Installation:
— Jenkins dashboard -> Manage Jenkins -> Manage Plugins -> Available tab.
— Search for “Eclipse Temurin Installer” and select it.
— Click “Install without restart”.
**2. Pipeline Maven Integration**
— Provides Maven support for Jenkins Pipeline.
**3. Config File Provider**
— Allows you to define and use configuration files centrally in Jenkins.
**4. SonarQube Scanner**
— Integrates Jenkins with SonarQube for code quality and security analysis.
**5. Kubernetes CLI**
— Allows Jenkins to interact with Kubernetes clusters using `kubectl`.
**6. Kubernetes**
— Integrates Jenkins with Kubernetes, allowing Jenkins agents to run as pods.
**7. Docker**
— Enables Jenkins to interact with Docker for building and managing containers.
**8. Docker Pipeline**
— Extends Jenkins Pipeline with Docker-specific steps.
**9. Maven Integration**
— Keeps your projects in sync and ensures they are always tested with the latest updates.
**Install and Configure Trivy on Jenkins Server**
- Note: There is no Jenkins plugin for Trivy, so install it directly on the Jenkins server and add it to your Jenkins pipeline stage.
Trivy Installation Command

`sudo apt-get install wget apt-transport-https gnupg lsb-release -y`
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update -y
sudo apt-get install trivy -y
trivy -v
# Expected output: Version: 0.53.0 (or the latest version)
**Global Tool Configuration:**
The “Global Tool Configuration” section (formerly known as “Manage Jenkins -> Configure Tools”) is where you define and manage tools that Jenkins uses across all jobs. This includes compilers, build tools, and other utilities required for building projects

**Creating Git credentials as Global Credentials**: with username as GitHub User and password value as token the we created in Part-2(while setting Private repository)
The “**Credentials**” section allows you to manage credentials that Jenkins uses to interact with external systems securely. Credentials can include usernames and passwords, SSH keys, API tokens, and more.

From here we will started writing out Jenkins pipeline code, you can get the complete code from this file : [ pipeline.groovy](https://github.com/navin5556/devops-pipeline-kubernetes/blob/main/phase-3/pipeline.groovy) and follow step by step.

**Jenkins Pipeline setups steps:**
- create Job Name:
**BoardGame**of type Pipeline
2. Enable — Discard old builds (Max # of builds to keep = 2)

**Manage Jenkins -> System**
The “**System**” section under “Manage Jenkins” is where you configure the overall system settings for Jenkins. This includes settings that affect the entire Jenkins installation and how it operates.

**Configuring SonarQube Server**
Before writing the SonarQube analysis stage in the Jenkins Pipeline, you need to configure the SonarQube server in Jenkins. Here are the steps to do this:

**Fetch SonarQube Server Credentials**:
. Go to SonarQube Server->Administration-> Security -> User->Tokens

**2. Create Global Credentials in Jenkins**:
3. **Configure SonarQube Server in Jenkins**:

Steps Before writing the SonarQube Quality Gate stage in the Jenkins Pipeline,

Go to SonarQube Server->Administration-> Configuration-> Webhooks->Tokens

Add Jenkins IP :

Here is the complete architecture of SonarQube and Jenkins integration for your reference:

## Configuring Nexus
Before writing code for **Publis to nexus **artifact stage we need to add the repository URL in our POM file.

To configure the Global Maven settings in Jenkins, follow these steps:

**Navigate to the Configuration:**
- Go to
**Manage Jenkins**->**Manage Files**. - Add a new configuration file.
**2. Set Configuration Type and ID:**
- Select the configuration type as
**Global Maven settings.xml**. - Set the ID of the configuration file to
`global-settings`
.
**3. Edit the Content:**
- Edit the content of the configuration file by adding the following code inside the
`<servers>`
tag:
`<servers>`
<server>
<id>maven-releases</id>
<username>nexus username</username>
<password>nexus password</password>
</server>
<server>
<id>maven-snapshots</id>
<username>nexus username</username>
<password>nexus password</password>
</server>
</servers>
Replace `nexus username`
and `nexus password`
with your actual Nexus credentials.

By following these steps, you will configure the Global Maven settings in Jenkins to include the necessary Nexus repository credentials

The “Manage Files” section in Jenkins under “Manage Jenkins” is used to handle configuration files that are centrally managed and can be referenced in Jenkins jobs. This feature is part of the Config File Provider plugin.

## Setting Docker-hub credentials:
**Stage: Deploy to Kubernetes Cluster**
Install **KUBECTL **on Jenkins server by running below command

`curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl`
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
kubectl version --short --client
To deploy an application to a Kubernetes Cluster correctly and securely, we need to follow proper procedures such as creating a service account and using Role-Based Access Control (RBAC).

RBAC stands for Role-Based Access Control. Let’s say we have three users in our project:

- User 1: The architect with comprehensive knowledge.
- User 2: A medium-level guy.
- User 3: An intern or a very fresh guy.When working with Kubernetes, we can’t grant complete access to a fresher or intermediate-level guy. So, we create roles:

1.

Role 1: Cluster Admin Access
— Full access to the cluster.
— This role is assigned to the architect (User 1).2.

Role 2: Intermediate Access
— Good level of permissions but not full admin.
— This role is assigned to the medium-level guy (User 2).3.

Role 3: Read-Only Access
— Only allows viewing resources, with no modification permissions.
— This role is assigned to the intern (User 3).This method ensures security by not giving complete access to everyone. Instead, we create specific roles with appropriate permissions and assign them to the respective users.

Now, let’s proceed to make our deployment secure by creating a service account.

1. Create a Service Account:
— This account will be used to manage permissions and control access levels.By following these steps, we ensure our Kubernetes deployment is secure and properly managed. Now, let’s move on to the practical part and create the service account.

Follow this file: [ service-role-for-jenkins.md](https://github.com/navin5556/devops-pipeline-kubernetes/blob/main/phase-3/service-role-for-jenkins.md) for creating service account for jenkins.

After created service account paste the copied token of **secret/mysecretname** into **Jenkins global credentials**:

**Setting Up HTML Email Notifications in Jenkins**
Steps To Configure Email at jenkins:

Now create credentials using this app password at Jenkins:

The provided command is a Jenkins pipeline `post`
block that executes certain actions always after the main pipeline stages have run. This specific block sends an email notification with details about the Jenkins build. Here's a breakdown of its use and what it does:

# Key Components:
:**post { always { ... } }**
- This block ensures that the enclosed script is executed after every build, no matter the result (success, failure, etc.).
**Environment Variables and Parameters**:
`jobName = env.JOB_NAME`
: Fetches the name of the Jenkins job.`buildNumber = env.BUILD_NUMBER`
: Fetches the build number.`pipelineStatus = currentBuild.result ?: 'UNKNOWN'`
: Gets the current build result; defaults to 'UNKNOWN' if the result is null.`bannerColor = pipelineStatus.toUpperCase() == 'SUCCESS' ? 'green' : 'red'`
: Sets the banner color based on the build status ('green' for success, 'red' otherwise).
**Email Body Construction**:
- Uses an HTML template to construct the email body, displaying the job name, build number, and build status. The background color of the banner changes based on the build result.
**emailext**** Step**:
: Sets the subject of the email to include the job name, build number, and build status.**subject**
: Sets the HTML body of the email.**body**
: Specifies the recipient's email address (your email: 'naveenkumarsingh5556@gmail.com').**to****from****and**
: Sets the sender's email address (here, 'jenkins@example.com').**replyTo**
: Specifies that the email content type is HTML.**mimeType**
: Includes an attachment pattern to attach the specified report file (here, 'trivy-image-report.html').**attachmentsPattern**
**Summary**:
**Purpose**: To notify via email about the Jenkins job build status.**Execution**: Always executed after the build.**Details in Email**: Job name, build number, build status, link to console output, and an attached report.**Customization**: Banner color changes based on the build result (green for success, red for failure or other statuses).
This command helps in keeping stakeholders informed about the build status through an automated email notification system.

End result:

Summary:
**In this article**, we covered the setup of a comprehensive CI/CD pipeline using Jenkins for a Java DevOps automation project. Key steps included installing essential Jenkins plugins, configuring tools like SonarQube, Nexus, Docker, and Kubernetes, and setting up global credentials. We also demonstrated how to deploy applications securely to a Kubernetes cluster using Role-Based Access Control (RBAC) and how to configure HTML email notifications for build status updates. By following these steps, you can ensure a robust, automated, and secure deployment pipeline for your Java applications.