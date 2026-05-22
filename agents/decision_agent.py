def make_decision(fraud_result):

    label = fraud_result["label"]
    score = fraud_result["score"]

    if label == "fraud" and score > 0.8:
        return "BLOCK TRANSACTION"

    elif label == "suspicious" and score > 0.7:
        return "FLAG FOR MANUAL REVIEW"

    else:
        return "ALLOW TRANSACTION"