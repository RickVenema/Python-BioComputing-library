#/usr/bin/python3

"""
My module for bioinformatics
---------------------------
__author__ = Rick Venema
__status__ = Stable
---------------------------
Contains functions that I've programmed 

"""
__author__ = 'Rick Venema'
__status__ = 'Stable'

import re
import argparse


def argparsing():
    """
    function to make the argparse
    """
    
    parser = argparse.ArgumentParser(description='My module')
    
    parser.add_argument("-Is_string", help="Checks if a variable is a string", action="store", type=var_is_string)
    parser.add_argument("-is_dna", help="Checks if a variable is a DNA strand", action="store", type=isvaliddna)
    parser.add_argument("-gb_to_fasta", help="Convert GenBank file to FASTA file", action="store", type=genbank_to_fasta)
    
    args = parser.parse_args()


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


def isvaliddna(check_if_dna):
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

        
def isvalidrna(check_if_rna):
    """
    Enter a string to check if it valid RNA


    Args:
        check_if_rna: a string to check if it is RNA or not

    Returns:
        A boolean value, if the string is RNA -> True, if not RNA -> False

    Exeptions:
        TypeError: if the type of the variable is not right, it will output an ERROR message
    """
    try:
        if var_is_string(check_if_rna):
            p = re.compile('[augcAUGC]+')
        
            rna = p.fullmatch(check_if_rna)
            if rna:
                return True
            else:
                return False
        else:
            raise TypeError
    except TypeError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in isvalidrna is not right type")
        print("SOLUTION: ENTER A STRING TYPE VARIABLE (str)")


def isavalid_protein(check_if_protein):
    """
    Enter a string to check if it can be a protein.

    Args:
       check_if_protein: a string to check if it is a protein

    Returns:
       A boolean value, if the string is a protein -> True, if not -> False

    Exeptions:
       TypeError: if the type is not correct, it will output an ERROR message
    """
    try:
        p = re.compile('[gavlimpfwstycnqkrhdeGAVLIMPFWSTYCNQKRHDE]+')
        if var_is_string(check_if_protein):
            is_protein = p.fullmatch(check_if_protein)
            if is_protein:   
                return True
            else:
                return False
        else:
            raise TypeError
        
    except TypeError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in isavalid_protein is not right type")
        print("SOLUTION: ENTER A STRING TYPE VARIABLE (str)")


def getopenreading_frames(getopenreading):
    """
    Enter a string to get the open reading frames from that string

    Args:
       getopenreading: a string containing dna

    Returns:
       a list containing all the open reading frames in the string

    Exeptions:
       ValueError: if the string is not DNA there will be an ERROR message
    """
    try:
        if isvaliddna(getopenreading):         
            getopenreading = getopenreading.upper()    
            frames = []
            items = re.findall(r'ATG(?:(?!TAA|TAG|TGA)...)*(?:TAA|TAG|TGA)', getopenreading)                   
            return items
        
        else:
            raise ValueError
    except ValueError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in getopenreading_frames is not DNA")
        print("SOLUTION: ENTER A VALID DNA STRING")


def create_fasta_header(identifier, comments):
    """
    Function to create an fasta header

    Args:
       identifier: the identifier of the header

       comments: the comments to go at the end of the header 
    """

    fasta_header = '>lcl' + "|" + identifier + "|" + comments
    return fasta_header


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


def get_reversed_complement_dna(dna_seq):
    """
    Gets the reversed complement dna string.

    Args:
       dna_seq: the sequence of the dna to get reversed complement dna


    Returns:
        A string containing the reversed complement dna string
        If it is not DNA the function will raise an error

    Raises:
        ValueError:
            An error to show that the string is not dna

        TypeError:
            An error to show that the variable is not string type
    """
    try:
        
        if var_is_string(dna_seq):
            reversed_complement_dna = dna_seq.upper()
            if isvaliddna(dna_seq):
                reversed_complement_dna = re.sub('A', 't', reversed_complement_dna)
                reversed_complement_dna = re.sub('T', 'a', reversed_complement_dna)
                reversed_complement_dna = re.sub('G', 'c', reversed_complement_dna)
                reversed_complement_dna = re.sub('C', 'g', reversed_complement_dna)
                reversed_complement_dna = reversed_complement_dna.upper()[::-1]
                return reversed_complement_dna
            else:
                raise ValueError
        else:
            raise TypeError
    # ERROR MESSAGES
    except TypeError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in get_reversed_complement_dna is not right type")
        print("SOLUTION: ENTER A STRING TYPE VARIABLE (str)")
        
    except ValueError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in get_reversed_complement_dna is not DNA")
        print("SOLUTION: ENTER A VALID DNA STRING")


def translate_dna_to_rna(dna):
    """
    Function to translate DNA to RNA

    Args:
       dna: The DNA to be translated to RNA

    Returns:
       rna: The RNA translated from the DNA string entered
    """
    try:
        if isvaliddna(dna):
            rna = dna.upper()
            rna = rna.replace("T", "U")
            return rna
        else:
            raise ValueError
            
    except ValueError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in translate_dna_to_rna is not DNA")
        print("SOLUTION: ENTER A VALID DNA STRING")


def get_mrna(seq):
    """
    A Function to get the mRNA contained in the dna. The DNA sequence must be the antisense.

    Args:
       seq: The antisense strand of the dna

    Returns:
       mrna_frames: The list of the mrna strands in the dna

    Exeptions:
        ValueError: If the sequence entered is not dna, it will output an ERROR message
    """
    try:
        if isvaliddna(seq):
            seq = get_reversed_complement_dna(seq)
            frames = getopenreading_frames(seq)
            mrna_frames = []
            for frame in frames:
                
                mrna_frames.append(translate_dna_to_rna(frame))
            
            return mrna_frames
        else:
            raise ValueError

    except ValueError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in get_mrna is not DNA")
        print("SOLUTION: ENTER A VALID DNA STRING")


def has_hairpin(seq):
    """
    A function to check if a string has a hairpin.

    Args:
       seq: Antisense strand of DNA, that needs to be checked.

    Returns:
       outcome: a boolean value, True if there is a hairpin, if not: False

    Exceptions:
       ValueError: The entered string is not DNA

    """
    try:
        seq = seq.upper()
        if isvaliddna(seq):
            
            seq_parts = [seq[i:i+30] for i in range(0, len(seq))]
            outcome = False
            for seq in seq_parts:
                print(seq)
                split_seq = [seq[i:i+3] for i in range(0, len(seq))]
                
                for i, part in enumerate(split_seq):
                    part = get_reversed_complement_dna(part)

                    for j in range(i, len(split_seq)):
                        
                        if split_seq[j] == part:
                            
                            outcome = True

        else:
            raise ValueError

        return outcome

    except ValueError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in has_hairpin is not DNA")
        print("SOLUTION: ENTER A VALID DNA STRING")


def codon_table():
    """
    A function to create the codon table:

    Returns:
       the codon table with the one letter codes
    """
    codontable = {
                'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
                'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
                'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
                'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
                'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
                'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
                'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
                'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
                'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
                'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
                'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
                'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
                'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
                'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
                'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
                'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
                }
    return codontable


def translate_dna_to_protein(seq):
    """
    A function to translate DNA to protein. 

    Args:
      seq: the DNA sequence

    Returns:
       proteins: the proteins in the dna sequence

    Raises:
       ValueError: if the entered sequence is not valid DNA the function will output an Error
    """
    try:
        if isvaliddna(seq):
            frames = getopenreading_frames(seq)
            codontabel = codon_table()
            proteins = []
            for frame in frames:
                split_frame = [ frame[i:i+3] for i in range(0, len(frame), 3) ]
                protein = ""
                for codon in split_frame:
                    protein = protein + codontabel[codon]
                protein = protein.replace("_","")
                proteins.append(protein)
                
            return proteins
        else:
            raise ValueError
                
    except ValueError:
        print("WARNING: An ERROR has occured!")
        print("ERROR: INPUT in has_hairpin is not DNA")
        print("SOLUTION: ENTER A VALID DNA STRING")
        
        
def genbank_to_fasta(file_path):
    """
    function to convert a genbank file to a fasta file

    Args:
       file_path: the path to the file to be converted

    Returns:
       output.fasta: the fasta file
    """
    with open(file_path, 'r') as gb_file:
        with open('outcome.fasta', 'w') as output:
            gb_file = gb_file.read()
            gb_after_origin = gb_file.rpartition('ORIGIN')
            unparsed_dna = gb_after_origin[2]
            no_nr = re.sub(r'\d', '', unparsed_dna)
            almost_clean = re.sub(r'//', '', no_nr)
            
            clean = cleanup_sequence(almost_clean)
            output_str = [ clean[i:i+80] for i in range(0, len(clean), 80) ]
            
            identifier = re.findall(r'(ACCESSION)(.*)', gb_file)
            identifier = cleanup_sequence(identifier[0][1])
            comments = "\n"
            header = create_fasta_header(identifier, comments)
            output.write(header)
            for item in output_str:
                output.write("%s\n" % item)

                
if __name__ == '__main__':
    argparsing()
