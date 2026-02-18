class Product:
    name = "iPhone"
    price = 150000
    brand = "Apple"
    warranty = 1

    def display(self):
        print(f"Product Name is: {self.name}, Price: {self.price}, Brand is: {self.brand}, Warranty of Product is: {self.warranty}")

    def cal_price(self, count):
        self.total_price = self.price * count
       
class Electrics(Product):
    type = "Electronics"
  

    def displayAlldetails(self):
        print(f"Name is {self.name}, Type is {self.type}, Price is {self.price}, Brand is {self.brand}, Warranty is {self.warranty}, Total price is of 10 device: {self.total_price}")


e = Electrics()
e.display()
e.cal_price(10)
e.displayAlldetails()
