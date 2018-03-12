""" ORF_finder.py
This program contains an Open Reading Frame finder and returns all the orfs in a list.
Version: 0.1a
Author: Rick Venema
"""
# IMPORTS
import re

# METADATA
__author__ = "Rick Venema"
__version__ = "0.1a"


def ORF_finder(sequence):
    """ ORF finder
    This function will search for all ORFs in a sequence
    :param sequence: The sequence that needs to be scanned for ORFs
    :return: A list containing all the orfs in the sequence
    """
    orfs = []
    for item in re.findall(r'(?=(ATG(?:...)+?)(TAG|TGA|TAA))', sequence):
        orfs.append(item[0] + item[1])
    return orfs


if __name__ == '__main__':
    print(ORF_finder("ATGAAATAG"))
