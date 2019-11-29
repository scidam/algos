# Bubbule sorting algorithm using recursion approach



arr = [1, 5, 39, 2, 5, 2, 1, 0, 47]

def bubble_sort_recursive(arr, maxind=len(arr)):
    print("Pre: ", arr)
    if maxind == 1:
        return
    for k in range(maxind - 1):
        if arr[k] > arr[k + 1]:
            arr[k], arr[k + 1] = arr[k + 1], arr[k]
    print("Post: ", arr)
    bubble_sort_recursive(arr, maxind=maxind - 1)

print("Original array: ", arr)
bubble_sort_recursive(arr)
print("Array sorted using bubble recursion: ", arr)