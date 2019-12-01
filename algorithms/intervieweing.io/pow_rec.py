# Recursive implementation of pow(x, n)


def pow_rec(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    p = pow_rec(x, n // 2)
    if n & 1:
        return x * p * p
    else:
        return p * p

print(pow_rec(2, 100))