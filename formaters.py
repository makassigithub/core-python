#Python’s str.format() method of the string class allows you to do variable substitutions and value formatting.
# This lets you concatenate elements together within a string through positional formatting.

#1. the formater contains placeholder "{}"that is resolve during python runtime.
print("Makassi is {} years old.".format(32))

#2. formater can also be assiged to strings.
fmt = "Makassi {} happy"
print(fmt.format("is"))

#3. we can use multiple placeholers at the same time. order of values are resolved
# in the order of curly braces appearance. that behavior can be overriden specifying indexes
# the format() takes tuples a argunemt, with a zero based index. if index is out of bound an exception is thrown
fmt = "Makassi {} {} happy"
print(fmt.format("is","not"))
fmt2 = "Makassi {1} {0} happy"
print(fmt2.format("is","not"))

#4. A placeholder {} can also be named. When mixed,
# positional argument must be specified before keyword args inside forma()
print("my {} is {bh} and I was {} in {year}".format("name","born", bh="Brahima", year="1983"))

#5. we can use types formater like {field_index:convertion} to format our variables, where
#conversion can take 3 values (d for Integer, f for floats, and s for strings) and may contain
# num of caracteres specs.

#a. specifying format types: if indexes are to be specified, they must be for all placeholders
# but placeholder are refers to as they are in the format(), index can be ommited
print("{0:d} over {1:d} can be represented as {2:f} {3}".format(1,4,0.25,"percent"))
print("{:d} over {:d} can be represented as {:f} {}".format(1,4,0.25,"percent"))


#bcontrolling number of decimal e.g. 2 places for the float, number of digit can be specified
# for before decimal places for pagination purpose e.g {2:3.2f}
print("{0:d} over {1:d} can be represented as {2:.2f} {3}".format(1,4,0.25,"percent"))

#c Inetegrs can be formated to be display as float but not the opposit
print("I have {:.2f} candy".format(5))
#print("I have {:d} candy".format(5.00)) // ValueError: Unknown format code 'd' for object of type 'float'
# this can be achieved by truncation the value
print("I have {:.0f} candy".format(5.00))

#6 Padding when printing using charactere control numbers after as conversion
print("I have {:5} pen".format(2))
print("I had {:6} pen before ".format(2))

# By default Strings are left-justified, numbers are right-justified, but these
# behavior can be overriden using >,<,^( display right, left, center)
print("-----------------------------------------")
print("I had {:6} pen {} ".format(2,"before"))
print("I had {:<6} pen {:<8} ".format(2,"before"))
print("I had {:>6} pen {:>8} ".format(2,"before"))
print("I had {:>6} pen {:^8} ".format(2,"before"))
print("I had {:^6} pen {:>8} ".format(2,"before"))

#using field-filler instead of python default white space
print("I had {:*^6} pen {:>8} ".format(2,"before"))

# formatting using variables:
# Aside form formaters that can be stored in variables, variable can also be used
# inside str.format()
print("-------------------------------------------")
name = "Komolo"
formater = "My friend {} is the best"
print(formater.format(name))

print("-------------------------------------------")
# formaters are eally handy in formating data output for end users
for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
