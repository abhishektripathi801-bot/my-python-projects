class Product:
    def __init__(self):
        self.id = 78
        self.name = "Amul"
        
        def display(self):
            print("ID:", self.id)
        print("Name:", self.name)

class Butter(Product):
    def __init__(self):
        super().__init__()
        self.category = "Butter"
        self.count = 50
    def display(self):
        super().display()
        print("Category:", self.category)
        print("Count:", self.count)

class Milk(Product):
    def __init__(self):
        super().__init__()
        self.category = "Milk"
        self.count = 90
    def display(self):
        super().display()
        print("Category:", self.category)
        print("Count:", self.count)

class Choco(Product):
    def __init__(self):
        super().__init__()
        self.category = "Choco"
        self.count = 56
    def display(self):
        super().display()
        print("Category:", self.category)
        print("Count:", self.count)

class SubA(Butter):
    def __init__(self):
        super().__init__()
        self.price = 30

    def calculate_total(self):
        total = self.count * self.price
        print("Price:", self.price)
        print("Total Price:", total)

class SubB(Milk):
    def __init__(self):
        super().__init__()
        self.price = 10

    def calculate_total(self):
        total = self.count * self.price
        print("Price:", self.price)
        print("Total Price:", total)
        
print("\nButter Product")
obj1 = SubA()
obj1.display()
obj1.calculate_total()

print("\nMilk Product")
obj2 = SubB()
obj2.display()
obj2.calculate_total()

print("\nChoco Product")
obj3 = Choco()
obj3.display()