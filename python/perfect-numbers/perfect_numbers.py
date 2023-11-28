def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number<1:
        raise ValueError("Classification is only possible for positive integers.")

    pos_divs_sum = 0

    for num in range(1,number):
        if number%num == 0:
            pos_divs_sum += num

    if number == pos_divs_sum:
        return "perfect"
    if number > pos_divs_sum:
        return "deficient"
    return "abundant"