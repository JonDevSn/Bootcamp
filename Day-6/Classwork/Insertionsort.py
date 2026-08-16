def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift larger elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Put key in its correct position
        arr[j + 1] = key

    return arr


arr = [5, 3, 4, 1, 2]
print(insertion_sort(arr))