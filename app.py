import pickle
from fastapi import FastAPI
from schema import LoanApplication

app = FastAPI()

with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.post("/predict")
def predict(data: LoanApplication):

    features = [[
        data.no_of_dependents,
        data.education,
        data.self_employed,
        data.income_annum,
        data.loan_amount,
        data.loan_term,
        data.cibil_score,
        data.residential_assets_value,
        data.commercial_assets_value,
        data.luxury_assets_value,
        data.bank_asset_value
    ]]

    prediction = model.predict(features)

    return {
        "prediction": int(prediction[0])
    }