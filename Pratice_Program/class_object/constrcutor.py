
class Room:
    
    def calculate_area(self,length,breadth): # self is a reference variable which refers to the current object of the class
        self.length = length
        self.breadth = breadth
        c = self.length*self.breadth   # self is used to access the class attributes
        print(f" Area of the room is:", c) # self is used to access the class attributes
        
# 1st object of the claas
study_room.calculate_area(42.0,10.0)
study_room.calculate_area()

# 2nd object of the class
bed_room = Room(30.0,20.0)
bed_room.calculate_area("Bed Room")
    
# 3rd object of the class
dineing_room = Room(45.00,34.00)
dineing_room.calculate_area("Dining Room")

# 4th object of the class
kitchen = Room(20.00,15.00)
kitchen.calculate_area("Kitchen")