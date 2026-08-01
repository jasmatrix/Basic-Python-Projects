def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))