def modify_int (a):
    b = a+1
    print(a,b)

a = 4
modify_int(a)

def modify_list(list):
    list2 = list
    list.append('x')
    print('list: ',list)
    print('list2:',list2)

myl = [1,2,3]

modify_list(myl)
