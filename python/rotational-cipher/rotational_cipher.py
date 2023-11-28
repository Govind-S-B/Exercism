def rotate(text, key):

    key = key % 26

    return_string = ""
    
    for char in text:

        if not char.isalpha():
            return_string += char
            continue

        if char.islower():
            start_chr = 'a'
            end_chr = 'z'
        elif char.isupper():
            start_chr = 'A'
            end_chr = 'Z'

        new_ord = ord(char) + key
        
        if new_ord > ord(end_chr):
            new_ord = ord(start_chr) + new_ord - ord(end_chr) - 1

        return_string += chr(new_ord)

    return return_string