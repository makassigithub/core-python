# working with Counter form  collections
from collections import Counter

data = [1,2,3,2,3,4,4,5,]
print("data: {}".format(data)) # print data

counter = Counter(data) # returns a dictionnary
print("data_counter: {}".format(counter)) #

print("counter_keys: {} and the type is: {}".format(counter.keys(), type(counter.keys()))) # returns an oject of type dic_keys
print("counter_values: {} and the type is: {}".format(counter.values(),type(counter.values())))# returns an oject of type dic_keys

# unique values of the initial list are received by converting dis_keys to list

unik_list = list(Counter(data).keys())
print("unique values of data are {} ".format(unik_list))


