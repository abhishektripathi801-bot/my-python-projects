class byke:
    name = ""
    gear = 0
    
# create object of class

byke1 = byke()

byke1.name = "Hero Honda"
byke1.gear = 4

print(f"Name: {byke1.name} has gear {byke1.gear}")


#2nd example

class Room:
    length = 0.0    # class attribute
    breadth = 0.0  # class attribute
    
    # area calculation method
    def calculate_area(self): # self is a reference variable which refers to the current object of the class
        c = self.length*self.breadth   # self is used to access the class attributes
        print(" Area of the room is" , c)
        
# 1st object of the claas
study_room = Room() 
study_room.length =  42.0 
study_room.breadth = 10.0

study_room.calculate_area()

# 2nd object of the class
bed_room = Room()
bed_room.length = 30.0
bed_room.breadth = 20.0
bed_room.calculate_area()   

# 3rd object of the class
dineing_room = Room()
dineing_room.length = 45.00
dineing_room.breadth = 30.00
dineing_room.calculate_area()

# 4th object of the class
kitchen = Room()
kitchen.lenghth = 20.00


