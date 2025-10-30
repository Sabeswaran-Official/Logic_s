#  custmer_id ,pickup_time ,pickup_place ,drop_place

class Customer:
    def __init__(self, customer_id, pickup, drop, pick_time):
        self.customer_id = customer_id
        self.pickup = pickup
        self.drop = drop
        self.pick_time = pick_time

    def get_customer_id(self):
        
        return self.customer_id

    def get_pickup(self):
        return self.pickup

    def get_drop(self):
        return self.drop

    def get_pick_time(self):
        return self.pick_time
