# Shuffle input array using Fisher-Yates algorithm


import random
arr = list(range(10))



def shuffle(arr):
    n = len(arr)
    for j in range(len(arr)-1):
        i = random.randint(0, j)
        arr[i], arr[j] = arr[j], arr[i]
    return arr




print("Before shuffling: ", arr)
print("After shuffling: ", shuffle(arr))