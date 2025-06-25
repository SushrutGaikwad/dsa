def merge_three_dictionaries(dict1, dict2, dict3):
    d = dict()
    dicts = [dict1, dict2, dict3]
    for dic in dicts:
        for key, value in dic.items():
            d[key] = value
    return d


if __name__ == "__main__":
    print(
        merge_three_dictionaries({"a": 1, "b": 2}, {"c": 3, "d": 4}, {"e": 5, "f": 6})
    )
    print(merge_three_dictionaries({"x": 10, "y": 20}, {"z": 30}, {"a": 40, "b": 50}))

# Output
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}
