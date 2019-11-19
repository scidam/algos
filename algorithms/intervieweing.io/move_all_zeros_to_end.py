


# Move all zeros to the end of the array

arr = [1,5,0,2,3,0,1]

def move(arr):
    zc = 0
    st = list()
    for el in arr:
        if el != 0:
            st.append(el)
        else:
            zc += 1
    st.extend([0] * zc)
    return st


def memory_efc(arr):
    zpos = 0
    for k in range(len(arr)):
        if arr[k] != 0:
            arr[zpos], arr[k]  = arr[k], arr[zpos]
            zpos += 1
    return arr


print("Should return 1, 5, 2, 3, 1, 0, 0: ", memory_efc(arr))

