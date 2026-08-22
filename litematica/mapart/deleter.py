import json

poping=[]
with open("block_colors.json", "r+", encoding="UTF-8") as f:
    data = json.load(f)
    for v in data:
        if ("infested" in v) or ("torch" in v) or ("lantern" in v) or (data[v]["colorName"]=="CLEAR") or ("glass" in v) or ("bed" in v) or ("copper" in v and not "waxed" in v) or ("stem" in v) or ("coral" in v and not "coral_block" in v) or ("flower" in v) or ("bush" in v) or ("banner" in v) or ("tulip" in v) or ("carpet" in v) or ("_bud" in v) or ("grass" in v) or ("stairs" in v) or ("slab" in v) or ("fence" in v) or ("wall" in v) or ("candle" in v) or ("candle" in v) or ("trapdoor" in v) or ("door" in v) or ("pressure_plate" in v) or ("sapling" in v) or ("sign" in v) or ("button" in v):
            poping.append(v)
    for p in poping:
        data.pop(p)
    f.seek(0)
    json.dump(data, f, indent=2)
    f.truncate()