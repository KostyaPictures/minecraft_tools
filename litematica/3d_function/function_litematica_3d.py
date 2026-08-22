# import nbtlib
#
# demo = nbtlib.load('test.litematic')
# try:
#     assert demo['Version'] == 7
# except AssertionError:
#     print("Wrong version!")
#
# print(demo)
#
# from nbtlib.tag import Int
# demo['Version'] = Int(7)
# demo.save()



import litemapy
from numpy import *

from litemapy import Schematic, Region, BlockState

# Shortcut to create a schematic with a single region
reg = Region(0, 0, 0, 101, 101, 101)
schem = reg.as_schematic(name="Function", author="Kostya_Pictures", description="Made with litemapy")
block = BlockState("minecraft:light_blue_concrete")

for x, y, z in reg.block_positions():
    fx=x-50
    fy=y-50
    fz=z-50
    if fy<=45/(0.05*sqrt(1.8*(fx**2+fz**2+100)))-25: #round(((x-10)**2 + (y-10)**2 + (z-10)**2)**.5) <= 10:
        reg[x, y, z] = block

schem.save("function.litematic")


# schem = Schematic.load("planet.litematic")
# reg = list(schem.regions.values())[0]

# for x in reg.xrange():
#     for z in reg.zrange():
#         b = reg[x, 10, z]
#         if b.id == "minecraft:air":
#             print(" ", end="")
#         else:
#             print("#", end='')
#     print()