def merge_lists_to_dictionary(keys, values):
    if len(keys) != len(values):
        return False
    d = dict()
    for idx, key in enumerate(keys):
        d[key] = values[idx]
    return d


if __name__ == "__main__":
    print(merge_lists_to_dictionary(["a", "b", "c"], [1, 2, 3]))
    print(merge_lists_to_dictionary(["x", "y", "z"], [10, 20, 30]))

# Output
# {'a': 1, 'b': 2, 'c': 3}
# {'x': 10, 'y': 20, 'z': 30}
