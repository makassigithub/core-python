class Domino:
    def __init__(self,a=0,b=0):
        self.face_A = a
        self.face_B = b

    def affiche_points(self):
        print("face A: {}, face B: {}".format(self.face_A,self.face_B))

    def valeur(self):
        return self.face_A + self.face_B


if __name__ == "__main__":
    d1 = Domino(2, 6)
    d2 = Domino(4, 3)
    d1.affiche_points()
    d2.affiche_points()
    print("total des points :", d1.valeur() + d2.valeur())
    liste_dominos = []
    for i in range(7):
        liste_dominos.append(Domino(6, i))
    print(liste_dominos[3])
