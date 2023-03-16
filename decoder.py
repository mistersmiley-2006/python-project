# AMIN

from PIL import Image
from easygui import *



image = Image.open('image.bmp')
def imgbin() :
    l,h = image.size
    for x in range(l):
        for y in range(h):
            r,g,b=image.getpixel((x,y))
            moyenne=int((r+g+b)/3)
            image.putpixel((x,y),(moyenne,moyenne,moyenne))


msgbox(msg)