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

#Exercice 2.4
std1_name = input("Entrez nom de l'etudiant1\n")
std1_num = int(input("Entrez numero de l'etudiant1\n"))
std1_grade1= float(input("Entrez note1 de l'etudiant1\n"))
std1_grade2= float(input("Entrez note2 de l'etudiant1\n"))

std2_name = input("Entrez nom de l'etudiant2\n")
std2_num = int(input("Entrez numero de l'etudiant2\n"))
std2_grade1= float(input("Entrez note1 de l'etudiant2\n"))
std2_grade2= float(input("Entrez note2 de l'etudiant2\n"))

std3_name = input("Entrez nom de l'etudiant3\n")
std3_num = int(input("Entrez numero de l'etudiant3\n"))
std3_grade1= float(input("Entrez note1 de l'etudiant3\n"))
std3_grade2= float(input("Entrez note2 de l'etudiant3\n"))

print("------------------TABLEAU RECAPUTILATIF------------")

name_formater = "{:>10} {:>6} {:>6} {:>6}"
num_formater = "{:10} {:6} {:6} {:6}"
mark_formater = "{:10} {:6.2f} {:6.2f} {:6.2f}"
average_formater = "{:10} {:6.2f} {:^6} {:6.2f}"

print(name_formater.format(" ",std1_name,std2_name,std3_name))
print(num_formater.format("NUM",std1_num,std2_num,std3_num))
print(mark_formater.format("NOTE1",std1_grade1,std2_grade1,std3_grade1))
print(mark_formater.format("NOTE2",std1_grade2,std2_grade2,std3_grade2))
print(average_formater.format("MOY/STD",(std1_grade1+std1_grade2)/2,(std2_grade1+std2_grade2)/2,(std3_grade1+std3_grade2)/2))
print("_______MOYENNE PAR EXAMEN_____")
print(average_formater.format("MOY/EXAM",(std1_grade1+std2_grade1+std3_grade1)/3,"-",(std1_grade2+std2_grade2+std3_grade2)/3))

