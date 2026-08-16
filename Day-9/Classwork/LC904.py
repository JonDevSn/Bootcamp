# Solve leetcode 904 
def totalFruit(fruits):
    # Initialize variables
    max_fruits = 0
    left = 0
    fruit_count = {}

    # Iterate through the fruits array
    for right in range(len(fruits)):
        # Add the current fruit to the count
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

        # If we have more than 2 types of fruits, shrink the window from the left
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        # Update the maximum number of fruits collected
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

