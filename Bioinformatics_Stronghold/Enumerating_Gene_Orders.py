
def enumerating_gene_orders(n):
    """
    Function calculate gene orders.
    Input: number of genes
    Output: number of possible permutations and possible rearrangements
    """
    import itertools

    perm = list(itertools.permutations(range(1, n+1)))
    return len(perm), perm

# ------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
    
    def test_enumerating_gene_orders(self):
        """Unit test for enumerating_gene_orders() function"""
        num_permutations, permutations = enumerating_gene_orders(3)
        self.assertEqual(num_permutations, 6)
        self.assertEqual(permutations, [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])

if __name__ == '__main__':
    unittest.main()
