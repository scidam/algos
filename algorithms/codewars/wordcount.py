
from collections import Counter
import re

def wordcount(s):
    word_pat = re.compile("[a-z\'\-]+")
    letter_pat = re.compile(".*[a-z]+.*")
    c = Counter()
    for item in s.lower():
        w = next(iter(word_pat.findall(item)), '')
        if w and letter_pat.match(w):
            c[w] += 1
    return list(map(lambda x: x[0], sorted([(item[0], item[1]) for item in c.most_common(3)], key=lambda x: x[1])))



print(wordcount(""" 'this is 'this and this is this this qgcwve'f qgcwve'f qgcwve'f' qgcwve'f' qgcwve'f' qgcwve'f'"""))
print(wordcount(""" '' """))


          
