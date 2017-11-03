# Booleans can take only two values: True, False
# zero is False, empty string is False
#  any other value is True
a,b = 4,5
c = a>b
d = a<b
print(c,d)

#Booleans are converted into binaries 0 and 1 for respec. False and True
# before being passed to the OS
cases = ['vrai', 'faux']
print(cases[c],cases[d]) 