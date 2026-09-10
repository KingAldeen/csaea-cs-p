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