# File: homework1. py
#  --- 3.1 Variables and Data Types ---

a = 10
print(a)
print(type(a))
# a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b))
# b is a float, a number with a decimal point

c = 3j
print(c)
print(type(c))
# c is a complex number, with an imaginary part 'j' and the real part

d = "hello"
print(d)
print(type(d))
# d is a string, a sequence of characters

e = [1, 2, 3]
print(e)
print(type(e))
# e is a list, an ordered and unchangeable collection

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a dictionary which stores information in key-value pairs

g = (1, 2)
print(g)
print(type(g))
# g is a tuple, an ordered and unchangeable collection

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list, an order collection of strings

i = True
print(i)
print(type(i))
# i is a boolean, representing either True/False

j = None
print(j)
print(type(j))
# j is a NoneType, representing the absense of a value

k = [True, "blue", 12]
print(k)
print(type(k))
# k is a list containing multipe data types

l = str(14)
print(l)
print(type(l))
# l is a string, creating by converting an integer to text

m = 1e4
print(m)
print(type(m))
# m is a float written in scientific notation

# Questions:
# 1. I found 9 different data types.
# 2. These data types consisted of integer, float, complex number, string, list, dictionary, tuple, boolean, Nonetype.
# 3. A couple variable have the same data type while most of them do not
    # b and m are both float while e, h and k are all list while d and l are both str
# 4. l is a string (str) and it is not an integar because str(14) converts the number into text, converting the value into a string data type.
# 5. Another example of another data type not given above
n = {1, 2, 3}
print(n)
print(type(n))
# n is a set, an unordered collection of unique values

# --- 3.2 Booleans ---

print(10 > 9) # True, 10 is greater than 9

print(10 == 9) # False, 10 is not equal to 9

print(10 <= 9) # False, 9 is not greater than or equal to 10

print(bool("abc")) # True, non-empty strings evaluates to True

print(bool(123)) # True, non-zero numbers evaluates to True

print(bool(["apple", "cherry", "banana"])) # True, a non-empty list evaluates to True

print(bool(True)) # True, True evaluates to True

print(bool(False)) # False, False evaluates to False

print(bool(0)) # False, 0 evaluates to False

print(bool("")) # False, an empty string evaluates to False

print(bool(" ")) # True since the space still counts as content

print(bool(())) # False, an empty tuple evaluates to False

print(bool([])) # False, an empty list evaluates to False

print(bool({})) # False, an empty dictionary evaluated to False

print(bool(True and False)) # False, True and False results in False

print(bool(True and True)) # True, both values are True

print(bool(False and False)) # False, both values are False

print(bool(True or False)) # True, at least one value is True

print(bool(True or True)) # True, both values are True

print(bool(False or False)) #False, neither value is True

print(bool(not(False))) # True, not reverses False to True

print(bool(not(True))) # False, not reverses True to False

# Questions
# 1. Expressions return True when conditions are met/values are non-empty and non-zero, and return False when condition are not met/values are empty/zero
# 2. The one that surprised me the most was the bool(" ") since it is True even though it appears empty, the space character counts
# 3. This expression returns True since the list is not empty
print(bool([1]))
# 4. This expression returns False since None represents the absence of a value which evaluates to False in Python
print(bool(None))

# --- 3.3.1 Arithmetic Operators ---

print(10 + 5) # 15 and performs addition

print(10 - 5) # 5 and performs subtraction

print(2 * 4) # 8 and performs multiplication

print(6 / 3) # 2.0 and performs division and returns a float

print(5 % 2) # 1, % returns the remainder

print(3 ** 2) # 9, ** performs exponents

print(15 // 2) # 7, // performs floor division

print(5 == 2) # False, checks if the values are equal but 5 and 2 are not equal

print(10 != 10) # False, checks if the values are not equal

print(2 < 5) # True, < checks if the left value is less than the right

print(12 > 5) # True, > checks if the left value is greater than the right

print(5 <= 6) # True, <= checks if the left value is less than or equal to the right

print(1 >= 10) # False, >= checks if the left value is greater than or equal to the right

# --- 3.3.3 Assignments Operators ---
x = 5

x += 5
print(x)
# 10, adds 5 to x and stores the result back in x

x -=4
print(x) 
# 6, subtracts 4 from x and stores the result back in x

x *= 3
print(x) 
# 18, multiplies x by 3 and stores the result back in x

# --- 3.3.3 Assignment Operators ---

# Logical Operators (Questions)
# 1. The and operator checks two conditions and returns True only if both are True.
10 > 5 and 3 < 7 # True
10 > 5 and 3 > 7 # False
# 2. The or operator returns True if at least one condition is True
10 > 5 and 3 > 7 # True
10 < 5 and 3 > 7 # False
# 3. The not operator reverses the Boolean value of an expression
not (4 < 2) # True
not (4 > 2) # False

# More Questions
# 1. The / performs regular division and returns a float while the // performs floor division and returns a whole number
# 2. The % returns the remainder of a divion while // returns the quotient without the remainder
# 3. To calculate the remainder when dividing two numbers, use the % operator (ex: 7 % 3 which = 1)
# 4. Assignment operators assign or update values in variables, often by combining an operation with assignment

# --- 3.4 Strings ---

my_string = "hello"

print(my_string) # Prints: hello

print(my_string[0]) # Prints: h (the first character)

print(my_string[1]) # Prints: e (the second character)

print(my_string[2]) # Prints: l (the third character)

print (my_string[3]) # Prints: l (the fourth character)

print (my_string[4]) # Prints: o (the fifth character)

print(my_string[-1]) # Prints: o (the last character)

print(my_string[1:3]) # Prints: el (characters from 1-3, but the 3rd chracter is not included)

print(my_string[0:5:2]) # Prints: hlo (every second character in the string))

print(len(my_string)) # Prints: 5 (the number of characters in the string)

print(my_string + " goodbye") # Prints: hello goodbye (string addition)

print(my_string * 7) # Prints: hellohellohellohellohellohellohello (the string repeats for a multitude of 7)

# Questions
# 1. Silicing is selecting a portion of a string using a start, stop and optional step.
# 2. 
name = "Oski"
print("Hello, my name is", name)
# 3. 
name = "Oski"
print(f"Hello, my name is {name}")
# 4. The first uses commas to print multiple values, while the second uses an f- spring to embed the variable directly inside the string

# --- 3.5 Terminal Commands ---

# cd
# Changes directories. Use it followed by a folder name
# Example: cd Desktop

# ls
# Lists all files and folders in the directory. Use it by typing ls in the terminal
# Example: ls

# ls -a
# Lists all the files, including hidden files. Use it with the -a flag
# Example: ls -a

# mkdir
# Creates a new directory (folder). Use it followed by the new folder name
# Example: mkdir projects

# cat
# Displays the contents of a file in the terminal. Use it followed by the file name.
# Example: cat notes.txt

# pwd
# Prints the current working directory (your current location). Use it by typing pwd
# Example: pwd

# cd ..
# Moves up one directory level. Use it when you want to go back to the parent folder
# Example: cd ..

# cd .
# Refers to the current directory. Often used in scripts or commands
# Example: cd .

# cd ~
# Changes directory to the home folder. Use it to quickly return home
# Example: cd ~

# cp
# Copies files/folders. Use it with a source and destination
# Example: cp file1.txt file2.txt

# mv
# Moves/renames files/folders. Use it with a source and destination
# Example: mv oldname.txt newname.txt

# rm
# Deletes files/folders (permanently). Use it carefully followed by the file name
# Example: rm oldfile.txt

# clear
# Clears all text from the terminal screen. Use it to clean up the terminal view
# Example: clear

# grep
# Searches for text inside files. use it with a search word and file name
# Example: grep "hello" notes.txt

# Questions
# 1. Three other terminal commands (not listed) include
        # touch, which creates a new empty file (ex: touch homework.txt)
        # echo, which prints texts to the terminal or writes text into a file (ex: echo "Hello world")
        #whoami, which displays the current user's username (ex: whoami)
# 2. The difference between ls and ls -a is that ls only shows the visible files/folders while ls -a shows all the files including the hidden files
# 3. A hidden file is a file whose name starts with a dot (.) and is not shown by default when using ls.
# 4. The three other flags are:
        # -l used with ls, shows files in a long detailed format (ex: ls -l)
        # -r used with rm, deletes folders and their contexts recursively (ex: rm -r old_folder)
        # -i used with rm, asks for confirmation before deleting a file (ex: rm -i file.txt)
        