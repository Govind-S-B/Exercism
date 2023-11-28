def response(hey_bob):
    hey_bob = hey_bob.strip()

    silence = hey_bob.isspace() or hey_bob==""

    if silence:
        return "Fine. Be that way!"
    
    is_english = False
    for char in hey_bob:
        if char.isalpha():
            is_english = True
            break
    
    question = True if hey_bob[-1] == '?' else False
    yell = True if hey_bob.upper() == hey_bob else False

    if question and yell and is_english:
        return "Calm down, I know what I'm doing!"
    elif question :
        return "Sure."
    elif yell and is_english:
        return "Whoa, chill out!"
    
    return "Whatever."