d1 = [{"id":101, "name":"abhishek","age": 32, "city":"Bangalore" }, {"id":102, "name":"sonam","age": 28, "city": "Varanasi"}]

print(d1)

d1[0]["state"] = "Karnataka"     # add new key-value pair to first dictionary in list
print(d1)

d1[1]["state"] = "Uttar Pradesh"     # add new key-value pair to second dictionary in list
print(d1)

d1[0].pop("age")        # remove key-value pair with key "age" from first dictionary in list
print(d1)
d1[0]["age"] = 33
print(d1)

d1[0][1].pop("age")        # remove key-value pair with key "age" from first dictionary in list
print(d1)
