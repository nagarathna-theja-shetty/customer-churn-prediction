# Customer Churn Prediction Web App

This project predicts whether a telecom customer is likely to churn using a Logistic Regression model trained on key customer data like tenure, monthly charges, contract type, etc.

🔗 **Live Demo:** [https://nagarathnatshetty.pythonanywhere.com](https://nagarathnatshetty.pythonanywhere.com)

---

## 💡 About the Project

- 🎯 **Objective:** Help telecom businesses predict which customers are likely to leave (churn) so they can take action to retain them.
- 🛠️ **Tools Used:** Python, Pandas, Logistic Regression, Flask, HTML/CSS
- 🧠 **ML Model:** Trained with balanced data and evaluated using confusion matrix and classification metrics
- 🌐 **Deployment:** PythonAnywhere (Free Flask hosting)

---

## 📂 Project Structure

```
churnapp/
├── app.py                 # Flask app to handle user input and serve predictions
├── churn_model.pkl        # Trained logistic regression model saved using pickle
├── churn_columns.pkl      # Column list used to align user inputs for prediction
└── templates/
    └── form.html          # Frontend HTML form to collect customer data
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/customer-churn-prediction

# 2. Move into the project folder
cd churnapp

# 3. Install dependencies
pip install flask pandas scikit-learn

# 4. Run the Flask app
python app.py
```

Then open your browser and go to `http://127.0.0.1:5000`

---

## 📈 Sample Output

- The user enters customer information through a web form.
- On clicking **Predict**, the model returns either:
  - `Likely to churn`
  - `Not likely to churn`

---

## 🙋‍♀️ Author

**Nagarathna T Shetty**  
Aspiring Data Scientist| BCA Graduate  
🔗 [Live Web App](https://nagarathnatshetty.pythonanywhere.com)  

---
