"""
test_mon_premier_script.py

Tests unitaires pour la fonction names() du script mon_premier_script.py
"""
cat << 'EOF' > tests/test_mon_premier_script.py
"""
test_mon_premier_script.py

Tests unitaires pour la fonction names() du script mon_premier_script.py
"""

import unittest
from mon_premier_script import names

class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = names(prenoms)
        # On sait que 4 prénoms ont plus de 7 lettres (Guillaume, Juliette, François, Cassandre)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
