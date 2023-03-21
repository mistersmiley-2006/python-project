# AMIN

from PIL import Image
from easygui import *

image = Image.open('image_test.bmp')

def imgbin(img:list)->list:
    '''
    renvoie le dernier bit de la composante bleue de chaque pixel de l'image en entrée (sous forme de tableau)
    '''
    codeBinaire = []
    l,h = img.size
    for x in range(l):
        for y in range(h):
            r,g,b=img.getpixel((x,y))
            codeBinaire.append(bin(b)[-1:])
    return codeBinaire

def imgascii(binaire:list)->str:
    '''
    Convertir un tableau de chiffres en binaire en texte ASCII, le programme s'arrête à la fin de la limite de caractère écrite dans les 16 premiers bits
    '''
    limite = ""
    increment = 0
    character = ""
    codeASCII = ""
    for bit in binaire :
        if increment < 16 :
            limite += bit
        elif increment==16 :
            limite = int(limite,2)
        else :
            if increment % 8 == 0 :
                codeASCII += chr(int(character,2))
                character = ""
            else :
                character += bit
        increment += 1
    return codeASCII

msgbox((imgascii(imgbin(image))))
            
            


