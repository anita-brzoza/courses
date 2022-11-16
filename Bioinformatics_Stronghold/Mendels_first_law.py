
def mendels_first_law(k, m, n):
    """
    A function that returns the probability that two randomly selected mating organisms 
    will produce an individual possessing a dominant allele (and thus displaying the 
    dominant phenotype)

    Three positive integers k, m, and n, representing a population containing k+m+n organisms:
    k - number of homozygous dominant organisms, 
    m - number of heterozygous organisms, 
    n - number of homozygous recessive organisms.
    """
    
    population = k + m + n

    #possible combinations of indywiduals that will give the dominant allele
    kk = (k/population) * ((k-1)/(population-1)) * 1
    mm = (m/population) * ((m-1)/(population-1)) * 0.75
    km_mk = (((k/population) * ((m)/(population-1))) + ((m/population) * ((k)/(population-1)))) * 1
    kn_nk = (((k/population) * ((n)/(population-1))) + ((n/population) * ((k)/(population-1)))) * 1
    mn_nm = (((m/population) * ((n)/(population-1))) + ((n/population) * ((m)/(population-1)))) * 0.5

    #the probability that two randomly selected mating organisms will produce an individual 
    # possessing a dominant allele
    dominant_probality = kk + mm + km_mk + kn_nk + mn_nm

    return dominant_probality


"""
------------------------------------------------------------------------------------------------
The unit tests
------------------------------------------------------------------------------------------------
"""

import unittest
class Test(unittest.TestCase):
    def test_mendels_first_law1(self):
        dominant_probality = mendels_first_law(26,23,29)
        self.assertEqual(dominant_probality, 0.7326839826839826)

    def test_mendels_first_law2(self):
        dominant_probality = mendels_first_law(2,2,2)
        self.assertEqual(round(dominant_probality, 5), 0.78333)

if __name__ == '__main__':
    unittest.main()