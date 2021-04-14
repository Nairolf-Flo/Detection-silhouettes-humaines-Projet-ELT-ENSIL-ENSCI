
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import io
import time
import numpy as np
import picamera

from PIL import Image
from tflite_runtime.interpreter import Interpreter


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

def main():

    interpreter = Interpreter(model_path="pretrainedmodel_avril_30epochs.tflite")
    interpreter.allocate_tensors()
    _, height, width, _ = interpreter.get_input_details()[0]['shape']
    labels=['humain','nonhumain']
    with picamera.PiCamera(resolution=(640, 480), framerate=30) as camera:
      camera.start_preview()
      try:
        stream = io.BytesIO()
        for _ in camera.capture_continuous(
            stream, format='jpeg', use_video_port=True):
          stream.seek(0)
          image = Image.open(stream).convert('RGB').resize((width, height),
                                                           Image.BILINEAR)
          start_time = time.time()
          resultat = classify_image(interpreter, image)
          results=list(np.resize(resultat,(2)))
          elapsed_ms = (time.time() - start_time) * 1000
          label_id=results.index(max(results))
          prob = results[label_id]
          stream.seek(0)
          stream.truncate()
          camera.annotate_text = '%s %.2f\n%.1fms' % (labels[label_id], prob,
                                                      elapsed_ms)
          print(labels[label_id],prob,elapsed_ms)
      finally:
        camera.stop_preview()


if __name__ == '__main__':
  main()
