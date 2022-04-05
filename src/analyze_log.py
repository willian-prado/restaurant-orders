from read_csv import read_csv
import os.path


def most_frequent(arr):
    frequencies = {}
    most_frequent = arr[0]

    for item in arr:
        if item not in frequencies:
            frequencies[item] = 1
        else:
            frequencies[item] += 1
        if frequencies[item] > frequencies[most_frequent]:
            most_frequent = item

    return most_frequent


def burguer_count(meals):
    burguers = [meal for meal in meals if meal == "hamburguer"]
    return len(burguers)


def meals_never_ordered(meals):
    all_meals = set(["hamburguer", "pizza", "coxinha", "misto-quente"])
    return all_meals.difference(set(meals))


def days_never_visited(days):
    all_days = set(["terça-feira", "segunda-feira", "sabado"])
    return all_days.difference(set(days))


def analyze_log(path_to_file):
    if path_to_file.endswith("csv"):
        if os.path.exists(path_to_file):
            orders = read_csv(path_to_file)
            with open("data/mkt_campaign.txt", "w") as file:
                print(most_frequent(orders["maria"]["meals"]), file=file)
                print(burguer_count(orders["arnaldo"]["meals"]), file=file)
                print(meals_never_ordered(orders["joao"]["meals"]), file=file)
                print(days_never_visited(orders["joao"]["days"]), file=file)
        else:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
