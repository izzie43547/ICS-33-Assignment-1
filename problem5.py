GLOBAL_VAR = 'global'

def scoper():
    """
    Demonstrates Python's variable resolution order (LEGB) by returning a tuple
    containing local, enclosing, and global variables.
    
    Returns:
        tuple: (local_var, ENCLOSING_VAR, GLOBAL_VAR)
    """
    ENCLOSING_VAR = 'enclosing'
    
    def inner():
        LOCAL_VAR = 'local'
        return LOCAL_VAR, ENCLOSING_VAR, GLOBAL_VAR
    
    return inner()
