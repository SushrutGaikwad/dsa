def merge_two_sorted_lists(list1, list2):
    i = 0
    j = 0
    output = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1
    while i < len(list1):
        output.append(list1[i])
        i += 1
    while j < len(list2):
        output.append(list2[j])
        j += 1
    return output


if __name__ == "__main__":
    print(merge_two_sorted_lists([1, 3, 5], [2, 4, 6]))
    print(merge_two_sorted_lists([1, 4, 7], [2, 3, 5, 8]))

# Output
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 7, 8]
