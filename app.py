from flask import Flask, request, render_template
import cv2
import numpy as np

app = Flask(__name__)

# Load YOLOv3 model with pre-trained weights and configuration file
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# Get the names of the output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Define classes
classes = ['cat', 'dog', 'bird']

@app.route('/', methods=['GET', 'POST'])

def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))
    return render_template('index.html', result=False)

if __name__ == '__main__':
    app.run(debug=True)



# def index(): 
#     if request.method == 'POST':
#         # Get uploaded image file
#         file = request.files['image']

#         # Read image file and resize it
#         img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
#         img = cv2.resize(img, None, fx=0.4, fy=0.4)

#         # Detect objects in the image
#         blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(416,416), mean=(0,0,0), swapRB=True, crop=False)
#         net.setInput(blob)
#         outs = net.forward(output_layers)

#         # Get bounding boxes and class labels for the detected objects
#         class_ids = []
#         confidences = []
#         boxes = []
#         for out in outs:
#             for detection in out:
#                 scores = detection[5:]
#                 class_id = np.argmax(scores)
#                 confidence = scores[class_id]
#                 if confidence > 0.5:
#                     center_x = int(detection[0] * img.shape[1])
#                     center_y = int(detection[1] * img.shape[0])
#                     w = int(detection[2] * img.shape[1])
#                     h = int(detection[3] * img.shape[0])
#                     x = int(center_x - w / 2)
#                     y = int(center_y - h / 2)
#                     boxes.append([x, y, w, h])
#                     confidences.append(float(confidence))
#                     class_ids.append(class_id)

#         # Apply non-maximum suppression to remove redundant bounding boxes
#         indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#         # Draw bounding boxes and class labels on the image
#         colors = np.random.uniform(0, 255, size=(len(classes), 3))
#         for i in indices:
#             i = i[0]
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             color = colors[class_ids[i]]
#             cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)
#             cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#         # Save image with bounding boxes and class labels
#         cv2.imwrite('static/result.jpg', img)

#         return render_template('index.html', result=True)