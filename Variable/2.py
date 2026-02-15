discount = 10
def dispaly_product_details(prod_id, prodName, price):
    global discount
    
    print("Product ID:", prod_id)
    print("Product Name:", prodName)
    print("product price:", price)
    
    total_price = price - (price*discount /100)
    print("Total Price after discount:", total_price)
    
    
    def calculate_total_price(price,quantity):
        global discount
        
        total = quantity*price
        
        final_price = total - (total*discount / 100)
        
        return final_price
    
    dispaly_product_details(101, "Laptop", 50000)
    
    total_amount = calculate_total_price(50000, 2)
    print("Total price after discount for given quantity:", total_amount)
    