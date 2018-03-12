import Bio.ORF_finder as ORF


class DNA:
    def __init__(self, input_sequence):
        self.sequence = input_sequence

    def __repr__(self):
        return "The sequence: {0}".format(self.sequence)

    def __getORFs__(self):
        self.orfs = ORF.ORF_finder(self.sequence)
