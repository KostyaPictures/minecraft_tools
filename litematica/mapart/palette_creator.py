import json

palette={}
with open("block_colors_with_non_solid.json", "r", encoding="UTF-8") as j:
    data = json.load(j)

    for block in ["minecraft:grass_block","minecraft:sandstone","minecraft:mushroom_stem","minecraft:redstone_block","minecraft:packed_ice", "minecraft:iron_block", "minecraft:bamboo_block", "minecraft:clay", "minecraft:jungle_planks", "minecraft:cobblestone", "minecraft:water", "minecraft:oak_planks", "minecraft:diorite", "minecraft:snow_block", "minecraft:acacia_planks", "minecraft:magenta_wool", "minecraft:light_blue_wool", "minecraft:bamboo_planks", "minecraft:lime_wool", "minecraft:pink_wool", "minecraft:gray_wool", "minecraft:light_gray_wool", "minecraft:cyan_wool", "minecraft:purple_wool", "minecraft:blue_wool", "minecraft:dark_oak_planks", "minecraft:green_wool", "minecraft:blue_wool", "minecraft:nether_wart_block", "minecraft:blackstone", "minecraft:gold_block", "minecraft:prismarine_bricks", "minecraft:lapis_block", "minecraft:emerald_block", "minecraft:spruce_planks", "minecraft:netherrack", "minecraft:white_terracotta", "minecraft:orange_terracotta", "minecraft:magenta_terracotta", "minecraft:light_blue_terracotta", "minecraft:yellow_terracotta", "minecraft:lime_terracotta", "minecraft:pink_terracotta", "minecraft:gray_terracotta", "minecraft:light_gray_terracotta", "minecraft:cyan_terracotta", "minecraft:purple_terracotta", "minecraft:blue_terracotta", "minecraft:brown_terracotta", "minecraft:green_terracotta", "minecraft:red_terracotta", "minecraft:black_terracotta", "minecraft:crimson_nylium", "minecraft:crimson_planks", "minecraft:crimson_hyphae", "minecraft:warped_nylium", "minecraft:warped_planks", "minecraft:warped_hyphae", "minecraft:warped_wart_block", "minecraft:cobbled_deepslate", "minecraft:raw_iron_block", "minecraft:verdant_froglight"]:
        palette.update({block: data[block]})

    with open("palette.json", "w", encoding="UTF-8") as f:
        f.seek(0)
        json.dump(palette, f, indent=2)
        f.truncate()