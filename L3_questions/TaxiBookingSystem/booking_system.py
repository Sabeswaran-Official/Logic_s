#  Taxi's -details as no.of taxis ,taxis id/name ,...
from taxi import Taxi
from booking import Booking
from customer import *

class BookingSystem:
    def __init__(self, taxi_count):
        self.taxis = [Taxi(i) for i in range(1, taxi_count + 1)]
        self.booking_id = 1

    def calculate_charges(self, pickup, drop):
        distance = abs(ord(pickup) - ord(drop)) * 15
        charges = 100
        distance -= 5
        if distance > 0:
            charges += distance * 10
        return charges

    def find_taxi(self, pickup, pickup_time):
        free_taxis = [t for t in self.taxis if t.is_free(pickup, pickup_time)]

        if not free_taxis:
            return None

        # Find the minimum distance from pickup point
        min_distance = min(abs(ord(pickup) - ord(t.get_current_spot())) for t in free_taxis)

        # Get all taxis that are at the minimum distance
        closest = [t for t in free_taxis if abs(ord(pickup) - ord(t.get_current_spot())) == min_distance]

        # Among closest taxis, pick the one with minimum earnings
        selected = min(closest, key=lambda t: t.get_earnings())
        return selected

    def book_taxi(self, customer):
        selected = self.find_taxi(customer.get_pickup(), customer.get_pick_time())

        if selected is None:
            print("No Taxi is Available")
            return

        travel_time = abs(ord(customer.get_pickup()) - ord(customer.get_drop()))
        drop_time = customer.get_pick_time() + travel_time
        charges = self.calculate_charges(customer.get_pickup(), customer.get_drop())

        booking = Booking(self.booking_id, drop_time, charges, customer)
        self.booking_id += 1

        selected.assign_booking(booking)
        selected.set_free_time(drop_time)
        selected.set_earnings(selected.get_earnings() + charges)
        selected.set_current_spot(customer.get_drop())

        print()
        print(f"Taxi-{selected.get_taxi_id()} is allocated")
        print()

    def display_taxi(self):
        print()
        for t in self.taxis:
            print(f"Taxi-{t.get_taxi_id()} Earnings: {t.get_earnings()}")
            print("Booking Id\tCustomer Id\tFrom\tTo\tPickup Time\tDrop Time\tCharges")
            for b in t.get_bookings():
                print(f"{b.get_booking_id()}\t\t{b.get_customer_id()}\t\t{b.get_pickup_point()}\t{b.get_drop_point()}\t"
                      f"{b.get_pickup_time()}\t\t{b.get_drop_time()}\t\t{b.get_amount()}")
            print()


