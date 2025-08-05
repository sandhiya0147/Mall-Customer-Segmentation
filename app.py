from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model_data = pickle.load(open("model.pkl", "rb"))
scaler = model_data['scaler']
kmeans = model_data['kmeans']
features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

@app.route('/')
def home():
    return render_template("home.html", features=features)

@app.route('/predict', methods=['POST'])
def predict():
    vals = {f: float(request.form[f]) for f in features}
    df = pd.DataFrame([vals])
    scaled = scaler.transform(df)
    cluster = int(kmeans.predict(scaled)[0])
    return render_template("result.html", cluster=cluster)

if __name__ == "__main__":
    app.run(debug=True)
