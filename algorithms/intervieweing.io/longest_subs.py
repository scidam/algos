
# Longest increasing subsequence (contigouos)


arr = [2, 6, 3, 4, 1, 2, 9, 5, 8]

def longest_subs(arr):
    current_subs = list()
    longest_subs = list()
    for k in range(len(arr) - 1):
        if arr[k] <= arr[k + 1]:
            if k not in current_subs:
                current_subs.append(k)
            if k + 1 not in current_subs:
                current_subs.append(k + 1)
            if len(longest_subs) < len(current_subs):
                longest_subs = current_subs[:]
        else:
            current_subs = list()
    return [arr[k] for k in longest_subs]


print(longest_subs(arr))
