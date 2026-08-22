file='1.png'
author="Kostya_Pictures"
#The main reason I created this script is to make open-sourced script for maparts
#Also just for fun

from PIL import Image
import json
from litemapy import Schematic, Region, BlockState

def find_color(r,g,b):
    with open("block_colors.json", "r+", encoding="UTF-8") as j:
        data = json.load(j)
        min_dif=["block",9999999]
        for block in data:
            dr=abs(data[block]["r"]-r)
            dg=abs(data[block]["g"]-g)
            db=abs(data[block]["b"]-b)
            diff=dr+dg+db
            if diff<min_dif[1]:
                min_dif[1]=diff
                min_dif[0]=block
        return min_dif


im = Image.open(file, 'r')
pix_val = list(im.getdata())
size=im.size

if im.width>im.height:
    coordinates = ((im.width-im.height)/2, 0, im.width-(im.width-im.height)/2, im.height)
    im = im.crop(coordinates)
elif im.width<im.height:
    coordinates = (0, (im.height-im.width)/2, im.width, im.height-(im.height-im.width)/2)
    im = im.crop(coordinates)
else:
    pass

if im.width*im.height!=128*128:
    im = im.resize(size=(128, 128))
im.save('scaled_image.png')


im = Image.open('scaled_image.png', 'r')
pix_val = list(im.getdata())
size=im.size

width=128
length=128

reg = Region(0, 0, 0, width, 1, length)
schem = reg.as_schematic(name="mapart", author=author, description="Made with litemapy")

x=0
z=0
for p in pix_val:
    r,g,b=p[0], p[1], p[2]
    block=BlockState(find_color(r,g,b)[0])

    reg[x, 0, z] = block

    x+=1
    if x%width==0:
        x=0
        z+=1

schem.save("mapart.litematic")