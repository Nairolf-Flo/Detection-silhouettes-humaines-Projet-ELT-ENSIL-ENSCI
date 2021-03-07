import os
import tensorflow as tf
import pathlib
dataDir = os.getcwd()
converter = tf.lite.TFLiteConverter.from_saved_model(dataDir)
tflite_model = converter.convert()
tflite_model_files = pathlib.Path("pretrainedmodel.tflite")
tflite_model_files.write_bytes(tflite_model)