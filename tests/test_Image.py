import sys
sys.path.append('../src')
sys.path.append('./src')
from image import Image
import numpy as np
from numpy.testing import assert_almost_equal
import unittest
import numbers

path_to_assets = '../assets/'

class Test_Image_binarisation(unittest.TestCase):
    def test_binarisation_is_not_none(self):
        """Teste si le résultat de la binarisation renvoie bien quelque chose.
        Cad, pas d'oublie du return...
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(10)
        assert image_binarisee is not None

    def test_binarisarisation_is_Image(self):
        """Teste si le résultat de la binarisastion est bien de la classe Image.
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(10)
        assert isinstance(image_binarisee, Image)

    def test_binarisation_is_different_image(self):
        """Teste si après binarisation, l'objet obtenu est bien une nouvelle image
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(20)
        assert image_binarisee is not image

    def test_binarisation_pixels_is_array(self):
        """Teste si les pixels de l'objet de type Image résultant de la méthode binarisation
        est bien un numpy array.
        """
        image = Image()
        image.load(path_to_assets + 'test2.JPG')
        image_binarisee = image.binarisation(30)
        assert isinstance(image_binarisee.pixels, np.ndarray)

    def test_binarisation_shape_attributes(self):
        """Teste si les attributs de taille de l'objet de type Image résultant de la méthode
        binarisation sont bien de les mêmes que l'image initiale.
        """
        image = Image()
        image.load(path_to_assets + 'test3.JPG')
        image_binarisee = image.binarisation(1)
        assert image_binarisee.H == image.H
        assert image_binarisee.W == image.W

    def test_binarisation_pixels_shape(self):
        """Teste si les pixels de de l'objet de type Image résultant de la méthode binarisation
        est bien un numpy array de la taille de l'image initiale.
        """
        image = Image()
        image.load(path_to_assets + 'test4.JPG')
        image_binarisee = image.binarisation(1)
        assert image_binarisee.pixels.shape == image.pixels.shape

    def test_binarisation_is_binary(self):
        """Teste si l'image binarisée renvoie bien une image avec seulement deux valeurs de 0 et 255.
        """
        image = Image()
        image.load(path_to_assets + 'test5.JPG')
        image_binarisee = image.binarisation(1)
        assert np.all(np.unique(image_binarisee.pixels) == [0, 255])


class Test_Image_localisation(unittest.TestCase):
    def test_localisation_is_not_none(self):
        """Teste si le résultat de la localisation renvoie bien quelque chose.
        Cad, pas d'oublie du return...
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(10)
        image_localisee = image_binarisee.localisation()
        assert image_localisee is not None

    def test_localisation_is_Image(self):
        """Teste si le résultat de la localisation est bien de la classe Image.
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(10)
        image_localisee = image_binarisee.localisation()
        assert isinstance(image_localisee, Image)

    def test_localisation_is_different_image(self):
        """Teste si après localisation, l'objet obtenu est bien une nouvelle image
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(20)
        image_localisee = image_binarisee.localisation()
        assert image_localisee is not image_binarisee

    def test_localisation_pixels_is_array(self):
        """Teste si les pixels de l'objet de type Image résultant de la méthode localisation
        est bien un numpy array.
        """
        image = Image()
        image.load(path_to_assets + 'test2.JPG')
        image_binarisee = image.binarisation(30)
        image_localisee = image_binarisee.localisation()
        assert isinstance(image_localisee.pixels, np.ndarray)

    def test_localisation_shape_attributes_are_smaller(self):
        """Teste si les attributs de taille de l'objet de type Image résultant de la méthode
        binarisation sont bien de les inférieurs à l'image initiale et image binarisée.
        """
        image = Image()
        image.load(path_to_assets + 'test3.JPG')
        image_binarisee = image.binarisation(1)
        image_localisee = image_binarisee.localisation()
        assert image_localisee.H <= image.H
        assert image_localisee.W <= image.W
        assert image_localisee.H <= image_binarisee.H
        assert image_localisee.W <= image_binarisee.W

    def test_localisation_pixels_shape_is_smaller(self):
        """Teste si le numpy array des pixels de l'objet de type Image résultant de la méthode
        localisation a bien une taille inférieure ou égale à l'image de départ
        """
        image = Image()
        image.load(path_to_assets + 'test4.JPG')
        image_binarisee = image.binarisation(30)
        image_localisee = image_binarisee.localisation()
        assert np.all(image_localisee.pixels.shape <= image.pixels.shape)
        assert np.all(image_localisee.pixels.shape <= image_binarisee.pixels.shape)


class Test_Image_resize(unittest.TestCase):
    def test_resize_is_not_none(self):
        """Teste si le résultat de resize renvoie bien quelque chose.
        Cad, pas d'oublie du return...
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(10)
        image_localisee = image_binarisee.localisation()
        new_H, new_W = 30, 70
        image_resizee = image_localisee.resize(new_H, new_W)
        assert image_resizee is not None

    def test_resize_is_Image(self):
        """Teste si le résultat de resize est bien de la classe Image.
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(10)
        image_localisee = image_binarisee.localisation()
        new_H, new_W = 30, 70
        image_resizee = image_localisee.resize(new_H, new_W)
        assert isinstance(image_resizee, Image)

    def test_resize_is_different_image(self):
        """Teste si après resize, l'objet obtenu est bien une nouvelle image
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        image_binarisee = image.binarisation(20)
        image_localisee = image_binarisee.localisation()
        new_H, new_W = 30, 70
        image_resizee = image_localisee.resize(new_H, new_W)
        assert image_resizee is not image_binarisee

    def test_resize_pixels_is_array(self):
        """Teste si les pixels de l'objet de type Image résultant de la méthode resize
        est bien un numpy array.
        """
        image = Image()
        image.load(path_to_assets + 'test2.JPG')
        image_binarisee = image.binarisation(30)
        image_localisee = image_binarisee.localisation()
        new_H, new_W = 30, 70
        image_resizee = image_localisee.resize(new_H, new_W)
        assert isinstance(image_resizee.pixels, np.ndarray)

    def test_resize_attributes(self):
        """Teste si les attributs de l'objet de type Image résultat de la méthode resize
        sont de la taille attendue.
        """
        image = Image()
        image.load(path_to_assets + 'test2.JPG')
        image_binarisee = image.binarisation(30)
        image_localisee = image_binarisee.localisation()
        new_H, new_W = 30, 70
        image_resizee = image_localisee.resize(new_H, new_W)
        assert image_resizee.H == new_H
        assert image_resizee.W == new_W


class Test_Image_similitude(unittest.TestCase):
    def test_similitude_is_not_none(self):
        """Teste la méthode similitude ne renvoie pas None (oublie de return...).
        """
        image = Image()
        image.load(path_to_assets + 'test2.JPG')
        assert image.similitude(image) is not None

    def test_similitude_is_number(self):
        """Teste si la méthode similitude renvoie un nombre et pas autre chose
        """
        image = Image()
        image.load(path_to_assets + 'test1.JPG')
        assert isinstance(image.similitude(image), numbers.Number)

    def test_similitude_same_image_is_one(self):
        image = Image()
        image.load(path_to_assets + 'test2.JPG')
        assert image.similitude(image) == 1

    def test_similitude_negative_image_is_zero(self):
        image = Image()
        image.load(path_to_assets + 'test3.JPG')
        image_binarisee = image.binarisation(10)
        negative_image = Image()
        negative_image.set_pixels(np.abs(255-image_binarisee.pixels))
        assert image.similitude(negative_image) == 0

if __name__ == '__main__':
    import nose2
    nose2.main()