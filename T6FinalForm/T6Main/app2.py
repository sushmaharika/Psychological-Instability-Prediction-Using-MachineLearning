from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
import pickle
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

model = pickle.load(open('model.pkl', 'rb'))
data = pd.read_csv("filtered.csv")

X = data[['age', 'gender', 'self_employed', 'family_history', 'work_interfere', 'no_employees',
        'remote_work', 'tech_company', 'benefits', 'care_options', 'wellness_program',
        'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 'phys_health_consequence',
        'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical',
        'obs_consequence']]

ord_encoder = OrdinalEncoder()
X = ord_encoder.fit_transform(X)

le = LabelEncoder()
y = data["treatment"]
y = le.fit_transform(y)

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/', methods=['GET', 'POST'])
def finalForm2():
    return render_template('finalForm.html')

@app.route('/finalForm', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    ready = ord_encoder.fit_transform([features])
    print(ready)
    prediction = model.predict(ready)
    if prediction[0] == 0:
        output = 'NO NEED ANY TREATMENT'
    else:
        output = 'YOU NEED TREATMENT'
    # return render_template('finalForm.html', prediction=output)
    if (output == 'YOU NEED TREATMENT'):
        return render_template('OutputYES.html', prediction=output)
    else:
        return render_template('OutputNO.html', prediction=output)


if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask, request, render_template
# from flask import Flask, render_template, request, redirect, url_for
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username == 'admin' and password == 'password':
#             return redirect(url_for('finalForm2'))
#         else:
#             return 'Invalid username or password. Please try again.'
#     return render_template('login.html')

# @app.route('/finalForm2')
# def finalForm2():
#     return render_template('finalForm.html')

# if __name__ == '__main__':
#     app.run(debug=True)









