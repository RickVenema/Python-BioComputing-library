""" check_type_var.py

This file contains a function that checks if a variable has the right type
"""


def var_is_string(variable):
    """
    Enter a variable to check if it is a string

    Args:
       variable: the variable to check if it is the right type

    Returns:
       A boolean value, if variable is str() type -> True, else -> False
    """
    if type(variable) is str:
        return True
    else:
        return False

