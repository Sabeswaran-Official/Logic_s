# Booking_id ,customerDetail ,trip_earning ,droptime
from customer import *  # Importing Customer class (aggregation relationship)

class Booking:
    def __init__(self, booking_id, drop_time, amount, customer):
        self.booking_id = booking_id
        self.drop_time = drop_time
        self.amount = amount
        self.customer = customer  # Aggregation: Booking "has a" Customer

    def get_booking_id(self):
        return self.booking_id

    def get_drop_time(self):
        return self.drop_time

    def get_amount(self):
        return self.amount

    def get_customer(self):
        return self.customer

    def get_customer_id(self):
        return self.customer.get_customer_id()

    def get_pickup_point(self):
        return self.customer.get_pickup()

    def get_drop_point(self):
        return self.customer.get_drop()

    def get_pickup_time(self):
        return self.customer.get_pick_time()

    