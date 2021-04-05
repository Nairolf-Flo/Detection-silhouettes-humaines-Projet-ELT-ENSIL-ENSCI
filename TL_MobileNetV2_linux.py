import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

target_size = 96
batchSize = 32

repertoire=os.getcwd() # Chemin du dossier ou s'execute le script
repertoireCoco=repertoire + "/personalCocoPI"

#Création des dataset
#https://keras.io/api/preprocessing/image/#image_dataset_from_directory-function
train_dataset=keras.preprocessing.image_dataset_from_directory(
    repertoireCoco + "/train",      # Répertoire des images # !
    labels="inferred",   # Label déduit du nom du répertoire des images
    label_mode="categorical", # 'binary' means that the labels (there can be only 2) are encoded as float32 scalars with values 0 or 1 (e.g. for binary_crossentropy)
    class_names=None,    # None donc l'ordre alphanumérique est utilisé pour ordonner les classes (mettre la liste des sous répertoires pour choisir l'ordre)
    color_mode="rgb",    # "grayscale", "rgb", "rgba" convertir les images si besoin
    batch_size=batchSize,       # Taille des batches, par défaut c'est 32
    image_size=(target_size, target_size), # Taille des images
    shuffle=True,        # Mélange les images
    seed=None,
    validation_split=None,    # Pas besoin ici on a déjà split nos images avec coco
    subset=None,              # Only used if validation_split is set
    interpolation="bilinear", # Méthode d'interpolation utilisée pour le redimensionnement des images. bilinear, nearest, bicubic, area, lanczos3, lanczos5, gaussian, mitchellcubic
    follow_links=False,
)

val_dataset=keras.preprocessing.image_dataset_from_directory(
    repertoireCoco + "/val", # !
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=batchSize,
    image_size=(target_size, target_size),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
)


# inputs = keras.Input(shape=(target_size, target_size, 3)) # !
# #inputs = keras.layers.Input(shape=(target_size, target_size ,3))

# #----------------------------------------------------------------------
# # Import le MobileNetV2 entrainé sur imagenet
# base_model = tf.keras.applications.MobileNetV2(
#     input_shape=(target_size, target_size,3),
#     alpha=1.0,
#     include_top=False,
#     weights='imagenet',
#     input_tensor=inputs, # !
#     pooling='max'
#     )

# # Bloque la modification du base_model
# base_model.trainable = False 
# # base_model :
# #     ----------------------
# #    | MobileNetV2 sans Top | 
# #     ----------------------
# #-----------------------------------------------------------------------
# # Ajout du classifieur à la fin du model
# x = base_model(inputs, training=False)
# #x = keras.layers.GlobalAveragePooling2D()(base_model.output) # calculates the average output of each feature map in the previous layer
# #x = keras.layers.Dense(256, activation='relu')(x)
# #x = keras.layers.Dropout(.25)(x)
# outputs = keras.layers.Dense(2,activation='softmax')(x)

# model = keras.Model(inputs=inputs, outputs=outputs)
# # model :
# #     ----------------------     ------------------------     -------
# #    | MobileNetV2 sans Top |---| GlobalAveragePooling2D |---| Dense |
# #     ----------------------     ------------------------     -------
# #-----------------------------------------------------------------------

# # Configuration du model pour l'entrainement
# model.compile(
#     optimizer = keras.optimizers.Adam(),
#     loss = "categorical_crossentropy", # Force le loss entre 0 et 1"""
#     metrics=["accuracy"]                  # Proportion d'images correctement identifiées
#     )
 
# # Entrainement du modèle
# history = model.fit(
#     train_dataset,
#     batch_size = batchSize, # par défaut 32
#     epochs=100,  # /!\
#     verbose = 2 # affiche des infos a la fin des epochs
#     )
    
# # Sauvegarder le modèle
# model_name='mobilenetv2_personalCocotest0'
# save_path=repertoire+'/saved_models/'+ model_name
# model.save(save_path)              #à décommenter pour sauvegarder le modèle (attention au nom)

# Rappeler le modèle :
model_name='mobilenetv2_personalCoco100epochs'
save_path=repertoire+'/saved_models/'+ model_name
model = keras.models.load_model(save_path)

# Tester le modèle sur les images de validation
model.evaluate(val_dataset,verbose=2)

