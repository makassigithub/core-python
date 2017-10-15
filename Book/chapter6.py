#6.1 Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie
#par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)
#mp = float(input("enter speed :\n"))
#print("the equivalent in km/h is: ", (mp*1609)/1000)
#print("the equivalent in m/ is: ", ((mp*1609)/1000)*1000/3600)


#######################################################################
def isPremier(n):
    '''
    Cette fonction permet de verifier si le nombre est premier. Elle est aussi performante car
    elle imprime True quand elle trouve le premier diviseur de n

    :param n: doit etre te type in, la valeur à passer a la fonction
    :return: la fonction ne retourne un boolean
    '''
    for i in range(2,n):
        print(i)                                                        # affiche les valeurs successives de position
        if n % i == 0:
            return False # return False pour la premiere valeur qui divise n
    return True # si auncune valeur n'est trouvé entre 2 et n-1, on quitte la boucle et return True

#######################################################################
def isPremier2(n):
    '''
    Cette fonction permet de verifier si le nombre est premier. Elle est aussi performante car
    elle imprime True quand elle trouve le premier diviseur de n
    :param n:
    :return:
    '''
    position = 2
    while position <= n-1:
        print(position)                                                # affiche les valeurs successives de position
        if n % position == 0:
            return False
        position = position+1
    return True
#######################################################################
def isPremier3(n):
    '''
    Retrouver la premiere valeur qui divise n
    cette fonction optimise la recherche de notre de premier
    :param n: doit etre te type in, la valeur à passer a la fonction
    :return: la fonction ne retourne rien elle doit juste imprimer le resultat

    '''
    premier = True
    position = 1                               # nous incrementons position avant le traitememt qui commence a 2
    while position <= n-2 and premier:         # le boucle doit s'arreter a n-1, puisque nous incrementons position                                               # avant la verification, nous allons à n-2
        position = position+1                  # affiche les valeurs successives de position
        print(position)
        premier = n % position != 0
    if position == n-1:                        # si n est premier la valeur maximale de position sera n-1
        return True
    else:
        return False

print('isPremier(99)',isPremier(99))
print('isPremier(137)',isPremier(137))


print('isPremier2(99)',isPremier3(99))
print('isPremier2(137)',isPremier3(137))


print('isPremier3(99)',isPremier3(99))
print('isPremier3(137)',isPremier3(137))
