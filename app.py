from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load dataset (ensure df is loaded properly)
df = pd.read_csv("C:/Users/Vvish/Videos/movies/java/diabetes.csv")  # Replace with actual dataset path
y = df['Outcome']
x = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 
        'BMI', 'DiabetesPedigreeFunction', 'Age']]

# Train model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=43)
model = LogisticRegression()
model.fit(x_train, y_train)

# Flask Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])

        # Prediction
        input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        prediction = model.predict(input_data)[0]

        # Result message
        result = "You have diabetes." if prediction == 1 else "You do not have diabetes."
        return render_template('result.html', result=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
