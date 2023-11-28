def is_armstrong_number(number):

    computer_num = 0

    seq = str(number)
    for num in seq:
        computer_num += int(num)**len(seq)

    return computer_num == number