import unittest
import shutil
from pathlib import Path
from cats_dogs_other.label.extraction import extract_images

# Définition des chemins
BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"

class TestExtraction(unittest.TestCase):

    def test_pdfs_images_should_be_extracted(self):
        """ Vérifie que les images sont bien extraites des PDFs """

        # Nettoyage du répertoire de sortie s'il existe déjà
        if output_directory.is_dir():
            shutil.rmtree(str(output_directory))

        # Exécute l'extraction
        result = extract_images(str(input_directory), str(output_directory))

        # Vérifie le nombre de fichiers d'entrée
        expected_number_files_input = 3
        self.assertEqual(expected_number_files_input, result.number_files_input)

        # Vérifie le nombre d'images extraites
        expected_number_images_output = 4
        self.assertEqual(expected_number_images_output, result.number_images_output)

        # Nettoyage après le test
        shutil.rmtree(str(output_directory))

if __name__ == "__main__":
    unittest.main()
