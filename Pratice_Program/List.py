lst = [23, 45, 90, 67]
lst.append(100)
lst.append(90)
lst.append(45)

print(lst)

lst.insert(2, 200)  # 2 is index and 200 is value to add in list
print(lst)

lst.remove(100) # remove number from list
print(lst)

lst.pop() # remove last element from list 
lst.pop() # remove last element from list 
print(lst)

del lst[3] # delete element from index 3
print(lst)

lst[3] = 400 # update element at index 3
print(lst)

lst.append(88) # add 88 at the end of list
lst.append(99)
lst.append(39)
print(lst)

print(200 in lst) # check if 200 is in list or not
print(10 in lst) # check if 10 is in list or not

list("abc")# convert string to list
print(list)
list((40,30,90,20)) # convert tuple to list
print(list)

list({30,40,20,40}) # convert set to list
print(list)

print("......................................................................")
print("      ")

# Convert list to Set

my_list = [20,90,45,21,100,101,205]
myset = set(my_list) # convert list to set
print("converted list to set:", myset)

#convert to tuple

mytuple = tuple(my_list) # convert list to tuple
print("converted list to tuple:", mytuple)

#Search element in list


