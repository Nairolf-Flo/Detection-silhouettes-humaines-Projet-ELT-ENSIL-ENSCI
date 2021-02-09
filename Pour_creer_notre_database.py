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
for className in cattest:
    catIds = coco.getCatIds(catNms=className) # Récupération des identifiants des catégories à sélectionner
    imgIds = coco.getImgIds(catIds=catIds)    # Récupération des images avec les catégories d'objets précisées
    images += coco.loadImgs(imgIds)[0]        # Récupération des images avec les catégories d'objets précisées
    nb_images=len(imgIds) # Nombre d'images avec les catégories d'objets précisées
    
    print(nb_images, "images sélectionnées avec le critère ", className, " \n")




unique_images = []

doss_destination=os.path.join(dataDir, 'personalCOCO/vehicule')
doss_depart=os.path.join(dataDir, 'val2017')
for im in images:
    type(im)
    annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
    anns = coco.loadAnns(annIds)
    max=anns[0]
    for a in anns:
        print("la catégorie numéro", a['category_id']," a pour aire", a['area'])
        if a['area'] > max['area']:
            max=a # annotations de la catégorie prépondérante dans l'image
            print("toc")
    if im not in unique_images and max['category_id'] in catIds :
        cheminImageSource = os.path.join(doss_depart, im['file_name'])
        print("enregistre : ",im['file_name'])
        #photo=plt.imread(filesname)
        #plt.imshow(photo)
        #shutil.copy(cheminImageSource,doss_destination)