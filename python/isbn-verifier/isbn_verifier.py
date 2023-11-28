def is_valid(isbn):
    
    isbn_list = []

    for char in isbn:
        if char == "-":
            continue
        if char.isdigit():
            isbn_list.append(int(char))
            continue
        if char == "X" and isbn[-1] == "X" :
            isbn_list.append(10)
            continue
        return False

    if len(isbn_list) != 10:
        return False
    
    isbn_sum = 0

    for index,num in enumerate(isbn_list):
        isbn_sum += num * (10-index)

    return isbn_sum%11==0