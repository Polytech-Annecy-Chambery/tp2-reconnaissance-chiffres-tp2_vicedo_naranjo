from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    bin_img = image.binarisation(S)  # on binarise l'image
    local_img = bin_img.localisation()  # on localise l'image
    resize_img = local_img.resize(40, 40)  # on resize l'image
    sim_max = 0  # similarité max trouvée
    k = -1  # nombre correspondant à la similarité max trouvée

    for index, model in enumerate(liste_modeles):  # on applique les mêmes traitements à chaques modèles et on calcule la similitude entre les deux images
        bin_model = model.binarisation(S)
        local_model = bin_model.localisation()
        resize_model = local_model.resize(40, 40)
        sim = resize_img.similitude(resize_model)
        if sim > sim_max:  # si la similarité est la plus grande trouvée, on la sauvegarde
            sim_max = sim
            k = index
    return k

