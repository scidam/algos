#          Number validation
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false


TOKEN_TYPES = ('DIG', 'MINUS', 'PLUS', 'EXP', 'POINT')

PLUS_PAT = '+'
MINUS_PAT = '-'
EXP_PAT = 'eE'
POINT_PAT = '.'
DIG_PAT = '1234567890'


def tokenize(s):
    result = list()
    i = 0
    while i < len(s) - 1:
        if s[i] == PLUS_PAT:
            result.append(('PLUS', ''))
        elif s[i] == MINUS_PAT:
            result.append(('MINUS', ''))
        elif s[i] in EXP_PAT:
            result.append(('EXP', ''))
        elif s[i] == POINT_PAT:
            result.append(('POINT', ''))
        elif s[i] in DIG_PAT:
            dig = ''
            k = i
            while s[k] in DIG_PAT and k < len(s) - 1:
                dig += s[k]
                k += 1
            i = k
            result.append(('DIG', dig))
            continue
        else:
            raise ValueError("This string contains illegal character {}".format(s[i]))
        i += 1
    return result


grammar = """
NUMBER ::= INT_NUMBER | FL_SIGNED | EXP_SIGNED
INT_NUMBER ::= [PLUS|MINUS] DIG
FL_SIGNED ::= [PLUS|MINUS] FL_NUMBER
FL_NUMBER ::= [DIG] POINT DIG
EXP_SIGNED ::= [PLUS|MINUS] EXP_NUMBER
EXP_NUMBER ::= [DIG] POINT DIG EXP [PLUS|MINUS] DIG
"""





