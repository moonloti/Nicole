# File: homework5.py
# --- 3.1 Vocabulary Review ---

# 1. Git vs. GitHub
# Git is a versional control tool that runs on your computer.
# GitHub is a website that hosts your Git repositories online.

# 2. Terminal vs. Command Line
# The terminal is the app you type commands into
# The command line is the actual line where you type.

# 3. Local vs. Remote Repository
# A local repository is your project saved on your computer
# A remote repository is the same project stored online (like GitHub).

# 4. Version Control
# A system that tracks changes to your code over time so you can undo 
# mistakes or go back to older versions.

# 5. Staging Area
# A space where you prepare changes before committing them using "git add".

# 6. git add
# Adds a file to the staging area to prepare it for a commit.

# 7. git commit
# Saves your staged changes to the local repository with a message.

# 8. git push
# Uploads you local commits to GitHub.

# 9. git status
# Shows which files are modified, staged or untracked.

# 10. git pull
# Downloads the latest changes from GitHub to your local repository.

# 11. pwd
# Prints the current folder path you are in.

# 12. ls
# Lists all files and folders in the current directory.

# 13. cd
# Changes the directory (folder) you are currently in.

# 14. nano
# A simple text editory that runs in the terminal

# 15. touch
# Creates a new empty file

# 16. mv
# Moves or renames a file

# 17. rm
# Deletes a file permanently

# 18. cat
# Displays the contents of a file in the terminal

# --- 3.2 A Directory Tree ---

# Q: You have been plopped into Judy's directory system. What command will
# tell you what your current working directory is?
# pwd

# Q: The terminal responds by saying you are in ~/python_decal/judy_decal.
# What command will list all the files in your current working directory?
# ls

# Q: Brianna just sent out an announcement saying there was a typo in homework.py.
# You need to pull the brianna_repo repository to find the updated file.
# What command(s) will let you move to the correct repository and pull the latest changes?
# cd ~/python_decal/brianna_repo
# git pull

# Q: How would you move this new homework.py to the homework/ folder
# in your personal repository?
# mv homework.py ~/python_decal/judy_decal/homework/

# Q: How would you move yourself to the same repository as homework.py?
# cd ~/python_decal/judy_decal/homework/

# Q: You want to see the contents of homework.py in your terminal,
# how would you do this?
# cat homework.py

# Q: Great job! You just finished the homework for this week. What command(s)
# allow you to save the changes and push from your local to your remote repository?
# git add homework.py
# git commit -m "Fix typo in homework.py"
# git push

# Q: Oh no! Git gave you the following error. What commands should you call
# to resolve this error and push your homework properly?
# What does the error mean? (i.e. what did "Judy" do wrong when trying to push?)
#
# The error means the remote repository has new changes that Judy does not
# have locally. Judy tried to push without first pulling the latest changes,
# so GitHub rejected it to prevent overwriting.
# To fix it:
# git pull
# git push

# Q: What absolute path will allow you to move to Recent/?
# cd ~/Recent/

# --- 4.1 Data Types ---
def checkDataType(value):
    if type(value) == int:
        return 'int'
    elif type(value) == float:
        return 'float'
    elif type(value) == str:
        return 'str'
    elif type(value) == bool:
        return 'bool'
    elif type(value) == list:
        return 'list'
    elif type(value) == dict:
        return 'dict'
    else:
        return 'unknown'
    
# --- 4.2 Conditionals ---
def evenOrOdd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
# --- 5. Loops ---
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# --- 6.1 Lists ---
def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

# --- 6.2 Debugging ---
# fixed
def square(num):
    return num * num

print(evenOrOdd(7))
