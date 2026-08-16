# Sum of a number till n suing recusrion
n = int(input("Enter a number: "))
def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

print(f"The sum of numbers till {n} is {sum_of_numbers(n)}") 
