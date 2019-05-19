def duplicate_encode(word):
    char_counter = {}

    if word:
        for char in word.lower():
            char_counter.update({char: char_counter.get(char, 0) + 1})

    return ''.join(map(lambda x: ')' if char_counter[x] > 1 else '(', word.lower()))
