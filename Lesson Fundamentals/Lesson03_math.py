#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 743543 + 24
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)
float_divide =  10 / 3
print("Float division:", float_divide)
integer_divide= 7 // 2
print("Integer Divide", integer_divide)

mod = 7 % 2
print("Modulus", mod)

exponent = 7 ** 2
print("Exponent", exponent)


#PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = 2 + 3 * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result 3:", result3)

width = 8
height = 5
result4 = width * height
print("Result 4:" ,result4)

pie = 3.14
radius = 7
area_of_circle = (7 ** 2) * pie
print("Result 5:", area_of_circle )

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.

book = 12.99
amount_of_books = 3
notebook = 3.50
amount_of_notebooks = 4
total_cost = book * amount_of_books + notebook * amount_of_notebooks
print(f" Book ${book} \n Notebook ${notebook} \n Total Cost ${total_cost} ")

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 

number = 57
mod = number % 2
print(mod)
if number % 2 == 1:
    print("Odd")
else:
    print("Even")