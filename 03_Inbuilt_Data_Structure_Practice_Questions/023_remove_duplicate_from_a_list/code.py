def remove_duplicates(lst):
    uniques = []
    for number in lst:
        if number not in uniques:
            uniques.append(number)
    return uniques


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print(remove_duplicates([4, 5, 5, 4, 6, 7]))

# Output
# [1, 2, 3, 4, 5]
# [4, 5, 6, 7]
