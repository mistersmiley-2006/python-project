# ETHAN
txt="le petit cheval dans la prairie"


def transfo(txt):
    '''
    '''
    long1=0
    long=len(txt)
    long1=bin(long)
    temp1=0
    list=[]
    list.append(long1)
    for element in txt :
        temp1=ord(element)
        temp1=bin(temp1)
        list.append(temp1)
        temp1=0
    return list

print(transfo(txt))