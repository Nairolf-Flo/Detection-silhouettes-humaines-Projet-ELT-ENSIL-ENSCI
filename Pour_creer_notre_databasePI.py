# coding: utf-8
from pycocotools.coco import COCO
from PIL import Image
import os
#import shutil

# Création de l'environemebt de la base d'images
repertoire_Train = os.path.join('personalCocoPI', 'train')
repertoire_Val = os.path.join('personalCocoPI', 'val')
repertoire_Humain_Train = os.path.join(repertoire_Train, 'humain')
repertoire_Non_Humain_Train = os.path.join(repertoire_Train, 'nonhumain')
repertoire_Humain_Val = os.path.join(repertoire_Val, 'humain')
repertoire_Non_Humain_Val = os.path.join(repertoire_Val, 'nonhumain')

os.mkdir('personalCocoPI')
os.mkdir(repertoire_Train)
os.mkdir(repertoire_Val)
os.mkdir(repertoire_Humain_Train)
os.mkdir(repertoire_Non_Humain_Train)
os.mkdir(repertoire_Humain_Val)
os.mkdir(repertoire_Non_Humain_Val)



dataDir=os.getcwd() # Chemin du dossier ou s'execute le script
categories_Humain = ['person']
#categories_Non_Humain = ['car']
categories_Non_Humain = [""]



# Fonction pour extraires les images intéressantes de coco
def exctraction(cate_selectionne,doss_depart,doss_destination):
    images = []
    for className in cate_selectionne:   # Il est peut être possible de se passer de la boucle
        catIds = coco.getCatIds(catNms=className) # Récupération des identifiants des catégories à sélectionner
        for classId in catIds:
            imgIds = coco.getImgIds(catIds=classId)    # Récupération des images avec les catégories d'objets précisées
            images += coco.loadImgs(imgIds)           # Récupération des images avec les catégories d'objets précisées
            nb_images=len(imgIds) # Nombre d'images avec les catégories d'objets précisées
            print(nb_images, "images sélectionnées avec le critère ", classId, " \n")
    
        print(len(images),"images ont été sélectionnées avec tous les critères")
        print("Vérification des images")
        unique_images = []
        
        if cate_selectionne != ['person']:
            p=0
            for im in images:
                annIds = coco.getAnnIds(imgIds=im['id'],iscrowd=None)
                anns = coco.loadAnns(ids=annIds)
                
                humain_is_present = 0
                for ann in anns:
                    if ann['category_id'] == 1:
                        humain_is_present=1
                
                if im not in unique_images and humain_is_present == 0 :
                    unique_images.append(im)
                    cheminImageSource = os.path.join(doss_depart, im['file_name'])
                    img = Image.open(cheminImageSource)
                    img.save(doss_destination + im['file_name']) # Enregistre uniquement l'objet d'intéret de la photo
                        
    
        elif cate_selectionne == ['person']:
            for im in images:
                annIds = coco.getAnnIds(imgIds=im['id'], iscrowd=None)
                anns = coco.loadAnns(ids=annIds)
                
                if im not in unique_images  : # Si pas de personnes sur l'image
                    unique_images.append(im)
                    cheminImageSource = os.path.join(doss_depart, im['file_name'])
                    img = Image.open(cheminImageSource)
                    img.save(doss_destination + im['file_name']) # Enregistre uniquement l'objet d'intéret de la photo
                    
        
        
        
        print(len(unique_images), "images intéressantes enregistrées sans doublon")
            
        # Remplir les répertoires avec les images
for i in range(4):
    if i==0:
        dataType = 'val2017'  # Dossier contenant les images
        annFile  = '{}/annotations/instances_{}.json'.format(dataDir,dataType)
        coco=COCO(annFile)     # initialize COCO api for instance annotations
        cate_selectionne = categories_Humain                         # Choisir ici la catégorie parmis categories_Humain / categories_Non_Humain
        doss_depart      = os.path.join(dataDir, 'images/val2017') # Choisir ici la source des images
        doss_destination = os.path.join(repertoire_Humain_Val, 'humain') # Choisir ici le dossier de destination des images
        exctraction(cate_selectionne,doss_depart,doss_destination)
    elif i==1:
        dataType = 'val2017'  # Dossier contenant les images
        annFile  = '{}/annotations/instances_{}.json'.format(dataDir,dataType)
        coco=COCO(annFile)      # initialize COCO api for instance annotations
        cate_selectionne = categories_Non_Humain                     # Choisir ici la catégorie parmis categories_Humain / categories_Non_Humain
        doss_depart      = os.path.join(dataDir, 'images/val2017') # Choisir ici la source des images
        doss_destination = os.path.join(repertoire_Non_Humain_Val, 'nonhumain') # Choisir ici le dossier de destination des images
        exctraction(cate_selectionne,doss_depart,doss_destination)
 