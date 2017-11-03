# 5.6 Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».
myWord = "enumerating"
print("e" in myWord)

# 5.7 Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne.
print(myWord.count("n"))

# 5.8 Écrivez un script qui recopie une chaîne (dans une nouvelle variable),
#  en insérant des astérisques entre les caractères.
#  Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »

# myword2 = "temoin"
# initialLentgh = 0
# while initialLentgh < len(myword2):
#     print(myword2[initialLentgh], end='*')
#     initialLentgh = initialLentgh + 1

myword3 = "temoin"
iLentgh = 0
modified = ""
while iLentgh < len(myword3):
    if iLentgh == len(myword3)-1:
        modified = modified + myword3[iLentgh]
    else:
        modified = modified + myword3[iLentgh] + '*'
    iLentgh = iLentgh + 1

print(modified)


# 5.9 Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant.
#  Ainsi par exemple, « zorglub » deviendra « bulgroz ».

myWord4 = "banal"
reverse = ""
counter = len(myWord4)-1
while counter >=0 :
    reverse = reverse + myWord4[counter]
    counter = counter - 1
print(reverse)

#5.10 En partant de l’exercice précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome
#  (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s ».

myWord5 = "radar"
reverse = ""
counter = len(myWord5)-1
while counter >=0 :
    reverse = reverse + myWord5[counter]
    counter = counter - 1
if myWord5 == reverse:
    print(myWord5, "is a palindrome")
else:
    print(myWord5, "is not a palindome")
