flight_no = "AI203"
base_fare = "4500.75"
tax_percent = "5"
seat_number = "12,12B,14C,15D"
is_international = "True"

base_fare = float(base_fare)
tax_percent = float(tax_percent)

final_fare=base_fare+(base_fare*tax_percent/100)
print("final fare for one passenger is:", final_fare)

#B

seat_list = seat_number.split(",")
print("list of seat", seat_list)

#C

seat_set = set(seat_list)
print("Seat Set:", seat_set)

#D

if is_international == "True":
    is_international = True 
else:
    Falseis_international = False
print(" Is International:", is_international)

#E

flight_summary = {
    "flight_no": str(flight_no),
    "flight_fare": int(final_fare),
    "seat_number": tuple(seat_list)
}
print("Flight Summary:", flight_summary)

