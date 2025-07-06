def half(n):
    """
    Returns half of the given number (integer division).
    
    Args:
        n (int): The number to halve
        
    Returns:
        int: Half of n (using integer division)
    """
    return n // 2

def describe_half(n):
    """
    Returns a string describing the result of halving n.
    
    Args:
        n (int): The number to describe
        
    Returns:
        str: A formatted string describing the result of halving n
    """
    return f"Half of {n} is {half(n)}"
