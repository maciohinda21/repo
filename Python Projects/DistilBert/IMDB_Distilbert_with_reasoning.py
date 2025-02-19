from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch

# Load the model and tokenizer
save_path = "Maciohinda/extra-fine-tuned-distilbert-imdb"  # Corrected path
model = DistilBertForSequenceClassification.from_pretrained(save_path)
tokenizer = DistilBertTokenizer.from_pretrained(save_path)

def interpret_prediction(logits):
    # Convert logits to probabilities
    probs = torch.softmax(logits, dim=-1)
    positive_prob = probs[0][1].item()
    negative_prob = probs[0][0].item()
    
    # Determine the prediction
    prediction = "positive" if positive_prob > negative_prob else "negative"
    
    # Generate reasoning
    reasoning = f"The model predicts that the sentiment is {prediction}.\n"
    reasoning += f"Probability of being positive: {positive_prob:.2f}\n"
    reasoning += f"Probability of being negative: {negative_prob:.2f}\n"
    
    return reasoning

# Use the model for inference
text_to_test = "This marvel movie was not what I expected."  # Replace with your text to test the model
inputs = tokenizer(text_to_test, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits

# Get the reasoning and prediction
reasoning = interpret_prediction(logits)
print(reasoning)
