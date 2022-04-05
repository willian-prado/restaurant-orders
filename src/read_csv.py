import csv


def read_csv(file_name):
    with open(file_name) as file:
        file_reader = csv.reader(file)
        orders = {}

        for row in file_reader:
            name, item, day = row[0], row[1], row[2]

            if name not in orders:
                orders[name] = {"meals": [item], "days": [day]}
            else:
                orders[name]["meals"].append(item)
                orders[name]["days"].append(day)

        return orders
