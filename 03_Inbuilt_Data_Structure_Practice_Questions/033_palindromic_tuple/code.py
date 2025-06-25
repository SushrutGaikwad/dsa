def is_palindromic_tuple(tup):
    if len(tup) == 0:
        return True
    i = 0
    j = len(tup) - 1
    while i <= len(tup) // 2:
        if tup[i] != tup[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    print(is_palindromic_tuple((1, 2, 3, 2, 1)))
    print(is_palindromic_tuple(("a", "b", "c", "b", "a")))
    print(is_palindromic_tuple((1, 2, 3, 4, 5)))
    print(is_palindromic_tuple(("x", "y", "z", "x")))
    print(is_palindromic_tuple(("a",)))

# Output
# True
# True
# False
# False
# True
