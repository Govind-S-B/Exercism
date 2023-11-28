def is_pangram(sentence):

    char_set = set()
    
    for char in sentence:
        if char.isalpha():
            char_set.add(char.lower())

    return len(char_set) == 26
