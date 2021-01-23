from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing import image
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as pltimage

mobile = MobileNetV2()
#model.summary() # Affiche la structure du réseau dans la console

def prepare_image(file):
    #img_path = 'images/'                                         # Localisation de l'image
    img = image.load_img(img_path + file, target_size=(224, 224)) # Redimensionne l'image pour le réseau 
    img_array = image.img_to_array(img)                           # Convertion de l'image en tableau
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)   # Augmente de 1 la dimension de l'image
    return preprocess_input(img_array_expanded_dims)


image_titre = 'imtest4.jpg'
img_path = 'images/'
preprocessed_image = prepare_image(image_titre)
predictions = mobile.predict(preprocessed_image)
results = imagenet_utils.decode_predictions(predictions)
print(results)

##-Affiche l'image analysée-##
image = pltimage.imread(img_path + image_titre)
plt.imshow(image)
plt.show()
##--------------------------##