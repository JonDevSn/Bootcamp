def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping happened, array is already sorted
        if not swapped:
            break

    return arr


arr = [5, 2, 8, 1, 3]
print(bubble_sort(arr))