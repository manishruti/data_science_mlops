from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET']) ## route to display the home page
def homepage():
    return render_template('index.html')

@app.route('/train', methods=['GET']) # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!"

@app.route('/predict', methods=['POST']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            account_Balance = float(request.form['Account_Balance'])
            duration_of_credit = float(request.form['Duration_of_Credit'])
            payment_status_of_previous_credit = float(request.form['Payment_Status_of_Previous_Credit'])
            purpose = request.form['Purpose']
            credit_amount = float(request.form['Credit_Amount'])
            value_saving_stocks = float(request.form['Value_Savings_Stocks'])
            length_of_current_employment = float(request.form['Length_of_current_employment'])
            instalment_per_cent = float(request.form['Instalment_per_cent'])
            sex_marital_status = float(request.form['Sex_Marital_Status'])
            guarantors = float(request.form['Guarantors'])
            present_residence_since = float(request.form['Duration_in_Current_address'])
            most_valuable_available_asset = float(request.form['Most_valuable_available_asset'])
            age = float(request.form['Age'])
            concurrent_credits = float(request.form['Concurrent_Credits'])
            type_of_apartment = float(request.form['Type_of_apartment'])
            no_of_credits_at_this_bank = float(request.form['No_of_Credits_at_this_Bank'])
            occupation_type = float(request.form['Occupation'])
            no_of_dependents = float(request.form['No_of_dependents'])
            telephone = float(request.form['Telephone'])
            foreign_worker = float(request.form['Foreign_Worker'])

            data = [account_Balance, duration_of_credit, payment_status_of_previous_credit, purpose, 
                    credit_amount, value_saving_stocks, length_of_current_employment, instalment_per_cent,
                    sex_marital_status,guarantors, present_residence_since, most_valuable_available_asset, age,
                    concurrent_credits, type_of_apartment, no_of_credits_at_this_bank, occupation_type,
                    no_of_dependents, telephone, foreign_worker
                    ]
            data = np.array(data, dtype=np.float64).reshape(1, len(data))

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', predictions=str(predict))
        except Exception as e:
            print('The Exception message is: ', e)
            return f"something is wrong:{e}"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)







