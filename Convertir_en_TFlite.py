import os
import tensorflow as tf
import pathlib
dataDir = os.getcwd()
converter = tf.lite.TFLiteConverter.from_saved_model(dataDir+"\\saved_models\\Model_du_Jeudi_8_Avril_30epochs")
tflite_model = converter.convert()
tflite_model_files = pathlib.Path("pretrainedmodel_avril_30epochs.tflite")
tflite_model_files.write_bytes(tflite_model)

# converter = tf.lite.TFLiteConverter.from_keras_model(model=model)
# tflite_model = converter.convert()
# # Save the model.
# with open('pretrainedmodel3.tflite', 'wb') as f:
#   f.write(tflite_model)