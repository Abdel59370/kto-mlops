import unittest
from typing import List

def count_names_with_more_than_seven_letters(name_list: List[str]) -> int:
    """
    Compte le nombre de prénoms ayant plus de 7 lettres.
    
    :param name_list: Liste des prénoms à analyser
    :return: Nombre de prénoms ayant plus de 7 lettres
    """
    return sum(1 for name in name_list if len(name) > 7)

class TestCountNamesMethod(unittest.TestCase):
    def test_count_names_with_more_than_seven_letters(self):
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_names_with_more_than_seven_letters(names_list)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
