class Flight:
    def __init__(self, flight_no, source, destination, base_fare):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.base_fare = base_fare
        
    def get_flight_info(self):
        return "Flight:", self.flight_no, "From:", self.source, "To:", self.destination
    
    def calculate_fare(self, passenger_count, discount_percent=0):
        total_fare = self.base_fare * passenger_count
        
        if discount_percent >0:
            discount_amount=total_fare - (total_fare * discount_percent / 100)
            return discount_amount
        
    def update_route(self, source=None, destination=None):
        if source and destination:
            self.source = source
            self.destination = destination
        elif destination:
            self.destination = destination
    
f1 = Flight("AI101", "Delhi", "Mumbai", 5000)

print(f1.get_flight_info())

print("Total Fare (3 passengers):", f1.calculate_fare(3))

print("Total Fare (3 passengers, 10% discount):", f1.calculate_fare(3, 10))

f1.update_route(destination="Bangalore")
print("Updated Info:", f1.get_flight_info())

f1.update_route("Chennai", "Hyderabad")
print("Updated Info:", f1.get_flight_info())
            
        
    
            
    
        
    
        
        