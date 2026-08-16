# print number from 1 to 5 using recursion
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n) 

print_numbers(5)  