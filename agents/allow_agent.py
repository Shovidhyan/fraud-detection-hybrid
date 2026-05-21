def allow_transaction(state):

    return {
        "final_action": """
Transaction APPROVED

Reason:
- Low fraud probability

Action Taken:
- Transaction completed successfully
"""
    }