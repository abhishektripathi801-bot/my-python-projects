# program for single inheritance to display 10 electronic products with their details and calculate the total price after for given quantity.

class product:
   naame = "Apple iPhone 17 pro max"
   price = 120000
   brand = "Apple"
   warranty = "1 year"
   def display_product_detials(self):
         print("Product Name:", self.naame)
         print("Price:", self.price)
         print("Brand:", self.brand)
         print("Warranty:", self.warranty)
    def calculate_total_price(self, quantity):