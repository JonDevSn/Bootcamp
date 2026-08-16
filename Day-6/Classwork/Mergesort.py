def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [8, 3, 5, 4, 7, 6, 1, 2]

print(merge_sort(arr))