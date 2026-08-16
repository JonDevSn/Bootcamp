n = int(input("Enter a number: "))
def print_numbers(n):
    if n > 0:
        print(n)
        print_numbers(n - 1)

print_numbers(n)