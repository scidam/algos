# find longest subsequence of a given array

arr = [2, 80, 60, 70, 3, 4, 5, 6]
#arr = [2, 3, 6]

longest =list()
def get_longest(arr, longest=longest, current_index=0):
    if current_index == len(arr):
        return
    if longest:
        if current_index > 0 and longest[-1] < arr[current_index]:
            longest.append(arr[current_index])
            current_index+=1
        else:
            longest.pop()
    else:
        longest.append(arr[current_index])
        current_index+=1
    get_longest(arr, longest=longest, current_index=current_index)


get_longest(arr, longest=longest, current_index=0)
print(longest)

get_longest(arr)
print(longest)
