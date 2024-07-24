# Part-2 End-to-End Java DevOps Automation Project
**Prerequisite**: [Part-1 End-to-End Java DevOps Automation Project](/@navin5556/part-1-end-to-end-java-devops-automation-project-97835d7b7914)
# Setting Up a Private GitHub Repository
# Step 1: Create a Private Git Repository
- Go to your preferred Git hosting platform (e.g., GitHub, GitLab, Bitbucket).
- Log in to your account or sign up if you don’t have one.
- Create a new repository and set it as private.
# Step 2: Generate a Personal Access Token
- Navigate to your account settings or profile settings.
- Find the “Developer settings” or “Personal access tokens” section.
- Generate a new token with the necessary permissions (e.g., repo access).
# Step 3: Clone the Repository Locally
- Open Git Bash or your terminal.
- Navigate to the directory where you want to clone the repository.
- Use the
`git clone`
command followed by the repository's URL:
`git clone <repository_URL>`
Replace `<repository_URL>`
with your private repository's URL.

# Step 4: Add Your Source Code Files
- Navigate into the cloned repository directory.
- Add your source code files or create new ones in this directory.
# Step 5: Stage and Commit Changes
- Stage the changes using:
`git add .`
2. Commit the staged changes with a meaningful message:

`git commit -m "Your commit message here"`
# Step 6: Push Changes to the Repository
- Push your committed changes to the remote repository:
`git push`
2. If it’s your first time pushing to this repository, you might need to specify the remote and branch:

`git push -u origin master`
Replace `master`
with the branch name if you're pushing to a different branch.

# Step 7: Enter Personal Access Token as Authentication
When prompted for credentials during the push, enter your username (usually your email) and use your personal access token as the password.

By following these steps, you’ll be able to create a private Git repository, connect to it using Git Bash, and push your code changes securely using a personal access token for authentication

Note: This is the end of **Part 2: Source Code Management,** part-3 will cover** **CI/CD Pipeline Configuration