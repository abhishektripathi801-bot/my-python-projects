# program for single inheritance to display 10 electronic products with their details and calculate the total price after for given quantity.

class product:
    naame = "Apple iPhone 17 pro max"
    price = 120000
    brand = "Apple"
    warranty = "1 year"
    
    def product_detials(self):
        print("Product Name:", self.naame)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
    
    def cal_price(self, count):
        self.total_price = self.price * count
          
class electronics(product):
    type = "electronics"
    
    def displayAlldetails(self):
        print(f"Name is: {self.naame}, Price is {self.price}, Brand is {self.brand}, Warranty is {self.warranty}, Total price is of 10 device: {self.total_price}")
      
e = electronics()
e.product_detials()
e.cal_price(10)
e.displayAlldetails()