#Assignment:
#Create a function to display the product details like- Id, prodName, price inside the function
#(a) calculate the total price of the product by passing the discount variable as 'global variable'
#And also you need  create another function that takes the quantity of the product as an argument and calculate the total price after applying the discount  and return the total price from the function
#(Note**: quantity * price = price  and then apply the discount over the price)

discount = 15

def display_product(Id,prodName,price):
    global discount
    print("Product Details")
    print("Product id is:", Id)
    print("Product Name is:",prodName)
    print("Product Price is:", price)
    
    discount_price = price*discount/100
    print("Discounted price is:", discount_price)
    Total_price = price - discount_price
    print("Price after discount", Total_price)
    
def quantity_product(price, quantity):
    global  discount
    
    total = price * quantity
    
    discount_product_quantity = total*discount/100
    final_price = total - discount_product_quantity
    
    return final_price

display_product(102, "Apple", 250)

Final_Price = quantity_product(250, 5)

print("Total price after discount as per quantity is:", Final_Price)