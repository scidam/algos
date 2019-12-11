arr =[1,2,0,3,0,0,4,5,6,0]

def move_zeros(arr):
    """ Move zeros to the end of the array """

    mem = 0
    index = 0
    while index < len(arr):
        if arr[index] != 0:
            arr[index], arr[mem] = arr[mem], arr[index]
            mem += 1
        index += 1

move_zeros(arr)
print(arr)
