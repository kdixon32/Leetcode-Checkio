def longest_word(text):
    words = text.split()
    word_lengths = list(map(len, words))
    return words[word_lengths.index(max(word_lengths))]
        