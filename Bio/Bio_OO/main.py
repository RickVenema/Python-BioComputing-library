""" main.py


"""
import OO_utils


class DNA:
    def __init__(self, sequence):
        self.sequence = sequence

    def reverse_sequence(self):
        return OO_utils.reverse_string(self.sequence)

