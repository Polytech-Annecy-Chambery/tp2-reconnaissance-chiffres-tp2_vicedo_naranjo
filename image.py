import numpy
import skimage.transform
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        tobin_array = np.copy(self.pixels) # on créée une copie du tableau de pixels

        mask = tobin_array < S  # on créée un masque identifiant les pixels inférieurs au seuil
        np.putmask(tobin_array, mask, 0)  # on l'applique
        mask = tobin_array >= S # même chose pour les pixels supérieurs ou égaux
        np.putmask(tobin_array, mask, 255)

        result = Image()
        result.set_pixels(tobin_array)
        return result


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        lmin = -1
        lmax = -1
        cmin = -1
        cmax = -1
        for y in range(len(self.pixels)): # on parcours les lignes de l'image unes à unes
            leftOffset = -1  # premier pixel noir rencontré sur la ligne
            rightOffset  = -1  # dernier pixel noir rencontré sur la ligne
            for x in range(len(self.pixels[y])):  # on  parcours les pixels de la ligne courante
                pixel = self.pixels[y][x]
                if leftOffset < 0 and pixel == 0:  # on trouve le premierr pixel noir de la ligne
                    leftOffset = x
                    rightOffset = x
                elif pixel == 0:  # on trouve un autre pixel noir qui devient pour l'instant le dernier de la ligne
                    rightOffset = x
            if leftOffset >= 0: # si on a trouvés au moins un pixel sur la ligne
                if lmin == -1: # si c'est la première ligne avec un pixel noir on set lmin
                    lmin = y
                lmax = y # la ligne courante est forcément lmax
                if leftOffset < cmin or cmin == -1:   # on sauvegarde le premier pixel rencontré si l'indice de sa colonne est inférieur au plus petit indice cmin
                    cmin = leftOffset
                if rightOffset > cmax:  # pareil pour cmax
                    cmax = rightOffset

        result = Image()
        result.set_pixels(self.pixels[lmin:lmax+1, cmin:cmax+1])
        return result

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        result = skimage.transform.resize(np.copy(self.pixels), (new_H, new_W), 0)
        resimg = Image()
        resimg.set_pixels(np.uint8(result*255))
        return resimg



    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        mask = self.pixels == im.pixels  # on utilise un masque sur les pixels identiques aux deux images
        return np.count_nonzero(mask) / (self.H * self.W) # on retourne le nombre de pixels identiques divisé par (H * W)


