class Flight:
    def __init__(self, flight_no, base_price, total_seats):
        self.flight_no = flight_no
        self.base_price = base_price
        self.total_seats = total_seats

    def display_flight_info(self):
        print("Flight Number:", self.flight_no)
        print("Base Price:", self.base_price)
        print("Total Seats:", self.total_seats)


class DomesticFlight(Flight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent):
        super().__init__(flight_no, base_price, total_seats)
        self.tax_percent = tax_percent

    def calculate_price(self):
        tax_amount = (self.base_price * self.tax_percent) / 100
        self.total_price = self.base_price + tax_amount
        print("Price after tax:", self.total_price)
        return self.total_price


class BookingFlight(DomesticFlight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent):
        super().__init__(flight_no, base_price, total_seats, tax_percent)
        self.booked_seats = 0

    def check_seat_availability(self, requested_seats):
        available = self.total_seats - self.booked_seats

        if requested_seats <= available:
            print("Seats available:", available)
            return True
        else:
            print("Only", available, "seats available")
            return False

    def book_seats(self, requested_seats):
        if self.check_seat_availability(requested_seats):
            self.booked_seats += requested_seats
            print(requested_seats, "seats booked successfully")
        else:
            print("Seats not available")

    def get_final_price(self, no_of_tickets):
        price_per_ticket = self.calculate_price()
        final_amount = price_per_ticket * no_of_tickets
        print("Final price for", no_of_tickets, "tickets:", final_amount)
        return final_amount

f1 = BookingFlight("90BZ", 5000, 100, 10)

f1.display_flight_info()
f1.book_seats(90)
f1.get_final_price(90)
                