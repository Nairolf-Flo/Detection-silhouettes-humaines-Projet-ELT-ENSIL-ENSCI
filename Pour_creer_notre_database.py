from pycocotools.coco import COCO
import matplotlib.pyplot as plt
from PIL import Image
import os
#import shutil

# Création de l'environemebt de la base d'images
repertoire_Train = os.path.join('personalCoco', 'train')
repertoire_Val = os.path.join('personalCoco', 'val')
repertoire_Humain_Train = os.path.join(repertoire_Train, 'humain')
repertoire_Non_Humain_Train = os.path.join(repertoire_Train, 'nonhumain')
repertoire_Humain_Val = os.path.join(repertoire_Val, 'humain')
repertoire_Non_Humain_Val = os.path.join(repertoire_Val, 'nonhumain')

os.mkdir('personalCoco')
os.mkdir(repertoire_Train)
os.mkdir(repertoire_Val)
os.mkdir(repertoire_Humain_Train)
os.mkdir(repertoire_Non_Humain_Train)
os.mkdir(repertoire_Humain_Val)
os.mkdir(repertoire_Non_Humain_Val)



dataDir=os.getcwd() # Chemin du dossier ou s'execute le script
categories_Humain = ['person']
categories_Non_Humain = ['car']
#categories_Non_Humain = ['car','bus','cat','dog','sheep','cow','horse']



# Fonction pour extraires les images intéressantes de coco
def exctraction(cate_selectionne,doss_depart,doss_destination):
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


  
# Remplir les répertoires avec les images
for i in range(4):
    if i==0:
        dataType = 'train2017'  # Dossier contenant les images
        annFile  = '{}/annotations/instances_{}.json'.format(dataDir,dataType)
        coco=COCO(annFile)      # initialize COCO api for instance annotations
        cate_selectionne = categories_Humain                         # Choisir ici la catégorie parmis categories_Humain / categories_Non_Humain
        doss_depart      = os.path.join(dataDir, 'images/train2017') # Choisir ici la source des images
        doss_destination = os.path.join(repertoire_Humain_Train, 'humain') # Choisir ici le dossier de destination des images
        exctraction(cate_selectionne,doss_depart,doss_destination)
    elif i==1:
        dataType = 'train2017'  # Dossier contenant les images
        annFile  = '{}/annotations/instances_{}.json'.format(dataDir,dataType)
        coco=COCO(annFile)      # initialize COCO api for instance annotations
        cate_selectionne = categories_Non_Humain                     # Choisir ici la catégorie parmis categories_Humain / categories_Non_Humain
        doss_depart      = os.path.join(dataDir, 'images/train2017') # Choisir ici la source des images
        doss_destination = os.path.join(repertoire_Non_Humain_Train, 'nonhumain') # Choisir ici le dossier de destination des images
        exctraction(cate_selectionne,doss_depart,doss_destination)
    #if i==2:
    elif i==2:
        dataType = 'val2017'  # Dossier contenant les images
        annFile  = '{}/annotations/instances_{}.json'.format(dataDir,dataType)
        coco=COCO(annFile)      # initialize COCO api for instance annotations
        cate_selectionne = categories_Humain                       # Choisir ici la catégorie parmis categories_Humain / categories_Non_Humain
        doss_depart      = os.path.join(dataDir, 'images/val2017') # Choisir ici la source des images
        doss_destination = os.path.join(repertoire_Humain_Val, 'humain') # Choisir ici le dossier de destination des images
        exctraction(cate_selectionne,doss_depart,doss_destination)
    elif i==3:
        dataType = 'val2017'  # Dossier contenant les images
        annFile  = '{}/annotations/instances_{}.json'.format(dataDir,dataType)
        coco=COCO(annFile)      # initialize COCO api for instance annotations
        cate_selectionne = categories_Non_Humain                   # Choisir ici la catégorie parmis categories_Humain / categories_Non_Humain
        doss_depart      = os.path.join(dataDir, 'images/val2017') # Choisir ici la source des images
        doss_destination = os.path.join(repertoire_Non_Humain_Val, 'nonhumain') # Choisir ici le dossier de destination des images
        exctraction(cate_selectionne,doss_depart,doss_destination)