import pickle
import json
from flask import Flask, request, app, jsonify, url_for, render_template

import numpy as np
import pandas as pd



app = Flask(__name__)

regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar=pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(list(data.values())[0])
    data_modified = np.array(list(data.values())).reshape(1,-1)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(data_modified)
    output=regmodel.predict(new_data)
    print(output)
    return jsonify(output[0])

@app.route('/predict_file', methods=["POST"])
def predict_house_prices():
    df_test=pd.read_csv(request.files.get("file"))
    predictions = regmodel.predict(df_test)
    return "The predicted house prices are" + str(list(prediction))


@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    print(data)
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text="The house price prediction is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)