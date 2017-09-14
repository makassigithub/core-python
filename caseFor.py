#The range func generates list from 0 to the indicated border
# range(stop) or range([start], stop[, step])
#       start: Starting number of the sequence.
#       stop: Generate numbers up to, but not including this number.
#       step: Difference between each number in the sequence.
#       All parameters must be integers, and All parameters can be positive or negative.


# range with only a stop value
my_list1 = range(5)
print(list(my_list1)) #use list to convert the variable to a list

# range with a start value
my_list2 = range(1,5)
print(list(my_list2))
print()

#range start, stop and step value
my_list3 = range(2,10,3)
print(list(my_list3))
print()

# using a for loop on a iterable
for i in [9,1,4,0,4,5]:
    print(i, end='@')
print()

# the for loop takes advantage of the range() function

# start only
for i in range(10):
    print(i, end= ' ')
print()

# with start and stop
for i in range(3,10):
    print(i, end= '-')
print()
# with start stop and step

for i in range(0,10,2):
    print(i, end='*')
print()

# looping  back
for i in range(0,-10,-2):
    print(i, end='- -')
print()

#looping using the index
my_list0 = ['Brahima', 'is', 'my', 'real', 'name']
for i in list(range(len(my_list0))):
    print(my_list0[i], end=' ')