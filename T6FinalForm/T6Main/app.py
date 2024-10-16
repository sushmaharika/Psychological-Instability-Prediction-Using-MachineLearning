from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the encoder and model
ord_encoder = pickle.load(open('ord_encoder.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template('finalForm.html')

@app.route('/finalForm', methods=['POST'])
def predict():
    try:
        # Extract features from form
        features = [x for x in request.form.values()]
        print(features)
        # Assuming the first feature is numeric and others are categorical
        numeric_features = np.array([features[0]], dtype=float)
        categorical_features = np.array(features[1:]).reshape(1, -1)

        # Encode categorical features
        encoded_features = ord_encoder.transform(categorical_features)
        features = np.concatenate([numeric_features, encoded_features.ravel()])

        # Make prediction
        prediction = model.predict(features.reshape(1, -1))
        output = 'YOU NEED TREATMENT' if prediction[0] == 1 else 'NO NEED ANY TREATMENT'

        template = 'OutputYES.html' if prediction[0] == 1 else 'OutputNO.html'
        return render_template(template, prediction=output)
    except Exception as e:
        print(e)
        return "Error processing input data."

if __name__ == '__main__':
    app.run(debug=True)