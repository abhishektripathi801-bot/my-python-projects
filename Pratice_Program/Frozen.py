f = {23,43,21,54,76,67}
print(f)
f.add(100)
f.add(200)
f.add(300)
print(f)

fs = frozenset(f)     # create frozenset from set f
print(fs)

list1 = list(fs)      # convert frozenset to list
print("converted fronzenset to list is:", list1)

list1.append(28)
list1.append(45)

print("adding elements to list1 is:", list1)

fs2 = frozenset(list1)     # create frozenset from list1
print("converted list1 to frozenset is:", fs2)

tuple1 = tuple(fs2)     # convert frozenset to tuple
print("converted frozenset to tuple is:", tuple1)


