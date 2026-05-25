from src.loader import load_data
from src.forecasting import forecast_fraud_risk
from src.fraud_engine import detect_fraud
from src.explainable_ai import explain_risk

def run_fraud_ai():

    df = load_data()

    prediction = forecast_fraud_risk(df)

    latest_amount = df["amount"].iloc[-1]
    latest_frequency = df["frequency"].iloc[-1]
    latest_location = df["location_risk"].iloc[-1]

    risk = detect_fraud(
        latest_amount,
        latest_frequency,
        latest_location
    )

    explanation = explain_risk(
        latest_amount,
        latest_frequency
    )

    return df, prediction, risk, explanation