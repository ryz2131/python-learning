# Python to GitHub: Quick Setup Guide (Mac + VS Code)

This guide explains how to upload your Python practice files from a
local folder on your Mac to a GitHub repository.

## 1. Open your Python folder in VS Code

Open the folder in VS Code, then open the integrated terminal:

-   Menu: Terminal → New Terminal
-   Shortcut: Control + \`

If your folder is in Documents, for example:

``` bash
cd ~/Documents/Python
```

Check that you are in the correct folder:

``` bash
pwd
ls
```

## 2. Check that Git is installed

``` bash
git --version
```

If Git is not installed, run:

``` bash
xcode-select --install
```

## 3. Set your Git name and email (one-time setup)

Use the name and email associated with your GitHub account:

``` bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

Check the settings:

``` bash
git config --global --list
```

## 4. Initialize Git in your Python folder (one-time per folder)

``` bash
git init
```

This creates a local Git repository in the current folder.

## 5. Add a .gitignore file

Create a file named `.gitignore` in your Python folder and add:

``` gitignore
__pycache__/
*.pyc
.venv/
venv/
.env
.DS_Store
```

This excludes common temporary files, virtual environments, and
environment-variable files.

**Security:** Never upload passwords, API keys, AWS credentials, access
tokens, or other secrets. Check your files before pushing.

## 6. Create a repository on GitHub

1.  Go to https://github.com/new
2.  Enter a repository name, for example `python-learning`.
3.  Choose Public or Private.
4.  For the simplest first push, do not initialize it with a README,
    .gitignore, or license.
5.  Click **Create repository**.
6.  Copy the repository's HTTPS URL. It should look like:

`https://github.com/YOUR_USERNAME/python-learning.git`

Replace `YOUR_USERNAME` with the exact GitHub username shown on your
profile.

## 7. Connect your local folder to GitHub

If this is the first time adding a remote:

``` bash
git remote add origin https://github.com/YOUR_USERNAME/python-learning.git
```

If Git says `remote origin already exists`, do not add it again. Update
the existing URL instead:

``` bash
git remote set-url origin https://github.com/YOUR_USERNAME/python-learning.git
```

Verify the URL:

``` bash
git remote -v
```

Make sure the username and repository name match the repository you
created on GitHub.

## 8. Upload your files (first push)

``` bash
git add .
git commit -m "Initial Python learning files"
git branch -M main
git push -u origin main
```

If GitHub asks you to authenticate, follow the browser sign-in prompt.
Do not paste passwords or tokens into public files or chats.

## 9. Upload changes in future (daily workflow)

Whenever you create or edit Python files, save them in VS Code and run:

``` bash
git add .
git commit -m "Describe what you changed"
git push
```

Example commit messages:

``` bash
git commit -m "Practice Python lists and dictionaries"
git commit -m "Add file handling exercises"
git commit -m "Solve Python loop problems"
```

If there are no changes to commit, Git will tell you that there is
nothing to commit.

## 10. Useful troubleshooting commands

See the current folder:

``` bash
pwd
```

See files, including hidden files:

``` bash
ls -la
```

Check Git status:

``` bash
git status
```

Check the remote GitHub URL:

``` bash
git remote -v
```

See recent commits:

``` bash
git log --oneline -5
```

If `git push` says the repository was not found:

1.  Open the repository in your browser and confirm it exists.
2.  Check that you copied the correct HTTPS URL.
3.  Check the GitHub username and repository name for spelling.
4.  Update the remote with `git remote set-url origin ...`.
5.  Confirm that you have access to the repository and are signed in to
    the correct GitHub account.

If Git says `src refspec main does not match any`, you may not have made
a commit yet. Run `git status`, then stage and commit your files before
pushing.

## Quick reminder

**First-time setup:** initialize Git, create the GitHub repository,
connect the remote, then make the first commit and push.

**Every later upload:**

``` bash
git add .
git commit -m "Your update message"
git push
```

Your local Python folder is not automatically synced with GitHub. You
must push your commits to upload changes.
