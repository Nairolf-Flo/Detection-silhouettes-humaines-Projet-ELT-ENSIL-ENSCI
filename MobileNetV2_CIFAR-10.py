from tensorflow.keras.applications import mobilenet_v2
from tensorflow import keras
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers



(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
num_classes = 10



# Pour voir les images :
for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(x_train[i].astype("uint8"))
    plt.title(y_train[i])
    plt.axis("off")
 
#transformation des vecteurs résultats en scalaires
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


input_shape = (32, 32, 3)
batch_size = 64
target_size = 96

#création d'un générateur
datagen=keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2)

train_generator=datagen.flow(x_train,y_train,subset='training')


def build_model( ):
    #input_tensor=layers.experimental.preprocessing.Resizing(height=96,width=96) ##faut il redimensionner ici ? ça marche ?
    input_tensor = layers.Input(shape=(target_size, target_size ,3))
    base_model = tf.keras.applications.MobileNetV2(
        include_top=False,
        weights='imagenet',
        input_tensor=input_tensor,
        input_shape=(target_size, target_size, 3),
        pooling='avg')

    for layer in base_model.layers:
        layer.trainable = False  # trainable has to be false in order to freeze the layers
        
    op = layers.Dense(256, activation='relu')(base_model.output)
    op = layers.Dropout(.25)(op)
    output_tensor = layers.Dense(10, activation='softmax')(op)

    model = keras.models.Model(inputs=input_tensor, outputs=output_tensor)


    return model

model=build_model()    
model.compile(
        optimizer=keras.optimizers.Adam(), loss="categorical_crossentropy", metrics=["accuracy"]
    )
 
epochs = 10

hist=model.fit(train_generator,epochs=epochs,verbose=2)

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['loss'])

#Sauvegarder le modèle
model_name='mobilenetv2_cifar'
tf.saved_model.save(model,'saved_models/'+ model_name)


#test de l'image numéro :
num=5 
from skimage.transform import resize
x = resize(x_train[num], (target_size, target_size,3))
x_expanded = np.expand_dims(x, axis=0)
predictions = model.predict(x_expanded)
print(predictions*100) #améliorer l'affichage des résultats

#Prédictions sur les images test
test_generator=datagen.flow(x_test,y_test)
model.evaluate(test_generator,verbose=2)