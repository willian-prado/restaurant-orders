class TrackOrders:
    def __init__(self):
        self.orders = 0
        self.registry = {}

    def __len__(self):
        return self.orders

    def add_new_order(self, customer, order, day):
        self.orders += 1
        if customer not in self.registry:
            self.registry[customer] = {"meals": [order], "days": [day]}
        else:
            self.registry[customer]["meals"].append(order)
            self.registry[customer]["days"].append(day)

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
