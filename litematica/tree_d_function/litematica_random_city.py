import time
################################## SEC1 100(0.1535915 s) x2(0.1507465 s) x3(0.1556018 s)
start=time.time_ns()
from litemapy import Schematic, Region, BlockState
import random

width=300
height=101
length=300
def f(x): #one point is chosen on abscissa from 0 to 1, ordinate represents building height
    return 100*((x-0.5)**2)+1
road_spacing=16
road_width=2
antenna_chance=0.3
blocks_={
    "minecraft:stone_bricks": 10,
    "minecraft:stone": 10,
    "minecraft:polished_tuff": 10,
    "minecraft:light_gray_stained_glass": 6,
    "minecraft:mossy_stone_bricks": 1
}

def normal_time(time_ns) -> str:
    time=time_ns/1_000_000_000
    result=""
    if time>=3600:
        result+=f"{time//3600}h "
        time%=3600
    if time>=60:
        result+=f"{time//60}m "
        time%=60
    result+=f"{time}s"
    return result


blocks_=[[block]*blocks_[block] for block in blocks_]
blocks=[]
for blocklist in blocks_:
    for block in blocklist:
        blocks.append(block)

def random_height():
    return int(f(random.random()))

reg = Region(0, 0, 0, width, height, length)
schem = reg.as_schematic(name="RandomCity", author="Kostya_Pictures", description="Made with litemapy")
road = BlockState("minecraft:gray_concrete")
antenna = BlockState("minecraft:iron_bars")

operations=0
there_are_buildings=False
first_time=True

################################## SEC2 100(0.1172267 s)(x10000) x2(0.5053375 s)(x4) x3(1.059631 s)(x9)
for x in range(width):
    time_start=time.time_ns()
    for z in range(length):
        if x%road_spacing>road_width-1 and z%road_spacing>road_width-1:
            there_are_buildings=True
            skyscraper_height=random_height()
            block=BlockState(random.choice(blocks))
            for y in range(skyscraper_height):
                reg[x, y, z] = block
            if random.random()<antenna_chance:
                reg[x, y+1, z] = antenna
        else:
            reg[x, 0, z] = road
    time_end=time.time_ns()
    if first_time and there_are_buildings:
        #for i9 3.6 GHz 64GB RAM its 83287 ns
        estimated=(time_end-time_start)*width+83287*width*length
        print("Estimated Time:",normal_time(estimated))
        first_time=False
################################## SEC3 100(0.8328699 s)(x10000) x2(3.3142538 s)(x4) x3(7.5267474 s)(x9)
schem.save("city.litematic")
realtime=time.time_ns()-start
print(f"Real Time: {normal_time(realtime)}, Inaccuracy: {round(1-(estimated/realtime),4)*100}% (\"-\" means, that it was faster)")