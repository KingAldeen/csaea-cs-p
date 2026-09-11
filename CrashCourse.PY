import math
# Comment
# Comment
# Comment
# Comment
# Comment
# Comment
print("Hello, World!")
# Variable Declarations and Types
A = 4 #integer
B = 5.5 #floats or floating point numbers
C = "CSAEA" #string
D = True #boolean always return True or False

print(A, B, C, D)

# Operators
# + - / *  % ** //
# += -= /=
e = 3 - 1
print(e)
e = 22 ** 2
print(e)
e += 7
print(f"e is equal to {e}")
e -= 7
e += 12
print(f"e is now equal to {e}")
# COMPARISONS (booleans, which always return True of False)

#  <   >    <=   >=    ==    !+
print(4<5)
print(100000000<1)
print(7 == 4)
print(1 != 2)

isEqual = "Yes" != "YES"
print(isEqual)
# LOGICAL OPERATORS
# in order of prescedence: not and or
f = False
t = True
#predict output. DOn't run!
print(not f) #true
print( f and t) #False
print(f or t) #true
print(f or t and not f) #true

#CASTING ()

g = int(5.5)
print(g)
a = int(5.9)
print(a)

#STRINGS
s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2 + s3 # concatenation with +
end += ", Cowboy."

print(end)
print(end + "\n") # print(end + "\n") new line in code

# Math library
print(math.sqrt(14))
print(math.ceil(3.1))
print(math.floor(2.3))
print(math.pow(2, 4))

# CONDITIONALS
# if elif else
t = True
f = False
if f: 
    print("Reached the first condition")
elif t:
    print("Reached second condition")
else: 
    print("Reached else")
if 1 > 1 and 1==78: 
    print("Reached the first condition")
elif 6 == 7 or 2 != 2 or 5 == 23:
    print("Reached second condition")
elif 9 == 10 and 20 + 10 == 30:
    print("Reached third condition")
else: 
    print("Reached else")

    #Lists
    # A list can hold any type, and can grow or shrink at any time.
   #Index:  0   1  2 3  4
    nums = [34,52,3,64,32]
    print(nums)
    print(nums[2])
    print(nums[0])
    print(nums[4])
    numb = [6,7]
    print(numb[0])
    print(numb[1])
    print(nums[1] + nums [2])
    nums[0] = 64
    print(nums[0])

    #LIST METHODS
    #Special built-in methods

    words = []
    words.append("Word 1")
    words.append("Word 2")
    words.append("Word 3")
    print(words)

    words.remove("Word 1")
    words.insert(0,"Word 4")
    words[1] = "Word 5"
    length = len(words)
    print(words)
    print(length)