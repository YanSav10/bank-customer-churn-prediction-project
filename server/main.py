from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Initialize the scaler directly on the input
scaler = StandardScaler()
sample_data = pd.DataFrame({
    'credit_score': [650, 600, 700, 750],
    'age': [40, 35, 60, 45],
    'balance': [12000, 15000, 10000, 20000],
    'estimated_salary': [50000, 55000, 60000, 45000]
})
scaler.fit(sample_data)

model = joblib.load('bank_customer_churn_prediction.pickle')

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    # Collect form data and create DataFrame
    input_data = {
        'credit_score': float(data['credit_score']),
        'age': float(data['age']),
        'tenure': int(data['tenure']),
        'balance': float(data['balance']),
        'products_number': int(data['products_number']),
        'credit_card': int(data['credit_card']),
        'active_member': int(data['active_member']),
        'estimated_salary': float(data['estimated_salary']),
        'country_Germany': 1 if data['country'] == 'Germany' else 0,
        'country_Spain': 1 if data['country'] == 'Spain' else 0,
        'gender_Male': 1 if data['gender'] == 'Male' else 0,
    }

    # Make sure the column order matches the training data
    input_df = pd.DataFrame([input_data])
    input_df = input_df[['credit_score', 'age', 'tenure', 'balance', 'products_number', 'credit_card',
                         'active_member', 'estimated_salary', 'country_Germany', 'country_Spain', 'gender_Male']]

    # Scale the numerical features
    numeric_features = ['credit_score', 'age', 'balance', 'estimated_salary']
    input_df[numeric_features] = scaler.transform(input_df[numeric_features])

    # Make the prediction
    prediction = model.predict(input_df)
    prediction_text = "Churn" if prediction[0] == 1 else "No Churn"

    return render_template('index.html', prediction=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
