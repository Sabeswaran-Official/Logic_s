# taxi_id ,cur_loc ,free_time ,earnings ,booking_list, isFree() ,assignBooking()
from booking import *  # Assuming Booking is defined in another file (booking.py)


class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.current_spot = 'A'
        self.free_time = 0
        self.earnings = 0
        self.bookings = []  # list of Booking objects

    def is_free(self, pickup, pickup_time):
        travel_time = abs(ord(pickup) - ord(self.current_spot))
        return self.free_time + travel_time <= pickup_time

    def assign_booking(self, booking):
        self.bookings.append(booking)

    def get_taxi_id(self):
        return self.taxi_id

    def get_current_spot(self):
        return self.current_spot

    def get_free_time(self):
        return self.free_time

    def get_earnings(self):
        return self.earnings

    def get_bookings(self):
        return self.bookings

    def set_free_time(self, free_time):
        self.free_time = free_time

    def set_earnings(self, earnings):
        self.earnings = earnings

    def set_current_spot(self, spot):
        self.current_spot = spot

    