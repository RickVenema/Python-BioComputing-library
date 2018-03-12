""" __init__.py

This is the test file of the Bio library
"""
import Bio.ORF_finder as ORF_finder
import Bio.DNA_object as DNA_object
import Bio.Global_Alignment as Global_Alignment


print(ORF_finder.ORF_finder("ATGAAATAG"))
print(ORF_finder.__author__)
test = DNA_object.DNA("ATGAAATAG")
test.__getORFs__()
print(test.orfs)
print(test)

Global_Alignment.main()