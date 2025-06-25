def merge_dicts_with_overlapping_keys(dicts):
    d = {}
    for dic in dicts:
        for key, value in dic.items():
            if key in d.keys():
                d[key] += value
            else:
                d[key] = value
    return d


if __name__ == "__main__":
    print(
        merge_dicts_with_overlapping_keys(
            [{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"c": 5, "d": 6}]
        )
    )
    print(
        merge_dicts_with_overlapping_keys(
            [{"x": 10, "y": 20}, {"y": 30, "z": 40}, {"z": 50, "x": 60}]
        )
    )

# Output
# {'a': 1, 'b': 5, 'c': 9, 'd': 6}
# {'x': 70, 'y': 50, 'z': 90}
