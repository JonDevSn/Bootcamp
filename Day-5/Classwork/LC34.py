def find_first(nums, target):
    left = 0
    right = len(nums) - 1
    first = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            first = mid
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return first