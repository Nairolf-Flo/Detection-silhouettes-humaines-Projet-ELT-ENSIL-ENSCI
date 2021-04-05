#source : https://thinkmobile.dev/testing-tensorflow-lite-image-classification-model/
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2
#import tflite_runtime.interpreter as tflite

interpreter = tf.lite.Interpreter(model_path="pretrainedmodel_PI0.tflite")
#interpreter = tflite.Interpreter(model_path="pretrainedmodel.tflite")

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
input_shape = input_details[0]['shape']
_, height, width, _ = input_shape  #taille des images acceptées
output_details = interpreter.get_output_details()

dataDir=os.getcwd() # Chemin du dossier ou s'execute le script

###--------------------------------------- TEST
# repertoire_Humain_Val = os.path.join(dataDir, 'personalCocoPI','val','nonhumain')
# repertoire_Humain_Val_Windows = os.path.join(dataDir, 'personalCocoPI','val','humain')
# image_test = "humain000000001584.jpg"

# im = np.array(Image.open(os.path.join(repertoire_Humain_Val_Windows,image_test)),dtype=np.float32)
# img = im[np.newaxis,:]
# img = np.resize(img,input_shape)

# interpreter.set_tensor(input_details[0]['index'], img) #tensor d'entrée
# interpreter.invoke()
# output_data = interpreter.get_tensor(output_details[0]['index'])
# print(output_data)
###--------------------------------------FIN TEST

taux_de_reussite = [0.0,0.0]
b=0
r=0
nb_reussite_total=0
longueur_total=0
for c in ['humain','nonhumain']:
    repertoire_Val_cat = os.path.join(dataDir, 'personalCocoPI','val', c )
    toutes_les_images = os.listdir(repertoire_Val_cat)
    longueur =len(toutes_les_images)
    longueur_total=longueur_total+longueur
    nb_reussite=0
   
    
    for image in toutes_les_images: # parcourt les noms des images du repertoire
        r+=1
        im = np.asarray(Image.open(os.path.join(repertoire_Val_cat,image)),dtype=np.float32)
        im=im/255
        im=cv2.resize(im,dsize=(96,96))
        img = im[np.newaxis,:]
        if img.shape == (1,96,96,3):
            b+=1
        
            #img = np.resize(img,input_shape)
            
            interpreter.set_tensor(input_details[0]['index'], img) #tensor d'entrée
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index']) #calcul de la sortie
            
            resultat=list(np.resize(output_data,(2)))
            if resultat.index(max(resultat)) == ['humain','nonhumain'].index(c) : #si la décision du reseau est égale à la catégorie correspondante
                nb_reussite+=1
                nb_reussite_total+=1
        else:
            longueur-=1
            longueur_total-=1
                
    taux_de_reussite[['humain','nonhumain'].index(c)] = nb_reussite / longueur # taux de réussite de la bonne catégorie
    
    
print('taux de réussite par classe = ',taux_de_reussite,' et taux de réussite global = ',
      nb_reussite_total/longueur_total)
        
    