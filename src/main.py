'''
File: main.py
Created Date: Friday August 27th 2021 - 02:35pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Aug 30 2021
Modified By: Ammar Mian
-----
Copyright (c) 2021 Université Savoie Mont-Blanc
'''
import matplotlib.pyplot as plt
from image import Image
from reconnaissance import reconnaissance_chiffre, lecture_modeles


if __name__ == '__main__':

    # Variables utiles
    path_to_assets = '../assets/'
    plt.ion() # Mode interactif de matplotlib our ne pas bloquer l'éxécutions lorsque l'on fait display

    #==============================================================================
    # Lecture image et affichage
    #==============================================================================
    image = Image()
    image.load(path_to_assets + 'test2.JPG')
    image.display("Exemple d'image")

    #==============================================================================
    # Binarisation de l'image et affichage
    #==============================================================================
    S = 70
    image_binarisee = image.binarisation(S)
    image_binarisee.display("Image binarisee")

    #==============================================================================
    # Localisation de l'image et affichage
    #==============================================================================
    image_localisee = image_binarisee.localisation()
    image_localisee.display("Image localisee")

    #==============================================================================
    # Redimensionnement de l'image et affichage
    #==============================================================================
    image_resizee = image_localisee.resize(100, 500)
    image_resizee.display("Image redimensionee")

    #==============================================================================
    # Lecture modeles et reconnaissance
    #==============================================================================
    liste_modeles = lecture_modeles(path_to_assets)
    chiffre = reconnaissance_chiffre(image, liste_modeles, 70)
    print("Le chiffre reconnu est : ", chiffre)