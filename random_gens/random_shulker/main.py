chance = 1/3 # Approximately how much space will be occupied in a shulker
# For example, if chance = 1/3 (0.333..), then it will most likely to occupy 9 shulker slots (27* 1/3).
# ("most likely" because of standard distribution)
maxCount = 64 # Maximum item count (1..maxCount)
# (problems may occur with non 64-stackable items)
ask = True # Gives you choice over what will you get
askCount = 3 # How many choices the script will give you (if "ask" is set to True)
# For example, if askCount=3, then the script will ask you: 1.cherry_pressure_plate or 2.jungle_wood or 3.chiseled_deepslate?
# (you need to enter number in console to choose)

res="/give @p minecraft:shulker_box[container=["

import json
f=open("items_get\\result.json","r",encoding="UTF-8")
items=json.load(f)
itemNames=[]
for item in items:
    itemNames.append(item)


import random as r
for slot in range(27):
    if r.random()<chance:
        if not ask:
            randomItem = r.choice(itemNames)
        else:
            l=[r.choice(itemNames) for _ in range(askCount)]
            askRes=""
            i=0
            for a in l:
                i+=1
                askRes+=str(i)+"."+a+" or "
            askRes=askRes[:-4]+"?"
            print(askRes)
            inp=int(input())
            randomItem = l[inp-1]

        stack = items[randomItem]

        res+=f"{{item:{{count:{r.randint(1,stack)},id:\"minecraft:{randomItem}\"}},slot:{slot}}},"

res=res[:-1]
res+="]]"

open("result.txt","w",encoding="UTF-8").write(res)