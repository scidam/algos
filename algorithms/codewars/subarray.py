
# my solution
def maxsubarray(arr):
    print(arr)
    if not arr:
        return 0
    if min(arr) >= 0:
        return sum(arr)
    if max(arr) < 0:
        return 0
    init = arr[0]
    for j in range(1, len(arr)):
        if arr[j] <= 0:
            pass
        else:
            maxres = max(sum(arr[k:j+1]) for k in range(j-1, -1, -1))
            if  maxres > init:
                init = maxres
    return init
            
            
# best solution
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
        
print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

