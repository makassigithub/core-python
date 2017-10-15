#Exercice 10.1
# slice: iterable[start_index:end_index]  with start_index included and end_index excluded.
data = "abcdefghi"
data_5 = data[:5]
print('data[:5] =',data_5)
print("data[2:2] = ",data[2:2]) # rien ne se passe si end_index = start_index, mais pas d'exception non plus.
print("data[2:1] = ",data[2:1]) # rien n'est retourné si end_index < start_index, mais pas d'exception non plus.
print("data[2:20] = ",data[2:20]) # l'iterable est copié jusqu'à la fin si end_index > iterable[len(iterable-1)]

#Exercice 10.2
def slice_n(chaine,n):
    slices = []             # list à construire
    start,end = 0,n         # debut et fin de sequences
    while start < len(chaine):
        if end > len(chaine):
            end = len(chaine)
        slice = chaine[start:end]
        slices.append(slice)
        start,end  = end, end+n
    return slices

#Exercice 10.3
def trouve_index(chaine,char,i = 0):
    while i < len(chaine):
        if chaine[i]== char:
            return i
        i += 1
    return -1

#Exercice 10.4
def trouve_index2(chaine,char,start_index):
    i = start_index
    while i < len(chaine):
        if chaine[i]== char:
            return i
        i += 1
    return -1

#Exercice 10.5
def compte_car(chaine,char,compteur = 0):
    for ch in chaine:
        if ch == char:
            compteur += 1
    return compteur

if __name__ == "__main__":

    #1 0.2
    chaine1 = "emdnéèehàhsagdmbéwèdjheqwl"
    assert len(slice_n(chaine1,3)) == 9
    print(slice_n(chaine1,3))

    # 10.3
    print("index du premier {} dans {} est: {} ".format("a","Brahima",trouve_index("Brahima","a")))
    print("index du premier {} dans {} est: {} ".format("e", "Brahima",trouve_index("Brahima", "e")))

    # 10.4
    print("index du premier {} dans {} est: {} ".format("a", "Brahima", trouve_index2("Brahima", "a",3)))
    print("index du premier {} dans {} est: {} ".format("e", "Brahima", trouve_index2("Brahima", "e",3)))

    # 10.5
    print("Il y a {} fois '{}' dans {} ".format(compte_car("BrahimaMakassi","a"),"a","BrahimaMakassi" ))
    print("Il y a {} fois '{}' dans {} ".format(compte_car("BrahimaMakassi", "e"), "e", "BrahimaMakassi"))






