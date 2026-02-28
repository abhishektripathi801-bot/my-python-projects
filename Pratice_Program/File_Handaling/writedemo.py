def add_product(product_id, name, price):
    file = open("products_new.txt", "a")   # Open file in append mode
    
    record = f"{product_id},{name},{price}\n"
    file.write(record)
    
    file.close()   # Manually closing file


add_product(101, "Laptop", 45000)
add_product(102, "Watch", 3000)
add_product(103, "Headphones", 1000)


print("============= Reading all data from the file =============")


def read_products():
    file = open("products_new.txt", "r")   # Open file in read mode
    
    data = file.read()
    print(data)
    
    file.close()   # Manually closing file


read_products()
