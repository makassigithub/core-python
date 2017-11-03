
import math


class Cercle(object):
    """
    La class de base servant à contruire ls figure circulaires.
    """
    def __init__(self,rayon):
        self.rayon = rayon    # Une instance de cette class aura un attr rayon

    def surface(self):
        "Retourne la surface de l'instance sous la formule PiR**2"
        return math.pi*(self.rayon)**2   # surface() var recuperer la valeur de rayon de cette instance
                                         # pour calculer la surface


class Cylindre(Cercle):                  # Cylindre herite de cercle
    "Le cylindre ayant un volume calculable sur la base et la hauteur de la fig"
    def __init__(self,rayon,hauteur):
        Cercle.__init__(self,rayon)      # Appel du constructeur du superclass qui va creer notre attribut rayon dans
        self.hauteur = hauteur           #dans le name space de l,instance qui sera creer.

    def volume(self):
        "le volume est le produit de la surface par la hauteur"
        surface = Cercle.surface(self)   # Appel de la methode du superclass pour creer la surface
        volume = surface*self.hauteur    # la hauteur sera preleve dans le name space de cette instance.
        return volume

class Cone(Cylindre):
    def __init__(self,rayon,hauteur):
        Cylindre.__init__(self,rayon,hauteur) # Cone appel Cylindre qui appel Cercle, ensemble, rayon et hauteur
                                              # seront creer dans mon namespace

    def volume(self):
        "Le volume du cone est le 1/3 de celui du Cylindre"
        return Cylindre.volume(self)/3


if __name__ == "__main__":
    cyl = Cylindre(5, 7)
    print("Le surface du cylindre est: {}".format(cyl.surface()))
    print("Le volume du cylindre est : {}".format(cyl.volume()))

    co = Cone(5, 7)
    print("Le volume du cone est : {}".format(co.volume()))