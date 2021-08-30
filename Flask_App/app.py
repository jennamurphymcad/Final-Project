from sqlalchemy import create_engine
from flask import Flask, render_template, jsonify
# import get_data
from flask import Flask,request, url_for, redirect, render_template, jsonify
# from pycaret.regression import *
import pandas as pd
# import pickle
import numpy as np

# Flask Setup
app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/data")
def data():

    return render_template("data.html")
   
@app.route("/comparisons")
def comparisons():
    return render_template("comparisons.html")


@app.route('/comparisons', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    print(variable)
    # return variable
# @app.route('/predict',methods=['POST'])
# def predict():

# #     # print(int_features)
# #     # final = np.array(int_features)
#     return render_template('comparisons.html')

#     # data_unseen = pd.DataFrame([final], columns = cols)
#     # prediction = predict_model(model, data=data_unseen, round = 0)
#     # prediction = int(prediction.Label[0])

if __name__ == '__main__':
    app.run(debug=True)