
def RNA_to_protein(RNA_sequence):
    """
    The function that return the protein string encoded by RNA sequence.
    """

    RNA_codon_table = {
        'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
        'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
        'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
        'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
        'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
        'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
        'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
        'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
        'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
        'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
        'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
        'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
        'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
        'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
        'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
        'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'
    }

    sequence_codon = [RNA_sequence[i : i+3] for i in range(0, len(RNA_sequence), 3)] 
    
    #finding first codon start - AUG
    if "AUG" in sequence_codon:
        start_codon_index = sequence_codon.index("AUG")

        #finding first codon stop - UAA, UAG, UGA
        stop_codon_index = []
        if 'UAA' in sequence_codon:
            stop_codon_index.append(sequence_codon.index("UAA"))
        elif 'UAG' in sequence_codon:
            stop_codon_index.append(sequence_codon.index("UAG"))
        elif "UGA" in sequence_codon:
            stop_codon_index.append(sequence_codon.index("UGA"))
        else:
            stop_codon_index.append(len(RNA_sequence))
        first_stop_codon = min(stop_codon_index)

        #translating RNA sequence into protein
        protein = ''
        for codon_index in range(start_codon_index, first_stop_codon):
            protein += RNA_codon_table[sequence_codon[codon_index]]
        
        return protein
        
    else:
        print("This RNA sequence don't have the start codon.")

# ------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
    def test_RNA_to_protein(self):
        protein = RNA_to_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
        self.assertEqual(protein, 'MAMAPRTEINSTRING')

if __name__ == '__main__':
    unittest.main()