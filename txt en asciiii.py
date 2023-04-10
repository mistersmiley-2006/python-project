# ETHAN
txt="le petit cheval dans la prairie"

def longueur(txt:str)->int:
    '''
    calcul la longueur du texte et la renvoie sur 16 bits
    '''
    long=bin(len(txt))[2:]          #long prends la valeur de la longueur du texte et passe ce nombre en binaire puis enleve le 0b
    while len(long)<16:             #regarde si la longueur du texte en binaire est inferieur a 16 si oui elle repete le nombre de fois l instruction ci dessous jusqu a que ce nombre de caractere en binaire soit de 16
        long='0'+long               #ajoute des 0 a long
    return long
    
    
    
    

def transfo (txt:str)->list:
    '''
    La fonction transfo prends comme parametre le texte qui est 
    demmander et utilise la fonction longueur pour calculer le nombre 
    de fois qu une instruction devrais être repete. La fonction 
    transforme donc le texte en ascii puis en binaire pour ensuite
    mettre tout ces chaîne de chiffre dans une liste.
    '''
    lettre=0
    list=[]                             #creer une liste vide
    list.append(longueur(txt))          #remplie cette meme liste en utilisant la fonction longueur 
    for element in txt:                 #parcour les element du texte 
        lettre=bin(ord(element))[2:]    #defini lettre en prenant l element 
        while len(lettre)<8:
            lettre='0'+lettre
        list.append(lettre)
    return list



def separation(txt:str)->list:
    '''
    Fonction qui separe chacun des caracteres de la liste forme par 
    la fonction transfo
    '''
    liste=[]
    for element in transfo(txt):
        for chiffre in element:
            liste.append(",".join(chiffre))
    return liste



def verification(txt:str)->list:
    '''
    '''
    compt=0
    for element in separation(txt):
        compt+=1
    return compt        