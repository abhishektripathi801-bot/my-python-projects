my_set = {20,23,20,13,95}
print(my_set) # print the set

my_set.add(100)         # add element to set
my_set.add(90)
my_set.add(200)
print(my_set)           # print the set after adding elements

y = my_set.pop()         # The removed element is arbitrary, not random can’t predict which one it will be.
print(y)                 # print the removed element

my_set.remove(23)
print(my_set)

#my_set.remove(300)       # remove element that is not present in set will raise error
#print(my_set)

my_set.discard(300)      # discard element that is not present in set will not raise error
print(my_set)


#Search element in set

print(90 in my_set)        # check if 90 is in set or not
print(20 in my_set)
print(19 in my_set)
print("Above are Serch elements are in set or not")
print("                           ")

a = {1,4,9,6,5}
b = {3,1,4,7,5}

print("Union of sets a and b:", a|b)               # union of set a and b

print("Intersection of set a and set b:", a&b)        # intersection of set a and b

print("Diffrence of set a and set b:", a-b)              # difference of set a and b

print("Symmetric difference of set a and set b:", a^b)     # symmetric difference of set a and b

#a.pop()         # The removed element is arbitrary, not random can’t predict which one it will be.

