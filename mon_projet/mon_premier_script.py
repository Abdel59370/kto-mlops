"""
test_mon_premier_script.py
Tests unitaires pour la fonction namespython -m unittest tests/test_mon_premier_script.py
() du script mon_premier_script.py
"""

import unittest
from mon_premier_script import names

class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = names(prenoms)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
