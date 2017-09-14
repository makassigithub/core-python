# Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7.
a = 0
while a < 20:
    a = a+1
    print(7*a, end=" ")

#Écrivez un programme qui affiche une table de conversion de sommes d’argent exprimées en
#euros, en dollars canadiens. La progression des sommes de la table sera « géométrique »,
#comme dans l’exemple ci-dessous

print("\n")
e, count = 1, 0
while e <= 16384:
    print(e,' euro',' = ',1.65*e,' cad')
    e = e*2

#Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit égal au triple du terme précédent.

b =c = count = 1
while count <= 12:
    print(c)
    b=c
    c= 3*b
    count = count +1

# Premier essai de script Python
# petit programme simple affichant une suite de Fibonacci, c.à.d. une suite
# de nombres dont chaque terme est égal à la somme des deux précédents.

print("Suite de Fibonacci :")

a,b,c = 1,1,1              # a & b servent au calcul des termes successifs
                           # c est un simple compteur
print(b)                   # affichage du premier terme
while c<15:                # nous afficherons 15 termes au total
    a,b,c = b,a+b,c+1
    print(b)


#4.5 Écrivez un programme qui calcule le volume d’un parallélépipède rectangle dont sont fournis au départ
#  la largeur, la hauteur et la profondeur.


#4.7 Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7,
#  en signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
#Exemple: 7 14 21*28 35 42*49...


# 5.4 Écrivez un programme qui calcule les intérêts accumulés chaque année pendant 20 ans,
# par capitalisation d’une somme de 100 euros placée en banque au taux fixe de 4,3 %
b = 1
while b <21 :
    print(b , ': ', b*(100*(4.3/100)))
    b = b+1

#5.5 Une légende de l’Inde ancienne raconte que le jeu d’échecs a été inventé par un vieux sage,
# que son roi voulut remercier en lui affirmant qu’il lui accorderait n’importe quel cadeau en récompense.
#  Le vieux sage demanda qu’on lui fournisse simplement un peu de riz pour ses vieux jours,
#  et plus précisément un nombre de grains de riz suffisant pour que l’on puisse en déposer 1 seul sur la première case du jeu qu’il venait d’inventer, deux sur la suivante, quatre sur la troisième, et ainsi de suite jusqu’à la 64e case.
#  Écrivez un programme Python qui affiche le nombre de grains à déposer sur chacune des 64 cases du jeu.
#  Calculez ce nombre de deux manières :
#  le nombre exact de grains (nombre entier) ;
#   lenombredegrainsennotationscientifique(nombreréel).
a,b = 1,1
while b <=64 :
   print(b, ' : ', a)
   a,b = a*2,b+1

# Writing as b as float
a,b = 1,1.
while b < 65 :
   print(b, ' : ', a)
   a,b = a*2,b+1

