# NX Tech Synch - Git & Python Demo

Welcome to the **NX Tech Synch** session! This repository is a hands-on demo to learn the basics of Git and Python.

---

## 📖 What is Git and Why Does It Exist?

**Git** is a **distributed version control system** created by Linus Torvalds in 2005 (the same person who created Linux).

It exists to solve a fundamental problem in software development: **how do multiple people work on the same codebase without overwriting each other's work?**

Before Git, teams would share code via email, USB drives, or shared folders — leading to chaos, lost work, and conflicting changes. Git solves this by:

- **Tracking every change** ever made to your code (full history).
- **Allowing multiple people** to work on the same project simultaneously.
- **Letting you revert** to any previous version if something breaks.
- **Enabling collaboration** through platforms like GitHub, GitLab, and Bitbucket.

Think of Git as an **unlimited undo button** for your entire project, combined with a **collaboration tool** that keeps everyone in sync.

---

## 🔑 Key Git Concepts

### Commit
A **commit** is a snapshot of your project at a specific point in time. Every time you make changes and commit them, Git saves a record of exactly what changed, who changed it, and when. Think of it as a **save point** in a video game — you can always go back to it.

```bash
git commit -m "Describe what you changed"
```

### Push
A **push** sends your local commits to a **remote repository** (e.g., GitHub). Until you push, your changes only exist on your machine. Pushing makes them available to everyone else.

```bash
git push origin main
```

### Pull
A **pull** downloads the latest changes from the remote repository to your local machine. This is how you stay up to date with what others have pushed.

```bash
git pull origin main
```

### Branch
A **branch** is an independent line of development. The default branch is usually called `main`. You can create new branches to work on features or fixes without affecting the main code. Once your work is ready, you **merge** it back into `main`.

```bash
git branch my-feature        # Create a new branch
git checkout my-feature      # Switch to it
# or in one command:
git checkout -b my-feature   # Create and switch
```

### Clone
**Cloning** creates a full copy of a remote repository on your local machine, including all its history.

```bash
git clone <repository-url>
```

### Staging (git add)
Before committing, you need to **stage** your changes. This tells Git which files you want to include in the next commit. Think of it as putting items in a box before shipping.

```bash
git add hello.py          # Stage a specific file
git add .                 # Stage all changed files
```

---

## 🚀 Getting Started

### Prerequisites
- [Git](https://git-scm.com/downloads) installed on your machine
- [Python 3](https://www.python.org/downloads/) installed
- A [GitHub](https://github.com) account (optional, for pushing)

### Step 1: Clone This Repository

Open a terminal and run:

```bash
git clone https://github.com/lpintoda/NXTechSynch.git
```

Then navigate into the project folder:

```bash
cd NXTechSynch
```

### Step 2: Run the Python Script

```bash
python hello.py
```

You should see a greeting and some system info printed to the terminal.

---

## 🔄 Common Git Workflow

Here's the typical day-to-day workflow with Git:

### 1. Check the status of your repo

```bash
git status
```

This shows which files have been modified, staged, or are untracked.

### 2. Make changes to a file

Edit `hello.py` (or any file) with your preferred editor.

### 3. Stage your changes

```bash
git add hello.py
```

Or stage everything:

```bash
git add .
```

### 4. Commit your changes

```bash
git commit -m "A short description of what you changed"
```

### 5. Push to the remote repository

```bash
git push origin main
```

### 6. Pull the latest changes (from others)

```bash
git pull origin main
```

---

## 📋 Quick Reference — Useful Git Commands

| Command | Description |
|---|---|
| `git init` | Initialize a new Git repository |
| `git clone <url>` | Clone a remote repository |
| `git status` | Check the state of your working directory |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit staged changes with a message |
| `git push origin main` | Push commits to the remote |
| `git pull origin main` | Pull latest changes from the remote |
| `git log` | View commit history |
| `git log --oneline` | View compact commit history |
| `git diff` | See unstaged changes |
| `git branch` | List branches |
| `git checkout -b <name>` | Create and switch to a new branch |
| `git merge <branch>` | Merge a branch into the current one |

---

## 🐍 Creating a Python Virtual Environment (venv)

A **virtual environment** isolates your Python project's dependencies so they don't conflict with other projects.

### Create a venv

```bash
python -m venv venv
```

### Activate it

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### Install packages (example)

```bash
pip install requests
```

### Deactivate when done

```bash
deactivate
```

> **Tip:** The `.gitignore` file in this repo is already configured to exclude the `venv/` folder from Git, since dependencies should not be committed.

---

## 🎯 Putting It All Together

Here's a full end-to-end example:

```bash
# 1. Clone the repo
git clone https://github.com/lpintoda/NXTechSynch.git
cd NXTechSynch

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 3. Run the script
python hello.py

# 4. Make a change to hello.py (edit with your preferred editor)

# 5. Stage, commit, and push
git add .
git commit -m "Updated hello.py with my changes"
git push origin main
```

---

Happy coding! 🚀
