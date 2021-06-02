import numpy as np

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD

import matplotlib as mpl
from matplotlib import pyplot

num_classes = 10          # Nombre de classes
input_shape = (28, 28, 1) # Dimensions de l'image d'entrée du réseau

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data() # Charge les images de la bdd MNIST

## Afficher un chiffre de bdd MNIST ##
# mpl.pyplot.imshow(train_images[0],cmap=pyplot.get_cmap('Oranges'))
# mpl.pyplot.show()
##----------------------------------##


train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

model = Sequential([
  Conv2D(8, 3, input_shape=(28, 28, 1), use_bias=False),
  MaxPooling2D(pool_size=2),
  Flatten(),
  Dense(10, activation='softmax'),
])

model.compile(SGD(lr=.005), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
  train_images,
  to_categorical(train_labels),
  batch_size=1,
  epochs=3,
  validation_data=(test_images, to_categorical(test_labels)),
)
