Abhishek Kumar
Roll no :- 2301010322

# Lab 1: DevOps Foundations & Continuous Integration

## 1. Overview

This lab focuses on understanding DevOps fundamentals, Git version control, GitHub repository management, and Jenkins-based Continuous Integration and Continuous Deployment (CI/CD).

The practicals demonstrate how source code can be managed, tested, built, and deployed automatically using DevOps tools.

## 2. Objectives

- Install and configure Git on Ubuntu Linux.
- Understand Git repository initialization, staging, committing, branching, and merging.
- Create and manage remote repositories using GitHub.
- Install and configure Jenkins.
- Implement a basic Jenkins CI/CD pipeline.
- Create a declarative Jenkinsfile with Build, Test, and Deploy stages.
- Automate application deployment using Jenkins.
- Document commands, configurations, screenshots, and observations.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Windows 10/11 | Host Operating System |
| WSL2 | Linux environment on Windows |
| Ubuntu 24.04 | Linux operating system |
| Git | Version control system |
| GitHub | Remote code repository |
| Java 21 | Jenkins runtime environment |
| Jenkins | CI/CD automation server |
| Python 3 | Sample application |
| Pytest | Automated testing |
| VS Code | Code editor (optional) |

## 4. Project Structure

```text
devops-lab/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Jenkinsfile
├── README.md
│
└── documentation/
    ├── commands.txt
    ├── observations.txt
    ├── commit-history.txt
    ├── pipeline-details.txt
    │
    └── screenshots/
        ├── exp1-git-installation.png
        ├── exp1-git-configuration.png
        ├── exp1-jenkins-dashboard.png
        ├── exp2-git-initialization.png
        ├── exp2-git-branch-merge.png
        ├── exp2-github-push.png
        ├── exp3-jenkins-build.png
        ├── exp4-jenkinsfile.png
        ├── exp4-pipeline-success.png
        └── exp5-deployment.png
```

## 5. Application Description

A simple Python application is developed to demonstrate Git version control and Jenkins automation.

### app.py

```python
def greet(name):
    return f"Hello, {name}! Welcome to DevOps Lab."

if __name__ == "__main__":
    print(greet("Student"))
```

### test_app.py

```python
from app import greet

def test_greet():
    assert greet("Abhishek") == "Hello, Abhishek! Welcome to DevOps Lab."

def test_greet_student():
    assert greet("Student") == "Hello, Student! Welcome to DevOps Lab."
```

### requirements.txt

```text
pytest
```

## 6. Experiments Performed

### Experiment 1: Install and Configure Git and Jenkins

**Objective:** Install Git on Ubuntu, verify its installation, and configure global Git username and email. Install Java and Jenkins for CI/CD automation.

**Important commands:**

```bash
sudo apt update
sudo apt install git -y
git --version

git config --global user.name "Abhishek Kumar"
git config --global user.email "YOUR_EMAIL@gmail.com"

git config --global --list

java -version

sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

### Experiment 2: Set Up Version Control Using Git

**Objective:** Initialize a repository, stage and commit changes, create branches, merge branches, and push the repository to GitHub.

**Important commands:**

```bash
git init
git status
git add app.py
git commit -m "Initial commit"

git branch feature
git switch feature

git add app.py
git commit -m "Add welcome function"

git switch main
git merge feature

git log --oneline --all --graph

git remote add origin REPOSITORY_URL
git branch -M main
git push -u origin main
```

### Experiment 3: Implement a Basic Jenkins CI/CD Pipeline

**Objective:** Configure Jenkins to retrieve source code from GitHub and execute an automated build.

**Activities:**

- Created a Jenkins Freestyle project.
- Configured the GitHub repository URL.
- Configured Poll SCM as a build trigger.
- Added shell commands to execute the Python application.
- Executed the Jenkins build and verified Console Output.

### Experiment 4: Create a Jenkinsfile Defining Pipeline Stages

**Objective:** Create a declarative Jenkins pipeline with Build, Test, and Deploy stages.

**Pipeline stages:**

1. **Build:** Create a Python virtual environment, install dependencies, and check application syntax.
2. **Test:** Execute automated test cases using Pytest.
3. **Deploy:** Copy the application into a deployment directory.

**Jenkinsfile:** The pipeline configuration is maintained in the `Jenkinsfile` at the root of the repository.

### Experiment 5: Automate Application Deployment

**Objective:** Automate application deployment using Jenkins by configuring build triggers, post-build actions, and deployment steps.

**Activities:**

- Configured Poll SCM to check for repository changes.
- Automated application deployment.
- Configured success and failure actions.
- Archived deployment files as Jenkins build artifacts.
- Verified the deployed application.

### Experiment 6: Record All Commands and Observations

**Objective:** Maintain documentation of all commands, pipeline configurations, screenshots, commit history, and observations.

**Documentation includes:**

- Git and Jenkins installation commands.
- Git commit and branch history.
- Jenkins job configurations.
- Pipeline execution results.
- Deployment verification.
- Practical screenshots and observations.

### Experiment 7: Prepare a CI/CD Workflow Report

**Objective:** Prepare a report describing pipeline architecture, stages, automation results, and observations with supporting screenshots.

The report includes:

- Introduction and objectives.
- Tools and technologies.
- CI/CD architecture.
- Build, Test, and Deploy stages.
- Automation results.
- Screenshots and observations.
- Conclusion.

## 7. CI/CD Workflow

The implemented workflow follows this sequence:

```text
Developer
    |
    v
Git Repository
    |
    v
GitHub
    |
    v
Jenkins
    |
    v
Build Stage
    |
    v
Test Stage
    |
    v
Deploy Stage
    |
    v
Application Deployment
    |
    v
Build Artifacts
```

## 8. Jenkins Pipeline Configuration

| Configuration | Value |
|---|---|
| Pipeline Type | Declarative Pipeline |
| Source Code Management | Git |
| Remote Repository | GitHub |
| Branch | main |
| Script Path | Jenkinsfile |
| Build Trigger | Poll SCM |
| Polling Schedule | H/2 * * * * |
| Build Tool | Python |
| Testing Tool | Pytest |
| Deployment | Local deployment directory |

## 9. Expected Results

The following results are expected after successful execution:

- Git is installed and configured.
- Git repository is initialized and managed successfully.
- Branch creation and merging operations work correctly.
- Source code is pushed to GitHub.
- Jenkins retrieves source code from GitHub.
- Jenkins executes the automated build.
- Automated test cases pass successfully.
- Build, Test, and Deploy pipeline stages execute.
- Application deployment files are generated.
- Jenkins archives the deployment artifacts.

## 10. Observations

The practical experiments demonstrate the integration of version control and CI/CD automation.

Git and GitHub provide source code management, while Jenkins automates the build, testing, and deployment processes.

The use of automated pipelines reduces manual effort and provides a structured software delivery workflow.

## 11. Conclusion

Successfully performed the DevOps Foundations and Continuous Integration lab using Git, GitHub, Jenkins, Python, and Ubuntu through WSL2 on Windows.

The practical exercises provided hands-on experience with version control, repository management, Jenkins configuration, automated builds, software testing, and application deployment.

## 12. References

- Git Documentation: https://git-scm.com/doc
- GitHub Documentation: https://docs.github.com/
- Jenkins Documentation: https://www.jenkins.io/doc/
- Ubuntu Documentation: https://ubuntu.com/tutorials
- WSL Documentation: https://learn.microsoft.com/en-us/windows/wsl/
- Pytest Documentation: https://docs.pytest.org/
