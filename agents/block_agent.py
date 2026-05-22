def block_transaction(state):

    return {
        "final_action": """
Transaction BLOCKED

Reason:
- High fraud probability detected
- Security threat identified

Action Taken:
- Transaction cancelled
- Security alert generated
- Account temporarily protected
"""
    }