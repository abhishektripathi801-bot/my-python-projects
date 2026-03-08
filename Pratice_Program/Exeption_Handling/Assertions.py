class FlightNotFoundError(Exception):
    pass

class Flight:
    def __init__(self, flight_no, source, destination, seats):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.seats = seats
        
    def add_flight(self, flight_no, source, destination, tota_seats):
        try:
            total_seats = int(total_seats)
            
            assert total_seats >0, "Seat need to be grater than 0"
            
            self.flight_no = flight_no
            self.source = source
            self.destination = destination
            self.seats = total_seats
            
            print("Flight Added")
            
        except AssertionError as e:
            print("AssertionError:", e)
            
        except ValueError:
            print("ValueError: Seat must be a number")
            
        except Exception as e:
            print("Exception:, e")
            
    