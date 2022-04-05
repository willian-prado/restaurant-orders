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


def analyze_log(path_to_file):
    raise NotImplementedError
