with open("Items.txt","r",encoding="UTF-8") as f:
    items=f.read()
items=items.split("\n")
final_items=[]
for item in items:
    item=item[::-1]
    for i in range(len(item)-1):
        if item[i]==" ":
            item=item[1:i].lower()[::-1]
            final_items.append(item)
            break
print(final_items)

res=""
for v in final_items:
    res+=v+"\n"
res=res[:-1]
print(res)
with open("result_raw.txt","w",encoding="UTF-8") as f:
    f.write(res)
