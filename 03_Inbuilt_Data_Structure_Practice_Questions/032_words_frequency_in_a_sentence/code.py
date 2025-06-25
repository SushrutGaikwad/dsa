def count_word_frequency(sentence):
    if len(sentence) == 0:
        return {}
    words_lst = sentence.split(" ")

    d = dict()
    for word in words_lst:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1

    return d


if __name__ == "__main__":
    print(count_word_frequency("hello world hello"))
    print(count_word_frequency("the quick brown fox jumps over the lazy dog"))

# Output
# {'hello': 2, 'world': 1}
# {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
