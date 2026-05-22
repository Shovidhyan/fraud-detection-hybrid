def review_transaction(state):

    return {
        "final_action": """
Transaction FLAGGED FOR REVIEW

Reason:
- Suspicious activity detected

Action Taken:
- Sent to fraud investigation team
- Awaiting manual verification
"""
    }