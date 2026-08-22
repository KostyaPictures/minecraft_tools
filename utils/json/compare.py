file1="input/small.json"
file2="input/big.json"

import json
f1=open(file1, encoding="UTF-8")
data1=json.load(f1)
f2=open(file2, encoding="UTF-8")
data2=json.load(f2)


print("MISSING:")
for v in data2:
    if v not in data1:
        print(f" \"{v}\": \"{data2[v]}\",")