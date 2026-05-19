def decide(analyzer_result, flags):
    prediction = analyzer_result["prediction"]
    confidence = analyzer_result["confidence"]

    if prediction == "fraudulent transaction" and confidence > 0.7:
        return "BLOCK"

    if confidence < 0.6 and len(flags) >= 2:
        return "BLOCK"

    if len(flags) > 0:
        return "SUSPICIOUS"

    return "ALLOW"