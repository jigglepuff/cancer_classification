# Workflow
## To add your changes
1. To see changes you made:
git status
2. Put files you want to push in a "waiting area":
git add [path/to/file1] [path/to/file2]
3. To see what you're about to commit:
git status
4. Commit/save your changes locally:
git commit -m "write a brief message about what changes you made"
5. Push to remote repository so that everyone can see it:
git push origin [branch_name]
(if pushing to master branch, branch_name should be master)


## if you are making major/drastic changes, please create a new branch:
1. Check which branch you're on:
git branch
2. Switch to branch you want to branch-off of
git checkout origin [branch_name]
(You most likely would like to branch off of master, in that case: branch_name should be master)
3. Make new branch locally:
git checkout -b [name_of_your branch]
4. When you're happy with your changes, push your branch to remote, so that everyone can see your hard work:
git push -u origin [name_of_your branch]
(the -u option is only needed for the first time you're pushing a new branch to remote)
