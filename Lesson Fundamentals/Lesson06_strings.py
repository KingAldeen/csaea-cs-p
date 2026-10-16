# STRING MANIPULATION IN PYTHON
# built-in methods: len(), upper(), lower(), capitalize()

# greeting = "Hello"
# first_name = "Ada"
# last_name = "lovelace"
# print(greeting, first_name)

# #Option 1
# print(first_name, last_name)
# print(first_name + "Hello" + last_name)
# print(f"{first_name} {last_name}")

# # 0 1 2 3 4 
# # H e l l o
# greeting = "Hello"
# second_letter = greeting[1]
# print(second_letter)

# # String indexing and slicing
# word = "Super-cali-fragil-istic-expi-ali-docious"
# print("\n The First Word is", word)
# print("First letter is:", word[0])
# print("Last letter is:", word[-1])
# print("Range of letters (non-inclusive)", word[3:7] )
# print("First five letters:", word[:5])
# print("Everything after the first five letters", word[5:] )
# print("The last seven letters are", word[-7:] )
# print("Step through every second character:", word[::2])
# print("String in reverse", word[::-1])

# last_name = "Lovelace"
# length = len(last_name)
# print(length)
# print("Length of string:", length)

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

# favorite_quote = input("Whats your favorite quote: ")
# print(favorite_quote)
# length = len (favorite_quote)
# print(length)

# Challenge 2:
# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.

# any_word = input("Give me any word that is at least 7 characters long: ")
# print("The 2nd to 6th letter is", any_word[1:7])

# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Formatted name: Lovelace, Ada

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Formatted name: {last_name}, {first_name}")

character = "spOngEbOB SQuArPaNts"
print("\nLowercase:", character.lower())
print("Uppercase:", character.upper())
print("Capitalize first letter:", character.capitalize())
print("Title format:", character.title())

print()

#find and replace text
sentence = "I'm a goofy goober."
new_sentence = sentence.replace("I'm", "You're")
print(sentence)
print(new_sentence)

#JOIN AND SPLIT
groceries = "milk,eggs,bread,butter,peanuts"
print("\nOriginal string: ", groceries)

# Split the string into a Python list, based on a 'delimiter'
# Split the string into a Python list, based on a 'delimiter'
items = groceries.split(",")
print(items)

# Join a python list back into a string
joined = " and ".join(items)
print(joined)

print(type(items))
print(type(joined))

word = input("Enter Any word: ")
print("Lowercase:", word.lower())
print("Uppercase:", word.upper())
print("In Reverse:", word[::-1])