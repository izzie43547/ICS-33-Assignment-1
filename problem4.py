from tools import double

def quadruple(n):
    """
    Returns quadruple the given number by using the double function twice.
    
    Args:
        n (int): The number to quadruple
        
    Returns:
        int: Quadruple the input number
    """
    return double(double(n))
