# AMIN

from PIL import Image

image = Image.open('./image_test.bmp')


def bintoint(binaire: str) -> int:
    '''
    renvoie l'integer qui correspond
    '''
    return int(binaire, 2)


def dernierbit(b: int) -> int:
    '''
    renvoie le dernier bit de la composante bleue
    '''
    return bin(b)[-1:]


def limitedetecter(img: list) -> int:
    '''
    renvoie la limite en integer
    '''
    temp = ""
    for x in range(16):
        r, g, b = img.getpixel((x, 0))
        temp += str(dernierbit(b))
    return bintoint(temp)


def imgbin(img: list) -> list:
    '''
    renvoie le dernier bit de la composante bleue de chaque pixel de l'image en entrée (sous forme de tableau)
    commence au 17ème pixel et tremine à la limite
    '''
    codeBinaire = []
    l, h = img.size
    increment = 0
    character = ""
    for x in range(17, l):
        for y in range(h):
            if increment < limitedetecter(img)*7:
                r, g, b = img.getpixel((x, y))
                if (increment+1) % 7 == 0:
                    codeBinaire.append(character)
                    character = dernierbit(b)
                else:
                    character += dernierbit(b)
                increment += 1
    return codeBinaire


def imgascii(binaire: list) -> str:
    '''
    Convertir un tableau de chiffres en binaire en texte ASCII
    '''
    texte = ""
    for code in binaire:
        texte += chr(bintoint(code))
    return texte


binary = imgbin(image)
print(binary)
print(imgascii(binary))
print("limite : " + str(limitedetecter(image)))
print("longueur : " + str(len(binary)))
