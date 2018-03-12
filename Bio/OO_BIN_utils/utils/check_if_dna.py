""" check_if_dna.py

"""

import re
from check_type_var import var_is_string
from cleanup_sequence import cleanup_sequence


def check_if_dna(check_if_dna):
    """
    Enter a string and the function will output True or False

    Function to check if the entered string is dna

    Args:
       check_if_dna: a string to be checked if it is DNA

    Returns:
       A boolean value, if it is DNA -> True, if it is not DNA -> False

    Exeptions:
        TypeError: If the type is not right, it will output an ERROR message with solution
    """

    try:
        if var_is_string(check_if_dna):
            check_if_dna = cleanup_sequence(check_if_dna)
            p = re.compile('[atgcATGC]+')

            is_valid_dna = p.fullmatch(check_if_dna)
            if is_valid_dna:

                return True
            else:

                return False
        else:
            raise TypeError

    except TypeError:

        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in isvaliddna is not right type")
        print("SOLUTION: ENTER A STRING TYPE VARIABLE (str)")

