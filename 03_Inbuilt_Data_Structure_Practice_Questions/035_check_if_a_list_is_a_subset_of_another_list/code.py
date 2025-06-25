def is_subset(lst1, lst2):
    subset = True
    for ele in lst1:
        if ele not in lst2:
            subset = False
    return subset


if __name__ == "__main__":
    print(is_subset([1, 2, 3], [1, 2, 3, 4, 5]))
    print(is_subset([1, 6], [1, 2, 3, 4, 5]))

# Output
# True
# False
