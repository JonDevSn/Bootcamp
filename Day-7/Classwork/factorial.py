# Find factorial of a number using recursion
n = int(input("Enter a number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"The factorial of {n} is {factorial(n)}") 