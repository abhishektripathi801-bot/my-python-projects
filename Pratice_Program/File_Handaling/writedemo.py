def add_product(product_id, name, price):
    file = open("product.txt", "a") #open file and update data
    
    record = f"{product_id},{name},{price}\n"
    file.write(record)
    
    file.close()


# Function calls (OUTSIDE the function)
add_product(101, "Laptop", 45000)
add_product(102, "Mobile", 85000)
add_product(103, "Watch", 5000)
add_product(104, "Earbud", 3000)
add_product(105, "Adapter", 1000)


print("========================reading all the data from file===============")

def read_prodct():
   file = open("product.txt", "r") #open file in read moe
   data = file.read()
   print(data)
   
   file.close()
   
   read_prodct()
