def bubble_sort(arr):
    while True:
        trocou = False
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                trocou = True
            print(i, "=>", arr)
        if not trocou:
            break
    return arr

arr = [5, 3, 8, 2, 1, 4]
print(bubble_sort(arr))

