


s = [0,1,0,0,1]


def find_bin(s):
    number = eval('0b' + ''.join(s))  # not safe, but fast
    right_part = list()
    left_part = list()
    right_part.append(number)
    left_part.append(0)
    for r in range(len(s)):
        if s[r] == 0:
            right_part.append(right_part[-1])
            left_part.append(left_part[-1] * 2)
        elif s[r] == 1:
            right_part.append(right_part[-1] % 2)
            left_part.append(left_part[-1] * 2 + 1)
    j = len(s)
    i = 0
    while j > i:
        if right_part[j] == left_part[i]:
            return i, j


    else:
        return [-1, -1]


