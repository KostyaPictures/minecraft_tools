file='block\\acacia_planks.png'

from PIL import Image
import sys
import os

im = Image.open(file, 'r')
im = im.resize(size=(1, 1))
im=im.convert(colors=(2**32))
pix_val = list(im.getdata())
print(pix_val)


blocks=os.listdir("block")
trash=[]
for block in blocks:
    if block[-3:]!="png":
        trash.append(block)
    print(block[:-4])
blocks=[f for f in blocks if f not in trash] # АХУЕТЬ, Я ЭТУ СТРОКУ САМ НАПИСАЛ
# короче удаляет из списка всё кроме png

print(blocks)

