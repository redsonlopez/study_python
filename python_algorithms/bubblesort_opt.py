def opt_bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - 1, i - 1, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            print(i, " - ", j, "=>", arr)
    return arr

arr = [5, 3, 8, 2, 1, 4]
print(opt_bubble_sort(arr))

