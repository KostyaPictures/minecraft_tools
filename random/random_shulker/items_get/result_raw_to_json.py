iWillUseOnlyOneItem = False
useOnlyNeeded = False

import json
def tryOpenJson():
    open("result.json","w",encoding="UTF-8").write("{}")

if not useOnlyNeeded:
    items=open("result_raw.txt","r",encoding="UTF-8").read().split("\n")
else:
    items=open("onlyNeeded.txt","r",encoding="UTF-8").read().split("\n")
if iWillUseOnlyOneItem:
    tryOpenJson()

    with open("result.json","r+",encoding="UTF-8") as f:
        res={}
        for item in items:
            res.update({item: 1})
        data = json.load(f)
        data.update(res)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()
else:
    tryOpenJson()
    with open("result.json","r+",encoding="UTF-8") as f:
        res={}
        for item in items:
            only1 = open("only1.txt","r",encoding="UTF-8").read().split("\n")
            only16 = open("only16.txt","r",encoding="UTF-8").read().split("\n")
            if item in only1:
                res.update({item: 1})
            elif item in only16:
                res.update({item: 16})
            else:
                res.update({item: 64})
        data = json.load(f)
        data.update(res)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()
