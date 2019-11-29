# Merge M presorted lists

import heapq

import random

def generate_data(M, N1, N2):
    result = []
    for j in range(M):
        result.append(sorted((random.randint(0, 100) for k in range(random.randint(N1, N2))), reverse=True))
    return result


print(generate_data(5, 4, 8))


def sort_data(arr):
    result = []
    heap = []
    for j in range(len(arr)):
        if arr[j]:
            heapq.heappush(heap, arr[j].pop())
    while any(arr):
        result.append(heapq.heappop(heap))
        for j in range(len(arr)):
            if arr[j]:
                heapq.heappush(heap, arr[j].pop())
    while heap:
        result.append(heapq.heappop(heap))
    return result

data = generate_data(5, 4, 8)
print("Original data:")
for d in data:
    print(d)

sorted_data = sort_data(data)
print("Sorted data: ", sorted_data)
