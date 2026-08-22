colors=["7","8","f"]
#↑↑↑ modify colors here

inp=input()

import random as r
res=""
for ch in inp:
    res+="§"+r.choice(colors)
    res+=ch

print(res)
