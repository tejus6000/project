from flask import Flask,render_template, request
import pandas as pd
from flask_cors import CORS,cross_origin

app = Flask(__name__)

df = pd.read_csv("pred.csv")

df.to_csv("pred.csv", index=False)

@app.route('/',methods=['GET'])
 # type: ignore@cross_origin
def csvtohtml():
    
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
 # type: ignore@cross_origin
def homepage():
    if request.method == 'POST':
        
        data = pd.read_csv("pred.csv")

        return render_template("results.html",tables=[data.to_html()], titles=[''])
    
    else:   
        return render_template("index.html")


if __name__ == "__main__":
   # app.run(host="0.0.0.0",port=int(5000))
   app.run(debug=True)