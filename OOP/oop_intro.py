class Point():
    "Le pint est definie par 2 coordonnes spaciales"


def calculer_distance(A,B):
    " etant donné point A et B, cette function calcul la distance qui les separe et la retourne "
    return ((B.x - A.x)**2 + (B.y - A.y)**2)**1/2

p1 = Point()
p1.x , p1.y = 2.0, 3.0

p2 = Point()
p2.x , p2.y = 4.0, 2.0

print(" distance entre p1 et p2 est: {}".format(calculer_distance(p1,p2)))


