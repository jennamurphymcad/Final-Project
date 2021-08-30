from sqlalchemy import create_engine
from flask import Flask, render_template, jsonify
# import get_data


# Database Setup
# engine = create_engine("sqlite:///MNPDUseofForce.sqlite")
# get_data.get_data()

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

if __name__ == '__main__':
    app.run(debug=True)