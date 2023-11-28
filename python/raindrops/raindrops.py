def convert(number):
    
    raindrop_string = ""

    word_map = {
        3:"Pling",
        5:"Plang",
        7:"Plong"
    }

    for num in word_map:
        if number%num == 0:
            raindrop_string+=word_map[num]
    
    if raindrop_string == "":
        raindrop_string = str(number)

    return raindrop_string