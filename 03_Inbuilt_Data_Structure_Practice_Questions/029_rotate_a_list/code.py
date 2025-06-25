def rotate_list(lst, k):
    if not lst:
        return lst
    for _ in range(k):
        lst.insert(0, lst.pop())
    return lst


if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))
    print(rotate_list([10, 20, 30, 40, 50], 3))

# Output
# [4, 5, 1, 2, 3]
# [30, 40, 50, 10, 20]
