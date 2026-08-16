# Climbing stairs problem using recursion
def climb_stairs(n):
    if n <= 1:
        return 1
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)