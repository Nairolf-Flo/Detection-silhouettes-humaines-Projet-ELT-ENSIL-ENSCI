#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
from tensorflow import keras
import pydot
target_size = 96


# In[2]:


CATEGORIES = ["animal" , "person" , "vehicle"]

dataDir=os.getcwd() # Chemin du dossier ou s'execute le script
dataDirCoco=dataDir + "\personalCoco"

for category in CATEGORIES :
    path = os.path.join(dataDirCoco,category)
    for img in os.listdir(path)[:3]:
        img_array=cv2.imread(os.path.join(path,img))
        img_resized= cv2.resize(img_array,(target_size,target_size))
        plt.imshow(img_array)
        plt.show()
        print(category)
        print(img_array.shape)
        
    


# In[4]:


target_size = 96

#création d'un générateur

train_generator=keras.preprocessing.image_dataset_from_directory(
    dataDirCoco,
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=64,
    image_size=(target_size, target_size),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
)

val_generator=keras.preprocessing.image_dataset_from_directory(
    dataDirCoco+"val",
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=64,
    image_size=(target_size, target_size),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
)


# In[5]:


def build_model( ):
    input_tensor = keras.layers.Input(shape=(target_size, target_size ,3))
    
    base_model = keras.applications.MobileNetV2(
        include_top=False,
        weights='imagenet',
        input_tensor=input_tensor,
        input_shape=(target_size, target_size, 3),
        pooling='avg')

    for layer in base_model.layers:
        layer.trainable = False  # Les poids sont figés
        
    op = keras.layers.Dense(256, activation='relu')(base_model.output)
    op = keras.layers.Dropout(.25)(op)
    output_tensor = keras.layers.Dense(3, activation='softmax')(op) # Indiquer le nombre de classe en sortie

    model = keras.models.Model(inputs=input_tensor, outputs=output_tensor) # Construction du modèle


    return model

model=build_model()    
model.compile(
        optimizer=keras.optimizers.Adam(), loss="categorical_crossentropy", metrics=["accuracy"]
    )


# In[10]:


#model.summary()
keras.utils.plot_model(model, show_shapes=True)


# In[6]:


epochs = 10

hist=model.fit(train_generator,epochs=epochs,verbose=2)


# In[7]:


plt.plot(hist.history['accuracy'])
plt.plot(hist.history['loss'])


# In[30]:


#Sauvegarder le modèle
model_name='mobilenetv2_personalCoco'
save_path=dataDir+'\saved_models\\'+ model_name
#model.save(save_path)              à décommenter pour sauvegarder le modèle (attention au nom)


# In[7]:


model.evaluate(val_generator,verbose=2)


# In[5]:


#rappeler le modèle :
model_name='mobilenetv2_personalCoco'
save_path=dataDir+'\saved_models\\'+ model_name
model = keras.models.load_model(save_path)


# In[ ]:




