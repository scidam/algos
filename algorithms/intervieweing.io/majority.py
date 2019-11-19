arr = [1,2,1,2,3,2,4,2,3,2,2]


def find_majority(arr):
    """Boyer-Moore algorithm"""

    major = None
    counter = 0
    for el in arr:
        print("Major element: ", major, "Current element: ", el)
        if counter == 0:
            major = el
            counter += 1
        elif el == major:
            counter += 1
        elif el != major:
            counter -= 1
    return major

print("Majority element: ", find_majority(arr))

