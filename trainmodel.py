import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

# Load and prepare the input image
img_path = './data/goat.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make predictions on the input image
preds = model.predict(x)

# Decode the predictions into a human-readable format
decoded_preds = decode_predictions(preds, top=3)[0]

# Print the top predicted object classes and their probabilities
for pred in decoded_preds:
    print(pred[1], pred[2])
