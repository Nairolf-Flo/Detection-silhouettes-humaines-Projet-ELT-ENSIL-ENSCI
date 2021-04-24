# Detection-silhouettes-humaines-Projet-ELT-ENSIL-ENSCI
Grâce à de l’analyse d’images, cet outil pourra déclencher des services variés tel qu’une alarme de sécurité ou la gestion du chauffage d’un bâtiment. L’intérêt est économique et écologique puisque ces services destinés uniquement aux humains seront activés uniquement dans des situations pertinentes.

<center>
<img src="https://github.com/Nairolf-Flo/Detection-silhouettes-humaines-Projet-ELT-ENSIL-ENSCI/blob/main/dft_sf_feu.gif" alt="Banner">
</center>
Rien à voir mais c'est beau ! 😀

## Table des matières
* [Création de la base d'images pour l'entraînement](#base-images)
* [Transfert d'apprentissage](#transfert-apprentissage)
* [Utilisation du CNN](#utilisation-du-cnn)
* [Liens utiles](#liens-utiles)
* [Test de la détection en temps réel](#Test de la détection en temps réel sur le Raspberry PI)


## Base images

 - Le script "Pour_creer_notre_databasePI.py" permet d'enregistrer les images val2017
 - Le script "Pour_creer_notre_database.py" permet d'enregistrer les images val2017 + train2017

## Transfert apprentissage

 - Le script "TL_MobileNetV2_linux.py" effectue le transfert d'apprentissage
 - Le script "Convertir_en_TFlite.py" permet de créer un modèle à utiliser avec tflite 
 
## Utilisation du CNN

 - Le script "run_on_Pi.py" permet d'utiliser le modèle tflite
 
 ## Test de la détection en temps réel sur le Raspberry PI

 - Le script "PI_temps_reel.py" utilise un modèle tflite pour classer des images provenant de la caméra du Raspberry PI. Les résultats de la classification s'affichent dans la console et sur l'écran. 	
 
## Liens utiles

- Création de la base d'images pour l'entaînement
	- https://towardsdatascience.com/master-the-coco-dataset-for-semantic-image-segmentation-part-1-of-2-732712631047
	- https://cocodataset.org/#format-data

 - Transfet d'apprentissage
	- https://keras.io/guides/functional_api/
	- https://keras.io/guides/transfer_learning/
	- https://medium.com/hackernoon/tf-serving-keras-mobilenetv2-632b8d92983c
