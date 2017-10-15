#Exercice7.2
def ligneCar(n,ca):
    chaine = ''
    for i in range(n):
        chaine += ca
    return chaine
if __name__ == "__main__":
    print(ligneCar(10, 'Ww'))
    assert ligneCar(10, 'Ww') == "WwWwWwWwWwWwWwWwWwWw"
######################################################
#Exercice7.3

from math import pi
def surfCercle(r):
    '''
    :param r:
    :return:
    '''
    return pi*r**2
if __name__ == "__main__":
    print(surfCercle(2.5))
    assert surfCercle(2.5) == pi*2.5**2

######################################################
#Exercice7.4
def volBoote(x,y,z):
    '''

    :param x:
    :param y:
    :param z:
    :return:
    '''
    return x*y*z
assert volBoote(3,2,4) == 24
print(volBoote(3,2,4))
#######################################################
#Exercice7.5
def maximum( x,y,z ):
    '''

    :param x:
    :param y:
    :param z:
    :return:
    '''
    if x == y == z:
        return x
    elif x > y and x > z :
        return x
    elif y> x and y > z :
        return y
    elif z > x and z >y :
        return z

if __name__ == "__main__":
    assert maximum(5,5,5) == 5
    assert maximum(2,5,8) == 8
    print(maximum(5,5,5))
########################################################
#Exercice7.9

def compteChar(ca,ch):
    '''

    :param ca:
    :param ch:
    :return:
    '''
    i = 0
    compte = 0
    while i < len(ch):
        if ch[i] == ca:
            compte = compte+1
        i = i +1
    return compte

if __name__ == "__main__":
    assert compteChar("b","bab") == 2
    assert compteChar(" ", "    ") == 4
    print(compteChar('e','Cette phrase est un exemple'))
############################################################
#Exercice7.10
def indexMax(liste):
    '''

    :param liste:
    :return:
    '''
    maxIndex = 0                            # supposons que l'element maximal est à l'index 0
    compteur = 0                            # le compteur ira de 0 à l'index du dernier element
    maxItem = liste[0]                      # suppsons le premier element de la liste comme maximal
    while compteur < len(liste):            # le compteur roule de 0 à len(liste)-1
        if liste[compteur] > maxItem:       # On compare la valeur à l'index à la première valeur de la liste
            maxItem = liste[compteur]       # On recadre la valeur maximal par rapport a la comparaison precedente
            maxIndex = compteur             # modifie maxIndex a chaque iteration
        compteur = compteur + 1             # On incremente le compteur pour passer a l'iteration suivante
    return maxIndex                         # doit quitter la loupe avant de retourner maxIndex
if __name__ == "__main__":
    assert indexMax([2,3,78,34,54,91,44,55,67,54]) == 5
    print("maxIndex: ",indexMax([2,3,78,34,504,91,44,55,67,54]))

############################################################
#Exercice7.11
def nomMois(n):
    '''
    :param n:
    :return:
    '''
    mois = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
    return mois[n-1]
if __name__ == "__main__":
    assert nomMois(4) == "Avril"
    assert nomMois(1) == "Janvier"
    print(nomMois(10))
#############################################################
#Exercice7.12
def inverse(ch):
    '''

    :param ch:
    :return:
    '''
    inv = ''                          # Une chaine vide qui va containir nos caracteres renversés
    for i in range(len(ch)-1,-1,-1):  # on loop de len(ch)-1 à 0 en regressant de -1
        inv += ch[i]                  # On concatine les pieces obtenues a inv
    return inv                        # on retourne inv

if __name__ == "__main__":
    assert inverse("mama") == "amam"
    assert inverse("dolo") == "olod"
    print(inverse("Brahima"))
#######################################################################
#Exercice7.13
def compteMots(phrase):
    espace = 0                        # compteur d'espace
    for i in range(0,len(phrase)):
        if phrase[i] == " ":
            espace = espace+1        # incremente le compteur d'espace
    return espace+1                  # notre de mot est egal au nombre d'espace si tous les espaces sont seulement contenue
if __name__  == "__main__":          #i l'interieur de la phrase
    assert compteMots("Je suis content") == 3
    assert compteMots("Je vais à mes rendez-vous") == 5
   