from ex_12_2 import CompteBancaire

class CompteEpargne(CompteBancaire):
    " Une variance de compte"
    def __init__(self,nom,solde,taux=0.3):
        CompteBancaire.__init__(self,nom,solde)  # self: tjrs passer la reference du sub au constructeur du super
        self.taux = taux                         # Ainsi il aura acces au namespace de sub pour ecriture

    def changeTaux(self,valeur):
        self.taux = valeur

    def capitalisation(self,nombreMois):
        print("Capitalisation sur {} mois au taux mensuel de {} %.".format(nombreMois,self.taux))
        mensuel_incrementation = self.solde*(self.taux)/100
        incrementation_12_mois = mensuel_incrementation*12
        self.solde += incrementation_12_mois

        #self.solde += (self.taux)*(self.solde)*nombreMois


if __name__ =="__main__":
    c1 = CompteEpargne('Duvivier', 600)
    c1.depot(350)
    c1.affiche()
    c1.capitalisation(12)
    c1.affiche()
    c1.changeTaux(.5)
    c1.capitalisation(12)
    c1.affiche()
