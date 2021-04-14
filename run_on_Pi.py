#source : https://thinkmobile.dev/testing-tensorflow-lite-image-classification-model/
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2

#import tflite_runtime.interpreter as tflite



def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image


def classify_image(interpreter, image, top_k=1):
  """Returns a sorted array of classification results."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output =interpreter.get_tensor(output_details['index'])
  return output


interpreter = tf.lite.Interpreter(model_path="pretrainedmodel_avril_30epochs.tflite")
#interpreter = tflite.Interpreter(model_path="pretrainedmodel.tflite")

dataDir=os.getcwd() # Chemin du dossier ou s'execute le script
interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']

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
        im = Image.open(os.path.join(repertoire_Val_cat,image)).convert('RGB').resize((width, height),
                                                         Image.BILINEAR)
        resultat = classify_image(interpreter, im)
        resultat=list(np.resize(resultat,(2)))
        if resultat.index(max(resultat)) == ['humain','nonhumain'].index(c) : #si la décision du reseau est égale à la catégorie correspondante
            nb_reussite+=1
            nb_reussite_total+=1
            
    taux_de_reussite[['humain','nonhumain'].index(c)] = nb_reussite / longueur # taux de réussite de la bonne catégorie
    
    
print('taux de réussite par classe = ',taux_de_reussite,' et taux de réussite global = ',
      nb_reussite_total/longueur_total)
        
        