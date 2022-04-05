from src.analyze_log import (
    most_frequent,
    meals_never_ordered,
    days_never_visited
)


class TrackOrders:
    def __init__(self):
        self.orders = 0
        self.registry = {}
        self.open_days = {}

    def __len__(self):
        return self.orders

    def add_new_order(self, customer, order, day):
        self.orders += 1
        if customer not in self.registry:
            self.registry[customer] = {"meals": [order], "days": [day]}
            self.add_visitor(day)
        else:
            self.registry[customer]["meals"].append(order)
            self.registry[customer]["days"].append(day)
            self.add_visitor(day)

    def add_visitor(self, day):
        if day not in self.open_days:
            self.open_days[day] = 1
        else:
            self.open_days[day] += 1

    def get_most_ordered_dish_per_customer(self, customer):
        return most_frequent(self.registry[customer]["meals"])

    def get_never_ordered_per_customer(self, customer):
        return meals_never_ordered(
            self.registry[customer]["meals"])

    def get_days_never_visited_per_customer(self, customer):
        return days_never_visited(
            self.registry[customer]["days"]
        )

    def get_busiest_day(self):
        return max(self.open_days, key=self.open_days.get)

    def get_least_busy_day(self):
        pass
