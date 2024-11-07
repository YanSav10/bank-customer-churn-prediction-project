# Bank Customer Churn Prediction
### Description
This project predicts customer churn for a banking institution based on user data, leveraging historical data and various customer metrics. The model preprocesses the data, normalizes key features, and encodes categorical variables, producing a structured dataset for training. The model, hosted in a Flask web application, enables customer service teams to input customer data and receive a churn prediction in real-time.

### Model Performance
The trained model achieves solid predictive metrics, providing useful insights for targeting retention efforts:

- **Overall Accuracy**: 87%
- **Precision (Non-Churn)**: 88%
- **Recall (Non-Churn)**: 96%
- **F1-Score (Churn)**: 59%

These results reflect the model’s reliability in predicting non-churning customers and provide actionable insights for potential churn cases.

### Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YanSav10/bank-customer-churn-prediction-project
2. Navigate to the project directory:
   ```bash
   cd bank-customer-churn-prediction-project
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Flask server:
   ```bash
   python main.py
5. Or use Gunicorn:
    ```bash
   gunicorn -b :5000 main:app
### Usage
1. Open your browser and go to http://localhost:5000.
2. Enter customer details, including metrics such as credit score, tenure, balance, and more.
3. The app will output a prediction indicating if the customer is likely to churn or stay.
### Technology Stack
- **Python**: Data processing and model training
- **Machine Learning**: Model built using Scikit-learn
- **Flask**: Web framework for model deployment
- **HTML/CSS**: Front-end interface
