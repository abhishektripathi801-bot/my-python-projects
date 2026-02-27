class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("we are in product constructor")
        
    def get_price(self):
        return self.price

class DiscountProduct(Product):
    def __init__(self, name, price,discount):
        super().__init__(name, price)
        self.discount = discount
        print("We are in the discountProduct constractor")
        
    def get_price(self):
        base_price = super().get_price()    #calling the parent class method with same nane
        return base_price - self.discount
    
class SeasonProduct(DiscountProduct):
    def __init__(self, name, price, discount,offer):
        super().__init__(name, price, discount)
        self.offer = offer
        print("we are in seasonProduct constrator")
        
    def get_price(self):
        price_after_discount = super().get_price()
        return price_after_discount - self.offer
    
p1 = SeasonProduct("laptop", 65000, 3000, 1000)
print(" Final price after discount and offer is:", p1.get_price())


        