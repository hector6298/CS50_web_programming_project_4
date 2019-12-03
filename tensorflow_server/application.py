from flask import Flask, request, jsonify
from neuralNetModel import MyModel
import dataset_creator
import numpy as np

app = Flask(__name__)

diagnostics = {
    0 : 'melanoma',
    1 : 'Atypical novu',
    2 : 'Common Novu'
}

model = MyModel()
   
@app.route('/')
def index():
    if model is not None:
        print('Successfully loaded model.')
    else:
        raise Exception("Model could not be loaded. Aborting ..")

    try:
        model.load_weights('./checkpoints/checkpoint')
        print("weights were successfully loaded onto model.")
    except:
        raise Exception("weights could no be loaded")
    return "done"

@app.route('/predict', methods=['POST'])
def prediction():
    content = request.json
    image = np.array(content['image'])
    image = np.reshape(image, [-1,100,100,3])

    prediction = model(image)
    return jsonify({'diagnostic' : diagnostics[np.argmax(prediction)]})


    