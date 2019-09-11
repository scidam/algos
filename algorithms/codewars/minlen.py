def minlen(s):
    return min([[x, y] for x, y in zip(range(len(s)), map(len, s.split()))], key=lambda x:x[1])[0]

minlen('sdfwe wefs wef')
