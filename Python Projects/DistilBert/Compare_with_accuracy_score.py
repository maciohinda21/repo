from transformers import DistilBertForSequenceClassification, DistilBertTokenizer, pipeline
from datasets import load_dataset
import torch
import numpy as np
from sklearn.metrics import accuracy_score
from tqdm import tqdm

# Load the IMDb test dataset
dataset = load_dataset("imdb")
test_dataset = dataset["test"].shuffle(seed=42).select(range(1000))  # Use a subset for quick evaluation

# Load the original model and tokenizer
original_model_name = "distilbert-base-uncased"
original_model = DistilBertForSequenceClassification.from_pretrained(original_model_name, num_labels=2)
original_tokenizer = DistilBertTokenizer.from_pretrained(original_model_name)

# Load your trained model and tokenizer
fine_tuned_path = "Maciohinda/extra-fine-tuned-distilbert-imdb"
fine_tuned_model = DistilBertForSequenceClassification.from_pretrained(fine_tuned_path)
fine_tuned_tokenizer = DistilBertTokenizer.from_pretrained(fine_tuned_path)

# Define a function to get predictions
def get_predictions(model, tokenizer, texts, device, batch_size=16):
    # Move model to the specified device (GPU)
    model.to(device)
    model.eval()  # Set the model to evaluation mode

    predictions = []
    total_batches = (len(texts) // batch_size) + 1

    # Process texts in batches
    for i in tqdm(range(0, len(texts), batch_size), desc="Predicting", unit="batch"):
        batch_texts = texts[i:i + batch_size]

        # Tokenize the batch and move tensors to the device
        inputs = tokenizer(batch_texts, return_tensors="pt", padding=True, truncation=True)
        inputs = {key: value.to(device) for key, value in inputs.items()}  # Move inputs to GPU

        # Perform inference
        with torch.no_grad():
            outputs = model(**inputs)

        # Get predictions
        logits = outputs.logits
        batch_predictions = torch.argmax(logits, dim=-1).cpu().numpy()  # Move predictions back to CPU for numpy
        predictions.extend(batch_predictions)

    return predictions

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Get predictions from both models
texts = test_dataset["text"]
labels = test_dataset["label"]

# Original model predictions
print("Getting predictions from the original model...")
original_predictions = get_predictions(original_model, original_tokenizer, texts, device)

# Trained model predictions
print("Getting predictions from the fine-tuned model...")
fine_tuned_predictions = get_predictions(fine_tuned_model, fine_tuned_tokenizer, texts, device)

# Calculate accuracy
original_accuracy = accuracy_score(labels, original_predictions)
fine_tuned_accuracy = accuracy_score(labels, fine_tuned_predictions)

# Print results
print(f"Original DistilBERT Accuracy: {original_accuracy * 100:.2f}%")
print(f"Extra-Fine-Tuned DistilBERT Accuracy: {fine_tuned_accuracy * 100:.2f}%")