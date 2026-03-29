x = input("Enter a number: ")
y = input("Enter another number: ")
try:
    result = int(x) + int(y)
    print("The sum is:", result)
except ValueError:
    print("Please enter valid numbers.")