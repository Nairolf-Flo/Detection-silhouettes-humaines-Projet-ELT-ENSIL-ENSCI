from pycocotools.coco import COCO
import matplotlib.pyplot as plt
import os
import shutil

dataDir=os.getcwd() # Chemin du dossier ou s'execute le script
dataType='val2017'  # Dossier contenant les images
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)


coco=COCO(annFile) # initialize COCO api for instance annotations

categoriesVehicules = ['car','bus']
categoriesPerson = ['person']
categoriesAnimals = ['cat','dog','sheep','cow','horse']
cattest = ['dog','cat']

images = []
touteslescatIds=coco.getCatIds(catNms=categoriesVehicules)
for className in categoriesVehicules:   #il est peut être possible de se passer de la boucle
    catIds = coco.getCatIds(catNms=className) # Récupération des identifiants des catégories à sélectionner
    imgIds = coco.getImgIds(catIds=catIds)    # Récupération des images avec les catégories d'objets précisées
    images +=coco.loadImgs(imgIds)      # Récupération des images avec les catégories d'objets précisées
    nb_images=len(imgIds) # Nombre d'images avec les catégories d'objets précisées
    
    print(nb_images, "images sélectionnées avec le critère ", className, " \n")

print(len(images),"images ont été sélectionnées avec tous les critères")

unique_images = []


doss_destination=os.path.join(dataDir, 'personalCOCOtest/vehicule')
doss_depart=os.path.join(dataDir, 'images/val2017')
for im in images:
    annIds = coco.getAnnIds(imgIds=im['id'], iscrowd=None)
    anns = coco.loadAnns(ids=annIds)
    max=anns[0]
    for a in anns:
       # print("la catégorie numéro", a['category_id']," a pour aire", a['area'])
        if a['area'] > max['area']:
            max=a # annotations de la catégorie prépondérante dans l'image
    if im not in unique_images and max['category_id'] in touteslescatIds :
        unique_images.append(im)
        cheminImageSource = os.path.join(doss_depart, im['file_name'])
        #print("enregistre : ",im['file_name'])
        shutil.copy(cheminImageSource,doss_destination)

print(len(unique_images), "images ont été enregistrées sans doublon")