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


def analyze_log(path_to_file):
    raise NotImplementedError
