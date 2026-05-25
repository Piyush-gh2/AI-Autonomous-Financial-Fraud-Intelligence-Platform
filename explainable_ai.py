def explain_risk(amount, frequency):

    if amount > 10000:
        return "Fraud alert generated due to unusually high transaction amount."

    elif frequency > 10:
        return "Fraud alert generated due to abnormal transaction frequency."

    else:
        return "Transaction behavior appears operationally stable."