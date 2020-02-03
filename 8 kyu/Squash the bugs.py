def find_longest(string):
    longest_word = ''
    for word in string.split():
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)