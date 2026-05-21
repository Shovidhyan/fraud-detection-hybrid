from model.model_loader import load_model

classifier = load_model()

def detect_fraud(transaction_text):

    labels = [
        "fraud",
        "safe",
        "suspicious"
    ]

    result = classifier(
        transaction_text,
        candidate_labels=labels
    )

    return {
        "label": result["labels"][0],
        "score": result["scores"][0]
    }