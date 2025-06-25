def reverse_list(lst):
    rev_lst = []
    for i in range(len(lst) - 1, -1, -1):
        rev_lst.append(lst[i])
    return rev_lst


if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4, 5]))

# Output
# [5, 4, 3, 2, 1]
