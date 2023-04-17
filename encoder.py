from PIL import Image

image = Image.open("image_test.bmp")

def TailleImgSuffisante(img: list, textAscii:list) ->bool:
    '''
    Renvoie un booleen vrai si la taille de l'image est suffisante
    pour coder le texte dedans.
    img : l'image dans laquelle on veut mettre le texte
    textAscii : le texte en binaire
    '''
    # calcule de la definition de l'image
    l, h = img.size

    if l*h > len(textAscii): # verifie si la definition de l'image est suffisante
        return True
    return False

def EncoderImage(img: list,textAscii:list)->list:
    '''
    Code le message dans l'image
    img : l'image a modifier
    textAscii : la liste contenant le message sous forme binaire
    '''
    if TailleImgSuffisante(img, textAscii):

        # definition de la taille de l'image et des coordonnée
        l, h = img.size 
        x, y = 16, 0

        for i in range(len(textAscii)):
            r, g, b = img.getpixel((x, y)) # on recupère la couleur

            if textAscii[i] != int(bin(b)[-1]): # on verifie si on a besoin de modifier le bleu
                b -= 1 # -1 pour changer le bit de 1

            img.putpixel((x, y), (r, g, b)) # on injecte la nouvelle couleur

            # conditions au cas ou on arrive au bout de la ligne de l'image
            if x >= l:
                x = 0
                y += 1
            else:
                x +=1

        return img
    else:
        print("Erreur : la taille de l'image est insuffisante pour coder le texte")
        return None
    