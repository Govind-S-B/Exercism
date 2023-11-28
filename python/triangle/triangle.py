def is_triangle(a,b,c):
    
    if a<=0 or b<=0 or c<=0:
        return False
    
    if a+b>=c and b+c>=a and a+c>=b:
        return True

    return False

def equilateral(sides):

    a,b,c = sides
    if is_triangle(a,b,c):
        return a==b==c
    
    return False

def isosceles(sides):
    
    a,b,c = sides
    if is_triangle(a,b,c):
        return a==b or a==c or b==c
    
    return False


def scalene(sides):

    a,b,c = sides
    if is_triangle(a,b,c):
        return a!=b and a!=c and b!=c
    
    return False
