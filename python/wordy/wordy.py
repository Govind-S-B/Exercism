def answer(question):
    words = question.split()

    if words[0] != "What":
        raise ValueError("Non-math questions")
    
    skip_flag = 0

    if len(words) < 3:
        raise ValueError("no operands or operends")
    
    num = words[2]

    for index,word in enumerate( words[3:-1] ):

        if skip_flag != 0:
            skip_flag -= 1
            continue

        if word == "plus":
            # fetch next num and set pass flag == 1
            if not words[index+1].isnumeric():
                raise ValueError("syntax error")
            num = num + int(words[index+1]) # this must be a int if not raise syntax error
            skip_flag +=1

        if word == "minus":
            # fetch next num and set pass flag == 1
            if not words[index+1].isnumeric():
                raise ValueError("syntax error")
            num = num - int(words[index+1]) # this must be a int if not raise syntax error
            skip_flag +=1

        elif word == "multiply":
            if words[index+1] != "by":
                raise ValueError("syntax error")
            if not words[index+1].isnumeric():
                raise ValueError("syntax error")
            num = num * int(words[index+2]) # this must be a int if not raise a syntax error or expected number
            # next word must be "by" if not syntax error
            # and the one after must be numeric
            skip_flag += 2

        # anything else invalid operation
        else:
            raise ValueError("unknown operation")

        
    return num