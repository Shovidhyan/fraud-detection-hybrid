from app.llm import client

def explain_risk(transaction_data):

    prompt = f"""
    Analyze this transaction and explain whether it looks fraudulent.

    Transaction:
    {transaction_data}

    Give:
    1. Risk Level
    2. Why suspicious
    3. Recommended action
    """

    try:

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {str(e)}"