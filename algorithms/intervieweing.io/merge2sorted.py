# Merge 2 sorted array, where one array has placeholders
# and the another one has presorted values. Resulting array should be
# sorted.

X = [1, 0, 5, 0, 7, 9, 0]
Y = [2, 6, 10]

def merge(X, Y):
    indx = 0
    posx = None
    while indx < len(X):
        if posx is None and X[indx] == 0:
            posx = indx
        if posx is not None:
            if X[indx] != 0:
                X[posx],  X[indx] = X[indx], X[posx]
                posx+=1
        indx += 1
       
    # merging arrays
    indy = 0
    indx = 0
    result = [0] * len(X)
    indr = 0
    while indy <= len(Y) - 1 and indx <= len(X) - 1:
        if Y[indy] < X[indx] or X[indx] == 0:
            result[indr] = Y[indy]
            indr += 1
            indy += 1
        elif  Y[indy] > X[indx]:
            result[indr] = X[indx]
            indx += 1
            indr += 1
        elif Y[indy] == X[indx]:
            result[indr] = X[indx]
            indx += 1
            indy += 1
            indr += 1
    return result

print("X = ", X)
print("Y = ", Y)
Z = merge(X, Y)
print("Z = ", Z)

        