""" cleanup_sequence.py


"""

import re


def cleanup_sequence(sequence):
    """
    Function to cleanup the sequence

    Args:
       sequence: The variable to clear from whitespaces.

    Returns:
       cl_seq: The clean variable
    """
    cl_seq = ""

    for item in re.findall('\S', sequence):
        cl_seq = cl_seq + item

    return cl_seq