# variables
print("hello" * 10)       # string multiplication
print(10*10 + 10/2)      # arithmetic operations
print(10 % 3)  # divides two numbers but prints only the remainder
print(10 // 3)  # divides two numbers but prints only the whole number
print(2 ** 3)  # exponentiation - raises number to the power of another number


students_uni = 1000, 2000, 3000

average_grade = 5.5             # Float

male_students = True            # Boolean
female_students = False         # Boolean

students_name = 'Roman'
food = "chicken"       # String

email_massage = """
Hello, Man

How are ya doing?
"""                     # Multiline String

print(len(students_name))   # len() function - length of string


print(food[0])          # indexing - first letter of string
print(food[-1])         # indexing - last letter of string
print(food[0:3])       # slicing - first 3 letters of string
print(food[:])         # slicing - whole string

course = "DCU \"Students\""     # Escape sequence - \ just saves the " character
name = "Roman \nPryima"         # Escape sequence - \n creates a new line
print(name)

first = "Roman"
last = "Pryima"

full_name = f"{first} {last}"
# f-string - is used to combine variables and text and also anything can be put inside of it
full_name = f"{len(first)} {25 + 15}"
print(full_name)

course = "Python for Beginners  "
print(course.upper())  # string method - makes all letters uppercase
print(course.lower())  # string method - makes all letters lowercase
print(course.title())  # string method - makes first letter of each word uppercase
# string method - removes whitespace from the left side or the right side of the from both if strip()
print(course.lstrip())
print(course.find("for"))  # finds the index of desired string
# replaces the first string with the second string
print(course.replace("Py", "IDK"))
# checks if the string is present in the variable and returns boolean value
print("for" in course)
# checks if the string is not present in the variable and returns boolean value
print("Beg" not in course)
