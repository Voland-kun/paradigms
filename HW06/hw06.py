def binary_search(arr, val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 3
print(binary_search(arr, val))
