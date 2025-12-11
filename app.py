from flask import Flask, render_template, request
import pickle

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data=[
        float(request.form["experience"]),
        float(request.form["skill"]),
        float(request.form["age"])
    ]
    pred=model.predict([data])[0]
    return render_template("result.html", prediction=round(pred,2))

app.run(debug=True)
