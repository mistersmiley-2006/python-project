from PIL import Image

image = Image.open("image_test.bmp")

def EncoderImage(img: list,textAscii:list)->list:
    '''
    Code le message dans l'image
    img : l'image a modifier
    textAscii : la liste contenant le message sous forme binaire
    '''
    l, h = img.size 
    i = 0
    msgSize = len(textAscii)
    for x in range(l):
        for y in range(h):
            if i >= msgSize:
                return img
            r, g, b = img.getpixel((x, y))
            if textAscii[i] != bin(b)[-1:]:
                bin(b)[-1:] = textAscii[i]
            i += 1
    return img
