from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and columns
model = joblib.load('churn_model.pkl')
columns = joblib.load('churn_columns.pkl')

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    # Convert numbers
    data['tenure'] = int(data['tenure'])
    data['MonthlyCharges'] = float(data['MonthlyCharges'])
    data['TotalCharges'] = float(data['TotalCharges'])

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    result = model.predict(df)[0]
    prediction = "⚠️ Likely to churn" if result == 1 else "✅ Not likely to churn"

    return render_template('form.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
