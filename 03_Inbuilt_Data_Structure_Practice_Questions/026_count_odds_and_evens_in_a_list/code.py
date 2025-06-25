def count_even_odd(lst):
    evens = 0
    odds = 0
    for num in lst:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds


if __name__ == "__main__":
    print(count_even_odd([1, 2, 3, 4, 5]))

# Output
# (2, 3)
