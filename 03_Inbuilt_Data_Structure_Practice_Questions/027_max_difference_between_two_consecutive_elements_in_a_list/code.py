def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(len(lst) - 1):
        if max_diff < abs(lst[i + 1] - lst[i]):
            max_diff = abs(lst[i + 1] - lst[i])
    return max_diff


if __name__ == "__main__":
    print(max_consecutive_difference([1, 7, 3, 10, 5]))
    print(max_consecutive_difference([10, 11, 15, 3]))

# Output
# 7
# 12
