class Product():
    def __init__(self, name, price, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.price = price
        print("We are into the product constractor")
        
    def display_basic(self):
        print(f"Product :{self.name} has the price as INR.{self.price}")
        
        
class Electronic(Product):
    def __init__(self, category, **kwargs):
        super().__init__(**kwargs)
        self.category = category
        print("we are into the clectronic constractor")
        
    def display_category(self):
         print(f"Product :{self.name} has the price as INR.{self.price} with cateogry as {self.category}")
        
        
class Brand(Product):
    def __init__(self, brand, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        print("we are in brand constractor")
        
    def display_brand(self):
      print(f"Product :{self.name} has the price as INR.{self.price} with brand as {self.brand}")
        
        
class MyProduct(Electronic, Brand):
    def __init__(self, name, price, category, brand, discount):
        super().__init__(name=name, price=price, category=category, brand=brand)
        self.discount = discount
        
    def all_details(self):
        self.display_category()
        self.display_brand()
        self.display_basic()
        
mypro = MyProduct("Laptop", 60000, "Electronic", "Dell", 500)
mypro.all_details()
        