class Espace(object):
    aa = 22
    def affiche(self):
        print(aa,Espace.aa,self.aa)

aa = 33
mon_espace = Espace()
mon_espace.aa = 33
mon_espace.affiche()

print(aa,Espace.aa,mon_espace.aa)
print(__doc__)
