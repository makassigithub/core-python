list1 = (10,2,4,2,1,6,8,9)
list2 = (-10,-2,-4,-2,-1,-17,6,-8,-9)

print("getting the maximun of a list")
def calculate_max(param):
    index = 0
    maxi=param[index]
    while index < len(param):
        if param[index] > maxi:
            maxi = param[index]
        index = index+1
    return maxi

print("maximum:",calculate_max(list2))


print("getting both the maximun and the minimum of a list")
def calculate_max_min(param):
    index = 0
    maxi=mini=param[index]
    while index < len(param):
        if param[index] > maxi:
            maxi = param[index]
        if param[index] < mini:
            mini = param[index]
        index = index+1
    return maxi,mini
mx,mn = calculate_max_min(list2)
print("maxi:", mx,"/", "mini:",mn)

def frog_combine(dist):
    combinaision = 0
    if dist == 0:
        return combinaision

    step3 = dist // 3
    step3_rem = dist % 3

    if   step3_rem == 0:
        combinaision = step3*3
    elif step3_rem == 1:
        combinaision = step3*3 + 2
    elif step3_rem == 2:
        combinaision = step3*3 + 4
    return combinaision

if __name__ == "__main__":
    print("{} contient {} possibilté(s)".format("0", frog_combine(0)))
    print("{} contient {} possibilté(s)".format("1", frog_combine(1)))
    print("{} contient {} possibilté(s)".format("2", frog_combine(2)))
    print("{} contient {} possibilté(s)".format("3", frog_combine(3)))
    print("{} contient {} possibilté(s)".format("4", frog_combine(4)))
    print("{} contient {} possibilté(s)".format("5", frog_combine(5)))
    print("{} contient {} possibilté(s)".format("6", frog_combine(6)))




