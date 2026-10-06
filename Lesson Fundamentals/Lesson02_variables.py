# Variables store any kind of information .
# Make sure to use descriptive variables names. 
# Note that variables can be overwritten

age = 73
print(age)
age = 74 
print(age)

password = "G00seberryPie5"
email = "hassan20300317@nhvweb.net"
print("Password:\t", password, "\nEmail:\t\t", email)

# variable name convention for booleans
isComplete = False
isEnabled = False
isAwake = True

# math conventions:
x = 3.14
y = 8
print(x + y)

# variables are flexible. you create or update another variable, like so:
count = 10 
print(count)
count_down = count - 1
print(count_down)
count = count_down
print(count)

Name = "Radia Perlman"
age = 34
Job = "Networking Engineer"

# Challenge 2: Update Variables  
# Create a variable called 'count' with a value of 10.  
# Use another variable to increase 'count' by 5
# Print the result

count = 10
new_count = count + 5
print(new_count)
# Challenge 3: Swap Variables  
# Given variables num = 4 and y = "hello".  
# Swap the values so that num = "hello" and y = 4. 
# Use a temporary variable.  
# Hint: You will need to create one new variable.

num = 4
vari = num
y = "hello"
num = y
y = vari
print(num)
print(y)