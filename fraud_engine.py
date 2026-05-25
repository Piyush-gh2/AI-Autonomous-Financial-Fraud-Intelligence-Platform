def detect_fraud(amount, frequency, location):

    if amount > 10000 and frequency > 10:
        return "High Fraud Risk"

    elif location == "High":
        return "Geographic Fraud Warning"

    else:
        return "Low Financial Risk"