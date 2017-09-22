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
