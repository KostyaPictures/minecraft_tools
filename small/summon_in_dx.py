x=-184
y=-11
z=-292
dx=32
dy=0
dz=32
tag="kill"
type="minecraft:villager"
count=30
#/summon minecraft:villager ~ ~ ~ {Tags:["kill"]}

import random
f=open("output.txt", "w", encoding="UTF-8")
res=""
for _ in range(count):
    res+="summon "+type+" "+str(random.randint(x, x+dx))+" "+str(random.randint(y, y+dy))+" "+str(random.randint(z, z+dz))+" {Tags:[\""+tag+"\"]}\n"
print(res)
f.write(res)
