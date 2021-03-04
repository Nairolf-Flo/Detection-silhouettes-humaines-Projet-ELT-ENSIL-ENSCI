from pycocotools.coco import COCO
import matplotlib.pyplot as plt
from PIL import Image
import os
#import shutil

dataDir=os.getcwd() # Chemin du dossier ou s'execute le script
dataType='val2017'  # Dossier contenant les images
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)


coco=COCO(annFile) # initialize COCO api for instance annotations

categoriesVehicules = ['car','bus']
categoriesPerson = ['person']
categoriesAnimals = ['cat','dog','sheep','cow','horse']
cattest = ['dog']

cate_selectionne = cattest # Choisir ici la catégorie parmis categoriesVehicules / categoriesPerson / categoriesAnimals
doss_depart=os.path.join(dataDir, 'images/val2017')                  # Choisir ici la source des images
doss_destination=os.path.join(dataDir, 'personalCOCOtest/vehicule/') # Choisir ici le dossier de destination des images


images = []
touteslescatIds=coco.getCatIds(catNms=cate_selectionne)
for className in cate_selectionne:   # Il est peut être possible de se passer de la boucle
    catIds = coco.getCatIds(catNms=className) # Récupération des identifiants des catégories à sélectionner
    imgIds = coco.getImgIds(catIds=catIds)    # Récupération des images avec les catégories d'objets précisées
    images += coco.loadImgs(imgIds)           # Récupération des images avec les catégories d'objets précisées
    nb_images=len(imgIds) # Nombre d'images avec les catégories d'objets précisées
    
    print(nb_images, "images sélectionnées avec le critère ", className, " \n")

print(len(images),"images ont été sélectionnées avec tous les critères")
print("Vérification des images")
unique_images = []


for im in images:
    annIds = coco.getAnnIds(imgIds=im['id'], iscrowd=None)
    anns = coco.loadAnns(ids=annIds)
    max=anns[0]
    for a in anns: # Selectionne l'objet qui occupe le plus de place dans la photo
        #print("la catégorie numéro", a['category_id']," a pour aire", a['area'])
        if a['area'] > max['area']:
            max=a # annotations de la catégorie prépondérante dans l'image
    if im not in unique_images and max['category_id'] in touteslescatIds :
        unique_images.append(im)
        cheminImageSource = os.path.join(doss_depart, im['file_name'])
        #shutil.copy(cheminImageSource,doss_destination) # Enregistre la photo en entier
        img = Image.open(cheminImageSource)
        img_box = img.crop((max['bbox'][0],max['bbox'][1],max['bbox'][0]+max['bbox'][2],max['bbox'][1]+max['bbox'][3]))
        img_box.save(doss_destination + im['file_name']) # Enregistre uniquement l'objet d'intéret de la photo
        #print(doss_destination + im['file_name'])

print(len(unique_images), "images intéressantes enregistrées sans doublon")