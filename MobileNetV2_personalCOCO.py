from tensorflow.keras.applications import mobilenet_v2
from tensorflow import keras
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

CATEGORIES = ["animal" , "person" , "vehicle"]

dataDir=os.getcwd() # Chemin du dossier ou s'execute le script
dataDirCoco=dataDir + "personalCoco"

for category in CATEGORIES :
    path = os.path.join(dataDirCoco,category)
    
