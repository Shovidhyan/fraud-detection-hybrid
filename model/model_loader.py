from transformers import pipeline

def load_model():
    return pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )