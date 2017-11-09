class JeuDeCartes():
    "Simulation d'un jeu de carte normal"
    valeur = (0,0,2,3,4,5,6,7,8,9,10,'valet','dame','roi','as')
    nom = ('Coeur','Carreau','Trèfle','Pique')

    def __init__(self):
        self.jeu = []
        for n in range(2,15):
            for m in range(4):
                valeur = n
                type = m
                carte = (valeur,type)
                self.jeu.append(carte)


    def nom_carte(self,carte):
        "Renvois le nom complet de la carte"

        return "{} de {} ".format(self.valeur[carte[0]],self.nom[carte[1]])

    def battre(self):
        from random import shuffle
        shuffle(self.jeu)

    def tirer(self):
        if self.jeu == []:
            return None
        else:
            carte = self.jeu[0]
            del self.jeu[0]
            return carte


if __name__ == "__main__":
    jeu = JeuDeCartes()  # instanciation d'un objet
    jeu.battre()  # mélange des cartes
    for n in range(53):  # tirage des 52 cartes :
        c = jeu.tirer()
        if c == None:  # il ne reste plus aucune carte
            print('Terminé !')  # dans la liste
        else:
            print(c)
            print(jeu.nom_carte(c))  # valeur et couleur de la carte

    A = JeuDeCartes()
    B = JeuDeCartes()
    A.battre()
    B.battre()
    point_A = 0
    point_B = 0
    for n in range(52):
        carte_A = A.tirer()
        print("A:",carte_A)
        carte_B = B.tirer()
        print("B:",carte_B)
        if carte_A[0]> carte_B[0]:
            point_A += 1
        elif carte_B[0]> carte_A[0]:
            point_B += 1
        else:
            point_A = point_A
            point_B = point_B

    print("A: {} and B:{}".format(point_A,point_B))