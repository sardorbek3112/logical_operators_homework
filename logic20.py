def main(a):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x1 = a % 10
    x2 = a // 10 % 10
    x3 = a // 100 % 10
    x4 = a // 1000 % 10
    x5 = a // 10000 % 10
    return x1 + x2 + x3 + x4 + x5 == ((x1 + 1) % 2 + (x2 + 1) % 2 + (x3 + 1) % 2 + (x4 + 1) % 2 + (x5 +1) % 2) or (x1 + x2 + x3 + x4 == (x1 + 1) % 2 + (x2 + 1) % 2 + (x3 + 1) % 2 + (x4 + 1) % 2 and a // 10000 == 0) or (x1 + x2 + x3 == (x1 + 1) % 2 + (x2 + 1) % 2 + (x3 + 1) % 2 and a // 1000 == 0) or (x1 + x2 == (x1 + 1) % 2 + (x2 + 1) % 2 and a // 100 == 0) 
