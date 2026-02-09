my_tuple = (20,45,200,45,200,32,34,101,202,301,90)
print(my_tuple)
print(my_tuple[4]) # access element at index 4

#Search element in tuple

print(202 in my_tuple) # check if 202 is in tuple or not
print(10 in my_tuple) # check if 10 is in tuple or not

print("-----------------------------------------------------------------")

print(my_tuple.count(200)) # count the number of times 200 appears in tuple
print(my_tuple.count(45)) # find the index of first occurrence of 45 in tuple
print(my_tuple.count(20)) # count the number of times 20 appears in tuple
print("--------------------------------------")
print(my_tuple.index(34)) # find the index of first occurrence of 34 in tuple
print(my_tuple.index(45)) # find the index of first occurrence of 45 in tuple

#list to tuple
tuple([3,4,5,8,9,21,]) # convert list to tuple
print(tuple([3,4,5,8,9,21,])) # print the tuple created from list

#String to tuple

tuple("Abhishek") # convert string to tuple

print(tuple("Abhishek")) # print the tuple created from string

# POP

# my_tuple.pop() # in tuple pop object does not support item deletion or assignment

list(my_tuple) # convert tuple to list
print(list(my_tuple)) # print the list created from tuple



