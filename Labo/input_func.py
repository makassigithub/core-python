#input can take an optional "text" param that's printed when called
# name = input("enter your name please \n")
# print("welcome",name )
# age  = input("would you enter your age ? \n")
# print("you already have",age,"year's old",name,"!")



#Exercice 2.1
#Écrivez un programme qui permet de saisir le nom de l’utilisateur (avec la
#fonction input()) et de renvoyer "Bonjour", suivi de ce nom.
# name = input("ecris le nom\n")
# print("Bonjour",name)

# Exercice 2.2
# Ajoutez au programme le code qui demande à l’utilisateur son année
# de naissance et qui a che son âge après lui avoir dit bonjour.
# L’année courante sera mise dans une variable.
# current_year = 2017
# name = input("ecris le nom\n")
# birth_year = int(input("ecris ton année de naissance\n"))
# print("Bonjour",name,"vous avez",current_year-birth_year,"ans")

#Exercice 2.3
# valeur1 = int(input("Entre une premiere valeur\n"))
# valeur2 = int(input("Entre une deuxieme valeur\n"))
# print("la sommes des valeurs est", valeur1+valeur2)
# # Or parse when printing
# valeur1 = input("Entre une premiere valeur\n")
# valeur2 = input("Entre une deuxieme valeur\n")
# print("la sommes des valeurs est", int(valeur1)+int(valeur2))

#Exercice 2.4
# import math
# Xa = float(input("entre l'abscisse Xa du point a\n"))
# Ya = float(input("entre l'ordonnée Ya du point a\n"))
# Xb = float(input("entre l'abscisse Xb du point b\n"))
# Yb = float(input("entre l'ordonnée Yb du point b\n"))
# print("la distance entre les point a et b est:",math.sqrt((Xb-Xa)**2+(Yb-Ya)**2))


#Formating Strings
# my_age = 45.5
# my_name = "Brahima"
# print("%s is my name" % my_name) # use %s for strings
# print("I am %d's years old"% my_age) # use %d for numerics
# print("%s is %d year's old"%(my_name,my_age))# can format many params together


