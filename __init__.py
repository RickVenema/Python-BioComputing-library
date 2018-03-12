""" __init__.py

This is the first file to call when using this library
"""
import Bio.ORF_finder as ORF_finder
import Bio.DNA_object as DNA_object

print(ORF_finder.ORF_finder("ATGAAATAG"))
print(ORF_finder.__author__)
test = DNA_object.DNA("ATGAAATAG")
test.__getORFs__()
print(test.orfs)
print(test)
