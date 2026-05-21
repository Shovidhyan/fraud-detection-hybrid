from agents.fraud_detector import detect_fraud
from agents.risk_explainer import explain_risk

transaction = """
Large transaction from unknown location.
Multiple login attempts detected.
Using a new device.
"""

fraud_result = detect_fraud(transaction)

print("\nFRAUD DETECTION RESULT:\n")
print(fraud_result)

ai_analysis = explain_risk(fraud_result)

print("\nAI SECURITY ANALYSIS:\n")
print(ai_analysis)