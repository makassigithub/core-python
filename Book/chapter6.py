#6.1 Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie
#par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)
#mp = float(input("enter speed :\n"))
#print("the equivalent in km/h is: ", (mp*1609)/1000)
#print("the equivalent in m/ is: ", ((mp*1609)/1000)*1000/3600)

def isPremier(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
        else:
            return True

def isPremier2(n):
    position = 2
    while position <= n-1:
        if(n % position == 0):
            return False
        else:
            return True
    ++position

print(isPremier(5))
print(isPremier(4))

print(isPremier2(5))
print(isPremier2(4))


