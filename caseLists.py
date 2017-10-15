# 5.11  Soient les listes suivantes :
#   t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
#   'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
#   Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des
#   deux listes en les alternant, de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :
#   ['Janvier',31,'Février',28,'Mars',31, etc...].


t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
  'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3=[]
counter = 0
while counter < len(t1):
   t3.append(t2[counter])
   t3.append(t1[counter])
   counter = counter +1
print(t3)


#5.12 Écrivez un programme qui affiche « proprement » tous les éléments d’une liste. Si on l’appliquait
#  par exemple à la liste t2 de l’exercice ci-dessus, on devrait obtenir :
#  Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre
#  Décembre

index = 0
while index < len(t2):
    print(t2[index], end = " ")
    index = index +1

#5.13 Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée.
#  Par exemple,sionl’appliquaitàlaliste[32, 5, 12, 8, 3, 75, 2, 15],ceprogrammedevrait afficher :
#  le plus grand élément de cette liste a la valeur 75.

t4 = [32, 5, 12, 8, 3, 75, 2, 15]
print("le plus grand élément de cette liste a la valeur ",max(t4))

#5.14 Écrivez un programme qui analyse un par un tous les éléments d’une liste de nombres
#  (par exemple celle de l’exercice précédent) pour générer deux nouvelles listes.
#  L’une contiendra seulement les nombres pairs de la liste initiale, et l’autre les nombres impairs.
#  Par exemple, si la liste initiale est celle de l’exercice précédent, le programme devra construire
#  une liste pairs quicontiendra[32, 12, 8, 2],etunelisteimpairsquicontiendra[5, 3, 75, 15].
#  Astuce: pensez à utiliser l’opérateur modulo (%) déjà cité précédemment.

t5 = [32, 5, 12, 8, 3, 75, 2, 15]
t_pair = []
t_impair = []
compteur = 0
while compteur < len(t5):
    if t5[compteur]%2 == 0:
        t_pair.append(t5[compteur])
    else:
        t_impair.append(t5[compteur])
    compteur = compteur + 1
print("t_pair: ",t_pair)
print("t_impair: ",t_impair)

# 5.15 Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots
# (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'])
# pour générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères,
# l’autre les mots comportant 6 caractères ou davantage.

t6 = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
lessThan6 = []
moreThan6 = []
compt = 0
while compt < len(t6):
    if len(t6[compt]) < 6:
        lessThan6.append(t6[compt])
    else:
        moreThan6.append(t6[compt])
    compt = compt + 1
print("lessThan6: ",lessThan6)
print("moreThan6: ",moreThan6)

# sum  des elements d'une liste
def somme(list):
    '''
    Calcul la somme d'une liste de nombre passé en argument
    :param list: la liste de nombra passé en argument
    :return: la somme retournées.
    '''
    total = 0
    for i in list:
        total += i
    return total


def element_unique(list):
    """
    :param list:
    :return:
    """
    unique = []
    for i in list:
        if list.count(i)== 1:
            unique.append(i)
    return unique

# Utilisation des methodes de collection
from collections import Counter
def element_unique2(liste):
    return list(Counter(liste).keys())

def element_unique3(liste):
    uniq = []
    for i in liste:
        if i not in uniq:
            uniq.append(i)
    return uniq

# a Set is a Collection of unique elements. must be converted to list()
def element_unique4(ma_liste):
    return list(set(ma_liste))


if __name__ =="__main__":
    print("somme 1...5: {}".format(somme([1,2,4,5])))
    print("element_unique: ",element_unique([1, 2, 2,4,4, 5]))