from model.model_loader import load_model

classifier = load_model()

def analyze_transaction(text):
    labels = ["legitimate transaction", "fraudulent transaction"]

    result = classifier(text, labels)

    return {
        "prediction": result["labels"][0],
        "confidence": result["scores"][0]
    }