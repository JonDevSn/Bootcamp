# print number from 5 to 1 using recursion
def print_numbers(n):
    if n > 0:
        print(n)
        print_numbers(n - 1)
print_numbers(5) 