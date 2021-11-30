import sys
sys.path.append('../src')
sys.path.append('./src')
from image import Image
import numpy as np
import unittest
from reconnaissance import lecture_modeles, reconnaissance_chiffre

path_to_assets = '../assets/'

class Test_reconnaissance_chiffre(unittest.TestCase):
    def test_reconnaissance_is_not_None(self):
        """Teste si la fonction de reconnaissance renvoie bien qquechose.
        Pas d'oublie du return.
        """
        liste_modeles = lecture_modeles(path_to_assets)
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        assert reconnaissance_chiffre(image, liste_modeles, 70) is not None

    def test_reconnaissance_is_int(self):
        """Teste si la fonction de reconnaissance renvoie un entier.
        """
        liste_modeles = lecture_modeles(path_to_assets)
        image = Image()
        image.load(path_to_assets + 'test2.JPG')
        chiffre = reconnaissance_chiffre(image, liste_modeles, 70)
        assert isinstance(chiffre, int)

    def test_reconnaissance_is_numeral(self):
        """Teste si la fonction de reconnaissance renvoie un chiffre.
        """
        liste_modeles = lecture_modeles(path_to_assets)
        image = Image()
        image.load(path_to_assets + 'test3.JPG')
        chiffre = reconnaissance_chiffre(image, liste_modeles, 70)
        assert chiffre <= 9
        assert chiffre >= 0

if __name__ == '__main__':
    import nose2
    nose2.main()