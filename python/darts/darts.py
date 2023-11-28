def score(x, y):
    
    dist = (x**2 + y**2)**(1/2)

    # score map maps : radius -> score
    score_map = {
        1:10,
        5:5,
        10:1
    }

    default_score = 0

    for range_lim,val in score_map.items():
        if dist <= range_lim:
            return val
    
    return default_score