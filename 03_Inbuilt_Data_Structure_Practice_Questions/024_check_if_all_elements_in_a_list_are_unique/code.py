def check_unique(lst):
    uniques = []
    for number in lst:
        if number not in uniques:
            uniques.append(number)
    return uniques == lst


if __name__ == "__main__":
    print(check_unique([1, 2, 3, 4, 5]))
    print(check_unique([1, 2, 3, 3, 4, 5]))

# Output
# True
# False
